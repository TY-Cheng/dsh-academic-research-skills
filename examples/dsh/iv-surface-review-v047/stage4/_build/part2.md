## 4. Findings I: How Each Family Enforces Static Admissibility

### 4.1 Parametric Construction

Parametric construction puts the constraint in the parameter domain: the family is parameterised so that every admitted vector yields a surface satisfying the stated conditions, and estimation is restricted to that set. Table 2 summarises the four focal families, with the two supporting groups shown for completeness.

The purest case is arbitrage-freeness inherited from the structure of a generalised SVI parameter set, holding for all admitted parameters rather than only at the fitted optimum (Guo et al., 2016)<!--ref:P1--><!--anchor:section:4.1-->. A second line replaces a sufficient parameter box with an exact butterfly characterisation, so the admissible set is not narrower than necessary (Martini & Mingone, 2022)<!--ref:P2--><!--anchor:section:4.1-->. A third calibrates an extended SSVI parameterisation jointly across maturities, making calendar monotonicity a property of the joint fit (Mingone, 2022)<!--ref:P3--><!--anchor:section:4.1-->; its sequential slice-wise counterpart is available only at title level (Corbetta et al., 2019)<!--ref:P4--><!--anchor:section:4.1-->. Three rows broaden the admissible shapes instead: a random-coefficient parameterisation admitting bimodal short-dated densities (Zaugg et al., 2025)<!--ref:P5--><!--anchor:section:4.1-->, a piecewise-cubic interpolation that guarantees its interpolant rather than its fit (Le Floc’h, 2025)<!--ref:P6--><!--anchor:section:4.1-->, and a bounded-factor model deriving static conditions while reporting time-indexed arbitrage probabilities, the only parametric row indexed by time (Barski & Wiśniewolski, 2026)<!--ref:P8--><!--anchor:section:4.1-->. One row claims necessary-and-sufficient conditions for the SSVI/S3 curve but is metadata-only and cannot corroborate them (Klassen, 2016 [preprint])<!--ref:P7--><!--anchor:section:4.1-->.

Six of eight rows are proof-level and none audits observed quotes: the guarantee is universal over the admitted set and silent about the fitted instance, and no row pairs it with a fit cost. The boundary with repair is real — a distortion of an arbitrage-free reference and a linear-programming construction both embed the constraint deterministically but certify a transformed object (Bender & Thiel, 2020<!--ref:R3--><!--anchor:section:4.1-->; Buehler et al., 2026)<!--ref:R6--><!--anchor:section:4.1-->.

| **Table 2.** Four-family evidence summary (two supporting groups shown for completeness) | | | | | | |
|---|---|---|---|---|---|---|
| **Family** | **n** | **Enforcement locus** | **Object claimed "arbitrage-free"** | **Guarantee shape** | **Evidence licensed** | **Verification reported** |
| Parametric (P) | 8 | Parameter domain | Admitted parameter set | Universal over the admitted set | Proof (6), assumption (2); no residual audit | None in abstract |
| Penalty (N) | 6 | Objective / loss | Evaluated sample at finite weight | Conditional on weight and tolerance | Residual rate; no guarantee | Residual or pass rate |
| Projection–repair (R) | 9 | Output image | Surface after a map | Conditional on the projection | Proof (3), test (4), assumption (2); distortion plus residual | Residual floor |
| Generation–filtering (G) | 8 | Sampler / acceptance | Accepted sample or inherited class | Within test power or model support | Proof (4), test (3), assumption (1); pass rate or architecture argument | Pass rate or proof |
| Conditions / evaluation (C) | 5 | Diagnostic | Neither constructor nor repair | Detector or condition set | Proof (3), test (1), assumption (1); detection result or review | Detection / review |
| Seminal baselines (S) | 5 | Pre-2015 baseline | Pre-constraint construction | No guarantee claim | Baseline only (1 proof, 2 test, 2 assumption) | None |

**Table 2 note.** The four focal families are the subject; C and S are supporting groups. "Evidence licensed" is the review's coding, not a source's claim. Per-row values are in Appendix B.

### 4.2 Penalty and Constrained Learning

Penalty methods add a violation term, or a differentiable surrogate for a constraint, to a training objective. The constraint is priced rather than imposed, so compliance is approximate and conditional on the weight, tolerance, and stopping rule. Six rows occupy this locus and none is proof-level.

A gated network whose slopes and weights make the price function frictionless and convex by design sits on the architectural boundary (Cao et al., 2020)<!--ref:N1--><!--anchor:section:4.2-->. A graph neural operator trained on a ten-year intraday SPX panel reports adherence without a stated tolerance (Wiedemann et al., 2025)<!--ref:N2--><!--anchor:section:4.2-->. A deep smoother adds soft penalties plus a plug-in correction for sparse quotes (Ackerer et al., 2019 [preprint])<!--ref:N3--><!--anchor:section:4.2-->. A GAN trained with a static-arbitrage loss on the ALSI index states that the condition cannot be learned through the penalty route, the corpus's most explicit statement of what a penalty cannot deliver (Sidogi et al., 2022)<!--ref:N4--><!--anchor:section:4.2-->. A second penalty model minimises violations and reports a residual rather than a certificate against an artificial neural network baseline (Na et al., 2023)<!--ref:N5--><!--anchor:section:4.2-->. A derivative-constrained deep network embeds strike and maturity derivative terms in its loss and trains on SABR-generated data, so its adherence is an in-sample property of a simulated generator (Hoshisashi et al., 2023 [preprint])<!--ref:N6--><!--anchor:section:4.2-->.

The pattern is consistent: all six report a numerical test, none a proof, and the residual is the mechanism working as designed. A penalty cannot certify a set, only report how much of the sample it failed to correct at a chosen weight, which is why its claim is indexed to an evaluated sample (Appendix D). The hybrid row is coded as a test because the review credits a proof only where a theorem over the admitted set is stated (Cao et al., 2020)<!--ref:N1--><!--anchor:section:4.2-->.

### 4.3 Projection and Repair

Repair fits first and maps afterwards. The certified object is the image of the map, and a projection proof is a statement about the map, not about the repaired surface across dates. Nine rows occupy this locus: three proof, four test, two assumption.

A linear-programming repair moves prices minimally inside the bid–ask with no cross-date claim (Cohen et al., 2020)<!--ref:R1--><!--anchor:section:4.3-->; an entropic projection to the arbitrage-free set proves the convergence of the projection, not the repaired family's admissibility over time (De March & Henry-Labordère, 2019 [preprint])<!--ref:R2--><!--anchor:section:4.3-->; a distortion of an arbitrage-free reference shares the observable with construction, with the Kahalé approach as a special case (Bender & Thiel, 2020)<!--ref:R3--><!--anchor:section:4.3-->; and a strictly arbitrage-free non-parametric construction calibrates by linear programming with positive discrete local volatility (Buehler et al., 2026)<!--ref:R6--><!--anchor:section:4.3-->.

Three rows report measured residuals. An observation-anchored repair over 252 out-of-sample SPX days and five completion backends reports a butterfly violation floor of about 5.4%, so the repaired surface is not violation-free on real quotes, and a cubic-spline backend has the lowest reconstruction error after repair (Xiong & Liu, 2026)<!--ref:R5--><!--anchor:section:4.3-->. A Chebyshev-tensor construction with a quadratic-programming stage reports under 1% static violations and 98–99% inside-spread coverage in calm years, with leakage under stress (Alvarez, 2025 [preprint])<!--ref:R7--><!--anchor:section:4.3-->. A Markov-chain approximation over 2,695 SPY options and 28 maturities on a single date carries a maturity axis but no date-indexed family and no dynamic audit (Madan & Schoutens, 2019)<!--ref:R9--><!--anchor:section:4.3-->. One row asserts transformations without proof or test (Zetocha, 2023 [preprint])<!--ref:R8--><!--anchor:section:4.3-->, and one extends the scope to joint American call-and-put smoothing at title level (Yao et al., 2026)<!--ref:R4--><!--anchor:section:4.3-->.

The family's baseline is the shape-constrained smoothing spline, which showed that ignoring the constraint matters (Fengler, 2009)<!--ref:S2--><!--anchor:section:4.3-->. Two earlier constructions enforced nothing: a nonparametric inversion without an explicit constraint set (Bodurtha & Jermakyan, 1999)<!--ref:S4--><!--anchor:section:4.3--> and a semiparametric factor model on DAX data estimated without enforcement (Fengler et al., 2006)<!--ref:S5--><!--anchor:section:4.3-->. Both are baselines, not counterexamples: they predate the constraint literature this review codes.

### 4.4 Generation and Filtering

Generation–filtering methods produce candidate surfaces, parameters, or prices and then accept, reject, project, or constrain them. The locus is the sampler with its acceptance test, and the family splits there: an inherited guarantee behaves like a parametric construction, while a penalised sampler reports a pass rate.

Four rows sit on the inherited side. A variational autoencoder over the parameters of stochastic-volatility models generates surfaces whose admissibility follows from the stochastic differential equation class rather than from the training objective (Ning et al., 2023)<!--ref:G1--><!--anchor:section:4.4-->. A neural-SDE state space defines a family of statically arbitrage-free prices and explicitly disclaims a dynamic guarantee (Cohen et al., 2021)<!--ref:G7--><!--anchor:section:4.4-->. A gated rational network is arbitrage-free by design (Yang et al., 2017)<!--ref:G8--><!--anchor:section:4.4-->. Trainable hard constraints go further: the constraint is a differentiable but hard architectural element, and the row reports 0.00% violations at a $10^{-4}$ tolerance over 15 runs on synthetic SVI data (Anagha, 2026)<!--ref:G6--><!--anchor:section:4.4-->, while reporting higher total-variance root-mean-square error than an SSVI baseline and a soft-penalty network — the corpus's one paired measurement, and it runs against the claim that a stronger guarantee buys a better fit.

Four further rows sit on the filtered side. A VolGAN generates joint surface and underlying scenarios evaluated through hedging, with the enforcement mechanism undescribed (Vuletić & Cont, 2024)<!--ref:G2--><!--anchor:section:4.4-->. A simulation approach places static constraints inside a generated process but is only partly available at abstract level (Cont & Vuletić, 2023)<!--ref:G3--><!--anchor:section:4.4-->. A GAN denoiser reports lower mean-squared error and runtime without a guarantee claim (Ginart Belmonte & Cole, 2025)<!--ref:G4--><!--anchor:section:4.4-->. A latent flow-matching generator reports that 90.8% of generated surfaces pass all tested static conditions, the corpus's clearest pass-rate statement (Bajalica et al., 2026)<!--ref:G5--><!--anchor:section:4.4-->.

## 5. Findings II: Evidence Status, Comparability, and Evaluation Coverage

### 5.1 Evidence Status and the Proof–Audit Gap

The corpus splits into 17 proof-level rows, 16 numerical-test rows, and 8 assumption rows; the in-window records split 16 / 14 / 6 and the seminal precursors 1 / 2 / 2, and Table 3 gives the family breakdown. The distribution follows the loci: a parameter domain licenses a theorem, an objective a sample, a map a statement about the map, a sampler a pass rate.

Six rows audit their own output: a graph neural operator reporting adherence on ten years of intraday data (Wiedemann et al., 2025)<!--ref:N2--><!--anchor:section:5.1-->, a deep network with derivative constraints on simulated data (Hoshisashi et al., 2023)<!--ref:N6--><!--anchor:section:5.1-->, a repair reporting a 5.4% butterfly floor (Xiong & Liu, 2026)<!--ref:R5--><!--anchor:section:5.1-->, a Chebyshev construction reporting under 1% violations (Alvarez, 2025)<!--ref:R7--><!--anchor:section:5.1-->, a flow-matching generator reporting a 90.8% pass rate (Bajalica et al., 2026)<!--ref:G5--><!--anchor:section:5.1-->, and a hard-constrained generator reporting 0.00% at $10^{-4}$ over 15 runs (Anagha, 2026)<!--ref:G6--><!--anchor:section:5.1-->. The two axes are counted separately, and the partition recomputes from the Audit column of Appendix B: 16 proof rows audit nothing and one audits its own output; 5 test rows audit their own output and 11 report a numerical result that is not a violation statistic on that output; 8 assumption rows audit nothing. Hence 16 + 1 + 5 + 11 + 8 = 41 rows and 1 + 5 = 6 audit rows. Proof and audit are nearly disjoint in exactly one sense: one of the six audit rows is also proof-level, and one of the 17 proof rows reports a violation rate on its own output. Those are the same fact stated from either side; the earlier 17 / 6 / 1 partition is that fact, not a third count.

On the dynamic condition the rule of Section 2.2 gives 0 of 41 rows at D3 — 0 of the 36 in-window records and 0 of the 31 construction rows — with three at D2 (G7, C3, G1), four at D1 (P8, C2, C5, R8), and 34 at D0. Table 3 carries the ten time-engaging rows by family so the claim can be read against the rows rather than asserted over them.

Table 4 adjudicates the three hypotheses. H1's static clause is supported — all 41 rows are coded on a static predicate and six of eight parametric rows are proof-level — while its dynamic clause is disconfirmed as stated: the hypothesis expected dynamic requirements to be asserted or tested, and no row states and checks a process-level condition, so the finding is absence rather than weak enforcement. H2's fit-error clause is unsupported, since no penalty or repair row reports a lower fit error than a constrained parametric baseline on the same data and the one paired measurement points the other way; its burden-displacement clause holds, because weights, tolerances, repair steps, and acceptance thresholds are where the constraint work is absorbed (Na et al., 2023<!--ref:N5--><!--anchor:section:5.1-->; Sidogi et al., 2022<!--ref:N4--><!--anchor:section:5.1-->; Xiong & Liu, 2026)<!--ref:R5--><!--anchor:section:5.1-->. H3 is supported for the penalised-sampling branch and disconfirmed for the inherited-guarantee branch, where four rows are structural rather than sample-filtered (Anagha, 2026<!--ref:G6--><!--anchor:section:5.1-->; Cohen et al., 2021<!--ref:G7--><!--anchor:section:5.1-->; Ning et al., 2023<!--ref:G1--><!--anchor:section:5.1-->; Yang et al., 2017)<!--ref:G8--><!--anchor:section:5.1-->.

Two coding conventions protect the result. Metadata-only rows are never counted as evidence for their own claims, so the proof count does not inherit a claim from a title, although the three rows remain in the structural tallies (Appendix D.2). Preprints are labelled wherever cited, so a reader can see that three of the six audit rows are preprints (N6, R7, G6).

| **Table 3.** Evidence status, audit, and time-axis count by family (review coding) | | | | | | |
|---|---|---|---|---|---|---|
| **Family** | **Proof** | **Numerical test** | **Assumption** | **Total** | **Audit rows** | **Time-axis rows** |
| P (parametric) | 6 | 0 | 2 | 8 | 0 | 1 (P8) |
| N (penalty) | 0 | 6 | 0 | 6 | 2 (N2, N6) | 0 |
| R (projection–repair) | 3 | 4 | 2 | 9 | 2 (R5, R7) | 1 (R8) |
| G (generation) | 4 | 3 | 1 | 8 | 2 (G5, G6) | 4 (G1, G2, G3, G7) |
| C (conditions) | 3 | 1 | 1 | 5 | 0 | 3 (C2, C3, C5) |
| S (seminal) | 1 | 2 | 2 | 5 | 0 | 1 (S5) |
| **Total** | **17** | **16** | **8** | **41** | **6** | **10** |

**Table 3 note.** In-window split 16 / 14 / 6 over 36 rows; seminal split 1 / 2 / 2 over 5 rows. An audit row reports a violation or residual statistic on its own output; evidence status and audit are separate columns, and G6 is the only row that is both proof-level and an audit row. "Time-axis" counts rows whose coded object is date-indexed (Appendix D.4); the ten rows are those named in Section 2.2.

| **Table 4.** Hypothesis adjudication | | | |
|---|---|---|---|
| **Hypothesis** | **Verdict** | **Basis** | **Residual uncertainty** |
| H1 — static enforcement is mostly by construction; dynamic requirements are asserted or tested rather than proved | Static clause supported; dynamic clause disconfirmed as stated | All 41 rows coded on a static predicate; 6 of 8 parametric rows proof-level; 0 of 41 state and check a process-level condition | The dynamic reading depends on abstract-level coding and on vocabulary (Section 6.2) |
| H2 — penalty and repair routes displace rather than remove the burden, and may fail to lower fit error | Burden-displacement clause supported; fit-error clause unsupported | No penalty or repair row reports lower fit error than a constrained parametric baseline on the same data; the one paired measurement reports a higher error (G6) | The fit clause was formulated after the first coding pass (§1.2); adequacy of any residual rate is not assessable without a loss and tolerance the corpus does not supply (§5.4) |
| H3 — generation's "arbitrage-free" often means "not rejected on this sample" | Supported for the penalised-sampling branch; disconfirmed for the inherited-guarantee branch | G5 reports a 90.8% pass rate; G1, G6, G7, G8 are structural rather than sample-filtered | Small branches (four and four); enforcement mechanism is under-described in several rows |

### 5.2 Comparability and the Metric Vocabulary

Comparability coding returns 0 direct, 30 context, and 11 not comparable (Table 5). Every parametric row is context or not comparable; no penalty or generation row is not comparable, because their objects and metrics fall inside the same loose vocabulary; the conditions group carries the largest share of not-comparable rows (three of five).

A direct comparison requires the four fields of Table 5, and no row reports all four. Tolerance is the field most often missing, which makes a reported rate uninterpretable even within its own study; dataset overlap is the second gap, since the SPX panel recurs on different date ranges, sampling frequencies, and option filters.

Seven metric families appear — price, volatility and total-variance errors, bid–ask capture, Wasserstein distance, hedging profit and loss, and runtime — and a number is context unless the protocol matches. Even violation rates are not comparable: 90.8% on generated surfaces, a 5.4% floor on out-of-sample SPX days, under 1% for a Chebyshev construction, and 0.00% at $10^{-4}$ on synthetic SVI data differ in data, definitions, tested conditions, and tolerance. Within-study baselines are the only licensed comparisons (Anagha, 2026<!--ref:G6--><!--anchor:section:5.2-->; Sidogi et al., 2022<!--ref:N4--><!--anchor:section:5.2-->; Na et al., 2023<!--ref:N5--><!--anchor:section:5.2-->; Xiong & Liu, 2026)<!--ref:R5--><!--anchor:section:5.2-->; a neural detector of model-free static arbitrage exists as an independent auditor but is never applied to another row here (Neufeld & Sester, 2024)<!--ref:C1--><!--anchor:section:5.2-->. The review therefore reports ranges with conditions and no league table; the absence of a common protocol is itself a finding.

| **Table 5.** Comparability matrix (review coding) | | | | |
|---|---|---|---|---|
| **Family** | **Direct** | **Context** | **Not comparable** | **Total** |
| P (parametric) | 0 | 4 | 4 | 8 |
| N (penalty) | 0 | 6 | 0 | 6 |
| R (projection–repair) | 0 | 6 | 3 | 9 |
| G (generation) | 0 | 8 | 0 | 8 |
| C (conditions) | 0 | 2 | 3 | 5 |
| S (seminal) | 0 | 4 | 1 | 5 |
| **Total** | **0** | **30** | **11** | **41** |

**Table 5 note.** A direct comparison requires the same dataset or panel, the same condition set and tolerance, the same metric and aggregation, and the same protocol. No row reports all four; tolerance is the most frequently missing field. Per-row codes are in Appendix B.

### 5.3 Evaluation Coverage: Seven Dimensions

Table 6 maps what the corpus measures against seven evaluation dimensions. Static no-arbitrage is populated: all 41 rows are coded on it, with tolerances rarely stated. Dynamic consistency is empty: ten rows engage the time axis and none states and checks a dynamic condition. Fit accuracy is partial — about eight rows report an error on held-out data, on disjoint datasets and in three metric spaces — and interpolation and stability are thin: about eight rows report held-out strike or maturity behaviour, none runs a boundary audit, and repeated-run stability is rarely reported. Computational cost is asserted in about five rows with no comparable measurement; interpretability and data efficiency are unpopulated, since no row reports density, wing, or parameter recoverability as an evaluation target and none reports fit or violation against quote, date, or training-set size.

These counts aggregate the per-row fields of Appendix D; the three "about" entries summarise a free-text metric field and are labelled approximations, not counts, and the matrix records whether a dimension is measured, not whether a method is good.

The cost of a stronger guarantee is measured on one side only. A hard-constrained generator reports a structural guarantee, a 0.00% audit, and a higher total-variance error than two baselines (Anagha, 2026)<!--ref:G6--><!--anchor:section:5.3-->; a repair reports a 5.4% floor and selects a backend by reconstruction error (Xiong & Liu, 2026)<!--ref:R5--><!--anchor:section:5.3-->; a Chebyshev construction reports sub-1% violations with stressed-year leakage (Alvarez, 2025)<!--ref:R7--><!--anchor:section:5.3-->; a flow-matching generator reports a pass rate without a paired fit-cost comparison (Bajalica et al., 2026)<!--ref:G5--><!--anchor:section:5.3-->. The corpus therefore cannot support the claim that a penalty or repair route lowers fit error, and the one paired measurement points the other way; Section 5.4 states what the numbers would need to become acceptance criteria.

| **Table 6.** Seven-dimension evaluation matrix: coverage, not performance | | |
|---|---|---|
| **Dimension** | **Operationalization** | **Coverage and status** |
| Static no-arbitrage | Condition set SC1–SC5, tolerance, verification mode | 41/41 coded; 17 proof / 16 test / 8 assumption — populated; tolerances rarely stated |
| Dynamic consistency | Path-level condition and test across dates | 10 rows engage the time axis; 0 enforce or test a dynamic condition — unpopulated |
| Fit accuracy | IV or total-variance error on held-out data | about 8 rows; disjoint datasets, three metric spaces — partial; not comparable |
| Interpolation and stability | Held-out strikes or maturities; repeated runs or subsamples | about 8 rows — thin; no boundary audit |
| Computational cost | Wall-clock or memory on a fixed grid | about 5 assertions — asserted; 0 comparable |
| Interpretability | Density, wing, or parameter recoverability as an evaluation target | 0 rows — unpopulated |
| Data efficiency | Fit or violations against quote, date, or training-set size | 0 learning curves — unpopulated |

**Table 6 note.** A coverage map, not a scorecard: no column orders methods, and an unpopulated dimension means "not measured in this corpus", not "not measurable". The three "about" entries summarise a free-text field and are approximations, not counts.

### 5.4 From Residual to Acceptance Criterion

The corpus's residual numbers are frequencies, and a frequency becomes a validation grade only when five inputs are supplied. This subsection states the specification, then states which inputs the corpus does not supply, so that no reported number in Sections 4 and 5 is read as a grade.

The five inputs are: a **loss function**, which says what is counted — the fraction of quoted strikes in violation, the maximum violation in price units, the surface-level maximum over a day, and whether days are aggregated equally or by volume are different losses giving different rates; a **tolerance**, the numerical threshold at which the loss is acceptable, in the units of the loss and on the conditions tested; **test power**, the probability that the check detects a violation of a stated size, with its false-negative rate, without which a zero or near-zero rate is consistent both with a good surface and with a weak test; **regime coverage**, the market states, index panel, and date range over which the rate was computed, without which it does not travel to a different panel; and an **independent check**, a detector not built from the construction's own condition set, so that a construction's own pass does not certify it.

The corpus supplies little on every one. One row states a tolerance and a loss together (G6: 0.00% violations at $10^{-4}$ over 15 synthetic runs) but neither test power nor regime coverage beyond synthetic SVI slices. One reports a rate over a real panel with a stated protocol but no tolerance (R5: a 5.4% butterfly floor over 252 out-of-sample SPX days, attributed by the source to rounding); one an under-1% rate with regime dependence noted but no tolerance (R7); one a pass rate over an unstated sample (G5); one adherence over ten years of intraday data without a tolerance (N2); one a residual on simulated data with no power analysis (N6). No row estimates test power, and no row applies an independent detector — the corpus contains one (Neufeld & Sester, 2024)<!--ref:C1--><!--anchor:section:5.4-->, never applied to another row. Zero of six audit rows supply three or more of the five inputs, and zero of 41 supply all five.

The consequence is stated rather than repaired: the rates in Sections 4 and 5 are descriptive frequencies under conditions the sources state unevenly, and the review grades no construction by them. A residual rate becomes a grade only when a study states all five inputs, and the agenda in Section 6.3 places the power-and-noise-floor study first because four of the five inputs depend on it.
