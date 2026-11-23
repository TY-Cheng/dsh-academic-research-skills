#!/usr/bin/env python3
"""Measure body words for the Stage 2 manuscript (canonical ARS convention).

Rules (shared/references/word_count_conventions.md + Phase 0 word-count convention):
  * whitespace split, len(text.split())
  * every <!--...--> HTML comment stripped first (ref/anchor/protected-hedges)
  * excluded: front matter before '## Draft Body', headings, markdown table rows,
    fenced code blocks (figure source), caption lines ('**Table'/'**Figure'),
    and everything from '## Declarations' onward (declarations, references, appendices)
Usage: python3 measure_words.py paper-draft.md [--per-section]
"""
import re
import sys

COMMENT = re.compile(r"<!--.*?-->", re.S)
SEC = re.compile(r"^## (\d+)\. ")
SUB = re.compile(r"^### (\d+\.\d+) ")


def body_lines(text):
    lines = text.splitlines()
    out, fenced, started, stopped = [], False, False, False
    for line in lines:
        if line.startswith("## Draft Body"):
            started = True
            continue
        if not started:
            continue
        if line.startswith("## Declarations"):
            stopped = True
        if stopped:
            continue
        if line.strip().startswith("```"):
            fenced = not fenced
            continue
        if fenced:
            continue
        out.append(line)
    return out


def count(lines):
    text = "\n".join(lines)
    text = COMMENT.sub("", text)
    total = 0
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("|"):
            continue
        if s.startswith("**Table") or s.startswith("**Figure"):
            continue
        total += len(s.split())
    return total


def main():
    path = sys.argv[1]
    text = open(path, encoding="utf-8").read()
    lines = body_lines(text)
    print(f"TOTAL body words: {count(lines)}")
    if "--per-section" in sys.argv:
        buckets, cur = [], None
        for line in lines:
            m = SEC.match(line)
            if m:
                cur = [m.group(1), []]
                buckets.append(cur)
            if cur is not None:
                cur[1].append(line)
        for sid, chunk in buckets:
            print(f"  section {sid}: {count(chunk)}")


if __name__ == "__main__":
    main()
