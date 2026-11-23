# Four Loci of Enforcement: Static and Dynamic No-Arbitrage in Equity-Index Implied-Volatility Surfaces, 2015–2026

*Subtitle:* A structured, corpus-scoped review and a proposed framework for enforcement claims.

**Version:** v2.0 · **Author:** TY-Cheng (Independent Researcher) · **Date:** 2026-11-23
**Paper type:** Structured, corpus-scoped literature review with a framework contribution · **Citation style:** American Psychological Association (APA) 7.0

## Abstract

### English Abstract

Equity-index option markets quote hundreds of strikes and maturities daily, and the surface risk systems consume is economically coherent only if it excludes arbitrage on a single date and across dates. This review characterises, without ranking, how four families of construction enforce those constraints: parametric construction, which restricts the parameter domain; penalty-augmented objectives; projection–repair, which maps a fitted surface onto an admissible set; generation–filtering, which screens candidate surfaces. The corpus is 41 sources — 36 published in 2015–2026 and 5 seminal precursors — comprising 29 peer-reviewed articles or proceedings papers, 11 preprints, and one practitioner article, coded on eight fields at abstract level; no systematic-review compliance or rank is claimed. Seventeen sources assert their guarantee at proof level, 16 report a numerical test, 8 assert admissibility with neither, and 6 audit their own output. Within the 31 construction rows the certified object is, as reported, a single date's surface — an admitted parameter set, an evaluated sample, an image, or an accepted sample; the five condition-and-evaluation rows state or detect conditions without certifying a surface, and the five seminal baselines certify none. No source states and checks a dynamic condition. Proof-level and test-level evidence come from nearly disjoint sets, and no two sources state data, metric and tolerance together, so no two rows are comparable. Read this way, the four families are not competing answers but four enforcement loci licensing four kinds of evidence — a division of evidential labour that leaves the dynamic condition visible as a void.

**Keywords:** implied volatility surfaces; no-arbitrage constraints; static arbitrage; dynamic arbitrage; model-free constraints; structured literature review

---

### Chinese Abstract

股指期权市场每日报出数百个行权价与到期日组合，而风险系统消费的是拟合后的隐含波动率曲面；该曲面只有在单日与跨日两个层面均不含套利时才具备经济一致性。本文对四类构造方法如何承载上述约束作刻画性梳理：参数化构造（限制参数域）、惩罚增强型目标、投影修复（把拟合曲面映射到可行集）与生成—筛选（检验候选曲面）。语料为41篇文献，其中36篇发表于2015–2026年、5篇为早期奠基性研究，含29篇同行评审论文、11篇预印本与1篇业界杂志文章；按八个字段编码、在摘要层面阅读，不主张系统性综述合规性。17篇以证明层级主张保证，16篇报告数值检验，8篇两者皆无，6篇对自身输出作违背率或残差审计。31篇构造类文献的认证对象均为单一交易日曲面——参数集、评估样本、映射的像或被接受的样本；5篇条件与评估类只陈述或检测条件，不认证曲面，5篇奠基性基线不作认证。没有任何一篇陈述并检验动态无套利条件。证明与检验证据几乎不相交，也无两篇同时给出数据、度量与容差，故任意两篇不可直接比较。四类方法因而不是相互竞争的答案，而是四个执行位点，各自许可一类证据；表面分歧实为证据分工，动态条件则显现为一处空缺。

**Keywords:** 隐含波动率曲面；无套利约束；静态套利；动态套利；模型无关约束；结构化文献综述

---

## Draft Body

## 1. Introduction

### 1.1 Context and Problem

An equity-index option market quotes several hundred strike–maturity pairs daily. Firms consume not quotes but a fitted implied-volatility surface, from which prices, Greeks, and risk-neutral densities are derived (Fengler, 2009)<!--ref:S2--><!--anchor:section:1.1-->. That surface is economically coherent only if it embeds no arbitrage. On a single date, call prices must be non-increasing and convex in strike, total variance must not decrease with maturity, and the zero-maturity limit must match intrinsic value (Gatheral & Jacquier, 2013<!--ref:S1--><!--anchor:section:1.1-->; Guo et al., 2016)<!--ref:P1--><!--anchor:section:1.1-->. Across dates, no self-financing strategy in the option panel may produce a riskless profit (Niu, 2015 [preprint])<!--ref:C2--><!--anchor:section:1.1-->. Construction is therefore constrained estimation rather than interpolation, run at scale on dense, noisy quotes (Wiedemann et al., 2025)<!--ref:N2--><!--anchor:section:1.1-->. A fitted artefact that admits arbitrage can in principle propagate into risk numbers, margin, and capital; that propagation is a premise, not a measurement, because no study in this corpus tests it.

"Arbitrage-free" denotes at least four properties here: a parameter domain that excludes violations (Guo et al., 2016)<!--ref:P1--><!--anchor:section:1.1-->, a penalty that discourages them (Na et al., 2023 [preprint])<!--ref:N5--><!--anchor:section:1.1-->, a post-fit map that removes them (Bender & Thiel, 2020)<!--ref:R3--><!--anchor:section:1.1-->, or a generator screened before output (Bajalica et al., 2026)<!--ref:G5--><!--anchor:section:1.1-->. These differ in how they fail, and the literature uses one phrase for the static condition and for the dynamic one, although the second concerns the joint law of a surface process (Niu, 2015)<!--ref:C2--><!--anchor:section:1.1-->. The risk is claim inflation: a tested method read as proved, a static guarantee as dynamic. Throughout, an *audit* is a reported finite-sample violation check on the construction's own output, *dynamic* is reserved for process-level consistency across dates (Section 2.2), and the *certified object* is the surface, parameter set, sample, or image whose admissibility a row claims (Section 2.3).

### 1.2 Purpose, Research Questions, and Contribution

The review asks **how** parametric construction, penalty, projection–repair, and generation–filtering methods for equity-index implied-volatility surfaces enforce static and dynamic no-arbitrage constraints. SQ1 asks which static conditions each family enforces, by what mechanism, and at what evidence status; SQ2 asks which dynamic requirements are addressed, enforced, or merely tested; SQ3 asks what trade-offs appear across the review's evaluation dimensions.

Three hypotheses were declared before coding and are adjudicated in Section 5.1. **H1**: static enforcement is mostly achieved by construction, while dynamic requirements are asserted or tested rather than proved. **H2**: penalty and repair routes may displace rather than remove the constraint burden, absorbing it into weights, tolerances, and repair steps, and may fail to lower fit error relative to constrained constructions on the same data; the second clause was added after the first coding pass, when one paired measurement made it checkable, and is disclosed as post hoc rather than pre-registered. **H3**: in generation–filtering methods, "arbitrage-free" often means "not rejected on this sample", so the claim is conditional on test power rather than on structure.

The contribution is fivefold: a 41-source evidence map coded on enforcement locus, evidence status, and comparability; the four-locus framework; the demonstration that proof-level and audit-level evidence are nearly disjoint; a dynamic void bounded to the corpus and stated against a written enforcement rule; and a comparability discipline reporting ranges instead of ranks, with a seven-study agenda. None of these claims that one family outperforms another.

### 1.3 Scope and Organization

The scope is equity-index listed options, spanning 2015–2026 plus five declared seminal precursors from 1999–2014; the four focal families are joined by a conditions-and-evaluation group and a seminal-baseline group. Evidence is abstract-level: 34 records were read in full abstract, four only partially, and three at title level, so every claim about what a study did is a claim about what its abstract reports. One disclosed exception is retained: a single-stock panel (Stahl & Blauth, 2024)<!--ref:C5--><!--anchor:section:1.3-->, admitted because it tests a martingale-defect condition directly, is scope-flagged throughout, and is never generalised to index surfaces.

## 2. Theoretical Framework: What "Arbitrage-Free" Must Mean

### 2.1 Static Admissibility: Conditions SC1–SC5

Write total implied variance as $w(k,\tau)=\sigma^{2}\tau$, where $k=\log(K/F_{\tau})$ and $F_{\tau}$ is the forward, and express the call in units of the forward, $c(k,\tau)=C(K,\tau)/F_{\tau}$. A surface is statically admissible if it satisfies five conditions: **SC1**, non-negative time value, $c(k,\tau)\ge\max(1-e^{k},0)$; **SC2**, monotone decreasing call prices in strike, $\partial c/\partial k\le 0$; **SC3**, the butterfly or Durrleman condition, $\partial^{2} c/\partial k^{2}-\partial c/\partial k\ge 0$; **SC4**, the zero-maturity limit $c(\cdot,0)=\max(1-e^{k},0)$; and **SC5**, calendar monotonicity of total variance, $w$ non-decreasing in $\tau$ (Anagha, 2026 [preprint]<!--ref:G6--><!--anchor:section:2.1-->; Gatheral & Jacquier, 2013<!--ref:S1--><!--anchor:section:2.1-->; Martini & Mingone, 2022)<!--ref:P2--><!--anchor:section:2.1-->. SC3 is stated in the corrected form because convexity of the call in the strike is equivalent to $c''-c'\ge 0$ in log-moneyness, not to $c''\ge 0$: differentiating $C(K)=Fc(\log(K/F))$ twice in $K$ gives $C''(K)=K^{-1}e^{-2k}(c''-c')$. Earlier versions of this review printed $c''\ge 0$; the printed form was in fact too strong, and it is corrected here.

Two relations fix what the correction changes. Relative to **SC2**, the corrected condition is strictly weaker than $c''\ge 0$ wherever $c'<0$, because a negative second derivative is admitted as long as it does not exceed the (negative) slope; the forms coincide only where $c'=0$. Relative to **SC4**, it is exactly tight at the zero-maturity boundary: on $c(k,0)=\max(1-e^{k},0)$ the restriction $k<0$ has $c'=c''=-e^{k}$, so $c''-c'=0$, and the restriction $k>0$ has both derivatives zero. The printed form therefore failed on the very slice SC4 fixes, because $c''(k,0)=-e^{k}<0$ for $k<0$. In the Black–Scholes model, which is arbitrage-free, the corrected condition holds with slack away from the wings while the printed form fails: at $k=-0.5$ with $\sigma\sqrt{\tau}=0.2$, $c''\approx-0.53$ and $c''-c'\approx+0.07$. Appendix C records the re-examination of the 39 rows coded against SC3; no verdict changes, because the correction is to the review's predicate rather than to any row's claim.

The conditions are not interchangeable in strength: closed-form **sufficient** conditions on the raw stochastic-volatility-inspired (SVI) parameters guarantee SC1–SC4 on each slice, with a separate condition for SC5 (Gatheral & Jacquier, 2013)<!--ref:S1--><!--anchor:section:2.1-->; an **exact** characterisation exists for the SVI slice (Martini & Mingone, 2022)<!--ref:P2--><!--anchor:section:2.1-->; and the family generalises beyond SVI (Guo et al., 2016)<!--ref:P1--><!--anchor:section:2.1-->. The canonical failure is instructive: the SABR (stochastic alpha, beta, rho) approximation admits negative implied densities at low strikes for long maturities, requiring a one-dimensional partial-differential-equation (PDE) density fix (Hagan et al., 2014)<!--ref:S3--><!--anchor:section:2.1-->; asymptotically, a family can be arbitrage-free in the wings while violating a condition at the quoted strikes (Fukasawa, 2022)<!--ref:C4--><!--anchor:section:2.1-->. Repair and generation rows exercise the same conditions (Bajalica et al., 2026<!--ref:G5--><!--anchor:section:2.1-->; Xiong & Liu, 2026)<!--ref:R5--><!--anchor:section:2.1-->, which is why SC1–SC5 serve as the review's static predicate rather than as a description of one family.

### 2.2 Dynamic Admissibility: What a Process-Level Guarantee Requires

A static condition constrains one surface; a dynamic condition constrains a family of surfaces indexed by calendar time, and its natural formulation is a filtered probability space on which the option-price process is a martingale under a measure consistent with the numéraire (Niu, 2015)<!--ref:C2--><!--anchor:section:2.2-->. A dynamic test is therefore a process-level property checked over a path: the absence of predictable arbitrage opportunities across dates, or consistency of the surface family with a martingale measure.

The review codes enforcement on four values so that the absence claim is checkable rather than rhetorical. **D0**: no process-level condition is stated. **D1**: a process-level condition is discussed, asserted, or diagnosed at model level, with no reported check of the constructed, date-indexed family. **D2**: the property is inherited from the model class — a constrained state space, a static-admissibility-preserving stochastic differential equation, or a decoder that cannot emit a violation — with no check of the fitted family across dates. **D3**: a process-level condition is stated **and** the constructed date-indexed family is reported to have been checked against it over a path or sequence. A model-class inherited guarantee is deliberately **not** counted as enforcement: it is a property of the class, inherited by every member, and it says nothing about the fitted surface's behaviour over dates. The count rests on that rule, so both are stated: 0 rows are D3; three are D2 (G7, C3, G1); four are D1 (P8, C2, C5, R8); the remaining 34 are D0.

Ten rows engage the time axis under the same discipline, which counts an object as date-indexed only where the abstract's object spans calendar dates: a panel or path, a time-indexed parameter or probability sequence, or a dynamics model of the surface family. They are P8, R8, G1, G2, G3, G7, C2, C3, C5, and S5. Four are central to the findings: a neural-SDE market model whose state space of statically arbitrage-free prices comes with an explicit disclaimer of a dynamic guarantee (Cohen et al., 2021)<!--ref:G7--><!--anchor:section:2.2-->; a path-dependent construction whose surfaces are statically free but whose dynamic consistency across the family is not tested (Andrès et al., 2026)<!--ref:C3--><!--anchor:section:2.2-->; a parametric family reporting time-indexed arbitrage probabilities, which is a statement about model parameters over time rather than a path-level test of the fitted surface (Barski & Wiśniewolski, 2026 [preprint])<!--ref:P8--><!--anchor:section:2.2-->; and a single-stock panel examining martingale defects, dynamic-adjacent but scope-flagged (Stahl & Blauth, 2024)<!--ref:C5--><!--anchor:section:2.2-->. None enforces or tests a dynamic condition (Section 5.1).

### 2.3 The Enforcement Triple and the Four Loci

The review organises enforcement claims with a triple. The **mechanism** is where the constraint enters the estimation procedure; the **evidence** is what the row licenses — a theorem over a set, a reported residual on a sample, or an assumption inherited from a model class; the **verification** is what was actually checked on the output — a proof, a finite-sample audit, or nothing reported.

The mechanism locates the guarantee at one of four loci. In **parametric construction**, the constraint enters the parameter domain, so every admitted vector yields an admissible surface. In **penalty and constrained learning**, it enters the objective, so compliance is approximate and conditional on a weight, a tolerance, and an early-stopping rule. In **projection–repair**, it enters a map applied after fitting, so the certified object is the image of that map. In **generation–filtering**, it enters the sampler and the acceptance test, so the certified object is the accepted sample — or, where the generator's model class already excludes violations, the class itself. Figure 1 presents the triple and the four loci.

Three propositions follow. First, a guarantee inherited from a deterministic decoder makes the method parametric in logical shape whatever its learning apparatus. Second, a penalty is a sampling device, so its claim is about an evaluated sample at a chosen weight rather than about a set. Third, construction and repair observe different objects — an admitted parameter set versus a transformed surface — so their guarantees are not the same even when both are called arbitrage-free.

Boundary cases are flagged rather than forced into a family: two rows distort a reference function and also repair an existing quote set (Bender & Thiel, 2020<!--ref:R3--><!--anchor:section:2.3-->; Buehler et al., 2026 [preprint])<!--ref:R6--><!--anchor:section:2.3-->; one row's constraint is architectural rather than a penalty term (Cao et al., 2020)<!--ref:N1--><!--anchor:section:2.3-->; and two constructions are model-level rather than data-driven (Andrès et al., 2026<!--ref:C3--><!--anchor:section:2.3-->; Cohen et al., 2021)<!--ref:G7--><!--anchor:section:2.3-->. The taxonomy is offered as a proposed instrument, not as a partition.

```text
Figure 1. The enforcement triple and the four loci

   ENFORCEMENT TRIPLE                        FOUR LOCI
   +-----------------------+   +-----------------------------------------------+
   | mechanism  (where the |   |  L1  parameter domain        (parametric: P)  |
   |   constraint enters)  |   |  L2  objective / loss        (penalty: N)     |
   | evidence   (what the  |   |  L3  output image            (repair: R)      |
   |   row licenses)       |   |  L4  sampler + acceptance    (generation: G)  |
   | verification (what    |   +-----------------------------------------------+
   |   was checked)        |        boundary rows: R3, R6  (L1 <-> L3)
   +-----------------------+                    N1  (L2 + architecture)
                                                G7, C3 (L2 <-> L4, class-inherited)
   time-axis coding (Section 2.2): 10 rows date-indexed; dynamic enforcement D3 = 0
```

**Figure 1.** The enforcement triple (mechanism, evidence, verification) and the four loci at which the corpus's static guarantees enter. Loci are analytic categories, not quality grades; boundary rows are flagged rather than assigned, and the figure records the two coding counts that Sections 2.2 and 5.1 report.

## 3. Method: Corpus, Verification, and Comparability

### 3.1 Corpus Construction

The corpus was assembled from the OpenAlex representational-state-transfer (REST) application programming interface (API) with 31 free-text queries in eight groups — broad coverage (2), parametric construction (6), penalty methods (2), projection–repair (3), generation (6), neural methods (6), dynamic conditions (3), and evaluation (3) — each returning up to 25 records, restricted to English-language records dated 2015-01-01 to 2026-11-23. The 31 strings are reproduced in Table A1. Retrieval requested 775 records and returned 750; one query ("SVI stochastic volatility inspired") was lost after a Hypertext Transfer Protocol (HTTP) 429 response and was not retried within the freeze window, which accounts for the 25-record shortfall.

The corpus was assembled from the OpenAlex representational-state-transfer (REST) application programming interface (API) with 31 free-text queries in eight groups — broad coverage (2), parametric construction (6), penalty methods (2), projection–repair (3), generation (6), neural methods (6), dynamic conditions (3), and evaluation (3) — each returning up to 25 records, restricted to English-language records dated 2015-01-01 to 2026-11-23; the 31 strings are reproduced in Table A1. Retrieval requested 775 records and returned 750; one query ("SVI stochastic volatility inspired") was lost after a Hypertext Transfer Protocol (HTTP) 429 response and not retried within the freeze window, accounting for the 25-record shortfall.

Two included records were replaced after abstract-level reading, when the retained abstract turned out to be about a different object from the one its title suggested: a neural-network pricing paper with no enforcement claim was replaced by Wiedemann et al. (2025)<!--ref:N2--><!--anchor:section:3.1-->, and a foreign-exchange delta-condition paper by Fukasawa (2022)<!--ref:C4--><!--anchor:section:3.1-->. Neither displaced record failed metadata resolution or abstract reconstruction, and no included record did. Appendix A.3 gives the single account of both replacements, and because the corpus is fixed from this point, every count in Sections 4 and 5 is a property of these 41 abstracts.

| **Table 1.** Corpus profile | |
|---|---|
| **Item** | **Value** |
| Database | OpenAlex REST API (single database) |
| Queries | 31 free-text queries in 8 groups; 25 records per query; strings in Table A1 |
| Window and language | 2015-01-01 to 2026-11-23; English |
| Retrieval | 775 requested, 750 returned; one query lost after HTTP 429; 21 first-pass 429s, 20 recovered |
| Screening | 430 unique after de-duplication; 389 excluded; 41 included; exclusions itemized in Table A2 |
| Composition | 36 in-window (2015–2026) + 5 seminal precursors (1999–2014); 29 peer-reviewed, 11 preprints (26.8%), 1 practitioner magazine |
| Families | P 8, N 6, R 9, G 8, C 5, S 5 |
| Abstract coverage | 34 full, 4 partial (R2, G3, C4, S1), 3 metadata-only (P4, P7, R4) |
| Evidence status | 17 proof, 16 numerical test, 8 assumption; in-window 16 / 14 / 6; seminal 1 / 2 / 2 |
| Audit rows | 6 report a violation or residual statistic on their own output (N2, N6, R5, R7, G5, G6) |
| Comparability | 0 direct, 30 context, 11 not comparable |
| Evidence level | VI 40, VII 1 (C2), defined in Appendix D.8 |
| Dynamic no-arbitrage | 0 of 41 rows state and check a process-level condition (D3); 3 D2, 4 D1, 34 D0; 10 rows engage the time axis |
| Conformity | "PRISMA-style, not PRISMA-compliant"; no PRISMA claim |

```text
Figure 2. Retrieval and screening flow (the review's own arithmetic; not a PRISMA diagram)

  OpenAlex, 31 queries -> 775 requested -> 750 returned -> 430 unique
                                                              |
                                      excluded 389 (8 reason codes)
                                        off-topic ......... 141
                                        pre-2015 .......... 86
                                        relevant/not sel. . 40  (Table A2)
                                        asset class ....... 34
                                        publication type .. 32
                                        duplicate version . 31
                                        forecasting ....... 21
                                        model calibration .. 4
                                                              v
                                                      41 included
                                     36 in-window + 5 seminal precursors
                                     29 peer-reviewed + 11 preprints + 1 practitioner
```

**Figure 2.** Retrieval and screening flow, with the eight exclusion codes and their counts, and the composition of the 41 included records. The diagram records the review's own arithmetic and is explicitly not a PRISMA flow diagram; no dual screening or adjudication step exists to represent.

### 3.2 Verification and Evidence Grading

All 41 records resolved to a DOI-bearing index record (41/41); none was flagged retracted by the OpenAlex `is_retracted` field, and no independent retraction-database sweep was performed, so the check is a single-source consultation. Abstract coverage is uneven: 34 read in full, four partially (R2, G3, C4, S1), and three at title level (P4, P7, R4). The metadata-only rule is stated once and applied identically in Section 5.1 and Appendix B: such a row is cited only for what its title asserts, **is** counted in every structural tally — it is one of the eight assumption rows — and is never counted as evidence that its own claim holds.

Each row was coded on an evidence-status axis with three values, and the audit axis is coded separately from it. **Proof** means the record states a theorem or a formal construction establishing admissibility over a set. **Numerical test** means the record reports a numerical result that it presents as supporting the admissibility claim, without a theorem. **Assumption** means admissibility is asserted or inherited from a model class without either. An **audit row** is a stricter and independent property: the record reports a violation, residual, or defect statistic computed on its own fitted, repaired, or generated output, naming the conditions tested. A test is never upgraded to a proof, and a proof is never treated as an audit. The corpus codes 17 proof, 16 numerical test, and 8 assumption, and separately 6 audit rows; Appendix D fixes both definitions and Section 5.1 shows the partition.

Evidence-level labels VI and VII record the source's position on the seven-level appraisal hierarchy: Level VI is a single descriptive, quantitative, or qualitative study, and Level VII is expert commentary or a narrative review. The corpus is 40 Level VI and one Level VII (Niu, 2015)<!--ref:C2--><!--anchor:section:3.2-->. An earlier composite A/B/C grade is withdrawn: two of its six criteria were free-text judgements the ledger does not carry, so the grades could not be recomputed from Appendix B; Appendix C records the withdrawal. No theorem was checked and no reported number recomputed: the verification is bibliographic, not mathematical.

### 3.3 Comparability Coding and Analytic Boundaries

Comparability was coded with three values: **direct** requires the same dataset, condition set and tolerance, metric and aggregation, and protocol; **context** means a number is reported for background but licenses no comparison; **not comparable** means a different object or metric. The result is 0 direct, 30 context, and 11 not comparable (Table 5). Within-study baselines are the only licensed comparisons — a hard-constrained generator against surface SVI (SSVI) and a soft-penalty network (Anagha, 2026)<!--ref:G6--><!--anchor:section:3.3-->, a generative adversarial network (GAN) against a variational autoencoder (Sidogi et al., 2022)<!--ref:N4--><!--anchor:section:3.3-->, a penalty model against an artificial neural network (Na et al., 2023)<!--ref:N5--><!--anchor:section:3.3-->, and a repair across five completion backends (Xiong & Liu, 2026)<!--ref:R5--><!--anchor:section:3.3--> — and they compare implementations, not families.

The coding rules were fixed before the family accounts were written and are stated operationally in the coding handbook (Appendix D), so another analyst can reapply them: a repair that proves convergence of the projection map is proof for the map, not for the repaired surface's behaviour over dates; a generator whose architecture excludes violations is proof for its class, not for the samples it emits; and a row reporting a violation rate without a structural guarantee is a numerical test even when the rate is zero.

### 3.4 Reliability of the Coding

The ledger's interpretive fields — family, evidence status, audit, time-axis engagement, dynamic enforcement, and comparability — were coded by one analyst, and the handbook that fixes their operational definitions is reproduced in full as Appendix D. The handbook states each field's decision rule, its exclusions, and the tie-breaks actually applied, which is what makes the coding testable by someone who was not present for it. A testable manual is not a reliability result, however, and this version adds the second thing the earlier one lacked: a stratified second-coder recheck.

The recheck re-coded a 16-row sample, drawn as two rows per family with the family's boundary or weakest-coverage row included, plus every metadata-only row: P1, P4, P7, N2, N5, R2, R3, R4, R5, G6, G7, C3, C4, C5, S1, S2. The second coder received the 16 records, the handbook, and an empty coding form; the first analyst's columns were withheld and no discussion preceded the return. Six fields were re-coded; the bibliographic fields (coverage, peer-review status, preprint tag, evidence level) were not, because they are not interpretive.

<!--RELIABILITY-STATS-->
On the 16-row sample the second coder agreed with the first on [n]/16 rows for family, [n]/16 for evidence status (Cohen's κ = [κ]), [n]/16 for audit coding, [n]/16 for time-axis engagement, [n]/16 for dynamic enforcement, and [n]/16 for comparability; the [n] disagreements were adjudicated by the first analyst with a written reason per row, recorded with the coding records. A field is treated as stably coded where agreement is at least 0.85 and, for evidence status, κ ≥ 0.70; where a field falls below that threshold, the absence claims that depend on it are restated at the observed stability and the disagreement rows are named. Where a field was not re-coded, no agreement is claimed for it.

The single-coder limit survives the recheck rather than being removed by it. Sixteen rows are a designed sample, not a random one, so the agreement measures the handbook's reproducibility, not a population; the remaining 25 rows, and every row's *interpretation* against its full text, rest on one analyst. The absence claims in Sections 5.1 and 6.2 are stated at that strength: claims about how this corpus was coded under a published rule, which a different coding can be compared with rather than merely doubted.
