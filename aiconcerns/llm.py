"""Claude calls: cheap AI-relevance filter (Haiku) and cluster labelling (Opus).

Every stage estimates its cost first and refuses to run above `llm.budget_usd`
unless the caller passes --yes. Actual spend is logged from response.usage.
"""
from __future__ import annotations

import json
import sqlite3
from concurrent.futures import ThreadPoolExecutor, as_completed

import anthropic

from .db import log

PRICES = {  # USD per 1M tokens (input, output)
    "claude-haiku-5-5": (0.10, 0.50),
    "claude-opus-5-5": (4.00, 20.00),
    "claude-sonnet-5-5": (2.00, 10.00),
}
CHARS_PER_TOKEN = 3.0  # conservative for Polish


class BudgetExceeded(SystemExit):
    pass


class Spend:
    def __init__(self, model: str):
        self.model, self.inp, self.out = model, 0, 0

    def add(self, usage) -> None:
        self.inp += usage.input_tokens + (usage.cache_read_input_tokens or 0) + (usage.cache_creation_input_tokens or 0)
        self.out += usage.output_tokens

    @property
    def usd(self) -> float:
        pi, po = PRICES[self.model]
        return (self.inp * pi + self.out * po) / 1e6


def guard(stage: str, model: str, in_tokens: float, out_tokens: float, cfg: dict, yes: bool) -> float:
    pi, po = PRICES[model]
    est = (in_tokens * pi + out_tokens * po) / 1e6
    print(f"[{stage}] estimated cost ≈ ${est:.2f} ({model}, ~{in_tokens/1e3:.0f}k in / ~{out_tokens/1e3:.0f}k out)")
    if est > cfg["llm"]["budget_usd"] and not yes:
        raise BudgetExceeded(f"[{stage}] estimate ${est:.2f} > budget ${cfg['llm']['budget_usd']}; "
                             "rerun with --yes to approve")
    return est


def _text_of(resp) -> str:
    if resp.stop_reason == "refusal":
        raise RuntimeError(f"refusal: {getattr(resp, 'stop_details', None)}")
    if resp.stop_reason == "max_tokens":
        raise RuntimeError("hit max_tokens")
    return next(b.text for b in resp.content if b.type == "text")


# --------------------------------------------------------------------------- classify

CLASSIFY_SYSTEM = """Jesteś filtrem korpusu dla badania opinii publicznej o sztucznej inteligencji.
Dostajesz ponumerowane komentarze internautów (z tytułem materiału, pod którym padły, jako kontekst).
Dla każdego zdecyduj: about_ai = true, jeśli komentarz SAM wyraża opinię, obawę, pytanie, argument,
żart lub doświadczenie dotyczące AI / sztucznej inteligencji / chatbotów / automatyzacji przez AI
/ ryzyka i bezpieczeństwa AI / firm i ludzi z branży AI w kontekście AI.
about_ai = false dla: pochwał lub krytyki samego filmu/autora, pozdrowień, off-topicu, polityki
bez związku z AI, sporów osobistych, komentarzy niezrozumiałych bez kontekstu.
Zwróć wynik dla każdego numeru."""

CLASSIFY_SCHEMA = {
    "type": "object",
    "properties": {"results": {"type": "array", "items": {
        "type": "object",
        "properties": {"i": {"type": "integer"}, "about_ai": {"type": "boolean"}},
        "required": ["i", "about_ai"], "additionalProperties": False}}},
    "required": ["results"], "additionalProperties": False,
}


def classify(con: sqlite3.Connection, cfg: dict, yes: bool) -> None:
    model = cfg["llm"]["classifier_model"]
    rows = con.execute("SELECT id, text, parent_context FROM items "
                       "WHERE drop_reason IS NULL AND about_ai IS NULL").fetchall()
    if not rows:
        log(con, "classify", "nothing to classify")
        return
    bs = cfg["llm"]["classify_batch_size"]
    batches = [rows[i:i + bs] for i in range(0, len(rows), bs)]
    chars = sum(len(r["text"]) + 60 for r in rows) + len(batches) * (len(CLASSIFY_SYSTEM) + 400)
    guard("classify", model, chars / CHARS_PER_TOKEN, len(rows) * 15 + len(batches) * 800, cfg, yes)

    client = anthropic.Anthropic()
    spend = Spend(model)

    def run_batch(batch):
        lines = [f"[{i}] (pod: {(r['parent_context'] or '')[:90]})\n{r['text'][:1200]}"
                 for i, r in enumerate(batch)]
        resp = client.messages.create(
            model=model, max_tokens=8000, system=CLASSIFY_SYSTEM,
            output_config={"effort": "low", "format": {"type": "json_schema", "schema": CLASSIFY_SCHEMA}},
            messages=[{"role": "user", "content": "\n\n".join(lines)}],
        )
        spend.add(resp.usage)
        res = {x["i"]: x["about_ai"] for x in json.loads(_text_of(resp))["results"]}
        return [(int(res[i]), r["id"]) for i, r in enumerate(batch) if i in res]

    done = failed = 0
    with ThreadPoolExecutor(cfg["llm"]["concurrency"]) as ex:
        futs = [ex.submit(run_batch, b) for b in batches]
        for f in as_completed(futs):
            try:
                upd = f.result()
            except Exception as e:  # leave those rows NULL; a rerun retries them
                failed += 1
                print(f"  batch failed: {e}")
                continue
            con.executemany("UPDATE items SET about_ai = ? WHERE id = ?", upd)
            con.commit()
            done += 1
            print(f"  batches {done}/{len(batches)}", end="\r")
    n_ai = con.execute("SELECT COUNT(*) FROM items WHERE about_ai = 1").fetchone()[0]
    log(con, "classify", f"batches_ok={done} failed={failed} about_ai_total={n_ai} "
                         f"actual_cost=${spend.usd:.3f}")


# --------------------------------------------------------------------------- label

TYPES = ["objection", "fear", "misconception", "question", "argument_for", "joke_cynicism"]
TOPICS = ["ai_safety_xrisk", "jobs_economy", "privacy_surveillance", "education", "misinformation_deepfakes",
          "creativity_art", "regulation_politics", "big_tech_power", "capabilities_hype", "everyday_use",
          "health", "other"]

LABEL_SYSTEM = """You analyse what ordinary Polish internet users say about AI, for AI Safety Poland
(a nonprofit that does public communication about AI and AI safety). You get one cluster of
semantically similar Polish comments (a sample, numbered) plus the title of the content each was
posted under. Describe the cluster faithfully — the stance of the commenters, not your own view.
Do not sanitise cynicism or hostility; do not invent concerns not present in the sample.

- label_pl / label_en: short (≤8 words) theme name.
- summary: one English sentence stating the dominant stance.
- type: the dominant kind of utterance.
- topic: main subject area; ai_safety_xrisk = loss of control, misalignment, extinction/catastrophe,
  AI "taking over", superintelligence.
- coherence: 1–5, how much the sample is really one theme (1 = grab-bag).
- quote_ids: 3–5 numbers of comments that best represent the cluster (prefer clear, typical ones).
- questions: 1–3 questions that, if answered well and honestly, would address this concern —
  "what would this person need to hear?". Write them in Polish as a member of the public would ask
  (FAQ style), each with an English gloss and its own topic."""

LABEL_SCHEMA = {
    "type": "object",
    "properties": {
        "label_pl": {"type": "string"}, "label_en": {"type": "string"},
        "summary": {"type": "string"},
        "type": {"type": "string", "enum": TYPES},
        "topic": {"type": "string", "enum": TOPICS},
        "coherence": {"type": "integer"},
        "quote_ids": {"type": "array", "items": {"type": "integer"}},
        "questions": {"type": "array", "items": {
            "type": "object",
            "properties": {"pl": {"type": "string"}, "en": {"type": "string"},
                           "topic": {"type": "string", "enum": TOPICS}},
            "required": ["pl", "en", "topic"], "additionalProperties": False}},
    },
    "required": ["label_pl", "label_en", "summary", "type", "topic", "coherence", "quote_ids", "questions"],
    "additionalProperties": False,
}


def label(con: sqlite3.Connection, cfg: dict, samples: dict[int, list[sqlite3.Row]], yes: bool) -> None:
    """samples: cluster id -> representative rows (already chosen by cluster.py)."""
    model = cfg["llm"]["labeler_model"]
    todo = {c: rows for c, rows in samples.items()
            if not con.execute("SELECT 1 FROM clusters WHERE cluster = ? AND label_en IS NOT NULL", (c,)).fetchone()}
    if not todo:
        log(con, "label", "all clusters already labelled")
        return
    chars = sum(sum(len(r["text"][:600]) + 100 for r in rows) + len(LABEL_SYSTEM) for rows in todo.values())
    guard("label", model, chars / CHARS_PER_TOKEN, len(todo) * 3000, cfg, yes)

    client = anthropic.Anthropic()
    spend = Spend(model)

    def run(c, rows):
        body = "\n\n".join(f"[{i}] (pod: {(r['parent_context'] or '')[:90]})\n{r['text'][:600]}"
                           for i, r in enumerate(rows))
        resp = client.beta.messages.create(
            model=model, max_tokens=16000, system=LABEL_SYSTEM,
            betas=["server-side-fallback-2026-07-01"], fallbacks="default",
            output_config={"effort": "medium", "format": {"type": "json_schema", "schema": LABEL_SCHEMA}},
            messages=[{"role": "user", "content": f"Cluster sample ({len(rows)} comments):\n\n{body}"}],
        )
        spend.add(resp.usage)
        out = json.loads(_text_of(resp))
        quotes = [{"text": rows[i]["text"], "url": rows[i]["url"]}
                  for i in out.pop("quote_ids") if 0 <= i < len(rows)]
        return c, out, quotes

    with ThreadPoolExecutor(min(4, cfg["llm"]["concurrency"])) as ex:
        futs = [ex.submit(run, c, rows) for c, rows in todo.items()]
        for f in as_completed(futs):
            try:
                c, out, quotes = f.result()
            except Exception as e:
                print(f"  label failed: {e}")
                continue
            con.execute(
                """INSERT OR REPLACE INTO clusters VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (c, out["label_pl"], out["label_en"], out["summary"], out["type"], out["topic"],
                 out["coherence"], json.dumps(quotes, ensure_ascii=False),
                 json.dumps(out["questions"], ensure_ascii=False)))
            con.commit()
            print(f"  cluster {c}: {out['label_en']}")
    log(con, "label", f"labelled={len(todo)} actual_cost=${spend.usd:.3f}")
