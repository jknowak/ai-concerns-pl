"""Anonymisation, language filter, spam filter, exact + near-duplicate removal."""
from __future__ import annotations

import hashlib
import re
import sqlite3
import unicodedata

from datasketch import MinHash, MinHashLSH
from lingua import Language, LanguageDetectorBuilder

from .db import log

_HANDLE = re.compile(r"(?<![\w.])@[\w.\-]{2,}|(?<!\w)/?u/[\w\-]{3,}", re.UNICODE)
_URL = re.compile(r"https?://\S+|www\.\S+")
_WS = re.compile(r"\s+")


def anonymise(text: str) -> str:
    """Drop @handles / u/names and URLs; we never store who said what."""
    text = _URL.sub("[link]", text)
    text = _HANDLE.sub("", text)
    return _WS.sub(" ", text).strip(" ,:")


# Kept deliberately narrow: on YouTube, real spam is mostly pre-filtered, and all-caps rants,
# emoji runs and talk about pay/jobs are genuine lay voices (an aggressive filter dropped 55/55 such).
_CONTACT = re.compile(r"telegram|whats\s?app|\bwa\.me\b|\+\s?48[\s-]?\d{3}|napisz (do mnie|na priv)|"
                      r"sub4sub|check my channel|onlyfans", re.I)
_MONEY = re.compile(r"zarob|inwest|crypto|krypto|bitcoin|forex|trader|dochód|profit|\$\d", re.I)


def spam_reason(text: str) -> str | None:
    if _CONTACT.search(text) and _MONEY.search(text):
        return "spam_promo"
    if text.count("[link]") >= 3 and len(text.split()) < 40:
        return "spam_links"
    words = text.lower().split()
    if len(words) >= 15 and len(set(words)) / len(words) < 0.25:
        return "spam_repeat"
    return None


def _norm(text: str) -> str:
    t = unicodedata.normalize("NFKC", text.lower())
    t = re.sub(r"[^\w\s]", " ", t)
    return _WS.sub(" ", t).strip()


def _detector():
    langs = [Language.POLISH, Language.ENGLISH, Language.GERMAN, Language.RUSSIAN,
             Language.UKRAINIAN, Language.CZECH, Language.SLOVAK, Language.FRENCH,
             Language.SPANISH, Language.ITALIAN]
    return LanguageDetectorBuilder.from_languages(*langs).build()


def run(con: sqlite3.Connection, cfg: dict) -> None:
    c = cfg["cleaning"]
    rows = con.execute("SELECT id, text, engagement FROM items").fetchall()  # whole corpus, so new sources dedupe against old
    det = _detector()
    reasons: dict[str, str | None] = {}
    langs: dict[str, str] = {}
    kept = []
    for r in rows:
        t = r["text"]
        if len(t.split()) < c["min_words"]:
            reasons[r["id"]] = "short"
            continue
        sr = spam_reason(t)
        if sr:
            reasons[r["id"]] = sr
            continue
        conf = det.compute_language_confidence(t, Language.POLISH)
        if conf < c["min_polish_confidence"]:
            top = det.detect_language_of(t)
            langs[r["id"]] = top.iso_code_639_1.name.lower() if top else "und"
            reasons[r["id"]] = "not_polish"
            continue
        langs[r["id"]] = "pl"
        kept.append(r)

    # exact dupes: keep the highest-engagement copy
    kept.sort(key=lambda r: -(r["engagement"] or 0))
    seen: set[str] = set()
    survivors = []
    for r in kept:
        h = hashlib.sha1(_norm(r["text"]).encode()).hexdigest()
        if h in seen:
            reasons[r["id"]] = "dup_exact"
            continue
        seen.add(h)
        survivors.append(r)

    # near dupes via MinHash LSH on word 3-shingles (same order: higher engagement wins)
    lsh = MinHashLSH(threshold=c["near_dup_threshold"], num_perm=128)
    for r in survivors:
        w = _norm(r["text"]).split()
        sh = {" ".join(w[i:i + 3]) for i in range(max(1, len(w) - 2))}
        m = MinHash(num_perm=128)
        for s in sh:
            m.update(s.encode())
        if lsh.query(m):
            reasons[r["id"]] = "dup_near"
            continue
        lsh.insert(r["id"], m)
        reasons[r["id"]] = None

    con.executemany("UPDATE items SET drop_reason = ?, lang = ? WHERE id = ?",
                    [(reasons.get(r["id"]), langs.get(r["id"]), r["id"]) for r in rows])
    con.commit()
    counts: dict[str, int] = {}
    for v in reasons.values():
        counts[v or "kept"] = counts.get(v or "kept", 0) + 1
    log(con, "clean", " ".join(f"{k}={v}" for k, v in sorted(counts.items(), key=lambda x: -x[1])))
