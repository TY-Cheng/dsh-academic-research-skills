# Phase 6 — Review Outcome (pipeline-facing summary)

**Run:** `examples/dsh/iv-surface-review-v047`, Stage 2 (WRITE), phases 4–6, ARS v3.24.4 end-to-end validation.
**Manuscript reviewed:** `paper-draft.md` v1.1 → **v1.2** after revision round 1.
**Contract pair:** `academic_paper/writer_full/v1` × `academic_paper/evaluator_full/v1`, v3.6.6 generator-evaluator gate.
**Criteria binding:** `criteria_binding_unavailable` — no author-confirmed `ReviewTargetContext`; no venue-alignment claim made at any point.

## Decision

| Field | Value |
|---|---|
| Evaluator decision as emitted (Phase 6b) | `request_revision` — fired by F2 (severity 70; mandatory dimension D3 at warn) |
| Revision rounds used | 1 of a maximum of 2 |
| Decision after round 1 | `accept` — F0 (severity 10; every mandatory dimension pass, no dimension at block) |
| Phase 7 gate | Accept for the draft going to Phase 7, so the #1087 stop does not apply; Phase 7 is out of scope for this stage and was not run |
| Calibration status | `NOT_CALIBRATED` (emitted unconditionally by every live Phase 6 report) |
| Stage 3 entry path | standard — F0 accept; exceptional path (F5) not used |

Scores, as first emitted: D1 originality **pass**, D2 methodological rigor **pass**, D3 evidence sufficiency **warn**, D4 argument coherence **warn**, D5 writing quality **pass**. Failure conditions: F1 not fired, **F2 fired**, F3 not fired, F6 not fired, F4 not fired (suppressed by F2), F5 not fired, F0 not fired at first scoring.

Scores after round 1: D1 pass, D2 pass, D3 **pass**, D4 **pass**, D5 pass. F0 fires; no block remains; the review closes as accept.

## Round 1 — issues, fixes, locations

| # | Dimension | Issue | Fix applied | Where |
|---|---|---|---|---|
| 1 | D3 | Selection counts contradicted each other: §3.1 reported four records included after abstract reading while Appendix A reported two replacements, with no reconciliation. The two-replacement version matches the Stage 1 provenance (Wiedemann et al., 2025 replacing a neural-network pricing paper; Fukasawa, 2022 replacing a foreign-exchange delta-condition paper). | Rewrote the sentence to "Two included records were replaced during abstract reading when the retrieved text showed no enforcement claim; both replacements are named in Appendix A and recorded in the run artifacts rather than presented as an algorithmic outcome." | `paper-draft.md` §3.1 (former line 103) |
| 2 | D3 | Three load-bearing Table 6 counts in §5.3 ("roughly eight rows" held-out error, "about eight rows" held-out strike or maturity behaviour, "about five rows" cost) had no per-row pointer; Appendix B's "Coverage" column is abstract coverage, not evaluation coverage. | Added one sentence stating that the counts aggregate the seventh coded field defined in Appendix C (the fit or accuracy metric a row reports) and that the per-row coding is held with the stage 1 records rather than reproduced column by column in Appendix B. | `paper-draft.md` §5.3, before "The distinction between coverage and performance is load-bearing." |
| 3 | D4 | N1 appeared as "frictionless and convex by design" and "structural rather than a soft term" while Table 3 coded all six penalty rows as numerical test, and §4.2 asserted "none is proof-level"; the coding rule that reconciles the two was stated only in Appendix C. | Added the rule in the paper's own vocabulary: "It is coded as a numerical test rather than as proof because the review credits a proof only where the abstract states a theorem over the admitted set (Appendix C), not where the shape of the function class is described as a design property." | `paper-draft.md` §4.2 final paragraph (N1 hybrid sentence) |
| 4 | D5 | §4.1 called Table 2 a summary of "the six families" although Table 2 is the four-family summary with two supporting groups. | "Table 2 summarises the four focal families on the review's dimensions, with the two supporting groups shown for completeness." | `paper-draft.md` §4.1, first paragraph |

Budget management during the round: the D4 fix and the D5 fix added words to §4, so nine micro-trims were made inside §4 (no claim, number, or citation removed) to keep §4 inside its ±15% allocation. Net effect: §3 925 → 934, §4 1,716 → 1,721, §5 1,299 → 1,341; total 7,573 → 7,629. After the round, all sections remained inside ±15% of the outline allocation and the total stayed inside the 7,400 ± 10% band and below the 8,000-word ceiling.

Verification after the round: `check_v3_7_3_three_layer_citation.py` PASSED (exit 0); `check_acronyms.py --scopes body,abstract_en,abstract_zh` exit 0 with the same advisory residue as Phase 4b; citations 41 distinct of 41 corpus IDs, 0 orphans, 0 unknown slugs; 41 reference entries; 6 tables; 2 figures; version line `v1.2 (Phase 6 revision round 1)`.

## Items fixed in total

Four: two evidence-traceability defects (round 1, items 1–2), one coherence defect (item 3), one word-choice defect (item 4). No reference was added, removed, or renumbered; no new source, search, dataset, or claim was introduced; no number was changed except the selection count corrected against the Stage 1 record.

## Residual issues and Acknowledged Limitations

1. **§4 sits at +14.7% of its 1,500-word allocation** (1,721 words against a ±15% band, upper bound 1,725). Compliant but with a 4-word margin, so any later addition to §4 must be offset by an equal trim. Recorded rather than silently absorbed.
2. **Abstract-level evidence, single analyst, no dual screening or inter-coder statistic** (§3.2, §3.3, §6.4, Appendix C). Disclosed and engaged rather than repaired; the review scored this as a stated design constraint, not a defect.
3. **Eleven preprints (26.8%) and one practitioner-magazine article** carry part of the proof and audit evidence; preprint status is marked in text and in the reference list, and Appendix B carries a peer-reviewed column, but no preprint was upgraded or excluded.
4. **The dynamic absence is a bounded corpus statement**, not a field claim: 0 of 41 abstracts, 0 of 36 in-window, 0 of 31 construction rows, stated with the #548 bounded-search qualifier in §6.2 and carried as a protected hedge.
5. **Three metadata-only rows** (P4, P7, R4) are cited at title level and excluded from every evidence count; their claims cannot be corroborated from this corpus.
6. **No page-level locators** accompany any citation (abstract-level corpus; anchors are `section:`-kind), and four reference entries carry a printed-issue-year note after the DOI. Both were flagged by Phase 5a and left in place deliberately; a strict-APA venue could ask for both to be revised.
7. **The framework is proposed, not validated** (§6.4, §7.2); the seven-study agenda is normative, and none of its studies is reported as done. No ranking, no PRISMA-compliance claim, no venue-fit claim.

## Artifact map for this stage

| Artifact | Content |
|---|---|
| `phase4a-precommitment.md` | Writer paper-blind acceptance-criteria paraphrase, D1–D7, terminal `[PRE-COMMITMENT-ACKNOWLEDGED]` |
| `phase4b-writer-record.md` | Writer `## Dimension Scores` (D1–D7) / `## Failure Condition Checks` (F1, F4, F2, F3, F0) / `## Writer Decision` + mechanical checks |
| `paper-draft-v1.md` | Phase 4b draft after the #849 acronym and preprint pass, before Phase 5 correction |
| `paper-draft.md` | Current manuscript, v1.2: abstracts, Draft Body §1–§7, Tables 1–6, Figures 1–2, Declarations, References, Appendices A–C |
| `measure_words.py` | Canonical body-word measurement (strips emission comments, excludes headings, table rows, captions, fenced blocks, and everything after `## Declarations`) |
| `phase5-citations.md` | Citation compliance report: 41/41, 0 orphans, APA auto-corrections (8 orderings, 1 apostrophe), 4 flagged items |
| `phase5-abstracts.md` | English abstract (225 words) + Simplified Chinese abstract (425 characters) + keywords + Abstract Quality Report |
| `phase6a-precommitment.md` | Evaluator paper-blind `## Contract Paraphrase`, `## Scoring Plan` (D1–D5, four fields each), pointer-only `criteria_binding_unavailable`, terminal tag |
| `phase6b-review.md` | Evaluator scores, failure-condition checks, evidence-cited Review Body, decision `request_revision` |
| `phase6-review.md` | This file: decision trail, round log, residual issues |
