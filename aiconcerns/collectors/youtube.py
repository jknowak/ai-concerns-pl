"""YouTube Data API v3: search Polish AI videos, pull top-level comments + replies.

Quota (10k units/day default): search.list = 100 units/page, everything else 1 unit/page.
"""
from __future__ import annotations

import sqlite3
import time

import requests

from ..cache import cached
from ..config import secret
from ..db import log, upsert_items
from ..textclean import anonymise

API = "https://www.googleapis.com/youtube/v3/"


class Quota:
    def __init__(self):
        self.used = 0
        self.cached_calls = 0


def _get(endpoint: str, params: dict, key: str, quota: Quota, cost: int) -> dict:
    def fetch():
        for attempt in range(5):
            r = requests.get(API + endpoint, params={**params, "key": key}, timeout=30)
            if r.status_code == 200:
                return r.json()
            if r.status_code == 403 and "commentsDisabled" in r.text:
                return {"items": [], "_comments_disabled": True}
            if r.status_code in (429, 500, 503):
                time.sleep(2 ** attempt)
                continue
            raise RuntimeError(f"YouTube {endpoint} {r.status_code}: {r.text[:300]}")
        raise RuntimeError(f"YouTube {endpoint}: retries exhausted")

    data, was_cached = cached("youtube", endpoint, params, fetch)
    if was_cached:
        quota.cached_calls += 1
    else:
        quota.used += cost
        time.sleep(0.1)  # be gentle
    return data


def _search_videos(cfg: dict, key: str, quota: Quota) -> list[str]:
    yt = cfg["sources"]["youtube"]
    per_kw: list[list[str]] = []
    for kw in cfg["keywords"]:
        ids, token = [], None
        for _ in range(yt["max_search_pages_per_keyword"]):
            params = {
                "part": "id", "q": kw, "type": "video", "maxResults": 50,
                "order": yt["order"], "regionCode": yt["region_code"],
                "relevanceLanguage": yt["relevance_language"],
                "publishedAfter": f"{cfg['date_range']['start']}T00:00:00Z",
                "publishedBefore": f"{cfg['date_range']['end']}T23:59:59Z",
            }
            if token:
                params["pageToken"] = token
            d = _get("search", params, key, quota, cost=100)
            ids += [it["id"]["videoId"] for it in d.get("items", [])]
            token = d.get("nextPageToken")
            if not token:
                break
        per_kw.append(ids)
    # round-robin across keywords so one query doesn't take all slots
    out, seen, i = [], set(), 0
    while any(per_kw) and i < 10_000:
        for ids in per_kw:
            while ids:
                v = ids.pop(0)
                if v not in seen:
                    seen.add(v)
                    out.append(v)
                    break
        i += 1
    return out


def _video_meta(ids: list[str], key: str, quota: Quota) -> dict[str, dict]:
    meta = {}
    for i in range(0, len(ids), 50):
        d = _get("videos", {"part": "snippet,statistics", "id": ",".join(ids[i:i + 50])}, key, quota, 1)
        for it in d.get("items", []):
            meta[it["id"]] = it
    return meta


def _polish_video(sn: dict) -> bool:
    """Drop videos YouTube itself tags as non-Polish (untagged videos are kept; text-level filter catches the rest)."""
    lang = (sn.get("defaultAudioLanguage") or sn.get("defaultLanguage") or "pl").lower()
    return lang.startswith("pl")


def _row(c: dict, vid: str, ctx: str, kind: str) -> dict:
    s = c["snippet"]
    return {
        "id": f"youtube:{c['id']}",
        "source": "youtube",
        "url": f"https://www.youtube.com/watch?v={vid}&lc={c['id']}",
        "parent_context": ctx,
        "parent_id": f"youtube:{vid}",
        "kind": kind,
        "text": anonymise(s.get("textOriginal") or s.get("textDisplay") or ""),
        "created_at": s.get("publishedAt"),
        "engagement": int(s.get("likeCount") or 0),
    }


def collect(con: sqlite3.Connection, cfg: dict) -> None:
    key = secret("YOUTUBE_API_KEY")
    if not key:
        log(con, "youtube", "SKIPPED: YOUTUBE_API_KEY missing in .env")
        return
    yt = cfg["sources"]["youtube"]
    quota = Quota()
    candidates = _search_videos(cfg, key, quota)
    meta = _video_meta(candidates, key, quota)
    videos = [v for v in candidates
              if v in meta and int(meta[v].get("statistics", {}).get("commentCount") or 0) > 0
              and _polish_video(meta[v]["snippet"])]
    videos = videos[: yt["max_videos"]]

    total = 0
    for vid in videos:
        sn = meta[vid]["snippet"]
        ctx = f"{sn['title']} — {sn['channelTitle']}"
        rows, token, threads = [], None, 0
        while threads < yt["max_comment_threads_per_video"]:
            params = {"part": "snippet,replies", "videoId": vid, "maxResults": 100,
                      "order": "relevance", "textFormat": "plainText"}
            if token:
                params["pageToken"] = token
            d = _get("commentThreads", params, key, quota, 1)
            for th in d.get("items", []):
                threads += 1
                top = th["snippet"]["topLevelComment"]
                rows.append(_row(top, vid, ctx, "comment"))
                n_replies = th["snippet"].get("totalReplyCount", 0)
                inline = th.get("replies", {}).get("comments", [])
                if n_replies > len(inline) and yt["max_replies_per_thread"] > len(inline):
                    inline, rtok = [], None
                    while len(inline) < yt["max_replies_per_thread"]:
                        rp = {"part": "snippet", "parentId": top["id"], "maxResults": 100,
                              "textFormat": "plainText"}
                        if rtok:
                            rp["pageToken"] = rtok
                        rd = _get("comments", rp, key, quota, 1)
                        inline += rd.get("items", [])
                        rtok = rd.get("nextPageToken")
                        if not rtok:
                            break
                for rc in inline[: yt["max_replies_per_thread"]]:
                    rows.append(_row(rc, vid, ctx, "reply"))
            token = d.get("nextPageToken")
            if not token:
                break
        rows = [r for r in rows if r["text"]]
        total += upsert_items(con, rows)
        print(f"  {vid}: {len(rows):5d} comments  | {ctx[:80]}")
    log(con, "youtube", f"videos={len(videos)} items={total} quota_units_used={quota.used} "
                        f"cached_calls={quota.cached_calls}")
