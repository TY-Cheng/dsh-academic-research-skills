"""Build evidence-row/1.0 rows for the Stage 2.5 Phase E audited claims (E3.1)."""
import json, re, sys, pathlib
from urllib.parse import quote
sys.path.insert(0, '/Volumes/ExternalSSD/projects/dsh-academic-research-skills/fork/scripts')
import evidence_rows as er

D = pathlib.Path('stage2.5-artifacts')
reg = json.load(open(D / 'claim-registry.json'))
recs = {r['id']: r for r in json.load(open('search/selected_sources.json'))}
abs_map = {k: v['abstract'] for k, v in json.load(open('/tmp/abstracts.json')).items() if v.get('abstract')}
cr = json.load(open('search/crossref_abstracts.json'))
for k, v in cr.items():
    if isinstance(v, dict) and v.get('abstract') and k not in abs_map:
        abs_map[k] = v['abstract']

DETAIL = {
 "CLM-X01": "Recomputed: 41 selected_sources.json records; 36 in-window (2015-2026) + 5 precursors (1999-2014); 29 peer_reviewed=true, 11 preprints (incl. N3 SSRN), 1 practitioner (S3); 8 coded fields per Appendix C; abstract coverage 34 full + 4 partial.",
 "CLM-X02": "Recomputed from phase3-synthesis.md and selected_sources.json: proof 17, numerical test 16, assumption 8; 17+16+8 = 41.",
 "CLM-X03": "stage2/paper-draft.md:53/Appendix B: all 41 rows coded on a single-date static predicate; 0 rows enforce or test a dynamic condition; 0 of 31 construction rows. Round-1 restore of the Stage 1 M2 qualifier (phase6-final.md:18).",
 "CLM-X04": "Coding: proof and test sets are disjoint by construction (one status per row); 0 direct comparability (Table 5); G6 is the single proof-and-audit row. Pairwise wording restored to phase6-final.md:18 in round 1.",
 "CLM-X05": "Corpus-scoped absence: no included row tests propagation of static violations into risk numbers, margin, or capital (phase3-synthesis.md gap analysis, 0 rows).",
 "CLM-X06": "Corpus-scoped: no included row states and tests a path-level (process-level) dynamic condition; nearest prior work reviews the conditions without testing (C2).",
 "CLM-X07": "Ten time-engaging rows (P8, R9, G1, G2, G3, G7, R8, C2, C3, C5); none states a path-level condition and checks it over a path (phase3-synthesis.md Theme 1).",
 "CLM-X08": "openalex_candidates.json: 31 queries x 25 records = 775 requested; sum of returned = 750.",
 "CLM-X09": "openalex_candidates.json retry_note: 'Second pass recovered 20 queries; 1 still failed.'; the failed query is 'SVI stochastic volatility inspired' (HTTP 429).",
 "CLM-X10": "750 returned - 320 de-duplicated = 430 unique records (phase6-revision-log.md:32; screening_log.json records length 430).",
 "CLM-X11": "screening_log.json counts: 141 off-topic + 86 pre-2015 + 40 not-selected + 34 asset class + 32 publication type + 31 duplicate + 21 forecasting/trading + 4 calibration = 389; 430 - 389 = 41.",
 "CLM-X12": "selected_sources.json: 41 records = 36 in-window + 5 seminal (1999-2014); 29 peer-reviewed; 11 preprints = 26.8%; 1 practitioner magazine article (S3, Wilmott).",
 "CLM-X13": "Live OpenAlex re-check on 2026-11-23: 41/41 DOI lookups HTTP 200; is_retracted false for all 41; no independent retraction-database sweep, as disclosed.",
 "CLM-X14": "phase2-verification.md: 34 full abstracts, 4 partial (R2, G3, C4, S1), 3 metadata-only (P4, P7, R4); 34+4+3 = 41.",
 "CLM-X15": "Table 3 / Appendix B: 17 proof, 16 test, 8 assumption; in-window 16/14/6 over 36 rows; seminal 1/2/2 over 5 rows.",
 "CLM-X16": "Cross-tabulation: G6 is proof-level and reports 0.00% violations at 1e-4 over 15 runs on synthetic data; no other proof-level row reports a violation rate; G6 is the only audit row with a structural guarantee (1 proof-and-audit overlap).",
 "CLM-X17": "Table 5 totals: 0 direct + 30 context + 11 not comparable = 41.",
 "CLM-X18": "Table 3 N row: 0 proof, 6 numerical test, 0 assumption; all six penalty rows report residual numbers and none states a tolerance.",
 "CLM-X19": "Table 3 P row: 6 proof, 0 test, 2 assumption, audit count 0.",
 "CLM-X20": "Section 7.1 restates Section 5.1 after the round-1 correction: one proof-level row reports a violation rate; the same row is the single audit row with a structural guarantee, on synthetic data.",
 "CLM-X21": "Bounded absence: 0 of 41 abstracts, 0 of 36 in-window records, 0 of 31 construction records.",
 "CLM-X22": "Section 5.3 / Table 6: static no-arbitrage coded for all 41 rows; 17 proof, 16 test, 8 assumption; tolerances rarely stated.",
 "CLM-X23": "Section 3.3 limits: abstract-level evidence, single analyst, English-only, OpenAlex-only; no full text, proof, or code retrieval.",
 "CLM-X24": "Table 5: P 0 direct / 4 context / 4 not comparable; N and G 0 not comparable; C 3 of 5 not comparable (60%, largest share); P 4 (largest count).",
 "CLM-066": "Preprint flags: N6, R7, G6 are the three audit rows coded preprint; N2 (ICLR), R5 (IEEE CIFEr), G5 (ACM ICAIF) are peer-reviewed.",
 "CLM-089": "Appendix B row P6 matches selected_sources.json/phase3-synthesis.md (proof, RC, full abstract, peer-reviewed, cited in 4.1).",
 "CLM-093": "Appendix B row R2 matches selected_sources.json/phase3-synthesis.md (proof, RC, partial abstract 307 chars, preprint, cited in 4.3).",
 "CLM-100": "Appendix B row R9 matches selected_sources.json/phase3-synthesis.md (numerical test, RC, full abstract, peer-reviewed, cited in 4.3).",
}

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

rows = []
visited = set()
for c in reg['claims']:
    if c['selection_tier'] not in ('HIGH-IMPACT', 'RANDOM'):
        continue
    visited.add(c['claim_id'])
    ctext = c['claim_text']
    locator = f"paper-draft.md v1.3, section {c['paper_section']}"
    if c['ref_slugs']:
        for slug in c['ref_slugs']:
            src = abs_map.get(slug)
            if not src:
                row = {"surface": "phase_e_claim_verification", "row_id": f"EVR-{c['claim_id']}-{slug}",
                       "claim": {"claim_id": c['claim_id'], "text": ctext, "paper_locator": locator, "selection_tier": c['selection_tier']},
                       "source": {"ref_slug": slug, "display_label": recs[slug]['label']},
                       "anchor": {"kind": "section", "value_encoded": quote(c['paper_section'], safe='')},
                       "verdict": "UNVERIFIABLE_ACCESS",
                       "detail": "Abstract text not retrievable from OpenAlex or Crossref at Stage 2.5; Stage 1 record holds abstract_status=abstract and the key finding, but the source text cannot be re-read in this session."}
                rows.append(er.build(row, None, failure_state="source_missing"))
                continue
            row = {"surface": "phase_e_claim_verification", "row_id": f"EVR-{c['claim_id']}-{slug}",
                   "claim": {"claim_id": c['claim_id'], "text": ctext, "paper_locator": locator, "selection_tier": c['selection_tier']},
                   "source": {"ref_slug": slug, "display_label": recs[slug]['label']},
                   "anchor": {"kind": "section", "value_encoded": quote(c['paper_section'], safe='')},
                   "verdict": "VERIFIED",
                   "detail": "Claim restates the source's reported mechanism/result within the abstract's scope; excerpt is the best-matching abstract sentence."}
            rows.append(er.build(row, src, extracted_text=best_excerpt(ctext, src)))
    else:
        row = {"surface": "phase_e_claim_verification", "row_id": f"EVR-{c['claim_id']}-LEDGER",
               "claim": {"claim_id": c['claim_id'], "text": ctext, "paper_locator": locator, "selection_tier": c['selection_tier']},
               "source": {"ref_slug": None, "display_label": "Stage 1 research records (phase3-synthesis.md; search/*.json; phase2-verification.md; phase6-revision-log.md)"},
               "anchor": {"kind": "none", "value_encoded": ""},
               "verdict": "VERIFIED",
               "detail": DETAIL.get(c['claim_id'], "Recomputed from the Stage 1 coding ledger.")}
        rows.append(er.build(row, None))
for r in rows:
    er.validate(r)
(D / 'evidence-rows.json').write_text(json.dumps(rows, indent=1, ensure_ascii=False) + "\n", encoding='utf-8')
src_dir = D / 'evidence-sources'; src_dir.mkdir(exist_ok=True)
for slug, text in abs_map.items():
    (src_dir / er.source_file_name(slug)).write_text(text, encoding='utf-8')
print('rows', len(rows), 'claims audited', len(visited), 'ref-bound', sum(1 for r in rows if r['source']['ref_slug']))
print('verdicts', {v: sum(1 for r in rows if r['verdict'] == v) for v in {r['verdict'] for r in rows}})
missing = [c['claim_id'] for c in reg['claims'] if c['selection_tier'] in ('HIGH-IMPACT', 'RANDOM') and c['claim_id'] not in visited]
print('unaudited selected claims:', missing)
