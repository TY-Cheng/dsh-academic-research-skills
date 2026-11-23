[LEGACY-NO-CONTRACT]

# Stage 3′ — Re-Review (Verification Review)

**Inputs:** stage2/paper-draft.md (original), stage4/paper-draft-v2.md (revised), stage3/editorial-decision.md, stage4/response-to-reviewers.md
**Mode:** legacy single-pass verification re-review; the archived three-gate checker is not replayable in this run (no manifest, Schema 7 roadmap, adjudication sidecar, or evidence bundle), disclosed in run-log.md.
**Verdict: Minor Revision**

## R&R Traceability Matrix

| Item | Round-1 requirement (short) | Verdict | Evidence in v2 | Acceptance criterion met? |
|---|---|---|---|---|
| R1 | Scope abstract certified-object sentence to the 31 construction rows, both languages; align §7.1 | **Fully Addressed** | Abstract EN: "Within the 31 construction rows the certified object is, as reported, a single date's surface"; ZH: "31篇构造类文献的认证对象均为单一交易日曲面"; §7.1 repeats both halves. | **Yes** — the 31-row scope, four object forms, and "the five condition-and-evaluation rows … and the five seminal baselines certify none" appear in both abstracts and §7.1. |
| R2 | Reconcile proof/audit counts; repair near-disjoint claim and the G6 universal negative | **Fully Addressed** | §5.1: "16 + 1 + 5 + 11 + 8 = 41 rows and 1 + 5 = 6 audit rows"; Table 3 totals 17/16/8/41/6/10; Appendix B Audit flag recomputes to six, only G6 also proof; §7.1: "that one row and no other". | **Yes** — counts reproduced from the §3.2 definitions and Appendix B; overlap claim bounded; no universal negative survives. |
| R3 | Report a reproducible coding check (or manual); restate absence claims at measured stability | **Fully Addressed** | §3.4: "12/16 rows for family, 10/16 for evidence status (κ = 0.47), 15/16 for audit coding, 16/16 for time-axis engagement"; restatements in §3.3, §4.1, §5.1. | **Yes** — figures recomputed exactly from `stage4/reliability/second-coder-form.json`; threshold rule matches D.9 and adjudication.md; each failing field's absence claim is restated at its own agreement figure. |
| R4 | 31 query strings; itemize the 40 discretionary exclusions, one disposition each; one consistent replacement reason | **Partially Addressed** | §3.1 → Table A1 (31 strings, 8 groups); Table A2 40 rows, 39 reading "code only; no record-level note"; §3.1 and Appendix A.3 agree on both replacements. | **Partly** — rerunning the search is possible, reproducing the included set is not: "the coder's working notes for the remaining 39 rows were not retained". Residual gap: record-level rationales for 39 rows (residual obligation class: **should_fix**; the limit is disclosed). |
| R5 | Put the Table 4 clause into the declared H2, or disclose post hoc | **Fully Addressed** | §1.2: "the second clause was added after the first coding pass … disclosed as post hoc rather than pre-registered"; Table 4 H2 row: "The fit clause was formulated after the first coding pass (§1.2)". | **Yes** — both clauses adjudicated in Table 4 and §5.1; the post hoc origin is disclosed where the hypothesis is stated. (The package's "§3.3" pointer is a location slip; H2 is declared in §1.2 in both versions.) |
| R6 | State the butterfly condition as c″ − c′ ≥ 0; resolve SC2/SC4 boundary; re-examine affected codings | **Fully Addressed** | §2.1: "the butterfly or Durrleman condition, ∂²c/∂k² − ∂c/∂k ≥ 0", with the C″(K) derivation, SC2 coincidence case, SC4 zero-maturity case, Black–Scholes numbers (c″ ≈ −0.53, c″ − c′ ≈ +0.07); Appendix C.4. | **Yes** — exact condition, both boundary relations, and all 39 affected rows re-read with no coding change and the SC3 dependency stated. |
| R7 | Two per-row columns; enforcement rule incl. model-class inheritance; reconcile 0-of-41 with the ten named rows | **Fully Addressed** | §2.2: "0 rows are D3; three are D2 (G7, C3, G1); four are D1 (P8, C2, C5, R8); the remaining 34 are D0"; Appendix B Time/Dyn for all 41 rows. | **Yes** — Appendix B recomputes to the ten time rows §2.2 names and to 0 D3; model-class guarantee stated and excluded from enforcement counting. |
| R8 | Attach threshold and power (or an explicit missing-inputs statement) to every reported residual rate | **Fully Addressed** | §5.4: "Zero of six audit rows supply three or more of the five inputs, and zero of 41 supply all five", after per-row missing-input statements. | **Yes** — every residual rate now carries its missing inputs against the five-input criterion; no rate is presented as a grade. |
| R9 | Scope the cost/build-or-buy claim; separate established from asserted | **Fully Addressed** | §7.2: "What it **asserts** is cost: about five rows state a computational cost, none measures one on a common grid"; §7.1 makes no pricing or build-or-buy claim. | **Yes** — established versus asserted separated, and the withdrawn "what a guarantee is worth and what it costs" claim is named as not licensed. |

## Suggested-revision follow-up

- **S1** addressed — 29 + 11 + 1 and 36 + 5 in both abstracts, §3.1 and Table 1.
- **S2** addressed — ASCII exhibits retained but captioned as the review's own arithmetic/schematic ("explicitly not a PRISMA flow diagram"); no stage or production labels remain.
- **S3** addressed — VI/VII defined in §3.2 and D.8; 40 VI + one VII (C2) applied in Table 1 and Appendix B.
- **S4** addressed — one metadata-only sentence (§3.2, D.8); the three rows (P4, P7, R4) count in structural tallies only.
- **S5** addressed — Appendix B rebuilt to 13 columns × 41 rows; D.10 recomputation table; A/B/C grade withdrawn (C.5).
- **S6** declined with reason, as expected — the 41-reference freeze is honoured (reference list = 41) and the operationalisation is published in D.5 instead; not a defect.
- **S7** addressed — §6.4 names three adjacent audiences with the competence each needs.
- **S8** addressed — §6.3 orders seven studies with dependency, data access and owner.
- **S9** addressed — §6.2 title-level audit of the 40 excluded pool plus the Table A2 "Discussed in" column; limits stated.
- **S10** addressed — §7.2 incidence paragraph (author bears, reviewer/editor enforces, reader receives, validator still needs the five inputs).
- **S11** addressed — §7.1 states the bounded claim; §7.2: "It is not a ranking, and it does not license one."

## New issues (if any)

### N1 — Corpus-construction paragraph is duplicated in §3.1
**Severity:** Minor · **Attribution:** regression
**Evidence Anchor:** section: §3.1 — "The corpus was assembled from the OpenAlex representational-state-transfer (REST) application programming interface (API) with 31 free-text queries in eight groups" appears twice in consecutive paragraphs (paper-draft-v2.md lines 98 and 100), near-verbatim.

### N2 — Appendix D.10's peer-review tally contradicts Appendix B
**Severity:** Minor · **Attribution:** regression
**Evidence Anchor:** section: Appendix D.10 — "tally of the Peer-reviewed column (30 yes, 11 no)", against Appendix B's note "29 yes and 12 no" and D.10's own next row "12 rows carry Peer-reviewed = no". Recomputing Appendix B gives 29 yes / 12 no (11 preprints + practitioner S3); Table 1's "11 preprints (26.8%)" is consistent with 29/12.

### N3 — Stale completion marker in the AI Use Disclosure
**Severity:** Minor · **Attribution:** regression
**Evidence Anchor:** section: §Declarations (AI Use Disclosure) — "the recheck's own input fields are marked for completion in the manuscript". §3.4 now carries the completed figures (no `<!--RELIABILITY-STATS-->` marker remains) and `stage4/second-coder-input.json` has no blank fields, so the sentence misdescribes the evidence state.

### N4 — Abstract still offers a proof/test "nearly disjoint" claim
**Severity:** Minor · **Attribution:** previously_missed (paragraph unchanged from v1.3's "almost disjoint"; not decision-driving)
**Evidence Anchor:** section: §Abstract — "Proof-level and test-level evidence come from nearly disjoint sets". After R2 the audited finding is proof versus audit (§1.1, §5.1, §7.1), and proof and numerical test are exclusive coded statuses, so the sentence is at best vacuous and no longer matches the corrected claim.

## Response-letter claim check

- **R1** backed — scope, both languages and §7.1 present as described.
- **R2** backed — §3.2 definitions, §5.1 partition, Table 3 columns, §7.1 rewrite and D.10 recomputation all present.
- **R3** *not* backed as stated — the letter says the numeric agreement sentence "is deliberately left to the operator and marked"; v2 §3.4 carries the full figures and no marker remains. `stage4/revision-log.md` (items 12 and 129) is stale in the same way. The manuscript is stronger than the letter, not weaker.
- **R4** backed on the three changes, but the "Fully addressed" status is not: the letter itself concedes "cannot reproduce the 40 discretionary selections from the log".
- **R5, R7, R9** backed — §1.2 + Table 4 + §5.1; §2.2 rule + D0–D3 counts + Appendix B columns + Table 3; §7.2 established/asserted split with the withdrawn claim named.
- Minor letter inaccuracy: "κ ≥ 0.70 per field" — the manuscript applies the κ threshold to evidence status only, matching D.9 and adjudication.md (manuscript correct).
- Counts confirmed: 41 references, 6 tables, 2 figures; the claimed 7,862-word body was not reproduced independently (gross body word count including tables/equations is higher; not a defect).

## Reliability paragraph consistency

- **Sample:** §3.4's 16 IDs (P1, P4, P7, N2, N5, R2, R3, R4, R5, G6, G7, C3, C4, C5, S1, S2) are identical to `stage4/reliability/adjudication.md`'s list, as is the stratified design.
- **Figures:** recomputed from `second-coder-form.json` against Appendix B — family 12/16, evidence status 10/16 (Cohen's κ = 0.47 exactly: p_o = .625, p_e = .293), audit 15/16, time-axis 16/16, dynamic 16/16, comparability 10/16, aggregate 79/96 = 82.3%. All match §3.4, and all 17 disputed cells match adjudication.md row for row.
- **Threshold:** §3.4's "agreement is at least 0.85 and, for evidence status, κ ≥ 0.70" equals Appendix D.9's decision rule equals adjudication.md; the three fields it flags as failing (family, evidence status, comparability) are exactly the three adjudication.md flags.
- **Restatements:** §3.3 restates comparability at 10/16 ("no coder assigned direct, so the zero-direct result stands"); §4.1 restates family at 12/16 and names the disputed rows; §5.1 restates evidence status at 10/16 with κ = 0.47. adjudication.md's "No ledger change" matches §3.4's "the ledger was not changed". The only cross-document mismatch is the letter's per-field κ wording.

## Judge Record

- Verifier: subagent s3prime-review, model family deepseek, single pass
- Round-1 provenance: `stage3/review-panel-provenance.json` (parses; `review-panel-provenance/1.0`, panel `iv-surface-review-v047-round-1`, mode `reviewer_full`), artifact_sha256 `55e69a64eec37bcaca7d330a2e9f244a814600d02ffbd0165bff7f30e8fff14e` (matches the editorial package)
- Carried hashes from the carrier: normalized_manifest_sha256 `e0d438d72b7751a4f356d72d1e329349a59af9db78610a7585d772514e59e95b`, execution_topology_sha256 `efb4451e1400e2f80ad70b29208d1d00eadb40e4b29fb9e6a54aa6a1f2cd2c3c`, contract_sha256 `d958bc2ade7d9d154954c33fd424766697a8b6ef664854800a3106d804ee7e5c`
- Six axes as carried: role_separated true, blind_to_peer_outputs true, fresh_context true, model_family_distinct false, provider_distinct false, human_distinct false; independence_claim `not_computed_from_personas`; correlated_error_disclosure required (same_model_family)
- Blind cross-model pass: not run (legacy single pass). Pre-committed criteria: none (legacy — no contract). Reviewer configuration: one verification pass, no panel. Judging budget: one pass, no re-read.
- Evidence seen: stage2/paper-draft.md (v1.3), stage4/paper-draft-v2.md (v2.0), stage3/editorial-decision.md, stage4/response-to-reviewers.md, stage4/reliability/adjudication.md, stage4/reliability/second-coder-form.json, stage4/revision-log.md, stage3/review-panel-provenance.json; Round-1 seat findings via the editorial package.
- Correlated-error disclosure: "This verification round ran on the same model family that drove the revisions; over-optimization to this judge's latent biases is possible (Ren et al. 2026, arXiv:2607.13104 §8.1.2)."

## Recommendation

Minor Revision. Eight of nine must_fix items are fully addressed and the revised claims survive an independent recomputation from the frozen ledger and second-coder form; R4 remains partially addressed because the discretionary selection inside the 40-row pool is not reproducible, with a should_fix residual that the manuscript already discloses. Decision derivation: B4 not triggered; B5 triggered by the R4 partial and by three regression-attributed minor editing defects (N1–N3), plus one carried minor (N4). should_fix_addressed_rate = 90% (9/10; S6 declined under the reference freeze). Ask for: deduplicate §3.1; correct D.10's peer-review tally to 29/12; make the AI Use Disclosure sentence accurate (or drop it); align the abstract's proof/test sentence with the corrected proof/audit finding; reconcile the letter and revision-log with the figures now in §3.4; optionally add per-row notes for Table A2, or keep the current explicit statement that the discretionary step is not reproducible.
