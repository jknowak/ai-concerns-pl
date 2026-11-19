"""Unified SQLite store. One row per collected text, whatever the source."""
from __future__ import annotations

import datetime as dt
import sqlite3
from typing import Iterable

from .config import DATA

DB_PATH = DATA / "corpus.sqlite"

SCHEMA = """
CREATE TABLE IF NOT EXISTS items (
    id             TEXT PRIMARY KEY,   -- '<source>:<native id>'
    source         TEXT NOT NULL,
    url            TEXT,
    parent_context TEXT,               -- video / post title (+ channel)
    parent_id      TEXT,               -- video / post id, for concentration checks
    kind           TEXT,               -- comment | reply | post | ...
    text           TEXT NOT NULL,      -- handles/usernames already stripped
    lang           TEXT,
    created_at     TEXT,
    engagement     INTEGER DEFAULT 0,  -- likes / upvotes
    collected_at   TEXT NOT NULL,
    drop_reason    TEXT,               -- NULL = kept by cleaning
    about_ai       INTEGER,            -- NULL = not yet classified
    cluster        INTEGER             -- NULL = not clustered, -1 = noise
);
CREATE INDEX IF NOT EXISTS items_source ON items(source);
CREATE TABLE IF NOT EXISTS clusters (
    cluster      INTEGER PRIMARY KEY,
    label_pl     TEXT, label_en TEXT, summary TEXT, type TEXT, topic TEXT, coherence INTEGER,
    quotes_json  TEXT, questions_json TEXT
);
CREATE TABLE IF NOT EXISTS runs (
    at TEXT, stage TEXT, note TEXT
);
"""


def connect() -> sqlite3.Connection:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    con.executescript(SCHEMA)
    return con


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def upsert_items(con: sqlite3.Connection, rows: Iterable[dict]) -> int:
    """Insert new items; existing ids keep their analysis columns but refresh engagement."""
    n = 0
    for r in rows:
        con.execute(
            """INSERT INTO items (id, source, url, parent_context, parent_id, kind, text, lang,
                                  created_at, engagement, collected_at)
               VALUES (:id, :source, :url, :parent_context, :parent_id, :kind, :text, NULL,
                       :created_at, :engagement, :collected_at)
               ON CONFLICT(id) DO UPDATE SET engagement = excluded.engagement""",
            {**r, "collected_at": now()},
        )
        n += 1
    con.commit()
    return n


def log(con: sqlite3.Connection, stage: str, note: str) -> None:
    print(f"[{stage}] {note}")
    con.execute("INSERT INTO runs VALUES (?, ?, ?)", (now(), stage, note))
    con.commit()
