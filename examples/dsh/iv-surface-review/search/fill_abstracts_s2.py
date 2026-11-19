#!/usr/bin/env python3
"""Fill OpenAlex-missing abstracts from Semantic Scholar (Phase 2 only).

OpenAlex returned no abstract for 10 of the 40 selected records. This script
queries S2 by DOI (title fallback) and records the abstract plus the S2
paperId, so the bibliography's Key Findings are not inferred from titles.
"""
from __future__ import annotations

import json
import time
import urllib.parse
import urllib.request
from pathlib import Path

BASE = "https://api.semanticscholar.org/graph/v1"
FIELDS = "title,abstract,year,venue,authors,externalIds"


def get(url: str) -> dict:
    request = urllib.request.Request(url, headers={"User-Agent": "ARS-e2e/0.3.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def main() -> None:
    out_dir = Path(__file__).resolve().parent
    path = out_dir / "selected_sources.json"
    records = json.loads(path.read_text(encoding="utf-8"))
    for record in records:
        if record.get("abstract"):
            continue
        doi = record.get("doi") or ""
        title = record.get("title") or ""
        try:
            if doi:
                data = get(
                    f"{BASE}/paper/DOI:{urllib.parse.quote(doi, safe='')}"
                    f"?fields={FIELDS}"
                )
            else:
                search = get(
                    f"{BASE}/paper/search?query={urllib.parse.quote(title)}"
                    f"&limit=3&fields={FIELDS}"
                )
                candidates = search.get("data") or []
                data = candidates[0] if candidates else {}
            record["s2_paper_id"] = data.get("paperId")
            record["s2_title"] = data.get("title")
            record["s2_venue"] = data.get("venue")
            record["abstract"] = data.get("abstract") or ""
            print(
                f"[s2] {record.get('year')} {title[:70]} | "
                f"abstract={len(record['abstract'])} | id={data.get('paperId')}"
            )
        except Exception as exc:  # noqa: BLE001
            record["s2_error"] = str(exc)
            print(f"[s2-error] {title[:70]}: {exc}")
        time.sleep(1.1)

    path.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = ["# Selected corpus with abstracts", ""]
    for index, record in enumerate(records, start=1):
        lines.append(
            f"## {index}. {record.get('title')} ({record.get('year')})\n\n"
            f"- DOI: `{record.get('doi') or ''}`\n"
            f"- Venue: {record.get('venue') or ''}\n"
            f"- Authors: {', '.join(record.get('authors') or [])}\n"
            f"- Abstract: {record.get('abstract') or '(unavailable)'}\n"
        )
    (out_dir / "selected_sources_full.md").write_text(
        "\n".join(lines), encoding="utf-8"
    )
    print(f"filled={sum(1 for r in records if r.get('abstract'))}/{len(records)}")


if __name__ == "__main__":
    main()
