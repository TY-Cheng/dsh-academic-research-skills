#!/usr/bin/env python3
"""Stage 4.5 Phase B coverage + Phase D originality (8-gram) checks.

Body = Draft Body / section 1 through section 7, ending before Declarations.
Paragraph = blank-line separated block of prose (headings, table rows, fences,
figure/table captions and notes excluded). Citation markers (HTML comments) are
stripped before tokenising.
"""
import json
import re
import sys
from difflib import SequenceMatcher
from pathlib import Path

RUN = Path(__file__).resolve().parents[1]
V3 = RUN / "stage4-prime/paper-draft-v3.md"
V2 = RUN / "stage4/paper-draft-v2.md"
V1 = RUN / "stage2/paper-draft.md"
ABS = Path("/tmp/abs45.json")

COMMENT = re.compile(r"<!--.*?-->")
TOKEN = re.compile(r"[a-z0-9]+(?:[-'][a-z0-9]+)*")
TABLE_ROW = re.compile(r"^\s*\|")
CAPTION = re.compile(
    r"^\s*(?:\*\*)?(?:Figure|Table)\s+(?:\d+|[A-Z]\d+)", re.IGNORECASE
)
FENCE = re.compile(r"^\s*```")


def body_lines(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    start = next(i for i, ln in enumerate(lines) if ln.startswith("## Draft Body"))
    end = next(i for i, ln in enumerate(lines) if ln.startswith("## Declarations"))
    return lines[start + 1:end]


def paragraphs(path):
    out = []
    buf = []

    def flush():
        if buf:
            text = " ".join(buf).strip()
            text = text.strip()
            if len(text) > 40:
                out.append(text)
            buf.clear()

    for ln in body_lines(path):
        s = ln.strip()
        if not s:
            flush()
            continue
        if s.startswith("#") or s.startswith("---") or FENCE.match(s):
            flush()
            continue
        if s.startswith(">"):
            flush()
            continue
        if TABLE_ROW.match(s) or CAPTION.match(s):
            flush()
            continue
        buf.append(s)
    flush()
    return out


def words(text):
    return TOKEN.findall(COMMENT.sub("", text).lower())


def best_match(a_tokens, b_paras):
    """Return (ratio, index) of the most similar paragraph in b_paras."""
    sm = SequenceMatcher(None, a_tokens, [], autojunk=False)
    best = (0.0, -1)
    for j, (b_tokens, _b_text) in enumerate(b_paras):
        sm.set_seq2(b_tokens)
        r = sm.ratio()
        if r > best[0]:
            best = (r, j)
    return best


def longest_shared_run(tokens, other_tokens, min_run=8):
    sm = SequenceMatcher(None, tokens, other_tokens, autojunk=False)
    longest = 0
    matches = 0
    for block in sm.get_matching_blocks():
        if block.size >= min_run:
            matches += block.size
            longest = max(longest, block.size)
    return longest, matches


def main():
    v3p = paragraphs(V3)
    v2p = paragraphs(V2)
    v1p = paragraphs(V1)
    v3t = [words(p) for p in v3p]
    v2t = [words(p) for p in v2p]
    v1t = [words(p) for p in v1p]

    # ---- Phase B: v3 vs v2 and v3 vs v1.3 paragraph status
    status_v2 = []
    status_v1 = []
    for i, toks in enumerate(v3t):
        r2, _ = best_match(toks, list(zip(v2t, v2p)))
        r1, _ = best_match(toks, list(zip(v1t, v1p)))
        status_v2.append(r2)
        status_v1.append(r1)

    def bucket(r):
        if r >= 0.90:
            return "unchanged"
        if r >= 0.60:
            return "substantially_modified"
        return "added"

    b_v2 = {"unchanged": 0, "substantially_modified": 0, "added": 0}
    b_v1 = {"unchanged": 0, "substantially_modified": 0, "added": 0}
    for r in status_v2:
        b_v2[bucket(r)] += 1
    for r in status_v1:
        b_v1[bucket(r)] += 1

    # ---- Phase D: 8-gram overlap with 41 source abstracts + prior drafts
    abstracts = json.loads(ABS.read_text(encoding="utf-8"))
    abs_tokens = {k: words(v) for k, v in abstracts.items()}
    draft_paras_v1 = list(zip(v1t, v1p))
    draft_paras_v2 = list(zip(v2t, v2p))

    grade_of = {"ORIGINAL": 0, "PARAPHRASE": 0, "CLOSE_MATCH": 0, "VERBATIM": 0}
    rows = []
    external_hits = 0
    for i, toks in enumerate(v3t):
        # longest shared run with any single abstract
        best_abs = (0, "", 0)
        for slug, at in abs_tokens.items():
            longest, total = longest_shared_run(toks, at)
            if longest > best_abs[0]:
                best_abs = (longest, slug, total)
        # longest shared run with any prior-draft paragraph
        best_v2 = (0, -1)
        for j, (bt, _) in enumerate(draft_paras_v2):
            longest, _ = longest_shared_run(toks, bt)
            if longest > best_v2[0]:
                best_v2 = (longest, j)
        best_v1 = (0, -1)
        for j, (bt, _) in enumerate(draft_paras_v1):
            longest, _ = longest_shared_run(toks, bt)
            if longest > best_v1[0]:
                best_v1 = (longest, j)

        if best_abs[0] >= 20:
            grade = "VERBATIM"
        elif best_abs[0] >= 12:
            grade = "CLOSE_MATCH"
        elif best_abs[0] >= 8:
            grade = "PARAPHRASE"
        else:
            grade = "ORIGINAL"
        grade_of[grade] += 1
        if best_abs[0] >= 8:
            external_hits += 1
        rows.append(
            {
                "index": i,
                "words": len(toks),
                "citations": len(re.findall(r"<!--ref:([A-Za-z0-9]+)-->", v3p[i])),
                "grade": grade,
                "longest_abstract_run": best_abs[0],
                "abstract_slug": best_abs[1],
                "draft_v2_run": best_v2[0],
                "draft_v1_run": best_v1[0],
                "status_vs_v2": bucket(status_v2[i]),
                "ratio_vs_v2": round(status_v2[i], 3),
                "status_vs_v1": bucket(status_v1[i]),
                "ratio_vs_v1": round(status_v1[i], 3),
            }
        )

    citations = sum(1 for p in v3p if "<!--ref:" in p)
    markers = sum(len(re.findall(r"<!--ref:([A-Za-z0-9]+)-->", p)) for p in v3p)
    summary = {
        "body_paragraphs_v3": len(v3p),
        "body_paragraphs_v2": len(v2p),
        "body_paragraphs_v1": len(v1p),
        "v3_paragraph_status_vs_v2": b_v2,
        "v3_paragraph_status_vs_v1": b_v1,
        "paragraphs_with_citations": citations,
        "body_citation_markers": markers,
        "phase_d_grades": grade_of,
        "paragraphs_with_external_8gram": external_hits,
        "rows": rows,
    }
    (RUN / "stage4.5-artifacts/phase-bd-checks.json").write_text(
        json.dumps(summary, indent=1), encoding="utf-8"
    )
    print(json.dumps({k: v for k, v in summary.items() if k != "rows"}, indent=1))
    print("\n// per-paragraph")
    for r in rows:
        print(
            f"{r['index']:3d} w={r['words']:4d} cit={r['citations']:2d} "
            f"grade={r['grade']:11s} abs={r['longest_abstract_run']:2d}"
            f"({r['abstract_slug']}) v2={r['draft_v2_run']:2d} v1={r['draft_v1_run']:2d} "
            f"status_v2={r['status_vs_v2']}"
        )


if __name__ == "__main__":
    sys.exit(main() or 0)
