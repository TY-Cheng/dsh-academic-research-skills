# Four Loci of Enforcement: Static and Dynamic No-Arbitrage in Equity-Index Implied-Volatility Surfaces, 2015–2026

*Subtitle:* A structured, corpus-scoped review and a proposed framework for enforcement claims.

**Version:** v2.0 · **Author:** TY-Cheng (Independent Researcher) · **Date:** 2026-11-23
**Paper type:** Structured, corpus-scoped literature review with a framework contribution · **Citation style:** American Psychological Association (APA) 7.0

## Abstract

### English Abstract

Equity-index option markets quote hundreds of strikes and maturities daily, and the surface risk systems consume is economically coherent only if it excludes arbitrage on a single date and across dates. This review characterises, without ranking, how four families of construction enforce those constraints: parametric construction, which restricts the parameter domain; penalty-augmented objectives; projection–repair, which maps a fitted surface onto an admissible set; generation–filtering, which screens candidate surfaces. The corpus is 41 sources — 36 published in 2015–2026 and 5 seminal precursors — comprising 29 peer-reviewed articles or proceedings papers, 11 preprints, and one practitioner article, coded on eight fields at abstract level, with a 16-row blind recheck of the interpretive fields reported; no systematic-review compliance or rank is claimed. Seventeen sources assert their guarantee at proof level, 16 report a numerical test, 8 assert admissibility with neither, and 6 audit their own output. Within the 31 construction rows the certified object is, as reported, a single date's surface — an admitted parameter set, an evaluated sample, an image, or an accepted sample; the five condition-and-evaluation rows state or detect conditions without certifying a surface, and the five seminal baselines certify none. No source states and checks a dynamic condition. Proof-level evidence and audit evidence come from nearly disjoint sets — one of the six audit rows is also proof-level — and no two sources state data, metric and tolerance together, so no two rows are directly comparable. Read this way, the four families are not competing answers but four enforcement loci licensing four kinds of evidence — a division of evidential labour that leaves the dynamic condition visible as a void.

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

Write total implied variance as $w(k,\tau)=\sigma^{2}\tau$, where $k=\log(K/F_{\tau})$ and $F_{\tau}$ is the forward, and express the call in units of the forward, $c(k,\tau)=C(K,\tau)/F_{\tau}$. A surface is statically admissible if it satisfies five conditions: **SC1**, non-negative time value, $c(k,\tau)\ge\max(1-e^{k},0)$; **SC2**, monotone decreasing call prices in strike, $\partial c/\partial k\le 0$; **SC3**, the butterfly or Durrleman condition, $\partial^{2} c/\partial k^{2}-\partial c/\partial k\ge 0$; **SC4**, the zero-maturity limit $c(\cdot,0)=\max(1-e^{k},0)$; and **SC5**, calendar monotonicity of total variance, $w$ non-decreasing in $\tau$ (Anagha, 2026 [preprint]<!--ref:G6--><!--anchor:section:2.1-->; Gatheral & Jacquier, 2013<!--ref:S1--><!--anchor:section:2.1-->; Martini & Mingone, 2022)<!--ref:P2--><!--anchor:section:2.1-->. SC3 is stated in the corrected form because convexity of the call in the strike is equivalent to $c''-c'\ge 0$ in log-moneyness, not to $c''\ge 0$: differentiating $C(K)=Fc(\log(K/F))$ twice in $K$ gives $C''(K)=K^{-1}e^{-k}(c''-c')$. Earlier versions of this review printed $c''\ge 0$; the printed form was in fact too strong, and it is corrected here.

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

Comparability was coded with three values: **direct** requires the same dataset, condition set and tolerance, metric and aggregation, and protocol; **context** means a number is reported for background but licenses no comparison; **not comparable** means a different object or metric. The result is 0 direct, 30 context, and 11 not comparable (Table 5). On the blind recheck this field agreed in 10 of 16 sampled rows, every dispute a context-versus-not-comparable refinement; no coder assigned direct, so the zero-direct result stands. Within-study baselines are the only licensed comparisons — a hard-constrained generator against surface SVI (SSVI) and a soft-penalty network (Anagha, 2026)<!--ref:G6--><!--anchor:section:3.3-->, a generative adversarial network (GAN) against a variational autoencoder (Sidogi et al., 2022)<!--ref:N4--><!--anchor:section:3.3-->, a penalty model against an artificial neural network (Na et al., 2023)<!--ref:N5--><!--anchor:section:3.3-->, and a repair across five completion backends (Xiong & Liu, 2026)<!--ref:R5--><!--anchor:section:3.3--> — and they compare implementations, not families.

The coding rules were fixed before the family accounts were written and are stated operationally in the coding handbook (Appendix D), so another analyst can reapply them: a repair that proves convergence of the projection map is proof for the map, not for the repaired surface's behaviour over dates; a generator whose architecture excludes violations is proof for its class, not for the samples it emits; and a row reporting a violation rate without a structural guarantee is a numerical test even when the rate is zero.

### 3.4 Reliability of the Coding

The ledger's interpretive fields — family, evidence status, audit, time-axis engagement, dynamic enforcement, and comparability — were coded by one analyst, and Appendix D reproduces the handbook that fixes their operational definitions: each field's decision rule, exclusions, and the tie-breaks applied, which makes the coding testable by someone who was not present for it. A testable manual is not a reliability result, so this version adds the second coder.

The recheck re-coded a 16-row sample, drawn as two rows per family with the family's boundary or weakest-coverage row included, plus every metadata-only row: P1, P4, P7, N2, N5, R2, R3, R4, R5, G6, G7, C3, C4, C5, S1, S2. The second coder received the 16 records, the handbook, and an empty coding form; the first analyst's columns were withheld and no discussion preceded the return. Six fields were re-coded; the bibliographic fields (coverage, peer-review status, preprint tag, evidence level) were not, because they are not interpretive.

On the 16-row sample the second coder agreed with the first on 12/16 rows for family, 10/16 for evidence status (κ = 0.47), 15/16 for audit coding, 16/16 for time-axis engagement, 16/16 for dynamic enforcement, and 10/16 for comparability — 79 of 96 field codes (82.3%). The 17 cell disagreements were adjudicated with a written reason per row; the ledger was not changed, and the record sits with the coding records. A field is stably coded where agreement is at least 0.85 and, for evidence status, κ ≥ 0.70: time-axis and dynamic enforcement clear the bar, audit clears it on agreement, and family (0.750), evidence status (0.625) and comparability (0.625) do not; the claims resting on the three failing fields are restated at that strength below and in Sections 3.3 and 5.1. Where a field was not re-coded, no agreement is claimed for it.

The single-coder limit survives the recheck. Sixteen rows are a designed sample, so the agreement measures the handbook's reproducibility, not a population; the remaining 25 rows, and every row's *interpretation* against its full text, rest on one analyst. Sections 5.1 and 6.2 state their absence claims at that strength.

## 4. Findings I: How Each Family Enforces Static Admissibility

### 4.1 Parametric Construction

Parametric construction puts the constraint in the parameter domain: the family is parameterised so that every admitted vector yields a surface satisfying the stated conditions, and estimation is restricted to that set. Table 2 summarises the four focal families, with the two supporting groups shown for completeness. Family attribution is the review's coding: the blind recheck agreed on 12 of 16 and disputed only P/N/C boundary rows (P7, G6, G7, C3), flagged in Appendix C.

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

The corpus splits into 17 proof-level rows, 16 numerical-test rows, and 8 assumption rows; the in-window records split 16 / 14 / 6 and the seminal precursors 1 / 2 / 2, and Table 3 gives the family breakdown. The blind recheck agreed on this field in 10 of 16 cases (κ = 0.47), concentrating the disputes where an abstract describes a guarantee without stating a theorem, so the distribution is a coding result, not a reproducible classification. The distribution follows the loci: a parameter domain licenses a theorem, an objective a sample, a map a statement about the map, a sampler a pass rate.

Six rows audit their own output: a graph neural operator reporting adherence on ten years of intraday data (Wiedemann et al., 2025)<!--ref:N2--><!--anchor:section:5.1-->, a deep network with derivative constraints on simulated data (Hoshisashi et al., 2023)<!--ref:N6--><!--anchor:section:5.1-->, a repair reporting a 5.4% butterfly floor (Xiong & Liu, 2026)<!--ref:R5--><!--anchor:section:5.1-->, a Chebyshev construction reporting under 1% violations (Alvarez, 2025)<!--ref:R7--><!--anchor:section:5.1-->, a flow-matching generator reporting a 90.8% pass rate (Bajalica et al., 2026)<!--ref:G5--><!--anchor:section:5.1-->, and a hard-constrained generator reporting 0.00% at $10^{-4}$ over 15 runs (Anagha, 2026)<!--ref:G6--><!--anchor:section:5.1-->. The two axes are counted separately, and the blind recheck disputed one audit code (N2), whose abstract reports adherence figures. The partition recomputes from the Audit column of Appendix B: 16 proof rows audit nothing and one audits its own output; 5 test rows audit their own output and 11 report a numerical result that is not a violation statistic on that output; 8 assumption rows audit nothing. Hence 16 + 1 + 5 + 11 + 8 = 41 rows and 1 + 5 = 6 audit rows. Proof and audit are nearly disjoint in exactly one sense: one of the six audit rows is also proof-level, and one of the 17 proof rows reports a violation rate on its own output. Those are the same fact stated from either side; the earlier 17 / 6 / 1 partition is that fact, not a third count.

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

## 6. Discussion: Four Meanings, the Dynamic Void, and an Agenda

### 6.1 Four Meanings of One Word

The findings resolve "arbitrage-free" into four claims stated with one phrase: a theorem over an admitted parameter set in parametric construction; an objective minimised to a tolerance on an evaluated sample in penalty methods; an output mapped onto an admissible set in projection–repair; an accepted sample, or a model class that cannot emit a violation, in generation–filtering. These differ in what is quantified over, and comparing them without that distinction compares a theorem with a sample.

The remedy is the reporting triple of Section 2.3: state the condition enforced (SC1–SC5 or a dynamic condition), the tolerance (numerical or exact), and the verification mode (proof, test, or assumption). A surface is then admissible under a named condition at a stated tolerance by a stated mode, and a reader can see which element is missing. One row reports all three, on synthetic data (Anagha, 2026)<!--ref:G6--><!--anchor:section:6.1-->, showing the triple is reportable rather than idealised.

### 6.2 The Dynamic Void and Calendar Conflation

The absence of dynamic enforcement is the review's most consequential finding and its most fragile one. It is not a proof that the field ignores dynamics; it is a bounded statement about 41 abstracts. To our knowledge, based on searches of OpenAlex covering 2015-01-01 to 2026-11-23, as of 2026-11-23 no included study states and tests a process-level dynamic no-arbitrage condition for an equity-index implied-volatility surface; the nearest prior work reviews the conditions without testing them (Niu, 2015)<!--ref:C2--><!--anchor:section:6.2-->.

Two explanations are consistent with the result and the review cannot distinguish them: a genuine gap, since visible rewards attach to static construction and a dynamic test requires a multi-date panel and a protocol no row reports; or a retrieval and vocabulary effect, since studies may test dynamic properties under uncaptured labels or abstracts may omit a test the full text reports. Choosing one would convert an absence into an inference the evidence cannot support.

The excluded pool was audited for the second reading, and the audit bounds it rather than removing it. Of the 40 discretionary exclusions itemized in Table A2, eight titles carry time, forecasting, martingale, or chain-consistency vocabulary (log indices 5, 17, 58, 111, 326, 335, 342, 393); five are forecasting or hedging papers, whose object is the forecast rather than the enforcement claim coded here, and the other three model or reconstruct a surface from martingale structure without announcing a path-level test. All eight sit in the discretionary class, so their exclusion is a selection judgement rather than a rule-based screen. The finding is title-level only: the excluded records were never read at abstract level, so the pool can neither support the void claim nor by itself overturn it; what it can show is that the review did not knowingly discard a record whose title announced the test it reports as absent.

Calendar conflation is the main reason the gap is easy to miss. SC5 is a static condition on the maturity axis of one surface, but it is routinely called "calendar arbitrage", a phrase that sounds dynamic. A generator that constrains maturity monotonicity has made a static claim (Anagha, 2026<!--ref:G6--><!--anchor:section:6.2-->; Bajalica et al., 2026)<!--ref:G5--><!--anchor:section:6.2-->, as has a repair that enforces it (Xiong & Liu, 2026)<!--ref:R5--><!--anchor:section:6.2-->. The neural-SDE row explicitly disclaims dynamics (Cohen et al., 2021)<!--ref:G7--><!--anchor:section:6.2-->; the review that treats dynamic conditions at length does not test them (Niu, 2015)<!--ref:C2--><!--anchor:section:6.2-->; and the path-dependent and time-indexed constructions build objects along a time axis without a process-level test (Andrès et al., 2026<!--ref:C3--><!--anchor:section:6.2-->; Barski & Wiśniewolski, 2026)<!--ref:P8--><!--anchor:section:6.2-->. Because the three model-class rows (G7, C3, G1) are coded inherited rather than enforcement under the rule of Section 2.2, the count does not rest on a reader's intuition about what "the model is arbitrage-free" implies.

### 6.3 A Priced-Trade-Off Research Agenda

The gaps convert into seven studies, each tied to a measurable outcome, a claim it would falsify, and the data access and owner the sequence requires. All are proposals; none is reported as done here.

The first is a **test-power and noise-floor study**, estimating the false-positive and false-negative rates of the violation tests the corpus reports and separating data noise from method error, with the 5.4% repair floor as its motivating case (Xiong & Liu, 2026)<!--ref:R5--><!--anchor:section:6.3-->. It runs first because four of the five acceptance-criterion inputs of Section 5.4 depend on it; it needs only quoted index panels and a tolerance sweep, and its owner is whoever holds this review's coding records.

The second is a **dynamic enforcement test**, depending on the first for the tolerance at which a path-level violation would count. Starting from a surface family with a stated process (Andrès et al., 2026<!--ref:C3--><!--anchor:section:6.3-->; Barski & Wiśniewolski, 2026)<!--ref:P8--><!--anchor:section:6.3-->, it would define a path-level condition and run it over a multi-year index panel, falsifying this review's bounded-absence claim if a tested condition existed under a different label. Its binding constraint is data access — a multi-year, date-indexed panel with consistent filters — so its owner must be a data-holding group rather than a modelling group.

The third is a **pre-registered head-to-head**: one index panel, a common condition set, a stated tolerance, one metric, and one aggregation frozen before fitting, producing the corpus's first direct comparison and falsifying the claim that cross-family comparison is not currently licensed. It depends on the first for the tolerance and on the second for the panel, and it requires that the panel be shared with at least two methods' authors, which makes governance the constraint and its owner a consortium.

The fourth is a **residual audit for proof constructions** — an independent detector (Neufeld & Sester, 2024)<!--ref:C1--><!--anchor:section:6.3--> applied to proof-bearing parametric and repair rows, reporting violations at a stated tolerance on observed quotes; it depends on the first, uses public panels, and falls to the review's own team. The fifth is a **data-efficiency study** of violation rate and fit against quote count, date count, and training size; it depends on the first and on a panel with varying coverage. The sixth is a **cross-market replication** with the third study's protocol on three indices, at least one non-US; it depends on the third. The seventh **prices the trade-off** in wall-clock and memory on a fixed grid plus an interpretability rubric; it depends on none of the others and needs no panel.

### 6.4 Limitations

The evidence is abstract-level (34 full, 4 partial, 3 metadata-only), 11 records are preprints, and one is a practitioner magazine article. Coding was single-analyst apart from the 16-row second-coder recheck of Section 3.4; retrieval was English-only and OpenAlex-only; one query was lost after HTTP 429; and the rows with known provenance are dominated by US indices (10 of 12), with non-US evidence resting on a 2006 DAX study and a 2022 Johannesburg Stock Exchange study. No full text, proof, or code was retrieved, and no theorem was re-derived and no reported number recomputed.

The instruments are proposed, not validated: the four-family taxonomy and the seven-dimension matrix are analytic categories, the boundary cases are disclosed rather than resolved, and a different coder applying the same rules could shift individual rows. The absence findings are bounded to 41 abstracts and stated at the stability Section 3.4 reports, not at an inter-rater level; the framework is explanatory and untested; and no causal, ranking, or field-wide claim is made. The single-stock panel is a disclosed exception, not index evidence.

The audience is bounded in the same way. This review addresses researchers and model developers able to evaluate construction guarantees against a stated condition set. Three adjacent audiences are neither claimed as served nor excluded: model validators and supervisors, who would need the acceptance-criterion inputs of Section 5.4 and the competence to supply the power and regime fields; model-risk and audit functions, whose competence is operational back-testing rather than surface construction and who need deployment evidence this corpus does not carry; and end investors, for whom neither the conditions nor the rates are decision-relevant without an intermediated summary, and whose competence is reading a validation report rather than a surface.

## 7. Conclusion

### 7.1 Key Takeaways

The research question was how four families enforce static and dynamic no-arbitrage; four answers survive the limitations.

Static admissibility is enforceable in all four families, but each enforces it on a different object, and the objects are not interchangeable. Within the 31 construction rows the certified object is, as the abstracts report it, a single date's surface: an admitted parameter set, an evaluated sample at a finite weight, the image of a projection, or an accepted sample from a sampler. The five condition-and-evaluation rows state or detect conditions without certifying a surface, and the five seminal baselines certify none. The locus explains the evidence — a parameter-domain construction licenses a theorem, an objective a residual, a map a statement about the map, and a sampler a pass rate — and the framework states the triple of mechanism, evidence, and verification at four loci, plus the reporting triple of condition, tolerance, and verification mode; each half is usable alone, and each names what a claim would have to report to be checkable.

Dynamic admissibility is neither stated nor checked anywhere in the corpus. Ten rows engage the time axis; none states a path-level condition and reports checking it over a path, and three of the ten carry a model-class property coded as inherited rather than enforcement (Section 2.2). The claim is bounded: 0 of 41 abstracts, 0 of 36 in-window records, and 0 of 31 construction records, not a statement about the field; a genuine gap and a retrieval-and-vocabulary effect remain open readings, and the review declines to choose.

Proof-level and audit-level evidence are nearly disjoint. Seventeen rows are proof-level and only one reports a violation rate on its own output; six rows audit their own output and that one is also proof-level, on synthetic data. A reader who wants both a theorem and a residual for the same surface will find that one row and no other in this corpus.

The corpus's reported numbers do not license a ranking. No row reports the four fields a direct comparison requires, and the metric vocabulary fragments into seven families whose numbers are not points on one scale. The review therefore reports ranges and conditions rather than a league table, and it does not claim that comparison is impossible: with a common protocol the agenda's head-to-head study could produce one, which is the weaker claim the evidence supports.

### 7.2 Implications and Closing

For authors, the practical implication is a reporting habit: state the condition, the tolerance, and the verification mode; report an audit even when the construction is a proof; and say whether the claim is static or dynamic. The triple costs about three sentences of prose per construction and one table row per family — no new dataset, computation, or notation. Who bears that cost matters, because the benefit falls on others: the author bears it; the reviewer or editor enforces it at no cost beyond asking; the reader receives a checkable claim rather than a validation; and the model validator, who needs the five inputs of Section 5.4, bears a cost the triple does not remove. The proposal is offered with its incidence stated and its effects unmeasured: no study here reports what a reporting standard changed, so the claim that publication norms would follow is asserted rather than established.

The payoff claim must be stated at the size the corpus supports. What the corpus **establishes** is a map: four loci, four evidence types, a near-disjointness of proof and audit, and one paired measurement in which the stronger guarantee carried the higher fit error (Anagha, 2026)<!--ref:G6--><!--anchor:section:7.2-->. What it **asserts** is cost: about five rows state a computational cost, none measures one on a common grid, and interpretability and data efficiency are unpopulated (Table 6). For a build-or-buy decision the corpus therefore does not price a method and does not identify a best one. It tells a decision-maker which guarantee a candidate's evidence carries, what that evidence omits, and where the omission would have to be closed before two candidates' numbers could be compared — a narrower input than the claim that the triple identifies what a guarantee is worth and what it costs, which the findings do not license.

The framework is offered as a proposed instrument with falsifiable consequences: a boundary row it cannot place, or agenda studies that fail to produce family-specific evidence, would count against it. It is not a ranking, and it does not license one. The closing point is a question of description rather than quality: for an equity-index implied-volatility surface, the useful question is not whether it is arbitrage-free, but which admissibility claim its construction licenses, at what tolerance, and how that claim was checked.

## Declarations

**Data Availability Statement.** The review is based on 41 published bibliographic records; the frozen corpus, the coding records, the search and screening provenance, the 31 query strings, and the coding handbook are held in the run directory for this study, and no new empirical data were generated. Reported numbers are drawn from those frozen records and from the sources' own abstracts.

**Ethics Declaration.** Not applicable. The study involves no human participants, no animal subjects, no personal data, and no sensitive materials; no ethics approval was required.

**Author Contributions (CRediT, Contributor Roles Taxonomy).** TY-Cheng: Conceptualization; Methodology; Investigation; Data Curation; Writing – original draft; Writing – review & editing; Visualization.

**Conflict of Interest Statement.** None declared. The author has no financial or personal relationship to any source, software, or venue discussed.

**Funding Acknowledgment.** No funding was received for this work.

**AI Use Disclosure.** This paper was produced with artificial-intelligence (AI)-assisted research tools operating under the Academic Research Skills (ARS) protocol. AI assisted with query construction and search, screening, abstraction, coding and grading of the 41-row evidence ledger, synthesis, drafting, bilingual abstract preparation, and the revision that produced this version. The generative model was a Claude-family agent operating within DeepSeek Harness (DSH) for the first version, and a DeepSeek-family agent for this revision; the exact model identifiers and versions were not recorded in the run log. Verification was limited to bibliographic resolution: all 41 records were resolved and none was flagged retracted, but no theorem was checked and no reported number recomputed, and the three metadata-only rows are cited at title level only. Screening and coding were single-analyst apart from the 16-row second-coder recheck of Section 3.4, without dual screening or adjudication; the recheck's measured figures are reported in Section 3.4 and its cell-level adjudication is recorded with the coding records. Human involvement consisted of run authorization and checkpoint review; no claim-level human verification of the 41 coded rows is recorded. The tools cannot read full texts, proofs, or code, depend on third-party metadata and abstract reconstruction, and can introduce retrieval, quotation, and coding errors that the Limitations in Section 6.4 bound but do not eliminate.

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

### A.1 The 31 query strings

The corpus was frozen before this manuscript was drafted and no new search was run for it. Retrieval targeted OpenAlex (English metadata and abstracts only) on 2026-11-23, using the 31 free-text queries below, each requesting up to 25 records over two pages, restricted to English-language records dated 2015-01-01 to 2026-11-23. The strings are reproduced verbatim from the retrieval script, one row per string, so that a third party can rerun the search and compare the included set.

| **#** | **Group** | **Query string** |
|---|---|---|
| 1 | broad | `arbitrage-free implied volatility surface` |
| 2 | broad | `implied volatility surface arbitrage` |
| 3 | parametric | `SVI stochastic volatility inspired` |
| 4 | parametric | `SSVI implied volatility surface` |
| 5 | parametric | `shape constrained implied volatility surface` |
| 6 | parametric | `nonparametric implied volatility surface` |
| 7 | parametric | `arbitrage-free smoothing implied volatility surface` |
| 8 | parametric | `SABR arbitrage-free volatility` |
| 9 | penalty | `penalty no-arbitrage implied volatility` |
| 10 | penalty | `arbitrage penalty optimization implied volatility` |
| 11 | projection-repair | `projection arbitrage-free option prices` |
| 12 | projection-repair | `repair arbitrage option price surface` |
| 13 | projection-repair | `convexification option prices arbitrage` |
| 14 | generation-filtering | `generative model implied volatility surface` |
| 15 | generation-filtering | `variational autoencoder implied volatility surface` |
| 16 | generation-filtering | `generative adversarial network implied volatility surface` |
| 17 | generation-filtering | `diffusion model implied volatility surface` |
| 18 | generation-filtering | `simulation arbitrage-free implied volatility surface` |
| 19 | generation-filtering | `neural SDE volatility surface` |
| 20 | neural | `neural network implied volatility surface` |
| 21 | neural | `deep learning implied volatility surface` |
| 22 | neural | `neural network option pricing arbitrage-free` |
| 23 | neural | `hard constraint neural network no arbitrage` |
| 24 | neural | `Gaussian process implied volatility surface` |
| 25 | neural | `rough volatility calibration neural network` |
| 26 | dynamic | `dynamic arbitrage implied volatility` |
| 27 | dynamic | `calendar arbitrage implied volatility` |
| 28 | dynamic | `butterfly arbitrage implied volatility` |
| 29 | evaluation | `implied volatility surface survey` |
| 30 | evaluation | `implied volatility surface interpolation no arbitrage` |
| 31 | evaluation | `static arbitrage option prices` |

**Table A1 note.** The eight groups correspond to the eight strata in Section 3.1: broad (2), parametric construction (6), penalty and constrained learning (2), projection and repair (3), generation and filtering (6), neural and learning (6), dynamic and time-indexed (3), and evaluation and conditions (3). Each query returned up to 25 records; the union, de-duplicated by DOI and then by normalised title, is the 430-record unique set reported in Table 1 (750 records were returned before de-duplication).

### A.2 The 40 discretionary exclusions

Screening excluded 389 of the 430 unique records under eight mutually exclusive reason codes: off-topic (141), pre-2015 background (86), relevant but not selected (40), out-of-scope asset (34), publication type (32), duplicate version (31), forecasting or trading (21), and model-calibration or pricing (4). The arithmetic is checkable: 141 + 86 + 40 + 34 + 32 + 31 + 21 + 4 = 389, and 389 + 41 = 430. The 40 rows below are the discretionary class: records judged topically relevant at title level and not selected, under the frozen rule that caps the corpus at 35–45 sources, balances the families, and prefers the more recent or stronger record where two represent the same family.

The screening log records the reason code for every one of these 40 rows but records a record-level rationale for only one of them. Where no rationale is recorded, the table says so rather than reconstructing one; the coder's working notes for the remaining 39 rows were not retained in the frozen artifacts, so the only recoverable statement is the class-level rule above.

| **Log idx** | **Year** | **Title as retrieved** | **Reason recorded** | **Discussed in** |
|---|---|---|---|---|
| 5 | 2026 | Forecasting implied volatility surface with generative diffusion models | code only; no record-level note | Section 6.2 audit |
| 6 | 2026 | Latent-Space No-Arbitrage Geometry of Generative Models for Implied Volatility Surfaces | code only; no record-level note | A.2 only |
| 9 | 2026 | Arbitrage-Constrained Diffusion-Inspired Denoising for Sparse Implied Volatility Surface Reconstruction | code only; no record-level note | A.2 only |
| 17 | 2026 | Arbitrage-Free Implied Volatility Surface Reconstruction via Additive Martingales | code only; no record-level note | Section 6.2 audit |
| 22 | 2026 | Volatility Surface Reconstruction using Deep Learning under No-Arbitrage Constraints | code only; no record-level note | A.2 only |
| 35 | 2025 | Controllable Generation of Implied Volatility Surfaces with Variational Autoencoders | code only; no record-level note | A.2 only |
| 36 | 2025 | PHYSICS-INFORMED NEURAL NETWORKS FOR ARBITRAGE-FREE VOLATILITY SURFACE CONSTRUCTION IN INCOMPLETE MARKETS | code only; no record-level note | A.2 only |
| 39 | 2026 | Arbitrage-Free Gaussian Process Interpolation for Implied Volatility Surfaces | code only; no record-level note | A.2 only |
| 42 | 2019 | Pricing Options and Computing Implied Volatilities using Neural Networks | code only; replacement note (A.3) | Section 3.1; A.3 |
| 51 | 2016 | Arbitrage-Free interpolation if Implied Volatility Surface | code only; no record-level note | A.2 only |
| 52 | 2026 | ART-Diff: Arbitrage-Consistent, Regime-Aware and Tail-Calibrated Diffusion for Implied Volatility Surfaces | code only; no record-level note | A.2 only |
| 53 | 2026 | Generative Adversarial Networks for Inpainting Implied Volatility Surfaces | code only; no record-level note | A.2 only |
| 56 | 2026 | Arbitrage-Free Construction of Volatility Surfaces in the Ultra-Short Tenor Regime: Applications to 0DTE Options and Stable Greeks Extraction | code only; no record-level note | A.2 only |
| 57 | 2026 | SABR-informed multitask Gaussian process: A synthetic-to-real framework for implied volatility surface construction | code only; no record-level note | A.2 only |
| 58 | 2026 | Arbitrage-Aware Probabilistic Multi-Step Forecasting of Implied Volatility Surfaces: Joint Generation of Surface-Return Trajectories Using Latent Diffusion | code only; no record-level note | Section 6.2 audit |
| 67 | 2025 | GAN-Enhanced Implied Volatility Surface Reconstruction for Option Pricing Error Mitigation | code only; no record-level note | A.2 only |
| 84 | 2020 | Robust Calibration For SVI Model Arbitrage Free | code only; no record-level note | A.2 only |
| 98 | 2017 | Calibration of Hybrid Model and Arbitrage-Free Implied Volatility Surface | code only; no record-level note | A.2 only |
| 111 | 2026 | Forecasting Implied Volatility Surfaces with Conditional Generative Diffusion Models | code only; no record-level note | Section 6.2 audit |
| 112 | 2026 | Generative Bayesian Computation for Volatility Surfaces | code only; no record-level note | A.2 only |
| 211 | 2016 | Approximate Arbitrage-Free Option Pricing Under the SABR Model | code only; no record-level note | A.2 only |
| 243 | 2025 | A Variational Autoencoder Approach to Conditional Generation of Possible Future Volatility Surfaces | code only; no record-level note | A.2 only |
| 258 | 2025 | Variational Autoencoders for Completing the Volatility Surfaces | code only; no record-level note | A.2 only |
| 286 | 2018 | Implied volatility parameterization based on a machine learning polynomial approach | code only; no record-level note | A.2 only |
| 293 | 2024 | A new encoding of implied volatility surfaces for their synthetic generation | code only; no record-level note | A.2 only |
| 310 | 2024 | Whack-a-mole Learning: Physics- Informed Deep Calibration for Implied Volatility Surface | code only; no record-level note | A.2 only |
| 323 | 2020 | An arbitrage-free interpolation of class $C^2$ for option prices | code only; no record-level note | A.2 only |
| 325 | 2026 | From No-Arbitrage to Foundation Models: A Review of Financial-Mathematics-Constrained Generative AI and Deep Learning for Quantitative Finance | code only; no record-level note | A.2 only |
| 326 | 2025 | Proof-Carrying No-Arbitrage Surfaces: Constructive PCA-Smolyak Meets Chain-Consistent Diffusion with c-EMOT Certificates | code only; no record-level note | Section 6.2 audit |
| 335 | 2026 | Diffusion models for dynamic volatility surface generation and data-driven hedging | code only; no record-level note | Section 6.2 audit |
| 342 | 2026 | A Wiener Chaos Approach to Martingale Modelling and Implied Volatility Calibration | code only; no record-level note | Section 6.2 audit |
| 343 | 2026 | Mixture-Preserving, Arbitrage-Free Interpolation for Volatility-Surface Models | code only; no record-level note | A.2 only |
| 369 | 2026 | Quasi-Explicit Recovery of Heston Parameters from SSVI-Parameterized Volatility Surfaces | code only; no record-level note | A.2 only |
| 372 | 2025 | Operator-Based Implied Volatility Smoothing: An Approach to Improve GNO Efficiency Using Bivariate Cubic B-Splines | code only; no record-level note | A.2 only |
| 373 | 2026 | Constructing and Fitting Implied Volatility Surfaces: A Practitioner Framework Using SVI Parametrization | code only; no record-level note | A.2 only |
| 378 | 2026 | One-X Property Conjecture, Stochastic Orders and Implied Volatility Surface Construction | code only; no record-level note | A.2 only |
| 385 | 2026 | Arbitrage-Free Volatility Surface Construction: SVI, SABR, SSVI, and Vanna-Volga Calibration Methods | code only; no record-level note | A.2 only |
| 391 | 2026 | Economically Interpretable Arbitrage-Free Option Prices: Physical GBM Benchmarks and Smile-Preserving Arbitrage-Consistent Projection | code only; no record-level note | A.2 only |
| 393 | 2026 | Option Pricing Based on Implied Volatility Forecasting and No-Arbitrage Projection Correction: Evidence from SSE 50ETF Options | code only; no record-level note | Section 6.2 audit |
| 422 | 2026 | Physics-Informed Neural Networks for Local Volatility Surface Calibration via the Dupire Equation | code only; no record-level note | A.2 only |

**Table A2 note.** "Log idx" is the row's position in the frozen screening log, not a count; the log is retained with the run artifacts so a reader can resolve any index to its DOI. "Discussed in" names the section where the row is used, if anywhere: eight titles use time, forecasting, martingale, or chain-consistency vocabulary and were re-read at title level for the audit in Section 6.2, and every other row appears in this table only. Titles are given as retrieved, including any irregularity. No excluded record is cited in the manuscript, and none appears in the reference list.

### A.3 The two post-screening replacements

Two records were replaced after abstract-level reading, and both replacements were made for the same reason: the retrieved abstract did not fit the frozen inclusion rule, although the title had matched a query. The first, log index 42, priced options and computed implied volatilities with neural networks and made no arbitrage-enforcement claim; it was replaced by Wiedemann et al. (2025), whose abstract states an adherence result. The second, log index 89, derived no-arbitrage conditions for a delta-parameterised volatility surface estimated on foreign-exchange options and fell outside the equity-index asset scope; it was replaced by Fukasawa (2022), whose subject is the equity-index implied-volatility asymptotics. Neither record failed metadata resolution or abstract reconstruction: every one of the 41 included records resolved to a DOI-bearing index record, with a DOI lookup status of 200 and a title match of 1.0, and the abstract coverage reported in Table 1 is the coverage those records actually had. The two replacement decisions are recorded in the frozen screening log at the indices named, and the earlier draft's attribution of the replacements to resolution failure is withdrawn here as inaccurate.

## Appendix B. Evidence Ledger

Each row records the review's coding of one source, with the field definitions of Appendix D. **Evidence** is the status of the no-arbitrage claim as reported: proof, numerical test, or assumption. **Audit** is the independent property defined in D.3: whether the row reports a violation, residual, or defect statistic on its own output. **Static** names the subset of SC1–SC5 stated in Section 2.1 that the row's claim expresses, or `none` where no admissibility condition is claimed; a row that claims admissibility without enumerating conditions is coded SC1–5, because the claim is then the full predicate. **Time** is time-axis engagement as defined in D.4 (Y where the row's coded object is date-indexed). **Dyn** is the dynamic-enforcement code of D.5: D0 none, D1 declares a process-level condition without checking it, D2 inherits a model-class property, D3 states and checks a dynamic condition. **Level** is the evidence level of D.8: VI single study, VII expert commentary or narrative review. **Comp.** is the comparability class: DC directly comparable, RC reported for context, NC not comparable. **Coverage** is the abstract coverage available to the coder. **Cited in Section** lists the sections that cite the row, as coded in the text.

| **ID** | **Source** | **Family** | **Evidence** | **Audit** | **Static** | **Time** | **Dyn** | **Level** | **Comp.** | **Coverage** | **Peer-reviewed** | **Cited in Section** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P1 | Guo et al. (2016) | P | proof | N | SC1–4 (+SC5 sep) | N | D0 | VI | NC | full | yes | 1.1, 2.1, 4.1 |
| P2 | Martini & Mingone (2022) | P | proof | N | SC1–4 | N | D0 | VI | RC | full | yes | 2.1, 4.1 |
| P3 | Mingone (2022) | P | proof | N | SC1–5 | N | D0 | VI | RC | full | yes | 4.1 |
| P4 | Corbetta et al. (2019) | P | assumption | N | SC1–5 | N | D0 | VI | NC | metadata-only | yes | 4.1 |
| P5 | Zaugg et al. (2025) | P | proof | N | SC1–5 | N | D0 | VI | RC | full | yes | 4.1 |
| P6 | Le Floc’h (2025) | P | proof | N | SC1–5 | N | D0 | VI | RC | full | yes | 4.1 |
| P7 | Klassen (2016) | P | assumption | N | SC1–5 | N | D0 | VI | NC | metadata-only | no [preprint] | 4.1 |
| P8 | Barski & Wiśniewolski (2026) | P | proof | N | SC1–3, 5 | Y | D1 | VI | NC | full | no [preprint] | 2.2, 4.1, 6.2, 6.3 |
| N1 | Cao et al. (2020) | N | numerical test | N | SC1–5 | N | D0 | VI | RC | full | yes | 2.3, 4.2 |
| N2 | Wiedemann et al. (2025) | N | numerical test | Y | SC1–5 | N | D0 | VI | RC | full | yes | 1.1, 3.1, 4.2, 5.1 |
| N3 | Ackerer et al. (2019) | N | numerical test | N | SC1–5 | N | D0 | VI | RC | full | no [preprint] | 4.2 |
| N4 | Sidogi et al. (2022) | N | numerical test | N | SC1–5 | N | D0 | VI | RC | full | yes | 3.3, 4.2, 5.1, 5.2 |
| N5 | Na et al. (2023) | N | numerical test | N | SC1–5 | N | D0 | VI | RC | full | no [preprint] | 1.1, 3.3, 4.2, 5.1, 5.2 |
| N6 | Hoshisashi et al. (2023) | N | numerical test | Y | SC2, 3, 5 | N | D0 | VI | RC | full | no [preprint] | 4.2, 5.1 |
| R1 | Cohen et al. (2020) | R | numerical test | N | SC1–5 | N | D0 | VI | RC | full | yes | 4.3 |
| R2 | De March & Henry-Labordère (2019) | R | proof | N | SC1–5 | N | D0 | VI | RC | partial | no [preprint] | 4.3 |
| R3 | Bender & Thiel (2020) | R | proof | N | SC1–5 | N | D0 | VI | NC | full | yes | 1.1, 2.3, 4.1, 4.3 |
| R4 | Yao et al. (2026) | R | assumption | N | SC1–5 | N | D0 | VI | NC | metadata-only | yes | 4.3 |
| R5 | Xiong & Liu (2026) | R | numerical test | Y | SC3, 5 | N | D0 | VI | RC | full | yes | 2.1, 3.3, 4.3, 5.1, 5.2, 5.3, 6.2, 6.3 |
| R6 | Buehler et al. (2026) | R | proof | N | SC1–5 | N | D0 | VI | RC | full | no [preprint] | 2.3, 4.1, 4.3 |
| R7 | Alvarez (2025) | R | numerical test | Y | SC1–3 | N | D0 | VI | RC | full | no [preprint] | 4.3, 5.1, 5.3 |
| R8 | Zetocha (2023) | R | assumption | N | SC1–5 | Y | D1 | VI | NC | full | no [preprint] | 4.3 |
| R9 | Madan & Schoutens (2019) | R | numerical test | N | SC1–5 | N | D0 | VI | RC | full | yes | 4.3 |
| G1 | Ning et al. (2023) | G | proof | N | SC1–5 | Y | D2 | VI | RC | full | yes | 4.4, 5.1 |
| G2 | Vuletić & Cont (2024) | G | numerical test | N | SC1–5 | Y | D0 | VI | RC | full | yes | 4.4 |
| G3 | Cont & Vuletić (2023) | G | assumption | N | SC1–5 | Y | D0 | VI | RC | partial | yes | 4.4 |
| G4 | Ginart Belmonte & Cole (2025) | G | numerical test | N | SC1–5 | N | D0 | VI | RC | full | yes | 4.4 |
| G5 | Bajalica et al. (2026) | G | numerical test | Y | SC1–3, 5 | N | D0 | VI | RC | full | yes | 1.1, 2.1, 4.4, 5.1, 5.3, 6.2 |
| G6 | Anagha (2026) | G | proof | Y | SC2, 3, 5 | N | D0 | VI | RC | full | no [preprint] | 2.1, 3.3, 4.4, 5.1, 5.2, 5.3, 6.1, 6.2, 7.2 |
| G7 | Cohen et al. (2021) | G | proof | N | SC1–5 | Y | D2 | VI | RC | full | yes | 2.2, 2.3, 4.4, 5.1, 6.2 |
| G8 | Yang et al. (2017) | G | proof | N | SC1–5 | N | D0 | VI | RC | full | yes | 4.4, 5.1 |
| C1 | Neufeld & Sester (2024) | C | proof | N | SC1–5 | N | D0 | VI | RC | full | yes | 5.2, 5.4, 6.3 |
| C2 | Niu (2015) | C | assumption | N | SC1–5 | Y | D1 | VII | NC | full | no [preprint] | 1.1, 2.2, 3.2, 6.2 |
| C3 | Andrès et al. (2026) | C | proof | N | SC1–5 | Y | D2 | VI | RC | full | yes | 2.2, 2.3, 6.2, 6.3 |
| C4 | Fukasawa (2022) | C | proof | N | SC1–3 | N | D0 | VI | NC | partial | yes | 2.1, 3.1 |
| C5 | Stahl & Blauth (2024) | C | numerical test | N | SC1–5 | Y | D1 | VI | NC | full | yes | 1.3, 2.2 |
| S1 | Gatheral & Jacquier (2013) | S | proof | N | SC1–4 (+SC5 sep) | N | D0 | VI | RC | partial | yes | 1.1, 2.1 |
| S2 | Fengler (2009) | S | numerical test | N | SC1–3, 5 | N | D0 | VI | NC | full | yes | 1.1, 4.3 |
| S3 | Hagan et al. (2014) | S | numerical test | N | SC3 | N | D0 | VI | RC | full | no [practitioner outlet] | 2.1 |
| S4 | Bodurtha & Jermakyan (1999) | S | assumption | N | none | N | D0 | VI | RC | full | yes | 4.3 |
| S5 | Fengler et al. (2006) | S | assumption | N | none | Y | D0 | VI | RC | full | yes | 4.3 |

**Appendix B note.** The columns are the review's own coding; no row was re-coded for this version except that the two interpretive columns this version adds (Audit, Time, Dyn) were coded from the same frozen records under the rules in Appendix D, and the Static column states what earlier versions kept in the coding records only. The counts are recomputable from the columns: 17 proof + 16 numerical test + 8 assumption = 41; 6 audit rows (N2, N6, R5, R7, G5, G6), of which one is proof-level (G6); 10 Time = Y rows (P8, R8, G1, G2, G3, G7, C2, C3, C5, S5); dynamic codes D3 = 0, D2 = 3 (G1, G7, C3), D1 = 4 (P8, C2, C5, R8), D0 = 34; comparability 0 DC, 30 RC, 11 NC; coverage 34 full, 4 partial (R2, G3, C4, S1), 3 metadata-only (P4, P7, R4); peer review 29 yes and 12 no, the 12 comprising 11 preprints and the practitioner-magazine outlet S3; evidence level 40 VI and one VII (C2).

## Appendix C. Instrument Reconciliation, Boundary Cases, and Correction Record

### C.1 What was coded

The interpretive fields were coded from title, abstract, and bibliographic metadata under the operational definitions now printed in full as Appendix D: family; evidence status; audit; the static condition subset expressed; time-axis engagement; dynamic enforcement; evidence level; the market or dataset named; the fit or accuracy metric reported; and the comparability class. A claim is coded as evidence only where the record states it. A title-level claim is coded as unverified and is not used as evidence for any finding. The metadata-only rule, the preprint convention, and the evidence-level definitions are D.8; the recomputation table for every count the manuscript reports is D.10.

### C.2 Instrument reconciliation: the seven-axis and eight-axis frames

An earlier version of this study used an eight-axis evaluation instrument that added extrapolation and reproducibility to the seven axes of Table 6. This manuscript uses the seven-axis frame for two reasons: extrapolation and reproducibility were sparsely and inconsistently codeable at abstract level, and the seven-axis frame maps one-to-one onto the dimensions the corpus actually reports. The two instruments were compared row by row during the appraisal stage; the seven-axis frame is the aggregation of the eight-axis coding, the reconciliation is recorded with the coding records, and no count, verdict, or claim in this manuscript changes between them.

### C.3 Boundary cases

Five rows sit across family borders and are retained with the friction disclosed rather than reassigned. R3 is a repair built on an admissible reference function, so its mechanism is closer to construction; it stays in R because the repair locus is defined by the certified object, and R3 certifies its output. R6 claims a strict guarantee through parameter positivity, which is architecturally parametric, but its object is a completed surface, and it anchors the repair family's strict end. N1 enforces constraints architecturally, like the G-family rows, but its output is a single fitted surface rather than a generative model, which keeps it in N. G7 satisfies its constraints on a modelled state space and explicitly disclaims a dynamic-arbitrage guarantee, which is why it is coded D2 rather than D3. C3 builds a path-dependent model whose surfaces are static-admissible but whose dynamic consistency is not discussed, so it is coded D2 as well. A sixth row, C5, is a single-stock panel retained as a disclosed exception; it is the only longitudinal dynamic-adjacent evidence in the corpus and is never counted as index evidence.

### C.4 The SC3 correction and the rows it touches

The earlier version of Section 2.1 printed SC3 as $\partial^{2} c/\partial k^{2}\ge 0$. The butterfly condition is $c''-c'\ge 0$ on the normalised call price in log-moneyness, and Section 2.1 now states it that way with the derivation and the two boundary relations. The correction is to the review's predicate, not to any row's claim, and the re-examination therefore takes the following form.

Thirty-nine of the 41 rows state a condition subset that includes SC3; S4 and S5 claim no admissibility condition and are the two exceptions. Every one of the 39 was re-read against the corrected form. No row's evidence status, audit code, time-axis code, dynamic code, or comparability code changes, because each of those columns records the mode of verification, the object coded, or the reporting protocol, and none of them was assigned from the algebraic form of the condition: a row that reports a residual at a stated tolerance is a numerical test whether the condition it tests is written as $c''\ge 0$ or as $c''-c'\ge 0$, and a row whose parameter domain guarantees every admissible vector is a proof under either form. The rows whose abstracts name conditions in the corrected family are N6 and G6 (convexity of the call price in log-moneyness together with non-negative maturity ramps), R5, G5 and S2 (calendar monotonicity with call-spread or butterfly conditions), and R7 and R6 (call-spread and butterfly conditions as linear inequalities); all seven are coded as before, and the two rows whose abstracts describe convexity in log-moneyness terms (G6 and S3) are unchanged, because the stronger printed form was sufficient for the claim each paper makes about its own construction. What changed is the review's statement of the predicate and its consistency with SC4; what did not change is any count, verdict, or family assignment.

### C.5 Withdrawal of the A/B/C appraisal grades

The earlier version reported a composite appraisal grade (A 11, B 13, C 17) per row. The grade is withdrawn from this version. Two of its six criteria were free-text judgements that the frozen ledger does not carry, so a reader could not recompute a single grade from Appendix B, and printing them would present a judgement as a derivation. The evidence-level label of D.8 is retained instead, because it is a published hierarchy level rather than a composite, it is defined in the manuscript, and it can be checked against the record. No finding in Sections 4 and 5 used the composite grade: the family distributions in Tables 3, 5 and 6 are tallies of evidence status, comparability, and coverage, and the one place the grade appeared in the body was a description of the appraisal instrument, which now describes the evidence-level axis instead.

## Appendix D. Coding Handbook

The handbook below is the operational definition of every ledger field. It was written so that a second analyst working only from the 41 frozen records and this document can reproduce Appendix B row by row, and it fixes the reliability protocol used for the stratified second-coder recheck reported in Section 3.4.

**Purpose.** This handbook defines every field of the evidence ledger (Appendix B) operationally, so that a second analyst working only from the 41 frozen records and this document can reproduce the ledger row by row. It also fixes the reliability protocol (Section D.9) used for the stratified second-coder recheck reported in Section 3.4 of the manuscript.

**Unit of coding.** One row is one source as represented by the record that entered the corpus: its title, its retained abstract, and its bibliographic metadata. Nothing outside that record is coded. A claim that appears only in a full text, a proof, or a code repository is outside the unit, and its absence is coded as absence of a *reported* claim, never as absence of the property.

**Freeze.** The record set, the abstracts, and the search provenance were frozen on 2026-11-23. A re-application of this handbook to records retrieved later is a different coding, not a replication of this one, because the OpenAlex index behind the records is live.

### D.1 Family code

Each row receives exactly one family code, assigned from the mechanism named in the abstract:

- **P, parametric construction**: the constraint enters a parameter domain or a function class specified before fitting, so that every admitted parameter vector yields an admissible object.
- **N, penalty and constrained learning**: the constraint enters a training objective or an architectural regulariser, so compliance is approximate and conditional on a weight, a tolerance, and a stopping rule.
- **R, projection and repair**: a map is applied to a fitted or quoted object after the fact, so the certified object is the image of that map.
- **G, generation and filtering**: candidate surfaces, parameters, or prices are produced and then accepted, rejected, projected, or constrained, so the certified object is the accepted sample or the generator's model class.
- **C, conditions and evaluation**: the row states, detects, or reviews admissibility conditions without constructing or repairing a surface.
- **S, seminal baseline**: a pre-2015 construction included as declared baseline rather than as a window record.

**Tie-break.** Where two mechanisms are present, code the family of the **certified object**, not of the estimator: a gated network whose decoder is a deterministic convex architecture is P-shaped but is coded N when its abstract presents the constraint as a loss or architectural term of a learned estimator (N1), and is coded G when the object is a generated surface family. Rows that sit across borders are retained in one family and flagged in Appendix C rather than reassigned.

### D.2 Evidence status

The evidence-status field records what the abstract presents as support for the row's admissibility claim. It has three values and no ranking order.

- **Proof**: the abstract states a theorem, a closed-form characterisation, or a formal construction that establishes admissibility over a set, for all objects in that set. A convergence proof for an algorithm is a proof about the algorithm, not about the admissibility of a repaired surface; a repair whose projection map is proved to land in the admissible set is coded **proof for the map** and the manuscript states that object in the row note.
- **Numerical test**: the abstract reports a numerical result that it presents as supporting the admissibility claim, where that result is not a violation or residual statistic computed on the row's own output. Examples: a fit or pricing error, a coverage or inside-spread statistic, a Wasserstein distance, a comparative accuracy against a baseline, or a hedging result. A numerical test is never upgraded to a proof.
- **Assumption**: admissibility is asserted, inherited from a model class, or left implicit, with neither a theorem nor a numerical result presented as support.

**Precedence.** Proof > numerical test > assumption applies only to *classification order*, not to evidential strength: a penalty row that reports a residual is coded numerical test even when the reported rate is zero, and a row whose architecture is described as convex by design but whose abstract states no theorem is coded numerical test, not proof.

### D.3 Audit row (separate from evidence status)

**Definition.** An audit row is a row whose abstract reports a **violation, residual, or defect statistic computed on the row's own fitted, repaired, or generated output**. The statistic must be about the row's own construction; a comparative error against a baseline, a runtime, a coverage measure, or a hedging profit is not an audit statistic.

**Decision rule.** Code audit = Y only if all three hold:

1. the reported quantity is a violation rate, a count of violated conditions, a residual of an admissibility condition, or a pass rate on an admissibility test;
2. it is computed on output the row itself produced, not on a benchmark dataset or on another row's surface;
3. the abstract names, implicitly or explicitly, the conditions tested. Where the tolerance is not stated, the row is still an audit row, and the missing tolerance is recorded as a limitation of the row (this is why the manuscript says a rate without a tolerance is uninterpretable even within its own study).

**Not an audit.** A residual for a *method* rather than a surface (e.g. a convergence residual), an accuracy number, a spread-capture percentage, or a pass rate on a test set that is not the row's own output is coded N. Consistent with this rule, six rows are audit rows (N2, N6, R5, R7, G5, G6) and the other eleven numerical-test rows are not: N1, N3, N4, N5, R1, R9, G2, G4, C5, S2, S3. The ledger's Audit column carries the value for every row, so the eleven can be recounted rather than taken on trust.

**Independence from evidence status.** Audit is coded on its own axis and is not a value of the evidence-status field. A proof row can be an audit row (G6 is both) and a test row can fail to be one. This is the separation the manuscript's Section 3.2 states and Section 5.1 recounts.

### D.4 Time-axis engagement

**Definition.** Code time-axis engagement = **Y** where the abstract's *object* is indexed by calendar time: a date-indexed panel, a surface path or process, a time-indexed parameter or probability sequence, a state that evolves over dates, or a dynamics model of the surface family. Ten rows are Y (P8, R8, G1, G2, G3, G7, C2, C3, C5, S5).

**Exclusions.** The maturity axis of a single surface is **not** calendar engagement. A construction that enforces non-decreasing total variance across maturities (SC5) has made a static statement about one date's object and is coded N here, however the abstract labels it. A continuous-time *model* whose evaluated object is one date's surface (R9) is coded N: the model is dynamic in its class, but the coded object is not date-indexed. A VAR or factor model estimated on a panel is Y even where no admissibility condition is imposed (S5). Conversely, a panel used only as an evaluation sample is **not** engagement: R5 repairs one surface per trading day over 252 out-of-sample days, N2 fits across ten years of intraday quotes, and R7 reports year-by-year panels, but in each case the coded object remains a single date's surface and no claim is indexed by calendar time. Engagement is a property of the object or the claim, not of the sample size in the date direction.

**Why the axis is separate from dynamic enforcement.** Engagement measures the object's indexing; enforcement measures whether a process-level condition is stated and checked. The two are coded independently so that a row can engage time without enforcing anything (the common case) and so that the absence claim can be bounded exactly.

### D.5 Dynamic enforcement

**Definition of a dynamic condition.** A condition on the joint law of the surface family indexed by calendar time: the absence of predictable arbitrage opportunities across dates, or consistency of the date-indexed family with a martingale measure for a stated numéraire. A condition on one date's surface, including a maturity-monotonicity condition and including anything called "calendar arbitrage", is **static** (Section 2.1, SC5) and is never coded as dynamic enforcement.

**Coding values.**

- **D0, none**: the abstract states no process-level admissibility condition. This includes rows that construct a date-indexed object without an admissibility claim.
- **D1, declared or described, not checked**: the abstract discusses, names, or asserts a process-level condition, or reports a model-level diagnostic of it, without stating that the constructed, date-indexed family was checked against it.
- **D2, inherited from a model class**: the admissibility property follows from the class the model belongs to (for example a constrained state space, an SDE whose coefficients keep the surface static-admissible, or a decoder that cannot emit a violation), and no check of the fitted family over dates is reported.
- **D3, stated and checked**: the abstract states a process-level condition **and** reports that the constructed date-indexed family was checked against it over a path or sequence.

**The model-class rule (the rule Section 2.2 of the manuscript states).** A model-class inherited guarantee is **not** dynamic-constraint enforcement under this coding. It is coded D2 and reported as what it is: a property of the class, inherited by every member, unaccompanied by any reported check of the fitted family across dates. The rule is deliberately conservative and it is the rule on which the "0 of 41" count rests: the count is 0 rows at D3, and the manuscript states that count together with the D1 and D2 rows by ID, so a reader who rejects the rule can recompute the count from the ledger without leaving the manuscript.

**Result.** D3 = 0; D2 = G1, G7, C3; D1 = P8, C2, C5, R8; D0 = the remaining 34 rows. The manuscript states each of the four groups and names the rows.

### D.6 Static condition statement

The static predicate is SC1–SC5 as defined in Section 2.1 of the manuscript, with SC3 in its corrected form, c'' − c' ≥ 0, in log-moneyness for the normalised call price.

- A row that claims full admissibility without enumerating conditions is coded `SC1–SC5`: its claim is assessed against the whole predicate.
- A row whose abstract names a subset is coded with that subset, using the abbreviated range notation in the ledger (e.g. `SC1–3,5`).
- A row that states no admissibility condition at all (the two pre-constraint baselines) is coded `none`.
- `ns` is retained only for a row whose claim cannot be mapped onto the predicate without inference; the ledger as frozen uses it for no row, because a bare "arbitrage-free" claim is treated as a claim on the full predicate.

**SC3 dependency.** Any row whose coded subset contains SC3 is a row whose coding depends on the corrected butterfly condition. The re-examination reported in Appendix C applies to exactly those rows; where a row's subset does not contain SC3, the correction cannot change it.

### D.7 Comparability

- **DC, directly comparable**: the same dataset or panel, the same condition set and tolerance, the same metric and aggregation, and the same protocol. No row qualifies in this corpus.
- **RC, reported for context**: a number is reported that a reader can place beside another row's number but that does not license a comparison, because at least one of the four fields differs.
- **NC, not comparable**: a different object or metric, or no number at all.

Comparability is coded from the abstract and is deliberately conservative: where a required field is unstated, the row cannot be DC.

### D.8 Abstract coverage, peer review, and evidence level

- **Coverage**: `full` where a complete abstract was retrieved; `partial` where the retained text is truncated or reconstructed from fragments (R2, G3, C4, S1); `metadata-only` where no abstract was retrievable and the row is coded from title and metadata only (P4, P7, R4).
- **Metadata-only rule**: a metadata-only row is cited only for what its title asserts; it is counted in every structural count (family, evidence status, comparability, coverage, peer review) and is never counted as evidence *for* its own claim. The rule is applied identically in Sections 3.2, 5.1 and Appendix B.
- **Preprint**: tagged at every point of use where the record has no peer-reviewed version of record in this corpus. Eleven rows are preprints.
- **Evidence level VI/VII**: the seven-level source hierarchy used for appraisal. Level VI is a single descriptive, quantitative, or qualitative study; level VII is expert commentary or a narrative review. Forty rows are VI; C2 is VII. The level is not an evidence-status value and not a quality grade.
- **Appraisal grades A/B/C**: recorded in the corpus's earlier appraisal record (A 11, B 13, C 17) but not reproduced per row in the ledger and therefore not used as a recomputable count anywhere in the manuscript. The reason is stated in Appendix C: two of the six appraisal criteria are free-text judgements that the ledger fields do not carry, so printing the grades alongside the fields would present a judgement as a derivation.

### D.9 Reliability protocol

**Design.** A stratified second-coder recheck of a 16-row sample, drawn to exercise every family and every weak-coverage class rather than to estimate a population rate.

**Strata and sample.** Two rows per family, chosen to include the family's boundary and weakest-coverage rows, plus every metadata-only row:

| Stratum | Rows |
|---|---|
| P (3) | P1, P4 (metadata-only), P7 (metadata-only, preprint) |
| N (2) | N2, N5 |
| R (4) | R2 (partial), R3, R4 (metadata-only), R5 |
| G (2) | G6, G7 |
| C (3) | C3, C4 (partial), C5 |
| S (2) | S1 (partial), S2 |

The sample is 16 rows: all three metadata-only rows, three of the four partial-abstract rows, both families' known boundary cases (R3, G7), and the only proof-and-audit row (G6).

**Blindness.** The second coder receives the 16 records, this handbook, and the empty coding form. The first analyst's coded columns are withheld. No discussion occurs before the second coder returns the form.

**Fields re-coded.** Family; evidence status; audit; time-axis engagement; dynamic enforcement; comparability. Metadata fields (coverage, peer review, preprint tag, evidence level) are not re-coded because they are bibliographic rather than interpretive.

**Statistics.** Percentage agreement per field. For the three-level evidence-status field, Cohen's κ (unweighted) over the sampled rows. For the binary fields (audit, time-axis engagement) and the four-level dynamic field, percentage agreement, with the raw disagreement count reported. Disagreements are adjudicated by the first analyst with a one-line written reason per row, and the adjudication is reported, not hidden.

**Decision rule.** A field is treated as *stably coded* where agreement is at least 0.85 and, for evidence status, κ ≥ 0.70. Any field below the threshold triggers a restatement of the absence claims that depend on it at the observed stability, with the disagreement rows named. No field is reported as reliable on the strength of a design alone.

**Reporting.** The result is reported in Section 3.4 and the completed forms are retained with the coding records. The manuscript does not claim inter-rater agreement for any field that was not re-coded.

### D.10 Recomputation

Every structural count in the manuscript can be recomputed from the ledger columns:

| Count | Rule |
|---|---|
| Rows | 41, one per ID |
| Family totals | tally of the Family column |
| Evidence status | tally of the Evidence column; in-window/seminal split follows the ID letter |
| Audit rows | tally of Audit = Y (6) |
| Proof-and-audit overlap | rows with Evidence = proof and Audit = Y (1, G6) |
| Time-engaging rows | tally of Time = Y (10) |
| Dynamic enforcement | tally of Dyn by value: D3 = 0, D2 = 3, D1 = 4, D0 = 34 |
| Comparability | tally of Comp. column (0 DC, 30 RC, 11 NC) |
| Coverage | tally of Coverage column (34 full, 4 partial, 3 metadata-only) |
| Peer review | tally of the Peer-reviewed column (29 yes, 12 no; 11 preprints plus the practitioner article S3) |
| Peer review, no | 12 rows carry Peer-reviewed = no: the 11 preprints plus the practitioner-magazine outlet (S3) |
| Preprints | rows tagged [preprint] (11) |
| Evidence level | tally of Level column (40 VI, 1 VII) |

**Arithmetic checks.** Evidence status: 17 proof + 16 numerical test + 8 assumption = 41. Partition by audit: 1 proof-and-audit (G6) + 16 proof-only + 5 test-and-audit (N2, N6, R5, R7, G5) + 11 test-only + 8 assumption = 41. Audit rows: 5 test-and-audit + 1 proof-and-audit = 6. Dynamic codes: 0 (D3) + 3 (D2) + 4 (D1) + 34 (D0) = 41. Time engagement: the ten Time = Y rows contain all four D1 rows and all three D2 rows; the other three (G2, G3, S5) are D0, so they engage the time axis without making any dynamic claim. Composition: 29 peer-reviewed + 11 preprints + 1 practitioner = 41; 36 in-window + 5 seminal = 41.
