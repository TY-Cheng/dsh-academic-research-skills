#!/usr/bin/env python3
"""Fetch OpenAlex metadata + abstracts for the 41-source Phase 2 corpus.

The selection is read from selected_index.json (produced by the discovery
stage of this run), not from the earlier example corpus. Every record is
looked up by DOI first; when the DOI lookup fails the script falls back to an
OpenAlex title search and requires a normalised title similarity >= 0.70
before accepting the hit.

Outputs (all inside search/):
  fetch_results.json   full OpenAlex-derived record per source + retrieval meta
  retrieval_log.json   one compact entry per source (method, status, abstract chars)

Anonymous OpenAlex budget: 1 request/second is observed by sleeping 1.1 s
between requests. Nothing here writes outside the run directory.
"""
from __future__ import annotations

import difflib
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

BASE = "https://api.openalex.org/works"
FIELDS = ",".join(
    [
        "id",
        "doi",
        "title",
        "display_name",
        "publication_year",
        "publication_date",
        "type",
        "authorships",
        "primary_location",
        "biblio",
        "cited_by_count",
        "is_retracted",
        "abstract_inverted_index",
    ]
)
SLEEP = 1.1
UA = "ARS-deep-research-validation/1.0 (mailto:validation@example.org)"

HERE = Path(__file__).resolve().parent
SELECTED = HERE / "selected_index.json"


def get(url: str, tries: int = 3) -> tuple[int, dict | None]:
    """GET a JSON document, honouring Retry-After on transient 429s."""
    for attempt in range(tries):
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=45) as resp:
                return resp.getcode(), json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", "replace")[:300]
            if exc.code == 429 and attempt < tries - 1:
                retry_after = 5
                try:
                    retry_after = int(exc.headers.get("Retry-After") or 5)
                except ValueError:
                    pass
                time.sleep(min(max(retry_after, 2), 60))
                continue
            return exc.code, {"error": body}
        except Exception as exc:  # timeouts, DNS, malformed JSON
            if attempt < tries - 1:
                time.sleep(2 ** attempt)
                continue
            return 0, {"error": f"{type(exc).__name__}: {exc}"}
    return 0, {"error": "exhausted retries"}


def reconstitute(index: dict | None) -> str:
    if not index:
        return ""
    positions: dict[int, str] = {}
    for word, locs in index.items():
        for pos in locs:
            positions[pos] = word
    if not positions:
        return ""
    return " ".join(positions[p] for p in range(max(positions) + 1))


def norm_title(text: str) -> str:
    return re.sub(r"[^a-z0-9 ]+", " ", (text or "").lower()).strip()


def similarity(a: str, b: str) -> float:
    return difflib.SequenceMatcher(None, norm_title(a), norm_title(b)).ratio()


def field(rec: dict, key: str, default=None):
    return rec.get(key, default)


def authors_of(rec: dict) -> list[str]:
    names = []
    for a in rec.get("authorships") or []:
        name = (a.get("author") or {}).get("display_name")
        if name:
            names.append(name)
    return names


def venue_of(rec: dict) -> str:
    loc = rec.get("primary_location") or {}
    src = loc.get("source") or {}
    return src.get("display_name") or loc.get("landing_page_url") or ""


def doi_of(rec: dict) -> str:
    raw = rec.get("doi") or ""
    return raw.replace("https://doi.org/", "").strip()


def fetch_one(item: dict) -> dict:
    doi = (item.get("doi") or "").strip()
    title = item.get("title") or ""
    meta = {
        "id": item["id"],
        "family": item["family"],
        "requested_doi": doi,
        "requested_title": title,
        "doi_lookup_status": None,
        "title_search_status": None,
        "title_match": None,
        "retrieval_method": None,
    }
    rec: dict | None = None

    if doi:
        status, payload = get(f"{BASE}/doi:{urllib.parse.quote(doi)}?select={FIELDS}")
        meta["doi_lookup_status"] = status
        if status == 200 and payload and not payload.get("error"):
            rec = payload
            meta["retrieval_method"] = "doi"
            meta["title_match"] = round(
                similarity(title, rec.get("display_name") or rec.get("title") or ""), 3
            )
        time.sleep(SLEEP)

    if rec is None:
        query = urllib.parse.quote(title)
        status, payload = get(
            f"{BASE}?search={query}&per-page=5&select={FIELDS}"
        )
        meta["title_search_status"] = status
        best = None
        best_score = 0.0
        if status == 200 and payload and payload.get("results"):
            for cand in payload["results"]:
                score = similarity(title, cand.get("display_name") or cand.get("title") or "")
                if score > best_score:
                    best, best_score = cand, score
        meta["title_match"] = round(best_score, 3)
        if best is not None and best_score >= 0.70:
            rec = best
            meta["retrieval_method"] = "title_search"
        time.sleep(SLEEP)

    if rec is None:
        return {
            "meta": meta,
            "record": None,
            "abstract": "",
            "abstract_status": "title-level",
        }

    abstract = reconstitute(rec.get("abstract_inverted_index"))
    if len(abstract) >= 500:
        abstract_status = "abstract"
    elif abstract:
        abstract_status = "partial"
    else:
        abstract_status = "metadata-only"

    return {
        "meta": meta,
        "record": {
            "openalex_id": rec.get("id"),
            "doi": doi_of(rec) or doi,
            "title": rec.get("display_name") or rec.get("title") or title,
            "year": rec.get("publication_year"),
            "publication_date": rec.get("publication_date"),
            "type": rec.get("type"),
            "venue": venue_of(rec),
            "authors": authors_of(rec),
            "biblio": rec.get("biblio") or {},
            "cited_by_count": rec.get("cited_by_count"),
            "is_retracted": rec.get("is_retracted"),
            "language": rec.get("language"),
        },
        "abstract": abstract,
        "abstract_status": abstract_status,
    }


def main() -> int:
    index = json.loads(SELECTED.read_text(encoding="utf-8"))
    results = []
    log = []
    for n, item in enumerate(index, 1):
        out = fetch_one(item)
        rec = out["record"]
        entry = {
            "id": item["id"],
            "requested_doi": out["meta"]["requested_doi"],
            "requested_title": out["meta"]["requested_title"],
            "resolved_openalex_id": rec["openalex_id"] if rec else None,
            "resolved_doi": rec["doi"] if rec else None,
            "resolved_title": rec["title"] if rec else None,
            "doi_lookup_status": out["meta"]["doi_lookup_status"],
            "title_search_status": out["meta"]["title_search_status"],
            "title_match": out["meta"]["title_match"],
            "retrieval_method": out["meta"]["retrieval_method"],
            "abstract_chars": len(out["abstract"]),
            "abstract_status": out["abstract_status"],
            "is_retracted": rec["is_retracted"] if rec else None,
            "resolved_ok": rec is not None,
        }
        log.append(entry)
        results.append(
            {
                "id": item["id"],
                "family": item["family"],
                "requested": item,
                "retrieval": out["meta"],
                "record": rec,
                "abstract": out["abstract"],
                "abstract_status": out["abstract_status"],
            }
        )
        print(
            f"[{n:02d}/{len(index)}] {item['id']:<3} {out['abstract_status']:<13} "
            f"doi={out['meta']['doi_lookup_status']} "
            f"title={out['meta']['title_search_status']} "
            f"match={out['meta']['title_match']} "
            f"chars={len(out['abstract'])} {item['title'][:60]}",
            flush=True,
        )

    (HERE / "fetch_results.json").write_text(
        json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    (HERE / "retrieval_log.json").write_text(
        json.dumps(log, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    counts: dict[str, int] = {}
    for e in log:
        counts[e["abstract_status"]] = counts.get(e["abstract_status"], 0) + 1
    print("\nretrieval status:", counts)
    print("resolved:", sum(1 for e in log if e["resolved_ok"]), "/", len(log))
    missing = [e["id"] for e in log if not e["resolved_ok"]]
    if missing:
        print("unresolved:", missing)
    return 0


if __name__ == "__main__":
    sys.exit(main())
