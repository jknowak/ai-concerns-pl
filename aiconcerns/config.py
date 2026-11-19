from __future__ import annotations

import datetime as dt
import os
from pathlib import Path

import yaml
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "out"


def load(path: str | Path = ROOT / "config.yaml") -> dict:
    load_dotenv(ROOT / ".env")
    with open(path, encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    dr = cfg.setdefault("date_range", {})
    dr["start"] = str(dr.get("start") or "2020-01-01")
    dr["end"] = str(dr.get("end") or dt.date.today().isoformat())
    DATA.mkdir(exist_ok=True)
    OUT.mkdir(exist_ok=True)
    return cfg


def secret(name: str) -> str | None:
    v = os.environ.get(name, "").strip()
    return v or None
