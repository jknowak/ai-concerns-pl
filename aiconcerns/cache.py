"""Disk cache of raw API responses so reruns don't re-hit APIs (or quota)."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Callable

from .config import DATA

SECRET_PARAMS = {"key", "api_key", "access_token", "client_secret"}


def _key(namespace: str, url: str, params: dict) -> Path:
    clean = {k: v for k, v in sorted(params.items()) if k not in SECRET_PARAMS}
    h = hashlib.sha256(json.dumps([url, clean], sort_keys=True, default=str).encode()).hexdigest()[:32]
    d = DATA / "cache" / namespace
    d.mkdir(parents=True, exist_ok=True)
    return d / f"{h}.json"


def cached(namespace: str, url: str, params: dict, fetch: Callable[[], dict]) -> tuple[dict, bool]:
    """Return (response, was_cached)."""
    p = _key(namespace, url, params)
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8")), True
    data = fetch()
    p.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    return data, False
