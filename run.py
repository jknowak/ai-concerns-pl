#!/usr/bin/env python
"""Polish lay-public AI concerns miner.

usage: python run.py [collect|clean|classify|cluster|report|all] [--yes]
  collect   pull raw texts from enabled sources (cached; reruns are free)
  clean     anonymise-checked texts → drop short / non-Polish / spam / duplicates
  classify  Claude Haiku: keep only texts actually about AI
  cluster   embed → UMAP → HDBSCAN, then Claude Opus labels each cluster + infers questions
  report    out/report.md + out/clusters.csv
--yes approves a stage whose estimated Claude cost exceeds llm.budget_usd.
"""
import argparse
import warnings

warnings.filterwarnings("ignore")

from aiconcerns import cluster, config, db, llm, pdf, report, textclean
from aiconcerns.collectors import reddit, youtube

# reddit is drafted but disabled in config.yaml (no API access; see docs/reddit-access.md)
COLLECTORS = {"youtube": youtube.collect, "reddit": reddit.collect}  # build order: wykop, x, trends, news


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("stage", nargs="?", default="all",
                    choices=["collect", "clean", "classify", "cluster", "report", "pdf", "all"])
    ap.add_argument("--yes", action="store_true")
    a = ap.parse_args()
    cfg = config.load()
    con = db.connect()
    all_ = a.stage == "all"
    if all_ or a.stage == "collect":
        for name, fn in COLLECTORS.items():
            if cfg["sources"].get(name, {}).get("enabled"):
                fn(con, cfg)
    if all_ or a.stage == "clean":
        textclean.run(con, cfg)
    if all_ or a.stage == "classify":
        llm.classify(con, cfg, a.yes)
    if all_ or a.stage == "cluster":
        samples = cluster.run(con, cfg)
        llm.label(con, cfg, samples, a.yes)
    if all_ or a.stage == "report":
        report.run(con, cfg)
    if all_ or a.stage in ("report", "pdf"):
        pdf.run(cfg)


if __name__ == "__main__":
    main()
