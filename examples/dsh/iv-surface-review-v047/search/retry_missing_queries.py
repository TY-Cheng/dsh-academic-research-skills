#!/usr/bin/env python3
"""Retry the OpenAlex discovery queries that hit transient 429s.

The first pass logged 21 transient "search cluster under elevated load"
responses with a Retry-After header. This script reloads the candidate pool,
re-runs only the failed queries with Retry-After-honouring backoff and 2 s
pacing, merges the results, and rewrites both candidate artifacts.

Usage:
    fork/.venv/bin/python examples/dsh/iv-surface-review-v047/search/retry_missing_queries.py
"""
from __future__ import annotations

import json
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

from openalex_search import BASE, FIELDS, author_names, venue

OUT = Path(__file__).resolve().parent
MAX_ATTEMPTS = 3


def fetch(query: str) -> dict:
    params = {"search": query, "per-page": "25", "select": FIELDS}
    url = f"{BASE}?{urllib.parse.urlencode(params)}"
    last: Exception | None = None
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            with urllib.request.urlopen(url, timeout=40) as response:
                return json.load(response)
        except urllib.error.HTTPError as exc:
            last = exc
            retry_after = int(exc.headers.get("Retry-After") or 0)
            wait = max(retry_after, 5) + 2 if exc.code == 429 else 5
            print(f"  [{exc.code}] attempt {attempt}/{MAX_ATTEMPTS}; waiting {wait}s")
            time.sleep(wait)
        except Exception as exc:  # noqa: BLE001
            last = exc
            print(f"  [err] attempt {attempt}/{MAX_ATTEMPTS}: {exc}")
            time.sleep(5)
    raise RuntimeError(f"failed after {MAX_ATTEMPTS} attempts: {last}")


def main() -> None:
    payload = json.loads((OUT / "openalex_candidates.json").read_text(encoding="utf-8"))
    records = {r["doi"] or r["title"].lower(): r for r in payload["records"]}
    still_failed = []
    recovered = 0

    for entry in payload["queries"]:
        if "error" not in entry:
            continue
        query, stratum = entry["query"], entry["stratum"]
        print(f"[retry] {stratum}: {query}")
        try:
            body = fetch(query)
        except Exception as exc:  # noqa: BLE001
            print(f"  [give-up] {exc}")
            still_failed.append(entry)
            continue
        results = body.get("results") or []
        entry.pop("error", None)
        entry.update({"count": body.get("meta", {}).get("count", 0), "returned": len(results)})
        recovered += 1
        for work in results:
            doi = (work.get("doi") or "").replace("https://doi.org/", "").lower()
            title = (work.get("title") or "").strip()
            key = doi or title.lower()
            if not key:
                continue
            record = records.setdefault(
                key,
                {
                    "doi": doi,
                    "title": title,
                    "year": work.get("publication_year"),
                    "publication_date": work.get("publication_date"),
                    "language": work.get("language"),
                    "venue": venue(work),
                    "authors": author_names(work),
                    "cited_by_count": work.get("cited_by_count") or 0,
                    "type": work.get("type") or "",
                    "is_retracted": bool(work.get("is_retracted")),
                    "openalex_id": work.get("id"),
                    "queries": [],
                    "strata": [],
                },
            )
            if query not in record["queries"]:
                record["queries"].append(query)
            if stratum not in record["strata"]:
                record["strata"].append(stratum)
        time.sleep(2.0)

    payload["records"] = sorted(
        records.values(), key=lambda r: (len(r["queries"]), r["cited_by_count"]), reverse=True
    )
    payload["retry_note"] = (
        f"Second pass recovered {recovered} queries; {len(still_failed)} still failed."
    )
    (OUT / "openalex_candidates.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    lines = [
        "# OpenAlex candidate pool (fresh v0.4.7 discovery)",
        "",
        f"Queries: {len(payload['queries'])}; unique records: {len(payload['records'])}.",
        "",
        "| # | Year | Hits | Cites | DOI | Title | Venue |",
        "|---:|---:|---:|---:|---|---|---|",
    ]
    for index, record in enumerate(payload["records"], start=1):
        title = record["title"].replace("|", "\\|")
        lines.append(
            f"| {index} | {record['year']} | {len(record['queries'])} | "
            f"{record['cited_by_count']} | `{record['doi']}` | {title} | "
            f"{record['venue'].replace('|', '\\|')} |"
        )
    (OUT / "openalex_candidates.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"recovered={recovered} failed={len(still_failed)} records={len(payload['records'])}")


if __name__ == "__main__":
    main()
