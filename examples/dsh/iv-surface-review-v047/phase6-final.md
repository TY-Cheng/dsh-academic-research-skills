# Enforcing No-Arbitrage in Equity-Index Implied Volatility Surfaces: A Structured Review of Four Method Families, 2015–2026, with Seminal Precursors

**Author:** TY-Cheng
**Affiliation:** Independent researcher
**Date:** 2026-11-23
**Report type:** `deep-research` full report — Stage 1, Phase 6 revised report (ARS v3.24.4 end-to-end validation run)
**Body word count:** 5,596 words (excluding references and appendices; section headings and citation-emission markers excluded)
**Corpus:** 41 sources (29 peer-reviewed, 11 preprints, 1 practitioner magazine): 36 within the 2015–2026 window, plus 5 seminal pre-2015 baselines (1999–2014) included deliberately as declared precursors and not counted as window hits; equity-index options
**Evidence status:** 17 proof-level claims / 16 numerical tests / 8 assumptions across the 41-row ledger; the 2015–2026 subset splits 16 / 14 / 6
**Read scope:** 34 full abstracts, 4 partial abstracts, 3 metadata-only records read at title level
**Competing interests and funding:** None declared. AI-assisted analysis is disclosed below; no external funding was received.
**Last search:** 2026-11-23

---

## Abstract

Equity-index option markets quote hundreds of strikes and maturities daily; the implied volatility surface risk systems consume is admissible only if it excludes arbitrage on a single date and across dates. This report synthesises 41 studies on how four families of construction methods enforce those constraints: parametric construction, penalty-augmented objectives, projection-repair, and generation-filtering. Thirty-six studies fall inside the 2015–2026 window; five seminal pre-2015 baselines are included deliberately as declared precursors. Search, verification and grading followed the `deep-research` full-mode protocol; no PRISMA compliance is claimed. Coding of an evidence matrix (Table 4; Appendix C) shows that 17 sources assert their guarantee at proof level, 16 report a numerical test, and 8 assert admissibility without either. As reported in the abstracts, the certified object in all 41 rows is a single date's surface; ten rows engage time at all, and none enforces or tests dynamic no-arbitrage, leaving the count at 0 of 36 in-window rows (0 of 31 construction rows). Proof-level and test-level evidence come from almost disjoint source sets, and no two studies state data, metric and tolerance together, so no pair is directly comparable from the abstracts. This corpus answers the static question and leaves the dynamic one open; the appropriate output is a research agenda, not a ranking of methods.

**Keywords:** implied volatility surface; no-arbitrage; static arbitrage; dynamic consistency; model validation; equity-index options

## 1. Introduction

### 1.1 Context

An equity-index option market quotes several hundred strike–maturity pairs on a typical trading day. Firms consume not quotes but a fitted implied volatility surface, from which prices, Greeks and risk-neutral densities are derived (Fengler, 2009)<!--ref:S2--><!--anchor:section:1.1-->. That surface is economically coherent only if it embeds no arbitrage. On a single date, call prices must be non-increasing and convex in strike, total variance must not decrease with maturity, and the zero-maturity limit must match intrinsic value (Gatheral & Jacquier, 2013<!--ref:S1--><!--anchor:section:1.1-->; Guo et al., 2016)<!--ref:P1--><!--anchor:section:1.1-->. Across dates, no self-financing strategy in the option panel may produce a riskless profit (Niu, 2015 [preprint])<!--ref:C2--><!--anchor:section:1.1-->. Construction is therefore constrained estimation rather than interpolation, run at scale on dense, noisy quotes (Wiedemann et al., 2025)<!--ref:N2--><!--anchor:section:1.1-->. Because the surface is what prices, hedges and clears, a fitted artefact that admits arbitrage can in principle propagate into risk numbers, margin and capital; that propagation is a premise, not a measurement: no study in this corpus tests it.

### 1.2 Problem Statement

The phrase "arbitrage-free" does not denote one property. A method may be arbitrage-free because its parameter domain excludes violations (Guo et al., 2016)<!--ref:P1--><!--anchor:section:1.2-->, because a penalty discourages them (Na et al., 2023 [preprint])<!--ref:N5--><!--anchor:section:1.2-->, because a post-fit map removes them (Bender & Thiel, 2020)<!--ref:R3--><!--anchor:section:1.2-->, or because a generator is screened before output (Bajalica et al., 2026)<!--ref:G5--><!--anchor:section:1.2-->. These are different guarantees with different failure modes. The literature rarely separates them, and uses the same phrase for the static condition and for the dynamic one, although the second concerns the joint law of a surface process rather than the admissibility of one surface (Niu, 2015)<!--ref:C2--><!--anchor:section:1.2-->. The risk is claim inflation: a tested method read as proved, a static guarantee as dynamic. Throughout this report, an *audit* means a reported finite-sample violation test run on the construction's own output, and *dynamic* is reserved for process-level consistency across dates (Section 2.1); the *certified object* is the surface whose admissibility a row claims. Three questions therefore follow for any claim: which condition, at what tolerance, and verified how. They structure the analysis; condition and tolerance are annotations where an abstract supplies them, while the ledger codes locus and verification mode.

### 1.3 Purpose and Research Question

This report characterises—not ranks—how the four families carry their constraints, and identifies what evidence exists for each. The guiding question is:

> How do parametric construction, penalty, projection-repair, and generation-filtering methods for constructing equity-index implied volatility surfaces enforce static and dynamic no-arbitrage constraints?

Three hypotheses structured the synthesis: that static admissibility is mostly obtained by construction while dynamic consistency is asserted or tested rather than proved; that penalty and repair methods reduce fit error but displace the burden onto tolerances, weights and repair steps that are rarely validated out of sample; and that for generation-filtering methods "arbitrage-free" usually means "not rejected on this sample". Their adjudication is summarised in Table 1 and reported with the evidence in Section 4. 

**Table 1**

*Hypothesis status at the close of synthesis*

| Hypothesis | Clause | Status | Basis |
|---|---|---|---|
| H1 | Static admissibility is mostly obtained by construction | Supported | 41 of 41 rows; 6 of 8 parametric rows are proof-level |
| H1 | Dynamic consistency is asserted or tested rather than proved | Disconfirmed as stated | No row asserts a dynamic condition and tests it; it is absent, not asserted-and-tested (0 of 36 in-window) |
| H2 | Penalty and repair reduce fit error | Unsupported | No family reports lower fit error than a constrained parametric baseline; the one measurement runs the other way (Anagha, 2026 [preprint]) |
| H2 | They displace the burden onto tolerances, weights and repair steps that are rarely validated | Supported | Residual reports omit tolerances; weights and repair parameters are rarely audited out of sample |
| H3 | For generation-filtering, "arbitrage-free" means "not rejected on this sample" | Supported for the penalised-sampling branch; disconfirmed for the inherited-guarantee branch | One row reports a pass rate on tested conditions; the other rows are model-class statements, not acceptance tests |

*Note.* Statuses are the Phase 3 adjudications; clauses are those in the preceding paragraph.

### 1.4 Significance

The result matters for model validation, benchmark design and the field's vocabulary. A validation team that reads "arbitrage-free" as a uniform property will over-credit methods whose guarantee holds only up to tolerance; a benchmark that compares violation rates without matching data, grid and tolerance will produce an ordering the evidence cannot support. The contribution is a diagnostic of what the corpus does and does not establish, not a recommendation among methods. If the corpus cannot compare families, the correct response is to design comparability rather than aggregate incomparable numbers.

### 1.5 Structure of the Report

Section 2 fixes the admissibility object and the taxonomy; Section 3 records search, screening and grading; Section 4 reports the evidence matrix, themes and tensions; Section 5 interprets the pattern and states its limits; Section 6 converts the gaps into an agenda. Appendices A–C reproduce the queries, screening counts and the 41-row ledger, so every number in the body traces to an artefact.

## 2. Literature Review and Theoretical Framework

### 2.1 The Static Admissibility Object

Following the corpus, write total implied variance as $w(k,\tau)=\sigma^2\tau$, where $k=\log(K/F_\tau)$ and $F_\tau$ is the forward. A surface is statically admissible if, expressed through the normalised call price $c(k,\tau)=C/F_\tau$, it satisfies: (C1) $c-\max(1-e^{k},0)\ge 0$; (C2) $\partial c/\partial k\le 0$; (C3) $\partial^2 c/\partial k^2\ge 0$, the butterfly or Durrleman condition; (C4) the zero-maturity limit $c(\cdot,0)=\max(1-e^{k},0)$; and (C5) $w$ is non-decreasing in $\tau$ (Gatheral & Jacquier, 2013<!--ref:S1--><!--anchor:section:2.1-->; Martini & Mingone, 2022<!--ref:P2--><!--anchor:section:2.1-->; Anagha, 2026 [preprint])<!--ref:G6--><!--anchor:section:2.1-->. Dynamic no-arbitrage concerns a filtered family of statically admissible surfaces whose joint law admits a martingale representation consistent with the numéraire (Niu, 2015 [preprint])<!--ref:C2--><!--anchor:section:2.1-->. Conditions (C1)–(C4) encode a non-negative risk-neutral density in price space; (C5) makes the object a surface rather than a family of slices. No source in the corpus states a testable version of the dynamic condition. The nearest construction is a neural SDE calibrated to satisfy a set of linear inequalities, which guarantees static and model-independent arbitrage only; because its abstract states no dynamic claim, this review codes it as making none (Cohen et al., 2021)<!--ref:G7--><!--anchor:section:2.1-->.

### 2.2 Four Families, Four Loci of Enforcement

The corpus supports a taxonomy organised by *where* the constraint acts rather than by model class (Table 2). Parametric methods restrict the parameter domain; penalty methods add violation terms to the fitting objective; projection-repair methods modify the fitted output; generation-filtering methods restrict the support of a sampler or screen its output. Boundary cases are disclosed rather than forced: the strict finite-grid construction of Buehler et al. (2026 [preprint])<!--ref:R6--><!--anchor:section:2.2-->, the distortion-based interpolation of Bender and Thiel (2020)<!--ref:R3--><!--anchor:section:2.2-->, and the gated architecture of Cao et al. (2020)<!--ref:N1--><!--anchor:section:2.2--> each sit under two loci. Each locus yields a different kind of evidence—theorem, residual, repaired point, accepted sample—which is why the four are compared by evidential kind rather than by a shared metric.

**Table 2**

*Four families of implied-volatility-surface construction, by enforcement locus*

| Family | Enforcement locus | Mechanism | What it establishes | Typical failure mode |
|---|---|---|---|---|
| Parametric construction | Parameter domain | Restrictions make slices convex and total variance monotone | Static admissibility by construction | Tight wings, fit loss, dynamic behaviour unaddressed |
| Penalty | Objective | Violation terms added to the fit loss with weights | Approximate compliance conditional on weight and tolerance | Residual violations, weight sensitivity, no guarantee |
| Projection-repair | Post-fit output | Surface projected onto the admissible set | Static conditions at the repaired point | Repair distorts fit and drifts; no cross-date enforcement |
| Generation-filtering | Sampler and acceptance test | Candidates generated, accepted or rejected by arbitrage tests | Compliance on the accepted finite sample | A passed test is not a proof; rejection cost; power unknown |

*Note.* Adaptation of the frozen taxonomy fixed in Phase 1; families are not asserted to be exhaustive, and three studies sit between two loci (Buehler et al., 2026; Bender & Thiel, 2020; Cao et al., 2020); each is assigned one family in Appendix C.

### 2.3 The Eight-Dimension Evaluation Matrix

Eight evaluation dimensions were declared before synthesis (Table 3). They are axes, not score columns: no weighting is implied, and coverage counts rows supplying the relevant kind of evidence. Read down, it shows where the corpus supplies almost nothing.

**Table 3**

*Declared evaluation dimensions and corpus coverage*

| Dimension | Rows contributing evidence | Status |
|---|---|---|
| Static no-arbitrage | 41 of 41 | Coded on every row (17 proof, 16 test, 8 assertion); tolerances rarely stated |
| Dynamic consistency | 10 | Ten rows engage time (named in §4.5); none enforces or tests |
| Fit accuracy | ~8 | Numbers reported on disjoint datasets; not comparable |
| Interpolation and stability | ~8 | Thin; no audit at the boundary where guarantees bind |
| Extrapolation and wings | ~6 | Wing behaviour asserted, not measured |
| Computational cost | ~5 | Claims only; no common-hardware measurements |
| Interpretability | 0 | No row assesses interpretability |
| Reproducibility | ~4 | Code and data availability rarely stated |

*Note.* Counts are from the Phase 3 evidence matrix; "~" marks counts that depend on how a reported artefact is classified.

### 2.4 The Condition Lineage and Scale-Relativity

The condition literature is a monotone refinement rather than a set of competing theories. Early nonparametric specifications carried no explicit constraint (Bodurtha & Jermakyan, 1999)<!--ref:S4--><!--anchor:section:2.4-->, so the refinement begins from a baseline that stated no admissibility condition. Gatheral and Jacquier (2013)<!--ref:S1--><!--anchor:section:2.4--> give sufficient closed-form conditions for SVI surfaces; Martini and Mingone (2022)<!--ref:P2--><!--anchor:section:2.4--> turn the butterfly requirement into an exact characterisation via the monotonicity of $-d_1$ and $-d_2$ and Durrleman's condition; Mingone (2022)<!--ref:P3--><!--anchor:section:2.4--> lifts the construction to a global all-maturity eSSVI parameterisation. Necessity claims enter more weakly: the only closed-form necessary-and-sufficient statement for the SSVI/S3 curve found in this corpus is a metadata-only preprint (Klassen, 2016 [preprint])<!--ref:P7--><!--anchor:section:2.4-->, the exact characterisation of Martini and Mingone (2022) is a statement about the SVI family, not a necessity claim for the wider class. Admissibility is also scale-relative: Fukasawa (2022)<!--ref:C4--><!--anchor:section:2.4--> proves asymptotic arbitrage-freeness of BBF, SABR and rough SABR formulas, while Hagan et al. (2014)<!--ref:S3--><!--anchor:section:2.4--> show that the explicit SABR formulas are arbitrageable in the low-strike wings at finite strikes. Two recent constructions widen rather than narrow the admissible set (Zaugg et al., 2025)<!--ref:P5--><!--anchor:section:2.4--> and interpolate raw quotes by construction (Le Floc'h, 2025)<!--ref:P6--><!--anchor:section:2.4-->, while Buehler et al. (2026)<!--ref:R6--><!--anchor:section:2.4--> sharpen the condition to a strict finite-grid form. The refinement runs toward finite-grid conditions—what an audit needs. "Arbitrage-free" is therefore always relative to a domain, a scale and a tolerance.

## 3. Methodology

### 3.1 Search Strategy and Scope

Discovery used the OpenAlex REST API, anonymously and without a key. Thirty-one free-text query strings were submitted on 2026-11-23 in eight groups (Appendix A), each requesting 25 relevance-ranked records. Queries decomposed the conceptual string formally. The first pass hit HTTP 429 rate limits on 21 of the 31 queries. A re-run submitted the failures again, recovered 20 of them, and left one—"SVI stochastic volatility inspired"—unusable after retry, so 30 queries returned 750 records of the 775 requested. One snowballing pass over the included records' references and citing works added no record that survived screening, and all 41 included rows have at least one direct query hit, so the flow is reported as query-driven with a null snowballing yield. Inclusion required an implied-volatility or option-price surface construction with an enforcement claim, equity-index applicability, English, OpenAlex resolvability, and one record per study. The corpus window is 2015-01-01 to 2026-11-23, with five pre-2015 precursors (1999–2014) included as declared background and never counted as window hits. Equity indices are the setting because their option panels are the deepest; single-name equities, foreign exchange, rates and crypto underlyings were excluded from scope-focused selection, with one disclosed exception: a row retained for its constraint-diagnostic contribution works on a single-stock panel and carries a scope flag wherever it is used (Section 4.5, Appendix C). These choices bound the generality of the findings.

### 3.2 Screening

De-duplication of the 750 returned records removed 320, leaving 430 unique records. Title screening excluded 389 records under eight pre-specified reason codes (Appendix B), leaving 41 studies whose abstracts were then read (Appendix B). The flow closes arithmetically: 430 − 389 = 41. Two included records were replaced during abstract reading when the retrieved text showed no enforcement claim: a neural-network implied-volatility pricing paper was replaced by Wiedemann et al. (2025), and a foreign-exchange delta-condition paper by Fukasawa (2022). Screening was single-reviewer; no dual screening or kappa is claimed. Exclusions were applied at title level for the whole pool and confirmed at abstract level only for included records; the 40 "relevant but not selected" records are the largest discretionary decision in the flow and are reported separately from the rule-based codes.

### 3.3 Verification

Each record was resolved through OpenAlex's DOI endpoint; all 41 lookups returned HTTP 200 and none is flagged retracted. Abstracts were reconstructed from the OpenAlex inverted index and, where necessary, Crossref and Semantic Scholar, producing 34 full abstracts, four partial abstracts—De March and Henry-Labordère (2019), Cont and Vuletić (2023), Fukasawa (2022) and Gatheral and Jacquier (2013)—and three metadata-only records (Corbetta et al., 2019; Klassen, 2016; Yao et al., 2026). The split reconciles to 41 and is the single source for every read-scope count in this report. Status is marked at the point of use: [preprint] denotes a manuscript with no peer-reviewed version of record in this corpus, and [title/metadata only] denotes a record read at title level. Five cross-source claim clusters covered 19 of the 41 sources; no claim is independently replicated within the corpus. Verification returned a conditional pass: metadata-only rows are cited at title level only, preprint status is flagged at point of use, no tested method is called arbitrage-free, cross-study numbers are not compared, and dynamic claims are reported as unverified. The clusters agree on the requirement, not on any measurement: penalty magnitudes are not comparable and repair floors depend on the grid.

### 3.4 Evidence Grading and Comparability Coding

Two grading axes were applied. Evidence level runs from level I (systematic review) to level VII (narrative review); the corpus contains 40 level VI studies and one level VII review (C2). A six-criterion rubric produced grades of A (11), B (13) and C (17), with integrity floors: a numerical test cannot receive A; a partial abstract cannot exceed B; and a claim-only, abstract-unavailable, preprint, practitioner or metadata-only row cannot exceed C. The partial floor binds two rows (C4 and S1, both graded B); the preprint cap explains the C grades of P7, P8, N3, N5, N6, R2, R6, R7, R8, G6 and C2, and C2 (Niu, 2015) is additionally the one level-VII narrative review, so the A/B/C distribution (11/13/17) follows from the rules. Each row also received an evidence-status label (proof, numerical test, assumption) and a comparability code. Comparability is deliberately conservative: judged from the abstracts, 0 rows can be shown directly comparable, 30 report numbers usable only for context, and 11 report none. No ranking, vote count or citation metric is used anywhere in this report. The floors cap what a source can claim whatever its abstract's confidence.

### 3.5 Analytical Framework and Boundedness

Synthesis coded each row as a triple of model class, enforcement operator and verification mode, using static and dynamic definitions fixed before coding (Section 2.1); a per-date maturity-monotonicity condition was not coded as dynamic. Condition identity and stated tolerance were annotated where an abstract supplied them rather than coded as ledger fields, because most abstracts state neither. Every statement about a method's evidence is bounded by what the abstract reports: absence of a reported audit is not evidence that none was performed. The design is a constraint-centred narrative synthesis with no meta-analysis or re-estimation, and claims no PRISMA compliance. Coding judgements were made by one analyst. Every count in Section 4 is a count of what abstracts report, hence the verb "reports".

## 4. Findings

### 4.1 Evidence-Status Distribution

Across the 41 rows the reported evidence splits 17 proof, 16 numerical test and 8 assumption (Table 4); within the 36 in-window rows it is 16/14/6, with the five seminal baselines contributing 1/2/2. The split follows the taxonomy (Table 4). The eight assumption rows include all three metadata-only records and two pre-constraint baselines, so the weakest evidence labels and the weakest retrieval coincide. The signal is structural: proof concentrates in parametric construction, tests in penalty methods, and assumption rows where inspection is least possible.

**Table 4**

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

The four subsections follow the taxonomy; each reports what a family's rows establish and what they leave unmeasured. Eleven rows are preprints, tagged at first use; claims drawn from them are provisional.

**Parametric construction.** Six of the eight parametric rows are proof-level, and the guarantee is typically structural: the parameter map is chosen so the admissible set is the image of the parameter domain (Guo et al., 2016<!--ref:P1--><!--anchor:section:4.2-->; Martini & Mingone, 2022)<!--ref:P2--><!--anchor:section:4.2-->. Martini and Mingone (2022) obtain a full butterfly characterisation with least-squares calibration restricted to the admissible domain; Mingone (2022)<!--ref:P3--><!--anchor:section:4.2--> builds a global all-maturity eSSVI parameterisation; Barski and Wiśniewolski (2026 [preprint])<!--ref:P8--><!--anchor:section:4.2--> derive explicit arbitrage probabilities for Gaussian factor models rather than a parameter-domain guarantee. The two metadata-only rows (Corbetta et al., 2019<!--ref:P4--><!--anchor:section:4.2-->; Klassen, 2016)<!--ref:P7--><!--anchor:section:4.2--> show only that a constrained calibration and a necessary-and-sufficient condition are claimed in their titles [Title/metadata only]. No parametric row reports a finite-sample violation audit or tests behaviour across dates.

**Penalty and constrained learning.** All six rows are numerical tests and none reports a violation-rate distribution. Cao et al. (2020)<!--ref:N1--><!--anchor:section:4.2--> gate hidden layers so slopes and weights satisfy the constraints and report forecasting and hedging gains on S&P 500 data; Wiedemann et al. (2025)<!--ref:N2--><!--anchor:section:4.2--> train a graph neural operator on ten years of intraday S&P 500 quotes and report adherence to critical constraints; Ackerer et al. (2019 [preprint])<!--ref:N3--><!--anchor:section:4.2--> use soft penalties with a plug-in correction and report gains on sparse or erroneous quotes. The remaining rows are candid: Sidogi et al. (2022)<!--ref:N4--><!--anchor:section:4.2--> find that a static-arbitrage loss improves distributional fit while the framework "cannot directly learn the static arbitrage condition"; Na et al. (2023 [preprint])<!--ref:N5--><!--anchor:section:4.2--> state in their title that violations are only minimised; Hoshisashi et al. (2023 [preprint])<!--ref:N6--><!--anchor:section:4.2--> penalise derivatives on SABR-generated prices. The two rows that report adherence (Cao et al., 2020; Wiedemann et al., 2025) state no tolerance, so their audits are hard to reproduce.

**Projection and repair.** Repair rows differ in what they owe: a distortion bound, an optimality property, or both. Cohen et al. (2020)<!--ref:R1--><!--anchor:section:4.2--> solve a linear program that changes prices minimally inside bid–ask bounds; De March and Henry-Labordère (2019 [preprint])<!--ref:R2--><!--anchor:section:4.2--> prove Sinkhorn projection convergence; Bender and Thiel (2020)<!--ref:R3--><!--anchor:section:4.2--> interpolate through an arbitrage-free reference function. Zetocha (2023 [preprint])<!--ref:R8--><!--anchor:section:4.2--> asserts transformations for extrapolation and dynamics without stating a proof or a test. Three rows report what repair leaves behind: Xiong and Liu (2026)<!--ref:R5--><!--anchor:section:4.2--> repair calendar violations to approximately zero and leave a butterfly floor of about 5.4 percent on the reported scale—252 out-of-sample SPX days—which the source attributes to finite-precision rounding rather than a modelling defect; Alvarez (2025 [preprint])<!--ref:R7--><!--anchor:section:4.2--> reports below one percent static violations with 98–99 percent inside-spread coverage in calm years; Madan and Schoutens (2019)<!--ref:R9--><!--anchor:section:4.2--> approximate 2,695 SPY options across 28 maturities. The metadata-only American-option row (Yao et al., 2026)<!--ref:R4--><!--anchor:section:4.2--> is title-level only [Title/metadata only]. The strictest proof-level member is explicit about the finite grid (Buehler et al., 2026 [preprint])<!--ref:R6--><!--anchor:section:4.2-->, though its market illustration is not quantified.

**Generation and filtering.** The family splits in two. The learned-parametric branch inherits its guarantee from the decoder or architecture: a VAE over SDE parameters (Ning et al., 2023)<!--ref:G1--><!--anchor:section:4.2-->, a constrained state space in a neural SDE (Cohen et al., 2021)<!--ref:G7--><!--anchor:section:4.2-->, gated networks (Yang et al., 2017)<!--ref:G8--><!--anchor:section:4.2-->. A denoiser maps noisy, arbitrage-violating surfaces to smooth ones and reports lower error and runtime than traditional smoothing (Ginart Belmonte & Cole, 2025)<!--ref:G4--><!--anchor:section:4.2-->. The penalised-sampling branch reports residuals: Bajalica et al. (2026)<!--ref:G5--><!--anchor:section:4.2--> report that 90.8 percent of generated surfaces pass all tested conditions, while Anagha (2026 [preprint])<!--ref:G6--><!--anchor:section:4.2--> reports zero violations at a tolerance of $10^{-4}$ across 15 runs on synthetic SVI slices, using input-convex blocks gated by maturity ramps—structural, not penalised—and higher total-variance RMSE than SSVI and a soft-penalty multilayer perceptron. Only the penalised-sampling branch audits arbitrage compliance, and only Anagha states a tolerance and reports the fit cost. The realism-driven models learn co-movement and hedging without stating an enforcement mechanism (Vuletić & Cont, 2024)<!--ref:G2--><!--anchor:section:4.2-->—the characteristic weakness of a family judged by plausibility.

### 4.3 Cross-Cutting Themes

Five themes survive the coding.

**Static scope of the certification.** Across the 41 rows, as reported in the abstracts, "arbitrage-free" is a predicate on a single surface. The dynamic condition is named in ten rows (Section 4.5), with Niu (2015 [preprint])<!--ref:C2--><!--anchor:section:4.3--> setting it out most fully, and enforced in none.

**Four loci, four meanings.** A parameter-domain statement, an optimisation residual, a repaired point and an accepted sample are not interchangeable evidence.

**Disjoint evidential channels.** Of the 17 proof-level rows only Anagha (2026 [preprint])<!--ref:G6--><!--anchor:section:4.3--> both guarantees and audits, and the audit is synthetic; of the six rows reporting residuals, none states a theorem and two state that violations are only minimised (Na et al., 2023<!--ref:N5--><!--anchor:section:4.3-->; Sidogi et al., 2022)<!--ref:N4--><!--anchor:section:4.3-->. An independent detector exists (Neufeld & Sester, 2024)<!--ref:C1--><!--anchor:section:4.3-->, but was never applied to another row's output.

**The measured cost of the guarantee.** Where measured, the trade-off points one way: a tighter constraint buys fewer violations at a higher fit error. The direction is observed once, on synthetic data (Anagha, 2026 [preprint])<!--ref:G6--><!--anchor:section:4.3-->, and is not corroborated elsewhere in the corpus: the repair floors of Xiong and Liu (2026)<!--ref:R5--><!--anchor:section:4.3--> and Alvarez (2025 [preprint])<!--ref:R7--><!--anchor:section:4.3--> measure residual violations left by projection, not the cost of tightening a constraint, and their magnitudes are not comparable with a fit-error change.

**Fragmented evaluation vocabulary.** At least seven metric families appear—violation rate, implied-volatility and total-variance RMSE, Wasserstein distance, hedging profit and loss, inside-spread coverage, detection performance and runtime.

### 4.4 Tensions

Five tensions are load-bearing.

**Static proof versus dynamic behaviour.** No row proves a process-level statement, and the one neural-SDE model makes no dynamic claim (Cohen et al., 2021)<!--ref:G7--><!--anchor:section:4.4-->. Reconcilable only by proving a property of the process, which no row does.

**Interpolation quality versus guarantees.** Irreconcilable on current evidence: no row measures interpolation error at the boundary where its own guarantee binds.

**Quote noise versus test rejection.** A zero violation rate on synthetic data (Anagha, 2026)<!--ref:G6--><!--anchor:section:4.4-->, approximately zero calendar violations on SPX (Xiong & Liu, 2026)<!--ref:R5--><!--anchor:section:4.4--> and a 90.8 percent pass rate (Bajalica et al., 2026)<!--ref:G5--><!--anchor:section:4.4--> cannot be separated without a noise floor, and no row estimates one or reports test power.

**Expressiveness versus constraint strength.** Enlarging the admissible set is demonstrated in two constructions (Zaugg et al., 2025<!--ref:P5--><!--anchor:section:4.4-->; Alvarez, 2025)<!--ref:R7--><!--anchor:section:4.4-->, but the cost of enlarging it is measured in one row only.

**Definitional conflation.** "Calendar" denotes both within-date maturity monotonicity and cross-date consistency; the conflation inflates apparent dynamic coverage and is the most consequential definitional problem in the corpus.

### 4.5 The Dynamic No-Arbitrage Void

Ten rows engage time at all, the basis for any claim of dynamic coverage: an arbitrage-probability model for Gaussian factors (Barski & Wiśniewolski, 2026 [preprint])<!--ref:P8--><!--anchor:section:4.5-->, a Markov-chain repair with a full maturity axis (Madan & Schoutens, 2019)<!--ref:R9--><!--anchor:section:4.5-->, three generative models of surface dynamics (Ning et al., 2023<!--ref:G1--><!--anchor:section:4.5-->; Vuletić & Cont, 2024<!--ref:G2--><!--anchor:section:4.5-->; Cont & Vuletić, 2023)<!--ref:G3--><!--anchor:section:4.5-->, a constrained state space inside a neural SDE (Cohen et al., 2021)<!--ref:G7--><!--anchor:section:4.5-->, an asserted transformation for extrapolation and dynamics (Zetocha, 2023 [preprint])<!--ref:R8--><!--anchor:section:4.5-->, a path-dependent volatility model (Andrès et al., 2026)<!--ref:C3--><!--anchor:section:4.5-->, a review of dynamic conditions (Niu, 2015 [preprint])<!--ref:C2--><!--anchor:section:4.5-->, and a martingale-defect bubble diagnostic (Stahl & Blauth, 2024)<!--ref:C5--><!--anchor:section:4.5-->. None converts its engagement into a dynamic guarantee or a dynamic test: the number is 0 of 41 rows as reported in the abstracts, 0 of the 36 in-window rows, and 0 of the 31 construction-level rows. The corpus therefore cannot answer the second half of the research question. The nearest statements are descriptive rather than conditional: surface paths that are static-arbitrage-free by construction (Andrès et al., 2026)<!--ref:C3--><!--anchor:section:4.5-->, and martingale defects used as bubble indicators (Stahl & Blauth, 2024)<!--ref:C5--><!--anchor:section:4.5-->—the one row whose panel is single-name equities rather than an index; it is retained for its constraint-diagnostic contribution and carries a scope flag at every use.

### 4.6 Comparability Caveats

No pair of rows shares data, metric and tolerance, so the comparability code is zero of 41. Violation rates are reported against synthetic SVI slices, SPX completion grids, equity panels and generated surfaces; fit errors use implied-volatility RMSE, total-variance RMSE, Wasserstein distance or reconstruction error; tolerances are frequently unstated. Comparisons are therefore limited to kinds of evidence and within-study orderings. A comparable design would fix four fields before any number is collected: the panel, the condition set with its tolerance, the metric with its aggregation rule, and the residual-reporting format. No row shows more than two of the four in its abstract. Tolerance is the most frequently missing field.

## 5. Discussion

### 5.1 Interpretation

The pattern is coherent once the two conditions are separated. Static admissibility is a finite-dimensional, checkable property, established by the four families in four ways that agree on the object even when they disagree on method. Dynamic admissibility is a statement about a stochastic process and requires a model of how the surface evolves; none of the constructions supplies one with a proof. The proof/audit asymmetry is the more interesting finding: the sources that establish results are rarely the sources that measure residual violations, so a reader who wants both must combine sources that were never designed to be combined. That asymmetry is plausibly a publication norm, but it is also why the corpus cannot adjudicate between families. A benign reading is equally consistent: abstracts may under-report audits present in full texts, so the asymmetry could be a retrieval effect. Within this read scope the two readings cannot be separated.

### 5.2 Implications

For model validation, the practical implication is that "arbitrage-free" must be resolved into three questions: which condition, at what tolerance, and verified how. A validation file recording mechanism and verification mode is more informative than one recording a label. For benchmark design, comparison requires a shared panel, a shared tolerance grid and a pre-registered metric before a head-to-head claim is credible. For the field's vocabulary, static and dynamic claims should be stated separately in titles and abstracts; the conflation is not stylistic but a source of misattribution. For reporting practice, a surface should carry its enforcement locus and verification mode as metadata. For journals, a narrower suggestion: consider requesting a machine-readable enforcement statement alongside empirical claims of arbitrage freeness, as numerical papers are expected to report solver tolerances—a suggestion motivated by the asymmetry documented here, not by evidence that such a requirement would improve practice.

### 5.3 Limitations

Eleven of the 41 sources (26.8 percent) are preprints, four of them from 2025–2026 (Alvarez, 2025; Anagha, 2026; Barski & Wiśniewolski, 2026; Buehler et al., 2026); the strictest claims cluster there. Three records are metadata-only (Corbetta et al., 2019<!--ref:P4--><!--anchor:section:5.3-->; Klassen, 2016<!--ref:P7--><!--anchor:section:5.3-->; Yao et al., 2026)<!--ref:R4--><!--anchor:section:5.3--> and are cited at title level only; four abstracts are partial (De March & Henry-Labordère, 2019 [preprint]<!--ref:R2--><!--anchor:section:5.3-->; Cont & Vuletić, 2023<!--ref:G3--><!--anchor:section:5.3-->; Fukasawa, 2022<!--ref:C4--><!--anchor:section:5.3-->; Gatheral & Jacquier, 2013<!--ref:S1--><!--anchor:section:5.3-->), while Niu (2015 [preprint])<!--ref:C2--><!--anchor:section:5.3--> supplied a full abstract that a short snippet had made look partial. The read scope was abstract-level throughout, so no theorem was checked, no residual recomputed, and absence claims are bounded by what abstracts report. Screening and coding were single-analyst, without dual screening, adjudication or inter-rater agreement; the same analyst wrote this synthesis, so construct-level judgements are single-coded. The corpus is English-only, drawn from one index (OpenAlex) and dominated by US data; provenance could be established for only a minority of rows, two of which (Fengler et al., 2006<!--ref:S5--><!--anchor:section:5.3-->; Sidogi et al., 2022)<!--ref:N4--><!--anchor:section:5.3--> are non-US. One discovery query failed on a rate limit and could not be recovered after retry, so the pool is not exhaustive. Two planned procedures were not executed and are recorded as deviations: the calibration-subset second coding (hence no inter-rater statistic) and the full-text retrieval of five load-bearing rows (G6, R5, P2, G2, G7) recommended at the Phase 3 checkpoint. Dual use is not a concern here: the methods synthesised are construction-level and the report contains no code, data or implementable procedure (Responsible Use Statement, above). One row (Stahl & Blauth, 2024)<!--ref:C5--><!--anchor:section:5.3--> uses a single-stock panel and carries a scope flag wherever used. No funding or conflict statement was retrieved for any record, and no citation counts were used. Finally, the taxonomy and the eight-dimension matrix are proposed instruments this report applies but does not validate. No negative results were retrieved: studies where a family's guarantee failed are not visible in the pool, so the prevalence of reported success may be overstated.

## 6. Conclusion and Recommendations

### 6.1 Research Agenda

The gaps translate into seven studies, offered as an agenda rather than a ranking. First, a dynamic enforcement study: fix a daily SPX panel, implement one construction per family, test the sequence for dynamic violations and report test power. Second, a pre-registered head-to-head evaluation on identical data, metrics and tolerance grid. Third, a residual audit for proof-level constructions—the cheapest gap, needing only a count of finite-precision violations at an implied tolerance (as Anagha, 2026, does on synthetic data). Fourth, measurement of test power and the noise floor, by injecting graduated arbitrage and reporting detection curves. Fifth, data-efficiency studies reporting learning curves against SVI at matched quote counts. Sixth, a cross-market study applying one method to three indices, including an emerging market. Seventh, measured rather than asserted computational cost and interpretability. The agenda is ordered by cost; the last three studies need new data.

### 6.2 Concluding Statement

On the evidence available, the four families are better understood as four kinds of claim than as four competing products. Table 4 makes the division concrete, and it does not support a clean four-way slogan. Parametric construction is 6 proof-level rows of 8 and no audit; penalty is 0 proof and 6 tests; projection and repair is 3 proof and 4 reported tests, so it does produce both proof and audit—they simply come from different rows; generation and filtering is 4 proof, 3 tests and 1 assertion, with the audit concentrated in one row. "Audit" here means a reported residual or violation check on the method's own output, not a reanalysis by this review. The counts sustain something narrower and more useful: proof-level and audit-level evidence come from almost disjoint source sets (Section 4.3), no row pairs a static theorem with a dynamic test, and the corpus answers the static question while leaving the dynamic one unposed in testable form. That is a claim about the evidence available in this read scope, not about the quality of any method.

## AI Disclosure

*AI Disclosure:* This report was produced with AI-assisted research tools operating under the ARS v3.24.4 deep-research protocol. AI performed query construction and search (31 OpenAlex queries), screening (750 returned of 775 requested, 41 included), abstraction (34 full, 4 partial, 3 metadata-only), coding and grading of the 41-row matrix, synthesis and drafting. The generative model was a Claude-family agent operating within DeepSeek Harness (DSH), on 2026-11-23; the exact model identifier and version were not recorded in the run log. Verification was abstract-level: all 41 records were resolved to an indexing record and none was flagged retracted, but no theorem was checked and no reported number was recomputed, and the three metadata-only rows are cited at title level only. Screening and coding were single-analyst, without dual screening or adjudication. Human oversight consisted of the operator's authorization of the run and review at the Phase 1–Phase 4 checkpoints recorded in the run log; no claim-level human verification of the 41 coded rows is recorded in the run artifacts. AI limitations: the pipeline could not read full texts, proofs or code, depends on third-party metadata and abstract reconstruction, and can introduce retrieval, quotation and coding errors that Section 5.3 bounds but does not eliminate.

## Competing Interests and Funding

*Competing interests:* None declared. The author is an independent researcher with no financial or personal relationship to any source, software or venue discussed. *Funding:* No funding was received for this work. The use of AI-assisted analysis is disclosed in the AI Disclosure section.

## Responsible Use Statement

*Responsible Use Statement:* The dual-use assessment returned **Level None**. Synthesising published construction and verification methods at abstract level, it adds no code, dataset, calibration recipe or implementable procedure, names no tradable strategy, and ranks no method for deployment. No content here is investment, valuation or risk-management advice.

## References

*Note on versions.* Four entries first appeared online before their printed issue was published. The year in the citation is the online year used throughout this report; the bracketed note gives the printed issue year, and each DOI resolves to the version of record. Preprint tags follow the corpus convention: they mark a manuscript with no peer-reviewed version of record in this corpus.

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
- Cohen, S. N., Reisinger, C., & Wang, S. (2021). Arbitrage-free neural-SDE market models. *Applied Mathematical Finance*, *30*(1), 1–46. https://doi.org/10.1080/1350486x.2023.2257217 [Issue published 2023.]
- Cont, R., & Vuletić, M. (2023). Simulation of arbitrage-free implied volatility surfaces. *Applied Mathematical Finance*, *30*(2), 94–121. https://doi.org/10.1080/1350486x.2023.2277960
- Corbetta, J., Cohort, P., Laachir, I., & Martini, C. (2019). Robust calibration and arbitrage-free interpolation of SSVI slices. *Decisions in Economics and Finance*, *42*(2), 665–677. https://doi.org/10.1007/s10203-019-00249-8
- De March, H., & Henry-Labordère, P. (2019). Building arbitrage-free implied volatility: Sinkhorn's algorithm and variants [Preprint]. *SSRN Electronic Journal*. https://doi.org/10.2139/ssrn.3326486
- Fengler, M. R. (2009). Arbitrage-free smoothing of the implied volatility surface. *Quantitative Finance*, *9*(4), 417–428. https://doi.org/10.1080/14697680802595585
- Fengler, M. R., Härdle, W. K., & Mammen, E. (2006). A semiparametric factor model for implied volatility surface dynamics. *Journal of Financial Econometrics*, *5*(2), 189–218. https://doi.org/10.1093/jjfinec/nbm005 [Issue published 2007.]
- Fukasawa, M. (2022). On asymptotically arbitrage-free approximations of the implied volatility. *Frontiers of Mathematical Finance*, *1*(4), 525–537. https://doi.org/10.3934/fmf.2022006
- Gatheral, J., & Jacquier, A. (2013). Arbitrage-free SVI volatility surfaces. *Quantitative Finance*, *14*(1), 59–71. https://doi.org/10.1080/14697688.2013.819986 [Issue published 2014.]
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
- Vuletić, M., & Cont, R. (2024). VolGAN: A generative model for arbitrage-free implied volatility surfaces. *Applied Mathematical Finance*, *31*(4), 203–238. https://doi.org/10.1080/1350486x.2025.2471317 [Issue published 2025.]
- Wiedemann, R., Jacquier, A., & Gonon, L. (2025). Operator deep smoothing for implied volatility. In *International Conference on Learning Representations (ICLR 2025)*. https://doi.org/10.48550/arxiv.2406.11520
- Xiong, Y., & Liu, B. (2026). Observation-anchored arbitrage repair for sparse implied volatility surface completion. In *2026 IEEE Conference on Computational Intelligence for Financial Engineering & Economics (CIFEr)* (pp. 155–162). https://doi.org/10.1109/cifer67845.2026.11692406
- Yang, Y., Zheng, Y., & Hospedales, T. M. (2017). Gated neural networks for option pricing: Rationality by design. In *Proceedings of the AAAI Conference on Artificial Intelligence*, *31*(1). https://doi.org/10.1609/aaai.v31i1.10505
- Yao, Y., Cui, Z., & Pan, Q. (2026). Joint arbitrage-free smoothing of American call and put options surfaces. *European Journal of Operational Research*, *336*(1), 388–404. https://doi.org/10.1016/j.ejor.2026.07.049
- Zaugg, N. F., Perotti, L., & Grzelak, L. A. (2025). Volatility parametrizations with random coefficients: Analytic flexibility for implied volatility surfaces. *SIAM Journal on Financial Mathematics*, *16*(4), 1374–1411. https://doi.org/10.1137/24m1713107
- Zetocha, V. (2023). Volatility transformers: An optimal transport-inspired approach to arbitrage-free shaping of implied volatility surfaces [Preprint]. *SSRN Electronic Journal*. https://doi.org/10.2139/ssrn.4623940

## Appendix A. Search Queries and Retrieval Flow

Thirty-one OpenAlex free-text queries were submitted on 2026-11-23, each requesting 25 relevance-ranked records (775 requested). The first pass hit HTTP 429 on 21 queries; a retry recovered 20, and one string ("SVI stochastic volatility inspired") remained unusable, so 750 records were returned.

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

*Note.* Retrieval flow: 775 records requested across 31 query strings, 750 returned (one query failed on a rate limit after retry), 430 unique after de-duplication, 389 excluded at title screening, 41 included. One snowballing pass added no record that survived screening, and every included record has at least one direct query hit. Abstract recovery used OpenAlex, Crossref and Semantic Scholar; DOI resolution used OpenAlex for all 41 records and Crossref for four.

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

*Note.* The flow closes arithmetically: 430 − 389 = 41 and 750 ≥ 430. Two included records were replaced during abstract reading when the retrieved text showed no enforcement claim: a neural-network implied-volatility pricing paper (Liu, Oosterlee & Bohte, 2019) was replaced by Wiedemann et al. (2025), and a foreign-exchange delta-condition paper (Wang, Zhao & Bao, 2018) by Fukasawa (2022); both displaced records remain visible in the screening log with their reason codes. Screening was performed by one reviewer without dual screening, adjudication or kappa.

## Appendix C. Evidence-Status Ledger

| ID | Source | Family | Evidence status | Abstract | Level | Time | Peer review |
|---|---|---|---|---|---|---|---|
| P1 | Guo et al. (2016) | Parametric | Proof | Full | VI | — | Yes |
| P2 | Martini & Mingone (2022) | Parametric | Proof | Full | VI | — | Yes |
| P3 | Mingone (2022) | Parametric | Proof | Full | VI | — | Yes |
| P4 | Corbetta et al. (2019) | Parametric | Assumption | Metadata only | VI | — | Yes |
| P5 | Zaugg et al. (2025) | Parametric | Proof | Full | VI | — | Yes |
| P6 | Le Floc'h (2025) | Parametric | Proof | Full | VI | — | Yes |
| P7 | Klassen (2016) | Parametric | Assumption | Metadata only | VI | — | Preprint |
| P8 | Barski & Wiśniewolski (2026) | Parametric | Proof | Full | VI | T | Preprint |
| N1 | Cao et al. (2020) | Penalty | Numerical test | Full | VI | — | Yes |
| N2 | Wiedemann et al. (2025) | Penalty | Numerical test | Full | VI | — | Yes |
| N3 | Ackerer et al. (2019) | Penalty | Numerical test | Full | VI | — | Preprint |
| N4 | Sidogi et al. (2022) | Penalty | Numerical test | Full | VI | — | Yes |
| N5 | Na et al. (2023) | Penalty | Numerical test | Full | VI | — | Preprint |
| N6 | Hoshisashi et al. (2023) | Penalty | Numerical test | Full | VI | — | Preprint |
| R1 | Cohen et al. (2020) | Repair | Numerical test | Full | VI | — | Yes |
| R2 | De March & Henry-Labordère (2019) | Repair | Proof | Partial | VI | — | Preprint |
| R3 | Bender & Thiel (2020) | Repair | Proof | Full | VI | — | Yes |
| R4 | Yao et al. (2026) | Repair | Assumption | Metadata only | VI | — | Yes |
| R5 | Xiong & Liu (2026) | Repair | Numerical test | Full | VI | — | Yes |
| R6 | Buehler et al. (2026) | Repair | Proof | Full | VI | — | Preprint |
| R7 | Alvarez (2025) | Repair | Numerical test | Full | VI | — | Preprint |
| R8 | Zetocha (2023) | Repair | Assumption | Full | VI | T | Preprint |
| R9 | Madan & Schoutens (2019) | Repair | Numerical test | Full | VI | T | Yes |
| G1 | Ning et al. (2023) | Generation | Proof | Full | VI | T | Yes |
| G2 | Vuletić & Cont (2024) | Generation | Numerical test | Full | VI | T | Yes |
| G3 | Cont & Vuletić (2023) | Generation | Assumption | Partial | VI | T | Yes |
| G4 | Ginart Belmonte & Cole (2025) | Generation | Numerical test | Full | VI | — | Yes |
| G5 | Bajalica et al. (2026) | Generation | Numerical test | Full | VI | — | Yes |
| G6 | Anagha (2026) | Generation | Proof | Full | VI | — | Preprint |
| G7 | Cohen et al. (2021) | Generation | Proof | Full | VI | T | Yes |
| G8 | Yang et al. (2017) | Generation | Proof | Full | VI | — | Yes |
| C1 | Neufeld & Sester (2024) | Conditions | Proof | Full | VI | — | Yes |
| C2 | Niu (2015) | Conditions | Assumption | Full | VII | T | Preprint |
| C3 | Andrès et al. (2026) | Conditions | Proof | Full | VI | T | Yes |
| C4 | Fukasawa (2022) | Conditions | Proof | Partial | VI | — | Yes |
| C5 | Stahl & Blauth (2024) | Conditions | Numerical test | Full | VI | T† | Yes |
| S1 | Gatheral & Jacquier (2013) | Baseline | Proof | Partial | VI | — | Yes |
| S2 | Fengler (2009) | Baseline | Numerical test | Full | VI | — | Yes |
| S3 | Hagan et al. (2014) | Baseline | Numerical test | Full | VI | — | Practitioner |
| S4 | Bodurtha & Jermakyan (1999) | Baseline | Assumption | Full | VI | — | Yes |
| S5 | Fengler et al. (2006) | Baseline | Assumption | Full | VI | — | Yes |

*Note.* Level refers to the evidence-level scale (I–VII); the corpus contains 40 level VI studies and one level VII review (C2). "Abstract" records the available read: full (34), partial (R2, G3, C4, S1) or metadata only (P4, P7, R4), reconciling to 41 (Section 3.3). "Time" marks the ten rows that engage surface dynamics in any form (Section 4.5); † marks the single-name panel retained under a scope flag. "Peer review" marks 29 peer-reviewed records, 11 preprints and one editorially reviewed practitioner magazine. The comparability code and the (M, E, V) triple are coded at the level of the analytical design (Section 3.5) and are read off the Family and Evidence-status columns rather than stored as separate row-level fields.

---

**Document metadata.** Body word count: 5,596 words (Abstract through the Responsible Use Statement, excluding section headings, citation-emission markers, references and appendices). Structure: Abstract, six numbered sections, AI Disclosure, Competing Interests and Funding, Responsible Use Statement, References, and Appendices A–C. Corpus: 41 sources—36 within 2015–2026 plus 5 seminal precursors (1999–2014); evidence 17 proof / 16 numerical test / 8 assumption, the in-window subset splitting 16 / 14 / 6; 0 of 36 in-window rows (0 of 31 construction rows) report a dynamic guarantee or test; 0 of 41 directly comparable from the abstracts. Generated 2026-11-23.
