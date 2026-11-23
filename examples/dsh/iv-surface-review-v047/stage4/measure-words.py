#!/usr/bin/env python3
"""Count the body words of the revised manuscript (v2.0).

Same counting rules as the stage-2 counter, so the two versions are comparable:
body = from the `## Draft Body` heading to the `## Declarations` heading, with
HTML comments stripped, headings, table rows, fenced code blocks and the
`**Table`/`**Figure` caption lines excluded. Words are whitespace-separated
tokens, so an em-dash between spaces counts as one token.

Usage:
    python measure_words.py [paper-draft-v2.md] [--per-section] [--per-subsection]
"""
import argparse
import re
import sys
from pathlib import Path

COMMENT = re.compile(r"<!--.*?-->", re.S)
BODY_START = "## Draft Body"
BODY_END = "## Declarations"
SECTION = re.compile(r"^## (\d+)\. ")
SUBSECTION = re.compile(r"^### (\d+\.\d+) ")


def body_lines(text: str) -> list[str]:
    text = COMMENT.sub("", text)
    lines = text.splitlines()
    start = next(i for i, ln in enumerate(lines) if ln.startswith(BODY_START))
    end = next(i for i, ln in enumerate(lines) if ln.startswith(BODY_END))
    out, fenced = [], False
    for ln in lines[start + 1 : end]:
        if ln.strip().startswith("```"):
            fenced = not fenced
            continue
        if fenced:
            continue
        out.append(ln)
    return out


def count(lines: list[str]) -> int:
    total = 0
    for ln in lines:
        s = ln.strip()
        if not s or s.startswith("#") or s.startswith("|"):
            continue
        if s.startswith("**Table") or s.startswith("**Figure"):
            continue
        total += len(s.split())
    return total


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    here = Path(__file__).resolve().parent
    ap.add_argument("path", nargs="?", default=str(here / "paper-draft-v2.md"))
    ap.add_argument("--per-section", action="store_true")
    ap.add_argument("--per-subsection", action="store_true")
    args = ap.parse_args()

    path = Path(args.path)
    if not path.is_file():
        print(f"no such file: {path}", file=sys.stderr)
        return 2
    lines = body_lines(path.read_text(encoding="utf-8"))
    total = count(lines)
    print(f"{path.name}: body words = {total}")

    if args.per_section or args.per_subsection:
        bucket, key = [], "preamble"
        buckets: dict[str, list[str]] = {}
        for ln in lines:
            m = SECTION.match(ln) if not args.per_subsection else SUBSECTION.match(ln)
            if m:
                key = m.group(1)
                bucket = [ln]
                buckets[key] = bucket
            else:
                buckets.setdefault(key, []).append(ln)
        for key, chunk in buckets.items():
            if key == "preamble":
                continue
            label = f"§{key}" if not args.per_subsection else f"§{key}"
            print(f"  {label:<8} {count(chunk):>5}")

    lo, hi, target = 6000, 8000, 7800
    verdict = "within" if lo <= total <= hi else "OUTSIDE"
    print(f"budget {lo}-{hi} (target <={target}): {verdict}"
          + ("" if total <= target else f"; over target by {total - target}"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
