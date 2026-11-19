# Stage 2.5 — Integrity Verification (Pre-Review)

**Manuscript:** `stage2/paper-draft.md` (v1.2)  
**Date:** 2026-11-19  
**Agent:** `integrity_verification_agent` (bounded e2e run)

## Verdict

**PASS — bounded coverage.** The checks that could be run found no fabricated reference, no retracted source, no orphan citation, and no contradicted high-impact claim. Three checks were not possible at full coverage: 100% Semantic Scholar batch verification (HTTP 429), full-text verification, and plagiarism/COI audit. These are recorded as advisories, not converted into a clean 100% claim.

## Phase A — Reference verification

| Check | Result | Status |
|---|---|---|
| References resolved | 40/40 through OpenAlex DOI/title lookup | Pass |
| DOI resolution | 39/40; 1 HAL record (Guo et al., 2016) with repository URL | Pass with note |
| Fabricated references | 0 | Pass |
| Retracted references | 0 flagged by OpenAlex `is_retracted` | Pass |
| Semantic Scholar Tier 0 batch | Not completed: 10/10 requests HTTP 429 | **Advisory** |
| WebSearch 100% check | Not performed | **Advisory** |
| Title-level-only source | Horvath et al. (2021); cited only in scope/dynamic discussion | Pass with note |
| Preprints | 10/40, labeled; not peer-reviewed | Advisory |

Reference-level detail: `../phase2-verification.md` and `../search/selected_sources.json`. The earlier Phase 5 ethics review spot-checked 20/40 metadata records and found 0 mismatches.

## Phase B — Citation context

Twelve high-impact claims were sampled across the abstract, findings, and conclusion. Each was checked against the cited source's abstract and the synthesis claim-intent record.

| Sampled claim | Support | Verdict |
|---|---|---|
| SVI/SSVI provide explicit static no-arbitrage conditions | Gatheral & Jacquier (2014); Guo et al. (2016); Martini & Mingone (2022) | Supported, abstract-level |
| Neural/generative methods use four enforcement mechanisms | Yang et al. (2017); Ackerer et al. (2019); Cohen et al. (2020); Ning et al. (2023); Vuletić & Cont (2025) | Supported, abstract-level |
| Dynamic no-arbitrage is under-tested | Cont & Vuletić (2023); Cohen et al. (2023); Andrès et al. (2026) | Supported, corpus-scoped |
| No shared benchmark identified in retrieved abstracts | Ruf & Wang (2020); Table 3 | Supported with scope qualifier |
| 30 peer-reviewed / 10 preprints | `selected_sources.json` | Supported |
| 28 recent / 12 older | `selected_sources.json` | Supported |
| 35 full / 4 partial / 1 title-level abstract | abstract coverage log | Supported |
| Horvath speed claim removed | v1.2 §4.3 | Supported |
| CP-004 indirect | v1.2 Table 4 note | Supported |
| Seven-dimension matrix is a proposal | v1.2 §5.3/§5.4 | Supported |
| No method ranking | v1.2 §1.5/§5.4/§6 | Supported |
| AI-use disclosure | v1.2 Declarations | Supported |

No sampled citation was contradicted by its source at the abstract level. One claim (the “no shared benchmark” finding) is a corpus-scoped negative finding and is worded accordingly.

## Phase C — Data and numerical consistency

- No original empirical data; no statistical tests, effect sizes, or p-values.
- Corpus counts (40; 30/10; 28/12; 35/4/1; 18/8/7/6/1) match `search/selected_sources.json` and `../phase2-verification.md`.
- Table 1–6 values are descriptive; no column sums or percentages beyond the stated counts.
- Search flow: 351 unique → 40 included; 311 not individually coded; no full-text screen. The flow is a rationale, not a PRISMA-compliant audit.
- No fabricated numerical result was found.

## Phase D — Originality

- No plagiarism scan was performed; the environment has no institutional similarity checker. **Advisory.**
- The paper is an original synthesis of the 40 sources; the taxonomy and matrix are the author's interpretive proposals.
- No text is copied verbatim beyond short standard terms; the synthesis was written for this paper.
- The 40 sources are cited; no ghost authorship or undisclosed source was found.

## Phase E — Claim verification and AI-failure checklist

| 7-mode failure | Finding |
|---|---|
| Fabricated citation | 0/40; all resolved |
| Numerical drift | 0 mismatches in corpus counts |
| Overclaim | Hedged; “no shared benchmark” is corpus-scoped; no ranking |
| Citation-context mismatch | 0 in 12 sampled claims |
| Scope drift | Disclosed: single database, abstract-level, 10 preprints |
| Simulated audit | Not simulated; S2/COI/plagiarism gaps are disclosed |
| Ghost reference | 0 |

## Advisories carried to Stage 3

1. Semantic Scholar was rate-limited; the 100% Tier 0 batch was not completed.
2. Full texts were not read; method-level claims are abstract-level.
3. No plagiarism or COI audit; disclose in the paper and the Stage 5 process record.
4. 10/40 sources are preprints.
5. The screening flow is a rationale, not a record-level audit.

## Decision

**PASS for Stage 3** with the five advisories above. The pass is bounded: it certifies the checks performed, not the checks that were unavailable. Stage 3 reviewers should treat the abstract-level and preprint limits as explicit scope conditions.
