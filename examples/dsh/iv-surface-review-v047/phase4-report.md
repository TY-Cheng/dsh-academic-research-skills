# Enforcing No-Arbitrage in Equity-Index Implied Volatility Surfaces: A Structured Review of Four Method Families, 2015–2026

**Author:** TY-Cheng
**Affiliation:** Independent researcher
**Date:** 2026-11-23
**Report type:** `deep-research` full report — Stage 1, Phase 4 draft (ARS v3.24.4 end-to-end validation run)
**Body word count:** 5,247 words (excluding references and appendices; citation-emission markers excluded)
**Corpus:** 41 sources (29 peer-reviewed, 11 preprints, 1 practitioner magazine), 2015–2026, equity-index options
**Evidence status:** 17 proof-level claims / 16 numerical tests / 8 assumptions
**Read scope:** abstract-level for all 41 sources
**Last search:** 2026-11-23

---

## Abstract

Equity-index option markets quote hundreds of strikes and maturities each day, and the implied volatility surface that risk systems consume is economically admissible only if it excludes arbitrage on a single date and across dates. This report synthesises 41 studies on how four families of construction methods enforce those constraints: parametric construction, penalty-augmented objectives, projection-repair, and generation-filtering. Search, screening, abstract-level verification and evidence grading followed the `deep-research` full-mode protocol; no PRISMA compliance is claimed. Coding of an evidence matrix shows that 17 sources assert their guarantee at proof level, 16 report a numerical test, and 8 assert admissibility without either (Anagha, 2026)<!--ref:G6--><!--anchor:section:Abstract-->. In all 41 rows the certified object is a single date's surface; only ten engage time at all, and none enforces or tests dynamic no-arbitrage (Niu, 2015)<!--ref:C2--><!--anchor:section:Abstract-->. Proof-level and audit-level evidence come from almost disjoint source sets, and no two studies share data, metric and tolerance, so zero rows are directly comparable (Xiong & Liu, 2026)<!--ref:R5--><!--anchor:section:Abstract-->. The literature answers the static question and leaves the dynamic one open; the appropriate output is a research agenda, not a ranking of methods.

**Keywords:** implied volatility surface; no-arbitrage; static arbitrage; dynamic consistency; model validation; equity-index options

## 1. Introduction

### 1.1 Context

An equity-index option market quotes several hundred strike–maturity pairs on a typical trading day. Risk systems, clearing houses and market-making desks do not consume those quotes individually; they consume a fitted implied volatility surface from which prices, Greeks and risk-neutral densities are derived (Fengler, 2009)<!--ref:S2--><!--anchor:section:1.1-->. That surface is economically coherent only if it embeds no arbitrage. On a single date, call prices must be non-increasing and convex in strike, total variance must not decrease with maturity, and the zero-maturity limit must match intrinsic value (Gatheral & Jacquier, 2013<!--ref:S1--><!--anchor:section:1.1-->; Guo et al., 2016)<!--ref:P1--><!--anchor:section:1.1-->. Across dates, no self-financing strategy in the option panel may produce a riskless profit (Niu, 2015)<!--ref:C2--><!--anchor:section:1.1-->. Construction is therefore a constrained estimation problem rather than an interpolation problem, and it operates at scale: fits run on dense, noisy quote panels (Wiedemann et al., 2025)<!--ref:N2--><!--anchor:section:1.1--> and repairs on grids of tens of thousands of cells (Xiong & Liu, 2026)<!--ref:R5--><!--anchor:section:1.1-->. Because the surface is what prices, hedges and clears, a fitted artefact that admits arbitrage propagates into risk numbers, margin and capital; it is not a cosmetic defect in a plot.

### 1.2 Problem Statement

The phrase "arbitrage-free" does not denote one property. A method may be arbitrage-free because its parameter domain excludes violations (Guo et al., 2016)<!--ref:P1--><!--anchor:section:1.2-->, because a penalty discourages them (Na et al., 2023)<!--ref:N5--><!--anchor:section:1.2-->, because a post-fit map removes them (Bender & Thiel, 2020)<!--ref:R3--><!--anchor:section:1.2-->, or because a generator is screened before output (Bajalica et al., 2026)<!--ref:G5--><!--anchor:section:1.2-->. These are different guarantees with different failure modes: a theorem, an optimisation residual, a repaired point, and an accepted sample are not interchangeable evidence. The literature rarely separates them, and it uses the same phrase for the static condition and for the dynamic one, although the second concerns the joint law of a surface process rather than the admissibility of one surface (Niu, 2015)<!--ref:C2--><!--anchor:section:1.2-->. The resulting risk is claim inflation: a numerically tested method may be read as a proved one, and a static guarantee as a dynamic one. Three questions therefore have to be asked of any claim: which condition is meant, at what tolerance it holds, and by what means it was verified. Those questions become the coding instrument used in Section 4.

### 1.3 Purpose and Research Question

The purpose of this report is to characterise—not rank—how the four families carry their constraints, and to identify what evidence exists for each. The guiding question is:

> How do parametric construction, penalty, projection-repair, and generation-filtering methods for constructing equity-index implied volatility surfaces enforce static and dynamic no-arbitrage constraints?

Three hypotheses structured the synthesis: that static admissibility is mostly obtained by construction while dynamic consistency is asserted or tested rather than proved; that penalty and repair methods reduce fit error but displace the burden onto tolerances, weights and repair steps that are rarely validated out of sample; and that for generation-filtering methods "arbitrage-free" usually means "not rejected on this sample". Each hypothesis is assessed explicitly in Section 4. They fix the evidential target; they are not a prediction about which family performs best.

### 1.4 Significance

The result matters for model validation, for benchmark design, and for the field's vocabulary. A validation team that reads "arbitrage-free" as a uniform property will over-credit methods whose guarantee holds only up to tolerance. A benchmark that compares violation rates across studies without matching data, grid and tolerance will produce an ordering that the underlying evidence cannot support. The contribution here is a diagnostic of what the corpus does and does not establish, not a recommendation among methods. It matters methodologically as well: if the corpus cannot compare families, the correct response is to design comparability rather than to aggregate incomparable numbers.

### 1.5 Structure of the Report

Section 2 fixes the admissibility object and the four-family taxonomy. Section 3 records how the corpus was found, screened, verified and graded. Section 4 reports the evidence matrix, themes and tensions. Section 5 interprets the pattern and states its limits, and Section 6 converts the gaps into an agenda. Appendices A–C reproduce the queries, the screening counts and the 41-row ledger, so that every number in the body can be traced to a recorded artefact.

## 2. Literature Review and Theoretical Framework

### 2.1 The Static Admissibility Object

Following the corpus, write total implied variance as $w(k,\tau)=\sigma^2\tau$, where $k=\log(K/F_\tau)$ and $F_\tau$ is the forward. A surface is statically admissible if, expressed through the normalised call price $c(k,\tau)=C/F_\tau$, it satisfies: (C1) $c-\max(1-e^{k},0)\ge 0$; (C2) $\partial c/\partial k\le 0$; (C3) $\partial^2 c/\partial k^2\ge 0$, the butterfly or Durrleman condition; (C4) the zero-maturity limit $c(\cdot,0)=\max(1-e^{k},0)$; and (C5) $w$ is non-decreasing in $\tau$ (Gatheral & Jacquier, 2013<!--ref:S1--><!--anchor:section:2.1-->; Martini & Mingone, 2022<!--ref:P2--><!--anchor:section:2.1-->; Anagha, 2026)<!--ref:G6--><!--anchor:section:2.1-->. Dynamic no-arbitrage is a statement about a filtered family of surfaces in which each member is statically admissible and the joint law admits a martingale representation consistent with the numéraire (Niu, 2015)<!--ref:C2--><!--anchor:section:2.1-->. Conditions (C1)–(C4) encode a non-negative risk-neutral density in price space; (C5) makes the object a surface rather than a family of slices. No source in the corpus states a testable version of the dynamic condition; the one model that comes closest explicitly declines to claim it (Cohen et al., 2021)<!--ref:G7--><!--anchor:section:2.1-->.

### 2.2 Four Families, Four Loci of Enforcement

The corpus supports a taxonomy organised by *where* the constraint acts rather than by model class (Table 1). Parametric methods restrict the parameter domain; penalty methods add violation terms to the fitting objective; projection-repair methods modify the fitted output; generation-filtering methods restrict the support of a sampler or screen its output. The loci differ in what evidence they can produce and in how they fail. Boundary cases are disclosed rather than forced: the strict finite-grid construction of Buehler et al. (2026)<!--ref:R6--><!--anchor:section:2.2-->, the distortion-based interpolation of Bender and Thiel (2020)<!--ref:R3--><!--anchor:section:2.2-->, and the gated architecture of Cao et al. (2020)<!--ref:N1--><!--anchor:section:2.2--> each sit under two loci. The loci are also evidence-generating conventions: a theorem, an optimisation residual and an acceptance test are the best each family can produce, which is why the four are compared by evidential kind rather than by a shared performance metric.

**Table 1**

*Four families of implied-volatility-surface construction, by enforcement locus*

| Family | Enforcement locus | Mechanism | What it establishes | Typical failure mode |
|---|---|---|---|---|
| Parametric construction | Parameter domain | Restrictions make slices convex and total variance monotone | Static admissibility by construction | Tight wings, fit loss, dynamic behaviour unaddressed |
| Penalty | Objective | Violation terms added to the fit loss with weights | Approximate compliance conditional on weight and tolerance | Residual violations, weight sensitivity, no guarantee |
| Projection-repair | Post-fit output | Surface projected onto the admissible set | Static conditions at the repaired point | Repair distorts fit and drifts; no cross-date enforcement |
| Generation-filtering | Sampler and acceptance test | Candidates generated, accepted or rejected by arbitrage tests | Compliance on the accepted finite sample | A passed test is not a proof; rejection cost; power unknown |

*Note.* Adaptation of the frozen taxonomy fixed in Phase 1; families are not asserted to be exhaustive, and three studies are coded under two loci.

### 2.3 The Seven-Dimension Evaluation Matrix

Eight evaluation dimensions were declared before synthesis (Table 2). They are axes, not score columns: a surface can be admissible and unstable, or accurate and uninterpretable, and no weighting is implied. Coverage is reported as the number of rows that supply evidence of the relevant kind, and coverage is not quality. The matrix is the instrument used in Section 4 to organise what the corpus can and cannot answer. Read across a row, it shows what evidence a dimension would require; read down a column, it shows where the corpus supplies almost nothing.

**Table 2**

*Declared evaluation dimensions and corpus coverage*

| Dimension | Rows contributing evidence | Status |
|---|---|---|
| Static no-arbitrage | 41 of 41 | Coded on every row (17 proof, 16 test, 8 assertion); tolerances rarely stated |
| Dynamic consistency | 10 | Ten engage time; none enforces or tests |
| Fit accuracy | ~8 | Numbers reported on disjoint datasets; not comparable |
| Interpolation and stability | ~8 | Thin; no audit at the boundary where guarantees bind |
| Extrapolation and wings | ~6 | Wing behaviour asserted, not measured |
| Computational cost | ~5 | Claims only; no common-hardware measurements |
| Interpretability | 0 | No row assesses interpretability |
| Reproducibility | ~4 | Code and data availability rarely stated |

*Note.* Counts are from the Phase 3 evidence matrix; "~" marks counts that depend on how a reported artefact is classified.

### 2.4 The Condition Lineage and Scale-Relativity

The condition literature is a monotone refinement rather than a set of competing theories. Early nonparametric specifications carried no explicit constraint (Bodurtha & Jermakyan, 1999)<!--ref:S4--><!--anchor:section:2.4-->, so the refinement begins from a baseline that was not admissible in any stated sense. Gatheral and Jacquier (2013)<!--ref:S1--><!--anchor:section:2.4--> give sufficient closed-form conditions for SVI surfaces; Martini and Mingone (2022)<!--ref:P2--><!--anchor:section:2.4--> turn the butterfly requirement into an exact characterisation via the monotonicity of $-d_1$ and $-d_2$ and Durrleman's condition; Mingone (2022)<!--ref:P3--><!--anchor:section:2.4--> lifts the construction to a global all-maturity eSSVI parameterisation. Necessity claims enter more weakly: the only necessary-and-sufficient statement is a metadata-only preprint (Klassen, 2016)<!--ref:P7--><!--anchor:section:2.4-->, and its result cannot be inspected at abstract level. A parallel line makes admissibility scale-relative: Fukasawa (2022)<!--ref:C4--><!--anchor:section:2.4--> proves asymptotic arbitrage-freeness of BBF, SABR and rough SABR formulas, while Hagan et al. (2014)<!--ref:S3--><!--anchor:section:2.4--> show that the explicit SABR formulas are arbitrageable in the low-strike wings at finite strikes. Two recent constructions widen rather than narrow the admissible set (Zaugg et al., 2025)<!--ref:P5--><!--anchor:section:2.4--> and interpolate raw quotes by construction (Le Floc'h, 2025)<!--ref:P6--><!--anchor:section:2.4-->, while Buehler et al. (2026)<!--ref:R6--><!--anchor:section:2.4--> sharpen the condition to a strict finite-grid form. The direction of refinement is toward conditions that can be checked on a finite grid, which is precisely what an audit would need. "Arbitrage-free" is therefore always relative to a domain, a scale and a tolerance.

## 3. Methodology

### 3.1 Search Strategy and Scope

Discovery used the OpenAlex REST API, anonymously and without a key, between 2026-01-01 and 2026-11-23; the last search ran on 2026-11-23. Thirty-one free-text query strings were submitted in eight groups—two broad, six parametric, two penalty, three projection-repair, six generation-filtering, six neural, three dynamic, three evaluation—each returning 25 relevance-ranked records. OpenAlex's interface accepts free text rather than Boolean expressions, so the conceptual string ("implied volatility surface" AND "no-arbitrage" AND a method term) was decomposed across queries (Appendix A). Inclusion required an implied-volatility or option-price surface construction with an enforcement claim, equity-index applicability, English, OpenAlex resolvability, and one record per study; pre-2015 work was admitted only as flagged seminal background. One query returned nothing after a transient rate-limit and was not successfully re-run, a limitation carried forward. The window starts at 2015 because earlier SVI and SABR results are treated as baselines, and it ends at the search date; a time-bounded corpus risks vocabulary drift, since method names change faster than the underlying conditions. One snowballing pass from the included set supplemented the queries. Equity indices are the setting because their option panels are the deepest and their arbitrage conditions the most studied; single-name equities, foreign exchange, rates and crypto underlyings were excluded by design, which bounds the generality of every finding.

### 3.2 Screening

The 31 queries yielded 775 records, of which 430 remained after de-duplication. Title screening excluded 389 records under eight pre-specified reason codes—off-topic (141), pre-2015 background (86), relevant but not selected (40), out-of-scope asset (34), publication type (32), duplicate version (31), forecasting or trading (21), and calibration or pricing only (4)—leaving 41 studies whose abstracts were then read (Appendix B). Two records were replaced during abstract reading when the retrieved text showed no enforcement claim. Screening was performed by a single reviewer; no dual screening, adjudication or kappa is claimed. Exclusions were applied at title level for the whole pool and confirmed at abstract level only for the included set; the asymmetric depth is a direct cost of the abstract-only read scope, and the "relevant but not selected" bucket keeps the decision visible rather than silent. That bucket is the largest discretionary decision in the flow: 40 records were excluded for relevance rather than for a rule, which is why it is reported separately from the rule-based codes.

### 3.3 Verification

Each record was resolved through OpenAlex's DOI endpoint; all 41 lookups returned HTTP 200 and none is flagged retracted. Abstracts were reconstructed from the OpenAlex inverted index and, where necessary, Crossref and Semantic Scholar, producing 34 full abstracts, four partial ones and three metadata-only records (Corbetta et al., 2019<!--ref:P4--><!--anchor:section:3.3-->; Klassen, 2016<!--ref:P7--><!--anchor:section:3.3-->; Yao et al., 2026)<!--ref:R4--><!--anchor:section:3.3-->. Five cross-source claim clusters covered 19 of the 41 sources; no claim is independently replicated within the corpus. Verification returned a conditional pass with five conditions: metadata-only rows may be cited only at title level; preprint status must be flagged at the point of use; no numerically tested method may be described as arbitrage-free; violation, fit and hedging numbers may not be compared across studies; and dynamic arbitrage must be reported as unverified. Within the five clusters, sources agree on the qualitative requirement but not on a single measurement: the SVI cluster agrees on the shape conditions, the penalty cluster disagrees on violation magnitudes, and the repair cluster reports floors that depend on the grid.

### 3.4 Evidence Grading and Comparability Coding

Two grading axes were applied. Evidence level runs from level I (systematic review) to level VII (narrative review); the corpus contains 40 level VI studies and one level VII review (C2). A six-criterion rubric produced grades of A (11), B (13) and C (17), with integrity floors: a numerical test cannot receive A, and claim-only, abstract-unavailable, preprint, practitioner or metadata-only rows cannot exceed C. Every row also received an evidence-status label taken from what the abstract reports—proof, numerical test, or assumption—and a comparability code. Comparability is deliberately conservative: 0 rows are directly comparable, 30 are reported for context, and 11 are not comparable at all. No ranking, vote count or citation metric is used anywhere in this report. The floors matter because they cap what a source can claim regardless of how confident its abstract sounds: a numerical test cannot be promoted to a proof by careful reading.

### 3.5 Analytical Framework and Boundedness

Synthesis coded each row as a triple of model class, enforcement operator and verification mode, using static and dynamic definitions fixed before coding (Section 2.1); a per-date maturity-monotonicity condition was not coded as dynamic. Because the read scope was abstracts throughout, every statement about a method's evidence is bounded by what the abstract reports: absence of a reported audit is not evidence that no audit was performed. The design is a comparative, constraint-centred narrative synthesis with no meta-analysis and no re-estimation, and it makes no PRISMA or PRISMA-ScR compliance claim. Coding judgements were made by one analyst. Every count in Section 4 is therefore a count of what abstracts report, and the verb "reports" is used deliberately throughout.

## 4. Findings

### 4.1 Evidence-Status Distribution

Across the 41 rows the reported evidence splits 17 proof, 16 numerical test and 8 assumption (Table 3). The split is uneven by family: parametric rows are almost entirely proof-level, penalty rows are entirely test-based, and generation-filtering contains both. The eight assumption rows include all three metadata-only records and two pre-constraint baselines, so they are weakest exactly where inspection is least possible. The proof concentration in the parametric family and the test concentration in the penalty family are the clearest structural signal: the two families almost never produce the same kind of evidence. The assumption rows cluster in exactly the families that also carry the metadata-only records, so the weakest evidence labels and the weakest retrieval coincide.

**Table 3**

*Reported evidence status by family*

| Family | Proof | Numerical test | Assumption | Total |
|---|---|---|---|---|
| Parametric construction | 6 | 0 | 2 | 8 |
| Penalty and constrained learning | 0 | 6 | 0 | 6 |
| Projection and repair | 3 | 4 | 2 | 9 |
| Generation and filtering | 4 | 3 | 1 | 8 |
| Conditions and diagnostics | 3 | 1 | 1 | 5 |
| Seminal baselines | 1 | 2 | 2 | 5 |
| **Total** | **17** | **16** | **8** | **41** |

*Note.* Status is the status reported by the source, not a quality grade; assumption rows include all three metadata-only records.

### 4.2 Family Findings

The four subsections follow the taxonomy; each reports what a family's rows establish and what they leave unmeasured. Eleven of the rows are preprints—P7, P8, N3, N5, N6, R2, R6, R7, R8, G6 and C2—and every claim drawn from them is read as provisional.

**Parametric construction.** Six of the eight parametric rows are proof-level, and the guarantee is uniformly structural: the parameter map is chosen so that the admissible set is the image of the parameter domain (Guo et al., 2016<!--ref:P1--><!--anchor:section:4.2-->; Martini & Mingone, 2022)<!--ref:P2--><!--anchor:section:4.2-->. Martini and Mingone (2022) obtain a full butterfly characterisation and report least-squares calibration restricted to the admissible domain; Mingone (2022)<!--ref:P3--><!--anchor:section:4.2--> builds a global all-maturity eSSVI parameterisation; Barski and Wiśniewolski (2026)<!--ref:P8--><!--anchor:section:4.2--> derive explicit arbitrage probabilities for Gaussian factor models. The two metadata-only rows (Corbetta et al., 2019<!--ref:P4--><!--anchor:section:4.2-->; Klassen, 2016)<!--ref:P7--><!--anchor:section:4.2--> show only that a constrained calibration and a necessary-and-sufficient condition are claimed in their titles [Title/metadata only]. No parametric row reports a finite-sample violation audit, and no parametric row tests behaviour across dates. The lineage is cumulative rather than competitive: one result generalises the SVI family, one characterises it exactly, one makes it global.

**Penalty and constrained learning.** All six rows are numerical tests and none reports a violation-rate distribution. Cao et al. (2020)<!--ref:N1--><!--anchor:section:4.2--> gate hidden layers so that slopes and weights satisfy the constraints and report out-of-sample forecasting and hedging gains on S&P 500 data; Wiedemann et al. (2025)<!--ref:N2--><!--anchor:section:4.2--> train a graph neural operator on ten years of intraday S&P 500 quotes and report adherence to critical constraints. Ackerer et al. (2019)<!--ref:N3--><!--anchor:section:4.2--> use soft-constraint penalties with a plug-in correction on classical volatility models and report gains on sparse or erroneous quotes [preprint]. The remaining rows are more candid: Sidogi et al. (2022)<!--ref:N4--><!--anchor:section:4.2--> find that a static-arbitrage loss improves distributional fit while the framework "cannot directly learn the condition"; Na et al. (2023)<!--ref:N5--><!--anchor:section:4.2--> state in their title that violations are only minimised; Hoshisashi et al. (2023)<!--ref:N6--><!--anchor:section:4.2--> penalise derivatives on SABR-generated prices. The two rows that report adherence do so without stating a tolerance, which makes their audits hard to reproduce.

**Projection and repair.** Repair rows differ in what they owe: a distortion bound, an optimality property, or both. Cohen et al. (2020)<!--ref:R1--><!--anchor:section:4.2--> solve a linear program that changes prices minimally inside bid–ask bounds; De March and Henry-Labordère (2019)<!--ref:R2--><!--anchor:section:4.2--> prove convergence of a Sinkhorn projection; Bender and Thiel (2020)<!--ref:R3--><!--anchor:section:4.2--> interpolate through an arbitrage-free reference function. Zetocha (2023)<!--ref:R8--><!--anchor:section:4.2--> asserts arbitrage-free transformations for extrapolation and surface dynamics without stating either a proof or a test [preprint]. Three rows report what repair actually leaves behind. Xiong and Liu (2026)<!--ref:R5--><!--anchor:section:4.2--> repair calendar violations to approximately zero and a butterfly floor of about 5.4 percent over 252 out-of-sample days on SPX; Alvarez (2025)<!--ref:R7--><!--anchor:section:4.2--> reports below one percent static violations with 98–99 percent inside-spread coverage in calm years; Madan and Schoutens (2019)<!--ref:R9--><!--anchor:section:4.2--> approximate 2,695 SPY options across 28 maturities. The metadata-only American-option row (Yao et al., 2026)<!--ref:R4--><!--anchor:section:4.2--> cannot be assessed beyond its title [Title/metadata only]. The strictest proof-level member of the family is explicit about the finite grid (Buehler et al., 2026)<!--ref:R6--><!--anchor:section:4.2-->, though its market illustration is not quantified.

**Generation and filtering.** The family splits in two. The learned-parametric branch inherits its guarantee from the decoder or architecture: a VAE over SDE parameters (Ning et al., 2023)<!--ref:G1--><!--anchor:section:4.2-->, a constrained state space in a neural SDE (Cohen et al., 2021)<!--ref:G7--><!--anchor:section:4.2-->, gated networks (Yang et al., 2017)<!--ref:G8--><!--anchor:section:4.2-->. A generator trained as a denoiser maps noisy, arbitrage-violating surfaces to smooth ones and reports lower error and runtime than traditional smoothing (Ginart Belmonte & Cole, 2025)<!--ref:G4--><!--anchor:section:4.2-->. The penalised-sampling branch reports residuals instead: Bajalica et al. (2026)<!--ref:G5--><!--anchor:section:4.2--> report that 90.8 percent of generated surfaces pass all tested conditions, while Anagha (2026)<!--ref:G6--><!--anchor:section:4.2--> reports zero violations at a tolerance of $10^{-4}$ across 15 runs—on synthetic SVI slices—using input-convex blocks gated by non-negative maturity ramps, an architecture that makes the constraint structural rather than penalised, and higher total-variance RMSE than SSVI and a soft-penalty multilayer perceptron. Only the second branch measures anything, and only on synthetic data. The realism-driven models learn co-movement and hedging behaviour without stating an enforcement mechanism (Vuletić & Cont, 2024)<!--ref:G2--><!--anchor:section:4.2-->, which is the characteristic weakness of a family judged by output plausibility rather than by constraints.

### 4.3 Cross-Cutting Themes

Five themes survive the coding, and each is stated with the source set that supports it.

**Static scope of the certification.** In all 41 rows "arbitrage-free" is a predicate on a single surface. The dynamic condition is named in fewer than a quarter of the corpus—Niu (2015)<!--ref:C2--><!--anchor:section:4.3--> sets it out most fully—and is enforced in none.

**Four loci, four meanings.** A parameter-domain statement, an optimisation residual, a repaired point and an accepted sample are not interchangeable evidence. The four loci produce four different meanings of the same phrase, and the difference is evidential rather than rhetorical.

**Disjoint evidential channels.** Proof and audit come from almost disjoint source sets. Of the 17 proof-level rows only Anagha (2026)<!--ref:G6--><!--anchor:section:4.3--> both guarantees and audits, and the audit is synthetic; of the six rows reporting residuals, none states a theorem and two state explicitly that violations are only minimised (Na et al., 2023<!--ref:N5--><!--anchor:section:4.3-->; Sidogi et al., 2022)<!--ref:N4--><!--anchor:section:4.3-->. An independent detector exists (Neufeld & Sester, 2024)<!--ref:C1--><!--anchor:section:4.3-->, but it was never applied to another row's output.

**The measured cost of the guarantee.** Where the trade-off is measured it points one way: a tighter constraint buys fewer violations at a higher fit error. The direction is observed once, on synthetic data (Anagha, 2026)<!--ref:G6--><!--anchor:section:4.3-->, and is consistent with the repair floors reported elsewhere (Xiong & Liu, 2026<!--ref:R5--><!--anchor:section:4.3-->; Alvarez, 2025)<!--ref:R7--><!--anchor:section:4.3-->.

**Fragmented evaluation vocabulary.** At least seven metric families are in use—violation rate, implied-volatility and total-variance RMSE, Wasserstein distance, hedging profit and loss, inside-spread coverage, detection performance and runtime—and no two rows share metric, dataset and tolerance together, so comparative claims can only be about kinds of evidence.

### 4.4 Tensions

Five tensions are load-bearing, and each has a verdict.

**Static proof versus dynamic behaviour.** A tension between objects rather than a contradiction: no row proves a process-level statement, and the one neural-SDE model explicitly declines the dynamic claim (Cohen et al., 2021)<!--ref:G7--><!--anchor:section:4.4-->. It is reconcilable only by proving a property of the process, which no row does.

**Interpolation quality versus guarantees.** Irreconcilable on current evidence: no row measures interpolation error at the boundary where its own guarantee binds, so a surface can satisfy every static condition and still distort prices between quoted strikes.

**Quote noise versus test rejection.** A zero violation rate on synthetic data (Anagha, 2026)<!--ref:G6--><!--anchor:section:4.4-->, approximately zero calendar violations on SPX (Xiong & Liu, 2026)<!--ref:R5--><!--anchor:section:4.4--> and a 90.8 percent pass rate on generated surfaces (Bajalica et al., 2026)<!--ref:G5--><!--anchor:section:4.4--> cannot be separated without a noise floor, and no row estimates one or reports the power of its test.

**Expressiveness versus constraint strength.** Enlarging the admissible set is possible in principle and demonstrated in two constructions (Zaugg et al., 2025<!--ref:P5--><!--anchor:section:4.4-->; Alvarez, 2025)<!--ref:R7--><!--anchor:section:4.4-->, but the cost of doing so is measured in one row only.

**Definitional conflation.** "Calendar" denotes both maturity monotonicity within a date and cross-date consistency. The conflation inflates apparent dynamic coverage and makes reported violation rates, which are usually static, look broader than they are; it is the most consequential definitional problem in the corpus.

### 4.5 The Dynamic No-Arbitrage Void

Ten rows engage time at all: an arbitrage-probability model for Gaussian factors (Barski & Wiśniewolski, 2026)<!--ref:P8--><!--anchor:section:4.5-->, a Markov-chain repair with a full maturity axis (Madan & Schoutens, 2019)<!--ref:R9--><!--anchor:section:4.5-->, three generative models of surface dynamics (Ning et al., 2023<!--ref:G1--><!--anchor:section:4.5-->; Vuletić & Cont, 2024<!--ref:G2--><!--anchor:section:4.5-->; Cont & Vuletić, 2023)<!--ref:G3--><!--anchor:section:4.5-->, a path-dependent volatility model (Andrès et al., 2026)<!--ref:C3--><!--anchor:section:4.5-->, a review of dynamic conditions (Niu, 2015)<!--ref:C2--><!--anchor:section:4.5-->, and a bubble diagnostic (Stahl & Blauth, 2024)<!--ref:C5--><!--anchor:section:4.5-->. None converts its engagement into a dynamic guarantee or a dynamic test: the number is 0 of 41. The consequence is that the corpus cannot answer the second half of the research question, and says so only implicitly. The nearest statements are descriptive rather than conditional: surface paths that are static-arbitrage-free by construction (Andrès et al., 2026)<!--ref:C3--><!--anchor:section:4.5-->, and martingale defects used as bubble indicators on a 2,576-stock, 26-year panel (Stahl & Blauth, 2024)<!--ref:C5--><!--anchor:section:4.5-->.

### 4.6 Comparability Caveats

No pair of rows shares data, metric and tolerance simultaneously, so the comparability code is zero out of 41. Violation rates are reported against synthetic SVI slices, SPX completion grids, equity panels and generated surfaces; fit errors use implied-volatility RMSE, total-variance RMSE, Wasserstein distance or reconstruction error; and tolerances are frequently unstated. Comparative statements in this report are therefore limited to kinds of evidence—proof versus test versus assertion—and to within-study orderings where a source compares its own baselines. A comparable design would fix four fields before any number is collected: the panel of quote dates and strikes, the condition set with its tolerance, the metric with its aggregation rule, and the format for reporting residual violations. No row in the corpus fixes more than two. Tolerance is the most frequently missing field: without it, a violation rate is not a reproducible measurement, and the three residual-reporting rows that do state their settings are the only ones whose numbers can be read at all.

## 5. Discussion

### 5.1 Interpretation

The pattern is coherent once the two conditions are separated. Static admissibility is a finite-dimensional, checkable property, and the field has solved it in four distinct ways that agree on the object even when they disagree on the method. Dynamic admissibility is a statement about a stochastic process; it requires a model of how the surface evolves, and none of the constructions supplies one with a proof. The proof/audit asymmetry is the more interesting finding: the sources that establish results are rarely the sources that measure residual violations, so a reader who wants both must combine sources that were never designed to be combined. That asymmetry is plausibly a publication norm—theorems and empirical audits belong to different journals—but it is also the reason the corpus cannot adjudicate between families. A second reading is equally consistent with the evidence: abstracts may under-report audits that exist in full texts, so the asymmetry could be a retrieval effect rather than a field-level fact. Within this read scope the two readings cannot be separated, and that is the most consequential unanswered question.

### 5.2 Implications

For model validation, the practical implication is that "arbitrage-free" must be resolved into three questions: which condition, at what tolerance, and verified how. A validation file that records the mechanism and the verification mode, as the ledger in Appendix C does, is more informative than one that records a label. For benchmark design, the implication is that comparison requires a shared panel, a shared tolerance grid and a pre-registered metric before any head-to-head claim is credible. For the field's vocabulary, the implication is that static and dynamic claims should be stated separately in titles and abstracts; the current conflation is not a stylistic issue but a source of misattribution. For reporting practice, the implication is that a surface should carry its enforcement locus and verification mode as metadata, much as a dataset carries its licence. For journals, the same logic argues for requiring a machine-readable enforcement statement alongside any empirical claim of arbitrage freeness, in the way that numerical papers are increasingly expected to report solver tolerances.

### 5.3 Limitations

Eleven of the 41 sources (26.8 percent) are preprints, six of them from 2025–2026, and the strictest claims cluster there, so the most recent and most confident claims are also the least settled ones; three records are metadata-only (Corbetta et al., 2019<!--ref:P4--><!--anchor:section:5.3-->; Klassen, 2016<!--ref:P7--><!--anchor:section:5.3-->; Yao et al., 2026)<!--ref:R4--><!--anchor:section:5.3--> and can be cited only at title level; four abstracts are partial (De March & Henry-Labordère, 2019<!--ref:R2--><!--anchor:section:5.3-->; Cont & Vuletić, 2023<!--ref:G3--><!--anchor:section:5.3-->; Niu, 2015<!--ref:C2--><!--anchor:section:5.3-->; Fukasawa, 2022)<!--ref:C4--><!--anchor:section:5.3-->. The read scope was abstract-level throughout, so no theorem was checked, no residual was recomputed, and absence claims are bounded by what abstracts report. Screening and coding were performed by a single analyst, without dual screening, adjudication or inter-rater agreement; the same analyst wrote this synthesis, so construct-level judgements are single-coded. The corpus is English-only, drawn from a single index (OpenAlex), and dominated by US index data—ten of the twelve rows with known provenance (approximately 83 percent)—with only a 2006 DAX study (Fengler et al., 2006)<!--ref:S5--><!--anchor:section:5.3--> and a 2022 JSE study (Sidogi et al., 2022)<!--ref:N4--><!--anchor:section:5.3--> outside the United States. One discovery query failed and was not re-run, so the pool is not exhaustive. No conflict-of-interest or funding statement was retrieved for any record, and no citation counts were used. Finally, the enforceability taxonomy and the seven-dimension matrix are proposed instruments that this report applies but does not validate. No negative results were retrieved: studies that applied a family and found the guarantee failed are not visible in the pool, so the prevalence of reported success may be overstated.

## 6. Conclusion and Recommendations

### 6.1 Research Agenda

The gaps translate into seven concrete studies, offered as an agenda rather than a method ranking. First, a dynamic enforcement study: fix a daily SPX panel, implement one construction per family, test the sequence for dynamic violations, and report test power alongside the result. Second, a pre-registered head-to-head evaluation on identical data, metrics and tolerance grid. Third, a residual audit for proof-level constructions—the cheapest gap to close, since it only requires counting finite-precision violations at an implied tolerance (as Anagha, 2026<!--ref:G6--><!--anchor:section:6.1--> does on synthetic data). Fourth, a measurement of test power and the noise floor, by injecting graduated arbitrage and reporting detection curves. Fifth, data-efficiency studies reporting learning curves against SVI at matched quote counts. Sixth, a cross-market study applying one method to three indices, including an emerging market. Seventh, measured rather than asserted computational cost and interpretability. The agenda is ordered by cost: residual audits and test-power estimation can run on existing quote panels, while the dynamic-panel and cross-market studies require new data collection before they can begin.

### 6.2 Concluding Statement

On the evidence available, the four families are better understood as four kinds of claim than as four competing products. Parametric construction offers proof without audit, repair offers audit without proof, penalty methods offer neither, and generation-filtering offers either, depending on how the generator is built. That division is the finding: the literature answers the static question and has not yet posed the dynamic one in a testable form. It is a claim about the evidence, not about the quality of any method.

## AI Disclosure

AI Disclosure: This report was produced with AI-assisted research tools. The research pipeline included AI-powered literature search, source verification, evidence synthesis, and report drafting. All findings were verified against cited sources. Human oversight was applied throughout the process.

## References

- Ackerer, D., Tagasovska, N., & Vatter, T. (2019). Deep smoothing of the implied volatility surface [Preprint]. *SSRN Electronic Journal*. https://doi.org/10.2139/ssrn.3402942
- Alvarez, R. J. (2025). Arbitrage-free option price surfaces via Chebyshev tensor bases and a Hamiltonian fog post-fit [Preprint]. *arXiv*. https://doi.org/10.48550/arxiv.2512.01967
- Anagha, S. (2026). Trainable hard constraints: Architectural enforcement of arbitrage-free implied volatility surfaces via automatic differentiation [Preprint]. *SSRN Electronic Journal*. https://doi.org/10.2139/ssrn.7577418
- Andrès, H., Boumezoued, A., & Jourdain, B. (2026). The implied volatility surface (also) is path-dependent. *Quantitative Finance*, *26*(7), 1017–1047. https://doi.org/10.1080/14697688.2026.2637739
- Bajalica, D., Brooks, O., & Ben Tahar, I. (2026). Latent flow matching for arbitrage-aware implied volatility surface generation. In *Proceedings of the ACM International Conference on AI in Finance (ICAIF)* (pp. 708–716). https://doi.org/10.1145/3858063.3858741
- Barski, M., & Wiśniewolski, M. (2026). Implied volatility models without static arbitrage [Preprint]. *arXiv*. https://doi.org/10.48550/arxiv.2611.18937
- Bender, C., & Thiel, M. (2020). Arbitrage-free interpolation of call option prices. *Statistics & Risk Modeling*, *37*(1–2), 55–78. https://doi.org/10.1515/strm-2018-0026
- Bodurtha, J. N., & Jermakyan, M. (1999). Nonparametric estimation of an implied volatility surface. *The Journal of Computational Finance*, *2*(4), 29–60. https://doi.org/10.21314/jcf.1999.034
- Buehler, H., Horvath, B. N., Kratsios, A., Limmer, Y., & Saqur, R. (2026). SANOS: Smooth strictly arbitrage-free non-parametric option surfaces [Preprint]. *arXiv*. https://doi.org/10.48550/arxiv.2601.11209
- Cao, Y., Liu, X., & Zhai, J. (2020). Option valuation under no-arbitrage constraints with neural networks. *European Journal of Operational Research*, *293*(1), 361–374. https://doi.org/10.1016/j.ejor.2020.12.003
- Cohen, S. N., Reisinger, C., & Wang, S. (2020). Detecting and repairing arbitrage in traded option prices. *Applied Mathematical Finance*, *27*(5), 345–373. https://doi.org/10.1080/1350486x.2020.1846573
- Cohen, S. N., Reisinger, C., & Wang, S. (2021). Arbitrage-free neural-SDE market models. *Applied Mathematical Finance*, *30*(1), 1–46. https://doi.org/10.1080/1350486x.2023.2257217
- Cont, R., & Vuletić, M. (2023). Simulation of arbitrage-free implied volatility surfaces. *Applied Mathematical Finance*, *30*(2), 94–121. https://doi.org/10.1080/1350486x.2023.2277960
- Corbetta, J., Cohort, P., Laachir, I., & Martini, C. (2019). Robust calibration and arbitrage-free interpolation of SSVI slices. *Decisions in Economics and Finance*, *42*(2), 665–677. https://doi.org/10.1007/s10203-019-00249-8
- De March, H., & Henry-Labordère, P. (2019). Building arbitrage-free implied volatility: Sinkhorn's algorithm and variants [Preprint]. *SSRN Electronic Journal*. https://doi.org/10.2139/ssrn.3326486
- Fengler, M. R. (2009). Arbitrage-free smoothing of the implied volatility surface. *Quantitative Finance*, *9*(4), 417–428. https://doi.org/10.1080/14697680802595585
- Fengler, M. R., Härdle, W. K., & Mammen, E. (2006). A semiparametric factor model for implied volatility surface dynamics. *Journal of Financial Econometrics*, *5*(2), 189–218. https://doi.org/10.1093/jjfinec/nbm005
- Fukasawa, M. (2022). On asymptotically arbitrage-free approximations of the implied volatility. *Frontiers of Mathematical Finance*, *1*(4), 525–537. https://doi.org/10.3934/fmf.2022006
- Gatheral, J., & Jacquier, A. (2013). Arbitrage-free SVI volatility surfaces. *Quantitative Finance*, *14*(1), 59–71. https://doi.org/10.1080/14697688.2013.819986
- Ginart Belmonte, V., & Cole, T. (2025). Arbitrage-free implied volatility surface smoothing via generative adversarial networks. In *Proceedings of the ACM International Conference on AI in Finance (ICAIF)* (pp. 518–524). https://doi.org/10.1145/3768292.3771252
- Guo, G., Jacquier, A., Martini, C., & Neufcourt, L. (2016). Generalized arbitrage-free SVI volatility surfaces. *SIAM Journal on Financial Mathematics*, *7*(1), 619–641. https://doi.org/10.1137/120900320
- Hagan, P. S., Kumar, D., Lesniewski, A. S., & Woodward, D. E. (2014). Arbitrage-free SABR. *Wilmott*, *2014*(69), 60–75. https://doi.org/10.1002/wilm.10290
- Hoshisashi, K., Phelan, C. E., & Barucca, P. (2023). No-arbitrage deep calibration for volatility smile and skewness [Preprint]. *arXiv*. https://doi.org/10.48550/arxiv.2310.16703
- Klassen, T. (2016). Necessary and sufficient no-arbitrage conditions for the SSVI/S3 volatility curve [Preprint]. *SSRN Electronic Journal*. https://doi.org/10.2139/ssrn.2725700
- Le Floc’h, F. (2025). The quadratic local variance gamma model: An arbitrage-free interpolation of class C3 for option prices. *The Journal of Derivatives*, *32*(4), 91–115. https://doi.org/10.3905/jod.2025.1.228
- Madan, D. B., & Schoutens, W. (2019). Arbitrage free approximations to candidate volatility surface quotations. *Journal of Risk and Financial Management*, *12*(2), 69. https://doi.org/10.3390/jrfm12020069
- Martini, C., & Mingone, A. (2022). No arbitrage SVI. *SIAM Journal on Financial Mathematics*, *13*(1), 227–261. https://doi.org/10.1137/20m1351060
- Mingone, A. (2022). No arbitrage global parametrization for the eSSVI volatility surface. *Quantitative Finance*, *22*(12), 2205–2217. https://doi.org/10.1080/14697688.2022.2117076
- Na, A., Zhang, M., & Wan, J. W. L. (2023). Computing volatility surfaces using generative adversarial networks with minimal arbitrage violations [Preprint]. *arXiv*. https://doi.org/10.48550/arxiv.2304.13128
- Neufeld, A., & Sester, J. (2024). Neural networks can detect model-free static arbitrage strategies. *Applied Mathematics & Optimization*, *90*(2), 41. https://doi.org/10.1007/s00245-024-10184-9
- Ning, B., Jaimungal, S., Zhang, X., & Bergeron, M. (2023). Arbitrage-free implied volatility surface generation with variational autoencoders. *SIAM Journal on Financial Mathematics*, *14*(4), 1004–1027. https://doi.org/10.1137/21m1443546
- Niu, Q. (2015). No arbitrage conditions and characters of implied volatility surface: A review for implied volatility modelers [Preprint]. *SSRN Electronic Journal*. https://doi.org/10.2139/ssrn.2672416
- Sidogi, T., Mongwe, W. T., Mbuvha, R., & Marwala, T. (2022). Creating synthetic volatility surfaces using generative adversarial networks with static arbitrage loss conditions. In *2022 IEEE Symposium Series on Computational Intelligence (SSCI)* (pp. 1423–1429). https://doi.org/10.1109/ssci51031.2022.10022219
- Stahl, P., & Blauth, J. (2024). Martingale defects in the volatility surface and bubble conditions in the underlying. *Review of Derivatives Research*, *27*(1), 85–111. https://doi.org/10.1007/s11147-023-09200-x
- Vuletić, M., & Cont, R. (2024). VolGAN: A generative model for arbitrage-free implied volatility surfaces. *Applied Mathematical Finance*, *31*(4), 203–238. https://doi.org/10.1080/1350486x.2025.2471317
- Wiedemann, R., Jacquier, A., & Gonon, L. (2025). Operator deep smoothing for implied volatility. In *International Conference on Learning Representations (ICLR 2025)*. https://doi.org/10.48550/arxiv.2406.11520
- Xiong, Y., & Liu, B. (2026). Observation-anchored arbitrage repair for sparse implied volatility surface completion. In *2026 IEEE Conference on Computational Intelligence for Financial Engineering & Economics (CIFEr)* (pp. 155–162). https://doi.org/10.1109/cifer67845.2026.11692406
- Yang, Y., Zheng, Y., & Hospedales, T. M. (2017). Gated neural networks for option pricing: Rationality by design. In *Proceedings of the AAAI Conference on Artificial Intelligence*, *31*(1). https://doi.org/10.1609/aaai.v31i1.10505
- Yao, Y., Cui, Z., & Pan, Q. (2026). Joint arbitrage-free smoothing of American call and put options surfaces. *European Journal of Operational Research*, *336*(1), 388–404. https://doi.org/10.1016/j.ejor.2026.07.049
- Zaugg, N. F., Perotti, L., & Grzelak, L. A. (2025). Volatility parametrizations with random coefficients: Analytic flexibility for implied volatility surfaces. *SIAM Journal on Financial Mathematics*, *16*(4), 1374–1411. https://doi.org/10.1137/24m1713107
- Zetocha, V. (2023). Volatility transformers: An optimal transport-inspired approach to arbitrage-free shaping of implied volatility surfaces [Preprint]. *SSRN Electronic Journal*. https://doi.org/10.2139/ssrn.4623940

## Appendix A. Search Queries and Retrieval Flow

Thirty-one OpenAlex free-text queries were submitted on 2026-11-23, each returning 25 relevance-ranked records (775 raw records before de-duplication). One string returned nothing after a transient HTTP 429 and was not successfully re-run.

| Group | Queries | Records requested |
|---|---|---|
| Broad surface / arbitrage | Arbitrage-free implied volatility surface; implied volatility surface arbitrage | 50 |
| Parametric (SVI, SSVI, SABR, shape constraints) | SVI stochastic volatility inspired (failed, rate-limited); SSVI implied volatility surface; shape constrained implied volatility surface; nonparametric implied volatility surface; arbitrage-free smoothing implied volatility surface; SABR arbitrage-free volatility | 150 |
| Penalty | Penalty no-arbitrage implied volatility; arbitrage penalty optimization implied volatility | 50 |
| Projection and repair | Projection arbitrage-free option prices; repair arbitrage option price surface; convexification option prices arbitrage | 75 |
| Generation and filtering | Generative model implied volatility surface; variational autoencoder implied volatility surface; generative adversarial network implied volatility surface; diffusion model implied volatility surface; simulation arbitrage-free implied volatility surface; neural SDE volatility surface | 150 |
| Neural | Neural network implied volatility surface; deep learning implied volatility surface; neural network option pricing arbitrage-free; hard constraint neural network no arbitrage; Gaussian process implied volatility surface; rough volatility calibration neural network | 150 |
| Dynamic | Dynamic arbitrage implied volatility; calendar arbitrage implied volatility; butterfly arbitrage implied volatility | 75 |
| Evaluation | Implied volatility surface survey; implied volatility surface interpolation no arbitrage; static arbitrage option prices | 75 |

*Note.* Retrieval flow: 775 records requested, 430 unique after de-duplication, 389 excluded at title screening, 41 included. Abstract recovery used OpenAlex, Crossref and Semantic Scholar; DOI resolution used OpenAlex for all 41 records and Crossref for four.

## Appendix B. Screening Summary

| Reason code | Records |
|---|---|
| OFF_TOPIC | 141 |
| PRE_2015_BACKGROUND | 86 |
| RELEVANT_NOT_SELECTED | 40 |
| OUT_OF_SCOPE_ASSET | 34 |
| PUBLICATION_TYPE | 32 |
| DUPLICATE_VERSION | 31 |
| FORECASTING_OR_TRADING | 21 |
| MODEL_CALIBRATION_PRICING | 4 |
| **Included** | **41** |

*Note.* Two included records were replaced during abstract reading when the retrieved text showed no enforcement claim (a neural-network implied-volatility computation paper and a foreign-exchange delta-condition paper). Screening was performed by one reviewer without dual screening, adjudication or kappa.

## Appendix C. Evidence-Status Ledger

| ID | Source | Family | Evidence status | Abstract | Level | Peer review |
|---|---|---|---|---|---|---|
| P1 | Guo et al. (2016) | Parametric | Proof | Full | VI | Yes |
| P2 | Martini & Mingone (2022) | Parametric | Proof | Full | VI | Yes |
| P3 | Mingone (2022) | Parametric | Proof | Full | VI | Yes |
| P4 | Corbetta et al. (2019) | Parametric | Assumption | Metadata only | VI | Yes |
| P5 | Zaugg et al. (2025) | Parametric | Proof | Full | VI | Yes |
| P6 | Le Floc'h (2025) | Parametric | Proof | Full | VI | Yes |
| P7 | Klassen (2016) | Parametric | Assumption | Metadata only | VI | Preprint |
| P8 | Barski & Wiśniewolski (2026) | Parametric | Proof | Full | VI | Preprint |
| N1 | Cao et al. (2020) | Penalty | Numerical test | Full | VI | Yes |
| N2 | Wiedemann et al. (2025) | Penalty | Numerical test | Full | VI | Yes |
| N3 | Ackerer et al. (2019) | Penalty | Numerical test | Full | VI | Preprint |
| N4 | Sidogi et al. (2022) | Penalty | Numerical test | Full | VI | Yes |
| N5 | Na et al. (2023) | Penalty | Numerical test | Full | VI | Preprint |
| N6 | Hoshisashi et al. (2023) | Penalty | Numerical test | Full | VI | Preprint |
| R1 | Cohen et al. (2020) | Repair | Numerical test | Full | VI | Yes |
| R2 | De March & Henry-Labordère (2019) | Repair | Proof | Partial | VI | Preprint |
| R3 | Bender & Thiel (2020) | Repair | Proof | Full | VI | Yes |
| R4 | Yao et al. (2026) | Repair | Assumption | Metadata only | VI | Yes |
| R5 | Xiong & Liu (2026) | Repair | Numerical test | Full | VI | Yes |
| R6 | Buehler et al. (2026) | Repair | Proof | Full | VI | Preprint |
| R7 | Alvarez (2025) | Repair | Numerical test | Full | VI | Preprint |
| R8 | Zetocha (2023) | Repair | Assumption | Full | VI | Preprint |
| R9 | Madan & Schoutens (2019) | Repair | Numerical test | Full | VI | Yes |
| G1 | Ning et al. (2023) | Generation | Proof | Full | VI | Yes |
| G2 | Vuletić & Cont (2024) | Generation | Numerical test | Full | VI | Yes |
| G3 | Cont & Vuletić (2023) | Generation | Assumption | Partial | VI | Yes |
| G4 | Ginart Belmonte & Cole (2025) | Generation | Numerical test | Full | VI | Yes |
| G5 | Bajalica et al. (2026) | Generation | Numerical test | Full | VI | Yes |
| G6 | Anagha (2026) | Generation | Proof | Full | VI | Preprint |
| G7 | Cohen et al. (2021) | Generation | Proof | Full | VI | Yes |
| G8 | Yang et al. (2017) | Generation | Proof | Full | VI | Yes |
| C1 | Neufeld & Sester (2024) | Conditions | Proof | Full | VI | Yes |
| C2 | Niu (2015) | Conditions | Assumption | Partial | VII | Preprint |
| C3 | Andrès et al. (2026) | Conditions | Proof | Full | VI | Yes |
| C4 | Fukasawa (2022) | Conditions | Proof | Partial | VI | Yes |
| C5 | Stahl & Blauth (2024) | Conditions | Numerical test | Full | VI | Yes |
| S1 | Gatheral & Jacquier (2013) | Baseline | Proof | Partial | VI | Yes |
| S2 | Fengler (2009) | Baseline | Numerical test | Full | VI | Yes |
| S3 | Hagan et al. (2014) | Baseline | Numerical test | Full | VI | Practitioner |
| S4 | Bodurtha & Jermakyan (1999) | Baseline | Assumption | Full | VI | Yes |
| S5 | Fengler et al. (2006) | Baseline | Assumption | Full | VI | Yes |

*Note.* Level refers to the evidence-level scale (I–VII); the corpus contains 40 level VI studies and one level VII review (C2). "Abstract" records the available read: full, partial or metadata only. Peer review marks 29 peer-reviewed records, 11 preprints and one editorially reviewed practitioner magazine.

---

**Document metadata.** Body word count: 5,247 words (excluding references and appendices; citation-emission markers excluded). Structure: Abstract, six numbered sections, AI Disclosure, References, and Appendices A–C. Corpus: 41 sources; 17 proof / 16 numerical test / 8 assumption; 0 of 41 dynamic; 0 directly comparable of 41. Generated 2026-11-23.
