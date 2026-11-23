# Academic Integrity Verification Report

**Pipeline stage:** Stage 2.5 INTEGRITY (pre-review) · **Mode:** 1 (Initial Verification)
**Run:** `examples/dsh/iv-surface-review-v047` · **ARS:** v3.24.4 (vendored authority) · **Date:** 2026-11-23
**Target manuscript:** `stage2/paper-draft.md`, v1.3 after this pass (was v1.2, 7,629 body words)
**Verdict:** **PASS WITH NOTES**

Mode 1 ran all five phases from scratch against the vendored v3.24.4 protocol: Phase A over all 41 references, Phase B over all 41 cited sources (100%, protocol floor 30%), Phase C over every statistical surface, Phase D over 77/77 body paragraphs (100%, floor 30%), Phase E over 25 HIGH-IMPACT + 10 RANDOM claims (35 of 142 registered claims). Ten issues were found (7 MEDIUM, 3 MINOR), all mechanically corrected in round 1 and re-verified in round 2. Remaining items are notes only, so the verdict is PASS WITH NOTES.

## Verification Summary

| Check | Result | Issues |
|---|---|---|
| Reference existence (A1) | 41/41 VERIFIED (live DOI resolution, 2026-11-23) | 0 |
| Bibliographic accuracy (A2) | 41/41 accurate (title/year/first author/DOI/authors-year/title/biblio compared field by field) | 0 |
| Ghost citations (A3) | 112 inline markers, 41 distinct IDs, 0 dangling, 0 orphan, 0 unknown slug | 0 |
| Citation context accuracy (B1) | 41/41 sources checked at sentence level | 1 MINOR (1 note) |
| Statistical data accuracy (C1) | 17 checks (14 headline quantities + 3 derived statements); 5 mismatches | 5 MEDIUM |
| Internal consistency (C2) | Tables 1–6 vs body vs abstract vs appendices | 2 MEDIUM, 2 MINOR |
| Figure/table caption fidelity (C3) | 2 schematic figures + 6 tables traced | 0 (note) |
| Experiment provenance (C4) | PASS WITH NOTE (declaration not persisted in run dir) | 0 (note) |
| Originality (D1) | 77/77 paragraphs; max shared 8-gram with any source abstract = 0 | 0 |
| Self-plagiarism (D2) | no prior publication of this text; only its own earlier draft | 0 |
| Claim verification (E) | 35 claims audited: 25 HIGH-IMPACT, 10 RANDOM; 142 registered | 0 (1 access note) |

## Scope and materials

Read (verification inputs): `stage2/paper-draft.md`; Stage 1 records `phase1-scoping.md`, `phase2-bibliography.md`, `phase2-verification.md`, `phase3-synthesis.md`, `phase6-final.md`, `phase6-revision-log.md`; `search/selected_sources.json`, `search/openalex_candidates.json`, `search/screening_log.json`, `search/retrieval_log.json`, `search/crossref_abstracts.json`; Stage 2 records `stage2/phase0-config.md`, `stage2/phase1-literature.md`, `stage2/phase2-outline.md`, `stage2/phase3-argument.md`, `stage2/phase5-abstracts.md`, `stage2/phase5-citations.md`, `stage2/phase6-review.md`.

Authority read: `skills/academic-pipeline/agents/integrity_verification_agent.md`, `skills/academic-pipeline/references/claim_verification_protocol.md`, `skills/academic-pipeline/references/ai_research_failure_modes.md`, `skills/academic-pipeline/SKILL.md` § Stage 2.5 (incl. the 3-round FAIL-loop rule). Stage 4.5-only revision-drift scripts were not used: no prior revision exists.

Scripts run: `scripts/claim_registry_coverage.py` (build, report, `--validate-report` replay), `scripts/evidence_rows.py` (via a thin builder at `stage2.5-artifacts/build_evidence_rows.py`), `stage2/measure_words.py`. Verification-only network retrieval: 41 live OpenAlex `works/doi:` lookups and abstract re-fetch for Phase D/E (disclosed under Tool limitation).

## Phase A — References

Verdict: **no issues.**

- Existence: all 41 DOI links re-resolved live through `https://api.openalex.org/works/doi:<DOI>`; HTTP 200 for 41/41; DOI echo identical; title, year and first-author surname match for 41/41. No NOT_FOUND, no MISMATCH, no gray-zone phrasing.
- Retraction: `is_retracted` false for 41/41. The paper discloses that no independent retraction-database sweep was performed (`stage2/paper-draft.md:137`), matching `phase2-verification.md`.
- Corpus match: 41 reference entries map one-to-one to the 41 frozen-corpus records by DOI; 0 orphan entries, 0 uncited records, 0 unknown slugs; 112 inline `<!--ref:ID-->` markers, every one carrying an `<!--anchor:section:…-->`; all 41 published years agree with the record set (5 seminal 1999–2014 + 36 in-window 2015–2026); the 11 records coded `preprint` are exactly P7, P8, N3, N5, N6, R2, R6, R7, R8, G6, C2.
- Bibliographic accuracy: 41/41 entries agree with the Stage 1 APA strings and record fields. Two records-side deltas were examined and dismissed as not paper defects: N3 (`selected_sources.json` `biblio` "33, 11552–11563" is the NeurIPS 2020 printed version; the paper correctly cites the SSRN version, matching `phase2-bibliography.md:196`) and R9 (record "12(2), 69–69" vs the paper's APA article-number form "12(2), 69.").
- Two venue deltas (N5, N6 list arXiv while OpenAlex primary location is RePEc) reproduce the documented Stage 1 convention at `phase2-verification.md:75`; no defect.

## Phase B — Citation context

Verdict: **1 MINOR** (fixed).

Coverage: all 41 sources' statements checked (source-level 100%), plus 15 sentences carrying absolute, comparative or generalization language re-read verbatim against the records. Zero quote drift: the manuscript contains no verbatim quotation of any source (no block quotes; all quotation marks are scare quotes, table headers, or the literal OpenAlex query string), so no wording to drift.

- IL-MINOR-1 (fixed): §4.2 attributed to N3 that it "treats residual violations as a data-quality signal rather than as a guarantee" (`stage2/paper-draft.md:181`). No Stage 1 record says this; the records say only that its penalty "is not a guarantee" and that the authors "report gains on sparse or erroneous quotes" (`phase6-final.md:160`). Rewritten to the supported statement.
- Definitional-citation note: see N-7 (C2 framed as the source of the filtered-probability-space formulation).
- No unsupported "explicitly / no evidence / all literature" generalization survives. G7's "explicitly disclaims a dynamic-arbitrage guarantee" is supported three times in Stage 1 (`phase3-synthesis.md:48`, `:113`, `:176`); the corpus-scoped absence statements remain bounded ("0 of 41 abstracts, 0 of 36 in-window records"); §6.2 uses search-bounded wording (see ADV-E5-1).

## Phase C — Statistical and data checks

Verdict: **7 MEDIUM + 2 MINOR** (all fixed): five statistical-data mismatches, two internal-consistency contradictions, two count/qualifier defects.

C1 — recomputation of the 14 headline quantities against `search/*.json` and the Stage 1 records, plus three derived statements. Seventeen checks, five mismatches:

| Quantity in the paper | Recomputed | Source | Outcome |
|---|---|---|---|
| 41 sources; 36 in-window + 5 seminal | 41; 36 + 5 | `selected_sources.json` years | ✓ |
| 29 peer-reviewed / 11 preprints (26.8%) / 1 practitioner | 29 / 11 (26.83%) / 1 | `peer_reviewed`, `flags` | ✓ |
| 8 coded fields | 8 | Appendix C | ✓ |
| Families 8/6/9/8/5/5 | 8/6/9/8/5/5 | `family_abbr` | ✓ |
| Abstracts 34 full / 4 partial / 3 metadata-only | 34/4/3 | `abstract_status` | ✓ |
| 775 requested, 750 returned, 21 first-pass 429s, 20 recovered | 31×25 = 775; Σ returned = 750; retry note "recovered 20; 1 still failed" | `openalex_candidates.json` | ✓ |
| 750 − 320 = 430 unique | 430 records | `screening_log.json` | ✓ |
| 430 − 389 = 41 included | 141+86+40+34+32+31+21+4 = 389; 430−389 = 41 | `screening_log.json` | ✓ |
| Evidence 17/16/8; in-window 16/14/6; seminal 1/2/2 | 17/16/8; 16/14/6; 1/2/2 | matrix + `selected_sources.json` | ✓ |
| Quality A 11 / B 13 / C 17 | 11/13/17 | `quality_level` | ✓ |
| Comparability 0 direct / 30 context / 11 not comparable | Table 5 totals 0/30/11 = 41 | `phase3-synthesis.md` | ✓ |
| 0 of 41 dynamic; 10 rows engage time; 0 of 31 construction | 0 / 10 / 0 | Theme 1 + matrix | ✓ |
| de-duplication "removed more records than screening did" | removed 320 < excluded 389 | `phase6-revision-log.md:32` | ✗ IL-MEDIUM-1 |
| "Seven further queries in the 'neural' group"; "densest overlap" | neural group has 6 queries; shared-hit share rank broad .92 > penalty .88 > dynamic .78 > generation .61 > neural .46 | `openalex_candidates.json` strata + `queries` lists | ✗ IL-MEDIUM-7 |
| "four of the six audit rows are preprints" | N2 ICLR, R5 IEEE CIFEr, G5 ACM ICAIF are peer-reviewed → three preprints (N6, R7, G6) | `selected_sources.json` flags | ✗ IL-MEDIUM-4 |
| "no source states data, metric and tolerance together" | G6 states all three (synthetic SVI slices, violation rate and RMSE, 1e-4); Stage 1 wording is "no two studies" | G6 record, `phase6-final.md:18` | ✗ IL-MEDIUM-5 |
| "repair and conditions groups carry the largest share" | compare P 4/8 = 50%, R 3/9 = 33%, C 3/5 = 60%; largest count P 4, largest share C | Table 5 | ✗ IL-MEDIUM-3 |

C2 — internal consistency: two contradictions beyond the table/body mismatches above.
- IL-MEDIUM-2: §5.1 (`:213`) and §7.1 (`:331`) said "among the 17 proof-level rows, none reports a violation rate on its own output", contradicting their own next clause (the one audit row with a structural guarantee), Table 3 (audit 6 incl. G6), §4.4 (G6 reports 0.00% at 1e-4) and Appendix C's own list ("1 proof-and-audit overlap"). Corrected in both places.
- IL-MEDIUM-6: Appendix C (`:469`) defined SC1–SC5 with a condition list that contradicts §2.1 (`:53`) and `stage2/phase2-outline.md:112-116`. The Appendix list was replaced with the §2.1 definitions.
- IL-MINOR-2: §4.3 (`:195`) "Two rows assert transformations … and one expands the scope" implies three assumption-level repair rows; Table 3 and Appendix B code two (R8, R4). Corrected to "One row … and another …".
- IL-MINOR-3: the abstract dropped the Stage 1 qualifier "As reported in the abstracts" while three coded rows (P4, P7, R4) are metadata-only, so the sentence read as a full-text claim. Restored in both languages.
- Tables 1–6, Section 5 cross-tabulations, Hypothesis adjudication and the appendix row codes were recomputed cell by cell against `phase3-synthesis.md` and `selected_sources.json`: 0 remaining mismatches. Abstract (EN/ZH) numbers agree with the body after correction.

C3 — caption fidelity: Figure 1 (four loci) is a framework diagram with no data extract; Figure 2 (PRISMA-style flow) reproduces 775/750/430/389/41, all traced to `openalex_candidates.json` and `screening_log.json`; Tables 1–6 all trace to records; limitations are visible in §6.4. PASS WITH NOTE: schematic figures carry no extractable values.

C4 — experiment provenance: the run is treated as post-#260. No `experiment_intake_declaration` artifact exists anywhere in the run directory (grep for `no_experiments_declared`, `experiment_intake`, `declared_by`, `intended_evidence_kind` returns nothing). The no-experiments status therefore rests on the Stage 2.5 task brief, and the manuscript heuristic was checked directly: no first-person experimental outcome (grep for "we ran/conducted/trained/measured/observed/found/report/tested" and "our experiment/results/dataset/model" → 0 hits), no Methods text describing experiments as performed (§3 describes a literature search and screening only). FAIL condition (4) is not met; condition (1) cannot be positively satisfied without the passport, recorded as note N-6 and as a residual unknown rather than silently passed.

## Phase D — Originality

Verdict: **0 CRITICAL / 0 SERIOUS / 0 MODERATE**.

Method: 77/77 body paragraphs (>25 words) compared against the 36 re-fetched source abstracts by 8-word shingle overlap; 0 overlapping paragraph–source pairs; no block quotes; no verbatim quotations of any kind (the manuscript states that all anchors are `section:`-kind and none is a quotation, which this check reproduces).

| Grade | Count | Notes |
|---|---|---|
| VERBATIM (20+ identical words, unquoted) | 0 | — |
| CLOSE_MATCH | 0 | — |
| PARAPHRASE | 0 | max shared 8-gram = 0 |
| COMMON_KNOWLEDGE | definitional sentences only | SC1–SC5, APA-style reference list |
| ORIGINAL | all 77 sampled paragraphs | synthesis, framework, coding tables |

D2 self-plagiarism: not applicable — this text has been published nowhere; the only sibling text is its own previous draft (`stage2/paper-draft-v1.md`), and the v1→v1.3 delta is the edit table below.

Limitation: 5 of 41 sources have no abstract text available for comparison at Stage 2.5 (P4, P7, R4 are metadata-only by Stage 1 design; N1 and C1 abstracts were not retrievable from OpenAlex or Crossref now). Their statements were checked against Stage 1 records only, not against source text.

## Phase E — Claim verification

Registry: `stage2.5-artifacts/claim-registry.json` (142 claims = 25 HIGH-IMPACT, 10 RANDOM, 107 NOT-SELECTED); coverage report `stage2.5-artifacts/claim-registry-coverage.json`; replay `claim-registry coverage replay: PASS`.

**Claim Registry Coverage sidecar (#737)**

| Field | Value |
|---|---|
| Status | completed |
| Registry path / SHA-256 | `stage2.5-artifacts/claim-registry.json` / `2d0da6643759f288c36d3d29568f052736722753a914173f7649f95e932110da` |
| Coverage report path / SHA-256 | `stage2.5-artifacts/claim-registry-coverage.json` / `6166752b2f17c7c80541f436e267538b596b56646dc8617641ec516fde4c8937` |
| Draft binding SHA-256 | `b19f4acbf9ffb39cb164b0dcf3b7824a4e4f9e274d8c8e9780b09b73bd241033` |
| Candidate scope | 118 bounded candidates (citation-bearing + quantitative sentences); 118 `registry_span_matched`; 24 registered claims outside candidate classes |
| Candidate-unregistered count | 0 |
| Semantic extraction coverage | `not_machine_detectable` |

**Persisted evidence rows (#656)**

| Field | Value |
|---|---|
| Artifact | `stage2.5-artifacts/evidence-rows.json`, schema `evidence-row/1.0`, surface `phase_e_claim_verification` |
| Rows | 43 (42 VERIFIED, 1 UNVERIFIABLE_ACCESS); excerpts 14 `agent_extracted`, 28 `anchorless`, 1 `source_missing` |
| Claims audited / reconciled | 35 distinct `claim_id` = E_claims.checked; 34 distinct VERIFIED = E_claims.verified |
| Source texts | `stage2.5-artifacts/evidence-sources/` (36 files written with `source_file_name(slug)`) |
| Coverage | 15 ref-bound (claim, ref_slug) pairs all have rows; no row cap, dedup, reorder or truncation |
| CLI validation | `validate stage2.5-artifacts/evidence-rows.json --source-dir stage2.5-artifacts/evidence-sources` → `PASS: 43 evidence row(s)` |

| Verdict | Claims |
|---|---|
| VERIFIED | 34 |
| MINOR_DISTORTION | 0 |
| MAJOR_DISTORTION | 0 |
| UNVERIFIABLE | 0 |
| UNVERIFIABLE_ACCESS | 1 (CLM-073 / C1) |

Sampling: 25 HIGH-IMPACT (100% of the high-impact tier), 10 RANDOM (10% of the remaining 117, rounded up), 0 TOP-UP needed (35 ≥ 10).

**Advisories**

| ID | Kind | Finding |
|---|---|---|
| ADV-E4-1 | Scope conformance | All coded claims stay inside the frozen scope (equity-index listed options, 2015-01-01–2026-11-23, English; 5 declared precursors). No SCOPE-BROADENED row. |
| ADV-E5-1 | Novelty/absence | The absence claim is search-bounded (§6.2 "To our knowledge, based on searches of OpenAlex covering 2015-01-01 to 2026-11-23…"), names the database and date range, and acknowledges the nearest prior work (Niu, 2015) → SUPPORTED_WITHIN_SEARCH. No global-absence claim. |
| E6 | Claim-strength drift | `[E6-SKIPPED: no revision evidence]` — first-pass audit; persisted as `skipped_no_revision_evidence`, findings `[]`. |
| ADV-REV | Revision drift | Not applicable: no prior revision exists; Stage 4.5-only scripts intentionally not used. |

## Issue list

| ID | Severity | Location | Issue | Status |
|---|---|---|---|---|
| IL-MEDIUM-1 | MEDIUM | `stage2/paper-draft.md:103` | Claimed de-duplication removed more records than screening; 320 < 389, contradicted by its own Table 1 | Fixed |
| IL-MEDIUM-2 | MEDIUM | `:213`, `:331` | "None of the 17 proof-level rows reports a violation rate" contradicted G6 (proof-level + audit, 0.00% at 1e-4) and Appendix C's "1 proof-and-audit overlap" | Fixed |
| IL-MEDIUM-3 | MEDIUM | `:241` | "Repair and conditions groups carry the largest share of not-comparable rows" contradicted Table 5 (largest share C 3/5, largest count P 4) | Fixed |
| IL-MEDIUM-4 | MEDIUM | `:217` | "Four of the six audit rows are preprints" — records give three preprints (N6, R7, G6) | Fixed |
| IL-MEDIUM-5 | MEDIUM | `:13`, `:21` | Abstract strengthened Stage 1's "no two studies" to "no source" although G6 states data, metric and tolerance | Fixed |
| IL-MEDIUM-6 | MEDIUM | `:469` | Appendix C's SC1–SC5 list contradicted §2.1 and `stage2/phase2-outline.md:112-116` | Fixed |
| IL-MEDIUM-7 | MEDIUM | `:103` | "Seven further queries" in the neural group (there are six), and "densest overlap" unsupported by any hit-count or shared-hit measure | Fixed |
| IL-MINOR-1 | MINOR | `:181` | N3 "treats residual violations as a data-quality signal" not stated in any record | Fixed |
| IL-MINOR-2 | MINOR | `:195` | "Two rows … and one" implied three assumption-level repair rows; coded count is two | Fixed |
| IL-MINOR-3 | MINOR | `:13`, `:21` | Abstract dropped the "As reported in the abstracts" qualifier while 3 of 41 rows are metadata-only | Fixed |

Counts: SERIOUS 0 · MEDIUM 7 · MINOR 3 · notes 7 (+4 advisory rows).

## Corrections applied (mechanical, traceable)

| # | Location | Before → After |
|---|---|---|
| 1 | `:5` | `**Version:** v1.2 (Phase 6 revision round 1)` → `**Version:** v1.3 (Stage 2.5 integrity corrections)` |
| 2 | `:13` | "In all 41 rows the certified object is a single date's surface" → "As reported in the abstracts, the certified object in all 41 rows is a single date's surface" |
| 3 | `:13` | "and no source states data, metric and tolerance together" → "and no two sources state data, metric and tolerance together" |
| 4 | `:21` | "41篇所认证的对象全部是单一交易日的曲面" → "据摘要所载，41篇所认证的对象全部是单一交易日的曲面" |
| 5 | `:21` | "且没有任何一篇同时给出数据、度量与容差" → "且没有任何两篇同时给出数据、度量与容差" |
| 6 | `:103` | "Seven further queries in the "neural" group and six in the "generation" group produced the densest overlap, which is why de-duplication removed more records than screening did." → "The six "neural" and six "generation" queries produced the largest hit volumes (150 and 149), which is why de-duplication removed 320 records — still fewer than the 389 that screening excluded." |
| 7 | `:181` | "and treats residual violations as a data-quality signal rather than as a guarantee" → "and the penalty is not a guarantee" |
| 8 | `:195` | "Two rows assert transformations" → "One row asserts transformations" |
| 9 | `:195` | "and one expands the scope" → "and another expands the scope" |
| 10 | `:213` | "among the 17 proof-level rows, none reports a violation rate on its own output, and among the six audit rows, only one also reports a structural guarantee" → "among the 17 proof-level rows, only one reports a violation rate on its own output, and among the six audit rows only that row also reports a structural guarantee" |
| 11 | `:217` | "four of the six audit rows are preprints or working papers" → "three of the six audit rows are preprints (N6, R7, G6)" |
| 12 | `:241` | "the repair and conditions groups carry the largest share of not-comparable rows" → "the conditions group carries the largest share of not-comparable rows (three of five) and the parametric group the largest number (four of eight)" |
| 13 | `:331` | "and none reports a violation rate on its own output" → "and only one reports a violation rate on its own output" |
| 14 | `:469` | Appendix C's SC1–SC5 parenthetical ("butterfly convexity … Lee's moment bounds …") → "(non-negative time value, monotone decreasing call prices in strike, strike convexity, the zero-maturity limit, and calendar monotonicity of total variance)" |

Word count: `stage2/measure_words.py stage2/paper-draft.md` → **7,641 body words** (v1.2: 7,629; +12). Method: HTML comments stripped, count limited to `## Draft Body` … `## Declarations`, excluding headings, table rows, fenced code and caption lines. Still inside the 8,000-word ceiling (`stage2/phase0-config.md`).

## Round log (3-round FAIL loop)

| Round | Pass | Issues | Outcome |
|---|---|---|---|
| 1 | Initial from-scratch Stage 2.5 | 10 (7 MEDIUM, 3 MINOR) | **FAIL** → correction list, edits 1–14 applied |
| 2 | Re-verification of corrected items + whole C2 re-run (tables, counts, abstract vs body, registry rebuild, evidence rows) | 0 | **PASS WITH NOTES** |

Rounds used: 2 of 3. The FAIL loop did not need exhaustion, so no user decision is required for this checkpoint.

## AI Research Failure Mode Checklist (v3.2)

| # | Mode | Outcome | Evidence | Blocks? |
|---|---|---|---|---|
| 1 | Implementation bug passing AI self-review | NOT APPLICABLE | No experiments declared (literature synthesis); no analysis code produces manuscript numbers — the only scripts are retrieval/screening. Independent recomputation of every reported aggregate found only reporting errors, all fixed (IL-MEDIUM-1, -4, -7). | No |
| 2 | Hallucinated citation | CLEAR | 41/41 DOI resolutions live, 41/41 bibliographic match, 112 markers all resolve to the frozen corpus, 0 orphan/dangling/unknown, 0 retracted. | No |
| 3 | Hallucinated experimental result | NOT APPLICABLE | No experiments; every quantitative statement is a corpus count or another author's reported number, and each was recomputed (Phase C) or traced (Phase E, 42 VERIFIED rows). | No |
| 4 | Shortcut reliance | NOT APPLICABLE | No experiments, so no spurious-feature result exists; the corpus-coding analogue (single analyst, abstract-level evidence) is disclosed in §3.3/§6.4 and flagged as a Stage 4.5 re-check. | No (flag-only at 2.5) |
| 5 | Implementation bug reframed as novel insight | NOT APPLICABLE | No experiments; grep for "surprisingly", "unexpectedly", "counterintuitively", "contrary to our hypothesis" → 0 hits. | No |
| 6 | Methodology fabrication | NOT APPLICABLE | §3 describes search (31 queries, OpenAlex) and screening only, both reproduced from `openalex_candidates.json`/`screening_log.json`; no Methods text describes experiments, datasets or hyperparameters as run. | No |
| 7 | Frame-lock at early pipeline stage | CLEAR | RQ and H1–H3 were fixed before coding (`phase1-scoping.md`, `stage2/phase0-config.md`); the four-locus framework is presented as proposed, not as a finding; no "in hindsight"/"we realized" tells; coding is frozen in Stage 1 and Appendix B says no row was re-coded. | No |

No mode is SUSPECTED; no blocking outcome. The checklist therefore does not change the Phase A–E verdict.

## Notes (non-blocking)

- **N-1 UNVERIFIABLE_ACCESS:** the abstract for C1 (Neufeld & Sester, 2024) could not be re-retrieved from OpenAlex or Crossref at Stage 2.5, so its evidence row is `UNVERIFIABLE_ACCESS`. The claim it supports is corroborated by the Stage 1 record (`abstract_status: abstract`, key finding on the synthetic-data detector).
- **N-2:** N3's cited DOI is the SSRN preprint, but a peer-reviewed NeurIPS 2020 publishedVersion exists (OpenAlex W2951241921) whose volume/pages equal the record's `biblio`. Re-coding the corpus preprint count is a Stage 1 decision; the paper's entry is accurate for the cited version.
- **N-3:** the abstract's "29 peer-reviewed and 11 preprints" omits the single practitioner magazine article (S3, *Wilmott*); the abstract asserts no total, and body §3.1/Table 1 are complete.
- **N-4:** terminology drift for the same datum — "three at title level" (§1.3), "metadata-only" (Table 1, §3.2, §6.4, Appendix B), "unavailable" (§3.2). Consistent in meaning and defined once; style only.
- **N-5:** Table 6's approximate counts (~8 fit-accuracy rows, ~8 interpolation/stability rows, ~5 cost claims) are Stage 1 approximations and cannot be recomputed mechanically from abstracts.
- **N-6 (C4):** no `experiment_intake_declaration` is persisted in the run directory; the no-experiments status is taken from the Stage 2.5 brief and corroborated by the manuscript heuristic (no author-run experiments, no Methods-as-done text). If a passport later shows a different status, re-run C4.
- **N-7:** the definitional sentence at `stage2/paper-draft.md:61` ("the natural formulation is a filtered probability space …") carries a topical citation to C2 (Niu, 2015), whose abstract states only that the review "will … talk about no dynamic arbitrage". The formulation is the manuscript's own framework definition (mirrored in `phase3-argument.md:176`), and the paragraph's next sentence already cites C2 for exactly what the record supports ("discusses the question without testing it"); the citation is topical rather than a paraphrase, so it is recorded as a note, not an edit.
- **ADV-CACHE:** not applicable — no cached verification artifacts were consumed; verification used live lookups.

## Residual unknowns

1. The passport-level `experiment_intake_declaration` is not in the run dir (N-6); C4's declaration-anchored condition cannot be positively shown, only the manuscript-side heuristic.
2. Source text for 5 of 41 sources (P4, P7, R4 metadata-only; N1, C1 unavailable now) was not available for originality or claim re-reading; those statements rest on Stage 1 records.
3. No independent retraction-database sweep exists (disclosed by the paper); this check inherited that limitation.
4. Table 6's approximate counts are not machine-recomputable (N-5).
5. N5/N6 venue strings depend on the documented Stage 1 arXiv-vs-RePEc convention; a reader re-resolving those DOIs will see RePEc.

## Tool limitation disclaimer

Phase A used live OpenAlex DOI resolution, not Turnitin/iThenticate-class plagiarism tooling. Phase D used local 8-word-shingle overlap against 36 re-fetched abstracts (sampling 77/77 paragraphs = 100%), not a commercial similarity database; 5 sources had no comparable text. The abstract re-fetch for Phases D and E is verification-only retrieval, disclosed above, and was not added to the corpus.

## Verification audit trail

- Draft bound at SHA-256 `b19f4acbf9ffb39cb164b0dcf3b7824a4e4f9e274d8c8e9780b09b73bd241033` (post-correction bytes); registry `2d0da66…`; coverage report `6166752…`.
- Live DOI re-check: `https://api.openalex.org/works/doi:<DOI>` for all 41 DOIs, 2026-11-23 (41×HTTP 200, 0 retracted).
- Abstract re-fetch: OpenAlex `abstract_inverted_index`, 32 records + `search/crossref_abstracts.json` (R2, R8, G6, C2) → 36 bodies, persisted under `stage2.5-artifacts/evidence-sources/`.
- Recomputation commands: `python3 scripts/claim_registry_coverage.py --draft stage2/paper-draft.md --registry stage2.5-artifacts/claim-registry.json --output … && … --validate-report …` (replay PASS); `python3 stage2/measure_words.py stage2/paper-draft.md` (7,641).
- Sampling: references 41/41 (100%); sources 41/41 (100%); paragraphs 77/77 (100%); claims 25 HIGH-IMPACT + 10 RANDOM = 35/142.
