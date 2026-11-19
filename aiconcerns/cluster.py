"""Embed AI-relevant texts → UMAP → HDBSCAN, sweeping min_cluster_size toward the target count."""
from __future__ import annotations

import hashlib
import random
import sqlite3

import numpy as np

from .config import DATA
from .db import log


def _embeddings(rows: list[sqlite3.Row], cfg: dict) -> np.ndarray:
    name = cfg["embedding"]["model"]
    path = DATA / f"emb_{hashlib.sha1(name.encode()).hexdigest()[:10]}.npz"
    store: dict[str, np.ndarray] = {}
    if path.exists():
        z = np.load(path, allow_pickle=False)
        store = dict(zip(z["ids"].tolist(), z["vecs"]))
    # key by text hash so a re-anonymised text gets re-embedded
    keys = [hashlib.sha1(r["text"].encode()).hexdigest() for r in rows]
    missing = [(k, r["text"]) for k, r in zip(keys, rows) if k not in store]
    if missing:
        from sentence_transformers import SentenceTransformer
        model = SentenceTransformer(name, device="cpu")
        vecs = model.encode([t for _, t in missing], batch_size=cfg["embedding"]["batch_size"],
                            normalize_embeddings=True, show_progress_bar=True)
        store.update({k: v for (k, _), v in zip(missing, vecs)})
        np.savez(path, ids=np.array(list(store)), vecs=np.stack(list(store.values())))
    return np.stack([store[k] for k in keys])


def run(con: sqlite3.Connection, cfg: dict) -> dict[int, list[sqlite3.Row]]:
    from sklearn.cluster import HDBSCAN
    import umap

    cc = cfg["clustering"]
    rows = con.execute("SELECT * FROM items WHERE drop_reason IS NULL AND about_ai = 1 ORDER BY id").fetchall()
    if len(rows) < 50:
        raise SystemExit(f"[cluster] only {len(rows)} AI-relevant texts — collect more before clustering")
    X = _embeddings(rows, cfg)
    red = umap.UMAP(n_neighbors=min(cc["umap_n_neighbors"], len(rows) - 1), n_components=cc["umap_n_components"],
                    metric="cosine", min_dist=0.0, random_state=cc["random_state"]).fit_transform(X)

    lo, hi = cc["target_min_clusters"], cc["target_max_clusters"]
    tried = []
    for mcs in cc["min_cluster_sizes"]:
        if mcs * 3 > len(rows):
            break
        labels = HDBSCAN(min_cluster_size=mcs, min_samples=max(2, mcs // 3)).fit_predict(red)
        k = len(set(labels) - {-1})
        noise = float((labels == -1).mean())
        tried.append((mcs, k, noise, labels))
        print(f"  min_cluster_size={mcs:4d} → {k:3d} clusters, noise {noise:.0%}")
    in_range = [t for t in tried if lo <= t[1] <= hi]
    # in range: least noise; otherwise: closest to the range
    pick = (min(in_range, key=lambda t: t[2]) if in_range
            else min(tried, key=lambda t: (min(abs(t[1] - lo), abs(t[1] - hi)), t[2])))
    mcs, k, noise, labels = pick
    note = "" if in_range else f" (target {lo}-{hi} not reachable at N={len(rows)})"

    # renumber clusters by size (0 = largest)
    sizes = {c: int((labels == c).sum()) for c in set(labels) - {-1}}
    order = {c: i for i, c in enumerate(sorted(sizes, key=lambda c: -sizes[c]))}
    final = [order.get(int(l), -1) for l in labels]

    sig = hashlib.sha1(",".join(f"{r['id']}={c}" for r, c in zip(rows, final)).encode()).hexdigest()
    prev = con.execute("SELECT note FROM runs WHERE stage = 'cluster_sig' ORDER BY at DESC LIMIT 1").fetchone()
    if not prev or prev["note"] != sig:
        con.execute("DELETE FROM clusters")  # labels refer to old ids
        con.execute("INSERT INTO runs VALUES (datetime('now'), 'cluster_sig', ?)", (sig,))
    con.execute("UPDATE items SET cluster = NULL")
    con.executemany("UPDATE items SET cluster = ? WHERE id = ?", [(c, r["id"]) for r, c in zip(rows, final)])
    con.commit()
    log(con, "cluster", f"N={len(rows)} min_cluster_size={mcs} clusters={k} noise={noise:.0%}{note}")

    # representative sample per cluster: nearest to centroid + most-liked + random
    n = cfg["report"]["sample_per_cluster_for_llm"]
    rng = random.Random(cc["random_state"])
    final_arr = np.array(final)
    samples = {}
    for c in range(k):
        idx = np.where(final_arr == c)[0]
        cen = X[idx].mean(0)
        by_cen = idx[np.argsort(-(X[idx] @ cen))].tolist()
        by_eng = sorted(idx.tolist(), key=lambda i: -(rows[i]["engagement"] or 0))
        chosen: list[int] = []
        for pool, quota in ((by_cen, n // 2), (by_eng, n // 4), (rng.sample(idx.tolist(), len(idx)), n)):
            for i in pool:
                if len(chosen) >= n or quota <= 0:
                    break
                if i not in chosen:
                    chosen.append(i)
                    quota -= 1
        samples[c] = [rows[i] for i in chosen]
    return samples
