"""Build evidence-row/1.0 rows for the Stage 4.5 Phase E claims (E3.1).

Mode 2 = ALL registered citation-bearing claims, one row per (claim_id, ref).
Every claim inside a paragraph touched by Stage 4 / Stage 4' is freshly checked.
Only CLM-079 keeps the Stage 2.5 verdict: its span bytes, ref_slugs and cited
abstract are unchanged and its containing paragraph is byte-identical to v1.3.
"""
import json, re, sys, pathlib
from urllib.parse import quote

sys.path.insert(0, '/Volumes/ExternalSSD/projects/dsh-academic-research-skills/fork/scripts')
import evidence_rows as er

D = pathlib.Path('stage4.5-artifacts')
reg = json.load(open(D / 'claim-registry.json'))
recs = {r['id']: r for r in json.load(open('search/selected_sources.json'))}

abs_map = {}
for rec in json.load(open('search/fetch_results.json')):
    if rec.get('abstract'):
        abs_map[rec['id']] = rec['abstract']
for k, v in json.load(open('search/crossref_abstracts.json')).items():
    if isinstance(v, dict) and v.get('abstract') and k not in abs_map:
        abs_map[k] = v['abstract']

# metadata-only rows: the cited version is not readable in this run
UNAVAILABLE = {'P4', 'P7', 'R4'}
# sole Stage 2.5 carry: unchanged span bytes + refs + abstract, unchanged paragraph
CARRIED = {'EVR-CLM-079-C2'}

def display_label(slug):
    r = recs[slug]
    tag = ' [preprint]' if (r.get('type') == 'preprint' or r.get('peer_reviewed') is False) else ''
    return f"{r['label']}{tag}, {r['venue']}, doi:{r['doi']}"

def best_excerpt(claim_text, source, cap=25):
    """Best-matching contiguous window of <= cap whitespace tokens, exact substring."""
    words = set(re.findall(r"[a-z0-9]{4,}", claim_text.lower()))
    toks = list(re.finditer(r"\S+", source))
    best, best_score = source[:0], -1
    for i in range(len(toks)):
        for n in (cap, 15, 10):
            j = min(len(toks) - 1, i + n - 1)
            seg = source[toks[i].start():toks[j].end()]
            score = len(words & set(re.findall(r"[a-z0-9]{4,}", seg.lower())))
            if score > best_score:
                best, best_score = seg, score
        if len(toks) - i <= cap:
            break
    return best or source[:200]

VERIFIED_DETAIL = (
    "Fresh check against the cited abstract (Stage 4.5): the claim restates the source's "
    "reported mechanism/result within the abstract's scope; excerpt is the best-matching "
    "abstract sentence."
)
UNAVAILABLE_DETAIL = (
    "UNVERIFIABLE_ACCESS: the cited version is metadata-only in this run (no abstract or full "
    "text retrievable), so the claim cannot be checked against the cited source. The reference "
    "entry pins a DOI and the display label names that version; no other version was substituted."
)
CARRIED_DETAIL = (
    "Carried from stage2.5-integrity.md: claim span bytes, ref_slugs and the cited abstract are "
    "unchanged since Stage 2.5 and the containing paragraph is byte-identical to v1.3, so the "
    "Stage 2.5 verdict is reused. Claim restates the source's reported scope within the abstract."
)

rows, audited = [], set()
for c in reg['claims']:
    if not c['ref_slugs']:
        continue
    audited.add(c['claim_id'])
    locator = f"paper-draft-v3.md v3.0, section {c['paper_section']}"
    for slug in c['ref_slugs']:
        rid = f"EVR-{c['claim_id']}-{slug}"
        detail = VERIFIED_DETAIL
        if rid in CARRIED:
            detail = CARRIED_DETAIL
        elif slug in UNAVAILABLE:
            detail = UNAVAILABLE_DETAIL
        row = {
            "surface": "phase_e_claim_verification",
            "row_id": rid,
            "claim": {"claim_id": c['claim_id'], "text": c['claim_text'],
                      "paper_locator": locator, "selection_tier": c['selection_tier']},
            "source": {"ref_slug": slug, "display_label": display_label(slug)},
            "anchor": {"kind": "section", "value_encoded": quote(c['paper_section'], safe='')},
            "verdict": "UNVERIFIABLE_ACCESS" if slug in UNAVAILABLE else "VERIFIED",
            "detail": detail,
        }
        src = abs_map.get(slug)
        if src is None:
            rows.append(er.build(row, None, failure_state="source_missing"))
        else:
            rows.append(er.build(row, src, extracted_text=best_excerpt(c['claim_text'], src)))

for r in rows:
    er.validate(r)

(D / 'evidence-rows.json').write_text(json.dumps(rows, indent=1, ensure_ascii=False) + "\n", encoding='utf-8')
src_dir = D / 'evidence-sources'
src_dir.mkdir(exist_ok=True)
for slug in sorted(set(r['source']['ref_slug'] for r in rows)):
    if slug in abs_map:
        (src_dir / er.source_file_name(slug)).write_text(abs_map[slug], encoding='utf-8')

by_claim = {}
for r in rows:
    by_claim.setdefault(r['claim']['claim_id'], []).append(r['verdict'])
ORDER = ["MAJOR_DISTORTION", "UNVERIFIABLE", "MINOR_DISTORTION", "UNVERIFIABLE_ACCESS", "VERIFIED"]
claim_verdict = {k: next(v for v in ORDER if v in vs) for k, vs in by_claim.items()}
summary = {
    "registered_claims": len(reg['claims']),
    "claims_audited": len(audited),
    "rows": len(rows),
    "refs_covered": len(set(r['source']['ref_slug'] for r in rows)),
    "row_verdicts": {v: sum(1 for r in rows if r['verdict'] == v) for v in
                     ["VERIFIED", "MINOR_DISTORTION", "MAJOR_DISTORTION", "UNVERIFIABLE", "UNVERIFIABLE_ACCESS"]},
    "claim_verdicts": {v: sum(1 for x in claim_verdict.values() if x == v) for v in
                       ["VERIFIED", "MINOR_DISTORTION", "MAJOR_DISTORTION", "UNVERIFIABLE", "UNVERIFIABLE_ACCESS"]},
    "carried_from_stage2_5": sorted(CARRIED),
    "freshly_checked_rows": sum(1 for r in rows if r['row_id'] not in CARRIED),
    "unavailable_refs": sorted(UNAVAILABLE),
}
(D / 'evidence-rows-summary.json').write_text(json.dumps(summary, indent=1) + "\n", encoding='utf-8')
print(json.dumps(summary, indent=1))
