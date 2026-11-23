# Four Loci of Enforcement: Static and Dynamic No-Arbitrage in Equity-Index Implied-Volatility Surfaces, 2015–2026

*Subtitle:* A structured, corpus-scoped review and a proposed framework for enforcement claims.

**Version:** v1.3 (Stage 2.5 integrity corrections) · **Author:** TY-Cheng (Independent Researcher) · **Date:** 2026-11-23
**Paper type:** Structured, corpus-scoped literature review with a framework contribution · **Citation style:** American Psychological Association (APA) 7.0
**Review-criteria status:** `criteria_binding_unavailable` — no author-confirmed `ReviewTargetContext` exists, so no venue alignment or submission readiness is claimed.

## Abstract

### English Abstract

Equity-index option markets quote hundreds of strikes and maturities daily, and the implied volatility surface that risk systems consume is economically coherent only if it excludes arbitrage on a single date and across dates. This review characterises, without ranking, how four families of construction methods enforce those constraints: parametric construction, which restricts the parameter domain; penalty-augmented objectives; projection-repair, which maps a fitted surface onto an admissible set; and generation-filtering, which screens candidate surfaces. The corpus is 41 sources — 36 published in 2015–2026 and 5 seminal precursors — of which 29 are peer-reviewed and 11 are preprints, coded on eight fields and read at abstract level; no systematic-review compliance or method ranking is claimed. Seventeen sources assert their guarantee at proof level, 16 report a numerical test, and 8 assert admissibility with neither. As reported in the abstracts, the certified object in all 41 rows is a single date's surface, and no source enforces or tests dynamic no-arbitrage, including none of the 31 construction rows. Proof-level and test-level evidence come from almost disjoint sets, and no two sources state data, metric and tolerance together, so no two rows are directly comparable. Read this way, the four families are not competing answers but four enforcement loci licensing four kinds of evidence, and the apparent disagreement between them is a division of evidential labour that leaves the dynamic condition visible as a void.

**Keywords:** implied volatility surfaces; no-arbitrage constraints; static arbitrage; dynamic arbitrage; model-free constraints; structured literature review

---

### Chinese Abstract

股指期权市场每一交易日都报出数百个行权价与到期日的组合，而风险系统实际消费的不是报价，是拟合后的隐含波动率曲面；该曲面只有在单日层面与跨日层面均不含套利时才具备经济一致性。本文对这四类构造方法如何承载上述约束作刻画性（而非排序性）梳理：参数化构造（以限制参数域实现）、惩罚增强型目标、投影修复（把拟合曲面映射到可行集），以及生成—筛选（对候选曲面进行检验）。语料为41篇文献，其中36篇发表于2015–2026年、5篇为有意纳入的早期奠基性研究，含29篇同行评审论文与11篇预印本；按八个字段编码、在摘要层面阅读，不主张系统性综述合规性，也不给出方法排序。17篇以证明层级主张其保证，16篇报告数值检验，另8篇既无证明也无检验却断言可行性。据摘要所载，41篇所认证的对象全部是单一交易日的曲面；没有任何一篇强制或检验动态无套利，31篇构造类文献无一例外。证明层级与检验层级的证据来自几乎不相交的集合，且没有任何两篇同时给出数据、度量与容差，因此任意两篇之间都不能直接比较。据此解读，四类方法不是相互竞争的答案，而是四个执行位点，各自许可一类证据；表面上的分歧实为证据分工，动态条件则被显现为一处空缺。

**Keywords:** 隐含波动率曲面；无套利约束；静态套利；动态套利；模型无关约束；结构化文献综述

---

## Draft Body

## 1. Introduction

### 1.1 Context and Problem

An equity-index option market quotes several hundred strike–maturity pairs on a typical trading day. Firms consume not quotes but a fitted implied-volatility surface, from which prices, Greeks, and risk-neutral densities are derived (Fengler, 2009)<!--ref:S2--><!--anchor:section:1.1-->. That surface is economically coherent only if it embeds no arbitrage. On a single date, call prices must be non-increasing and convex in strike, total variance must not decrease with maturity, and the zero-maturity limit must match intrinsic value (Gatheral & Jacquier, 2013<!--ref:S1--><!--anchor:section:1.1-->; Guo et al., 2016)<!--ref:P1--><!--anchor:section:1.1-->. Across dates, no self-financing strategy in the option panel may produce a riskless profit (Niu, 2015 [preprint])<!--ref:C2--><!--anchor:section:1.1-->. Construction is therefore constrained estimation rather than interpolation, run at scale on dense, noisy quotes (Wiedemann et al., 2025)<!--ref:N2--><!--anchor:section:1.1-->. Because the surface is what prices, hedges, and clears, a fitted artefact that admits arbitrage can in principle propagate into risk numbers, margin, and capital; that propagation is a premise, not a measurement: no study in this corpus tests it.

The phrase "arbitrage-free" does not denote one property. A method may be arbitrage-free because its parameter domain excludes violations (Guo et al., 2016)<!--ref:P1--><!--anchor:section:1.1-->, because a penalty discourages them (Na et al., 2023 [preprint])<!--ref:N5--><!--anchor:section:1.1-->, because a post-fit map removes them (Bender & Thiel, 2020)<!--ref:R3--><!--anchor:section:1.1-->, or because a generator is screened before output (Bajalica et al., 2026)<!--ref:G5--><!--anchor:section:1.1-->. These are different guarantees with different failure modes. The literature rarely separates them, and uses the same phrase for the static condition and for the dynamic one, although the second concerns the joint law of a surface process rather than the admissibility of one surface (Niu, 2015)<!--ref:C2--><!--anchor:section:1.1-->. The risk is claim inflation: a tested method read as proved, a static guarantee as dynamic. Throughout this review, an *audit* means a reported finite-sample violation test run on the construction's own output, and *dynamic* is reserved for process-level consistency across dates (Section 2.2); the *certified object* is the surface whose admissibility a row claims. Three questions therefore follow for any claim: which condition, at what tolerance, and verified how. They structure the analysis; condition and tolerance are annotations where an abstract supplies them, while the ledger codes locus and verification mode.

### 1.2 Purpose, Research Questions, and Contribution

The review asks **how** parametric construction, penalty, projection–repair, and generation–filtering methods for constructing equity-index implied-volatility surfaces enforce static and dynamic no-arbitrage constraints. Three sub-questions organise the answer. SQ1 asks which static conditions each family enforces, by what mechanism, and at what evidence status — proof, numerical test, or assumption. SQ2 asks which dynamic requirements are addressed, enforced, or merely tested. SQ3 asks what trade-offs appear across the review's evaluation dimensions.

Three hypotheses were declared before coding and are adjudicated in Section 5.1. **H1**: static enforcement is mostly achieved by construction, while dynamic requirements are asserted or tested rather than proved. **H2**: penalty and repair routes may displace rather than remove the constraint burden, absorbing it into weights, tolerances, and repair steps. **H3**: in generation–filtering methods, "arbitrage-free" often means "not rejected on this sample", so the claim is conditional on test power rather than on structure.

The contribution is fivefold: a 41-source evidence map coded on enforcement locus, evidence status, and comparability; the four-locus framework, which identifies the parameter domain, the objective, the output image, and the sampler-with-acceptance-test as the sites where constraints actually enter; the demonstration that proof-level and audit-level evidence are nearly disjoint; the identification of a dynamic void, bounded to the corpus; and a comparability discipline that forbids ranking and a seven-study agenda that would test the framework. None of these is a claim that one family outperforms another. Whether such a comparison is even licensed is one of the findings.

### 1.3 Scope and Organization

The scope is equity-index listed options. The corpus spans 2015–2026 plus five declared seminal precursors from 1999–2014; the four focal families are joined by a conditions-and-evaluation group and a seminal-baseline group. Evidence is abstract-level: 34 records were read in full abstract, four only partially, and three at title level, so every claim about what a study did is a claim about what its abstract reports. One disclosed exception is retained: a single-stock panel (Stahl & Blauth, 2024)<!--ref:C5--><!--anchor:section:1.3-->, admitted because it tests a martingale-defect condition directly, is scope-flagged throughout, and is never generalised to index surfaces. Section 2 defines the object and the framework, Section 3 the corpus and evidence rules, Section 4 the family-by-family findings, Section 5 the cross-family evidence, Section 6 the interpretation and agenda, and Section 7 the conclusion.

## 2. Theoretical Framework: What "Arbitrage-Free" Must Mean

### 2.1 Static Admissibility: Conditions SC1–SC5

Following the corpus, write total implied variance as $w(k,\tau)=\sigma^{2}\tau$, where $k=\log(K/F_{\tau})$ and $F_{\tau}$ is the forward. A surface is statically admissible if, expressed through the normalised call price $c(k,\tau)=C/F_{\tau}$, it satisfies five conditions: **SC1**, non-negative time value, $c(k,\tau)\ge\max(1-e^{k},0)$; **SC2**, monotone decreasing call prices in strike, $\partial c/\partial k\le 0$; **SC3**, strike convexity, the butterfly or Durrleman condition, $\partial^{2} c/\partial k^{2}\ge 0$; **SC4**, the zero-maturity limit $c(\cdot,0)=\max(1-e^{k},0)$; and **SC5**, calendar monotonicity of total variance, $w$ non-decreasing in $\tau$ (Anagha, 2026 [preprint]; Gatheral & Jacquier, 2013<!--ref:S1--><!--anchor:section:2.1-->; Martini & Mingone, 2022<!--ref:P2--><!--anchor:section:2.1-->)<!--ref:G6--><!--anchor:section:2.1-->. SC1–SC4 encode a non-negative risk-neutral density in price space; SC5 makes the object a surface rather than a family of slices.

The conditions are not interchangeable in strength, and the corpus exploits the difference. Gatheral and Jacquier (2013)<!--ref:S1--><!--anchor:section:2.1--> give closed-form **sufficient** conditions on the raw stochastic-volatility-inspired (SVI) parameters that guarantee SC1–SC4 on each slice, with a separate condition for SC5. Martini and Mingone (2022)<!--ref:P2--><!--anchor:section:2.1--> establish a characterisation that is **exact** for the SVI slice, expressed through monotonicity of the quantities $-d_{1}$ and $-d_{2}$ rather than through a restricted parameter box. Guo et al. (2016)<!--ref:P1--><!--anchor:section:2.1--> generalise the family and show that arbitrage-free surfaces exist outside the SVI class, with the guarantee carried by the parameter domain itself. A sufficient condition that is easy to impose can therefore exclude admissible surfaces, and an exact characterisation can be harder to enforce numerically. Which one a paper adopts is itself a design choice with evidential consequences.

A second distinction concerns scale, and it recurs throughout the review. Conditions are checked in specific units — price, total variance, moneyness — and a guarantee at one scale is not automatically a guarantee at another. The canonical failure is instructive: the SABR (stochastic alpha, beta, rho) implied-volatility approximation admits negative implied densities at low strikes for long maturities, a finite-strike violation that required a one-dimensional partial-differential-equation (PDE) density fix (Hagan et al., 2014)<!--ref:S3--><!--anchor:section:2.1-->. Asymptotic statements sit on the other side of the same distinction: a family can be asymptotically arbitrage-free in the wings while violating a condition at the strikes a desk actually quotes (Fukasawa, 2022)<!--ref:C4--><!--anchor:section:2.1-->. A surface described as arbitrage-free without a stated scale has therefore not stated its claim. Operationally, the corpus's conditions are exercised by repair and generation rows as well as by parametric ones (Bajalica et al., 2026; Xiong & Liu, 2026<!--ref:R5--><!--anchor:section:2.1-->)<!--ref:G5--><!--anchor:section:2.1-->, which is why SC1–SC5 serve as the review's static predicate rather than as a description of one family.

### 2.2 Dynamic Admissibility: What a Process-Level Guarantee Requires

A static condition constrains one surface. A dynamic condition constrains a family of surfaces indexed by calendar time, and the natural formulation is a filtered probability space on which the option-price process is a martingale under a measure consistent with the numéraire (Niu, 2015)<!--ref:C2--><!--anchor:section:2.2-->. What would count as a dynamic test is therefore a process-level property checked over a path: the absence of predictable arbitrage opportunities across dates, or the consistency of the surface family with a martingale measure, established by a stated argument and verified on a sequence of surfaces rather than on one slice.

The corpus contains no such test. One review of static and dynamic conditions discusses the question without testing it (Niu, 2015)<!--ref:C2--><!--anchor:section:2.2-->. A neural stochastic-differential-equation (SDE) market model constructs a state space of statically arbitrage-free prices and explicitly limits its claim to static, model-independent admissibility (Cohen et al., 2021)<!--ref:G7--><!--anchor:section:2.2-->. A path-dependent construction builds surfaces along stochastic paths that are statically free but does not test dynamic consistency across the resulting family (Andrès et al., 2026)<!--ref:C3--><!--anchor:section:2.2-->. A parametric family reports time-indexed arbitrage probabilities, which is a statement about a model's parameters over time rather than a path-level test of the fitted surface (Barski & Wiśniewolski, 2026 [preprint])<!--ref:P8--><!--anchor:section:2.2-->. A single-stock panel examines martingale defects and bubble conditions and is dynamic-adjacent, but it is scope-flagged (Stahl & Blauth, 2024)<!--ref:C5--><!--anchor:section:2.2-->. Ten rows in total engage time in some way; none enforces or tests a dynamic condition (Section 5.1).

The terminology matters because it changes the count. A calendar condition, in the sense of SC5, constrains the maturity axis of a single surface; it is often called "calendar arbitrage", which sounds dynamic. It is not. A construction that guarantees non-decreasing total variance across maturities has made a static statement about one date's object, and this review codes it as static wherever it appears. Once the term is fixed to process-level consistency, the dynamic count returns to zero, and the finding can be stated in a form that a later study could overturn.

### 2.3 The Enforcement Triple and the Four Loci

The review organises enforcement claims with a triple. The **mechanism** is where the constraint enters the estimation procedure. The **evidence** is what the resulting row licenses: a theorem over a set, a reported residual on a sample, or an assumption inherited from a model class. The **verification** is what was actually checked on the output: a proof, a finite-sample audit, or nothing reported. The triple separates three things that the phrase "arbitrage-free" fuses, and it is the instrument the findings are reported against.

The mechanism locates the guarantee at one of four loci. In **parametric construction**, the constraint enters the parameter domain, so every admitted parameter vector yields an admissible surface. In **penalty and constrained learning**, it enters the objective, so compliance is approximate and conditional on a weight, a tolerance, and an early-stopping rule. In **projection–repair**, it enters a map applied after fitting, so the certified object is the image of that map. In **generation–filtering**, it enters the sampler and the acceptance test, so the certified object is the accepted sample — or, where the generator's model class already excludes violations, the class itself. Figure 1 presents the triple and the four loci.

Three propositions follow, and they are tested in Section 4. First, when a guarantee is inherited from a deterministic decoder, the method is parametric in logical shape whatever its learning apparatus; the learning changes the estimator, not the form of the claim. Second, a penalty is a sampling device: its compliance statement is conditional on the weight and tolerance actually used, so the claim is about an evaluated sample rather than about a set. Third, construction and repair differ in what is observed — an admitted parameter set versus a transformed surface — so their guarantees are not the same object even when both are described as arbitrage-free.

Boundary cases are flagged rather than forced into a family. Two rows construct by distorting a reference function and also repair an existing quote set, so they sit between construction and repair (Bender & Thiel, 2020<!--ref:R3--><!--anchor:section:2.3-->; Buehler et al., 2026 [preprint])<!--ref:R6--><!--anchor:section:2.3-->. One row's constraint is architectural rather than a penalty term, which makes it a hybrid (Cao et al., 2020)<!--ref:N1--><!--anchor:section:2.3-->. Two constructions are model-level rather than data-driven, so their guarantee is inherited from the model class (Andrès et al., 2026; Cohen et al., 2021<!--ref:G7--><!--anchor:section:2.3-->)<!--ref:C3--><!--anchor:section:2.3-->. The taxonomy is offered as a proposed instrument, not as a partition, and the boundary cases are disclosed for that reason.

```text
Figure 1 (source diagram; to be typeset at Phase 7)

  ENFORCEMENT TRIPLE                        FOUR LOCI
  ┌───────────────────────┐   ┌──────────────────────────────────────────────┐
  │ mechanism  (where the │   │ L1  parameter domain   (parametric: P)       │
  │   constraint enters)  │   │ L2  objective / loss   (penalty: N)          │
  │ evidence   (what the  │   │ L3  output image       (projection–repair: R)│
  │   row licenses)       │   │ L4  sampler + acceptance test (generation: G)│
  │ verification (what    │   └──────────────────────────────────────────────┘
  │   was checked)        │      boundary cases: R3, R6 (L1↔L3), N1 (L2+arch),
  └───────────────────────┘      G7, C3 (model-level, guarantee inherited)
```

**Figure 1.** The enforcement triple (mechanism, evidence, verification) and the four loci at which the corpus's static guarantees enter. Loci are analytic categories, not quality grades; boundary cases are flagged rather than assigned.

## 3. Method: Corpus, Verification, and Comparability

### 3.1 Corpus Construction

The corpus was assembled from the OpenAlex representational-state-transfer (REST) application programming interface (API) with 31 free-text queries in eight groups — broad coverage (2), parametric construction (6), penalty methods (2), projection–repair (3), generation (6), neural methods (6), dynamic conditions (3), and evaluation (3) — each returning up to 25 records, restricted to English-language records dated 2015-01-01 to 2026-11-23. Retrieval requested 775 records and returned 750. One query ("SVI stochastic volatility inspired") was lost after a Hypertext Transfer Protocol (HTTP) 429 response; 21 first-pass responses were rate-limited and 20 were recovered on retry. One citation-chaining pass added no included source. Abstract recovery used Crossref and Semantic Scholar to complete records, not to add them.

De-duplication left 430 unique records. Screening excluded 389 under eight reason codes: off-topic (141), pre-2015 background (86), relevant but not selected (40), out-of-scope asset class (34), publication type (32), duplicate version (31), forecasting or trading (21), and model-calibration pricing (4). Forty-one studies were included: 36 in-window records and five declared seminal precursors dated 1999–2014, comprising 29 peer-reviewed articles or proceedings papers, 11 preprints (26.8%), and one practitioner magazine article. Table 1 profiles the corpus.

The inclusion frame required an equity-index option object, a construction or enforcement question, an explicit static or dynamic constraint, an English-language record, and a retrievable abstract, with one record per study. The procedure is **PRISMA 2020-style, not PRISMA-compliant**: no dual screening, adjudication, or protocol registration was performed, and no conformity with the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) or its scoping-review extension is claimed. Figure 2 shows the flow.

The six "neural" and six "generation" queries produced the largest hit volumes (150 and 149), which is why de-duplication removed 320 records — still fewer than the 389 that screening excluded. The eight reason codes are mutually exclusive by construction; a record excluded as off-topic is not also counted as a duplicate. Two included records were replaced during abstract reading when the retrieved text showed no enforcement claim; both replacements are named in Appendix A and recorded in the run artifacts rather than presented as an algorithmic outcome. Because the corpus is fixed from this point, every count in Sections 4 and 5 is a property of these 41 abstracts.

| **Table 1.** Corpus profile | |
|---|---|
| **Item** | **Value** |
| Database | OpenAlex REST API (single database) |
| Queries | 31 free-text queries in 8 groups; 25 records per query |
| Window and language | 2015-01-01 to 2026-11-23; English |
| Retrieval | 775 requested, 750 returned; one query lost after HTTP 429; 21 first-pass 429s, 20 recovered |
| Screening | 430 unique after de-duplication; 389 excluded; 41 included |
| Composition | 36 in-window (2015–2026) + 5 seminal precursors (1999–2014); 29 peer-reviewed, 11 preprints (26.8%), 1 practitioner magazine |
| Families | P 8, N 6, R 9, G 8, C 5, S 5 |
| Abstract coverage | 34 full, 4 partial (R2, G3, C4, S1), 3 metadata-only (P4, P7, R4) |
| Evidence status | 17 proof, 16 numerical test, 8 assumption; in-window 16 / 14 / 6; seminal 1 / 2 / 2 |
| Comparability | 0 direct, 30 context, 11 not comparable |
| Quality labels | A 11, B 13, C 17 (appraisal labels, not performance ranks) |
| Dynamic no-arbitrage | 0 of 41 rows enforce or test a dynamic condition; 10 rows engage time |
| Conformity | "PRISMA-style, not PRISMA-compliant"; no PRISMA claim |

```text
Figure 2 (source diagram; to be typeset at Phase 7) — not a PRISMA diagram

  OpenAlex, 31 queries ──► 775 requested ──► 750 returned ──► 430 unique
                                                                 │
                                      excluded 389 (8 reason codes)
                                                                 ▼
                                                        41 included
                                       36 in-window + 5 seminal precursors
```

**Figure 2.** Retrieval and screening flow. The diagram records the review's own arithmetic and is explicitly not a PRISMA flow diagram; no dual screening or adjudication step exists to represent.

### 3.2 Verification and Evidence Grading

All 41 records were resolved to a DOI-bearing index record (41/41); no record was flagged retracted by the OpenAlex `is_retracted` field. No independent retraction-database sweep was performed, so the check is a single-source consultation. Abstract coverage is uneven: 34 abstracts were read in full, four only partially (R2, G3, C4, S1), and three were unavailable, leaving those rows at title level (P4, P7, R4). Metadata-only rows are cited only for what their title asserts, and they are excluded from every evidence count.

Each row was coded on an evidence-status axis with three values. **Proof** means the record states a theorem or a formal construction that establishes admissibility over a set. **Numerical test** means the record reports a residual or violation check on its own output. **Assumption** means admissibility is asserted or inherited from a model class without either a proof or a test. A test is never upgraded to a proof, and a proof is never treated as an audit. The corpus codes 17 proof, 16 numerical test, and 8 assumption; 11 preprints are labelled where cited, and four of those appeared in 2025–2026.

Two further instruments were applied. Evidence-level labels VI (40 rows) and VII (one row) record the document type and reporting completeness, and the A/B/C quality labels (11/13/17) record source appraisal — peer review, method reporting, currency, and conflict-of-interest retrievability. Neither instrument ranks methods, and neither is used in Sections 4 and 5 to order families. No theorem was checked and no reported number was recomputed in this review; the verification is bibliographic, not mathematical.

### 3.3 Comparability Coding and Analytic Boundaries

Comparability was coded with three values. **Direct** requires the same dataset or panel, the same condition set and tolerance, the same metric and aggregation, and the same protocol. **Context** means a number is reported for background but does not license a comparison. **Not comparable** means a different object or metric. The result is 0 direct, 30 context, and 11 not comparable. Within-study baselines are the only licensed comparisons: a hard-constrained generator against surface SVI (SSVI) and a soft-penalty network (Anagha, 2026)<!--ref:G6--><!--anchor:section:3.3-->, a generative adversarial network (GAN) against a variational autoencoder (Sidogi et al., 2022)<!--ref:N4--><!--anchor:section:3.3-->, a penalty model against an artificial neural network (Na et al., 2023)<!--ref:N5--><!--anchor:section:3.3-->, and a repair procedure across five completion backends (Xiong & Liu, 2026)<!--ref:R5--><!--anchor:section:3.3-->. They compare implementations, not families.

Three consequences bound the analysis. First, no league table and no vote counting: results are reported as ranges with their conditions. Second, aggregate counts are this review's coding, not any source's claim, and are attributed accordingly. Third, the evidence is abstract-level, single-analyst, English-only, and OpenAlex-only, with no full text, proof, or code retrieval. Those limits are not repaired anywhere in the paper; they are stated once here and carried into Section 6.4.

The coding rules were fixed before the family accounts were written, which matters because several rows could plausibly be coded otherwise. A repair that proves a convergence property of the projection map is coded proof for the map, not for the repaired surface's dynamic behaviour. A generator whose architecture excludes violations is coded proof for its model class, not for the samples it emits. A row that reports a violation rate without a structural guarantee is coded numerical test even when the rate is zero. Applying these rules consistently is what makes the distributions in Section 5 interpretable; it is also why the boundary cases in Section 2.3 stay visible rather than being resolved by coding.

## 4. Findings I: How Each Family Enforces Static Admissibility

### 4.1 Parametric Construction

Parametric construction puts the constraint in the parameter domain: the family is parameterised so that every admitted vector yields a surface satisfying the stated conditions, so estimation is restricted to that set. Table 2 summarises the four focal families on the review's dimensions, with the two supporting groups shown for completeness.

The clearest case is a generalised SVI family whose arbitrage-freeness is inherited from the structure of the parameter set, with the guarantee holding for all admitted parameters rather than only at the fitted optimum (Guo et al., 2016)<!--ref:P1--><!--anchor:section:4.1-->. A second line replaces a sufficient parameter box with an exact butterfly characterisation, so that the admissible set is not narrower than necessary and calibration proceeds on the true admissible region (Martini & Mingone, 2022)<!--ref:P2--><!--anchor:section:4.1-->. A third extends the construction across maturities jointly, calibrating an extended SSVI parameterisation as one object rather than slice by slice, so that calendar monotonicity is a property of the joint fit (Mingone, 2022)<!--ref:P3--><!--anchor:section:4.1-->. That row is worth marking: it is a static guarantee across the maturity axis, not evidence of dynamic consistency (Section 2.2). A sequential slice-wise counterpart reaches the same family by a different route, available here only at title level (Corbetta et al., 2019)<!--ref:P4--><!--anchor:section:4.1-->.

Three further rows broaden the admissible shapes rather than the enforcement argument. A random-coefficient parameterisation widens the set of shapes the family can represent, including bimodal short-dated densities that fixed-coefficient forms cannot produce, while retaining a structural guarantee (Zaugg et al., 2025)<!--ref:P5--><!--anchor:section:4.1-->. A class-C3 interpolation constructs from a smaller knot set rather than calibrating to quotes, which changes what the guarantee is a claim about: the interpolant is admissible by construction, and the fit to data is a separate question (Le Floc’h, 2025)<!--ref:P6--><!--anchor:section:4.1-->. A bounded-factor model derives conditions under which the implied surface of a Gaussian-factor structure is free of static arbitrage and reports time-indexed arbitrage probabilities; it is the only parametric row that reports anything indexed by time (Barski & Wiśniewolski, 2026)<!--ref:P8--><!--anchor:section:4.1-->. A further row claims necessary-and-sufficient conditions for the SSVI/S3 curve but is metadata-only here and cannot corroborate them (Klassen, 2016 [preprint])<!--ref:P7--><!--anchor:section:4.1-->.

The evidence profile is the sharpest in the corpus: six of eight rows are proof-level, two assumption-level, and no row reports a residual audit on observed quotes. The guarantee is universal over the admitted set and silent about the fitted instance. The cost side is thin: restricting the parameter domain can tighten the wings or reduce fit where data are sparse, but no row pairs a parametric guarantee with a fit-cost measurement, so any such cost is stated qualitatively (Section 5.3).

The boundary with repair is real. An interpolation-by-distortion that begins from an arbitrage-free reference and a linear-programming construction both embed the constraint in a deterministic construction, yet what they certify is a transformed object rather than an admitted parameter vector (Bender & Thiel, 2020<!--ref:R3--><!--anchor:section:4.1-->; Buehler et al., 2026)<!--ref:R6--><!--anchor:section:4.1-->. Both are retained in the repair group rather than resolved: what distinguishes them is the certified object, and these two certify an image.

| **Table 2.** Four-family evidence summary (two supporting groups shown for completeness) | | | | | | |
|---|---|---|---|---|---|---|
| **Family** | **n** | **Enforcement locus** | **Object claimed "arbitrage-free"** | **Guarantee shape** | **Evidence licensed** | **Verification reported** | **Rows** |
| Parametric (P) | 8 | Parameter domain | Admitted parameter set | Universal over the admitted set | Proof (6), assumption/title-level (2); no residual audit | None in abstract | P1–P8 |
| Penalty (N) | 6 | Objective / loss | Evaluated sample at finite weight | Conditional on weight and tolerance | Residual rate; no guarantee | Residual or pass rate | N1–N6 |
| Projection–repair (R) | 9 | Output image | Surface after a map | Conditional on the projection | Proof (3), test (4), assumption (2); distortion plus residual | Residual floor | R1–R9 |
| Generation–filtering (G) | 8 | Sampler / acceptance | Accepted sample or inherited class | Within test power or model support | Proof (4), test (3), assumption (1); pass rate or architecture argument | Pass rate or proof | G1–G8 |
| Conditions / evaluation (C) | 5 | Diagnostic | Neither constructor nor repair | Detector or condition set | Proof (3), test (1), assumption (1); detection result or review | Detection / review | C1–C5 |
| Seminal baselines (S) | 5 | Pre-2015 baseline | Pre-constraint construction | No guarantee claim | Baseline only (1 proof, 2 test, 2 assumption) | None | S1–S5 |

**Table 2 note.** The four focal families are the subject; C and S are supporting groups. "Evidence licensed" is the review's coding, not a source's claim.

### 4.2 Penalty and Constrained Learning

Penalty methods add a violation term, or a differentiable surrogate for a constraint, to a training objective. The mechanism is an objective rather than a domain: the constraint is priced, so compliance is approximate and conditional on the weight, tolerance, and stopping rule. Six rows occupy this locus, and none is proof-level.

The clearest architectural case is a gated network whose slopes and weights are constructed so that the option-price function is frictionless and convex by design; the gate is a constraint-bearing architecture, so the row sits on the penalty/architectural boundary (Cao et al., 2020)<!--ref:N1--><!--anchor:section:4.2-->. A graph neural operator is trained across a ten-year intraday S&P 500 index (SPX) panel and reports adherence without a stated tolerance, which makes the claim hard to audit (Wiedemann et al., 2025)<!--ref:N2--><!--anchor:section:4.2-->. A deep-smoothing approach adds soft penalties plus a plug-in correction, aimed at sparse and erroneous quotes, and the penalty is not a guarantee (Ackerer et al., 2019 [preprint])<!--ref:N3--><!--anchor:section:4.2-->. A GAN with a static-arbitrage loss on the FTSE/JSE All Share (ALSI) index states plainly that the condition cannot be directly learned through the penalty route, which is the most explicit statement in the corpus of what a penalty can and cannot deliver (Sidogi et al., 2022)<!--ref:N4--><!--anchor:section:4.2-->. A second penalty model minimises violations and compares accuracy and runtime against an artificial neural network, reporting a residual rather than a certificate (Na et al., 2023)<!--ref:N5--><!--anchor:section:4.2-->. A deep convolutional network embeds derivative constraints, including a maturity-derivative term, in the loss and trains on SABR-generated data, so its reported adherence is an in-sample property of a simulated generator (Hoshisashi et al., 2023 [preprint])<!--ref:N6--><!--anchor:section:4.2-->.

The pattern is consistent: zero of six rows are proof-level, all six report a numerical test, and the residual violations are the mechanism working as designed rather than a defect. A penalty cannot certify a set; it can only report how much of the sample it failed to correct at a chosen weight. That is why the family's claim is indexed to an evaluated sample, and why a reader comparing a residual rate against a parametric guarantee is comparing two different claims.

One row is a hybrid: a gated network's constraint is structural rather than a soft term, so it is flagged and not used to support either claim alone (Cao et al., 2020)<!--ref:N1--><!--anchor:section:4.2-->. It is coded as a numerical test rather than as proof because the review credits a proof only where the abstract states a theorem over the admitted set (Appendix C), not where the shape of the function class is described as a design property.

### 4.3 Projection and Repair

Repair fits first and maps afterwards. The certified object is the image of the map, and the guarantee's strength depends on what the map proves: a projection can be shown to land in an admissible set, which is a statement about the map, not about the repaired surface across dates. Nine rows occupy this locus: three proof, four test, two assumption.

The projection line is represented by a linear-programming repair that moves prices minimally inside the bid–ask without any cross-date enforcement claim (Cohen et al., 2020)<!--ref:R1--><!--anchor:section:4.3-->, and by an entropic projection to the arbitrage-free set built on Sinkhorn's algorithm, whose convergence proof is a proof about the projection (De March & Henry-Labordère, 2019 [preprint])<!--ref:R2--><!--anchor:section:4.3-->. A third line begins from an arbitrage-free reference function and distorts it, so the construction and the repair share the same observable; the Kahalé approach appears as a special case (Bender & Thiel, 2020)<!--ref:R3--><!--anchor:section:4.3-->. A strictly arbitrage-free non-parametric construction calibrates by linear programming with a positive discrete local volatility, which places it at the construction edge of the repair locus (Buehler et al., 2026)<!--ref:R6--><!--anchor:section:4.3-->.

Three rows report measured residuals. An observation-anchored repair runs over 252 out-of-sample SPX days and five completion backends and reports a butterfly violation floor of about 5.4%, so the repaired surface is not violation-free on real quotes; a cubic-spline backend has the lowest reconstruction error after repair (Xiong & Liu, 2026)<!--ref:R5--><!--anchor:section:4.3-->. A Chebyshev-tensor surface with a quadratic-programming stage and a post-fit adjustment reports under 1% static violations and 98–99% inside-spread coverage in calm years, with out-of-band leakage under stress (Alvarez, 2025 [preprint])<!--ref:R7--><!--anchor:section:4.3-->. A Markov-chain approximation over 2,695 SPDR S&P 500 ETF (SPY) options across 28 maturities carries a time axis without a dynamic audit (Madan & Schoutens, 2019)<!--ref:R9--><!--anchor:section:4.3-->. One row asserts transformations without either proof or test (Zetocha, 2023 [preprint])<!--ref:R8--><!--anchor:section:4.3-->, and another expands the scope to joint American call-and-put smoothing at title level (Yao et al., 2026)<!--ref:R4--><!--anchor:section:4.3-->.

The family's baseline is the shape-constrained smoothing spline, which showed that ignoring the constraint matters, before the four-family split existed (Fengler, 2009)<!--ref:S2--><!--anchor:section:4.3-->. Two earlier constructions did not enforce admissibility at all: a nonparametric inversion solved for a surface without an explicit constraint set (Bodurtha & Jermakyan, 1999)<!--ref:S4--><!--anchor:section:4.3-->, and a semiparametric factor model on DAX (Deutscher Aktienindex) data estimated dynamics without enforcement (Fengler et al., 2006)<!--ref:S5--><!--anchor:section:4.3-->. Both are baselines, not counterexamples: they predate the constraint literature this review codes.

### 4.4 Generation and Filtering

Generation–filtering methods produce candidate surfaces, parameters, or prices and then accept, reject, project, or constrain them. The locus is the sampler with its acceptance test, and the family splits there: an inherited guarantee behaves like a parametric construction, while a penalised sampler reports a pass rate.

Four rows sit on the inherited side. A variational autoencoder over the parameters of stochastic-volatility models generates surfaces whose admissibility follows from the SDE class rather than from the training objective (Ning et al., 2023)<!--ref:G1--><!--anchor:section:4.4-->. A neural-SDE state space defines a family of statically arbitrage-free prices and explicitly disclaims a dynamic guarantee (Cohen et al., 2021)<!--ref:G7--><!--anchor:section:4.4-->. A gated rational network is arbitrage-free by design, one of the earliest architectural guarantees in the corpus (Yang et al., 2017)<!--ref:G8--><!--anchor:section:4.4-->. Trainable hard constraints go further: the constraint is imposed as a differentiable but hard architectural element, and the row reports 0.00% violations at a $10^{-4}$ tolerance over 15 runs on synthetic SVI data (Anagha, 2026)<!--ref:G6--><!--anchor:section:4.4-->. That row is the only one in the corpus that reports both a structural guarantee and an audit of its own output, and reports higher total-variance root-mean-square error (RMSE) than an SSVI baseline and a soft-penalty network — the corpus's one clear paired measurement, and it runs against the claim that a stronger guarantee buys a better fit.

Four further rows sit on the filtered side. A VolGAN (a volatility GAN) generates joint surface and underlying scenarios and evaluates them through hedging against a Black–Scholes delta, while the enforcement mechanism is not described (Vuletić & Cont, 2024)<!--ref:G2--><!--anchor:section:4.4-->. A simulation approach places static constraints inside a generated process but is only partly available at abstract level (Cont & Vuletić, 2023)<!--ref:G3--><!--anchor:section:4.4-->. A GAN denoiser reports lower mean-squared error (MSE) and runtime without a guarantee claim, which makes it a smoothing tool rather than a certified generator (Ginart Belmonte & Cole, 2025)<!--ref:G4--><!--anchor:section:4.4-->. A latent flow-matching generator reports that 90.8% of generated surfaces pass all tested static conditions, the corpus's clearest pass-rate statement (Bajalica et al., 2026)<!--ref:G5--><!--anchor:section:4.4-->.

The split tracks the locus, as the framework predicts. Inherited-guarantee rows behave like parametric constructions; penalised-sampling rows report a number whose meaning depends on test power and tolerance, and none of them estimates either. A pass rate is not a guarantee, and a guarantee is not an audit; a reader who wants both must look for the one row that reports both, on synthetic data, and accept its fit cost.

## 5. Findings II: Evidence Status, Comparability, and Evaluation Coverage

### 5.1 Evidence Status and the Proof–Audit Gap

The corpus splits into 17 proof-level rows, 16 numerical tests, and 8 assumptions; within the 36 in-window records the split is 16 / 14 / 6, and the five seminal precursors contribute 1 / 2 / 2. By family, parametric construction is 6 proof / 0 test / 2 assumption, penalty 0 / 6 / 0, repair 3 / 4 / 2, generation 4 / 3 / 1, conditions 3 / 1 / 1, and seminal baselines 1 / 2 / 2 (Table 3). The distribution is not an accident of coding: it follows the loci. A parameter-domain construction licenses a theorem; an objective licenses a sample; a map licenses a statement about the map; a sampler licenses a pass rate.

Six rows audit their own output: a graph neural operator reporting adherence on ten years of intraday data (Wiedemann et al., 2025)<!--ref:N2--><!--anchor:section:5.1-->, a deep network with derivative constraints on simulated data (Hoshisashi et al., 2023)<!--ref:N6--><!--anchor:section:5.1-->, a repair reporting a 5.4% butterfly floor (Xiong & Liu, 2026)<!--ref:R5--><!--anchor:section:5.1-->, a Chebyshev construction reporting under 1% violations (Alvarez, 2025)<!--ref:R7--><!--anchor:section:5.1-->, a flow-matching generator reporting a 90.8% pass rate (Bajalica et al., 2026)<!--ref:G5--><!--anchor:section:5.1-->, and a hard-constrained generator reporting 0.00% at $10^{-4}$ over 15 runs (Anagha, 2026)<!--ref:G6--><!--anchor:section:5.1-->. The cross-tabulation is the finding: among the 17 proof-level rows, only one reports a violation rate on its own output, and among the six audit rows only that row also reports a structural guarantee — and it does so on synthetic data. Proof and audit are therefore nearly disjoint channels: a reader can inspect the theorem or the residual, usually not both.

Table 4 adjudicates the three hypotheses. H1 is supported in its static clause, since all 41 rows are coded on a static predicate and six of eight parametric rows are proof-level. Its dynamic clause is disconfirmed as stated: the hypothesis expected dynamic requirements to be asserted or tested, but no row in the corpus asserts a tested dynamic condition, so the correct statement is absence rather than weak enforcement (0 of 41; 0 of 36 in-window). H2 is unsupported in its fit-error clause — no penalty or repair row reports a lower fit error than a constrained parametric baseline on the same data, and the one paired measurement reports a higher error for the stronger guarantee — while its burden-displacement clause is supported: weights, tolerances, repair steps, and acceptance thresholds are where the constraint work is absorbed (Na et al., 2023<!--ref:N5--><!--anchor:section:5.1-->; Sidogi et al., 2022<!--ref:N4--><!--anchor:section:5.1-->; Xiong & Liu, 2026)<!--ref:R5--><!--anchor:section:5.1-->. H3 is supported for the penalised-sampling branch, where a pass rate is the whole claim, and disconfirmed for the inherited-guarantee branch, where four rows are structural rather than sample-filtered (Anagha, 2026<!--ref:G6--><!--anchor:section:5.1-->; Cohen et al., 2021<!--ref:G7--><!--anchor:section:5.1-->; Ning et al., 2023<!--ref:G1--><!--anchor:section:5.1-->; Yang et al., 2017)<!--ref:G8--><!--anchor:section:5.1-->.

Two coding conventions protect the result. Metadata-only rows are not counted as evidence for their claims, so the proof count does not inherit a claim from a title. Preprints are labelled wherever cited, so a reader can see that three of the six audit rows are preprints (N6, R7, G6). Neither convention changes the direction of any count, and both are stated so that a different coder could reproduce or contest them.

| **Table 3.** Evidence-status distribution (review coding) | | | | | |
|---|---|---|---|---|---|
| **Family** | **Proof** | **Numerical test** | **Assumption** | **Total** | **Audit rows** |
| P (parametric) | 6 | 0 | 2 | 8 | 0 |
| N (penalty) | 0 | 6 | 0 | 6 | 2 (N2, N6) |
| R (projection–repair) | 3 | 4 | 2 | 9 | 2 (R5, R7) |
| G (generation) | 4 | 3 | 1 | 8 | 2 (G5, G6) |
| C (conditions) | 3 | 1 | 1 | 5 | 0 |
| S (seminal) | 1 | 2 | 2 | 5 | 0 |
| **Total** | **17** | **16** | **8** | **41** | **6** |

**Table 3 note.** In-window split 16 / 14 / 6 over 36 rows; seminal split 1 / 2 / 2 over 5 rows. An audit row reports a residual or violation check on its own output; G6 is the only row that also reports a structural guarantee.

| **Table 4.** Hypothesis adjudication | | | |
|---|---|---|---|
| **Hypothesis** | **Verdict** | **Basis** | **Residual uncertainty** |
| H1 — static enforcement is mostly by construction; dynamic requirements are asserted or tested rather than proved | Static clause supported; dynamic clause disconfirmed as stated | All 41 rows coded on a static predicate; 6 of 8 parametric rows proof-level; 0 of 41 enforce or test a dynamic condition | The dynamic reading depends on abstract-level coding and on vocabulary (Section 6.2) |
| H2 — penalty and repair routes displace rather than remove the constraint burden | Burden-displacement clause supported; fit-error clause unsupported | No penalty or repair row reports lower fit error than a constrained parametric baseline on the same data; tolerances, weights, and repair steps absorb the constraint; one paired measurement reports a higher error (G6) | Adequacy of any residual rate is not assessable without a loss and tolerance the corpus does not supply |
| H3 — generation's "arbitrage-free" often means "not rejected on this sample" | Supported for the penalised-sampling branch; disconfirmed for the inherited-guarantee branch | G5 reports a 90.8% pass rate; G1, G6, G7, G8 are structural rather than sample-filtered | Small branches (four and four); enforcement mechanism is under-described in several rows |

### 5.2 Comparability and the Metric Vocabulary

The comparability coding returns 0 direct, 30 context, and 11 not comparable, and the breakdown by family is uneven in an informative way (Table 5). Every parametric row is context or not comparable; no penalty or generation row is not comparable, because their objects and metrics fall inside the same loose vocabulary; the conditions group carries the largest share of not-comparable rows (three of five) and the parametric group the largest number (four of eight), because their objects differ.

A direct comparison requires four fields: the same dataset or panel, the same condition set and tolerance, the same metric and aggregation, and the same protocol. No row reports all four. Tolerance is the field most often missing: several rows report a violation rate without stating the tolerance at which it was computed, which makes the rate uninterpretable even within its own study. Dataset overlap is the second gap: the SPX panel recurs, but on different date ranges, sampling frequencies, and option filters.

Seven metric families appear across the corpus: price-space error, volatility-space error, total-variance error, bid–ask spread capture, Wasserstein distance, hedging P&L, and runtime. A reported number is context unless the protocol matches, and protocols do not match across families. Even the apparently comparable violation-rate family is not comparable: a 90.8% pass rate on generated surfaces, a 5.4% butterfly floor on out-of-sample SPX days, an under-1% violation rate for a Chebyshev construction, and 0.00% at $10^{-4}$ on synthetic SVI data differ in data, definitions, tested conditions, and tolerance. Ordering them would compare methods, datasets, and reporting conventions at once.

Within-study baselines are the only licensed comparisons. A hard-constrained generator is compared with SSVI and a soft-penalty network on the same data (Anagha, 2026)<!--ref:G6--><!--anchor:section:5.2-->; a GAN with a variational autoencoder (Sidogi et al., 2022)<!--ref:N4--><!--anchor:section:5.2-->; a penalty model with an artificial neural network (Na et al., 2023)<!--ref:N5--><!--anchor:section:5.2-->; and a repair procedure across five completion backends (Xiong & Liu, 2026)<!--ref:R5--><!--anchor:section:5.2-->. A neural detector of model-free static arbitrage exists as an independent auditor, but it is never applied to another row in this corpus (Neufeld & Sester, 2024)<!--ref:C1--><!--anchor:section:5.2-->. The consequence is that the review reports ranges with conditions and no league table, and that the absence of a common protocol is itself a finding rather than a gap in the review.

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

**Table 5 note.** A direct comparison requires the same dataset or panel, the same condition set and tolerance, the same metric and aggregation, and the same protocol. No row reports all four; tolerance is the most frequently missing field.

### 5.3 Evaluation Coverage: Seven Dimensions

Table 6 maps what the corpus measures against seven evaluation dimensions. The first is populated: static no-arbitrage is coded for all 41 rows, with 17 proof, 16 test, and 8 assumption, and tolerances are rarely stated. The second is empty: ten rows engage time, none enforces or tests a dynamic condition. Fit accuracy is partial — roughly eight rows report an error on held-out data, but on disjoint datasets and in three different metric spaces, so the numbers are context. Interpolation and stability are thin: about eight rows report held-out strike or maturity behaviour, none runs a boundary audit, and repeated-run or subsample stability is rarely reported. Computational cost is asserted in about five rows with no comparable measurement. Interpretability is unpopulated: no row reports density, wing, or parameter recoverability as an evaluation target. Data efficiency is unpopulated: no row reports fit or violation rate as a function of quote count, date count, or training-set size.

These counts aggregate the seventh coded field defined in Appendix C, the fit or accuracy metric a row reports, and the per-row coding is held with the stage 1 records of this study rather than reproduced column by column in Appendix B. The distinction between coverage and performance is load-bearing. The matrix records whether a dimension is measured, not whether a method is good; a populated row is an evidentiary fact, and an empty row is an absence of measurement, which is not evidence that the dimension cannot be measured. The pattern across the matrix is what the agenda in Section 6.3 responds to: the static dimension is populated, the dynamic, interpretability, and data-efficiency dimensions are empty, and cost is asserted rather than measured.

The cost of a stronger guarantee is measured on one side only. A hard-constrained generator reports a structural guarantee and a 0.00% audit, and also reports a higher total-variance error than two baselines (Anagha, 2026)<!--ref:G6--><!--anchor:section:5.3-->. A repair reports a 5.4% floor and selects a backend by reconstruction error (Xiong & Liu, 2026)<!--ref:R5--><!--anchor:section:5.3-->. A Chebyshev construction reports sub-1% violations and inside-spread coverage with stressed-year leakage (Alvarez, 2025)<!--ref:R7--><!--anchor:section:5.3-->. A flow-matching generator reports a pass rate without a paired fit-cost comparison (Bajalica et al., 2026)<!--ref:G5--><!--anchor:section:5.3-->. The corpus therefore cannot support the claim that a penalty or repair route lowers fit error, and one paired measurement points the other way; whether any reported residual is operationally adequate is not assessable without a loss function and a tolerance that the corpus does not supply.

Table 6 is a seven-axis coverage frame. An earlier Stage 1 instrument used eight axes, adding extrapolation and reproducibility; the seven-axis frame is the manuscript's instrument, the two are reconciled in Appendix C, and no count or claim changes between them.

| **Table 6.** Seven-dimension evaluation matrix: coverage, not performance | | |
|---|---|---|
| **Dimension** | **Operationalization** | **Coverage and status** |
| Static no-arbitrage | Condition set SC1–SC5, tolerance, verification mode | 41/41 coded; 17 proof / 16 test / 8 assumption — populated; tolerances rarely stated |
| Dynamic consistency | Path-level condition and test over time | 10 rows engage time; 0 enforce or test — unpopulated |
| Fit accuracy | IV or total-variance error on held-out data | ~8 rows; datasets disjoint — partial; not comparable |
| Interpolation and stability | Held-out strikes/maturities; repeated runs or subsamples | ~8 rows — thin; no boundary audit |
| Computational cost | Wall-clock or memory on a fixed grid | ~5 claims — asserted; 0 comparable |
| Interpretability | Density, wing, or parameter recoverability as an evaluation target | 0 rows — unpopulated |
| Data efficiency | Fit or violations against quote, date, or training size | 0 learning curves — unpopulated |

**Table 6 note.** A coverage map, not a scorecard: no column orders methods, and an unpopulated dimension means "not measured in this corpus", not "not measurable".

## 6. Discussion: Four Meanings, the Dynamic Void, and an Agenda

### 6.1 Four Meanings of One Word

The findings resolve "arbitrage-free" into four claims that the corpus states with one phrase. In a parametric construction it is a theorem over an admitted parameter set. In a penalty method it is an objective minimised to a tolerance on an evaluated sample. In projection–repair it is an output mapped onto an admissible set. In generation–filtering it is an accepted sample that passed a test, or a model class that cannot emit a violation. These are not four degrees of the same claim: they differ in what is quantified over, and a reader who compares them without that distinction compares a theorem with a sample.

The reporting remedy is a triple rather than a new vocabulary (Section 2.3). A paper should state the condition it enforces, which of SC1–SC5 or a dynamic condition; the tolerance, numerical or exact; and the verification mode, proof, test, or assumption. A surface is then admissible under a named condition at a stated tolerance by a stated mode, and a reader can see which of the three elements is missing. The one row that reports all three does so on synthetic data (Anagha, 2026)<!--ref:G6--><!--anchor:section:6.1-->, which shows that the triple is reportable rather than idealised. The two penalty rows that concede the limit of their route are the clearest evidence that the authors know which claim they are making (Na et al., 2023; Sidogi et al., 2022<!--ref:N4--><!--anchor:section:6.1-->)<!--ref:N5--><!--anchor:section:6.1-->.

The implications run to three audiences. Authors should report the locus and the verification mode, because a proof and a passed test are not interchangeable evidence of the same property. Reviewers and editors should ask for the missing element rather than accept the phrase as a completion label. Readers should not compare numbers produced under different modes, datasets, and tolerances — which, given Section 5.2, means almost all of the numbers in this corpus.

### 6.2 The Dynamic Void and Calendar Conflation

The absence of dynamic enforcement is the review's most consequential finding and its most fragile one. It is not a proof that the field ignores dynamics; it is a bounded statement about 41 abstracts. To our knowledge, based on searches of OpenAlex covering 2015-01-01 to 2026-11-23, as of 2026-11-23 no included study states and tests a process-level dynamic no-arbitrage condition for an equity-index implied-volatility surface; the nearest prior work reviews the conditions without testing them (Niu, 2015)<!--ref:C2--><!--anchor:section:6.2-->.

Two explanations are consistent with the coding result, and the review cannot distinguish them. The first is a genuine gap: the visible rewards in this literature attach to static construction, fit, and generation, and a dynamic test requires a multi-date panel and a protocol that no row reports. The second is a retrieval and vocabulary effect: studies may test dynamic properties under labels the search did not capture, or abstracts may omit a test the full text reports. The review states both readings because selecting one would convert an absence into an inference it cannot support.

Calendar conflation is the main reason the gap is easy to miss. SC5 is a static condition on the maturity axis of one surface, but it is routinely described as "calendar arbitrage", a phrase that sounds dynamic. A generator that constrains maturity monotonicity has made a static claim (Anagha, 2026<!--ref:G6--><!--anchor:section:6.2-->; Bajalica et al., 2026<!--ref:G5--><!--anchor:section:6.2-->), as has a repair that enforces it (Xiong & Liu, 2026)<!--ref:R5--><!--anchor:section:6.2-->. The neural-SDE row explicitly disclaims dynamics (Cohen et al., 2021)<!--ref:G7--><!--anchor:section:6.2-->; the one review that treats dynamic conditions at length does not test them (Niu, 2015)<!--ref:C2--><!--anchor:section:6.2-->; and the path-dependent and time-indexed constructions build objects along a time axis without a process-level test (Andrès et al., 2026<!--ref:C3--><!--anchor:section:6.2-->; Barski & Wiśniewolski, 2026)<!--ref:P8--><!--anchor:section:6.2-->.

Scale relativity compounds the confusion in a second dimension. A finite-strike SABR failure and an asymptotic arbitrage-free approximation are compatible statements because they hold in different regimes: the first says a quoted surface admits a negative density at long maturities, the second says the wings behave correctly as strikes grow (Fukasawa, 2022; Hagan et al., 2014<!--ref:S3--><!--anchor:section:6.2-->)<!--ref:C4--><!--anchor:section:6.2-->. A guarantee at one scale is not a guarantee at another, and the corpus rarely states which scale it means.

### 6.3 A Priced-Trade-Off Research Agenda

The gaps convert into seven studies, each tied to a measurable outcome and to a claim it would falsify. All are proposals; none is reported as done here.

The first is a dynamic enforcement test. Starting from a surface family with a stated process (Andrès et al., 2026<!--ref:C3--><!--anchor:section:6.3-->; Barski & Wiśniewolski, 2026)<!--ref:P8--><!--anchor:section:6.3-->, it would define a path-level admissibility condition and run it over a multi-year index panel. It would falsify this review's bounded-absence claim if a tested dynamic condition turned out to be already present under a different label, and it would convert "dynamic" from a label into a testable property.

The second is a pre-registered head-to-head. With one index panel, a common condition set, a stated tolerance, one metric, and one aggregation, frozen before fitting, it would produce the corpus's first direct comparison and falsify the claim that cross-family comparison is not currently licensed. The third is a residual audit for proof constructions: applying an independent detector (Neufeld & Sester, 2024)<!--ref:C1--><!--anchor:section:6.3--> to proof-bearing parametric and repair rows would test whether their guarantees survive finite-sample implementation, reporting violations at a stated tolerance on observed quotes. The fourth is a test-power and noise-floor study, which would estimate false-positive and false-negative rates of violation tests and separate data noise from method error; the 5.4% repair floor is the motivating case (Xiong & Liu, 2026)<!--ref:R5--><!--anchor:section:6.3-->. The fifth is a data-efficiency study that reports violation rate and fit against quote count, date count, and training size, filling an empty column of Table 6. The sixth is a cross-market replication with the second study's protocol on three indices, at least one non-US, testing whether the findings are index-specific. The seventh prices the trade-off: wall-clock and memory on a fixed grid, plus an interpretability rubric for density, wing, and parameter recoverability.

Two design decisions hold the agenda together. Each study names a claim it would falsify, so that a null result is informative rather than a call for more research. And each is scoped to produce a different evidence type for a different family, which is the framework's own test: if the four loci are real, these studies should not converge on a single ranking, and a study that produced one would force the framework to be revised.

### 6.4 Limitations

The evidence is abstract-level (34 full, 4 partial, 3 metadata-only), 11 records are preprints, and one is a practitioner magazine article. Coding was single-analyst, retrieval was English-only and OpenAlex-only, one query was lost after HTTP 429, and known-provenance rows are dominated by US indices (10 of 12), with non-US evidence resting on a 2006 DAX study and a 2022 Johannesburg Stock Exchange study. No full text, proof, or code was retrieved, and no theorem was re-derived and no reported number recomputed.

The instruments are proposed, not validated. The four-family taxonomy and the seven-dimension matrix are analytic categories, the boundary cases are disclosed rather than resolved, and a different coder applying the same rules could shift individual rows. The absence findings are bounded to 41 abstracts; the framework is explanatory and untested; and no causal, ranking, or field-wide claim is made. The single-stock panel is a disclosed exception, not index evidence.

## 7. Conclusion

### 7.1 Key Takeaways

The research question was how four families enforce static and dynamic no-arbitrage. Four answers survive the limitations.

Static admissibility is enforceable in all four families, but each family enforces it on a different object: an admitted parameter set, an evaluated sample at a finite weight, the image of a projection, or an accepted sample from a sampler. The locus explains the evidence: a parameter-domain construction licenses a theorem, an objective licenses a residual, a map licenses a statement about the map, and a sampler licenses a pass rate. This is the review's central descriptive finding, and it holds across the boundary cases rather than requiring them to be resolved. Stated as an instrument, the framework is the enforcement triple — mechanism, evidence, verification — applied at four loci, plus the reporting triple of condition, tolerance, and verification mode; each half is usable alone, and each names what a claim would have to report to be checkable.

Dynamic admissibility is neither enforced nor tested anywhere in the corpus. Ten rows engage time; none states a path-level condition and checks it over a path. The claim is bounded: 0 of 41 abstracts, 0 of 36 in-window records, and 0 of 31 construction records, not a statement about the field. Two readings remain open, a genuine gap or a retrieval and vocabulary effect, and the review declines to choose between them.

Proof-level and audit-level evidence are nearly disjoint. Seventeen rows are proof-level and only one reports a violation rate on its own output; six rows audit their own output and that one also reports a structural guarantee, on synthetic data. A reader who wants a theorem and a residual for the same surface will not find the pair in this corpus.

Direct comparison is unavailable, so no ranking is possible. No row reports the four fields a direct comparison requires, and the metric vocabulary fragments into seven families whose numbers are not points on one scale. The review therefore reports ranges and conditions rather than a league table.

### 7.2 Implications and Closing

For authors, the practical implication is a reporting habit: state the condition, the tolerance, and the verification mode; report an audit even when the construction is a proof; and say whether the claim is static or dynamic. The triple costs three sentences and would make the literature's own numbers comparable in a way they currently are not. It would also make a negative result publishable, since a construction that fails a stated audit at a stated tolerance is a finding rather than a silence, and it would let a reader distinguish a method that was tested and passed from one that was never tested. For reviewers and editors, the implication is to ask for the missing element rather than accept the phrase. For practitioners, the corpus does not identify a best method; it identifies what each method's guarantee is worth and what it costs, which is a more useful input to a build-or-buy decision than an unqualified label.

The framework is offered as a proposed instrument with falsifiable consequences: a boundary row it cannot place, or agenda studies that fail to produce family-specific evidence, would count against it. It is not a ranking, and it does not license one.

The closing point is a question of description rather than quality. For an equity-index implied-volatility surface, the useful question is not whether it is arbitrage-free, but which admissibility claim its construction licenses, at what tolerance, and how that claim was checked.

<!--protected-hedges: To our knowledge, based on searches of OpenAlex covering 2015-01-01 to 2026-11-23, as of 2026-11-23-->

## Declarations

**Data Availability Statement.** The review is based on 41 published bibliographic records; the frozen corpus, the coding records, and the search and screening provenance are held in the run directory for this study, and no new empirical data were generated. Reported numbers are drawn from those frozen records and from the sources' own abstracts.

**Ethics Declaration.** Not applicable. The study involves no human participants, no animal subjects, no personal data, and no sensitive materials; no ethics approval was required.

**Author Contributions (CRediT, Contributor Roles Taxonomy).** TY-Cheng: Conceptualization; Methodology; Investigation; Data Curation; Writing – original draft; Writing – review & editing; Visualization.

**Conflict of Interest Statement.** None declared. The author has no financial or personal relationship to any source, software, or venue discussed.

**Funding Acknowledgment.** No funding was received for this work.

**AI Use Disclosure.** This paper was produced with artificial-intelligence (AI)-assisted research tools operating under the Academic Research Skills (ARS) v3.24.4 protocol. AI assisted with query construction and search, screening, abstraction, coding and grading of the 41-row evidence ledger, synthesis, drafting, and bilingual abstract preparation. The generative model was a Claude-family agent operating within DeepSeek Harness (DSH) on 2026-11-23; the exact model identifier and version were not recorded in the run log. Verification was limited to bibliographic resolution: all 41 records were resolved and none was flagged retracted, but no theorem was checked and no reported number recomputed, and the three metadata-only rows are cited at title level only. Screening and coding were single-analyst, without dual screening or adjudication. Human involvement consisted of run authorization and checkpoint review; no claim-level human verification of the 41 coded rows is recorded. The tools cannot read full texts, proofs, or code, depend on third-party metadata and abstract reconstruction, and can introduce retrieval, quotation, and coding errors that the Limitations in Section 6.4 bound but do not eliminate.

**Responsible Use Statement.** The dual-use assessment returned Level None. Synthesising published construction and verification methods at abstract level, this paper adds no code, dataset, calibration recipe, or implementable procedure, names no tradable strategy, and ranks no method for deployment. Nothing here is investment, valuation, or risk-management advice.

## References

*Note on versions.* Four entries first appeared online before their printed issue was published. The year in the citation is the online year used throughout this paper; the bracketed note gives the printed issue year, and each DOI resolves to the version of record. Preprint tags follow the corpus convention: they mark a manuscript with no peer-reviewed version of record in this corpus.

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

## Appendix A. Search and Screening Record

The corpus was frozen in Stage 1 of this study and is reused unchanged; no new search was run for this manuscript. Retrieval targeted OpenAlex (English metadata and abstracts only) on 2026-11-23.

**Query groups and yield.** Thirty-one queries in eight groups: broad (2), parametric construction (6), penalty and constrained learning (2), projection and repair (3), generation and filtering (6), neural and learning (6), dynamic and time-indexed (3), evaluation and conditions (3). The requests asked for 750 records over two pages; 775 requests were issued, 750 records were returned (one page failed with HTTP 429 and was not retried within the freeze window), and 430 unique records remained after de-duplication.

**Screening arithmetic.** Of the 430 unique records, 389 were excluded and 41 retained. Exclusion codes: off-topic 141; pre-2015 background 86; relevant but not selected 40; out-of-scope asset 34; publication type 32; duplicate version 31; forecasting or trading 21; model calibration or pricing 4. Two records initially retained failed both metadata resolution and abstract reconstruction and were replaced from the relevant-but-not-selected pool; both replacements are recorded in the Stage 1 bibliography and verification artifacts. The remaining 40 exclusions under relevant-but-not-selected are discretionary, made on topic fit under the frozen inclusion rule (equity-index implied-volatility surfaces plus an explicit no-arbitrage condition or enforcement mechanism), and are recorded per record rather than reconstructed here. Ten of the 12 rows with known provenance are US-index studies.

**What this is not.** This is a structured, corpus-scoped review, not a systematic review: single-analyst screening, no dual coding, English-only retrieval, and a discretionary final selection mean that PRISMA 2020 compliance is not claimed and the corpus is not exhaustive. The flow from 430 unique records to 41 is reported for auditability, not as a PRISMA diagram.

## Appendix B. Evidence Ledger

Each row records the review's coding of one source. "Evidence" is the status of the no-arbitrage claim as reported (proof, numerical test, or assumption); "Comp." is the comparability class (DC directly comparable, RC reported for context, NC not comparable); "Coverage" is the abstract coverage available to the coder; "Cited in §" lists the manuscript sections that cite the row.

| **ID** | **Source** | **Family** | **Evidence** | **Comp.** | **Coverage** | **Peer-reviewed** | **Cited in §** |
|---|---|---|---|---|---|---|---|
| P1 | Guo et al. (2016) | Parametric | proof | NC | full | yes | 1.1, 2.1, 4.1 |
| P2 | Martini & Mingone (2022) | Parametric | proof | RC | full | yes | 2.1, 4.1 |
| P3 | Mingone (2022) | Parametric | proof | RC | full | yes | 4.1 |
| P4 | Corbetta et al. (2019) | Parametric | assumption | NC | metadata-only | yes | 4.1 |
| P5 | Zaugg et al. (2025) | Parametric | proof | RC | full | yes | 4.1 |
| P6 | Le Floc’h (2025) | Parametric | proof | RC | full | yes | 4.1 |
| P7 | Klassen (2016) | Parametric | assumption | NC | metadata-only | no [preprint] | 4.1 |
| P8 | Barski & Wiśniewolski (2026) | Parametric | proof | NC | full | no [preprint] | 2.2, 4.1, 6.2, 6.3 |
| N1 | Cao et al. (2020) | Penalty | numerical test | RC | full | yes | 2.3, 4.2 |
| N2 | Wiedemann et al. (2025) | Penalty | numerical test | RC | full | yes | 1.1, 4.2, 5.1 |
| N3 | Ackerer et al. (2019) | Penalty | numerical test | RC | full | no [preprint] | 4.2 |
| N4 | Sidogi et al. (2022) | Penalty | numerical test | RC | full | yes | 3.3, 4.2, 5.1, 5.2, 6.1 |
| N5 | Na et al. (2023) | Penalty | numerical test | RC | full | no [preprint] | 1.1, 3.3, 4.2, 5.1, 5.2, 6.1 |
| N6 | Hoshisashi et al. (2023) | Penalty | numerical test | RC | full | no [preprint] | 4.2, 5.1 |
| R1 | Cohen et al. (2020) | Repair | numerical test | RC | full | yes | 4.3 |
| R2 | De March & Henry-Labordère (2019) | Repair | proof | RC | partial | no [preprint] | 4.3 |
| R3 | Bender & Thiel (2020) | Repair | proof | NC | full | yes | 1.1, 2.3, 4.1, 4.3 |
| R4 | Yao et al. (2026) | Repair | assumption | NC | metadata-only | yes | 4.3 |
| R5 | Xiong & Liu (2026) | Repair | numerical test | RC | full | yes | 2.1, 3.3, 4.3, 5.1, 5.2, 5.3, 6.2, 6.3 |
| R6 | Buehler et al. (2026) | Repair | proof | RC | full | no [preprint] | 2.3, 4.1, 4.3 |
| R7 | Alvarez (2025) | Repair | numerical test | RC | full | no [preprint] | 4.3, 5.1, 5.3 |
| R8 | Zetocha (2023) | Repair | assumption | NC | full | no [preprint] | 4.3 |
| R9 | Madan & Schoutens (2019) | Repair | numerical test | RC | full | yes | 4.3 |
| G1 | Ning et al. (2023) | Generation | proof | RC | full | yes | 4.4, 5.1 |
| G2 | Vuletić & Cont (2024) | Generation | numerical test | RC | full | yes | 4.4 |
| G3 | Cont & Vuletić (2023) | Generation | assumption | RC | partial | yes | 4.4 |
| G4 | Ginart Belmonte & Cole (2025) | Generation | numerical test | RC | full | yes | 4.4 |
| G5 | Bajalica et al. (2026) | Generation | numerical test | RC | full | yes | 1.1, 2.1, 4.4, 5.1, 5.3, 6.2 |
| G6 | Anagha (2026) | Generation | proof | RC | full | no [preprint] | 2.1, 3.3, 4.4, 5.1, 5.2, 5.3, 6.1, 6.2 |
| G7 | Cohen et al. (2021) | Generation | proof | RC | full | yes | 2.2, 2.3, 4.4, 5.1, 6.2 |
| G8 | Yang et al. (2017) | Generation | proof | RC | full | yes | 4.4, 5.1 |
| C1 | Neufeld & Sester (2024) | Conditions | proof | RC | full | yes | 5.2, 6.3 |
| C2 | Niu (2015) | Conditions | assumption | NC | full | no [preprint] | 1.1, 2.2, 6.2 |
| C3 | Andrès et al. (2026) | Conditions | proof | RC | full | yes | 2.2, 2.3, 6.2, 6.3 |
| C4 | Fukasawa (2022) | Conditions | proof | NC | partial | yes | 2.1, 6.2 |
| C5 | Stahl & Blauth (2024) | Conditions | numerical test | NC | full | yes | 1.3, 2.2 |
| S1 | Gatheral & Jacquier (2013) | Seminal | proof | RC | partial | yes | 1.1, 2.1 |
| S2 | Fengler (2009) | Seminal | numerical test | NC | full | yes | 1.1, 4.3 |
| S3 | Hagan et al. (2014) | Seminal | numerical test | RC | full | no [preprint] | 2.1, 6.2 |
| S4 | Bodurtha & Jermakyan (1999) | Seminal | assumption | RC | full | yes | 4.3 |
| S5 | Fengler et al. (2006) | Seminal | assumption | RC | full | yes | 4.3 |

**Appendix B note.** Codes are the review's own; "evidence" and "comp." follow the Stage 1 ledger verbatim and no row was re-coded for this manuscript. Sections are listed as coded in the text, so a row cited twice in one section appears once.

## Appendix C. Coding Protocol, Instrument Reconciliation, and Boundary Cases

**What was coded.** Eight fields per row were recorded from title, abstract, and bibliographic metadata: family (P, N, R, G, C, S); evidence status (proof, numerical test, assumption); the static condition set expressed among SC1–SC5 (non-negative time value, monotone decreasing call prices in strike, strike convexity, the zero-maturity limit, and calendar monotonicity of total variance); whether the row engages a time axis and whether it enforces or tests a dynamic condition; quality level; the market or dataset named; the fit or accuracy metric reported; and the comparability class (DC, RC, NC). A claim is coded as evidence only where the abstract states it. A title-level claim is coded as unverified and is not used as evidence for any finding.

**Instrument reconciliation.** Stage 1 used an eight-axis evaluation instrument that added extrapolation and reproducibility to the seven axes of Table 6. This manuscript uses the seven-axis frame for two reasons: extrapolation and reproducibility were sparsely and inconsistently codeable at abstract level, and the seven-axis frame maps one-to-one onto the dimensions the corpus actually reports. The two instruments were compared row by row during Stage 1 revision; the seven-axis frame is the aggregation of the eight-axis coding, the reconciliation is recorded in the Stage 1 synthesis, and no count, verdict, or claim in this manuscript changes between them. The eight-axis record remains available in the run directory.

**Boundary cases.** Five rows sit across family borders and are retained with the friction disclosed rather than reassigned. R3 is a repair built on an admissible reference function, so its mechanism is closer to construction; it stays in R because the manuscript's repair locus is defined by the certified object, and R3 certifies its output. R6 claims a strict guarantee through parameter positivity, which is architecturally parametric, but its object is a completed surface, and it anchors the repair family's strict end. N1 enforces constraints architecturally, like the G-family rows, but its output is a single fitted surface rather than a generative model, which keeps it in N. G7 satisfies its constraints on a modelled state space and explicitly disclaims a dynamic-arbitrage guarantee, which is why it marks the static/dynamic boundary rather than a gap in it. C3 builds a path-dependent model whose surfaces are static-admissible but whose dynamic consistency is not discussed, so it is coded as conditions rather than as a dynamic test. A sixth row, C5, is a single-stock panel retained as a disclosed exception; it is the only longitudinal dynamic-adjacent evidence in the corpus and is never counted as index evidence.

**Single-analyst limit.** All coding, grading, and adjudication were performed by one analyst without dual screening or an adjudicator. The protocol above is written so that a second coder could reproduce the ledger, and the boundary cases are named so that disagreement would be locatable rather than diffuse, but no inter-coder agreement statistic exists for this corpus. A different coder applying the same rules would be expected to agree on the large counts (41 rows, 0 dynamic enforcement, 0 direct comparability, 6 audit rows, 1 proof-and-audit overlap) and could reasonably shift individual rows at the family borders.
