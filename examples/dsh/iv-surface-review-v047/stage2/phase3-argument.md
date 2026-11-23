# Phase 3 — Argument Blueprint

**Run:** `iv-surface-review-v047` · **Stage 2, Phase 3** · **Agent role:** argument builder · **Date:** 2026-11-23
**Inputs:** `phase0-config.md`; `phase1-literature.md`; `phase2-outline.md`; frozen Stage 1 records (`phase3-synthesis.md`, `phase6-final.md`, `search/selected_sources.json`).
**Review-criteria binding status:**

```text
criteria_binding_unavailable
```

No FORMATIVE receipt exists to reuse. This blueprint does not resolve a target review, map criterion ids, copy registry prose, or make a venue-fit claim. The status is carried unchanged from Phases 0 and 2.

## 1. Central Thesis

The four method families for constructing equity-index implied-volatility surfaces are not competing solutions to one problem: they enforce static admissibility at four different loci and license four different kinds of evidence. Once "arbitrage-free" is resolved into a condition, a tolerance, and a verification mode, the corpus's apparent disagreement becomes an evidential division of labour — and its central gap, the absence of any dynamic enforcement or test, becomes visible.

**Scope of the thesis.** The claim is about the 41-source corpus, not the field. It is an interpretive and evidential claim, not a claim that any family is more accurate, faster, or preferable. The framework it proposes is a proposed instrument, not a validated result.

## 2. Sub-Arguments (CER Chains)

### SA-1 — Static admissibility is enforceable in all four families, but each family enforces it on a different object

- **Claim.** Every family can produce a surface that satisfies a static admissibility condition, but the object that satisfies it differs: an admitted parameter set, a minimized objective, a transformed output, or an accepted sample.
- **Evidence.** Parameter domain: P1 (generalized SVI on a structural parameter set), P2 (exact butterfly characterisation via −d1/−d2 monotonicity), P3 (global eSSVI across maturities), P5 (random-coefficient family), P6 (C3 interpolation), P8 (bounded-factor conditions). Output image: R1 (LP repair), R2 (Sinkhorn/MOT projection), R3 (distortion of an arbitrage-free reference), R6 (SANOS construction). S2 (shape-constrained smoothing splines) is the corpus's early constrained-interpolation baseline; it predates the four-family split and is used for lineage, not as a fifth family. Inherited architecture: G1 (VAE over SDE parameters), G6 (trainable hard constraints), G7 (neural-SDE state space), G8 (gated rational network). Penalty: N3 (soft penalties plus a plug-in correction), N4 (GAN with arbitrage loss), N5 (penalty minimization); N1 is a boundary case (gated constraints). Pass-rate branch: G5 (90.8% of generated surfaces pass all tested static conditions).
- **Reasoning.** The static predicate is the same in name — no butterfly or calendar violation — but the quantifier differs. A parameter-domain proof says "all admitted parameters"; a penalty says "the evaluated sample, at this weight and tolerance"; a repair says "the image of this map"; a sampler says "accepted candidates, within test power." Those are four different claims. The corpus's evidence types track the difference: 6 of 8 parametric rows are proof-level, 0 of 6 penalty rows are, and the generation group splits between inherited guarantees (G1, G6, G7, G8) and pass-rate reports (G2, G4, G5).
- **Counter-argument.** The taxonomy is imposed: families overlap (R3 and R6 construct as well as repair; N1 is architecture as much as penalty; G7 is a model, not a data-driven generator), so the "four objects" may be an artefact of classification.
- **Rebuttal.** *Concede and limit.* The boundary cases are real and are flagged (R3, R6, N1, G7). But the distinctions survive them: the mixed cases do not produce the evidence type of the family they resemble, and the clean rows align locus with evidence. If the taxonomy were arbitrary, the proof/test split would not track it. The paper reports the taxonomy as a proposed instrument and discloses the boundary cases rather than claiming a partition.
- **Sections:** §2.3, §4.1–4.4, §6.1.
- **Trace:** `phase6-final.md` §4.2; `phase3-synthesis.md` §5.2–5.3.
- **Strength:** Strong evidence; Valid logic; Medium counter-argument risk (classification).

### SA-2 — Dynamic no-arbitrage is absent from the corpus, not merely unproven

- **Claim.** No source in the corpus enforces or tests a process-level dynamic no-arbitrage condition. The finding is a bounded absence over 41 abstracts, not a claim that the field ignores dynamics.
- **Evidence.** 0 of 41 rows enforce or test a dynamic condition; 0 of 36 in-window rows; 0 of 31 construction rows. Ten rows engage time without a dynamic test: P8, R9, G1, G2, G3, G7, R8, C2, C3, C5. C2 reviews dynamic conditions but does not test them. G7 explicitly limits its claim to static admissibility. C3 constructs path-dependent surfaces that are statically free but does not test dynamic consistency. P8 reports time-indexed arbitrage probabilities for parametric models. C5 is a single-stock panel and is scope-flagged.
- **Reasoning.** A static condition constrains one surface; a dynamic condition constrains a family of surfaces over calendar time, typically through a martingale representation. Coding a row as dynamic requires a stated path-level condition and a check over a path. No row states one. The ten time-engaging rows fail at least one of those requirements: they model time, index by time, or review time, but do not test process consistency. The absence is therefore structural in the coded evidence, not an accident of one metric.
- **Counter-argument.** The absence may be a retrieval or vocabulary effect: papers may test dynamics under labels the search did not capture (e.g., "consistent surface dynamics," "martingale defects," "joint calibration over time"), or abstracts may omit a dynamic test that the full text reports.
- **Rebuttal.** *Acknowledge as limitation, then bound the claim.* The review cannot distinguish a genuine gap from a retrieval effect; it says so. But the claim is about what the corpus licenses, and that remains 0 of 41. The paper reports two possible readings (publication norm vs retrieval effect) and makes the gap the first agenda study rather than filling it by inference.
- **Sections:** §5.1, §6.2.
- **Trace:** `phase6-final.md` §4.5; `phase3-synthesis.md` §5.1.
- **Strength:** Strong (within the bounded corpus); Qualified logic (absence, not proof of field-level absence); High counter-argument risk.

### SA-3 — Proof-level and audit-level evidence are nearly disjoint

- **Claim.** The corpus rarely reports a structural guarantee and a finite-sample violation audit for the same surface. A reader can inspect the proof or the residual, usually not both.
- **Evidence.** 17 rows are coded proof-level; none reports a violation rate in the abstract. Six rows audit their own output: N2 (graph neural operator on 10-year intraday SPX), N6 (DCNN on SABR-generated data), R5 (observation-anchored repair; ~5.4% butterfly floor on 252 OOS SPX days), R7 (Chebyshev + QP; <1% violations, 98–99% inside-spread coverage), G5 (90.8% pass rate), G6 (0.00% at 1e-4 over 15 runs on synthetic SVI). G6 is the only row that also reports a structural guarantee, and it does so on synthetic data. G6 also reports higher total-variance RMSE than SSVI and a soft-penalty MLP.
- **Reasoning.** A proof without an audit is a claim about a mathematical object, not necessarily about the implemented surface; an audit without a proof is a claim about a sample, not a guarantee. For applied use, the two answer different questions: "does this construction admit arbitrage?" and "did this implementation violate a condition on these data?" The corpus's near-disjointness means the reader usually has to choose which question is answered.
- **Counter-argument.** Proofs do not need audits — a theorem is stronger than a test; and abstracts often omit implementation checks that the full text reports.
- **Rebuttal.** *Refute the sufficiency claim; concede the reporting limit.* A theorem is stronger in its domain, but it does not report finite-precision implementation violations, data noise, or the tolerance actually used; G6 shows that a proof-bearing construction can be audited and that doing so is informative. The abstract-level limitation is acknowledged: the review codes what is reported, not what was done. The remedy is a reporting norm and agenda study 3, not an inference that audits exist.
- **Sections:** §5.1, §6.1.
- **Trace:** `phase6-final.md` §4.1, §4.3, Table 1; `phase2-verification.md` audit rows.
- **Strength:** Strong; Valid; Medium counter-argument risk (reporting omission).

### SA-4 — Cross-family comparison is not licensed by the corpus; a ranking would be a category error

- **Claim.** The corpus contains no direct cross-family comparison. Reported numbers are context, not a common scale, so ordering methods by performance is not warranted.
- **Evidence.** Comparability coding: 0 direct / 30 context / 11 not comparable. No row reports the four fields required for a direct comparison: same dataset/panel, same condition set and tolerance, same metric and aggregation, same protocol. Seven metric families appear (price-space, volatility-space, total-variance, bid–ask spread, Wasserstein, hedging P&L, runtime). The only licensed comparisons are within a study: G6 against SSVI and a soft-penalty MLP; N4 against a VAE; N5 against an ANN; R5 across five completion backends. Even the apparent violation-rate family is not comparable: G5 reports a 90.8% pass rate, R5 a ~5.4% butterfly floor, R7 <1% violations, G6 0.00% at a 1e-4 tolerance — different data, definitions, and tolerances.
- **Reasoning.** A comparison requires a shared protocol: the same surface, the same condition set, the same tolerance, the same metric, and the same aggregation. Without those, a difference in a reported number cannot be attributed to the method. The coding result says no pair of rows shares the protocol, so any ordering would compare constructions, datasets, and reporting conventions at once. The correct report is a range with conditions, not a league table.
- **Counter-argument.** The rows all report "violations," so their rates are at least ordinally comparable; a reader can see that 0.00% is better than 5.4%.
- **Rebuttal.** *Refute.* A 0.00% at 1e-4 on synthetic SVI data and a 5.4% floor on 252 SPX days are not points on one scale. The denominators, the tested conditions, the tolerance, and the data-generating process differ. Ordinal comparison would inherit those differences. The paper therefore reports rates as context and confines comparison to within-study baselines; the absence of a common protocol is itself a finding and the second agenda study.
- **Sections:** §5.2, §6.1.
- **Trace:** `phase6-final.md` §4.6; `phase3-synthesis.md` §5.5.
- **Strength:** Strong; Valid; Medium counter-argument risk (reader pressure to rank).

### SA-5 — The cost of a stronger guarantee is measured on one side only; the "lower fit error" claim is unsupported

- **Claim.** The corpus rarely measures both the strength of a guarantee and its cost in fit or residual violations. The claim that penalty or repair routes reduce fit error relative to constrained construction is not supported; the claim that they displace the constraint burden into weights, tolerances, and repair steps is supported.
- **Evidence.** G6 is the clearest paired measurement: hard constraints reach 0.00% violations at 1e-4 over 15 runs but report higher total-variance RMSE than SSVI and a soft-penalty MLP. R5 reports a ~5.4% butterfly floor and finds a cubic-spline backend with the lowest reconstruction error after repair. R7 reports <1% static violations and 98–99% inside-spread coverage in calm years, with stressed out-of-band leakage. G5 reports a 90.8% pass rate without a paired fit-cost comparison. N4 and N5 report accuracy or runtime gains, but not a violation rate against a constrained parametric baseline on the same data. N4 also states that the arbitrage condition cannot be directly learned.
- **Reasoning.** A guarantee is not free: it restricts the admissible set, adds a penalty, or moves the output after fitting. The trade-off is priced only when the same study reports both the guarantee and the fit/residual on the same data. The corpus has one clear paired measurement (G6), and it runs against the "lower fit error" claim; the other rows report one side. The burden-displacement claim is supported because the rows that do report residuals locate the cost in weights, tolerance, repair, or acceptance thresholds.
- **Counter-argument.** Strict guarantees may be cheap in practice; a 90.8% pass rate or a 5.4% floor may be operationally adequate; and fit error is not the only cost that matters.
- **Rebuttal.** *Concede and limit.* The paper does not claim that strict guarantees are expensive in general, nor that any pass rate is inadequate; adequacy requires a loss function and a tolerance the corpus does not supply. It claims only that the corpus does not measure the trade-off well enough to support the "lower fit error" claim, and that the one paired measurement points the other way. Agenda studies 4 and 7 would price the trade-off.
- **Sections:** §5.3, §6.3.
- **Trace:** `phase6-final.md` §4.3, Table 1 (H2); `phase3-synthesis.md` §5.3.
- **Strength:** Moderate; Qualified; Medium counter-argument risk (adequacy).

### SA-6 — Calendar conflation and asymptotic scale relativity inflate apparent dynamic coverage

- **Claim.** Part of the reason the dynamic gap is easy to miss is definitional: maturity-monotonicity is called "calendar arbitrage" even though it is a static condition, and asymptotic arbitrage-free statements are read as finite-strike guarantees.
- **Evidence.** C2 distinguishes static from dynamic conditions. G5, G6, and R5 use calendar conditions in the static (maturity-monotonicity) sense; G7 explicitly limits its claim to static admissibility; C4's asymptotic arbitrage-free result for BBF/SABR/rough SABR is scale-relative, while S3's SABR arbitrage is a finite-strike failure — the two are compatible only in the asymptotic regime. P8 reports time-indexed arbitrage probabilities; C3 constructs path-dependent surfaces; C5 is a dynamic-adjacent single-stock panel. None is a dynamic test.
- **Reasoning.** If "dynamic" is allowed to mean "anything with a maturity axis," then many static rows look dynamic, and the 0/41 result looks implausible. Once the term is fixed to process-level consistency, the count returns to zero. The scale case is the same logic in a different dimension: a guarantee as strikes tend to infinity or as time tends to zero is not a guarantee at the strikes and maturities where a surface is used.
- **Counter-argument.** This is a terminological quibble, not a substantive finding; the underlying methods are unaffected by what we call the condition.
- **Rebuttal.** *Refute.* The terminology changes the evidence count and the claim a method can make. A static calendar condition does not constrain the process, and an asymptotic guarantee does not constrain a finite grid. Naming the difference is what makes the dynamic claim testable. The paper therefore defines both terms in §2 and applies the definitions in §5.1; the correction is not cosmetic.
- **Sections:** §2.1–2.2, §6.2.
- **Trace:** `phase6-final.md` §2.1, §4.5; `phase3-synthesis.md` §5.1–5.2.
- **Strength:** Moderate; Valid; Medium counter-argument risk (definitional).

### SA-7 — The enforcement framework explains the convergence and yields a falsifiable agenda

- **Claim.** The mechanism–evidence–verification triple and the four loci explain why the families converge on the same phrase while producing different evidence, and they generate seven studies whose outcomes would test the framework.
- **Evidence.** The pattern across groups: inherited guarantees (G1, G6, G7, G8) behave like parametric constructions in logical shape; penalized sampling (N4, N5, G5) reports residual or pass rates; construction (P, R6) and repair (R1–R5, R7) differ in what is observed; the boundary cases (R3, R6, N1, G7, C3) are exactly where the mechanism is mixed. G6 is the only row that reports the full triple (structural constraint, 0.00% audit, synthetic data). The seven gaps (§6.3) name what the framework predicts is missing.
- **Reasoning.** If the guarantee is inherited from a deterministic decoder, the learning apparatus does not change the logical form of the claim; if compliance comes from a penalty, the claim is conditional on sampling; if it comes from a map applied after fitting, the object is the image; if it comes from an acceptance test, the object is the accepted sample. Those differences predict the evidence type, and the corpus bears the prediction out. The framework is explanatory, not a ranking: it says what a claim is worth, not which claim is best.
- **Counter-argument.** The framework is descriptive; it may fit any taxonomy post hoc; it has not been tested and could be a relabeling of the four families.
- **Rebuttal.** *Acknowledge as limitation and reframe.* The framework is proposed and unvalidated; the paper says so. Its value is that it makes discriminating predictions: agenda study 1 should produce a dynamic test that no current locus covers; study 2 should produce the first direct comparison; study 3 should show whether proofs survive implementation. If those studies do not discriminate, the framework should be revised. It is not offered as a result, and it does not license a ranking.
- **Sections:** §2.3, §6.1, §6.3.
- **Trace:** `phase3-synthesis.md` §5.2–5.3, §6; `phase6-final.md` §6.1.
- **Strength:** Moderate; Qualified; Medium counter-argument risk (post hoc fit).

## 3. Counter-Argument Register

| ID | Counter-argument | Raised by / alternative reading | Rebuttal strategy | Residual risk |
|---|---|---|---|---|
| CA-1 | The four-family taxonomy is imposed; families overlap | R3, R6, N1, G7; any boundary row | Concede and limit: flag boundaries; show evidence type tracks locus; label taxonomy as proposed | Medium — a partition is not claimed, but readers may reify it |
| CA-2 | Dynamic absence is a retrieval or vocabulary artefact | Search scope; abstract-level coding; C2's review existence | Acknowledge as limitation; bound the claim to the corpus; make it agenda study 1 | High — cannot be resolved without full-text or a new search |
| CA-3 | Proofs do not need audits; abstracts omit checks | Proof-bearing rows; publication norms | Refute sufficiency for applied use; concede reporting limit; cite G6 as feasibility | Medium |
| CA-4 | Violation rates are comparable enough to rank | G5, R5, R7, G6 numbers | Refute: different data, definitions, tolerances; report ranges; no ranking | Medium — reader pressure persists |
| CA-5 | Penalty/repair reduce fit error; strict guarantees are costly or unnecessary | N4, N5 accuracy claims; G5 pass rate | Concede adequacy is not assessed; note one paired measurement runs the other way; agenda study 7 | Medium |
| CA-6 | Calendar arbitrage is dynamic; the terminology point is cosmetic | Common usage of "calendar arbitrage" | Refute: definition changes the count and the claim; static calendar is a maturity condition | Medium |
| CA-7 | The framework is post hoc description | Any taxonomy; absence of validation | Acknowledge as limitation; state falsifiable predictions; agenda as test | Medium |

## 4. Logical Flow

| Section | Argument move | Chains | Sources |
|---|---|---|---|
| 1 Introduction | The phrase is used as a completion label; the problem is that the label hides different claims | SA-1 setup, SA-2 setup | S3, S4, S5, C2 |
| 2 Framework | Define static conditions, dynamic requirement, and the enforcement triple; introduce the four loci | SA-1, SA-6, SA-7 | S1, P1, P2, P8, C2, C3, C4, C5, G7, R3, R6, N1 |
| 3 Method | Fix the evidence rules: corpus, verification, evidence status, comparability | all chains (method) | corpus-level; C5 flag |
| 4 Findings I | Show the four mechanisms and their evidence types family by family | SA-1, SA-7 | P1–P8, N1–N6, R1–R9, G1–G8 |
| 5 Findings II | Cross-tab the evidence: proof vs audit, comparability, evaluation coverage | SA-2, SA-3, SA-4, SA-5, SA-6 | audit rows; P/R/G representatives; C1 |
| 6 Discussion | Resolve the phrase into condition + tolerance + verification; interpret the dynamic void; propose the agenda | SA-2, SA-3, SA-4, SA-5, SA-6, SA-7 | C1–C5, P8, G1–G5, G7, R1, R5–R7, N2, N4, N5, P2, P6, S5 |
| 7 Conclusion | State what survives the limitations; no new evidence | all chains (synthesis) | none new |

**Narrative test.** A reader should be able to answer three questions after §5: what each family's "arbitrage-free" claim is about (SA-1); what evidence supports it (SA-3); and why the numbers cannot be ranked (SA-4). §6 then answers why the gap persists (SA-2, SA-6) and what would close it (SA-7).

## 5. Argument Strength Assessment

| Sub-argument | Evidence Strength | Logic Validity | Counter-Arg Risk | Basis |
|---|---|---|---|---|
| SA-1 Four objects | Strong | Valid | Medium | Multiple proof-level P/R/G rows; evidence type tracks locus; boundary cases disclosed |
| SA-2 Dynamic absence | Strong | Qualified | High | 0/41, 0/36, 0/31; bounded to abstracts; retrieval alternative acknowledged |
| SA-3 Proof/audit gap | Strong | Valid | Medium | 17 proof rows, 6 audit rows, G6 only both; abstract-level reporting limit |
| SA-4 No comparability | Strong | Valid | Medium | 0 direct / 30 context / 11 not comparable; seven metric families; four-field test |
| SA-5 Cost one-sided | Moderate | Qualified | Medium | One clear paired measurement (G6); sparse fit-cost reporting; adequacy not assessed |
| SA-6 Calendar/scale | Moderate | Valid | Medium | Definitional analysis; C2, C4, S3, G7, G5, G6, R5; no field-level claim |
| SA-7 Framework/agenda | Moderate | Qualified | Medium | Explanatory fit; proposed, not validated; seven falsifiable studies |

**Reading the table.** "Strong" means multiple rows and an unambiguous coding result within the corpus; "Moderate" means the pattern is real but the measurements are sparse. "Qualified" means the conclusion holds only under the stated bounded-absence or proposed-framework caveat. No chain is rated Strong on a field-wide claim.

## 6. Limitations of the Argument

1. **Evidence base.** Abstract-level only (34 full / 4 partial / 3 metadata-only); 11 preprints; single analyst; no full text, proof, or code check; no theorem re-derived and no reported number recomputed.
2. **Inference.** Absence findings are bounded to the 41 abstracts, not the field; the framework is proposed, not validated; no causal claim and no ranking.
3. **Instruments.** The four-family taxonomy, the seven-dimension matrix, and the A/B/C quality labels are review instruments, not validated scales. Boundary cases (R3, R6, N1, G7, C3) are disclosed, not resolved.
4. **Coverage.** English-only, OpenAlex-only, US-index-dominated (10 of 12 known-provenance rows); one query lost after HTTP 429; 40 discretionary exclusions; four replacement decisions after abstract reading.
5. **Scope.** C5's single-stock panel is a disclosed exception; no index-transfer claim. No PRISMA or PRISMA-ScR claim; no meta-analysis; no effect sizes.

**Falsifiers.** Each chain names what would overturn it:

| Chain | What would overturn it |
|---|---|
| SA-1 | A row whose evidence type contradicts its locus, or a family that cannot be classified even after boundary treatment |
| SA-2 | A source with a stated path-level dynamic condition and a test over a path |
| SA-3 | A proof row that reports an implementation audit, or an audit row that also proves a structural guarantee (beyond G6) |
| SA-4 | Two rows meeting all four comparability fields (dataset, condition/tolerance, metric/aggregation, protocol) |
| SA-5 | A paired measurement showing a stronger guarantee improves fit at no residual cost |
| SA-6 | A source that uses "calendar" to mean a process-level dynamic condition, and tests it |
| SA-7 | A boundary row the framework cannot place, or agenda studies that produce no discriminating evidence |

## 7. Notes for the Draft Writer (Phase 4)

**Use the chains as the spine.** §4 carries SA-1 and SA-7; §5 carries SA-2 through SA-6; §6 interprets and proposes. Do not introduce a chain in §7 that was not set up earlier.

**Numbers and attribution.**
- Aggregate counts (17/16/8; 0/30/11; 34/4/3; 11/13/17; 0/41) are the review's coding. Attribute them to "this review's coding," never to a source.
- Per-source numbers (G5's 90.8%; R5's ~5.4%; G6's 0.00% at 1e-4; R7's <1% and 98–99%) are the source's reported result. Report them with the source, dataset, and tolerance when stated.
- 41/41 DOI resolution and 0 retractions are verification results, not quality evidence.
- Do not call a numerical test "arbitrage-free"; write "reported no violations at tolerance X on dataset Y" or "the method's admissibility claim is conditional on the penalty and tolerance."

**Language discipline.**
- "The corpus" or "these 41 sources," not "the literature."
- "Reports" or "codes," not "proves," unless the source proves a theorem.
- "Static calendar condition" for maturity monotonicity; "dynamic" only for process-level consistency.
- "No direct comparison" and "no ranking," not "outperforms" or "best."
- No PRISMA/PRISMA-ScR claim; "PRISMA-style" only in the method appendix with the explicit disclaimer.
- Metadata-only rows (P4, P7, R4) at title level only; preprints labeled.

**Structure and budget.**
- 7,400 body words; §1 700, §2 1,100, §3 900, §4 1,500, §5 1,250, §6 1,300, §7 650. Hard ceiling 8,000.
- Tables T1–T6 and Figures F1–F2 as planned; do not add a table that implies a ranking.
- Abstract: English 150–250 (target 200); Simplified Chinese 300–500 characters (target 420); 6 keywords each; independently written; no citations.
- All 41 references cited; reuse the Stage 1 APA list; no new sources.

**Declarations.** Data Availability; Ethics (not applicable); Author Contributions (CRediT); COI (none); Funding (none); AI use (bounded Stage 1 wording); Limitations. Responsible-use statement: dual-use Level None; not investment advice.

**Review-criteria line.** If the manuscript includes a methods/limitations note on review criteria, it must use exactly `criteria_binding_unavailable` and must not claim venue fit, submission readiness, or criterion coverage.

**Forbidden moves.** Fabricated citations; a new source; a field-wide absence claim; a league table; upgrading a test to a proof; treating a preprint as peer-reviewed; treating a metadata-only row as evidence for its claim; calling a calendar condition dynamic; claiming H2's fit-improvement clause is supported; claiming the framework is validated.

## 8. Review-Criteria Continuity

The approved outline carries `criteria_binding_unavailable`; no FORMATIVE receipt, target-review authority, or criterion-id coverage plan exists. This blueprint therefore does not reuse a receipt, resolve a target, copy registry statements, collapse interdisciplinary conflicts, or create a second receipt. A review criterion, if one had been bound, could identify an argument or evidence need but could not license invented evidence, results, or methods, or a silent thesis change. If a `ReviewTargetContext` appears later, this blueprint is not retrofitted; a new Phase 0 record and a new Phase 2 coverage plan would be required.

## 9. Handoff to Phase 4

The argument blueprint is complete and consistent with the approved outline. Phase 4 may draft from it without adding evidence. The draft must preserve: the bounded-absence wording for SA-2; the reporting-limit caveat for SA-3; the no-ranking rule for SA-4; the adequacy caveat for SA-5; the definitional correction for SA-6; and the proposed-not-validated status of SA-7. Any draft passage that cannot be traced to a source in `phase1-literature.md` §5 or to a review-coding result in the Stage 1 records is out of scope.
