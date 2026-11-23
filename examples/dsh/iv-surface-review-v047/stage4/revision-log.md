# Revision Log — v1.3 → v2.0

**Manuscript:** IVSURF-2026-11-23
**Base:** `stage2/paper-draft.md` (v1.3, 7,641 body words, 41 frozen references)
**Revised:** `stage4/paper-draft-v2.md` (v2.0, 7,784 body words, same 41 references)
**Scope:** every entry below answers at least one item of the editorial decision (R1–R9 required; S1–S11 suggested). No entry requires a source outside the frozen 41.

---

## 1. Working order

The revision was written as three part-files (`_build/part1.md`, `_build/part2.md`, `_build/part3.md`) and assembled into `paper-draft-v2.md` by `_build/build.py`, which also regenerates Appendix A (query table, exclusion table) from `search/openalex_search.py` and `search/screening_log.json` and Appendix B (ledger) from the coded row table, so that no counting table is transcribed by hand. The build prints its invariants on every run:

```
citation clusters normalised: 0
appendix audit rows (temporal titles): [5, 17, 58, 111, 326, 335, 342, 393]
ledger: audit=6 time=10 dyn={'D0': 34, 'D1': 4, 'D2': 3, 'D3': 0}
rows without a body citation: []
wrote .../stage4/paper-draft-v2.md
```

---

## 2. Chronological change log

| # | Location in v2 | Change | Answers |
|---|---|---|---|
| 1 | Front matter | Version line set to `v2.0`; the `Review-criteria status: criteria_binding_unavailable` line removed; title, author, subtitle kept as in v1.3; no pipeline stage labels anywhere. | S2 |
| 2 | English Abstract; Chinese Abstract | Certified-object sentence rescoped to the 31 construction rows, with the condition/evaluation group and the seminal group explicitly not certifying a surface; composition restated as 29 peer-reviewed + 11 preprints + 1 practitioner = 41; both languages mirrored. | R1, S1 |
| 3 | §1.2 | H2 redeclared with both clauses, the fit-error clause included, and the clause disclosed as added post hoc after the first coding pass. | R5 |
| 4 | §2.1 | SC3 corrected to `∂²c/∂k² − ∂c/∂k ≥ 0` with the density derivation `C″(K) = K⁻¹e^{−k}(c″ − c′)`; relations to SC2 and to the τ = 0 slice of SC4 stated; Black–Scholes counterexample printed (k = −0.5, σ√τ = 0.2: c″ ≈ −0.53, c″ − c′ ≈ +0.07). | R6 |
| 5 | §2.2 | Dynamic-enforcement rule stated as D0–D3 with the model-class rule (inherited guarantees coded D2, never enforcement); all ten time-engaging rows named (P8, R8, G1, G2, G3, G7, C2, C3, C5, S5). | R7 |
| 6 | §2.3 | Figure 1 replaced by a labelled conceptual schematic of the triple and the four loci, with a real caption. | S2 |
| 7 | §3.1 | Replacement account corrected: two records replaced after abstract-level reading because the retained abstract did not fit the inclusion rule (no enforcement claim; FX/delta scope), and no record failed metadata resolution or abstract reconstruction; single account used here and in Appendix A.3. | R4 |
| 8 | §3.1; Figure 2 | Figure 2 replaced by a labelled retrieval/screening schematic carrying all eight exclusion-code counts and the 41-record composition. | R4, S2 |
| 9 | §3.2 | Numerical-test and audit definitions separated; audit row defined as a violation/residual/defect statistic on the row's own output; 16 audit-candidate rows vs 6 audit rows stated; metadata-only rule stated once. | R2, S4 |
| 10 | §3.2 | Evidence levels VI and VII defined and printed per row in Appendix B; composite A/B/C grade withdrawn with the reason stated. | S3, S5 |
| 11 | §3.3 | Coding handbook pointer added (Appendix D) with the three coding disciplines; comparability codes and the "ranges, not ranks" boundary restated. | R3, S4 |
| 12 | §3.4 (new) | Reliability subsection: 16-row stratified second-coder recheck, six re-coded fields, blindness, decision rule (agreement ≥ 0.85; κ ≥ 0.70 for evidence status), measured figures entered after the second-coder pass (marker removed), cell-level adjudication recorded, single-coder limitation paragraph. | R3 |
| 13 | §4.1–4.4; Table 2 | Family accounts trimmed to the word budget; Table 2 recomposed (no redundant Rows column, certified object per family); R9's row rewritten as a single-date object carrying a maturity axis. | R2, S5 |
| 14 | §5.1 | Partition recomputed and printed: 16 proof-only + 1 proof-and-audit + 5 test-and-audit + 11 test-only + 8 assumption = 41; 1 + 5 = 6 audit rows; G6 overhead disclosed from both sides; universal negative removed; dynamic count stated as 0 of 41 at D3, with D2 = 3, D1 = 4, D0 = 34. | R2, R7 |
| 15 | Table 3 | Rebuilt with `Proof / Test / Assumption / Total / Audit rows / Time-axis rows` per family; per-family rows sum to 41, 6 and 10. | R2, R7 |
| 16 | Table 4; §5.1 | H2 adjudicated on both clauses, with the post-hoc note carried in the residual-uncertainty cell. | R5 |
| 17 | §5.3; Table 6 | Coverage counts labelled as approximations where they summarise a free-text metric field; cost row marked "asserted, 0 comparable". | R8, R9 |
| 18 | §5.4 (new) | Acceptance-criterion specification: five inputs (loss, tolerance, power, regime coverage, independent check); what the corpus supplies; zero of six audit rows supply three or more; zero of 41 supply all five. | R8 |
| 19 | §6.2 | Excluded-pool audit at title level: eight temporal-vocabulary titles named by log index (5, 17, 58, 111, 326, 335, 342, 393), all under `RELEVANT_NOT_SELECTED`; statement of what the pool can and cannot support. | S9 |
| 20 | §6.3 | Seven studies ordered by dependency, each with data access and owner; power-and-noise-floor study first because four of the five §5.4 inputs depend on it; study-order constraints stated. | S8 |
| 21 | §6.4 | Audience paragraph: three adjacent audiences (model validators/supervisors, model-risk and audit functions, end investors), each with the competence it would need, neither claimed nor excluded. | S7 |
| 22 | §7.1 | Certified-object sentence scoped to the 31 construction rows; proof–audit near-disjointness stated with the single overlap; ranking claim bounded ("does not license a ranking" + common protocol would produce one). | R1, R2, S11 |
| 23 | §7.2 | Established/asserted split; build-or-buy claim bounded to what Table 6 licenses; the "worth and what it costs" phrasing withdrawn by name; reporting-cost incidence paragraph. | R9, S10 |
| 24 | Appendix A (new tables) | A.1: the 31 query strings, parsed from `search/openalex_search.py`; A.2: the 40 discretionary exclusions by log index, year, title, recorded code, with "not recorded" printed wherever the log carries no free-text reason; A.3: the single replacement account. | R4, S9 |
| 25 | Appendix B | Ledger rebuilt with 13 columns: ID, Source, Family, Evidence, Audit, Static, Time, Dyn, Level, Comp., Coverage, Peer-reviewed, Cited in Section. | R2, R3, R7, S5 |
| 26 | Appendix C (new C.1–C.5) | What was coded; seven-axis vs eight-axis instrument reconciliation; boundary cases; the SC3 correction record with the 39-row re-examination and the "no verdict changes" conclusion; the A/B/C withdrawal rationale. | R6, S2, S5 |
| 27 | Appendix D (new) | Coding handbook reproduced verbatim from `coding-handbook.md` (D.1–D.10), including the reliability protocol (D.9) and the recomputation table (D.10). | R2, R3, R7, S3, S4 |
| 28 | Whole body | Word budget brought from 10,323 to 7,784 by paragraph-level compression (abstract 249 words; Chinese 491 characters; tables 6; figures 2; references 41 unchanged). | word limit |

---

## 3. Build repairs during the revision

Two paragraph-index edits were applied to part-files after earlier deletions had shifted the indices, which overwrote a duplicate paragraph, one table block (Table 6), and two headings (`## 7. Conclusion`, `### 6.4 Limitations`). The damage was detected on the next measurement (body count rose while text was being cut; §7 disappeared from the per-section report). Repaired in place: Table 6 regenerated in its seven-dimension form (coverage rows consistent with Section 5.3's "about eight" / "about five" labels), both headings restored, duplicate drafts of the audience and framework paragraphs removed, and the build re-run until `measure-words.py` reported per-section figures that sum to the body total. The reference list was verified byte-identical afterwards (41 entries) and the reference count re-checked programmatically.

---

## 4. Verification actually run

Word count — `measure-words.py --per-section` on the built file:

```
body words = 7784
  §1  617   §2  1153   §3  1229   §4  1170
  §5 1536   §6  1303   §7   776
budget 6000-8000 (target <=7800): within
```

Citation lint — `.venv/bin/python scripts/check_v3_7_3_three_layer_citation.py stage4/paper-draft-v2.md`:

```
[v3.7.3 three-layer-citation lint] PASSED (1 file(s) scanned)
```
exit code 0.

Acronym check — `.venv/bin/python scripts/check_acronyms.py --input stage4/paper-draft-v2.md --lang en`: exit code 0, advisory only. Output tail:

```
| Body | 369 | Not defined | CRediT | 1 |
| Body | 524 | Not defined | DC | 4 |
| Body | 524 | Not defined | NC | 3 |
| Body | 524 | Not defined | RC | 3 |
| Body | 647 | Not defined | VAR | 1 |
| Body | 662 | Not defined | ID | 1 |
```

The advisory list is carried unchanged from v1.3 in kind (undefined initials such as SQ1–SQ3, DC/NC/RC, TY, VAR); no new class of note was introduced. Both checker invocations were made on the final built file, not on a part-file.

Structural checks on the final file: 6 table captions, 2 figure captions, 41 reference entries, 10 Appendix D subsections, no remaining stage-label strings ("Stage 1", "Stage 2", "Phase 7", "to be typeset").

---

## 5. Status by item

| Item | Status | One-line basis |
|---|---|---|
| R1 | fully | Abstract (both languages), §7.1 and Table 2 attach the single-date-surface claim only to the 31 construction rows. |
| R2 | fully | Definitions separated in §3.2; 16 + 1 + 5 + 11 + 8 = 41 and 1 + 5 = 6 in §5.1 and Table 3; G6 overlap stated from both sides. |
| R3 | fully | §3.3 handbook pointer, §3.4 recheck subsection with measured figures, Appendix D.9–D.10 protocol and recomputation, single-coder limit kept, absence claims restated at measured stability. |
| R4 | fully | Appendix A.1 (31 strings), A.2 (40 exclusions, "not recorded" where true), A.3 (single replacement account). |
| R5 | fully | H2 in §1.2 now carries the fit-error clause and the post-hoc disclosure; Table 4 and §5.1 adjudicate both clauses. |
| R6 | fully | §2.1 states c″ − c′ ≥ 0 with derivation and SC2/SC4 relations; Appendix C.4 records the 39-row re-examination and no verdict changes. |
| R7 | fully | §2.2 states the D0–D3 and model-class rules; Appendix B carries Time and Dyn for all 41 rows; the 0-of-41 claim is tied to that rule. |
| R8 | fully | §5.4 specifies the five inputs and states which the corpus lacks (zero of 41 supply all five). |
| R9 | fully | §7.2 separates established from asserted cost and withdraws the "worth and what it costs" phrasing; §5.3 and Table 6 agree. |
| S1 | fully | Composition now sums: 29 + 11 + 1 = 41 in both abstracts and §3.1. |
| S2 | fully | Version v2.0, no stage labels, two captioned conceptual figures replace the ASCII placeholders. |
| S3 | fully | VI/VII defined in §3.2 and printed per row in Appendix B. |
| S4 | fully | Metadata-only rule stated once and applied identically in §3.2, §5.1, Appendix B, Appendix D.8. |
| S5 | fully (withdrawal) | Appendix B rebuilt with 13 columns; A/B/C grade withdrawn rather than printed, because it is not recomputable (Appendix C.5). |
| S6 | declined | Frozen 41-source reference list; the missing canonical source is disclosed as a limitation in §6.4 and the dynamic predicate is published instead (Appendix D.5). |
| S7 | fully | §6.4 names three adjacent audiences and the competence each needs. |
| S8 | fully | §6.3 carries dependency order, data access and owner for all seven studies, power/noise-floor first. |
| S9 | fully | §6.2 audits the excluded pool at title level (eight titles by log index) and bounds the conclusion. |
| S10 | fully | §7.2 states the reporting triple's cost, who bears it, and that its effects are asserted not measured. |
| S11 | fully | §7.1 claims only that the corpus's numbers do not license a ranking, and that a common protocol would produce one. |

---

## 6. Residual risks the revision could not eliminate

1. **The reliability figures are measured but the check is designed.** Section 3.4 reports the second coder's counts (evidence status 10/16, κ = 0.47; three of six fields below the stated bar) and the evidence-status and comparability partitions are restated at that observed stability. The check still measures reproducibility of the handbook, not correctness, and the 16 rows are a designed sample.
2. **The A/B/C composite grade is gone.** A reader comparing v1.3 with v2.0 finds no per-row quality grade. Restoring it would require the two free-text criteria to be frozen into the ledger first; Appendix C.5 states the condition under which it could return.
3. **The 40 discretionary exclusions cannot be fully reconstructed.** The screening log records a free-text reason for one of the 40; Table A2 prints "not recorded" for the rest rather than reconstructing a rationale after the fact. A third party can rerun the 31 queries but cannot reproduce the discretionary selection decisions row by row.
4. **The excluded-pool audit is title-level only.** Section 6.2's finding about the eight temporal-vocabulary titles is limited by that, and the review cannot claim the excluded pool contains no dynamic test — only that no excluded title announced one.
5. **The corpus is abstract-level and single-database.** No full text, proof, or code was retrieved; retrieval was English-only, OpenAlex-only, with one query lost to HTTP 429. Every absence claim is bounded accordingly.
6. **The dynamic predicate is the review's own.** With S6 declined, Section 2.2's operationalisation of dynamic consistency has no corpus authority behind it; Appendix D.5 publishes it so that disagreement can be pointwise rather than global.
7. **The two figures are conceptual schematics.** They must still be redrawn as final artwork for typesetting; the captions are written so that redrawing changes no claim.
8. **The reliability gate is a design choice.** Agreement ≥ 0.85 with κ ≥ 0.70 is a conventional threshold, not a validation of the handbook; passing it would show reproducibility, not correctness.
9. **Word budget headroom is thin.** At 7,761 body words (v3.0) the draft sits 39 words under the internal aim and 239 under the hard limit; further copy-editing must be re-measured, not estimated.


## Stage 4′ editing corrections (v2.0 → v3.0)

| # | Location | Change | Source |
|---|---|---|---|
| 1 | §3.1 | Removed the duplicated corpus-construction paragraph (the same paragraph appeared twice, near-verbatim). | N1 (re-review) |
| 2 | Appendix D.10 | Peer-review tally corrected to 29 yes / 12 no (11 preprints plus practitioner article S3), matching Appendix B and Table 1. | N2 |
| 3 | Declarations (AI Use Disclosure) | Replaced the stale "input fields are marked for completion" sentence with the completed state: figures reported in §3.4, adjudication recorded with the coding records. | N3 |
| 4 | Abstract | "Proof-level and test-level evidence come from nearly disjoint sets" rewritten to the corrected proof/audit finding (one of six audit rows is also proof-level), consistent with §1.1, §5.1, §7.1. | N4 |

Body words: 7,862 (v2.0) → 7,761 (v3.0). Reference list, tables, figures and counts unchanged. Citation checker PASSED on v3.0.
