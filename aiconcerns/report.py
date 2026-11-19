"""report.md + clusters.csv from the DB."""
from __future__ import annotations

import json
import math
import sqlite3

import pandas as pd

from .config import OUT

TOPIC_PL = {"ai_safety_xrisk": "AI safety / x-risk"}


def _md_cell(s: str, n: int = 160) -> str:
    s = (s or "").replace("|", "\\|").replace("\n", " ")
    return s if len(s) <= n else s[: n - 1] + "…"


def run(con: sqlite3.Connection, cfg: dict) -> None:
    items = pd.read_sql("SELECT * FROM items", con)
    corpus = items[(items.drop_reason.isna()) & (items.about_ai == 1)]
    clustered = corpus[corpus.cluster >= 0].astype({"cluster": int})
    meta = pd.read_sql("SELECT * FROM clusters", con).set_index("cluster")
    N = len(corpus)

    recs = []
    for c, g in clustered.groupby("cluster"):
        by_src = g.source.value_counts()
        top_parent_share = g.parent_id.value_counts(normalize=True).iloc[0]
        m = meta.loc[c] if c in meta.index else None
        recs.append({
            "cluster": int(c),
            "label_en": m["label_en"] if m is not None else f"(unlabelled {c})",
            "label_pl": m["label_pl"] if m is not None else "",
            "type": m["type"] if m is not None else "",
            "topic": m["topic"] if m is not None else "",
            "coherence": m["coherence"] if m is not None else None,
            "summary": m["summary"] if m is not None else "",
            "size": len(g),
            "pct_corpus": 100 * len(g) / N,
            # engagement-weighted: each text counts 1 + log(1 + likes) so one viral comment can't dominate
            "eng_weighted": float(sum(1 + math.log1p(e or 0) for e in g.engagement)),
            "total_likes": int(g.engagement.fillna(0).sum()),
            "top_source": by_src.index[0],
            "by_source": "; ".join(f"{s}={n}" for s, n in by_src.items()),
            "n_parents": g.parent_id.nunique(),
            "top_parent_share": float(top_parent_share),
            "quotes": json.loads(m["quotes_json"]) if m is not None and m["quotes_json"] else [],
            "questions": json.loads(m["questions_json"]) if m is not None and m["questions_json"] else [],
        })
    if not recs:
        print("[report] no clusters yet — run collect, clean, classify, cluster first")
        return
    df = pd.DataFrame(recs).sort_values("size", ascending=False)
    df["rank_size"] = range(1, len(df) + 1)
    df["rank_eng"] = df.eng_weighted.rank(ascending=False, method="min").astype(int)

    csv = df.drop(columns=["quotes", "questions"]).copy()
    csv["example_quote"] = [q[0]["text"] if q else "" for q in df.quotes]
    csv["questions_pl"] = [" | ".join(x["pl"] for x in qs) for qs in df.questions]
    csv.to_csv(OUT / "clusters.csv", index=False)

    L = ["# What Polish internet users say and ask about AI", ""]
    L.append(f"Corpus: **{N}** AI-relevant Polish texts, of which **{len(clustered)}** "
             f"({100*len(clustered)/max(N,1):.0f}%) fall into **{len(df)}** clusters; "
             f"the rest is HDBSCAN noise (too idiosyncratic to group).")
    L.append("")
    L.append("## 1. Ranked themes")
    L.append("")
    L.append("Ranked by size. **Eng. rank** = rank when each text counts `1 + ln(1 + likes)`. "
             "**1 video** = share of the cluster coming from its single biggest source video/thread "
             "(high → one piece of content may be driving the theme). **Coh.** = model-judged coherence 1–5.")
    L.append("")
    L.append("| # | Theme (EN / PL) | Type | Topic | Size | % corpus | Eng. rank | Top source | 1 video | Coh. | Example quote |")
    L.append("|---|---|---|---|---|---|---|---|---|---|---|")
    for _, r in df.iterrows():
        q = r.quotes[0]["text"] if r.quotes else ""
        L.append(f"| {r.rank_size} | **{_md_cell(r.label_en, 60)}**<br>{_md_cell(r.label_pl, 60)} | {r.type} | "
                 f"{r.topic} | {r['size']} | {r.pct_corpus:.1f}% | {r.rank_eng} | {r.by_source} | "
                 f"{r.top_parent_share:.0%} | {r.coherence if r.coherence is not None else ''} | "
                 f"„{_md_cell(q)}” |")
    L.append("")

    L.append("## 2. Questions to answer, by theme")
    L.append("")
    L.append(f"Top {cfg['report']['top_n_questions']} themes by size. Questions are inferred "
             "(\"what would this person need to hear?\"), not quoted. ⚠️ marks AI-safety / x-risk.")
    L.append("")
    for _, r in df.head(cfg["report"]["top_n_questions"]).iterrows():
        L.append(f"### {r.rank_size}. {r.label_en} — *{r.label_pl}*")
        L.append(f"{r.summary}  ")
        L.append(f"`{r.type}` · `{r.topic}` · {r['size']} texts")
        L.append("")
        for qn in r.questions:
            flag = "⚠️ " if qn["topic"] == "ai_safety_xrisk" else ""
            L.append(f"- {flag}**{qn['pl']}** — {qn['en']} `{qn['topic']}`")
        if r.quotes:
            L.append("")
            L.append("<details><summary>Representative quotes</summary>\n")
            for qt in r.quotes[: cfg["report"]["quotes_per_cluster"]]:
                L.append(f"> {_md_cell(qt['text'], 500)} ([link]({qt['url']}))\n")
            L.append("</details>")
        L.append("")

    L.append("## 3. Search questions (Google Trends)")
    L.append("")
    L.append("_Not collected yet — the Trends collector is not built in this run._")
    L.append("")

    # caveats
    L.append("## 4. Caveats")
    L.append("")
    src = items.groupby("source").agg(
        collected=("id", "size"),
        kept_after_cleaning=("drop_reason", lambda s: int(s.isna().sum())),
    )
    src["about_ai"] = corpus.groupby("source").size()
    src["parents"] = items.groupby("source").parent_id.nunique()
    src["from"] = corpus.groupby("source").created_at.min().str[:10]
    src["to"] = corpus.groupby("source").created_at.max().str[:10]
    L.append(src.fillna(0).to_markdown())
    L.append("")
    drops = items.drop_reason.fillna("kept").value_counts()
    L.append("Cleaning outcomes: " + ", ".join(f"{k} {v}" for k, v in drops.items()) + ".")
    L.append("")
    skipped = pd.read_sql("SELECT stage, note FROM runs WHERE note LIKE 'SKIPPED%' ORDER BY at DESC", con)
    skipped = skipped.drop_duplicates("stage")
    planned = ["reddit", "wykop", "x (xAI)", "google trends", "news-site comments"]
    L += [
        "- **Sampling bias.** YouTube comments are drawn from videos YouTube's search ranks for our "
        "keywords, so they over-represent popular/sensational AI content and the people who comment "
        "on it. Comment order is YouTube's 'relevance', which favours liked comments. This is not a "
        "representative sample of Polish internet users, let alone of Poles.",
        "- **Per-video concentration.** Commenters react to the specific video; check the '1 video' "
        "column before reading a theme as a general public concern.",
        "- **Pipeline judgments.** AI-relevance (Claude Haiku), clustering (HDBSCAN; noise is excluded) "
        "and labels/questions (Claude Opus) are model outputs; spot-check quotes against links.",
        "- **Anonymisation.** No author names are stored; @handles and URLs are stripped from text. "
        "Quotes are verbatim otherwise and links point to the public comment.",
        "- **Sources skipped this run:** "
        + (", ".join(f"{r.stage} ({r.note})" for r in skipped.itertuples()) or "none")
        + f". Not yet built: {', '.join(planned)}. Facebook and TikTok are out of scope.",
    ]
    (OUT / "report.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"[report] wrote {OUT/'report.md'} and {OUT/'clusters.csv'} ({len(df)} clusters)")
