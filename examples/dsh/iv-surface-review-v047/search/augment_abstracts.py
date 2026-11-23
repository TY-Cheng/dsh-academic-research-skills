#!/usr/bin/env python3
"""Augment OpenAlex abstracts with Crossref and Semantic Scholar fallbacks.

fetch_selected.py only reads OpenAlex's abstract_inverted_index. Some records
in this corpus are metadata-only there, and two are short truncated snippets.
For every record whose abstract_status is not "abstract", this script tries:

  1. Crossref  https://api.crossref.org/works/{doi}      (JATS abstract, stripped)
  2. Semantic Scholar graph/v1/paper/DOI:{doi}?fields=title,abstract,year

and keeps the longest plausible abstract it found. The abstract is then
reclassified: >= 500 chars -> "abstract", shorter non-empty -> "partial",
nothing -> "metadata-only". The source is recorded as abstract_source
(openalex / crossref / semanticscholar / None) so the verification report can
state where each abstract came from.

Reads and rewrites search/fetch_results.json in place; also refreshes the
abstract fields of search/retrieval_log.json. 1 request/second pacing.
"""
from __future__ import annotations

import html
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
CROSSREF = "https://api.crossref.org/works/"
S2 = "https://api.semanticscholar.org/graph/v1/paper/DOI:"
UA = "ARS-deep-research-validation/1.0 (mailto:validation@example.org)"
SLEEP = 1.0

TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")


def get_json(url: str, tries: int = 3) -> dict | None:
    for attempt in range(tries):
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=40) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            if exc.code in (404, 400):
                return None
            if attempt < tries - 1:
                time.sleep(2 + attempt * 2)
        except Exception:
            if attempt < tries - 1:
                time.sleep(2 + attempt * 2)
    return None


def clean(text: str) -> str:
    text = html.unescape(text or "")
    text = TAG_RE.sub(" ", text)
    text = html.unescape(text)
    return WS_RE.sub(" ", text).strip()


def crossref_abstract(doi: str) -> str:
    data = get_json(CROSSREF + urllib.parse.quote(doi))
    if not data:
        return ""
    msg = data.get("message") or {}
    return clean(msg.get("abstract") or "")


def s2_abstract(doi: str) -> str:
    data = get_json(
        S2 + urllib.parse.quote(doi) + "?fields=title,abstract,year"
    )
    if not data:
        return ""
    return clean(data.get("abstract") or "")


def main() -> int:
    results = json.loads((HERE / "fetch_results.json").read_text(encoding="utf-8"))
    log = json.loads((HERE / "retrieval_log.json").read_text(encoding="utf-8"))
    log_by_id = {e["id"]: e for e in log}

    changed = 0
    for item in results:
        sid = item["id"]
        rec = item.get("record") or {}
        doi = (rec.get("doi") or item.get("requested", {}).get("doi") or "").strip()
        current = item.get("abstract") or ""
        status = item.get("abstract_status") or "metadata-only"
        source = "openalex" if current else None

        if status != "abstract" and doi:
            cr = crossref_abstract(doi)
            time.sleep(SLEEP)
            s2 = ""
            if len(cr) < 200:
                s2 = s2_abstract(doi)
                time.sleep(SLEEP)
            best = max((current, cr, s2), key=len)
            if best and best != current:
                current = best
                source = "crossref" if best == cr else "semanticscholar"
                changed += 1
        elif current:
            source = item.get("abstract_source") or "openalex"

        if len(current) >= 500:
            status = "abstract"
        elif current:
            status = "partial"
        else:
            status = "metadata-only"
            source = None

        item["abstract"] = current
        item["abstract_status"] = status
        item["abstract_source"] = source
        entry = log_by_id.get(sid)
        if entry is not None:
            entry["abstract_chars"] = len(current)
            entry["abstract_status"] = status
            entry["abstract_source"] = source
        print(f"{sid:<3} {status:<13} {len(current):>5} chars  {source}")

    (HERE / "fetch_results.json").write_text(
        json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    (HERE / "retrieval_log.json").write_text(
        json.dumps(log, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    counts: dict[str, int] = {}
    sources: dict[str, int] = {}
    for item in results:
        counts[item["abstract_status"]] = counts.get(item["abstract_status"], 0) + 1
        sources[item["abstract_source"]] = sources.get(item["abstract_source"], 0) + 1
    print("\nabstract_status:", counts)
    print("abstract_source:", sources)
    print("newly recovered:", changed)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
