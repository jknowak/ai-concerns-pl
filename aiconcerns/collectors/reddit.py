"""Reddit (OAuth, application-only): search Polish subreddits + site-wide for our keywords,
store each post (title + body) and its comment tree.

Needs REDDIT_CLIENT_ID / REDDIT_CLIENT_SECRET from an approved Reddit app. Self-service app creation
(reddit.com/prefs/apps) is closed and Reddit's Responsible Builder Policy may not allow this use at all;
see docs/reddit-access.md before running. Without credentials the collector is skipped.
Rate limit is ~100 requests/min for OAuth clients; we stay well under it.
Comments hidden behind "load more" stubs are not expanded (that would cost one call per stub).
"""
from __future__ import annotations

import datetime as dt
import sqlite3
import time

import requests

from ..cache import cached
from ..config import secret
from ..db import log, upsert_items
from ..textclean import anonymise

AUTH = "https://www.reddit.com/api/v1/access_token"
API = "https://oauth.reddit.com"
# Reddit asks for a descriptive User-Agent; override with REDDIT_USER_AGENT if you want your own.
DEFAULT_UA = "linux:ai-concerns-pl:0.1 (research; Polish public opinion on AI)"
GONE = {"[deleted]", "[removed]", ""}


class Session:
    def __init__(self, cid: str, csecret: str):
        self.ua = secret("REDDIT_USER_AGENT") or DEFAULT_UA
        self.cid, self.csecret = cid, csecret
        self.token, self.expires = None, 0.0
        self.calls = 0
        self.cached_calls = 0

    def _auth(self) -> None:
        r = requests.post(AUTH, auth=(self.cid, self.csecret), data={"grant_type": "client_credentials"},
                          headers={"User-Agent": self.ua}, timeout=30)
        if r.status_code != 200:
            raise RuntimeError(f"Reddit auth {r.status_code}: {r.text[:300]}")
        d = r.json()
        self.token, self.expires = d["access_token"], time.time() + d.get("expires_in", 3600) - 60

    def get(self, path: str, params: dict) -> dict | list:
        def fetch():
            for attempt in range(5):
                if not self.token or time.time() > self.expires:
                    self._auth()
                r = requests.get(API + path, params={**params, "raw_json": 1}, timeout=30,
                                 headers={"User-Agent": self.ua, "Authorization": f"bearer {self.token}"})
                self.calls += 1
                time.sleep(0.7)  # ≈85 req/min, under the 100/min limit
                if r.status_code == 200:
                    return r.json()
                if r.status_code == 401:
                    self.token = None
                    continue
                if r.status_code in (404, 403):  # private / banned / quarantined sub or post
                    return {"_unavailable": r.status_code}
                if r.status_code in (429, 500, 502, 503):
                    time.sleep(int(r.headers.get("retry-after") or 2 ** attempt))
                    continue
                raise RuntimeError(f"Reddit {path} {r.status_code}: {r.text[:300]}")
            raise RuntimeError(f"Reddit {path}: retries exhausted")

        data, was_cached = cached("reddit", path, params, fetch)
        if was_cached:
            self.cached_calls += 1
        return data


def _ts(utc: float) -> str:
    return dt.datetime.fromtimestamp(utc, dt.timezone.utc).isoformat(timespec="seconds")


def _in_range(utc: float, cfg: dict) -> bool:
    day = _ts(utc)[:10]
    return cfg["date_range"]["start"] <= day <= cfg["date_range"]["end"]


def _search(s: Session, cfg: dict) -> list[dict]:
    """Post metadata from every (scope, keyword) search, round-robin merged and deduped."""
    rd = cfg["sources"]["reddit"]
    scopes = [f"/r/{sub}/search" for sub in rd["subreddits"]] + (["/search"] if rd["search_all"] else [])
    per_query: list[list[dict]] = []
    for path in scopes:
        for kw in cfg["keywords"]:
            params = {"q": kw, "sort": rd["sort"], "t": "all", "limit": rd["max_posts_per_query"],
                      "type": "link"}
            if path != "/search":
                params["restrict_sr"] = 1
            d = s.get(path, params)
            posts = [c["data"] for c in (d.get("data", {}).get("children", []) if isinstance(d, dict) else [])
                     if c.get("kind") == "t3"]
            per_query.append([p for p in posts
                              if _in_range(p["created_utc"], cfg)
                              and not p.get("over_18")
                              and p.get("num_comments", 0) >= rd["min_comments"]])
    out, seen = [], set()
    while any(per_query):
        for posts in per_query:
            while posts:
                p = posts.pop(0)
                if p["id"] not in seen:
                    seen.add(p["id"])
                    out.append(p)
                    break
    return out


def _row(d: dict, post: dict, ctx: str, kind: str, text: str) -> dict:
    return {
        "id": f"reddit:{d['name']}",          # t3_xxx for posts, t1_xxx for comments
        "source": "reddit",
        "url": "https://www.reddit.com" + d["permalink"],
        "parent_context": ctx,
        "parent_id": f"reddit:{post['name']}",
        "kind": kind,
        "text": anonymise(text),
        "created_at": _ts(d["created_utc"]),
        "engagement": max(0, int(d.get("score") or 0)),  # downvoted → 0, keeps log1p weighting valid
    }


def _walk(children: list, post: dict, ctx: str, cfg: dict, out: list, limit: int) -> None:
    for c in children:
        if len(out) >= limit:
            return
        if c.get("kind") != "t1":  # "more" stubs
            continue
        d = c["data"]
        if d.get("body", "") not in GONE and _in_range(d["created_utc"], cfg) and not d.get("stickied"):
            kind = "comment" if d.get("parent_id", "").startswith("t3_") else "reply"
            out.append(_row(d, post, ctx, kind, d["body"]))
        rep = d.get("replies")
        if isinstance(rep, dict):
            _walk(rep["data"]["children"], post, ctx, cfg, out, limit)


def collect(con: sqlite3.Connection, cfg: dict) -> None:
    cid, csecret = secret("REDDIT_CLIENT_ID"), secret("REDDIT_CLIENT_SECRET")
    if not (cid and csecret):
        log(con, "reddit", "SKIPPED: REDDIT_CLIENT_ID / REDDIT_CLIENT_SECRET missing in .env")
        return
    rd = cfg["sources"]["reddit"]
    s = Session(cid, csecret)
    posts = _search(s, cfg)[: rd["max_posts"]]

    total = 0
    for p in posts:
        ctx = f"{p['title']} — r/{p['subreddit']}"
        rows = []
        body = p.get("selftext") or ""
        post_text = p["title"] + ("\n\n" + body if body not in GONE else "")
        rows.append(_row(p, p, ctx, "post", post_text))
        d = s.get(f"/comments/{p['id']}", {"limit": rd["max_comments_per_post"], "sort": "top",
                                           "depth": rd["max_depth"]})
        if isinstance(d, list) and len(d) == 2:
            _walk(d[1]["data"]["children"], p, ctx, cfg, rows, rd["max_comments_per_post"] + 1)
        rows = [r for r in rows if r["text"]]
        total += upsert_items(con, rows)
        print(f"  {p['id']}: {len(rows):5d} items  | {ctx[:80]}")
    log(con, "reddit", f"posts={len(posts)} items={total} api_calls={s.calls} cached_calls={s.cached_calls}")
