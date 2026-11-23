# Editorial Decision

## Manuscript Information

- **Title**: Four Loci of Enforcement: Static and Dynamic No-Arbitrage in Equity-Index Implied-Volatility Surfaces, 2015-2026
- **Manuscript ID**: IVSURF-2026-11-23
- **Submission Date**: 2026-11-23
- **Decision Date**: 2026-11-23
- **Review Round**: 1

## Review Panel Provenance (#540/#740)

- **Typed artifact**: `examples/dsh/iv-surface-review-v047/stage3/review-panel-provenance.json` (`review-panel-provenance/1.0`; contract `reviewer/reviewer_full/v2`)
- **Artifact SHA-256**: `55e69a64eec37bcaca7d330a2e9f244a814600d02ffbd0165bff7f30e8fff14e`
- **Panel ID**: `iv-surface-review-v047-round-1`
- **Normalized manifest SHA-256**: `e0d438d72b7751a4f356d72d1e329349a59af9db78610a7585d772514e59e95b`
- **Execution topology SHA-256**: `efb4451e1400e2f80ad70b29208d1d00eadb40e4b29fb9e6a54aa6a1f2cd2c3c`
- **Fresh-context scope**: `within_panel_attempt_only` (does not compare retries or prior rounds)

| Seat | Role ID | Actor type | Context ID | Peer outputs visible | Model family | Provider | Human reviewer ID |
|---|---|---|---|---|---|---|---|
| EIC | eic | model | `subagent-seat-eic` | false | deepseek | deepseek | null |
| R1 | methodology | model | `subagent-seat-methodology` | false | deepseek | deepseek | null |
| R2 | domain | model | `subagent-seat-domain` | false | deepseek | deepseek | null |
| R3 | perspective | model | `subagent-seat-perspective` | false | deepseek | deepseek | null |
| DA | da | model | `subagent-seat-da` | false | deepseek | deepseek | null |

| Provenance axis | Status (`true` / `false` / `unknown`) |
|---|---|
| Role-separated | true |
| Within-panel invocation-context separation | true |
| Blind to peer outputs | true |
| Model-family distinct | false |
| Provider distinct | false |
| Human-reviewer distinct | false |

- **Binary independence claim**: Not computed (`independence_claim: not_computed_from_personas`). Persona or role diversity proves only `role_separated`; do not relabel the panel as independent.
- **Correlated-error disclosure**: All model-executed review seats used one model family; role separation does not remove correlated-error risk. (Reason: `same_model_family`; `required: true`.)

## Decision

### Major Revision

No reject subtype applies: subtypes attach to Reject only.

## Blocking Issues

Three issues currently block acceptance, in immutable source order. The remaining required items are material but repairable inside the same revision cycle.

| Transport ref | Blocking issue | Source reviewer(s) | Evidence anchor | Resolving roadmap item |
|---|---|---|---|---|
| R1 | The abstract's certified-object sentence claims one object for all 41 rows, while §2.3 and Table 2 record four objects and the ten condition and seminal rows do not certify a surface. | EIC; DA (same sub-claim, M4) | `text: "the certified object in all 41 rows is a single date's surface"` | R1 |
| R2 | The proof and audit counts cannot be re-derived: §3.2's definition of a numerical test covers 16 Table 3 rows while §5.1 reports 6 audit rows, and the 17 proof / 6 audit / 1 overlap partition is not reproducible, so §7.1's universal negative is contradicted by the ledger. | R1; DA (same sub-claim, M5) | `text: "An audit row reports a residual or violation check on its own output; G6 is the only row that also reports a structural guarantee."` | R2 |
| R6 | SC3 misstates the butterfly condition as c'' ≥ 0 instead of c'' − c' ≥ 0, which is strictly stronger given SC2, excludes valid surfaces, and cannot hold on the zero-maturity slice fixed by SC4, so SC1–SC5 are not mutually consistent. | R2 | `text: "**SC3**, strike convexity, the butterfly or Durrleman condition, $\partial^{2} c/\partial k^{2}\ge 0$"` | R6 |

## Reviewer Summary

| Reviewer | Role | Recommendation | Confidence |
|---|---|---|---|
| Journal-Fit Reviewer | Senior quantitative-finance scholar, editorial experience on reviews-and-surveys tracks (field-general: no venue bound) | Major Revision | 4–5 (per finding; W1 = 4, W2–W4 = 5) |
| Reviewer 1 | Research-synthesis and information-science professor, review methodology | Major Revision | 4–5 (per finding; W1 and W6 = 5, W2–W5 = 4) |
| Reviewer 2 | Mathematical-finance professor, implied-volatility-surface construction and no-arbitrage parameterisation | Major Revision | — `[CONFIDENCE-SOURCE: report-level]` |
| Reviewer 3 | Head of model validation and model risk at a derivatives dealer | Major Revision | 3–4 (per finding; W1 and W2 = 4, W3 and W4 = 3) |
| Devil's Advocate | Fixed adversarial seat | N/A — findings only | N/A — per-finding only |

Recommendations are derived from each seat's dimension scores: a warn-or-worse on any assessed dimension supports Major Revision under the `reviewer_full` contract; no seat's scores support Accept or Reject. The DA issues no recommendation; its seven MAJOR rows (M1–M7) are findings, and its CRITICAL table is empty.

## Consensus Analysis

Sub-claims `SC-1` to `SC-20` are the granular units this package transports; every roadmap row names its driving sub-claim, and the counts below use the four non-DA scoring seats as the denominator.

### Points of Agreement (Consensus)

**[CONSENSUS-4]** (all four non-DA scoring seats agree):

1. The manuscript states its evidence limits accurately and bounds the dynamic-absence claim where the claim is stated. EIC S2 quotes `text: "PRISMA 2020-style, not PRISMA-compliant"`; R1 S3 records the bounded-absence statement at `section: §6.2` as sound; R2 S1 quotes `text: "Once the term is fixed to process-level consistency, the dynamic count returns to zero"`; R3 S2 quotes `text: §3.3 "Those limits are not repaired anywhere in the paper; they are stated once here and carried into Section 6.4."` This agreement covers the stated limits only; whether every headline restatement honours them is the subject of R1, R2 and R9.

**[CONSENSUS-3]** (three agree; the fourth is **silent**):

1. The four-locus framework and its Table 2 mapping are operationalised well enough to organise the corpus by enforcement locus. EIC S3 (`table: Table 2`), R1 S2 (`table: Table 2`) and R2 S2 (the taxonomy is usable and honest) agree. R3 is silent: its S1 addresses the enforcement triple's legibility for adjacent readers, not the locus mapping.

### Below the Consensus Bar (#1100)

**[CORROBORATED]** (2/4 non-DA seats agree, none disputes):

1. R1 and R3: the §7.2 practitioner-cost claim is asserted, not measured — R1 W7 and R3 W2 quote the same sentence `text: §7.2 "it identifies what each method's guarantee is worth and what it costs"`, against §5.3 and Table 6 (cost asserted in about five rows, comparable in none). Carried at R9. DA-corroborated: the DA reports the same sub-claim (M1). The DA is not an independent seat and does not change the count.
2. EIC and R2: the abstract's corpus composition does not sum — both quote `text: "of which 29 are peer-reviewed and 11 are preprints"` while Table 1 and §6.4 count a 41st practitioner-magazine record. Carried at S1.
3. R1 and R2: the metadata-only records' treatment is inconsistent — R1 W4 finds P4, P7 and R4 violating the retrievable-abstract inclusion rule; R2 W5 finds the same rows coded in Appendix B but excluded from "every evidence count". Carried at S4.

**[SINGLE-REVIEWER]** (1/4 non-DA seats raises it, none disputes):

1. EIC: the abstract overgeneralises the certified object to all 41 rows — SC-1, carried at R1. DA-corroborated: the DA reports the same sub-claim (M4). The DA is not an independent seat and does not change the count.
2. R1: the audit and proof-audit counts do not follow from the stated definitions — SC-2, carried at R2. DA-corroborated: the DA reports the same sub-claim (M5). The DA is not an independent seat and does not change the count.
3. R1: abstract-level coding is single-analyst with no reliability check — SC-3, carried at R3.
4. R1: H2 is adjudicated against a fit-error clause absent from the declared hypothesis — SC-5, carried at R5.
5. R2: SC3 mistranslates the butterfly condition and is inconsistent with SC4 at the zero-maturity boundary — SC-6, carried at R6.
6. R2: the 0-of-41 dynamic claim has no row-level time-axis or enforcement coding — SC-7, carried at R7. DA-corroborated: the DA reports the same sub-claim (M2). The DA is not an independent seat and does not change the count.
7. R3: reported residuals never become a validation acceptance criterion — SC-9, carried at R8.
8. EIC: production artifacts and stage labels remain in the draft — SC-19, carried at S2.
9. EIC: the VI/VII evidence-level labels are unexplained — SC-20, carried at S3.
10. R1: Appendix B lacks per-row values for the counts the body reports — SC-15, carried at S5.
11. R2: the dynamic formulation rests on one assumption-level preprint — SC-16, carried at S6.
12. R3: users outside the research core are neither named nor excluded — SC-17, carried at S7.
13. R3: the seven-study agenda lacks dependencies, data access and ownership — SC-18, carried at S8.

**DA-only items (no consensus level; no scoring seat raises these sub-claims):**

1. S9: the excluded pool of 40 discretionary records is never audited for dynamic tests (DA M3, SC-8).
2. S10: the reporting triple's enforcement cost and its incidence are unanalysed (DA M6, SC-11).

The DA is not an independent seat; these items carry no scoring-seat agreement and change no count.

### Points of Disagreement

**Disagreement 1: Whether the unrerunnable search path is a defect or an accurately disclosed bound**
- **R1 view**: W3 (Major) — §3.1 and Appendix A do not carry the query strings, a per-record disposition of the 40 discretionary exclusions, or a consistent record of the two post-screening replacements; the two narratives conflict.
- **R3 view**: S2 — the corpus limits, including single-database English-only retrieval and abstract-level coding, are disclosed once and carried forward; their honesty is a strength, not a further defect.
- **Disagreement type**: Severity disagreement.
- **Editor's Resolution**: Sustain R1's Major severity at R4. R3's point stands for the disclosure's honesty, which the package preserves: the requirement adds the missing record rather than withdrawing the limits statement.
- **Resolution Rationale**: R1 anchors a factual inconsistency (§3.1's "no enforcement claim" reason against Appendix A's metadata-resolution reason), which a disclosure cannot repair; R3's assessment concerns the adequacy of the stated limits, a different question, so neither view is withdrawn.

**Disagreement 2: Whether the 0-of-41 dynamic claim fails as a reporting gap or as an evidence gap**
- **DA view**: the alternative explanation in the DA report (abstract-level non-reporting) and the reasoning in M5 that a reporting gap is converted into an evidential one — the corpus was coded from abstracts, so an unreported test is not an absent test, and the headline sentence travels without the qualifier.
- **R2 view**: S1 holds that once the term is fixed to process-level consistency the dynamic count returns to zero; W2 holds that the claim nonetheless lacks a row-level time-axis and enforcement coding, so the evidence must be shown row by row.
- **Disagreement type**: Direction disagreement (what the defect is, and therefore what repair follows).
- **Editor's Resolution**: Both diagnoses survive in part. R7 requires the row-level coding and a stated enforcement rule; the claim stays corpus-scoped as §6.2 states it and is not extended to the field; the DA's reporting-gap alternative is recorded as a limitation because full texts were outside the coding scope.
- **Resolution Rationale**: R2's S1 fixes the term's meaning, which is what keeps the claim checkable; the DA's mechanism explains why the abstract wording can still overreach, which R7's coding answers at the corpus level. Neither seat's evidence is displaced, so the repair combines them.

**Disagreement 3: Whether the non-ranking stance contains an overclaim**
- **R1 view**: S4 — the no-comparability rule (0 direct, 30 context, 11 not comparable) is declared ex ante, which is a methodological strength.
- **R3 view**: S3 — the corpus does not identify a best method, so the stance is appropriate.
- **DA view**: M7 — §7.1 infers "no ranking is possible" from "direct comparison is unavailable", which licenses only the weaker claim about the corpus's reported numbers; the agenda's head-to-head study concedes ranking becomes possible with a common protocol.
- **Disagreement type**: Existence disagreement (whether an overclaim is present at all).
- **Editor's Resolution**: Sustain the DA as a wording correction at S11; withdraw no seat's strength. The ex-ante rule and the "no best method" finding survive; only the modal sentence changes.
- **Resolution Rationale**: R1's and R3's anchors concern the rule and the corpus finding, not the modal inference DA M7 quotes; the three views can all hold once §7.1 distinguishes "no ranking licensed by these numbers" from "no ranking possible".

## Decision Rationale

All four mandatory dimensions sit at warn: methodology (D1), domain accuracy (D2), argumentative coherence (D3) and venue fit and contribution (D6, assessed on its contribution half only because no venue was bound). D4 and D5 are warn as well, so F3 and F5 both fire; F3, the higher-severity condition, fixes the action at Major Revision, and F5's Minor Revision is subsumed by that severity rather than reported as a second decision. Reject is not available: no dimension blocks, there is no fatal, and every Major finding is repairable inside the frozen 41-source corpus — one condition is corrected in §2.1 and its row codings re-examined (R6), one appendix gains a column and a coding rule (R7), the abstract and §7.1 are rescoped (R1), and two definitions are separated so the counts reconcile (R2). Major rather than Minor because a mandatory-dimension warn here is not a copyedit: R6 changes a definition on which row codings rest, and R1 and R2 change the support of the two headline findings the paper is judged on. The seats press different points — the EIC on positioning, R1 on reproducibility of the evidence base, R2 on a mistranslated no-arbitrage condition and an uncoded void, R3 on residuals that never become acceptance criteria and a cost claim the corpus cannot measure. Their shared agreements concern the accuracy of stated limits and the usability of the framework, which touch no dimension score. The disagreements do not move the arithmetic either: R1's rerunnability defect is a factual conflict between §3.1 and Appendix A that R3's accurate disclosure cannot repair, and the DA's reporting-gap reading of the void is kept as a limitation, not accepted as a rebuttal, because §6.2 bounds the claim.

### Required Revisions

| Transport ref | Revision Item | Sub-Claim(s) | Severity | Evidence Anchor | Confidence | Source Reviewer | Obligation class | Cost scope | Bounded consequence |
|---|---|---|---|---|---|---|---|---|---|
| R1 | Scope the abstract's certified-object sentence to the rows that certify a surface, in both language versions, and align §7.1. | SC-1 | Major | `text: "the certified object in all 41 rows is a single date's surface"` | 4 — abstract compared directly with §2.3 and Table 2 | EIC | must_fix | sentence — Abstract (English and Chinese); §7.1 | claim_scope_unsupported — claim: Abstract certified-object sentence and §7.1 |
| R2 | Reconcile the proof and audit counts from the stated definitions, and repair the near-disjoint claim and its universal negative in light of G6. | SC-2 | Major | `text: "An audit row reports a residual or violation check on its own output; G6 is the only row that also reports a structural guarantee."` | 5 — the definition and Table 3 counts are compared directly | R1 | must_fix | section — §3.2, §5.1, §7.1, Table 3 | method_reproducibility_unresolved — section: §3.2, §5.1, Table 3 |
| R3 | Add a reliability check or an explicit coding manual for the abstract-level coding, and restate the absence claims at their measured stability. | SC-3 | Major | `text: "Coding was single-analyst, retrieval was English-only and OpenAlex-only"` | 4 — method statements and Appendix C limits compared | R1 | must_fix | section — §3.2, Appendix C | method_reproducibility_unresolved — section: §3.2, Appendix C |
| R4 | Make the search and selection path re-runnable from the manuscript, and state one consistent reason for the two post-screening replacements. | SC-4 | Major | `absence: §3.1 and Appendix A — expected the 31 query strings, a per-record disposition of the 40 discretionary exclusions, and a record of the two post-screening replacements; checked §3.1, Appendix A, Table 1, Appendix B` | 4 — §3.1, Appendix A and Table 1 compared | R1 | must_fix | section — §3.1, Appendix A | method_reproducibility_unresolved — section: §3.1, Appendix A |
| R5 | Align H2 with the clause actually adjudicated in Table 4, or disclose the post hoc revision. | SC-5 | Major | `text: "penalty and repair routes may displace rather than remove the constraint burden"` | 5 — H2 as declared compared with Table 4 | R1 | must_fix | section — §3.3, §5.1, Table 4 | claim_scope_unsupported — claim: H2 as declared in §3.3 |
| R6 | Correct SC3's butterfly condition to c'' − c' ≥ 0, state its relation to SC2 and SC4 at the zero-maturity boundary, and re-examine every row coded as expressing SC3. | SC-6 | Major | `text: "**SC3**, strike convexity, the butterfly or Durrleman condition, $\partial^{2} c/\partial k^{2}\ge 0$"` | — `[CONFIDENCE-SOURCE: report-level]` | R2 | must_fix | section — §2.1; rows coded to SC3 in Appendix B and Appendix C | claim_scope_unsupported — claim: SC1–SC5 condition set in §2.1 |
| R7 | Add row-level time-axis and dynamic-enforcement coding to the ledger, and state whether a model-class guarantee counts as enforcing the dynamic condition. | SC-7 | Major | `absence: Appendix B and Appendix C — expected a per-row time-axis and dynamic-enforcement coding for the 41 sources; checked Section 2.2, Table 3 in Section 5.1, the Appendix B table body, and the Appendix C field list` | — `[CONFIDENCE-SOURCE: report-level]` | R2 | must_fix | section — Appendix B, Appendix C, §2.2 | evidence_gap_remains — section: Appendix B, Appendix C, §2.2 |
| R8 | Turn the reported residuals into an acceptance criterion by supplying the loss function, tolerance, test power and regime coverage, or state exactly which inputs are missing. | SC-9 | Major | `text: §5.3 "whether any reported residual is operationally adequate is not assessable without a loss function and a tolerance that the corpus does not supply"` | 4 — the residual numbers are compared with the missing inputs | R3 | must_fix | section — §5.3 | acceptance_criterion_unmet — claim: reported residual rates in §4.3–§5.3 |
| R9 | Scope the §7.2 cost and build-or-buy claim to what the corpus measures, or state that cost is asserted and not comparable in the corpus. | SC-10 | Major | `text: §7.2 "it identifies what each method's guarantee is worth and what it costs"` | 4 — §7.2 compared with §5.3 and Table 6 | R1, R3 | must_fix | sentence — §7.2; §7.1 | claim_scope_unsupported — claim: §7.2 cost and build-or-buy sentence |

#### Required Item Details

**R1: Scope the abstract's certified-object sentence**
- **Problem**: The abstract says the certified object in all 41 rows is a single date's surface. §1.1 defines the certified object as the surface a row claims admissible, and Table 2 records four objects: the admitted parameter set, the evaluated sample, the image of a projection, and the accepted sample or inherited model class. The total includes five condition rows and five seminal baselines that do not construct or repair a surface in the same sense, and two seminal constructions enforced no admissibility at all.
- **Source**: EIC W1 (Major, confidence 4); the DA reports the same sub-claim from Table 2 (M4).
- **Requirement**: Restate the certified-object sentence in the English and Chinese abstracts and at §7.1 so that the all-rows formula is scoped to the rows that certify a surface (31 construction rows), with the condition, evaluation and seminal groups explicitly stated to certify no surface.
- **Acceptance criteria**: Abstract (both languages) and §7.1 attach the single-date-surface claim only to the rows that certify a surface, name the 31 construction rows as that scope, and state that the condition, evaluation and seminal rows certify none.

**R2: Reconcile the proof and audit counts**
- **Problem**: §3.2 defines a numerical test in the same words used for an audit row, Table 3 reports 16 numerical-test rows (6 N, 4 R, 3 G, 1 C, 2 S) while §5.1 reports 6 audit rows (N2, N6, R5, R7, G5, G6), and the 17 proof / 6 audit / 1 overlap partition is not reproducible. G6 is both a structural guarantee and an audit, so §7.1's "will not find the pair" is contradicted by the paper's own ledger.
- **Source**: R1 W1 (Major, confidence 5); the DA reports the same sub-claim on the universal negative (M5).
- **Requirement**: Separate the numerical-test and audit-row definitions, rerun the count from the Appendix B coding, publish the recomputed partition, and restate the proof-audit claim as the ledger supports, with the G6 overlap and its synthetic-data qualification stated where the claim is made.
- **Acceptance criteria**: A reader can reproduce the proof, numerical-test, audit and overlap counts from the definitions in §3.2 and the Appendix B rows, the reported numbers match, and §7.1 no longer states a universal negative that G6 contradicts.

**R3: Add a coding reliability check**
- **Problem**: Coding was performed by one analyst from 34 full abstracts, 4 partial abstracts and 3 titles, with no second coder, codebook test or agreement statistic; the absence claims (0 of 41 dynamic, 0 direct comparability, 6 audit rows) therefore have unmeasured stability, which the report itself notes.
- **Source**: R1 W2 (Major, confidence 4).
- **Requirement**: Either dual-code a sample of rows with a second coder and report agreement, or state a coding manual precise enough to be re-applied, and qualify the absence claims with the measured stability of the coding they depend on.
- **Acceptance criteria**: The method states a reproducible coding check (second coder with agreement, or a testable manual), and every absence claim is stated at the stability the check supports.

**R4: Make the search and selection path re-runnable**
- **Problem**: §3.1 and Appendix A carry no query strings, no per-record disposition of the 40 discretionary exclusions, and no consistent record of the two post-screening replacements; §3.1 says the retrieved text showed no enforcement claim while Appendix A attributes the replacement to metadata resolution and abstract reconstruction failure.
- **Source**: R1 W3 (Major, confidence 4).
- **Requirement**: Report the 31 query strings, itemize the 40 discretionary exclusions with one disposition each, and give one consistent reason for the two replacements.
- **Acceptance criteria**: A third party can rerun the search from the reported strings and reproduce the included set, and the two replacement reasons agree between §3.1 and Appendix A.

**R5: Align H2 with the clause actually adjudicated**
- **Problem**: Table 4 reports the burden-displacement clause as supported and the fit-error clause as unsupported, but the declared H2 in §3.3 contains only the burden-displacement clause, so one adjudicated clause was never declared.
- **Source**: R1 W6 (Major, confidence 5).
- **Requirement**: Restore the fit-error clause to the declared H2 and adjudicate it as declared, or drop the clause from Table 4 and disclose the post hoc revision to H2.
- **Acceptance criteria**: Every clause adjudicated in Table 4 appears in the declared H2 in §3.3, or the post hoc change is disclosed where the hypothesis is stated.

**R6: Correct SC3's butterfly condition**
- **Problem**: §2.1 states SC3 as ∂²c/∂k² ≥ 0. The butterfly or Durrleman condition is c'' − c' ≥ 0; given SC2 (c' ≤ 0) the printed form is strictly stronger and excludes valid surfaces — Black–Scholes gives c'' ≈ −0.53 at k = −0.5 with c'' − c' ≈ +0.07 — and SC3 cannot hold on the zero-maturity slice fixed by SC4 (c''(k,0) = −e^k < 0 for k < 0), so SC1–SC5 are mutually inconsistent at their own boundary and every row coded as expressing SC3 inherits the error.
- **Source**: R2 W1 (Major; no per-finding confidence is stated in the card, so the report-level tag is transported).
- **Requirement**: Correct the condition in §2.1, state its relation to SC2 and SC4 at the zero-maturity boundary, and re-examine the rows whose coding depends on SC3, reporting which rows move.
- **Acceptance criteria**: §2.1 states the exact butterfly condition, the boundary inconsistency with SC4 is resolved or disclosed, and the affected row codings in Appendix B and Appendix C are re-verified.

**R7: Add row-level dynamic-enforcement coding**
- **Problem**: §2.2 says ten rows engage the time axis and names four (G7, C3, P8, C5); Appendix B carries eight fields with no time-axis or dynamic-enforcement column, so the remaining six and the 29 construction rows cannot be checked, and no rule says whether a model-class guarantee (G1, G7, C3) counts as enforcement. The 0-of-41 count therefore rests on an unstated coding decision.
- **Source**: R2 W2 (Major; report-level confidence tag); the DA reports the same sub-claim from the coding rule (M2).
- **Requirement**: Add a per-row time-axis and dynamic-enforcement column to Appendix B, state the enforcement rule (including model-class inheritance), and reconcile the count with the ten rows §2.2 names.
- **Acceptance criteria**: Appendix B carries the two columns for all 41 rows, the enforcement rule is stated, and the reported 0-of-41 count follows from the coded rows.

**R8: Make the residuals an acceptance criterion**
- **Problem**: §5.3 reports a 5.4% butterfly-violation floor over 252 out-of-sample SPX days, sub-1% static violations with stressed-year leakage, a 90.8% pass rate and 0.00% at 1e-4 on synthetic data, but no loss function, tolerance, test power or regime coverage, so none of these can serve as a validation acceptance criterion.
- **Source**: R3 W1 (Major, confidence 4).
- **Requirement**: Supply the loss function, tolerance, test power and regime coverage for each reported residual rate, or state in bounded terms exactly which inputs the corpus does not supply and which claims the numbers therefore cannot carry.
- **Acceptance criteria**: Each reported residual rate is accompanied by the threshold and power needed to read it as an acceptance criterion, or by an explicit statement of the missing inputs.

**R9: Scope the cost and build-or-buy claim**
- **Problem**: §7.2 says the review tells a build-or-buy decision what each method's guarantee is worth and what it costs, but §5.3 and Table 6 report cost as asserted in about five rows and comparable in none, with interpretability and data efficiency unpopulated, so the practitioner payoff is not supported by the findings.
- **Source**: R3 W2 (Major, confidence 4); R1 W7 raises the same sentence at minor severity, and the DA reports the same sub-claim (M1).
- **Requirement**: Separate what the corpus establishes from what it asserts, state that cost is asserted in about five rows and comparable in none, and limit the §7.2 and §7.1 payoff sentences to what the corpus measures.
- **Acceptance criteria**: §7.2 and §7.1 make no cost or build-or-buy claim beyond the asserted cost rows and the zero comparable measurements, and the distinction between established and asserted is stated where the payoff is claimed.

### Suggested Revisions

| Transport ref | Revision Item | Sub-Claim(s) | Severity | Evidence Anchor | Confidence | Source Reviewer | Obligation class | Cost scope | Bounded consequence |
|---|---|---|---|---|---|---|---|---|---|
| S1 | Make the abstract's corpus composition exhaustive by adding the practitioner-magazine record, or drop the sub-counts. | SC-13 | Minor | `text: "of which 29 are peer-reviewed and 11 are preprints"` | 5 — 29 + 11 = 40 is compared with Table 1 and §6.4 | EIC, R2 | should_fix | sentence — Abstract (English and Chinese); §6.4 | claim_scope_unsupported — claim: abstract corpus composition |
| S2 | Replace the ASCII/source exhibits with final figures, and remove stage labels and production placeholders from the draft. | SC-19 | Minor | `text: "Figure 1 (source diagram; to be typeset at Phase 7)"` | 5 — the placeholders are quoted in place | EIC | should_fix | section — Figures 1–2; front matter; §1–§7 | editorial_conformance_unmet — manuscript: front matter and Figures 1–2 |
| S3 | Define or delete the VI and VII evidence-level labels. | SC-20 | Minor | `text: "Evidence-level labels VI (40 rows) and VII (one row)"` | 5 — labels are used without definition | EIC | should_fix | sentence — §5.1 evidence labels | interpretive_ambiguity_remains — section: §5.1 |
| S4 | Make the metadata-only rows' treatment consistent: state the exception to the retrievable-abstract inclusion rule and say which counts include P4, P7 and R4. | SC-14 | Minor | `text: "Metadata-only rows are cited only for what their title asserts, and they are excluded from every evidence count."` | 4 — Appendix B coding versus the exclusion sentence | R1, R2 | should_fix | section — §3.1, §5.1, Appendix B | reporting_requirement_unmet — section: §3.1 and Appendix B |
| S5 | Add the per-row coded values Appendix B lacks for the counts the body reports (time axis, dynamic condition, audit rows, quality grades, Table 6 coverage). | SC-15 | Minor | `absence: Appendix B — expected per-row values for the eight fields named in Appendix C, including time-axis and dynamic-condition coding; checked Appendix B, Table 3, Table 6, Appendix C` | 4 — Appendix C fields compared with the Appendix B table | R1 | should_fix | section — Appendix B | reader_traceability_reduced — section: Appendix B |
| S6 | Cite the canonical source for the dynamic consistency formulation alongside the assumption-level preprint, without re-coding. | SC-16 | Minor | `text: "filtered probability space on which the option-price process is a martingale under a measure consistent with the numéraire (Niu, 2015)"` | — `[CONFIDENCE-SOURCE: report-level]` | R2 | should_fix | sentence — §1.1, §2.2 | evidence_gap_remains — section: §1.1 and §2.2 |
| S7 | Add one limitations sentence naming the audiences outside the research core and the competence each would need. | SC-17 | Minor | `absence: §6.4 and §7.2 — expected named supervisory and end-investor users and the competence each would require; checked §1.1, §5.1, §6.1, §6.4, §7.2, Appendix A` | 3 — scope of the audience claim | R3 | consider | sentence — §6.4 | reader_traceability_reduced — section: §6.4 |
| S8 | State the seven-study agenda's dependency order, data access and ownership. | SC-18 | Minor | `absence: §6.3 — expected dependency order, data access, and resource or owner requirements for the seven studies; checked §6.3, §6.4, Table 6` | 3 — agenda text compared with Table 6 | R3 | consider | section — §6.3 | reporting_requirement_unmet — section: §6.3 |
| S9 | Audit the 40 discretionary exclusions for dynamic or process-level tests, or state why the excluded pool cannot support the void claim. | SC-8 | Major | `absence: §6.2 and §3.1 — expected an audit of the excluded pool for dynamic tests; checked §3.1 exclusion codes, Appendix A, §6.2 stated alternatives` | 4 — exclusion counts and codes compared | DA | should_fix | re_analysis — Appendix A exclusion pool (40 discretionary records) | evidence_gap_remains — section: §3.1 and Appendix A |
| S10 | Analyse the reporting triple's enforcement cost and its incidence, or present it as a proposal with unexamined costs. | SC-11 | Major | `text: §7.2 "The triple costs three sentences"` | 4 — §7.2 compared with §1.3 and §5.1 counts | DA | should_fix | section — §7.2 | claim_scope_unsupported — claim: §7.2 reporting-triple proposal |
| S11 | Weaken §7.1's modal inference to the claim the corpus licenses. | SC-12 | Major | `text: §7.1 "Direct comparison is unavailable, so no ranking is possible."` | 4 — §7.1 compared with §3.3 and §6.3 | DA | should_fix | sentence — §7.1 | claim_scope_unsupported — claim: §7.1 non-ranking sentence |

## Revision Roadmap

### Source-traceability checklist

> Keep this in immutable source order. Do not suggest a work order. The author chooses `will_address`, `wont_address`, or `not_on_point` later in the separate author-adjudication checkpoint.

- [ ] R1 — obligation `must_fix`: Scope the abstract's certified-object sentence to the rows that certify a surface.
- [ ] R2 — obligation `must_fix`: Reconcile the proof and audit counts and repair the proof-audit claim.
- [ ] R3 — obligation `must_fix`: Add a coding reliability check and restate absence claims at their measured stability.
- [ ] R4 — obligation `must_fix`: Make the search and selection path re-runnable and give one consistent replacement reason.
- [ ] R5 — obligation `must_fix`: Align H2 with the clause adjudicated in Table 4.
- [ ] R6 — obligation `must_fix`: Correct SC3's butterfly condition and re-examine the rows coded to it.
- [ ] R7 — obligation `must_fix`: Add row-level time-axis and dynamic-enforcement coding and state the enforcement rule.
- [ ] R8 — obligation `must_fix`: Make the residuals an acceptance criterion or state the missing inputs.
- [ ] R9 — obligation `must_fix`: Scope the §7.2 cost and build-or-buy claim to what the corpus measures.
- [ ] S1 — obligation `should_fix`: Make the abstract's corpus composition exhaustive.
- [ ] S2 — obligation `should_fix`: Replace exhibits and remove stage labels and placeholders.
- [ ] S3 — obligation `should_fix`: Define or delete the VI and VII evidence-level labels.
- [ ] S4 — obligation `should_fix`: Make the metadata-only rows' treatment consistent.
- [ ] S5 — obligation `should_fix`: Add the missing per-row values to Appendix B.
- [ ] S6 — obligation `should_fix`: Cite the canonical dynamic-consistency source.
- [ ] S7 — obligation `consider`: Name the audiences outside the research core and their required competence.
- [ ] S8 — obligation `consider`: State the seven-study agenda's dependencies, data access and ownership.
- [ ] S9 — obligation `should_fix`: Audit the excluded pool for dynamic tests or state why it cannot support the void claim.
- [ ] S10 — obligation `should_fix`: Analyse the reporting triple's enforcement cost and incidence.
- [ ] S11 — obligation `should_fix`: Weaken §7.1's modal inference to the claim the corpus licenses.

- **Machine artifact**: revision-roadmap/1.1 is emitted separately at stage3/revision-roadmap.json (deferred to the Stage 4 revision adapter); this package's tables are the transported source.

## Journal-Supplied Deadline

- **Exact deadline from source letter**: `NOT PROVIDED`
- Do not infer a deadline, duration, or work estimate.

## Response Letter Instructions

Please use the format in `templates/revision_response_template.md` to respond to every reviewer comment item by item.

**Must include**:
1. Response and revision description for each Required Revision
2. Response for each Suggested Revision (adopted or reason for not adopting)
3. Change markup (mark all changes in the revised manuscript with color or track changes)
4. Cross-reference table of new page numbers/paragraphs

## Closing

We encourage you to carefully consider the reviewers' comments and submit a substantially revised manuscript. Please note that the revised manuscript will undergo another round of review. No deadline is stated here: the review letter supplied none, and no date or duration is inferred.

## Mechanical Audit Lines

```text
fired_conditions: [F3, F5]
dimension_verdicts: [D1=warn, D2=warn, D3=warn, D4=warn, D5=warn, D6=pass]
da_critical_adjudications: []
editorial_decision=major_revision
```

## Appendix: Full Reviewer Reports

The complete reviewer reports ship as the five files below and are not reproduced here:

- `examples/dsh/iv-surface-review-v047/stage3/reviews/phase2-eic.md` — Journal-Fit Reviewer
- `examples/dsh/iv-surface-review-v047/stage3/reviews/phase2-methodology.md` — Reviewer 1 (Methodology)
- `examples/dsh/iv-surface-review-v047/stage3/reviews/phase2-domain.md` — Reviewer 2 (Domain)
- `examples/dsh/iv-surface-review-v047/stage3/reviews/phase2-perspective.md` — Reviewer 3 (Cross-disciplinary/Practical)
- `examples/dsh/iv-surface-review-v047/stage3/reviews/phase2-da.md` — Devil's Advocate

## Attachment: Suggested-Reference Check (advisory, #1001)

Suggested-reference check (script output, not a reviewer finding; #1001)
Seats read: R2, R3 (partial).
Not read:
- R2: the report has no suggested-references block.
- R3: the report has no suggested-references block.
No suggested reference could be read.

## Attachment: Reviewer Claim Check (advisory, #1002)

The reviewer claim check did not run: the auditor prompt file it reads is not present in this vendored repository.

## Attachment: Acronym Check (advisory, #849)

### Acronym check (advisory; no reply needed)
Coverage: body, English abstract, Chinese abstract (partial)
Not checked:
- Body, line 55: SVI (the initials before its parentheses do not spell it)
- Body, line 57: PDE (the initials before its parentheses do not spell it)
- Body, line 57: SABR (a definition form this check does not read)
- Body, line 63: SDE (the initials before its parentheses do not spell it)
- Body, line 97: HTTP (the initials before its parentheses do not spell it)
- Body, line 97: REST (the initials before its parentheses do not spell it)
- Body, line 101: PRISMA (the initials before its parentheses do not spell it)
- Body, line 145: SSVI (the initials before its parentheses do not spell it)
- Body, line 181: ALSI (the initials before its parentheses do not spell it)
- Body, line 181: SPX (the initials before its parentheses do not spell it)
- Body, line 193: SPY (the initials before its parentheses do not spell it)
- Body, line 201: RMSE (the initials before its parentheses do not spell it)
- Body, line 203: MSE (the initials before its parentheses do not spell it)
- Body, line 357: AI (the initials before its parentheses do not spell it)
- Body, line 357: DSH (the initials before its parentheses do not spell it)

| Scope | Line | Rule | Acronym | Uses |
|---|---|---|---|---|
| Body | 5 | Not defined | TY | 2 |
| Body | 39 | Not defined | SQ1 | 1 |
| Body | 39 | Not defined | SQ2 | 1 |
| Body | 39 | Not defined | SQ3 | 1 |
| Body | 181 | Not defined | FTSE | 1 |
| Body | 181 | Not defined | JSE | 1 |
| Body | 193 | Not defined | ETF | 1 |
| Body | 193 | Not defined | SPDR | 1 |
| Body | 195 | Not defined | DAX | 2 |
| Body | 203 | Not defined | VolGAN | 1 |
| Body | 351 | Not defined | CRediT | 1 |
| Body | 419 | Not defined | DC | 2 |
| Body | 419 | Not defined | NC | 2 |
| Body | 419 | Not defined | RC | 2 |
