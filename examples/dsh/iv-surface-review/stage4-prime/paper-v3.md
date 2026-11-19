# Arbitrage-Free Implied Volatility Surface Construction: A Structured Literature Review of Parametric, Nonparametric, and Neural Approaches

**Author:** TY-Cheng  
**Affiliation:** Independent Researcher  
**Date:** 2026-11-19  
**Paper type:** Literature review  
**Citation style:** APA 7.0  
**Running head:** Which Guarantee?  
**JEL codes:** G13, C45, C63  
**Body word count:** 6804 words (excluding abstract, declarations, references, and appendices)  
**Target:** General academic journal / arXiv-style preprint (no specific venue)  
**Revision log:** v3.0 Stage 4′ copy-edit — tables renumbered; year note added; no content change. Prior: v2.0 Stage 4 revision + point-by-point response (2026-11-19)

---

## Abstract

Constructing an arbitrage-free implied volatility surface (IVS) is a central problem in derivatives modelling. Parametric, nonparametric, and neural approaches each claim to enforce static or dynamic no-arbitrage, but the meaning of “arbitrage-free” and the strength of the supporting evidence differ across families. This structured review synthesizes 40 sources—30 peer-reviewed articles or conference papers and 10 preprints, published between 2009 and 2026—identified through 24 OpenAlex full-text queries and assessed at metadata/abstract level. The review organizes the literature by where the constraint enters the pipeline—construction, penalty, projection/repair, or generation/filtering—rather than by method family alone. Parametric SVI/SSVI/eSSVI families provide explicit static-arbitrage conditions but can be inflexible; nonparametric, neural, and generative methods rely on soft penalties, hard architectures, two-step projection, or post-hoc repair, with guarantees that are method-specific and often untested dynamically. Dynamic no-arbitrage is less standardized and less frequently evaluated; static admissibility is necessary but not sufficient. Evaluation is fragmented: fit metrics dominate, and no shared benchmark for violations, out-of-sample stability, wing behaviour, computational cost, and interpretability was identified in the retrieved abstracts. The review proposes a four-family enforcement taxonomy and a seven-dimension evaluation matrix, and identifies six gaps: benchmark design, dynamic testing, cross-market evidence, interpretability, generative validation, and full-text evidence. The findings are corpus-scoped; no method ranking is implied.

**Keywords:** implied volatility surface; no-arbitrage; SVI; neural networks; generative models; model calibration; literature review

## 摘要

构建无套利隐含波动率曲面（IVS）是衍生品定价的核心问题。本文以结构化文献综述方式综合 40 项来源（30 篇同行评议论文、10 篇预印本；2009–2026），通过 24 条 OpenAlex 查询检索，并在元数据/摘要层面评估。本文不以方法家族为唯一组织维度，而是按无套利约束进入构建流程的位置分类：构造约束、惩罚约束、投影/修复约束、生成/过滤约束。参数化 SVI/SSVI/eSSVI 模型给出显式的静态无套利条件，但可能缺乏灵活性；非参数、神经网络与生成式方法依赖软惩罚、硬结构、两步投影或事后修复，其保证因方法而异，且动态一致性常未被检验。动态无套利标准化程度较低、评估较少；静态可容许是必要条件而非充分条件。评估维度碎片化：拟合指标占主导，检索摘要中未发现同时覆盖违规、样本外稳定性、翼部行为、计算成本与可解释性的共享基准。本文提出四类约束执行分类与七维评估矩阵，并识别六个缺口：基准设计、动态检验、跨市场证据、可解释性、生成模型验证与全文证据。结论限定于本语料，不构成方法排序。

**关键词：** 隐含波动率曲面；无套利；SVI；神经网络；生成模型；模型校准；文献综述

---

## 1. Introduction

### 1.1 Context

The implied volatility surface is the mapping from option strikes and maturities to the volatility implied by observed prices. It is used for pricing, risk management, scenario generation, and model calibration. A surface that admits static arbitrage contains internal inconsistencies—violations of butterfly (strike-convexity) or calendar (maturity-monotonicity) conditions—that can be exploited by a static portfolio. A surface that admits dynamic arbitrage is inconsistent with a joint martingale model for the underlying and the surface over time. Both forms of arbitrage matter, but they are different constraints and are enforced by different methods (Gatheral & Jacquier, 2014<!--ref:src-01--><!--anchor:section:Abstract-->; Fengler, 2009<!--ref:src-03--><!--anchor:section:Abstract-->).

Three broad families dominate construction. Parametric models impose a functional form—SVI, SSVI, eSSVI, or random-coefficient extensions—and constrain its parameters (Gatheral & Jacquier, 2014<!--ref:src-01--><!--anchor:section:Abstract-->; Guo et al., 2016<!--ref:src-02--><!--anchor:section:Abstract-->; Martini & Mingone, 2022<!--ref:src-32--><!--anchor:section:Abstract-->; Mingone, 2022<!--ref:src-33--><!--anchor:section:Abstract-->; Zaugg et al., 2025<!--ref:src-31--><!--anchor:section:Abstract-->). Nonparametric models use splines, PCA, Gaussian processes, kriging, symbolic regression, or constrained optimization (Fengler, 2009<!--ref:src-03--><!--anchor:section:Abstract-->; Avellaneda et al., 2020<!--ref:src-12--><!--anchor:section:Abstract-->; Zhuang & Wu, 2026<!--ref:src-28--><!--anchor:section:Abstract-->; Yao et al., 2026<!--ref:src-29--><!--anchor:section:Abstract-->; Luo & Yu, 2023<!--ref:src-34--><!--anchor:section:Abstract-->; Appana et al., 2024<!--ref:src-36--><!--anchor:section:Abstract-->; Cousin & Gueye, 2021<!--ref:src-39--><!--anchor:section:Abstract-->). Neural and generative models learn the surface or its dynamics with multilayer networks, neural SDEs, variational autoencoders, generative adversarial networks, normalizing flows, or operator learning (Ackerer et al., 2019<!--ref:src-05--><!--anchor:section:Abstract-->; Bayer & Stemper, 2018<!--ref:src-06--><!--anchor:section:Abstract-->; Ning et al., 2023<!--ref:src-13--><!--anchor:section:Abstract-->; Horvath et al., 2021<!--ref:src-14--><!--anchor:section:Abstract-->; Vuletić & Cont, 2025<!--ref:src-16--><!--anchor:section:Abstract-->).

The three method families are a different axis from the four enforcement families in §2.6: a method family can use more than one enforcement mechanism, and the taxonomy classifies the mechanism that carries the guarantee.

### 1.2 Problem Statement

The literature is large and method-specific, but it lacks a shared vocabulary for what a construction guarantees. “Arbitrage-free” may mean that the surface is generated inside an admissible parametric region, that a penalty term reduced violations during training, that a second step projects the prediction onto a constrained set, or that a post-hoc repair algorithm removed detected arbitrage. These are not equivalent guarantees. The ambiguity is compounded by heterogeneous evaluation: papers report fit errors, violation counts, stability, wing behaviour, cost, or interpretability on different data and with different definitions. The result is that cross-paper claims of superiority are difficult to justify, and practitioners lack a compact map from method family to guarantee, evidence strength, and failure mode.

### 1.3 Purpose and Research Question

This review synthesizes the construction and evaluation literature for equity-index implied volatility surfaces, with emphasis on how no-arbitrage is enforced and what trade-offs are reported. The research question is:

> How do parametric, nonparametric, and neural methods for constructing equity-index implied volatility surfaces enforce static and dynamic no-arbitrage constraints, and what trade-offs do they report across fit, stability, extrapolation, computational cost, and interpretability?

The review has three aims: (a) organize the literature by where the constraint enters the construction pipeline; (b) assess the strength of the evidence for each family at abstract level; and (c) identify gaps that a shared research programme should address.

### 1.4 Significance

For researchers, the review offers a taxonomy that separates construction, penalty, projection/repair, and generation/filtering, and it identifies where the evidence is thin. For practitioners, it makes explicit that the choice of method is also a choice of guarantee: a parametric surface may be arbitrage-free by construction but inflexible; a neural surface may fit better but require a repair step; a generative model may produce plausible surfaces but lack independent dynamic validation. For benchmark designers, it proposes seven evaluation dimensions that any cross-method comparison should report.

---

### 1.5 Contribution and Positioning

This review makes three contributions. First, it replaces a method-family list with an enforcement taxonomy: the same construction pipeline can be classified by whether the guarantee is carried by construction, penalty, projection/repair, or generation plus filtering (§2.6). Second, it separates static from dynamic no-arbitrage and treats the latter as a distinct, under-tested layer rather than an extension of the former. Third, it consolidates the evaluation dimensions that the corpus reports unevenly into a seven-dimension matrix (§4.5, Table 4).

The review is closest to three bodies of work. Homescu (2011)<!--ref:src-04--><!--anchor:section:Abstract--> surveys construction methodologies and makes the constraint taxonomy explicit; Ruf and Wang (2020)<!--ref:src-08--><!--anchor:section:Abstract--> review neural option pricing and hedging and find no common benchmark; the no-arbitrage SVI literature (Gatheral & Jacquier, 2014<!--ref:src-01--><!--anchor:section:Abstract-->; Guo et al., 2016<!--ref:src-02--><!--anchor:section:Abstract-->; Martini & Mingone, 2022<!--ref:src-32--><!--anchor:section:Abstract-->) supplies the explicit static conditions. This review differs in three respects: it covers parametric, nonparametric, neural, and generative methods in one frame; it treats enforcement mechanism, not method family, as the organizing variable; and it maps evidence strength and evaluation gaps rather than only describing models.

The contribution is deliberately modest. The review does not propose a new arbitrage theory, a new estimator, or a validated benchmark. The four-family taxonomy is interpretive; the seven-dimension matrix is a proposal; the corpus is 40 sources assessed at metadata/abstract level, and no full texts were read. The paper is therefore a corpus-scoped map and a set of testable propositions, not a ranking or a solution. The primary reader is a model-risk/model-validation analyst or a benchmark designer; the paper is written for a general finance/quant-finance review venue, not a top-three empirical journal. This positioning is restated in §5.4, §5.5, and §6.

## 2. Literature Review and Theoretical Framework

### 2.1 Static No-Arbitrage and Parametric Surfaces

Static no-arbitrage is a shape constraint on a single surface. In the strike dimension, call prices must be convex and their density non-negative; in the maturity dimension, total implied variance must be non-decreasing. Parametric SVI-type models translate these conditions into restrictions on parameters or into closed-form inequalities. Gatheral and Jacquier (2014)<!--ref:src-01--><!--anchor:section:Abstract--> give explicit conditions for the raw SVI parameterization and for SSVI; Guo et al. (2016)<!--ref:src-02--><!--anchor:section:Abstract--> generalize the arbitrage-free SVI construction; Martini and Mingone (2022)<!--ref:src-32--><!--anchor:section:Abstract--> and Mingone (2022)<!--ref:src-33--><!--anchor:section:Abstract--> develop no-arbitrage SVI and eSSVI parameterizations. Zaugg et al. (2025)<!--ref:src-31--><!--anchor:section:Abstract--> add random coefficients to recover analytic flexibility while retaining explicit constraints. Homescu (2011)<!--ref:src-04--><!--anchor:section:Abstract--> surveys construction methodologies and makes the constraint taxonomy explicit.

The strength of this literature is that the guarantee is structural: if the calibrated parameters lie in the admissible region, the surface is arbitrage-free by construction. The limitation is equally structural: the admissible region can be conservative, and fit quality in sparse wings may suffer. Fengler (2009)<!--ref:src-03--><!--anchor:section:Abstract--> approaches the problem from constrained smoothing rather than a parametric family, and the contrast is instructive: smoothing can adapt to the data but must solve a constrained optimization problem, while a parametric family encodes the constraint in its parameterization but restricts the shape.

### 2.2 Nonparametric and Constrained Smoothing

Nonparametric methods trade a closed-form guarantee for flexibility. Fengler’s constrained least-squares smoother is an early benchmark (Fengler, 2009<!--ref:src-03--><!--anchor:section:Abstract-->). Avellaneda et al. (2020)<!--ref:src-12--><!--anchor:section:Abstract--> use PCA to represent the surface in a low-dimensional factor space; Zhuang and Wu (2026)<!--ref:src-28--><!--anchor:section:Abstract--> combine a SABR-informed source with a multitask Gaussian process to stabilize sparse wings; Yao et al. (2026)<!--ref:src-29--><!--anchor:section:Abstract--> formulate a joint cubic-spline quadratic program for American call and put surfaces with linear arbitrage constraints. Luo and Yu (2023)<!--ref:src-34--><!--anchor:section:Abstract--> apply symbolic regression, Appana et al. (2024)<!--ref:src-36--><!--anchor:section:Abstract--> use Gaussian processes, and Cousin and Gueye (2021)<!--ref:src-39--><!--anchor:section:Abstract--> use kriging.

These methods are attractive when the data are sparse or when uncertainty quantification is required: Gaussian-process and kriging estimators return a posterior distribution, not only a point surface. The guarantee, however, is method-specific. A constrained spline or quadratic program can enforce static conditions; a generic GP or kriging estimator does not, unless the constraint is built into the prior or the projection step. The corpus does not compare these alternatives under a common probabilistic scoring rule.

### 2.3 Neural and Generative Approaches

Neural methods learn the map from market observables or model parameters to the surface. The literature contains five recurring design patterns. First, soft penalties add an arbitrage term to the training loss (Ackerer et al., 2019<!--ref:src-05--><!--anchor:section:Abstract-->; Cao et al., 2020<!--ref:src-09--><!--anchor:section:Abstract-->; Zhang et al., 2022<!--ref:src-15--><!--anchor:section:Abstract-->). Second, hard or gated architectures restrict the function class so that rationality holds by design (Yang et al., 2017<!--ref:src-07--><!--anchor:section:Abstract-->; Anagha, 2026<!--ref:src-40--><!--anchor:section:Abstract-->). Third, two-step pipelines predict a surface and then project or adjust it (Zhang et al., 2022<!--ref:src-15--><!--anchor:section:Abstract-->; Cohen et al., 2020<!--ref:src-10--><!--anchor:section:Abstract-->). Fourth, post-hoc repair detects and removes arbitrage from observed or predicted prices (Cohen et al., 2020<!--ref:src-10--><!--anchor:section:Abstract-->; Xiong & Liu, 2026<!--ref:src-27--><!--anchor:section:Abstract-->; Neufeld & Sester, 2024<!--ref:src-26--><!--anchor:section:Abstract-->). Fifth, generative models—VAEs, GANs, flows, and operator models—generate surfaces and rely on a filter or repair step for admissibility (Ning et al., 2023<!--ref:src-13--><!--anchor:section:Abstract-->; Vuletić & Cont, 2025<!--ref:src-16--><!--anchor:section:Abstract-->; Ginart Belmonte & Cole, 2025<!--ref:src-22--><!--anchor:section:Abstract-->; Bajalica et al., 2026<!--ref:src-23--><!--anchor:section:Abstract-->; Wang et al., 2025<!--ref:src-24--><!--anchor:section:Abstract-->; Wiedemann et al., 2024<!--ref:src-35--><!--anchor:section:Abstract-->; Zetocha, 2023<!--ref:src-38--><!--anchor:section:Abstract-->).

The reported advantages are faster calibration (Bayer & Stemper, 2018<!--ref:src-06--><!--anchor:section:Abstract-->; Bayer et al., 2025<!--ref:src-21--><!--anchor:section:Abstract-->), improved fit in some settings (Liu et al., 2019<!--ref:src-11--><!--anchor:section:Abstract-->; Zheng et al., 2021<!--ref:src-20--><!--anchor:section:Abstract-->; Medvedev & Wang, 2021<!--ref:src-19--><!--anchor:section:Abstract-->), and plausible generated surfaces (Ning et al., 2023<!--ref:src-13--><!--anchor:section:Abstract-->; Vuletić & Cont, 2025<!--ref:src-16--><!--anchor:section:Abstract-->). The reported costs are constraint violations under distribution shift, unstable extrapolation in sparse wings, and limited interpretability. The evidence is unevenly distributed: 10 of the 40 sources are preprints, and several neural claims are supported at abstract level only.

### 2.4 Dynamic No-Arbitrage

Dynamic no-arbitrage requires consistency between the surface and the underlying over time. It is a joint martingale condition, not a shape condition on a single surface. Cont and Vuletić (2023)<!--ref:src-17--><!--anchor:section:Abstract--> construct arbitrage-free surface simulations; Cohen et al. (2023)<!--ref:src-18--><!--anchor:section:Abstract--> develop neural-SDE market models; Vuletić and Cont (2025)<!--ref:src-16--><!--anchor:section:Abstract--> extend the generative approach; Andrès et al. (2026)<!--ref:src-30--><!--anchor:section:Abstract--> argue that the surface is path-dependent, which changes the object that a dynamic model must reproduce. The dynamic literature is much smaller than the static literature in this corpus, and most neural papers evaluate static violations only.

The key theoretical point is that static no-arbitrage is necessary but not sufficient. A surface can pass butterfly and calendar checks and still be inconsistent with a joint model of the underlying and the surface. The corpus does not contain a shared dynamic test, and the dynamic papers use different state variables and different notions of consistency.

### 2.5 Evaluation, Detection, and Repair

Evaluation is the connective tissue of the literature. Ruf and Wang (2020)<!--ref:src-08--><!--anchor:section:Abstract--> review neural option-pricing and hedging methods and find no common benchmark. Cohen et al. (2020)<!--ref:src-10--><!--anchor:section:Abstract--> detect and repair arbitrage in traded option prices; Neufeld and Sester (2024)<!--ref:src-26--><!--anchor:section:Abstract--> use neural networks to detect model-free static arbitrage; Xiong and Liu (2026)<!--ref:src-27--><!--anchor:section:Abstract--> anchor repair to observations for sparse surfaces. These papers make the evaluation problem visible: if violations are common enough to require repair, then a construction that reports only fit error is incomplete.

### 2.6 Theoretical Framework: A Four-Family Enforcement Taxonomy

The review organizes the literature by where the constraint enters the pipeline:

1. **Constraint by construction.** The admissible region is part of the model: SVI/SSVI/eSSVI parameter restrictions, gated or architectural networks. The guarantee is structural; the cost is fit flexibility and a potentially conservative admissible region.
2. **Constraint by penalty.** A soft loss penalizes violations during training. The method is flexible and easy to optimize; the guarantee is absent at inference, and performance can degrade under distribution shift.
3. **Constraint by projection or repair.** A predicted or observed surface is projected onto the arbitrage-free set, or repaired minimally. The guarantee is post-hoc and depends on the projection/repair rule; observation fidelity may be traded for admissibility.
4. **Constraint by generation and filtering.** A generative model proposes surfaces and a filter or repair step enforces constraints. The guarantee is only as good as the filter; dynamic consistency is usually untested.

This taxonomy is an interpretive contribution of the review, not a claim that the literature uses these labels. It explains why the same word—“arbitrage-free”—can refer to different guarantees and why cross-paper comparisons are difficult. The taxonomy also generates testable expectations: construction methods should be stable but potentially inflexible; penalty methods should be flexible but vulnerable to shift; projection methods should be accurate but sensitive to the repair rule; generative methods should be plausible but dependent on validation.

The four families describe the primary mechanism that carries the guarantee; a method may combine stages. A two-step predictor/projection is penalty plus projection; a generative model with a repair step is generation plus filtering; a gated network with a post-hoc repair is construction plus projection. A hybrid is classified by the mechanism that carries the guarantee, not by every step in its pipeline.

---

## 3. Methodology

### 3.1 Research Design

This is a structured literature review in `deep-research` full mode. It is not a PRISMA-compliant systematic review, and no PRISMA or PRISMA-ScR compliance is claimed. The unit of analysis is a source that constructs, evaluates, or repairs an equity-index implied volatility surface with an explicit or implicit no-arbitrage objective. The review combines a reproducible search, metadata/abstract extraction, source verification, thematic synthesis, a Devil’s Advocate checkpoint, and a narrative report.

**Review type.** This is a structured narrative review with a frozen corpus. It is not a systematic review, not PRISMA-compliant, and not registered. The 351 → 40 flow is a screening rationale, not a record-level audit.

### 3.2 Search Strategy

The primary discovery source was OpenAlex, queried with 24 full-text search strings on 2026-11-19 (Asia/Singapore). Each query returned up to 25 records; after DOI/title deduplication, 351 unique records remained. The conceptual Boolean string combined surface terms (“implied volatility surface” or “volatility surface”), arbitrage terms (“arbitrage-free”, “no-arbitrage”, “static arbitrage”, “calendar arbitrage”, “butterfly arbitrage”), and method terms (“SVI”, “SSVI”, “parametric”, “nonparametric”, “neural network”, “deep learning”, “generative”, “Gaussian process”). Crossref was used for metadata and DOI checks (10 targeted lookups; four abstracts recovered; one HTTP 429). Semantic Scholar was attempted for title/DOI verification and abstract completion (10 requests; all HTTP 429). arXiv, SSRN, and publisher pages supplied five spot-check abstracts. No Web of Science, Scopus, or institutional database access was available.

The date range was 2015-01-01 to 2026-11-19. Pre-2015 seminal works were admitted only when they define a construction or constraint used by later work (Fengler, 2009<!--ref:src-03--><!--anchor:section:Abstract-->; Homescu, 2011<!--ref:src-04--><!--anchor:section:Abstract-->; Gatheral & Jacquier, 2014<!--ref:src-01--><!--anchor:section:Abstract-->). Included sources were equity-index or option-surface construction papers with a static/dynamic no-arbitrage contribution, a parametric/nonparametric/neural/generative method, or an evaluation/repair contribution; English-language; peer-reviewed or credible preprint. Excluded were pure option-pricing papers without surface construction, local/stochastic-volatility calibration without a surface/arbitrage contribution, crypto/FX applications unless the method transfers directly, practitioner blogs and vendor notes, and papers with no arbitrage or surface focus.

### 3.3 Screening and Corpus

Of the 351 unique records, 311 were not advanced after title/abstract screening (off-topic, duplicate, no surface/arbitrage focus, non-English, or outside scope). Forty records were assessed at metadata/abstract level and included; no full texts were assessed. The corpus contains 30 peer-reviewed articles or conference papers and 10 preprints (75%/25%), above the 60% peer-reviewed floor. Twenty-eight sources (70%) are from 2021–2026 and 12 (30%) are pre-2021, including seminal work; the currency distribution is at the 30% cap and does not trigger an advisory. The method mix is neural/generative 18 (45%), constraints/evaluation 8 (20%), parametric 7 (17.5%), nonparametric 6 (15%), and dynamics 1 (2.5%). No single method exceeds 70%. The 311 non-advanced records were not individually coded; Appendix C gives the screening rationale, and the counts should be read as a rationale rather than a full excluded-record log. No full-text screening was performed.

**Table 1.** Corpus composition by method family

| Family | N | Peer-reviewed | Preprints | Representative sources |
|---|---:|---:|---:|---|
| Parametric | 7 | 6 | 1 | Gatheral & Jacquier (2014); Guo et al. (2016); Fengler (2009); Zaugg et al. (2025) |
| Nonparametric / GP | 6 | 4 | 2 | Avellaneda et al. (2020); Zhuang & Wu (2026); Yao et al. (2026); Appana et al. (2024) |
| Neural / generative | 18 | 12 | 6 | Ackerer et al. (2019); Ning et al. (2023); Vuletić & Cont (2025); Zhang et al. (2022) |
| Constraints / evaluation | 8 | 7 | 1 | Yang et al. (2017); Ruf & Wang (2020); Cohen et al. (2020); Neufeld & Sester (2024) |
| Dynamics | 1 | 1 | 0 | Andrès et al. (2026) |
| **Total** | **40** | **30** | **10** | |

### 3.4 Data Extraction and Verification

For each included source, the review extracted title, authors, year, venue, DOI, source type, citation count, and abstract. The OpenAlex DOI endpoint resolved all 40 records; 39 have a DOI and one (Cousin & Gueye, 2021<!--ref:src-39--><!--anchor:section:Abstract-->) is a HAL record without a DOI. Abstract coverage is 35 full, four partial publisher/web snippets (Cao et al., 2020<!--ref:src-09--><!--anchor:section:Abstract-->; Neufeld & Sester, 2024<!--ref:src-26--><!--anchor:section:Abstract-->; Zhuang & Wu, 2026<!--ref:src-28--><!--anchor:section:Abstract-->; Yao et al., 2026<!--ref:src-29--><!--anchor:section:Abstract-->), and one title-level-only record (Horvath et al., 2021<!--ref:src-14--><!--anchor:section:Abstract-->). OpenAlex marked zero retracted records; no fabricated reference was found; no predatory-journal alert was raised at metadata level. No COI or funding audit was possible from the retrieved metadata.

### 3.5 Analytical Approach

The analysis proceeded in five steps: (a) an evidence matrix mapping each source to themes, method family, and evidence level; (b) convergence/divergence analysis, with themes requiring at least three sources and silence noted where fewer than two sources address a point; (c) contradiction analysis, distinguishing genuine tensions from conditional differences and method-class differences; (d) a cross-paper tension inventory, with seven candidate pairs assessed and a coverage note; and (e) a Devil’s Advocate checkpoint that tested cherry-picking, confirmation bias, missing evidence, alternative explanations, and inclusion-criteria sensitivity. Evidence levels follow the corpus grading: Level VI for a single peer-reviewed study and Level VII for a preprint, review, or working paper. No meta-analysis was performed; the synthesis is narrative.

### 3.6 Validity, Ethics, and Limitations

Validity rests on a reproducible search, DOI/title checks, explicit inclusion/exclusion criteria, and a source-level evidence matrix. The main threats are abstract-level evidence (no full texts), the 40/351 selection, 10 preprints, Semantic Scholar rate-limiting, no COI audit, and a corpus concentrated on SPX/US equity-index options. The review has no human subjects, no proprietary data, and no personal data. The AI-assisted pipeline and the author’s oversight are disclosed below. These limitations are carried into the Discussion rather than treated as resolved.

---

**Scope and excluded streams.** The review does not systematically cover rough-volatility models, stochastic-volatility calibration, American options beyond one source, crypto/FX surfaces, or reinforcement-learning approaches. These are candidate extensions, not silent omissions; the 40-source corpus is the boundary of the claims.

### 3.7 Screening Audit and Reproducibility

The screening counts are a rationale, not a full audit. The 24 OpenAlex queries, the deduplication and selection scripts, and the frozen 40-source metadata are in `examples/dsh/iv-surface-review/search/` (`openalex_search.py`, `fetch_selected.py`, `selected_sources.json`). The search returned 351 unique records; 311 were not advanced after title/abstract screening; 40 were assessed at metadata/abstract level and included; no full text was assessed. The 311 non-advanced records were not individually coded, and the exclusion reasons are category-level: off-topic, duplicate, no surface/arbitrage focus, insufficient methodological relevance, or non-English. Appendix C gives the flow and the reproducibility note.

This is a reproducibility limit, not a claim that the 40 sources are exhaustive. A systematic review would register a protocol, double-screen titles and abstracts, retain a record-level excluded list, and assess full texts for method and evidence quality. This review does none of those things. The corpus is a purposive, reproducible-but-not-exhaustive sample; re-running the search on a different date, database, or query set may add sources, especially for dynamic no-arbitrage, which the 24 queries may under-cover. The 40 included records are frozen in `search/selected_sources.json`; the counts in Table 1 and Appendix C describe that frozen set.

## 4. Findings

### 4.1 Corpus and Evidence Base

The corpus contains 40 sources: 30 peer-reviewed articles or conference papers and 10 preprints. Twenty-eight sources (70%) are from 2021–2026; 12 (30%) are older, including the seminal parametric and smoothing work. The method mix is neural/generative 18, constraints/evaluation 8, parametric 7, nonparametric 6, and dynamics 1 (Table 1). Abstract coverage is 35 full, four partial, and one title-level-only record. OpenAlex resolved all 40 records; 39 have a DOI and one is a HAL record without a DOI. No retracted record was flagged and no fabricated reference was found. These counts describe the evidence base, not its quality; the quality assessment is source-level and abstract-level.

### 4.2 Finding 1: Static No-Arbitrage Is Well-Characterized for Parametric Surfaces, Not Solved

The parametric literature provides the clearest guarantee in the corpus. SVI, SSVI, and eSSVI express static no-arbitrage as parameter restrictions or closed-form conditions (Gatheral & Jacquier, 2014<!--ref:src-01--><!--anchor:section:Abstract-->; Guo et al., 2016<!--ref:src-02--><!--anchor:section:Abstract-->; Martini & Mingone, 2022<!--ref:src-32--><!--anchor:section:Abstract-->; Mingone, 2022<!--ref:src-33--><!--anchor:section:Abstract-->). Zaugg et al. (2025)<!--ref:src-31--><!--anchor:section:Abstract--> extend the family with random coefficients; Fengler (2009)<!--ref:src-03--><!--anchor:section:Abstract--> provides a constrained-smoothing alternative; Homescu (2011)<!--ref:src-04--><!--anchor:section:Abstract--> supplies the survey taxonomy. The guarantee is structural—if the parameters are admissible, the surface is arbitrage-free—but it is conditional. The admissible region can be conservative, and fit quality in sparse wings can suffer. “Well-characterized” therefore means that the constraint language is explicit, not that every calibrated surface is acceptable. The review treats this as strong evidence for the parametric construction, but not as evidence that the construction problem is closed.

### 4.3 Finding 2: Neural and Generative Methods Multiply Enforcement Mechanisms Without a Common Comparison

Eighteen neural/generative sources and eight constraints/evaluation sources address enforcement. The mechanisms fall into four families (Table 2): construction (parametric restrictions or gated/architectural networks), penalty (soft loss), projection/repair (quadratic program, spline, or minimal adjustment), and generation plus filtering (VAE, GAN, flow, operator, or neural SDE with a constraint step). Representative construction work includes Yang et al. (2017)<!--ref:src-07--><!--anchor:section:Abstract--> and Anagha (2026)<!--ref:src-40--><!--anchor:section:Abstract-->; penalty work includes Ackerer et al. (2019)<!--ref:src-05--><!--anchor:section:Abstract-->, Cao et al. (2020)<!--ref:src-09--><!--anchor:section:Abstract-->, and Zhang et al. (2022)<!--ref:src-15--><!--anchor:section:Abstract-->; repair work includes Cohen et al. (2020)<!--ref:src-10--><!--anchor:section:Abstract-->, Xiong and Liu (2026)<!--ref:src-27--><!--anchor:section:Abstract-->, and Neufeld and Sester (2024)<!--ref:src-26--><!--anchor:section:Abstract-->; generative work includes Ning et al. (2023)<!--ref:src-13--><!--anchor:section:Abstract-->, Vuletić and Cont (2025)<!--ref:src-16--><!--anchor:section:Abstract-->, Ginart Belmonte and Cole (2025)<!--ref:src-22--><!--anchor:section:Abstract-->, Bajalica et al. (2026)<!--ref:src-23--><!--anchor:section:Abstract-->, Wang et al. (2025)<!--ref:src-24--><!--anchor:section:Abstract-->, Wiedemann et al. (2024)<!--ref:src-35--><!--anchor:section:Abstract-->, and Zetocha (2023)<!--ref:src-38--><!--anchor:section:Abstract-->.

The reported advantages are consistent in direction: neural surrogates reduce calibration time (Bayer & Stemper, 2018<!--ref:src-06--><!--anchor:section:Abstract-->; Bayer et al., 2025<!--ref:src-21--><!--anchor:section:Abstract-->), improve fit in some settings (Liu et al., 2019<!--ref:src-11--><!--anchor:section:Abstract-->; Zheng et al., 2021<!--ref:src-20--><!--anchor:section:Abstract-->; Medvedev & Wang, 2021<!--ref:src-19--><!--anchor:section:Abstract-->), and generate plausible surfaces (Ning et al., 2023<!--ref:src-13--><!--anchor:section:Abstract-->; Vuletić & Cont, 2025<!--ref:src-16--><!--anchor:section:Abstract-->). Intraday and calibration-specific designs add further evidence: Hoshisashi et al. (2024)<!--ref:src-25--><!--anchor:section:Abstract--> use a physics-informed network for intraday surfaces, and Hoshisashi et al. (2023)<!--ref:src-37--><!--anchor:section:Abstract--> develop no-arbitrage deep calibration for smile and skewness. The costs are also consistent: violations can reappear under distribution shift, wing extrapolation is unstable, and interpretability is limited. The critical caveat is that the mechanisms are not equivalent. A gated architecture may guarantee a property that a soft penalty only encourages; a two-step pipeline may restore admissibility while changing the prediction; a generative model may produce a plausible sample that fails an independent arbitrage test. The corpus does not contain a head-to-head comparison that holds data, metrics, and constraint definitions fixed, and 10 of the 40 sources are preprints. The evidence is therefore moderate, not settled.

**Table 2.** Constraint-enforcement families in the corpus

| Family | Mechanism | Guarantee | Representative sources | Main failure mode |
|---|---|---|---|---|
| Construction | Admissible parametric region; gated/architectural networks | Static, by construction | Gatheral & Jacquier (2014); Yang et al. (2017); Zaugg et al. (2025); Anagha (2026) | Conservative region; reduced fit flexibility |
| Penalty | Soft arbitrage term in the loss | None at inference | Ackerer et al. (2019); Cao et al. (2020); Zhang et al. (2022) | Violations under shift; weight sensitivity |
| Projection / repair | QP, spline, or minimal adjustment | Post-hoc static | Fengler (2009); Cohen et al. (2020); Xiong & Liu (2026) | Observation changes; repair-rule dependence |
| Generation + filter | VAE, GAN, flow, operator, neural SDE + constraint step | Filter-dependent | Ning et al. (2023); Vuletić & Cont (2025); Bajalica et al. (2026); Zetocha (2023) | Static-only validation; mode collapse |

**Table 2 note.** Families describe the mechanism that carries the guarantee; hybrids are classified by that mechanism (see §2.6).

### 4.4 Finding 3: Dynamic No-Arbitrage Is the Frontier—and the Evidence Is Thin

Only a small subset of the corpus engages dynamic consistency. Cont and Vuletić (2023)<!--ref:src-17--><!--anchor:section:Abstract--> construct arbitrage-free surface simulations; Cohen et al. (2023)<!--ref:src-18--><!--anchor:section:Abstract--> build neural-SDE market models; Vuletić and Cont (2025)<!--ref:src-16--><!--anchor:section:Abstract--> extend the generative approach; Andrès et al. (2026)<!--ref:src-30--><!--anchor:section:Abstract--> argue that the surface is path-dependent. These are different mechanisms, and they do not share a common definition of dynamic consistency. The review’s claim is deliberately weak: static no-arbitrage is necessary but not sufficient for dynamic no-arbitrage, and the corpus does not contain a shared dynamic test. The dynamic literature is also under-sampled: the 24 queries emphasized static-arbitrage vocabulary, and only a handful of records survived. The “frontier” label is therefore a statement about this corpus, not a universal claim about the field. One neural source, Horvath et al. (2021)<!--ref:src-14--><!--anchor:section:Abstract-->, is title-level only in this review; its findings are not used for a substantive dynamic claim. [MATERIAL GAP: full abstract unavailable for Horvath et al. (2021).]

**Table 3.** Dynamic-consistency evidence in the corpus

| Source | Mechanism | Dynamic test reported | Data | Result |
|---|---|---|---|---|
| Cont & Vuletić (2023) | Arbitrage-free surface simulation | Simulation consistency; no common test | Simulated | Construction; no independent benchmark |
| Cohen et al. (2023) | Neural-SDE market model | Joint surface–underlying consistency by construction | SPX | Construction; no common test |
| Vuletić & Cont (2025) | Generative (VolGAN) + filter | Static filter; dynamic validation limited | SPX | Filter-dependent; no common dynamic test |
| Andrès et al. (2026) | Path-dependent surface | Conceptual; no joint test | — | Argues path dependence; no test |
| Horvath et al. (2021) | Neural calibration | Not assessed (title-level) | — | Not used for a dynamic claim |

**Table 3 note.** “Dynamic” means a joint surface–underlying or time-consistency test, not a static butterfly/calendar check. The table is the evidence behind the “frontier” label; it is thin by design.

### 4.5 Finding 4: Evaluation Is Fragmented and No Shared Benchmark Was Identified

The evaluation landscape is heterogeneous. Fit metrics (RMSE, MAPE, implied-volatility error) dominate; arbitrage violations, out-of-sample stability, wing behaviour, computational cost, and interpretability are reported inconsistently. The repair and detection literature makes the gap concrete: Cohen et al. (2020)<!--ref:src-10--><!--anchor:section:Abstract--> detect and repair arbitrage in traded prices; Neufeld and Sester (2024)<!--ref:src-26--><!--anchor:section:Abstract--> use neural networks to detect model-free static arbitrage; Xiong and Liu (2026)<!--ref:src-27--><!--anchor:section:Abstract--> anchor repair to observations for sparse surfaces. Ruf and Wang (2020)<!--ref:src-08--><!--anchor:section:Abstract--> review the neural option-pricing literature and find no common benchmark. The review’s synthesis is that a shared evaluation matrix should report at least seven dimensions: fit, static violations, dynamic consistency, out-of-sample stability, wing behaviour, computational cost, and interpretability (Table 4). The corpus supplies pieces of this matrix but no paper reports all seven on a common dataset. “No shared benchmark identified in the retrieved abstracts” is a gap hypothesis, not a claim that no benchmark exists anywhere.

**Table 4.** Evaluation dimensions and reporting gaps

| Dimension | Representative metrics | Reporting in corpus | Gap |
|---|---|---|---|
| Fit | RMSE, MAPE, IV error | Common | Different data, weights, and error definitions |
| Static arbitrage | Butterfly/calendar violations | Common in constraint papers | Violation definitions and tolerances vary |
| Dynamic consistency | Joint surface–underlying tests | Rare | No shared dynamic test |
| Out-of-sample stability | Train/test or temporal split | Uneven | No common split or stress period |
| Wing behaviour | Sparse-strike error | Method-specific | No standard wing metric |
| Computational cost | Calibration/inference time | Uneven | No common budget or hardware |
| Interpretability | Parameter meaning, attention, rules | Uneven | No accepted metric |

The matrix is diagnostic, not causal. A method can score well on fit and poorly on static violations, or vice versa; the dimensions are not a composite index, and no weighting is proposed. The corpus reports fit and static violations most often, out-of-sample stability and wings less often, and cost and interpretability rarely. This pattern is itself a finding: the field measures what is easy to compute, not what a risk manager needs. A shared benchmark would need to report all seven dimensions, including failures, rather than select the dimension on which a method performs best.

### 4.6 Finding 5: Flexibility, Uncertainty, and Data Coverage Trade Guarantees for Adaptability

The nonparametric group—PCA (Avellaneda et al., 2020<!--ref:src-12--><!--anchor:section:Abstract-->), Gaussian processes (Appana et al., 2024<!--ref:src-36--><!--anchor:section:Abstract-->), kriging (Cousin & Gueye, 2021<!--ref:src-39--><!--anchor:section:Abstract-->), symbolic regression (Luo & Yu, 2023<!--ref:src-34--><!--anchor:section:Abstract-->), SABR-informed multitask GP (Zhuang & Wu, 2026<!--ref:src-28--><!--anchor:section:Abstract-->), and joint American call/put smoothing (Yao et al., 2026<!--ref:src-29--><!--anchor:section:Abstract-->)—offers flexibility, and in the GP/kriging cases a posterior uncertainty. The guarantee is not uniform: a constrained spline or quadratic program can enforce static conditions; a generic GP or kriging estimator does not, unless the constraint is built into the prior or a projection step. The data motivation is recurrent: several methods target sparse wings or incomplete surfaces, and neural experiments often use simulated or synthetic data. The corpus is SPX/US-equity-index heavy; cross-market evidence is thin. The practical implication is conditional: nonparametric methods are attractive when uncertainty and adaptability matter, but the user must check whether the specific estimator carries a constraint guarantee.

### 4.7 Cross-Paper Tensions

Seven candidate pairs were assessed in the synthesis. Five were resolved as conditional differences or method-class differences; one was flagged unresolved; one was not applicable because the pair addresses different mechanisms (Table 5). The unresolved pair is the tension between generative claims of realistic arbitrage-free surfaces and the absence of independent dynamic/out-of-sample validation. The review does not claim that all contradictions are resolved; it reports the coverage and the residual flag.

**Table 5.** Cross-paper tension summary

| Pair | Tension | Assessment | Status |
|---|---|---|---|
| CP-001 | Gated/hard construction vs soft penalty (Yang et al., 2017 vs Ackerer et al., 2019) | Conditional difference | Resolved in synthesis |
| CP-002 | Smoothing vs minimal repair (Fengler, 2009 vs Cohen et al., 2020) | Objective-dependent | Resolved in synthesis |
| CP-003 | Two-step outperformance vs no shared benchmark identified in the retrieved abstracts (Zhang et al., 2022 vs Ruf & Wang, 2020) | Scope difference | Resolved in synthesis |
| CP-004 | Generative realism vs absence of independent validation (Vuletić & Cont, 2025 vs Cohen et al., 2020) | Indirect tension | Flagged unresolved |
| CP-005 | Static guarantee vs neural penalty (Gatheral & Jacquier, 2014 vs Ackerer et al., 2019) | Method-class difference | Resolved in synthesis |
| CP-006 | Simulation vs path-dependent dynamics (Cont & Vuletić, 2023 vs Andrès et al., 2026) | No material conflict | Not applicable |
| CP-007 | GP uncertainty vs controllable generation (Appana et al., 2024 vs Wang et al., 2025) | No material conflict | Not applicable |

**Table 5 note.** CP-004 is indirect: Cohen et al. (2020) is a repair study, not a direct test of generated surfaces; the tension is between generative claims and the absence of independent validation. CP-003 is a scope difference: the two-step result is benchmark-specific, while Ruf and Wang’s negative finding is corpus-wide.

### 4.8 Summary of Findings

The five findings are connected by one argument: “arbitrage-free” is not a single property. Parametric construction supplies an explicit static guarantee; nonparametric methods supply flexibility and sometimes uncertainty; neural and generative methods supply fit or generation at the cost of a weaker or post-hoc guarantee; dynamic consistency is a separate, under-tested layer; and evaluation does not yet support cross-family ranking. The four-family taxonomy in Section 2.6 is the integrating device, and the seven-dimension evaluation matrix is the practical implication.

---

## 5. Discussion

### 5.1 From “Arbitrage-Free” to “Which Guarantee?”

The most important interpretive move is to replace the binary question—“is the surface arbitrage-free?”—with a question about the guarantee: by construction, by penalty, by projection, or by generation plus filtering? Each answer implies a different failure mode. Construction methods can be conservative and inflexible; penalty methods can violate constraints under distribution shift; projection methods can change observations and depend on the repair rule; generative methods can produce plausible samples that fail independent tests. This taxonomy explains the apparent contradictions in the literature: papers that use the same phrase are often making different claims. It also explains why a single fit metric cannot adjudicate between them.

### 5.2 Theoretical Implications

The taxonomy treats constraint enforcement as a design dimension, not an implementation detail. It generates four testable propositions for future work. First, construction methods should be more stable but less flexible than penalty methods on sparse wings. Second, penalty methods should degrade more under distribution shift than construction or projection methods. Third, projection/repair methods should be accurate on observed points but sensitive to the repair rule and to observation noise. Fourth, generative methods should be plausible in-sample but dependent on the filter for admissibility and on independent tests for dynamic consistency. These propositions are not tested in the corpus; they are a research agenda, not findings. The static/dynamic distinction adds a second dimension: a method can be strong on static constraints and silent on dynamic ones, and most neural papers are in that position.

The taxonomy also reframes the theoretical debate. The question is not whether neural networks “can” be arbitrage-free, but which mechanism carries the guarantee and what that mechanism assumes. A hard architecture encodes the constraint in the function class; a penalty assumes the optimizer finds the feasible region; a projection assumes the repair map is idempotent and stable; a generator assumes the filter catches what the generator misses. These are different theoretical commitments, and they fail differently. Recognizing the commitment is more useful than ranking the family.

**Table 6.** Testable propositions

| # | Proposition | What would support it | What would falsify it |
|---|---|---|---|
| P1 | Construction methods are more stable but less flexible than penalty methods on sparse wings. | Controlled comparison on common data. | Construction loses stability or wins flexibility. |
| P2 | Penalty methods degrade more under distribution shift. | Shift tests with a fixed architecture. | Penalty matches construction under shift. |
| P3 | Projection/repair is accurate on observed points but sensitive to the repair rule. | Repair-rule ablation. | Accuracy is rule-invariant. |
| P4 | Generative surfaces are filter-dependent for admissibility. | Remove the filter; measure violations. | The generator alone is admissible. |
| P5 | Dynamic consistency is not implied by static admissibility. | Joint test on a static-admissible surface. | Static-admissible surfaces pass all dynamic tests. |
| P6 | Evaluation fragmentation biases method comparisons. | Meta-analysis of metrics. | Metrics converge across studies. |

**What would change this map.** A method that carries a guarantee through a fifth mechanism, a demonstration that static admissibility implies dynamic consistency on a common test, or a full-text review showing that the abstract-level classification misassigns a substantial share of the 40 sources. None of these is in the corpus; they are the falsifiers the map invites.

### 5.3 Practical Implications

For practitioners, the choice of method is a choice of guarantee. A desk that needs a provably static-arbitrage-free surface for pricing may prefer a parametric or constrained-smoothing construction, accepting fit limitations. A desk that needs flexible scenario generation may prefer a neural or generative model, but should add a static repair step and an independent dynamic check. For model risk, the review recommends reporting the guarantee family, the static and dynamic test results, and the evaluation dimensions in Table 4. For benchmark designers, the seven dimensions are proposed as a minimum reporting standard, not a validated instrument. For regulators, the absence of a shared benchmark may warrant supervisory attention; this review does not evaluate regulatory practice or establish that “arbitrage-free” claims are incomparable in all settings.

The following decision guide is a proposed aid, not a validated selection rule. It restates the taxonomy in practitioner terms and should be read with the evidence caveats in §5.4.

**Table 7.** A proposed decision guide by guarantee family. The table is an aid, not a validated selection rule or a ranking.

| Decision question | Parametric SVI/SSVI/eSSVI | Nonparametric / GP / spline | Neural / generative |
|---|---|---|---|
| Is a static guarantee needed? | Yes, if parameters are in the admissible region | Only if the estimator or projection enforces it | Only with hard construction, projection, or repair |
| Is uncertainty quantification needed? | No, unless a Bayesian extension is used | GP/kriging can provide a posterior | Usually no; ensembles are not a guarantee |
| Are the wings sparse? | May be inflexible; fit can suffer | GP/MTGP/spline methods target this case | Data-hungry; repair is often needed |
| Is dynamic consistency needed? | Not automatic | Not automatic | Not automatic; rarely tested |
| Is interpretability a priority? | High: parameters have meaning | Medium: depends on the basis | Low: post-hoc explanation is required |
| Is calibration cost a constraint? | Low-dimensional; fast | Solver-dependent | Training/inference cost; surrogates can be fast |

No cell in this table is a ranking. The table is a decision aid for the guarantee family, not a claim that one family is superior.

**Use case.** A desk choosing between an SVI construction and a neural generator should first ask whether it needs a provable static guarantee or flexible generation. If the former, choose the construction and budget for fit limits; if the latter, add a repair step and an independent dynamic test. The guide does not validate either choice; it makes the trade-off explicit, and the guarantee family should be reported with the surface.

### 5.4 Limitations

The review has six main limitations. First, evidence is abstract-level: 35 full abstracts, four partial snippets, and one title-level record; no full texts were read, so method details and negative results may be missing. Second, the corpus is 40 of 351 unique records; 311 were not advanced, and the 24 queries emphasized static-arbitrage, parametric, and neural vocabulary, so dynamic-arbitrage coverage may be under-sampled. Third, 10 of the 40 sources are preprints; neural claims are weaker than the prose sometimes implies. Fourth, Semantic Scholar returned HTTP 429 for all 10 requests; Crossref returned one 429 and four abstracts; no COI or funding audit was possible. Fifth, the corpus is SPX/US-equity-index heavy; cross-market and stressed-period generalization is not established. Sixth, the review is narrative; no meta-analysis or effect-size synthesis was performed. A Devil’s Advocate checkpoint returned REVISE with five Major issues (selection/coverage bias, abstract/preprint evidence, the “no shared benchmark” overclaim, implied hard-constraint superiority, and “mature/solved” language). The five issues were addressed by hedging, scope caveats, and removing ranking language; the residual limits are disclosed rather than resolved. Funding: none was received for this review. Conflict of interest: none declared; a full COI audit was not possible from the retrieved metadata. No plagiarism scan and no full-text claim verification were performed.

The limitations are structural: a single-date, single-database, English-language corpus; a 40/351 selection that is not a full systematic-review screen; abstract-level evidence; 10 preprints; no COI/funding audit; and no plagiarism scan. The four-family taxonomy and the seven-dimension matrix are interpretive proposals, not validated instruments. These limits bound the claims: the paper maps the corpus and proposes a research agenda; it does not rank methods or certify surfaces.

### 5.5 Future Research

Six gaps follow directly from the findings; the agenda below turns each into a research design.

A research agenda follows from the gaps. First, build a public benchmark with a common equity-index dataset, a fixed set of maturities and strikes, and a violation suite that separates butterfly, calendar, and dynamic tests. Second, define a dynamic-consistency test that is independent of the construction family. Third, run a full-text, multi-database review with dual screening and a record-level excluded list. Fourth, compare hard construction, soft penalty, projection, and generation under distribution shift, with negative results reported. Fifth, validate generative surfaces with independent static and dynamic tests, not only visual plausibility. Sixth, measure interpretability and cost head-to-head rather than asserting them. These are research designs, not findings; the corpus does not yet support a ranking.

**Table 8.** Research agenda derived from the six gaps.

| Agenda item | Question | Evidence needed |
|---|---|---|
| Shared benchmark | Do methods rank differently under one dataset and metric set? | Common data, code, and violation suite |
| Dynamic test | Which methods remain consistent over time? | Joint surface–underlying tests |
| Full-text review | Do abstracts hide method weaknesses? | Full-text extraction and quality appraisal |
| Head-to-head enforcement | Hard vs soft vs projection under shift | Controlled experiments with negative results |
| Generative validation | Are generated surfaces independently admissible? | Adversarial arbitrage and out-of-sample tests |
| Interpretability/cost | What is traded for what? | Common measurement protocol |

**What this review can and cannot support.** It can support a corpus-scoped map of enforcement mechanisms, a proposed evaluation frame, and a set of testable propositions. It cannot support a method ranking, a claim that no benchmark exists anywhere, a regulatory determination, or a full-text assessment of method behaviour. The recommendations in §5.3 are proposals for reporting and research design, not validated findings.

---

## 6. Conclusion

This review synthesized 40 sources on arbitrage-free implied volatility surface construction. The central conclusion is that “arbitrage-free” names a family of guarantees, not a single property. Parametric SVI/SSVI/eSSVI families provide the clearest static guarantee but are conditional and can be inflexible; nonparametric methods provide flexibility and sometimes uncertainty but not a uniform guarantee; neural and generative methods provide fit and generation through a mixture of construction, penalty, projection, and filtering, with method-specific failure modes; dynamic no-arbitrage is a separate and under-tested layer; and evaluation is too fragmented to support cross-family ranking. The review contributes a four-family enforcement taxonomy, a seven-dimension evaluation matrix, and a corpus-scoped evidence map. The practical recommendation is to report the guarantee family and the evaluation dimensions explicitly, and the research recommendation is to build a shared benchmark that tests static and dynamic constraints together across markets. These conclusions are limited by abstract-level evidence, a 40/351 selection, 10 preprints, and the absence of full-text and COI audits. They are offered as a map of the evidence, not as a ranking of methods.

The practical message is conditional: choose the guarantee before the model. The research message is that a shared benchmark, a dynamic test, and full-text evidence are needed before cross-family claims can be adjudicated. The four-family taxonomy and the seven-dimension matrix are offered as organizing devices for that work, not as its result.

---

## Declarations

**Data Availability.** No new empirical data were generated. The search scripts, selected-source metadata, verification logs, and the frozen corpus are available in `examples/dsh/iv-surface-review/`; the 40 cited sources are public.

**Ethics Declaration.** No human subjects, personal data, or animal experiments were involved.

**CRediT Author Contributions.** TY-Cheng: conceptualization, methodology, investigation, data curation, writing—original draft, writing—review and editing, visualization, supervision, project administration.

**Conflict of Interest.** The author declares no competing interests. A full conflict-of-interest audit of the 40 sources was not possible from the retrieved metadata; the review does not infer undisclosed conflicts.

**Funding.** No funding was received for this work.

**AI-Use Statement.** The author used DeepSeek Harness with the ARS academic-pipeline (v0.3.0) for literature search assistance, metadata extraction, synthesis drafting, citation checking, and language editing. All sources were verified at the metadata/abstract level; full texts were not read. The author reviewed and is responsible for the final text. This statement discloses tool use; it does not transfer authorship.

---

## References

- Ackerer, D., Tagasovska, N., & Vatter, T. (2019). Deep Smoothing of the Implied Volatility Surface. *SSRN*. https://doi.org/10.2139/ssrn.3402942

- Anagha, S. (2026). Trainable Hard Constraints: Architectural Enforcement of Arbitrage-Free Implied Volatility Surfaces via Automatic Differentiation. *SSRN*. https://doi.org/10.2139/ssrn.7577418

- Andrès, H., Boumezoued, A., & Jourdain, B. (2026). The implied volatility surface (also) is path-dependent. *Quantitative Finance*. https://doi.org/10.1080/14697688.2026.2637739

- Appana, T., Carranti, A., Koshal, A., Moszczyński, A., & Thomas, M. (2024). Gaussian Processes for Implied Volatility Estimation. *SSRN*. https://doi.org/10.2139/ssrn.4803161

- Avellaneda, M., Healy, B., Papanicolaou, A. C., & Papanicolaou, G. (2020). PCA for Implied Volatility Surfaces. *Journal of Financial Data Science*. https://doi.org/10.3905/jfds.2020.1.032

- Bajalica, D., Brooks, O., & Ben Tahar, I. (2026). Latent Flow Matching for Arbitrage-Aware Implied Volatility Surface Generation. *Proceedings of the ACM International Conference on AI in Finance*. https://doi.org/10.1145/3858063.3858741

- Bayer, C., & Stemper, B. (2018). Deep calibration of rough stochastic volatility models. *arXiv*. https://doi.org/10.48550/arxiv.1810.03399

- Bayer, C., Horvath, B. N., Muguruza, A., Stemper, B., & Tomas, M. (2025). On Deep Calibration of (rough) Stochastic Volatility Models. *Journal of FinTech*. https://doi.org/10.1142/s2705109925500051

- Cao, Y., Liu, X., & Zhai, J. (2020). Option valuation under no-arbitrage constraints with neural networks. *European Journal of Operational Research*. https://doi.org/10.1016/j.ejor.2020.12.003

- Cohen, S. N., Reisinger, C., & Wang, S. (2020). Detecting and Repairing Arbitrage in Traded Option Prices. *Applied Mathematical Finance*. https://doi.org/10.1080/1350486x.2020.1846573

- Cohen, S. N., Reisinger, C., & Wang, S. (2023). Arbitrage-Free Neural-SDE Market Models. *Applied Mathematical Finance*. https://doi.org/10.1080/1350486x.2023.2257217

- Cont, R., & Vuletić, M. (2023). Simulation of Arbitrage-Free Implied Volatility Surfaces. *Applied Mathematical Finance*. https://doi.org/10.1080/1350486x.2023.2277960

- Cousin, A., & Gueye, D. (2021). Kriging for implied volatility surface. *HAL*. https://openalex.org/W3184266889

- Fengler, M. R. (2009). Arbitrage-free smoothing of the implied volatility surface. *Quantitative Finance*. https://doi.org/10.1080/14697680802595585

- Gatheral, J., & Jacquier, A. (2014). Arbitrage-free SVI volatility surfaces. *Quantitative Finance*. https://doi.org/10.1080/14697688.2013.819986

- Ginart Belmonte, V., & Cole, T. (2025). Arbitrage-Free Implied Volatility Surface Smoothing via Generative Adversarial Networks. *Proceedings of the ACM International Conference on AI in Finance*. https://doi.org/10.1145/3768292.3771252

- Guo, G., Jacquier, A., Martini, C., & Neufcourt, L. (2016). Generalized Arbitrage-Free SVI Volatility Surfaces. *SIAM Journal on Financial Mathematics*. https://doi.org/10.1137/120900320

- Homescu, C. (2011). Implied Volatility Surface: Construction Methodologies and Characteristics. *arXiv*. https://doi.org/10.48550/arxiv.1107.1834

- Horvath, B. N., Muguruza, A., & Tomas, M. (2021). Deep Learning Volatility. *Quantitative Finance*. https://doi.org/10.1080/14697688.2020.1817974

- Hoshisashi, K., Phelan, C. E., & Barucca, P. (2023). No-Arbitrage Deep Calibration for Volatility Smile and Skewness. *arXiv*. https://doi.org/10.48550/arxiv.2310.16703

- Hoshisashi, K., Phelan, C. E., & Barucca, P. (2024). Whack-a-mole Online Learning: Physics-Informed Neural Network for Intraday Implied Volatility Surface. *Proceedings of the ACM International Conference on AI in Finance*. https://doi.org/10.1145/3677052.3698601

- Liu, S., Oosterlee, C. W., & Bohté, S. M. (2019). Pricing Options and Computing Implied Volatilities using Neural Networks. *Risks*. https://doi.org/10.3390/risks7010016

- Luo, J., & Yu, C. L. (2023). The Application of Symbolic Regression on Identifying Implied Volatility Surface. *Mathematics*. https://doi.org/10.3390/math11092108

- Martini, C., & Mingone, A. (2022). No Arbitrage SVI. *SIAM Journal on Financial Mathematics*. https://doi.org/10.1137/20m1351060

- Medvedev, N., & Wang, Z. (2021). Multistep forecast of the implied volatility surface using deep learning. *Journal of Futures Markets*. https://doi.org/10.1002/fut.22302

- Mingone, A. (2022). No arbitrage global parametrization for the eSSVI volatility surface. *Quantitative Finance*. https://doi.org/10.1080/14697688.2022.2117076

- Neufeld, A., & Sester, J. (2024). Neural Networks Can Detect Model-Free Static Arbitrage Strategies. *Applied Mathematics & Optimization*. https://doi.org/10.1007/s00245-024-10184-9

- Ning, B., Jaimungal, S., Zhang, X., & Bergeron, M. (2023). Arbitrage-Free Implied Volatility Surface Generation with Variational Autoencoders. *SIAM Journal on Financial Mathematics*. https://doi.org/10.1137/21m1443546

- Ruf, J., & Wang, W. (2020). Neural Networks for Option Pricing and Hedging: A Literature Review. *Journal of Computational Finance*. https://doi.org/10.21314/jcf.2020.390

- Vuletić, M., & Cont, R. (2025). VolGAN: A Generative Model for Arbitrage-Free Implied Volatility Surfaces. *Applied Mathematical Finance*. https://doi.org/10.1080/1350486x.2025.2471317

- Wang, J., Liu, S., & Vuik, C. (2025). Controllable Generation of Implied Volatility Surfaces with Variational Autoencoders. *arXiv*. https://doi.org/10.48550/arxiv.2509.01743

- Wiedemann, R., Jacquier, A., & Gonon, L. (2024). Operator Deep Smoothing for Implied Volatility. *arXiv*. https://doi.org/10.48550/arxiv.2406.11520

- Xiong, Y., & Liu, B. (2026). Observation-Anchored Arbitrage Repair for Sparse Implied Volatility Surface Completion. *IEEE Conference on Computational Intelligence for Financial Engineering & Economics*. https://doi.org/10.1109/cifer67845.2026.11692406

- Yang, Y., Zheng, Y., & Hospedales, T. M. (2017). Gated Neural Networks for Option Pricing: Rationality by Design. *Proceedings of the AAAI Conference on Artificial Intelligence*. https://doi.org/10.1609/aaai.v31i1.10505

- Yao, Y., Cui, Z., & Pan, Q. (2026). Joint arbitrage-free smoothing of American call and put options surfaces. *European Journal of Operational Research*. https://doi.org/10.1016/j.ejor.2026.07.049

- Zaugg, N. F., Perotti, L., & Grzelak, L. A. (2025). Volatility Parametrizations with Random Coefficients: Analytic Flexibility for Implied Volatility Surfaces. *SIAM Journal on Financial Mathematics*. https://doi.org/10.1137/24m1713107

- Zetocha, V. (2023). Volatility Transformers: an optimal transport-inspired approach to arbitrage-free shaping of implied volatility surfaces. *SSRN*. https://doi.org/10.2139/ssrn.4623940

- Zhang, W., Li, L., & Zhang, G. (2022). A two-step framework for arbitrage-free prediction of the implied volatility surface. *Quantitative Finance*. https://doi.org/10.1080/14697688.2022.2135454

- Zheng, Y., Yang, Y., & Chen, B. (2021). Incorporating Prior Financial Domain Knowledge into Neural Networks for Implied Volatility Surface Prediction. *Proceedings of the 27th ACM SIGKDD Conference on Knowledge Discovery and Data Mining*. https://doi.org/10.1145/3447548.3467115

- Zhuang, J., & Wu, X. (2026). SABR-informed multitask Gaussian process: A synthetic-to-real framework for implied volatility surface construction. *Journal of Computational Science*. https://doi.org/10.1016/j.jocs.2026.102818

---

## Appendix A. Search Strategy and Screening Flow

**Databases and sources.** The primary discovery source was OpenAlex full-text search (24 queries, 25 results per query, deduplicated by DOI or normalized title). Crossref was used for DOI metadata and abstract completion; Semantic Scholar was queried for reference existence but returned HTTP 429 for all 10 requests at the time of search. arXiv, SSRN, and publisher pages were consulted only to recover abstracts or bibliographic details for records already in the corpus.

**Date range and Boolean logic.** The core window was 2015–2026; pre-2015 records were included only when they are seminal for the method family (Gatheral & Jacquier, 2014; Fengler, 2009; Homescu, 2011). The conceptual Boolean string was:

`("implied volatility surface" OR "volatility surface") AND ("no-arbitrage" OR "arbitrage-free" OR "static arbitrage" OR "calendar arbitrage" OR "butterfly arbitrage") AND ("parametric" OR "SVI" OR "SSVI" OR "eSSVI" OR "nonparametric" OR "spline" OR "Gaussian process" OR "neural" OR "deep learning" OR "generative")`

The exact 24 OpenAlex queries are recorded in `search/openalex_search.py`.

**Inclusion and exclusion.** Included records address equity-index or option-implied volatility surfaces and either construct a surface with an explicit no-arbitrage treatment or evaluate/repair/verify such a surface. Excluded records address option pricing without a surface focus, local- or stochastic-volatility calibration without surface construction, crypto/FX applications without a transferable method, practitioner commentary without evidence, or surfaces with no arbitrage discussion.

**Screening flow.** OpenAlex returned 351 unique records. After title/abstract screening, 311 were not advanced (off-topic, duplicate, no surface/arbitrage focus, or insufficient methodological relevance). Forty records advanced to metadata/abstract screening and were included: 30 peer-reviewed articles or conference papers and 10 preprints. Abstract coverage was 35 full, four partial, and one title-level record. No full-text screening was performed. The flow is PRISMA-style but not PRISMA-compliant, and the review does not claim PRISMA or PRISMA-ScR status.

**Verification.** OpenAlex resolved 40/40 records; 39 have a DOI and one is a HAL record without a DOI. Crossref returned four abstracts and one HTTP 429; Semantic Scholar returned HTTP 429 for all 10 requests. No retracted record was flagged and no fabricated reference was found; no predatory-journal alert was raised. COI and funding were not assessed because metadata did not provide a reliable disclosure record. These limits are carried into the report’s limitations.

**Scope note.** The corpus is SPX/US-equity-index heavy and abstract-level. The 24 queries emphasize static-arbitrage, parametric, and neural vocabulary; dynamic-arbitrage coverage may be under-sampled. The review is a structured, corpus-scoped synthesis, not a systematic review with full-text extraction.

---

## Appendix B. Corpus Index

The table lists all 40 included sources. Bucket labels follow the corpus construction; Level is the source-verification rubric (VI = peer-reviewed/scholarly; VII = preprint/other).

**Year convention.** Online-first articles are cited by their online-first year; the print issue year may be later (e.g., #29).

| # | Source | Bucket | Level | DOI / record |
|---|---|---|---|---|
| 1 | Gatheral & Jacquier (2014) | Parametric surfaces | VI | 10.1080/14697688.2013.819986 |
| 2 | Guo et al. (2016) | Parametric surfaces | VI | 10.1137/120900320 |
| 3 | Fengler (2009) | Parametric surfaces | VI | 10.1080/14697680802595585 |
| 4 | Homescu (2011) | Parametric surfaces | VII | 10.48550/arxiv.1107.1834 |
| 5 | Ackerer et al. (2019) | Neural and generative surfaces | VII | 10.2139/ssrn.3402942 |
| 6 | Bayer & Stemper (2018) | Neural and generative surfaces | VII | 10.48550/arxiv.1810.03399 |
| 7 | Yang et al. (2017) | Constraint enforcement, arbitrage repair, and evaluation | VI | 10.1609/aaai.v31i1.10505 |
| 8 | Ruf & Wang (2020) | Constraint enforcement, arbitrage repair, and evaluation | VI | 10.21314/jcf.2020.390 |
| 9 | Cao et al. (2020) | Constraint enforcement, arbitrage repair, and evaluation | VI | 10.1016/j.ejor.2020.12.003 |
| 10 | Cohen et al. (2020) | Constraint enforcement, arbitrage repair, and evaluation | VI | 10.1080/1350486x.2020.1846573 |
| 11 | Liu et al. (2019) | Constraint enforcement, arbitrage repair, and evaluation | VI | 10.3390/risks7010016 |
| 12 | Avellaneda et al. (2020) | Nonparametric, spline, and Gaussian-process surfaces | VI | 10.3905/jfds.2020.1.032 |
| 13 | Ning et al. (2023) | Neural and generative surfaces | VI | 10.1137/21m1443546 |
| 14 | Horvath et al. (2021) | Neural and generative surfaces | VI | 10.1080/14697688.2020.1817974 |
| 15 | Zhang et al. (2022) | Neural and generative surfaces | VI | 10.1080/14697688.2022.2135454 |
| 16 | Vuletić & Cont (2025) | Neural and generative surfaces | VI | 10.1080/1350486x.2025.2471317 |
| 17 | Cont & Vuletić (2023) | Neural and generative surfaces | VI | 10.1080/1350486x.2023.2277960 |
| 18 | Cohen et al. (2023) | Neural and generative surfaces | VI | 10.1080/1350486x.2023.2257217 |
| 19 | Medvedev & Wang (2021) | Neural and generative surfaces | VI | 10.1002/fut.22302 |
| 20 | Zheng et al. (2021) | Neural and generative surfaces | VI | 10.1145/3447548.3467115 |
| 21 | Bayer et al. (2025) | Neural and generative surfaces | VI | 10.1142/s2705109925500051 |
| 22 | Ginart Belmonte & Cole (2025) | Neural and generative surfaces | VI | 10.1145/3768292.3771252 |
| 23 | Bajalica et al. (2026) | Neural and generative surfaces | VI | 10.1145/3858063.3858741 |
| 24 | Wang et al. (2025) | Neural and generative surfaces | VII | 10.48550/arxiv.2509.01743 |
| 25 | Hoshisashi et al. (2024) | Neural and generative surfaces | VI | 10.1145/3677052.3698601 |
| 26 | Neufeld & Sester (2024) | Constraint enforcement, arbitrage repair, and evaluation | VI | 10.1007/s00245-024-10184-9 |
| 27 | Xiong & Liu (2026) | Constraint enforcement, arbitrage repair, and evaluation | VI | 10.1109/cifer67845.2026.11692406 |
| 28 | Zhuang & Wu (2026) | Nonparametric, spline, and Gaussian-process surfaces | VI | 10.1016/j.jocs.2026.102818 |
| 29 | Yao et al. (2026) | Nonparametric, spline, and Gaussian-process surfaces | VI | 10.1016/j.ejor.2026.07.049 |
| 30 | Andrès et al. (2026) | Surface dynamics and path dependence | VI | 10.1080/14697688.2026.2637739 |
| 31 | Zaugg et al. (2025) | Parametric surfaces | VI | 10.1137/24m1713107 |
| 32 | Martini & Mingone (2022) | Parametric surfaces | VI | 10.1137/20m1351060 |
| 33 | Mingone (2022) | Parametric surfaces | VI | 10.1080/14697688.2022.2117076 |
| 34 | Luo & Yu (2023) | Nonparametric, spline, and Gaussian-process surfaces | VI | 10.3390/math11092108 |
| 35 | Wiedemann et al. (2024) | Neural and generative surfaces | VII | 10.48550/arxiv.2406.11520 |
| 36 | Appana et al. (2024) | Nonparametric, spline, and Gaussian-process surfaces | VII | 10.2139/ssrn.4803161 |
| 37 | Hoshisashi et al. (2023) | Neural and generative surfaces | VII | 10.48550/arxiv.2310.16703 |
| 38 | Zetocha (2023) | Neural and generative surfaces | VII | 10.2139/ssrn.4623940 |
| 39 | Cousin & Gueye (2021) | Nonparametric, spline, and Gaussian-process surfaces | VII | HAL (no DOI) |
| 40 | Anagha (2026) | Constraint enforcement, arbitrage repair, and evaluation | VII | 10.2139/ssrn.7577418 |

---

## Appendix C. Screening Rationale and Reproducibility Note

The 311 records not advanced were not individually coded. The table below is a rationale summary, not a full excluded-record log; it is provided so that the 40/351 selection is auditable at the level of counts and criteria, not at the level of individual records.

| Stage | Records | Note |
|---|---:|---|
| Unique OpenAlex records | 351 | 24 full-text queries, 25 per query; DOI/title deduplication |
| Not advanced after title/abstract screen | 311 | Off-topic, duplicate, no surface/arbitrage focus, insufficient methodological relevance, or non-English; not individually coded |
| Metadata/abstract assessed | 40 | 30 peer-reviewed, 10 preprints |
| Full-text assessed | 0 | No full-text screening performed |
| Included in synthesis | 40 | 7 parametric, 6 nonparametric, 18 neural/generative, 8 constraints/evaluation, 1 dynamics |

**Reproducibility note.** The 24 query strings and the selection script are in `examples/dsh/iv-surface-review/search/` (`openalex_search.py`, `fetch_selected.py`). The search was executed on 2026-11-19 (Asia/Singapore). Re-running it later will change the candidate set; the included corpus is frozen in `search/selected_sources.json`. The flow is PRISMA-style but not PRISMA-compliant; no dual-screening or full-text extraction was performed. The 40 included records are listed in Appendix B; the 311 non-advanced records were not retained as a record-level list, which is a reproducibility limitation.

---

## Appendix D. Source-Level Taxonomy Mapping

Interpretive mapping by the primary mechanism that carries the guarantee. “Static” = a reported butterfly/calendar check or construction; “dynamic” = a reported joint surface–underlying or time-consistency test. Ambiguous and hybrid cases are classified by the primary mechanism, not every step. The table is not a ranking.

| # | Source | Method family | Enforcement family | Static test | Dynamic test | Evidence |
|---|---|---|---|---|---|---|
| 1 | Gatheral & Jacquier (2014) | Parametric | Construction | Y | N | VI |
| 2 | Guo et al. (2016) | Parametric | Construction | Y | N | VI |
| 3 | Fengler (2009) | Parametric | Projection/repair | Y | N | VI |
| 4 | Homescu (2011) | Parametric | Survey (no construction) | Review | N | VII |
| 5 | Ackerer et al. (2019) | Neural/generative | Penalty | N (soft) | N | VII |
| 6 | Bayer & Stemper (2018) | Neural/generative | Construction (calibration map) | N | N | VII |
| 7 | Yang et al. (2017) | Constraints/evaluation | Construction | Y | N | VI |
| 8 | Ruf & Wang (2020) | Constraints/evaluation | Survey/evaluation | Review | N | VI |
| 9 | Cao et al. (2020) | Constraints/evaluation | Penalty | N (soft) | N | VI |
| 10 | Cohen et al. (2020) | Constraints/evaluation | Projection/repair | Y | N | VI |
| 11 | Liu et al. (2019) | Constraints/evaluation | None/soft | N | N | VI |
| 12 | Avellaneda et al. (2020) | Nonparametric | None/soft | N | N | VI |
| 13 | Ning et al. (2023) | Neural/generative | Generation + filter | N (soft) | N | VI |
| 14 | Horvath et al. (2021) | Neural/generative | None/soft (title-level) | N | N (title-level) | VI |
| 15 | Zhang et al. (2022) | Neural/generative | Penalty / two-step | N (soft) | N | VI |
| 16 | Vuletić & Cont (2025) | Neural/generative | Generation + filter | N (soft) | Y | VI |
| 17 | Cont & Vuletić (2023) | Neural/generative | Construction (simulation) | Y | Y | VI |
| 18 | Cohen et al. (2023) | Neural/generative | Generation (neural SDE) | Y | Y | VI |
| 19 | Medvedev & Wang (2021) | Neural/generative | None/soft | N | N | VI |
| 20 | Zheng et al. (2021) | Neural/generative | Penalty (prior knowledge) | N (soft) | N | VI |
| 21 | Bayer et al. (2025) | Neural/generative | Construction (calibration map) | N | N | VI |
| 22 | Ginart Belmonte & Cole (2025) | Neural/generative | Generation + filter | N (soft) | N | VI |
| 23 | Bajalica et al. (2026) | Neural/generative | Generation + filter | N (soft) | N | VI |
| 24 | Wang et al. (2025) | Neural/generative | Generation + filter | N (soft) | N | VII |
| 25 | Hoshisashi et al. (2024) | Neural/generative | Penalty (PINN) | N (soft) | N | VI |
| 26 | Neufeld & Sester (2024) | Constraints/evaluation | Evaluation/detection | Y | N | VI |
| 27 | Xiong & Liu (2026) | Constraints/evaluation | Projection/repair | Y | N | VI |
| 28 | Zhuang & Wu (2026) | Nonparametric | None/soft (GP) | N | N | VI |
| 29 | Yao et al. (2026) | Nonparametric | Projection/repair | Y | N | VI |
| 30 | Andrès et al. (2026) | Dynamics | Construction (path-dependent) | Y | Y | VI |
| 31 | Zaugg et al. (2025) | Parametric | Construction | Y | N | VI |
| 32 | Martini & Mingone (2022) | Parametric | Construction | Y | N | VI |
| 33 | Mingone (2022) | Parametric | Construction | Y | N | VI |
| 34 | Luo & Yu (2023) | Nonparametric | None/soft (symbolic) | N | N | VI |
| 35 | Wiedemann et al. (2024) | Neural/generative | Penalty/operator | N (soft) | N | VII |
| 36 | Appana et al. (2024) | Nonparametric | None/soft (GP) | N | N | VII |
| 37 | Hoshisashi et al. (2023) | Neural/generative | Construction (calibration map) | N (soft) | N | VII |
| 38 | Zetocha (2023) | Neural/generative | Generation + filter | N (soft) | N | VII |
| 39 | Cousin & Gueye (2021) | Nonparametric | None/soft (kriging) | N | N | VII |
| 40 | Anagha (2026) | Constraints/evaluation | Construction | Y | N | VII |

**Mapping note.** The evidence column is the source-verification level: VI = peer-reviewed article/conference paper; VII = preprint or other. The 10 preprints are 4, 5, 6, 24, 35, 36, 37, 38, 39, and 40.

---

## Appendix E. Search Query Log

OpenAlex full-text queries executed on 2026-11-19 (Asia/Singapore). “Matches” is the OpenAlex total count for the query; 25 records were retrieved per query, and the candidate pool was deduplicated to 351 unique records. Per-query counts are reported for reproducibility; the included corpus is frozen in `selected_sources.json`.

| # | Query | OpenAlex matches | Retrieved |
|---:|---|---:|---:|
| 1 | arbitrage-free implied volatility surface | 5171 | 25 |
| 2 | implied volatility surface arbitrage | 6490 | 25 |
| 3 | SVI stochastic volatility inspired | 225 | 25 |
| 4 | SSVI implied volatility surface | 114 | 25 |
| 5 | shape constrained implied volatility surface | 33973 | 25 |
| 6 | nonparametric implied volatility surface | 6540 | 25 |
| 7 | neural network implied volatility surface | 23636 | 25 |
| 8 | deep learning implied volatility surface | 47896 | 25 |
| 9 | neural network option pricing arbitrage-free | 3376 | 25 |
| 10 | rough volatility calibration neural network | 3113 | 25 |
| 11 | implied volatility surface machine learning | 38286 | 25 |
| 12 | dynamic arbitrage implied volatility | 30236 | 25 |
| 13 | implied volatility surface interpolation no arbitrage | 1189 | 25 |
| 14 | generative model implied volatility surface | 11135 | 25 |
| 15 | variational autoencoder implied volatility surface | 1233 | 25 |
| 16 | neural SDE volatility surface | 3700 | 25 |
| 17 | deep calibration stochastic volatility | 19520 | 25 |
| 18 | no-arbitrage smoothing implied volatility | 18279 | 25 |
| 19 | calendar arbitrage implied volatility | 6341 | 25 |
| 20 | butterfly arbitrage implied volatility | 651 | 25 |
| 21 | implied volatility surface survey | 100152 | 25 |
| 22 | arbitrage-free option prices neural network | 3371 | 25 |
| 23 | Gaussian process implied volatility surface | 25579 | 25 |
| 24 | neural network calibration rough volatility | 3112 | 25 |

**Note.** The 24 queries are the discovery set; they emphasize static-arbitrage, parametric, and neural vocabulary. Dynamic-arbitrage coverage may be under-sampled; this is disclosed in §4.4 and §5.4.
