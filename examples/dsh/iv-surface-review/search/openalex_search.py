#!/usr/bin/env python3
"""Phase 2 discovery pass for the IV-surface review.

Runs a fixed set of OpenAlex full-text queries, deduplicates by DOI/title,
and writes the raw candidate pool plus a ranked Markdown shortlist. The
OpenAlex query list is the "Databases/Keywords/Boolean/Date Range" record
for the bibliography's Search Strategy section.

Usage:
    .venv/bin/python openalex_search.py
"""
from __future__ import annotations

import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

BASE = "https://api.openalex.org/works"
FIELDS = ",".join(
    [
        "id",
        "doi",
        "title",
        "publication_year",
        "authorships",
        "primary_location",
        "cited_by_count",
        "type",
        "is_retracted",
    ]
)

QUERIES = [
    "arbitrage-free implied volatility surface",
    "implied volatility surface arbitrage",
    "SVI stochastic volatility inspired",
    "SSVI implied volatility surface",
    "shape constrained implied volatility surface",
    "nonparametric implied volatility surface",
    "neural network implied volatility surface",
    "deep learning implied volatility surface",
    "neural network option pricing arbitrage-free",
    "rough volatility calibration neural network",
    "implied volatility surface machine learning",
    "dynamic arbitrage implied volatility",
    "implied volatility surface interpolation no arbitrage",
    "generative model implied volatility surface",
    "variational autoencoder implied volatility surface",
    "neural SDE volatility surface",
    "deep calibration stochastic volatility",
    "no-arbitrage smoothing implied volatility",
    "calendar arbitrage implied volatility",
    "butterfly arbitrage implied volatility",
    "implied volatility surface survey",
    "arbitrage-free option prices neural network",
    "Gaussian process implied volatility surface",
    "neural network calibration rough volatility",
]


def author_names(work: dict) -> list[str]:
    names = []
    for authorship in work.get("authorships") or []:
        name = (authorship.get("author") or {}).get("display_name")
        if name:
            names.append(name)
    return names


def venue(work: dict) -> str:
    source = (work.get("primary_location") or {}).get("source") or {}
    return source.get("display_name") or ""


def main() -> None:
    out_dir = Path(__file__).resolve().parent
    records: dict[str, dict] = {}
    query_log = []

    for query in QUERIES:
        params = {"search": query, "per-page": "25", "select": FIELDS}
        url = f"{BASE}?{urllib.parse.urlencode(params)}"
        try:
            with urllib.request.urlopen(url, timeout=30) as response:
                payload = json.load(response)
        except Exception as exc:  # noqa: BLE001 - log and continue per API protocol
            print(f"[skip] {query!r}: {exc}")
            query_log.append({"query": query, "count": 0, "error": str(exc)})
            continue

        results = payload.get("results") or []
        query_log.append(
            {
                "query": query,
                "count": payload.get("meta", {}).get("count", 0),
                "returned": len(results),
            }
        )
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
                    "venue": venue(work),
                    "authors": author_names(work),
                    "cited_by_count": work.get("cited_by_count") or 0,
                    "type": work.get("type") or "",
                    "is_retracted": bool(work.get("is_retracted")),
                    "openalex_id": work.get("id"),
                    "queries": [],
                },
            )
            if query not in record["queries"]:
                record["queries"].append(query)
        time.sleep(1.1)

    rows = sorted(
        records.values(),
        key=lambda r: (len(r["queries"]), r["cited_by_count"]),
        reverse=True,
    )
    (out_dir / "openalex_candidates.json").write_text(
        json.dumps(
            {
                "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
                "queries": query_log,
                "records": rows,
            },
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )

    lines = [
        "# OpenAlex candidate pool",
        "",
        f"Queries: {len(QUERIES)}; unique records: {len(rows)}.",
        "",
        "| # | Year | Hits | Cites | DOI | Title | Venue |",
        "|---:|---:|---:|---:|---|---|---|",
    ]
    for index, record in enumerate(rows[:120], start=1):
        title = record["title"].replace("|", "\\|")
        lines.append(
            f"| {index} | {record['year']} | {len(record['queries'])} | "
            f"{record['cited_by_count']} | `{record['doi']}` | {title} | "
            f"{record['venue'].replace('|', '\\|')} |"
        )
    (out_dir / "openalex_candidates.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"queries={len(QUERIES)} records={len(rows)}")
    for index, record in enumerate(rows[:40], start=1):
        print(
            f"{index:02d}. [{record['year']}] ({len(record['queries'])} hits, "
            f"{record['cited_by_count']} cites) {record['title']} -- {record['doi']}"
        )


if __name__ == "__main__":
    main()
