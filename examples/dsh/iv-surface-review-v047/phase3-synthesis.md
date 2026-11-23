# Phase 3 — Synthesis Report

**Run:** `iv-surface-review-v047` · **Stage 1 (deep-research, `full` mode)** · Phase 3 ANALYSIS
**Date:** 2026-11-23
**Inputs:** `phase1-scoping.md`, `phase2-bibliography.md` (41 sources), `phase2-verification.md`, `search/selected_sources.json`
**Process:** synthesis_agent (thematic synthesis → contradiction resolution → convergence map → gap analysis → theoretical integration), then devils_advocate CHECKPOINT 2.
**Read scope:** abstracts as recorded in Phase 2 (34 full, 4 partial, 3 metadata-only). No full text was retrieved in this run; no proof was re-derived.

**Coding rules used throughout.** (a) *Static no-arbitrage* = conditions that make one surface admissible: strike convexity/butterfly, monotonicity of total variance in maturity ("static calendar"), and their price-space equivalents. (b) *Dynamic no-arbitrage* = conditions on the joint law of surfaces indexed by calendar time, i.e. that no self-financing strategy in the option panel is free. A maturity-monotonicity condition on one date is **not** coded as dynamic, however the source labels it. (c) Evidence statuses are the *reported* statuses recorded in Phase 2; this synthesis does not upgrade a numerical test to a proof. (d) No ranking, league table, or vote count is produced or implied.

---

## 1. Evidence Matrix

41 rows, one per Phase 2 source. Comparability classes: **DC** = directly comparable (Phase 2 recorded a dataset *and* metric *and* protocol matching another row); **RC** = reported for context (the row reports a data-based result on data or metrics the corpus cannot match); **NC** = not comparable (theory only, metadata-only, or scope-flagged out of the index frame). Family codes: P parametric construction, N penalty/constrained learning, R projection/repair, G generation/filtering, C constraints/evaluation, S seminal baseline.

| ID | Fam | Core mechanism | Static no-arb handling | Dynamic no-arb handling | Evidence | Data / market | Fit or accuracy metric reported | Comp. | Note |
|---|---|---|---|---|---|---|---|---|---|
| P1 | P | Generalized SVI total-variance family with a restricted, butterfly-free parameter domain | Guarantee by parameter-domain restriction (theorem) | None; one surface per date | proof | None (analytical) | None | NC | Shows arbitrage-free members exist outside the standard SVI slice; no fit evidence |
| P2 | P | Exact characterization of when SVI total variance is butterfly-arbitrage-free; least squares confined to that domain | Complete butterfly characterization, calibration restricted to it | None | proof | Market data, market not identified | Fit performed, no metric in abstract | RC | Butterfly only in the abstract; "fits market data" is asserted, not quantified |
| P3 | P | Global all-maturity eSSVI parameterization that is arbitrage-free across maturities at once, vs sequential (Zeliade) calibration | Guarantee by joint parameterization over maturities | None; cross-maturity static only | proof | Market data, dataset unspecified | None | RC | Joint-in-maturity construction; the abstract gives neither dataset nor fit numbers |
| P4 | P | Robust calibration plus arbitrage-free interpolation of SSVI slices | Claimed in title only; unverified | Not visible | assumption | Not visible | None | NC | Metadata-only; the sequential counterpart of P3 cannot be checked here |
| P5 | P | Random-coefficient parameterization of implied vol with an analytic guarantee; admits bimodal short-dated densities | Analytic guarantee | None | proof | Short-term index and single-name options, event dates | None | RC | Extends expressiveness without leaving the guaranteed set; no fit metric |
| P6 | P | Piecewise-quadratic local variance gamma; C³ arbitrage-free interpolation of raw quotes | Construction-level guarantee (C³ interpolation) | None | proof | Raw option quotes, market unnamed | None; fewer knots and lower cost only asserted | RC | Interpolation rather than calibration; cost claims unquantified |
| P7 | P | Necessary and sufficient no-arbitrage conditions for the SSVI/S3 curve | Claimed in title only; unverified | Not visible | assumption | Not visible | None | NC | Metadata-only and non-peer-reviewed; the only "necessary and sufficient" claim in P |
| P8 | P | Arbitrage probabilities for Gaussian factor models; bounded-factor conditions; arbitrage-free Jacobi modification preserving empirical features | Deterministic necessary and sufficient conditions under a bounded factor framework | Explicitly time-indexed: probabilities of calendar-spread, call-spread and butterfly arbitrage across time | proof | None (theory); applied to the Cont–Vuletić model | None | NC | The only parametric source that treats arbitrage across time rather than across strikes |
| N1 | N | Gated neural network whose multiplicative hidden layer plus slope/weight selection satisfies surface constraints | Constraints imposed by the architecture (gating) | None | numerical test | S&P 500 options | Out-of-sample forecasting and hedging reported to beat alternatives | RC | Classified N but enforced architecturally, like G6–G8: a classification friction |
| N2 | N | Graph neural operator mapping raw quotes to smoothed IV surfaces | Reported adherence to critical no-arb constraints; no guarantee | None | numerical test | Ten years raw intraday S&P 500 options | Accuracy and robustness vs classical NNs and SVI | RC | Strongest empirical no-arb claim in N, still self-reported and never audited by a C1-style detector |
| N3 | N | Neural "plug-in" correction with a soft penalty on top of classical IVS models | Soft penalty only; no guarantee | None | numerical test | Unnamed market, sparse/erroneous quotes | Prediction accuracy and uncertainty, no numbers | RC | Correction layer rather than construction; market withheld in abstract |
| N4 | N | GAN on sparse `ALSI` index options with a static-arbitrage loss term | Penalty improves fit but cannot enforce; "cannot directly learn the condition" | None | numerical test | JSE ALSI (South Africa), sparse index options | Wasserstein distance to historical distribution; GAN over VAE | RC | Only African/emerging index in the corpus; the penalty limitation is stated in the abstract |
| N5 | N | GAN with no-arbitrage regularisation and a distribution discriminator, shallow networks | Violations "minimised", not removed (conceded in title) | None | numerical test | Market unnamed | Accuracy and runtime vs an ANN baseline | RC | The residual-not-guarantee meaning of "arbitrage-free" in its clearest form |
| N6 | N | Derivative-constrained NN: the loss contains strike and maturity derivatives tied to no-arb inequalities | Differential-inequality loss terms | Maturity-derivative term present; no dynamic test | numerical test | Synthetic SABR-generated prices | Stability across configurations, no numbers | RC | Closest N approach to the differential view of admissibility; synthetic only |
| R1 | R | Linear-program repair: minimal price change inside bid–ask bounds subject to no-arbitrage | Enforced by LP constraints; changes only what is necessary | None | numerical test | Traded option prices, source unnamed | Calibration robustness/error improved, no numbers | RC | A strict projection by construction; "minimal change" is its defining claim |
| R2 | R | Sinkhorn / martingale-optimal-transport projection of bid–ask quotes onto the arbitrage-free set | Projection onto the no-arb set, convergence proved | None | proof | Bid–ask quotes, market unnamed | None | RC | Only transport-theoretic projection in the corpus; partial abstract limits checking |
| R3 | R | Distortion of an arbitrage-free reference call-price function for strike interpolation, then maturity interpolation | Static guarantee by construction from the reference | Maturity interpolation only, not calendar time | proof | None (construction); recovers Kahalé under Black–Scholes | None | NC | A repair that is really a construction: the reference is already admissible |
| R4 | R | Joint arbitrage-free smoothing of American call and put surfaces | Claimed in title only | Not visible | assumption | Not visible | None | NC | Metadata-only; the only American-exercise source, so its mechanism cannot be assessed |
| R5 | R | Deterministic two-step repair of an observed grid (calendar in total variance, butterfly in normalised call price), touching only unobserved cells | Enforcement by construction on the completed grid | Calendar = maturity monotonicity only | numerical test | SPX, OptionMetrics Ivy DB, 252 out-of-sample days, five completion backends | Calendar violations ≈0; butterfly floor ≈5.4%; cubic spline plus repair lowest reconstruction error | RC | Most explicit violation floor in the corpus; attributes it to finite-precision rounding |
| R6 | R | SANOS: strictly arbitrage-free nonparametric surface via LP with bid–ask penalties and a positive discrete local-vol parameterization | Strict guarantee claimed, reduced to parameter positivity | Surface spans maturity and strike axes; single date | proof | S&P 500 illustration | None quantified | RC | Strictest "strictly" in the corpus, with a short feasibility argument only |
| R7 | R | Chebyshev tensor basis with static no-arbitrage as linear inequalities in a convex QP; post-fit density "fog" preserving global admissibility | Constrained convex QP; post-fit perturbation keeps admissibility | None | numerical test | Equity option panels, market unnamed | 98–99% inside-spread coverage in calm years; <1% static violations | RC | Reports the leakage cost of its own post-fit step under stress: a rare self-audit |
| R8 | R | Optimal-transport-inspired arbitrage-free transforms (extrapolation, skew change, event, arbitrage removal, surface dynamics) | Asserted shaping; no proof | Claims to generate surface dynamics as one transform | assumption | None | None | NC | Programmatic rather than evidential: neither proved nor tested |
| R9 | R | Continuous-time Markov-chain approximation whose non-negative transition probabilities make surfaces arbitrage-free | By construction (non-negative transition probabilities) | Continuous-time dynamics; no dynamic no-arb audit | numerical test | SPY, 2,695 options, 28 maturities, 2018-02-08 | Adequate/competitive/stable, but slow | RC | Only repair source with a full time axis; the cheapness of its check is its selling point |
| G1 | G | VAE over SDE parameters (regime-switching, additive Lévy); decode to arbitrage-free surfaces | Guarantee inherited from the SDE model class | Regime-switching dynamics generated; static per surface | proof | Historical surfaces, market unspecified | Generative quality tested, no metric | RC | The guarantee comes from the decoder's model class, not from training |
| G2 | G | VolGAN on SPX IV time series plus underlying; joint surface and underlying scenarios | Claimed in title; mechanism not described | Generates joint dynamics; hedging and VIX realism evaluated | numerical test | SPX IV time series | Hedging beats Black–Scholes delta and delta–vega | RC | Best dynamic-realism evidence in the corpus, weakest description of enforcement |
| G3 | G | Simulation of arbitrage-free surfaces reconciling static constraints with IV co-movement statistics | Static constraints reconciled in simulation | Ambition stated; abstract truncated mid-argument | assumption | SPX historical context | None visible | RC | Partial abstract (448 chars) cuts the argument; treat as programmatic |
| G4 | G | GAN denoiser mapping noisy, arbitrage-violating surfaces to smooth arbitrage-free ones | Empirical de-arbitrage; no guarantee | None | numerical test | Synthetic noise, market unnamed | Lower MSE and runtime than traditional smoothing | RC | Pairs naturally with C1 as generator plus detector; the pair is never run jointly |
| G5 | G | VAE with differentiable calendar, call-spread and butterfly penalties plus latent flow matching | Penalties only; 90.8% of generated surfaces pass all tested conditions | None | numerical test | Empirical surface distribution, market unnamed | 90.8% all-condition pass rate; Wasserstein distances | RC | The corpus's clearest quantitative "arbitrage-free = pass rate" statement |
| G6 | G | Architectural hard constraints: input-convex blocks for log-moneyness convexity, non-negative maturity ramps for monotonicity | Hard architectural guarantee (Durrleman audited empirically) | Calendar = maturity monotonicity only | proof | Synthetic rejection-sampled SVI slices plus Gaussian noise, 15 runs | 0.00% violations at tolerance 1e-4; total-variance RMSE above SSVI and soft-penalty MLP | RC | The only row that both guarantees and audits, and the only one reporting the fit cost of the guarantee |
| G7 | G | Neural SDE whose drift and diffusion networks preserve static no-arbitrage linear inequalities by construction | Constrained state space (guarantee for the modelled state) | State evolves in time; explicitly not a dynamic-arbitrage guarantee | proof | Heston–SLV simulated data | Calibration validated, no metric | RC | The clearest statement of the static/dynamic boundary in the corpus |
| G8 | G | Gated network "rational by design" that encodes a valid call-price surface | Guarantee by architectural encoding | None | proof | Pricing benchmarks, market unnamed | Generalisation improved, no numbers | RC | Earliest architectural-guarantee network here; no no-arb audit reported |
| C1 | C | Neural-network detection of model-free static arbitrage whenever present; solves a convex semi-infinite program | Detector, not constructor; detection guarantee | None | proof | Real financial data examples | Detection tractability and robustness, no numbers | RC | The corpus's only independent auditor; never applied to another row's output |
| C2 | C | Review of static and dynamic no-arbitrage conditions, ending with a recommended condition group | Enumerates sufficient and close-to-necessary conditions | The only source that explicitly discusses dynamic arbitrage conditions | assumption | None | None | NC | Narrative evidence with no worked example; the conceptual backbone of the dynamic gap |
| C3 | C | Path-dependent IV model: two path-dependent ATM SSVI parameters plus PVD/OU/Jacobi, producing static-arbitrage-free surface paths | SSVI core guarantees static admissibility | Model of surface paths over time; dynamic consistency not discussed | proof | SPX/VIX-style equity-index evidence | Explains much ATM-forward IV movement up to two years, no R² | RC | Bridges static guarantee and empirical path dependence without closing the dynamic gap |
| C4 | C | Proves BBF, SABR and rough SABR formulas are asymptotically arbitrage-free under their models | Asymptotic (small-maturity) guarantee | None | proof | None | None | NC | Establishes that "arbitrage-free" is scale-relative; the asymptotic caveat is the finding |
| C5 | C | SABR strict-local-martingale and martingale-defect conditions as bubble indicators | Diagnostic of model-implied arbitrage-like behaviour | Dynamic-adjacent: martingale defects over a panel | numerical test | 2,576 stocks, 26 years | Defect absorption, no summary statistic | NC | Scope-flagged single-stock panel; the only longitudinal dynamic-adjacent evidence, out of index scope |
| S1 | S | Sufficient closed-form conditions for static-arbitrage-free SVI | Sufficient conditions (not necessary) | None | proof | SPX numerical example | "High-quality fits" asserted, no metric | RC | The canonical sufficient-condition baseline that P2 later completes |
| S2 | S | Shape-constrained natural smoothing splines for the SPD | Shape constraints built into the spline basis | None | numerical test | No market results in abstract | None | NC | Establishes the cost of ignoring constraints: negative transition probabilities, false Greeks |
| S3 | S | Explicit SABR formula shown arbitrageable at low strikes; replaced by a 1-D forward PDE for the density | Finite-strike repair of an asymptotic formula | None | numerical test | Model prices, no market data | Matches explicit curves except a low-rate boundary layer | RC | Practitioner-venue source; the canonical "asymptotic is not arbitrage-free" demonstration |
| S4 | S | Nonparametric inversion of CBOE S&P 500 prices into a state- and time-dependent vol function | No arbitrage enforcement | None | assumption | CBOE S&P 500, 1990s | None | RC | Pre-constraint baseline: flexible but unconstrained |
| S5 | S | Semiparametric factor model with VAR dynamics on DAX index options | No arbitrage constraint | Factor dynamics over time, unconstrained | assumption | DAX index options, 2006 | None | RC | The corpus's only non-US index source; pre-dates the constraint literature |

**Matrix accounting (traces to Phase 2):** 41 rows; evidence status 17 proof / 16 numerical test / 8 assumption; abstracts 34 full / 4 partial (R2, G3, C4, S1) / 3 metadata-only (P4, P7, R4). Comparability classes: **0 directly comparable, 30 reported-for-context, 11 not comparable.** Zero cross-study comparability is a finding, not an omission: no two rows share dataset, metric, and protocol, so no column-wise comparison across families is licensed anywhere in this file. Within-study baselines exist (G6 against SSVI and a soft-penalty MLP; N4 GAN against VAE; N5 against an ANN; R5 across five backends) and are used only as internal orderings, never as corpus-level comparisons.

---

## 2. Key Themes

Seven themes. Each carries an evidence-strength label, the sources it rests on, and the synthesis (integration, not summary).

### Theme 1 — "Arbitrage-free" is a static-surface predicate in all 41 rows; dynamic no-arbitrage is named but never enforced (Strong)

Sources: all 41. The coded matrix contains no row in which a method enforces, or a study audits, no-arbitrage for a *family of surfaces indexed by calendar time*. Ten rows touch time in some way — P8 (arbitrage probabilities over a factor model), R9 (continuous-time chain), G1 (regime-switching decoder), G2 (joint scenarios), G3 (stated ambition), G7 (constrained state space), R8 (asserted dynamics transform), C2 (condition review), C3 (path-dependent model), C5 (martingale defects) — but none converts that into a dynamic no-arbitrage guarantee or test. The construct that the literature calls "arbitrage-free" is therefore a property of a snapshot; the process-level property that the RQ names as the second half of its object is, in this corpus, programmatic. This is an absence result bounded by the read scope (34 full abstracts, 4 partial, 3 metadata-only) and stated as such in §7.

### Theme 2 — Four enforcement loci, four different meanings of the same word (Strong)

The four families do not disagree about a fact; they attach the word "arbitrage-free" to four different objects. In P it is a theorem about a parameter set (P1, P2, P3, P5, P6, P8, plus R3, R6, S1). In N it is a residual that is minimised (N4, N5) or an architectural side-effect (N1). In R it is the image of a map applied to an observed surface (R1, R2, R5, R7). In G it is either a pass rate on a sample (G5, 90.8%) or an inherited model-class property (G1, G6, G7, G8). Counted by reported status: 17 proof, 16 numerical test, 8 assumption — and the 8 assumptions include all 3 metadata-only rows and both pre-constraint baselines. The word travels; the referent does not.

### Theme 3 — Proof and audit are produced by disjoint source sets (Moderate)

Seventeen rows claim a proof-level static guarantee; six report residual, adherence, or stability information (N2, N6, R5, R7, G5, G6). Exactly one row, G6, does both — and it does so on synthetic rejection-sampled SVI slices rather than market surfaces. The corpus therefore contains no instance of "theorem plus audit on observed quotes". This is the central evidential weakness the four-family literature shares, and it is structural rather than incidental: a proof is cheap for a construction that restricts a parameter domain, and expensive for anything that must be evaluated on real quotes.

### Theme 4 — Where the cost of the guarantee is measured, it points one way: tighter constraint, worse fit (Emerging — single-source for the quantified direction)

G6 reports 0.00% violations at tolerance 1e-4 across 15 runs and, in the same study, total-variance RMSE higher than both SSVI and a soft-penalty MLP. R5 reports a persistent butterfly floor of ≈5.4% after repair while a cubic spline plus repair has the lowest reconstruction error among five backends. G5 reports 90.8% all-condition pass rate. R7 reports <1% static violations with 98–99% inside-spread coverage in calm years and controlled leakage under stress. The direction is consistent — constraint strength is paid for in fit or in residual — but only G6 measures both sides on one dataset, so the strength label stays Emerging. The complementary literature (penalty methods reporting accuracy gains, N4, N5) never reports a violation rate against a constrained parametric baseline, so the two halves of the trade-off are never priced together.

### Theme 5 — The condition literature is a monotone refinement, and "arbitrage-free" is scale-relative (Moderate)

The corpus contains a visible lineage: sufficient conditions for SVI (S1) are completed into an exact butterfly characterization (P2); a global rather than sequential construction follows (P3, with P4 as its unverified sequential counterpart); a necessary-and-sufficient claim appears only in an unrefereed preprint (P7); an asymptotic guarantee is proved for three model formulas (C4) while the same asymptotic formula is shown arbitrageable at finite strikes (S3); and a strict finite-grid construction claims strictness by reducing to parameter positivity (R6). Read together, the family of statements is not contradictory but graded — and the gradient is in the *scale* at which arbitrage is excluded (all strikes vs low strikes; all maturities vs asymptotically; a grid vs a continuum). No source states the scale at which its own claim stops holding as a headline result except C4 and S3.

### Theme 6 — Evaluation vocabulary is fragmented, and family-local metrics cannot be exchanged (Strong)

The corpus draws on at least seven metric families: violation rate (R5, R7, G5, G6), implied-vol or total-variance RMSE (G6, R5), Wasserstein distance (N4, G5), hedging P&L relative to deltas (G2, N1), inside-spread coverage (R7), detection performance (C1), and runtime (R6, R9, N5, G4). No two rows share a metric *and* a dataset. Because Phase 2 declined to rank (correctly), the consequence is that comparative claims about families can only be made about *kinds of evidence*, never about performance. This is why §1 has 0 directly-comparable rows and why §5's evaluation matrix is a coverage map rather than a score.

### Theme 7 — Convergence: generation-filtering is splitting into a learned-parametric branch and a penalised-sampling branch (Moderate)

G1, G6, G7, G8 and N1 place the constraint in the decoder or architecture, so their guarantee is inherited from a deterministic map — structurally the parametric family with a learned parameterization. G2, G4, G5, N4 and N5 place it in the loss and report residuals or assertions. The split predicts evidential behaviour: inherited-guarantee rows claim proof-level status and report no violation rate (except G6, which audits), while penalised rows report pass rates and no guarantee. If the field converges, it will be on the architecture side, because it inherits proofs; the cost is that expressiveness is capped by whatever class the architecture can encode, which is exactly what G6's RMSE penalty measures.

### Hypothesis status against the Phase 1 hypotheses

| H | Phase 1 hypothesis | Verdict from this corpus | Basis |
|---|---|---|---|
| H1 | Static constraints mostly by construction in the parametric family; dynamic consistency usually asserted or tested, not proved | **Half supported, half disconfirmed.** Static-by-construction holds (6 of 8 P rows are proof-level). The second clause is disconfirmed in direction: dynamic consistency is *absent*, not asserted-and-tested. | P1–P6, P8; C2; no row with a dynamic test |
| H2 | Penalty and projection-repair report lower fit error, moving the burden into a tolerance, weight, or repair step rarely validated out of sample | **Second clause supported, first clause not supported.** No penalty or repair row reports a lower fit error against a constrained parametric baseline on the same data; G6 reports the opposite direction (constraint costs RMSE). The tolerance/weight/repair displacement is visible (N4, N5, R5, R7). | N4, N5, R5, R7, G6 |
| H3 | Generation-filtering "arbitrage-free" means "not rejected on this sample" | **Supported for the penalised branch, disconfirmed for the inherited-guarantee branch.** G5 (90.8%) is a sample statement; G1, G6, G7, G8 are model-class or architecture statements. | G5 vs G1, G6, G7, G8 |

---

## 3. Contradictions and Tensions

Eight tensions, each with positions, sources, a resolution verdict (reconcilable / conditional / irreconcilable on current evidence), and the observation that would resolve it. These are candidate tensions assessed at the level of claims, not an exhaustive pairwise sweep.

| # | Tension | Position A (sources) | Position B (sources) | Verdict | What would resolve it |
|---|---|---|---|---|---|
| T1 | Proof-level static admissibility vs. empirical dynamic behaviour | Static exclusion is proved or constructed (P1, P2, P3, P5, P6, P8, R2, R3, R6, G1, G6, G7, G8, S1, C1, C3, C4) | Surface paths are modelled or evaluated empirically (C2, C3, G2, G7, R8, R9, C5) | Reconcilable — different objects. No row proves a process-level statement, and the rows that model paths say so (G7 explicitly). | A stated and tested process-level condition on one panel (Gap 1). |
| T2 | Expressiveness vs. constraint strength | Admissible sets can be enlarged while staying inside a guarantee (P5 random coefficients, P8 factor models, R7 Chebyshev basis plus admissibility-preserving perturbation, G1 latent SDE classes) | Tightening the constraint costs fit (G6: RMSE above SSVI and soft-penalty MLP; R5: residual floor persists after repair) | Conditional — enlarging the set is possible in principle; the corpus supplies one measurement of its cost and none of its benefit. | G6's design repeated across families on one dataset (Gap 2). |
| T3 | Data-free parametric structure vs. data-hungry learning | Analytical constructions need no training sample and make universal statements (P1, P2, P3, R2, R3, R6, S1) | Learning methods trained on large samples (N2 ten years intraday SPX; G2 SPX time series; G5; G4; N1) | Reconcilable — complementary tasks; the learning rows estimate a surface from quotes, the analytic rows characterize an admissible set. | Not a factual dispute; a quote-count scaling curve would show where each helps (Gap 5). |
| T4 | Interpolation and overfitting vs. no-arbitrage guarantees | Flexible or minimal-perturbation fits with weak constraints (S2 shape-constrained splines, R1 minimal-change repair, R9 Markov chain on 2,695 quotes, N3 sparse-data correction) | Strict constructions with no out-of-sample interpolation audit (R6, P1, P3, P5, P6) | Irreconcilable on current evidence — no row measures interpolation error *at* the boundary where its guarantee binds; G6 measures error under a guarantee and finds it worse. | Hold out extreme strikes and maturities and measure error at the guarantee boundary (Gap 3). |
| T5 | Quote noise vs. test rejection | Low residual is achievable: 0.00% on clean synthetic data (G6), calendar violations ≈0 (R5), <1% static violations (R7) | Material residual on empirical data: 90.8% pass rate on all tested conditions (G5), butterfly floor ≈5.4% after repair (R5) | Conditional — indistinguishable from a difference in measurement model (noise, tolerance, test power), because no row estimates either. | Estimated noise floor plus a power calculation on injected arbitrage (Gap 4). |
| T6 | Single-index vs. multi-index generality | 10 of 12 known-provenance rows use US equity-index data (SPX, SPY, CBOE S&P 500) | Two non-US rows: DAX (S5, 2006, unconstrained) and JSE ALSI (N4, 2022, sparse) | Irreconcilable — no row applies one method to two indices, so index generality is unmeasured, not merely untested. | One method, three indices, identical protocol (Gap 6). |
| T7 | Sufficient vs. necessary conditions | Sufficient conditions are enough for construction (S1, P1, P5, P6, R3, R6) | Completeness is claimed or approached (P2 exact characterization; P7 claims N&S but is unverified; C4 asymptotic only; S3 shows finite-strike failure) | Reconcilable as a refinement lineage, except P7, whose N&S claim cannot be checked at abstract level. | Full-text check of P7; a finite-strike counterpart to C4. |
| T8 | "Calendar" in the static sense vs. "calendar" in the dynamic sense | Calendar means maturity monotonicity of total variance within one date (R5, G5, G6, N6, the P1-type conditions) | Calendar means consistency of the surface across dates (C2, C3, P8, C5, G7's explicit caveat) | Reconcilable by definition — but currently conflated, which inflates apparent dynamic coverage and is the most consequential definitional problem in the corpus. | Keep the two constructs as separate coding columns, as §1 does, and state the distinction in the report. |

**Resolution notes.** T1, T3, T7 and T8 are reconciled by construct separation and are treated as settled for this synthesis. T2 and T5 are conditional: each has a plausible measurement that would settle it and neither measurement exists in the corpus. T4 and T6 are irreconcilable on current evidence and reappear as gaps 2 and 6 rather than as claims. No tension is "explained away": the pattern that survives the table is that the corpus's disagreements are mostly about *what is being claimed*, and its genuine substantive uncertainty is confined to the cost of constraint strength and the interpretation of residual rates.

---

## 4. Convergence, Divergence, and Knowledge Gaps

### 4.1 Convergence map

Convergence here is convergence of *claims*, not of measurements — because §1 found no directly comparable pair. ● = the claim is directly supported by evidence in that family; ◐ = partially or by a different mechanism; ○ = absent.

| Cross-cutting claim | P | N | R | G | C | S |
|---|---|---|---|---|---|---|
| Static admissibility is characterizable and enforceable | ● | ◐ | ● | ● | ● | ◐ |
| Enforcement by restricting the parameter domain | ● | ○ | ○ | ◐ | ○ | ● |
| A residual violation rate is reported for the method's own output | ○ | ◐ | ● | ● | ○ | ○ |
| Dynamic no-arbitrage is enforced or audited | ○ | ○ | ○ | ○ | ○ | ○ |
| Static admissibility is proved (not only tested) | ● | ○ | ● | ● | ● | ◐ |
| Out-of-sample stability is tested | ○ | ◐ | ◐ | ◐ | ○ | ○ |
| A shared benchmark across studies exists | ○ | ○ | ○ | ○ | ○ | ○ |
| Computational cost is measured on common hardware | ○ | ◐ | ◐ | ◐ | ○ | ○ |
| Interpretability of the fitted object is assessed | ○ | ○ | ○ | ○ | ○ | ○ |

Three rows of that table are all-○: dynamic enforcement, shared benchmark, and interpretability. Their conjunction is the knowledge-gap core.

### 4.2 Divergence

The corpus diverges on three axes only. (i) *Tightness*: strict constructions (R6, P1, P8) vs. minimised residuals (N4, N5, G5). (ii) *Object of estimation*: an admissible set (P, R) vs. a distribution over surfaces (G1, G2, G5) vs. a diagnostic statistic (C1, C5). (iii) *Time*: a single snapshot (P, R3, R6, G6) vs. a simulated path (R9, G1, G2, G7) vs. an empirical panel (C3, C5, N2). Divergence is not disagreement: no two rows assert incompatible propositions about the same quantity.

### 4.3 Knowledge gaps

**Gap 1 — Dynamic no-arbitrage enforcement (methodological).** Evidence absence: 0 of 41 rows enforce or audit no-arbitrage for a surface family indexed by calendar time; C2 is the only source that discusses the conditions, and no source states a testable version. Design: fix a daily panel of SPX surfaces (the R5 Ivy DB route already exists in the corpus), apply one construction per family at each date, then test the *sequence* — e.g. whether the repaired or generated path admits a self-financing strategy against the realised next-date surface; report both per-date violations and the path-level test. Report the test's power under injected arbitrage.

**Gap 2 — Head-to-head comparison on identical data and metrics (methodological).** Evidence absence: 0 directly comparable rows; the corpus's comparisons are all within-study. Design: one panel, one tolerance grid, one metric set (static violation rate at three tolerances, IV RMSE inside spread, wall-clock, quote-count sensitivity), applied to one representative per family (e.g. P2-style restricted SVI, N2 neural operator, R1 LP repair, G6 architectural constraint). Pre-register the metric set and publish the full grid, since the point is not a winner but a priced trade-off.

**Gap 3 — Residual audit for proof-level constructions (empirical).** Evidence absence: the 17 proof-level rows report no violation rate; only G6 audits, on synthetic data. Design: take a construction whose proof is stated (P2's restricted calibration or S1's sufficient SVI) and, at the tolerance the proof implies, count finite-precision violations on SPX quotes; report the ratio of realised to predicted violation rate. This is the cheapest study in the list and closes the largest evidential asymmetry.

**Gap 4 — Test power and the noise floor (theoretical/methodological).** Evidence absence: no row estimates the power of its own arbitrage test, and R5 attributes its 5.4% butterfly floor to rounding without quantifying it. Design: simulation study injecting known arbitrage of graduated size into clean slices, adding quote noise at market-observed levels, then measuring detection and retention for a C1-style detector and for the R5/R7 repair criteria; report ROC and the minimum detectable arbitrage.

**Gap 5 — Data efficiency (empirical).** Evidence absence: no row reports performance as a function of sample size, although N2 (ten years) and R9 (2,695 quotes, one date) sit at opposite ends of the data spectrum. Design: learning curves for N2, G4 and G5 on subsampled quote grids (e.g. 5/10/20/50 strikes per expiry, 1/10/100 dates) against an SVI calibration at matched quote counts; report fit error and violation rate at each point.

**Gap 6 — Index and market generality (geographic).** Evidence absence: 10 of 12 known-provenance rows are US equity-index; the only non-US rows are a 2006 DAX study with no constraint enforcement (S5) and a 2022 ALSI GAN with a penalty (N4). Design: one method, three indices (SPX, and two non-US index option markets, including an emerging one), identical protocol, reporting violation rate and fit; also report quote-availability and sparse-grid behaviour, which N4 suggests is the binding constraint outside the US.

**Gap 7 — Computational cost and interpretability, measured rather than asserted (methodological).** Evidence absence: cost is claimed in five rows (P6, R6, R9, N5, G4) and measured comparably in none; no row assesses whether its fitted object is interpretable to a desk. Design: wall-clock and memory on fixed hardware for a fixed grid, plus a structured interpretability protocol (can a practitioner recover the risk-neutral density and the wing behaviour from the reported object?); report both dimensions separately, since §5 treats them as non-commensurable.

---

## 5. Proposed Theoretical Framework

**Status: proposed by this synthesis. It is not taken from any source in the corpus, has not been validated, and is offered as an organizing language for Phase 4 and for future empirical work. It produces no ranking and no composite score.**

### 5.1 Objects

Let a surface be total implied variance `w(k, τ) = σ²(k, τ)·τ` on `D = {(k, τ): k ∈ ℝ, τ ∈ (0, T]}`, with `k = log(K/F_τ)` the normalised log-moneyness. Define the **static admissible set** `A_s` as the set of `w` whose normalised call-price function `c(k, τ) = C(K, τ)/F_τ` satisfies, for every `τ`: (C1) `c(k, τ) − max(1 − e^k, 0) ≥ 0`; (C2) `∂c/∂k ≤ 0`; (C3) `∂²c/∂k² ≥ 0` (butterfly / Durrleman); (C4) `c(·, 0) = max(1 − e^k, 0)`; and across `τ`: (C5) `w(k, ·)` non-decreasing (static calendar). Every static condition used in §1 maps onto C1–C5: G5 and G6 target (C3, C5) plus the call-spread bounds (C1–C2); R5 repairs C5 then C3; R7 and R6 encode C1–C3 as linear inequalities; P1, P2, S1 restrict parameters so that C3 holds for all `k`.

A **dynamic admissible family** is a filtered family `{S_t}` with each `S_t ∈ A_s` and with the joint law of `{S_t}` admitting a martingale representation consistent with the numéraire; equivalently, no self-financing strategy in the option panel is free. No source in the corpus states a testable version of that sentence (C2 reviews candidate conditions without one; G7 explicitly declines to claim it).

### 5.2 Enforcement as a triple

Represent any method as `(M, E, V)`: a model class `M`, an enforcement operator `E: M → A_s` (or a sampler with support in `A_s`), and a verification mode `V ∈ {proof, test, none}`. The four-family taxonomy is a taxonomy of *where `E` acts*:

| Family | Where E acts | Guarantee shape | Evidence it licenses | Corpus rows |
|---|---|---|---|---|
| Parametric construction | Parameter domain: `Θ_A ⊂ Θ`, model maps `Θ_A → A_s` | Universal over the admitted parameter set; model-conditional | A theorem plus the statement of `Θ_A` | P1, P2, P3, P5, P6, P8, S1, R3, R6 |
| Penalty | Objective: `L(θ) = L_fit(θ) + λ Σ_j φ(g_j(θ))` | None at finite `λ`; asymptotic only if the optimum is attained and `λ → ∞` | A residual rate on the evaluated sample | N1 (via gating), N3, N4, N5, N6 |
| Projection–repair | Post-fit output: `Ŝ ↦ Π(Ŝ)`, `im Π ⊆ A_s` | Image of a map; conditional on `Π` being a true projection | A bound on distortion plus residual rate on the grid | R1, R2, R5, R6, R7, R8, R9 |
| Generation–filtering | Sampler or architecture: `supp(p_θ) ⊆ A_s`, or accept iff `x ∈ Â` | Probability statement within test power, or support statement | Pass rate, or an architecture argument | G1, G2, G4, G5, G6, G7, G8 |

Three rows (R3, R6, N1) appear under two loci because their enforcement spans families — a distortion construction is a repair whose reference is already admissible, and N1's constraint lives in the architecture while its label is penalty. §1 keeps the Phase 1 family assignment; the duplication here records the boundary cases rather than reassigning them.

### 5.3 Three propositions the framework makes explicit

**P-1 (the families are not disjoint).** A parametric construction is the special case of generation–filtering with a deterministic decoder `f: Θ_A → A_s` and an exact membership test; the difference is evidential, not mathematical — a theorem substitutes for an acceptance sample. This explains Theme 7: the inherited-guarantee branch of G converges on P because it *is* P with a learned map, and it is why G6's architectural claim and P1's parameter-domain claim have the same logical shape.

**P-2 (penalty never reaches the guarantee without conditions no source states).** `L_fit + λ·penalty` yields an admissible optimum only if the penalty is exact, the optimum is attained, and the admissible set is compact — conditions stated by no row in the corpus. N4 and N5 do not even claim the limit: their abstracts concede that violations are minimised, not removed. Under the framework, a penalty method is a *sampling device for approximately admissible points*, and its evidence obligation is a residual rate, not a proof.

**P-3 (repair and construction differ in observable, not in guarantee class).** Both deliver a point in `A_s`. R is defined relative to an observed surface `S_obs` and therefore has a measurable distortion `d(Π(S_obs), S_obs)` (R1's minimal-change objective is exactly this), whereas P's guarantee is universal over `Θ_A` but says nothing about distance to any observed surface. The two obligations are complementary: R owes a distortion bound, P owes a coverage argument for `Θ_A`.

### 5.4 Seven-dimension evaluation matrix (proposed, non-ranking)

Dimensions are non-commensurable axes, not columns of a score. "Coverage" counts rows in §1 whose reported material could populate the dimension; it measures how much of the corpus speaks to the axis, **not** how well any method performs on it.

| Dimension | Proposed operationalization | Corpus coverage | Status |
|---|---|---|---|
| Static no-arbitrage | Which of C1–C5 the method guarantees or tests, at what tolerance, with which verification mode `V` | 41/41 coded; 17 proof-claiming, 16 test-based, 8 asserted | Populated but incompletely specified (tolerances rarely stated) |
| Dynamic consistency | A path-level test over a surface panel; nothing weaker counts | 10 rows touch time; 0 enforce or test | Effectively unpopulated |
| Fit accuracy | IV or total-variance RMSE inside the bid–ask band, on held-out quotes | ~8 rows report any number; datasets disjoint | Partially populated, not comparable |
| Interpolation and stability | Error at held-out strikes and maturities; behaviour across repeated runs and subsampled grids | ~8 rows (P6, R3, R5, R6, R7, G4, G6, N2/N6) | Thin; no boundary-specific audit |
| Computational cost | Wall-clock and memory on fixed hardware for a fixed grid | ~5 claims, 0 comparable measurements | Asserted, not measured |
| Interpretability | Recoverability of the density, wings, and parameter meaning; practitioner usability | 0 rows assess it; P-family objects are transparent by construction | Unpopulated |
| Data efficiency | Fit error and violation rate as a function of quote count and date count | 0 rows report a learning curve; endpoints implicitly contrasted (R9 one date, N2 ten years) | Unpopulated |

### 5.5 What the framework does not do

It does not rank methods, does not assert that the four families are exhaustive (C3 and G7 enforce through the dynamics of an underlying model and sit between P and G), does not claim any row's reported proof is correct, and does not imply that coverage on a dimension is evidence of quality on it. Its only validated content is the coding of §1 under the definitions of 5.1 — and that coding is a synthesis judgement, not a measurement.

---

## 6. Devil's Advocate Report — Checkpoint 2

**Target:** this synthesis (sections 1–5) and the evidence base behind it.

### Verdict: PASS — no Critical issues; three Major issues raised, all three closed by in-place revision before this file was finalized; two Major-class limitations are intrinsic to abstract-level retrieval and are carried forward as disclosures.

### 6.1 Cherry-picking check

Three specific checks. (a) *Theme 4* rests on a quantified direction reported by G6 alone; the text says so and labels the theme Emerging, and G6 is also disclosed as the only guarantee-plus-audit row — so the single strongest source is not doing hidden work, it is doing visible work. (b) *Theme 1* is an absence claim over all 41 rows, which is the least cherry-pickable form available; it is bounded to the abstracts actually read and stated as such. (c) The two most attractive claims for the RQ — that penalty methods buy fit accuracy and that no-arbitrage is essentially solved by construction — are both **not** made: H2's first clause is reported as unsupported, and 17 proof-level rows are reported as never audited. No row is cited in a theme that its own §1 entry does not support; the 3 metadata-only rows (P4, P7, R4) are used for no substantive claim and appear only as titles.

### 6.2 Confirmation-bias check

*Family favouritism.* No family is privileged: P is credited with 17 proofs and charged with zero audits; G is credited with the only guarantee-plus-audit row and charged with the weakest enforcement descriptions (G2, G4). *Noisy-literature bias.* The 11 preprints are 26.8% of the corpus and 6 of them are 2025–2026; two carry the strongest "strict" claims (R6, G6) and one is the only dynamic-relevant parametric source (P8). The synthesis does not discount a claim for being a preprint, but tags evidence status independently of venue, and §7 states that recent-generation claims are provisional. *Hypothesis anchoring.* H1–H3 were fixed in Phase 1, creating a real risk of post-hoc confirmation. It was checked explicitly, and the result is disconfirming on two of three clauses (H1's second clause, H2's first clause) — the pattern that a confirmation-seeking synthesis would have produced is absent.

### 6.3 Logic-chain validation (Toulmin)

| Claim | Data | Warrant | Backing | Qualifier | Rebuttal |
|---|---|---|---|---|---|
| Dynamic no-arbitrage is not enforced in this corpus | 41 coded rows, 0 instances | Coding rule that static calendar ≠ dynamic | The definition in 5.1 and C2's distinction | Bounded to abstracts read (7 of 41 partial or metadata-only) | Would fail if any abstract's phrase "across time" means calendar time — checked, R6's does not, and G7's caveat settles its own case |
| Constraint strength costs fit | G6: 0.00% violations and higher RMSE than SSVI and soft-penalty MLP | A paired within-study comparison is the only valid form | G6 is the sole paired instance | Single study, synthetic data | Not extended to market data or to other families |
| Evidence statuses are asymmetric between families | 17 proof rows report no residual; 6 rows report residuals | A guarantee without audit cannot be inspected | G6's existence proves the combination is feasible | Descriptive only | If proof-level rows audit residuals internally and the abstract omits it, the asymmetry is a reporting artefact — irreducible at abstract level |

The weakest warrant is the third: "no audit reported" is not "no audit performed". The text says "reports", and §7 records this.

### 6.4 Alternative explanations

1. *The static/dynamic split is a retrieval artefact.* Dynamic-arbitrage work may use vocabulary ("consistent surface dynamics", "no free lunch in the panel") that the Phase 2 query set did not match. This is the strongest alternative and cannot be excluded at abstract level; it is recorded as a retrieval limitation, not as evidence of absence in the field.
2. *The proof/audit asymmetry is a publication norm.* Theory journals do not publish empirical violation rates; empirical venues do not publish proofs. On this reading the asymmetry is a venue effect, not an evidential gap. It is still a gap for a practitioner choosing a method, which is the synthesis's frame.
3. *Residual rates differ because data differ.* G5's 90.8% and G6's 0.00% are consistent with one underlying property — the noise floor of empirical quotes — and T5 treats this as the live alternative rather than dismissing it.
4. *The four-family taxonomy is imposed.* It was frozen in Phase 1 to make the review comparable, and it does produce friction (N1 is architecturally gated; C3 and G7 sit between families). The friction is disclosed in 5.5 rather than hidden.

### 6.5 Major issues (all closed by revision)

**M1 — Absence claims were stated too strongly in the first draft.** The claim "dynamic no-arbitrage is not enforced" read as a claim about the literature rather than about 41 abstracts. *Closed by* bounding every absence statement to the read scope, naming the 7 non-full abstracts, and adding Alternative Explanation 1. *Residual:* irreducible at abstract level; carried to §7.

**M2 — Theme 4 risked being read as a performance claim.** "Tighter constraint, worse fit" could be taken as a cross-family ranking. *Closed by* labelling the theme Emerging, restricting it to G6's within-study comparison, and adding the explicit statement that no corpus-level comparison is licensed.

**M3 — H1–H3 were tested but the verdicts were not visible.** A theme list that approximates a pre-declared hypothesis set invites confirmation bias. *Closed by* adding the hypothesis-status table at the end of §2, with two clauses reported as disconfirmed.

### 6.6 Minor issues and observations

**m1** — C2 is a 2015 non-peer-reviewed review carrying the entire conceptual load for dynamic no-arbitrage; the synthesis marks this and does not let C2's enumeration stand in for evidence. **m2** — R6's "across time and strike" was read as the two surface axes, not calendar time; the reading is stated in §1 so a reviewer can overrule it. **m3** — The taxonomy's boundary rows (N1, C3, G7) are flagged rather than reassigned, because reassignment at synthesis time would silently overrule Phase 1's frozen coding. **Observation:** the corpus contains no negative result — no study reports a method failing on a benchmark — which is consistent with publication bias and cannot be corrected from abstracts.

### 6.7 Strongest counter-argument

The whole synthesis might be read as an artefact of what abstracts say: a paper that proves a theorem has no reason to report violation rates, and a paper that reports violation rates has no reason to prove a theorem, so the "proof/audit gap" could be a property of abstracts rather than of practice. The counter-argument does not survive fully, because G6 exists — one source found both worth reporting — and because G5's and N5's own abstracts concede the residual framing. But it does force the weaker, correct form of the claim: *the corpus, as abstracted, does not contain the evidence needed to compare families* — which is the finding, and is weaker than "the field lacks it".

### 6.8 What is missing

Full texts (would test M1 and the retrieval-artefact alternative), an independent second coder for the dynamic/static coding (would test reliability of the single most load-bearing judgement), and any source that applies one method to two markets (would test T6). The first is achievable in Phase 4 by retrieving 3–5 PDFs of the highest-impact rows (G6, R5, P2, G2, G7); the second and third are out of scope for this run.

### 6.9 Stress tests

| Stress test | Result |
|---|---|
| Remove the strongest source (P2, the exact static characterization) | Themes 1, 2, 5 survive via P1, P3, S1; T7 weakens to a two-source lineage. No verdict changes. |
| Remove the second strongest (G6) | Theme 4 collapses to Emerging-with-no-quantified-direction and T5 loses its contrast; the version of Theme 4 and T5 in this file is explicitly conditioned on G6 and would be withdrawn without it. **This is the file's most source-dependent claim.** |
| Flip the RQ ("which method fits best?") | Corpus cannot answer: 0 comparable rows. Reported as a finding, not a failure. |
| Change the context (single-stock options) | C5 is the only single-name panel and is scope-flagged; the index frame holds, and the synthesis does not generalize to single names. |
| "So what?" | The practical content is the obligation structure: a method owes a theorem *or* a residual rate, and a study should report which it has; the corpus shows most methods report one and never the other. |

### 6.10 Residual bias record

English-only corpus (100% by protocol: English-only was a Phase 1 inclusion rule); abstract-level evidence (34 full, 4 partial, 3 metadata-only; 7 of 41 rows carry less than a complete abstract); 2015–2026 window with 5 flag-exempt seminal rows and 20 rows from 2023–2026 (49%), so the taxonomy over-represents the learning era; US-index dominance (10 of 12 known-provenance rows); preprint share 26.8%, with the strictest claims concentrated there; single-index discovery (OpenAlex only, 31 queries, one failed request) and no citation-network tracing; no citation counts anywhere, so influence is unmeasurable; single coder (this agent) for every coding judgement, so the coding reliability is unestimated; and the author of the synthesis is also the run operator, with no independent second reader before Phase 4.

---

## 7. Synthesis Limitations

1. **Abstract-level only.** Every row is coded from an abstract as recorded in Phase 2; no proof was re-derived, no dataset inspected, no number recomputed. Statements such as "the theorem holds" mean "the abstract reports a theorem".
2. **Absence claims are bounded.** "No source enforces dynamic no-arbitrage" means no source *says so in the abstract*; 4 partial and 3 metadata-only abstracts cannot support even that.
3. **No comparability, therefore no performance claims.** 0 directly comparable rows; §1's metric column records what was reported, not a measurement, and §4's convergence map is a map of claims.
4. **Retrieval is single-index and time-bounded.** OpenAlex only, 2015–2026 with 5 seminal exemptions; work using different vocabulary for surface dynamics may be under-represented (Alternative Explanation 1).
5. **Evidence status is reported status.** The 17/16/8 split is Phase 2's coding under Phase 1's rule that a test is never upgraded to a proof; it is not a quality grade, and C-graded sources (17 by Phase 2 verification) contribute to themes with their grade attached.
6. **The framework in §5 is proposed, not validated.** It is this synthesis's own formalization; no source proposes it, and its coding of §1 is a judgement that a second coder has not checked.
7. **No meta-analysis, no vote counting, no ranking.** Prohibited by the Phase 1 design; the file states neither a best method nor a consensus.
8. **Publication and reporting bias are unobservable here.** No negative results in the corpus; venue norms plausibly explain part of the proof/audit asymmetry (Alternative Explanation 2).
9. **Construct conflation is corrected but not resolved.** T8 separates static calendar from dynamic calendar; sources that use the same word for both remain coded by their mechanism, not their wording, and that coding is a single-coder judgement.

---

## 8. Revisions Applied After Devil's Advocate

| # | Issue | Revision | Location |
|---|---|---|---|
| M1 | Absence claims read as field-level | All absence statements bounded to the read scope; 7 non-full abstracts named; Alternative Explanation 1 added | §1 accounting, §2 Theme 1, §6.4, §7.2 |
| M2 | Theme 4 could be read as a ranking | Emerging label; single-study restriction; no-comparison statement | §2 Theme 4, §4.1 preamble |
| M3 | H1–H3 tested but invisible | Hypothesis-status table with two disconfirmed clauses | §2, final table |
| m1 | C2 over-loaded | C2's status (non-peer-reviewed review) stated where it is used | §1 C2 row, §2 Theme 1 |
| m2 | R6 "across time and strike" ambiguity | Reading stated in the row so a reviewer can overrule it | §1 R6 row |

---

## 9. Phase 3 Checkpoint

| Item | Status |
|---|---|
| Evidence matrix complete (41/41 rows, all ten required fields) | Done |
| Thematic synthesis (7 themes, each with strength, sources, synthesis) | Done |
| Contradictions/tensions (8, with positions, sources, verdicts, resolution) | Done |
| Convergence/divergence map and knowledge gaps (7 gaps with absence + design) | Done |
| Proposed framework (four-family taxonomy + seven dimensions), labelled proposed, non-ranking | Done |
| Devil's Advocate CHECKPOINT 2 (cherry-picking, confirmation bias, logic chain, alternatives, verdict) | Done — PASS, 3 Major closed, 2 limitations carried |
| Every quantitative claim traced to a Phase 2 entry | Done |
| No new sources, no invented metrics, no ranking or winner declared | Done |
| File scope: this run directory only | Done |
**Phase 3 verdict:** PASS — proceed to Phase 4 (report), carrying the abstract-level limitation and the single-coder reliability caveat as disclosed constraints.
