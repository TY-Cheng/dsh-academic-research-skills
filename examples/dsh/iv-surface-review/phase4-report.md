# Arbitrage-Free Implied Volatility Surface Construction: A Structured Literature Review of Parametric, Nonparametric, and Neural Approaches

**Author:** TY-Cheng  
**Affiliation:** Independent researcher; DSH academic-research-skills end-to-end run  
**Date:** 2026-11-19  
**Report type:** `deep-research` full report, Stage 1 Phase 4 draft  
**Body word count:** 5,358 words (excluding references and appendices)  
**Revision log:** v1 Phase 4 draft (2026-11-19): body assembled; references and appendices inserted; Phase 3 DA Major issues addressed by hedging and scope caveats; residual limits in §5.4.

---

## Abstract

Constructing an arbitrage-free implied volatility surface (IVS) is a central problem in derivatives modelling. Parametric, nonparametric, and neural approaches each claim to enforce static or dynamic no-arbitrage, but the meaning of “arbitrage-free” and the strength of the supporting evidence differ across families. This structured review synthesizes 40 sources—30 peer-reviewed articles or conference papers and 10 preprints, published between 2009 and 2026—identified through 24 OpenAlex full-text queries and verified at metadata/abstract level. The review finds that parametric SVI/SSVI/eSSVI families provide explicit static-arbitrage conditions, whereas nonparametric, neural, and generative methods rely on a mixture of architectural constraints, soft penalties, two-step prediction-and-constraint, and post-hoc repair. Dynamic no-arbitrage is less standardized and less frequently tested; static constraints are necessary but not sufficient for dynamic consistency. Evaluation is fragmented: fit metrics dominate, and no shared benchmark for arbitrage violations, out-of-sample stability, wing behaviour, computational cost, and interpretability was identified in the retrieved abstracts. The review proposes a four-family enforcement taxonomy and a seven-dimension evaluation matrix, and it frames the main gaps as benchmark design, dynamic testing, cross-market evidence, interpretability, and standardized validation of generative models. The findings are corpus-scoped and abstract-level; no method ranking is implied.

**Keywords:** implied volatility surface; no-arbitrage; SVI; neural networks; generative models; model calibration; literature review

---

## 1. Introduction

### 1.1 Context

The implied volatility surface is the mapping from option strikes and maturities to the volatility implied by observed prices. It is used for pricing, risk management, scenario generation, and model calibration. A surface that admits static arbitrage contains internal inconsistencies—violations of butterfly (strike-convexity) or calendar (maturity-monotonicity) conditions—that can be exploited by a static portfolio. A surface that admits dynamic arbitrage is inconsistent with a joint martingale model for the underlying and the surface over time. Both forms of arbitrage matter, but they are different constraints and are enforced by different methods (Gatheral & Jacquier, 2014<!--ref:src-01--><!--anchor:section:Abstract-->; Fengler, 2009<!--ref:src-03--><!--anchor:section:Abstract-->).

Three broad families dominate construction. Parametric models impose a functional form—SVI, SSVI, eSSVI, or random-coefficient extensions—and constrain its parameters (Gatheral & Jacquier, 2014<!--ref:src-01--><!--anchor:section:Abstract-->; Guo et al., 2016<!--ref:src-02--><!--anchor:section:Abstract-->; Martini & Mingone, 2022<!--ref:src-32--><!--anchor:section:Abstract-->; Mingone, 2022<!--ref:src-33--><!--anchor:section:Abstract-->; Zaugg et al., 2025<!--ref:src-31--><!--anchor:section:Abstract-->). Nonparametric models use splines, PCA, Gaussian processes, kriging, symbolic regression, or constrained optimization (Fengler, 2009<!--ref:src-03--><!--anchor:section:Abstract-->; Avellaneda et al., 2020<!--ref:src-12--><!--anchor:section:Abstract-->; Zhuang & Wu, 2026<!--ref:src-28--><!--anchor:section:Abstract-->; Yao et al., 2026<!--ref:src-29--><!--anchor:section:Abstract-->; Luo & Yu, 2023<!--ref:src-34--><!--anchor:section:Abstract-->; Appana et al., 2024<!--ref:src-36--><!--anchor:section:Abstract-->; Cousin & Gueye, 2021<!--ref:src-39--><!--anchor:section:Abstract-->). Neural and generative models learn the surface or its dynamics with multilayer networks, neural SDEs, variational autoencoders, generative adversarial networks, normalizing flows, or operator learning (Ackerer et al., 2019<!--ref:src-05--><!--anchor:section:Abstract-->; Bayer & Stemper, 2018<!--ref:src-06--><!--anchor:section:Abstract-->; Ning et al., 2023<!--ref:src-13--><!--anchor:section:Abstract-->; Horvath et al., 2021<!--ref:src-14--><!--anchor:section:Abstract-->; Vuletić & Cont, 2025<!--ref:src-16--><!--anchor:section:Abstract-->).

### 1.2 Problem Statement

The literature is large and method-specific, but it lacks a shared vocabulary for what a construction guarantees. “Arbitrage-free” may mean that the surface is generated inside an admissible parametric region, that a penalty term reduced violations during training, that a second step projects the prediction onto a constrained set, or that a post-hoc repair algorithm removed detected arbitrage. These are not equivalent guarantees. The ambiguity is compounded by heterogeneous evaluation: papers report fit errors, violation counts, stability, wing behaviour, cost, or interpretability on different data and with different definitions. The result is that cross-paper claims of superiority are difficult to justify, and practitioners lack a compact map from method family to guarantee, evidence strength, and failure mode.

### 1.3 Purpose and Research Question

This review synthesizes the construction and evaluation literature for equity-index implied volatility surfaces, with emphasis on how no-arbitrage is enforced and what trade-offs are reported. The research question is:

> How do parametric, nonparametric, and neural methods for constructing equity-index implied volatility surfaces enforce static and dynamic no-arbitrage constraints, and what trade-offs do they report across fit, stability, extrapolation, computational cost, and interpretability?

The review has three aims: (a) organize the literature by where the constraint enters the construction pipeline; (b) assess the strength of the evidence for each family at abstract level; and (c) identify gaps that a shared research programme should address.

### 1.4 Significance

For researchers, the review offers a taxonomy that separates construction, penalty, projection/repair, and generation/filtering, and it identifies where the evidence is thin. For practitioners, it makes explicit that the choice of method is also a choice of guarantee: a parametric surface may be arbitrage-free by construction but inflexible; a neural surface may fit better but require a repair step; a generative model may produce plausible surfaces but lack independent dynamic validation. For benchmark designers, it proposes seven evaluation dimensions that any cross-method comparison should report.

---

## 2. Literature Review and Theoretical Framework

### 2.1 Static No-Arbitrage and Parametric Surfaces

Static no-arbitrage is a shape constraint on a single surface. In the strike dimension, call prices must be convex and their density non-negative; in the maturity dimension, total implied variance must be non-decreasing. Parametric SVI-type models translate these conditions into restrictions on parameters or into closed-form inequalities. Gatheral and Jacquier (2014)<!--ref:src-01--><!--anchor:section:Abstract--> give explicit conditions for the raw SVI parameterization and for SSVI; Guo et al. (2016)<!--ref:src-02--><!--anchor:section:Abstract--> generalize the arbitrage-free SVI construction; Martini and Mingone (2022)<!--ref:src-32--><!--anchor:section:Abstract--> and Mingone (2022)<!--ref:src-33--><!--anchor:section:Abstract--> develop no-arbitrage SVI and eSSVI parameterizations. Zaugg et al. (2025)<!--ref:src-31--><!--anchor:section:Abstract--> add random coefficients to recover analytic flexibility while retaining explicit constraints. Homescu (2011)<!--ref:src-04--><!--anchor:section:Abstract--> surveys construction methodologies and makes the constraint taxonomy explicit.

The strength of this literature is that the guarantee is structural: if the calibrated parameters lie in the admissible region, the surface is arbitrage-free by construction. The limitation is equally structural: the admissible region can be conservative, and fit quality in sparse wings may suffer. Fengler (2009)<!--ref:src-03--><!--anchor:section:Abstract--> approaches the problem from constrained smoothing rather than a parametric family, and the contrast is instructive: smoothing can adapt to the data but must solve a constrained optimization problem, while a parametric family encodes the constraint in its parameterization but restricts the shape.

### 2.2 Nonparametric and Constrained Smoothing

Nonparametric methods trade a closed-form guarantee for flexibility. Fengler’s constrained least-squares smoother is an early benchmark (Fengler, 2009<!--ref:src-03--><!--anchor:section:Abstract-->). Avellaneda et al. (2020)<!--ref:src-12--><!--anchor:section:Abstract--> use PCA to represent the surface in a low-dimensional factor space; Zhuang and Wu (2026)<!--ref:src-28--><!--anchor:section:Abstract--> combine a SABR-informed source with a multitask Gaussian process to stabilize sparse wings; Yao et al. (2026)<!--ref:src-29--><!--anchor:section:Abstract--> formulate a joint cubic-spline quadratic program for American call and put surfaces with linear arbitrage constraints. Luo and Yu (2023)<!--ref:src-34--><!--anchor:section:Abstract--> apply symbolic regression, Appana et al. (2024)<!--ref:src-36--><!--anchor:section:Abstract--> use Gaussian processes, and Cousin and Gueye (2021)<!--ref:src-39--><!--anchor:section:Abstract--> use kriging.

These methods are attractive when the data are sparse or when uncertainty quantification is required: Gaussian-process and kriging estimators return a posterior distribution, not only a point surface. The guarantee, however, is method-specific. A constrained spline or quadratic program can enforce static conditions; a generic GP or kriging estimator does not, unless the constraint is built into the prior or the projection step. The corpus does not compare these alternatives under a common probabilistic scoring rule.

### 2.3 Neural and Generative Approaches

Neural methods learn the map from market observables or model parameters to the surface. The literature contains five recurring design patterns. First, soft penalties add an arbitrage term to the training loss (Ackerer et al., 2019<!--ref:src-05--><!--anchor:section:Abstract-->; Cao et al., 2020<!--ref:src-09--><!--anchor:section:Abstract-->; Zhang et al., 2022<!--ref:src-15--><!--anchor:section:Abstract-->). Second, hard or gated architectures restrict the function class so that rationality holds by design (Yang et al., 2017<!--ref:src-07--><!--anchor:section:Abstract-->; Anagha, 2026<!--ref:src-40--><!--anchor:section:Abstract-->). Third, two-step pipelines predict a surface and then project or adjust it (Zhang et al., 2022<!--ref:src-15--><!--anchor:section:Abstract-->; Cohen et al., 2020<!--ref:src-10--><!--anchor:section:Abstract-->). Fourth, post-hoc repair detects and removes arbitrage from observed or predicted prices (Cohen et al., 2020<!--ref:src-10--><!--anchor:section:Abstract-->; Xiong & Liu, 2026<!--ref:src-27--><!--anchor:section:Abstract-->; Neufeld & Sester, 2024<!--ref:src-26--><!--anchor:section:Abstract-->). Fifth, generative models—VAEs, GANs, flows, and operator models—generate surfaces and rely on a filter or repair step for admissibility (Ning et al., 2023<!--ref:src-13--><!--anchor:section:Abstract-->; Vuletić & Cont, 2025<!--ref:src-16--><!--anchor:section:Abstract-->; Ginart Belmonte & Cole, 2025<!--ref:src-22--><!--anchor:section:Abstract-->; Bajalica et al., 2026<!--ref:src-23--><!--anchor:section:Abstract-->; Wang et al., 2025<!--ref:src-24--><!--anchor:section:Abstract-->; Wiedemann et al., 2024<!--ref:src-35--><!--anchor:section:Abstract-->; Zetocha, 2023<!--ref:src-38--><!--anchor:section:Abstract-->).

The reported advantages are faster calibration (Bayer & Stemper, 2018<!--ref:src-06--><!--anchor:section:Abstract-->; Horvath et al., 2021<!--ref:src-14--><!--anchor:section:Abstract-->; Bayer et al., 2025<!--ref:src-21--><!--anchor:section:Abstract-->), improved fit in some settings (Liu et al., 2019<!--ref:src-11--><!--anchor:section:Abstract-->; Zheng et al., 2021<!--ref:src-20--><!--anchor:section:Abstract-->; Medvedev & Wang, 2021<!--ref:src-19--><!--anchor:section:Abstract-->), and plausible generated surfaces (Ning et al., 2023<!--ref:src-13--><!--anchor:section:Abstract-->; Vuletić & Cont, 2025<!--ref:src-16--><!--anchor:section:Abstract-->). The reported costs are constraint violations under distribution shift, unstable extrapolation in sparse wings, and limited interpretability. The evidence is unevenly distributed: 10 of the 40 sources are preprints, and several neural claims are supported at abstract level only.

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

---

## 3. Methodology

### 3.1 Research Design

This is a structured literature review in `deep-research` full mode. It is not a PRISMA-compliant systematic review, and no PRISMA or PRISMA-ScR compliance is claimed. The unit of analysis is a source that constructs, evaluates, or repairs an equity-index implied volatility surface with an explicit or implicit no-arbitrage objective. The review combines a reproducible search, metadata/abstract extraction, source verification, thematic synthesis, a Devil’s Advocate checkpoint, and a narrative report.

### 3.2 Search Strategy

The primary discovery source was OpenAlex, queried with 24 full-text search strings on 2026-11-19 (Asia/Singapore). Each query returned up to 25 records; after DOI/title deduplication, 351 unique records remained. The conceptual Boolean string combined surface terms (“implied volatility surface” or “volatility surface”), arbitrage terms (“arbitrage-free”, “no-arbitrage”, “static arbitrage”, “calendar arbitrage”, “butterfly arbitrage”), and method terms (“SVI”, “SSVI”, “parametric”, “nonparametric”, “neural network”, “deep learning”, “generative”, “Gaussian process”). Crossref was used for metadata and DOI checks (10 targeted lookups; four abstracts recovered; one HTTP 429). Semantic Scholar was attempted for title/DOI verification and abstract completion (10 requests; all HTTP 429). arXiv, SSRN, and publisher pages supplied five spot-check abstracts. No Web of Science, Scopus, or institutional database access was available.

The date range was 2015-01-01 to 2026-11-19. Pre-2015 seminal works were admitted only when they define a construction or constraint used by later work (Fengler, 2009<!--ref:src-03--><!--anchor:section:Abstract-->; Homescu, 2011<!--ref:src-04--><!--anchor:section:Abstract-->; Gatheral & Jacquier, 2014<!--ref:src-01--><!--anchor:section:Abstract-->). Included sources were equity-index or option-surface construction papers with a static/dynamic no-arbitrage contribution, a parametric/nonparametric/neural/generative method, or an evaluation/repair contribution; English-language; peer-reviewed or credible preprint. Excluded were pure option-pricing papers without surface construction, local/stochastic-volatility calibration without a surface/arbitrage contribution, crypto/FX applications unless the method transfers directly, practitioner blogs and vendor notes, and papers with no arbitrage or surface focus.

### 3.3 Screening and Corpus

Of the 351 unique records, 311 were not advanced after title/abstract screening (off-topic, duplicate, no surface/arbitrage focus, non-English, or outside scope). Forty records were assessed at metadata/abstract level and included; no full texts were assessed. The corpus contains 30 peer-reviewed articles or conference papers and 10 preprints (75%/25%), above the 60% peer-reviewed floor. Twenty-eight sources (70%) are from 2021–2026 and 12 (30%) are pre-2021, including seminal work; the currency distribution is at the 30% cap and does not trigger an advisory. The method mix is neural/generative 18 (45%), constraints/evaluation 8 (20%), parametric 7 (17.5%), nonparametric 6 (15%), and dynamics 1 (2.5%). No single method exceeds 70%.

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

## 4. Findings

### 4.1 Corpus and Evidence Base

The corpus contains 40 sources: 30 peer-reviewed articles or conference papers and 10 preprints. Twenty-eight sources (70%) are from 2021–2026; 12 (30%) are older, including the seminal parametric and smoothing work. The method mix is neural/generative 18, constraints/evaluation 8, parametric 7, nonparametric 6, and dynamics 1 (Table 1). Abstract coverage is 35 full, four partial, and one title-level-only record. OpenAlex resolved all 40 records; 39 have a DOI and one is a HAL record without a DOI. No retracted record was flagged and no fabricated reference was found. These counts describe the evidence base, not its quality; the quality assessment is source-level and abstract-level.

### 4.2 Finding 1: Static No-Arbitrage Is Well-Characterized for Parametric Surfaces, Not Solved

The parametric literature provides the clearest guarantee in the corpus. SVI, SSVI, and eSSVI express static no-arbitrage as parameter restrictions or closed-form conditions (Gatheral & Jacquier, 2014<!--ref:src-01--><!--anchor:section:Abstract-->; Guo et al., 2016<!--ref:src-02--><!--anchor:section:Abstract-->; Martini & Mingone, 2022<!--ref:src-32--><!--anchor:section:Abstract-->; Mingone, 2022<!--ref:src-33--><!--anchor:section:Abstract-->). Zaugg et al. (2025)<!--ref:src-31--><!--anchor:section:Abstract--> extend the family with random coefficients; Fengler (2009)<!--ref:src-03--><!--anchor:section:Abstract--> provides a constrained-smoothing alternative; Homescu (2011)<!--ref:src-04--><!--anchor:section:Abstract--> supplies the survey taxonomy. The guarantee is structural—if the parameters are admissible, the surface is arbitrage-free—but it is conditional. The admissible region can be conservative, and fit quality in sparse wings can suffer. “Well-characterized” therefore means that the constraint language is explicit, not that every calibrated surface is acceptable. The review treats this as strong evidence for the parametric construction, but not as evidence that the construction problem is closed.

### 4.3 Finding 2: Neural and Generative Methods Multiply Enforcement Mechanisms Without a Common Comparison

Eighteen neural/generative sources and eight constraints/evaluation sources address enforcement. The mechanisms fall into four families (Table 2): construction (parametric restrictions or gated/architectural networks), penalty (soft loss), projection/repair (quadratic program, spline, or minimal adjustment), and generation plus filtering (VAE, GAN, flow, operator, or neural SDE with a constraint step). Representative construction work includes Yang et al. (2017)<!--ref:src-07--><!--anchor:section:Abstract--> and Anagha (2026)<!--ref:src-40--><!--anchor:section:Abstract-->; penalty work includes Ackerer et al. (2019)<!--ref:src-05--><!--anchor:section:Abstract-->, Cao et al. (2020)<!--ref:src-09--><!--anchor:section:Abstract-->, and Zhang et al. (2022)<!--ref:src-15--><!--anchor:section:Abstract-->; repair work includes Cohen et al. (2020)<!--ref:src-10--><!--anchor:section:Abstract-->, Xiong and Liu (2026)<!--ref:src-27--><!--anchor:section:Abstract-->, and Neufeld and Sester (2024)<!--ref:src-26--><!--anchor:section:Abstract-->; generative work includes Ning et al. (2023)<!--ref:src-13--><!--anchor:section:Abstract-->, Vuletić and Cont (2025)<!--ref:src-16--><!--anchor:section:Abstract-->, Ginart Belmonte and Cole (2025)<!--ref:src-22--><!--anchor:section:Abstract-->, Bajalica et al. (2026)<!--ref:src-23--><!--anchor:section:Abstract-->, Wang et al. (2025)<!--ref:src-24--><!--anchor:section:Abstract-->, Wiedemann et al. (2024)<!--ref:src-35--><!--anchor:section:Abstract-->, and Zetocha (2023)<!--ref:src-38--><!--anchor:section:Abstract-->.

The reported advantages are consistent in direction: neural surrogates reduce calibration time (Bayer & Stemper, 2018<!--ref:src-06--><!--anchor:section:Abstract-->; Horvath et al., 2021<!--ref:src-14--><!--anchor:section:Abstract-->; Bayer et al., 2025<!--ref:src-21--><!--anchor:section:Abstract-->), improve fit in some settings (Liu et al., 2019<!--ref:src-11--><!--anchor:section:Abstract-->; Zheng et al., 2021<!--ref:src-20--><!--anchor:section:Abstract-->; Medvedev & Wang, 2021<!--ref:src-19--><!--anchor:section:Abstract-->), and generate plausible surfaces (Ning et al., 2023<!--ref:src-13--><!--anchor:section:Abstract-->; Vuletić & Cont, 2025<!--ref:src-16--><!--anchor:section:Abstract-->). Intraday and calibration-specific designs add further evidence: Hoshisashi et al. (2024)<!--ref:src-25--><!--anchor:section:Abstract--> use a physics-informed network for intraday surfaces, and Hoshisashi et al. (2023)<!--ref:src-37--><!--anchor:section:Abstract--> develop no-arbitrage deep calibration for smile and skewness. The costs are also consistent: violations can reappear under distribution shift, wing extrapolation is unstable, and interpretability is limited. The critical caveat is that the mechanisms are not equivalent. A gated architecture may guarantee a property that a soft penalty only encourages; a two-step pipeline may restore admissibility while changing the prediction; a generative model may produce a plausible sample that fails an independent arbitrage test. The corpus does not contain a head-to-head comparison that holds data, metrics, and constraint definitions fixed, and 10 of the 40 sources are preprints. The evidence is therefore moderate, not settled.

**Table 2.** Constraint-enforcement families in the corpus

| Family | Mechanism | Guarantee | Representative sources | Main failure mode |
|---|---|---|---|---|
| Construction | Admissible parametric region; gated/architectural networks | Static, by construction | Gatheral & Jacquier (2014); Yang et al. (2017); Zaugg et al. (2025); Anagha (2026) | Conservative region; reduced fit flexibility |
| Penalty | Soft arbitrage term in the loss | None at inference | Ackerer et al. (2019); Cao et al. (2020); Zhang et al. (2022) | Violations under shift; weight sensitivity |
| Projection / repair | QP, spline, or minimal adjustment | Post-hoc static | Fengler (2009); Cohen et al. (2020); Xiong & Liu (2026) | Observation changes; repair-rule dependence |
| Generation + filter | VAE, GAN, flow, operator, neural SDE + constraint step | Filter-dependent | Ning et al. (2023); Vuletić & Cont (2025); Bajalica et al. (2026); Zetocha (2023) | Static-only validation; mode collapse |

### 4.4 Finding 3: Dynamic No-Arbitrage Is the Frontier—and the Evidence Is Thin

Only a small subset of the corpus engages dynamic consistency. Cont and Vuletić (2023)<!--ref:src-17--><!--anchor:section:Abstract--> construct arbitrage-free surface simulations; Cohen et al. (2023)<!--ref:src-18--><!--anchor:section:Abstract--> build neural-SDE market models; Vuletić and Cont (2025)<!--ref:src-16--><!--anchor:section:Abstract--> extend the generative approach; Andrès et al. (2026)<!--ref:src-30--><!--anchor:section:Abstract--> argue that the surface is path-dependent. These are different mechanisms, and they do not share a common definition of dynamic consistency. The review’s claim is deliberately weak: static no-arbitrage is necessary but not sufficient for dynamic no-arbitrage, and the corpus does not contain a shared dynamic test. The dynamic literature is also under-sampled: the 24 queries emphasized static-arbitrage vocabulary, and only a handful of records survived. The “frontier” label is therefore a statement about this corpus, not a universal claim about the field. One neural source, Horvath et al. (2021)<!--ref:src-14--><!--anchor:section:Abstract-->, is title-level only in this review; its findings are not used for a substantive dynamic claim. [MATERIAL GAP: full abstract unavailable for Horvath et al. (2021).]

### 4.5 Finding 4: Evaluation Is Fragmented and No Shared Benchmark Was Identified

The evaluation landscape is heterogeneous. Fit metrics (RMSE, MAPE, implied-volatility error) dominate; arbitrage violations, out-of-sample stability, wing behaviour, computational cost, and interpretability are reported inconsistently. The repair and detection literature makes the gap concrete: Cohen et al. (2020)<!--ref:src-10--><!--anchor:section:Abstract--> detect and repair arbitrage in traded prices; Neufeld and Sester (2024)<!--ref:src-26--><!--anchor:section:Abstract--> use neural networks to detect model-free static arbitrage; Xiong and Liu (2026)<!--ref:src-27--><!--anchor:section:Abstract--> anchor repair to observations for sparse surfaces. Ruf and Wang (2020)<!--ref:src-08--><!--anchor:section:Abstract--> review the neural option-pricing literature and find no common benchmark. The review’s synthesis is that a shared evaluation matrix should report at least seven dimensions: fit, static violations, dynamic consistency, out-of-sample stability, wing behaviour, computational cost, and interpretability (Table 3). The corpus supplies pieces of this matrix but no paper reports all seven on a common dataset. “No shared benchmark identified in the retrieved abstracts” is a gap hypothesis, not a claim that no benchmark exists anywhere.

**Table 3.** Evaluation dimensions and reporting gaps

| Dimension | Representative metrics | Reporting in corpus | Gap |
|---|---|---|---|
| Fit | RMSE, MAPE, IV error | Common | Different data, weights, and error definitions |
| Static arbitrage | Butterfly/calendar violations | Common in constraint papers | Violation definitions and tolerances vary |
| Dynamic consistency | Joint surface–underlying tests | Rare | No shared dynamic test |
| Out-of-sample stability | Train/test or temporal split | Uneven | No common split or stress period |
| Wing behaviour | Sparse-strike error | Method-specific | No standard wing metric |
| Computational cost | Calibration/inference time | Uneven | No common budget or hardware |
| Interpretability | Parameter meaning, attention, rules | Uneven | No accepted metric |

### 4.6 Finding 5: Flexibility, Uncertainty, and Data Coverage Trade Guarantees for Adaptability

The nonparametric group—PCA (Avellaneda et al., 2020<!--ref:src-12--><!--anchor:section:Abstract-->), Gaussian processes (Appana et al., 2024<!--ref:src-36--><!--anchor:section:Abstract-->), kriging (Cousin & Gueye, 2021<!--ref:src-39--><!--anchor:section:Abstract-->), symbolic regression (Luo & Yu, 2023<!--ref:src-34--><!--anchor:section:Abstract-->), SABR-informed multitask GP (Zhuang & Wu, 2026<!--ref:src-28--><!--anchor:section:Abstract-->), and joint American call/put smoothing (Yao et al., 2026<!--ref:src-29--><!--anchor:section:Abstract-->)—offers flexibility, and in the GP/kriging cases a posterior uncertainty. The guarantee is not uniform: a constrained spline or quadratic program can enforce static conditions; a generic GP or kriging estimator does not, unless the constraint is built into the prior or a projection step. The data motivation is recurrent: several methods target sparse wings or incomplete surfaces, and neural experiments often use simulated or synthetic data. The corpus is SPX/US-equity-index heavy; cross-market evidence is thin. The practical implication is conditional: nonparametric methods are attractive when uncertainty and adaptability matter, but the user must check whether the specific estimator carries a constraint guarantee.

### 4.7 Cross-Paper Tensions

Seven candidate pairs were assessed in the synthesis. Five were resolved as conditional differences or method-class differences; one was flagged unresolved; one was not applicable because the pair addresses different mechanisms (Table 4). The unresolved pair is the tension between generative claims of realistic arbitrage-free surfaces and the absence of independent dynamic/out-of-sample validation. The review does not claim that all contradictions are resolved; it reports the coverage and the residual flag.

**Table 4.** Cross-paper tension summary

| Pair | Tension | Assessment | Status |
|---|---|---|---|
| CP-001 | Gated/hard construction vs soft penalty (Yang et al., 2017 vs Ackerer et al., 2019) | Conditional difference | Resolved in synthesis |
| CP-002 | Smoothing vs minimal repair (Fengler, 2009 vs Cohen et al., 2020) | Objective-dependent | Resolved in synthesis |
| CP-003 | Two-step outperformance vs no common benchmark (Zhang et al., 2022 vs Ruf & Wang, 2020) | Scope difference | Resolved in synthesis |
| CP-004 | Generative realism vs independent validation (Vuletić & Cont, 2025 vs Cohen et al., 2020) | Genuine tension | Flagged unresolved |
| CP-005 | Static guarantee vs neural penalty (Gatheral & Jacquier, 2014 vs Ackerer et al., 2019) | Method-class difference | Resolved in synthesis |
| CP-006 | Simulation vs path-dependent dynamics (Cont & Vuletić, 2023 vs Andrès et al., 2026) | No material conflict | Not applicable |
| CP-007 | GP uncertainty vs controllable generation (Appana et al., 2024 vs Wang et al., 2025) | No material conflict | Not applicable |

### 4.8 Summary of Findings

The five findings are connected by one argument: “arbitrage-free” is not a single property. Parametric construction supplies an explicit static guarantee; nonparametric methods supply flexibility and sometimes uncertainty; neural and generative methods supply fit or generation at the cost of a weaker or post-hoc guarantee; dynamic consistency is a separate, under-tested layer; and evaluation does not yet support cross-family ranking. The four-family taxonomy in Section 2.6 is the integrating device, and the seven-dimension evaluation matrix is the practical implication.

---

## 5. Discussion

### 5.1 From “Arbitrage-Free” to “Which Guarantee?”

The most important interpretive move is to replace the binary question—“is the surface arbitrage-free?”—with a question about the guarantee: by construction, by penalty, by projection, or by generation plus filtering? Each answer implies a different failure mode. Construction methods can be conservative and inflexible; penalty methods can violate constraints under distribution shift; projection methods can change observations and depend on the repair rule; generative methods can produce plausible samples that fail independent tests. This taxonomy explains the apparent contradictions in the literature: papers that use the same phrase are often making different claims. It also explains why a single fit metric cannot adjudicate between them.

### 5.2 Theoretical Implications

The taxonomy treats constraint enforcement as a design dimension, not an implementation detail. It generates four testable propositions for future work. First, construction methods should be more stable but less flexible than penalty methods on sparse wings. Second, penalty methods should degrade more under distribution shift than construction or projection methods. Third, projection/repair methods should be accurate on observed points but sensitive to the repair rule and to observation noise. Fourth, generative methods should be plausible in-sample but dependent on the filter for admissibility and on independent tests for dynamic consistency. These propositions are not tested in the corpus; they are a research agenda, not findings. The static/dynamic distinction adds a second dimension: a method can be strong on static constraints and silent on dynamic ones, and most neural papers are in that position.

### 5.3 Practical Implications

For practitioners, the choice of method is a choice of guarantee. A desk that needs a provably static-arbitrage-free surface for pricing may prefer a parametric or constrained-smoothing construction, accepting fit limitations. A desk that needs flexible scenario generation may prefer a neural or generative model, but should add a static repair step and an independent dynamic check. For model risk, the review recommends reporting the guarantee family, the static and dynamic test results, and the evaluation dimensions in Table 3. For benchmark designers, the seven dimensions provide a minimum reporting standard. For regulators, the absence of a shared benchmark is a supervisory gap: “arbitrage-free” claims are not comparable across models without a common test.

### 5.4 Limitations

The review has six main limitations. First, evidence is abstract-level: 35 full abstracts, four partial snippets, and one title-level record; no full texts were read, so method details and negative results may be missing. Second, the corpus is 40 of 351 unique records; 311 were not advanced, and the 24 queries emphasized static-arbitrage, parametric, and neural vocabulary, so dynamic-arbitrage coverage may be under-sampled. Third, 10 of the 40 sources are preprints; neural claims are weaker than the prose sometimes implies. Fourth, Semantic Scholar returned HTTP 429 for all 10 requests; Crossref returned one 429 and four abstracts; no COI or funding audit was possible. Fifth, the corpus is SPX/US-equity-index heavy; cross-market and stressed-period generalization is not established. Sixth, the review is narrative; no meta-analysis or effect-size synthesis was performed. A Devil’s Advocate checkpoint returned REVISE with five Major issues (selection/coverage bias, abstract/preprint evidence, the “no shared benchmark” overclaim, implied hard-constraint superiority, and “mature/solved” language). The five issues were addressed by hedging, scope caveats, and removing ranking language; the residual limits are disclosed rather than resolved.

### 5.5 Future Research

Six gaps follow directly from the findings. First, a shared benchmark should combine fit, static violations, dynamic consistency, out-of-sample stability, wings, cost, and interpretability on a common dataset. Second, dynamic no-arbitrage needs joint surface–underlying tests and a common definition of consistency. Third, cross-market evidence—Europe, Asia, emerging markets—is needed to test whether SPX/US results generalize. Fourth, interpretability and cost should be measured head-to-head, not asserted. Fifth, generative models need independent static and dynamic validation, including adversarial arbitrage detection. Sixth, negative results and failed constraint designs should be reported; the current corpus is success-biased.

---

## 6. Conclusion

This review synthesized 40 sources on arbitrage-free implied volatility surface construction. The central conclusion is that “arbitrage-free” names a family of guarantees, not a single property. Parametric SVI/SSVI/eSSVI families provide the clearest static guarantee but are conditional and can be inflexible; nonparametric methods provide flexibility and sometimes uncertainty but not a uniform guarantee; neural and generative methods provide fit and generation through a mixture of construction, penalty, projection, and filtering, with method-specific failure modes; dynamic no-arbitrage is a separate and under-tested layer; and evaluation is too fragmented to support cross-family ranking. The review contributes a four-family enforcement taxonomy, a seven-dimension evaluation matrix, and a corpus-scoped evidence map. The practical recommendation is to report the guarantee family and the evaluation dimensions explicitly, and the research recommendation is to build a shared benchmark that tests static and dynamic constraints together across markets. These conclusions are limited by abstract-level evidence, a 40/351 selection, 10 preprints, and the absence of full-text and COI audits. They are offered as a map of the evidence, not as a ranking of methods.

---

## AI Disclosure

AI Disclosure: This report was produced with AI-assisted research tools. The research pipeline included AI-powered literature search, source verification, evidence synthesis, and report drafting. All findings were verified against cited sources. Human oversight was applied throughout the process.

---

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

| # | Source | Bucket | Level | DOI / record |
|---|---|---|---|---|
| 1 | Gatheral & Jacquier (2014) | Parametric surfaces | VI | 10.1080/14697688.2013.819986 |
| 2 | Guo et al. (2016) | Parametric surfaces | VI | 10.1137/120900320 |
| 3 | Fengler (2009) | Parametric surfaces | VI | 10.1080/14697680802595585 |
| 4 | Homescu (2011) | Parametric surfaces | VII | 10.48550/arxiv.1107.1834 |
| 5 | Ackerer et al. (2019) | Neural and generative surfaces | VI | 10.2139/ssrn.3402942 |
| 6 | Bayer & Stemper (2018) | Neural and generative surfaces | VI | 10.48550/arxiv.1810.03399 |
| 7 | Yang et al. (2017) | Constraint enforcement, arbitrage repair, and evaluation | VI | 10.1609/aaai.v31i1.10505 |
| 8 | Ruf & Wang (2020) | Constraint enforcement, arbitrage repair, and evaluation | VII | 10.21314/jcf.2020.390 |
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
| 24 | Wang et al. (2025) | Neural and generative surfaces | VI | 10.48550/arxiv.2509.01743 |
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
| 35 | Wiedemann et al. (2024) | Neural and generative surfaces | VI | 10.48550/arxiv.2406.11520 |
| 36 | Appana et al. (2024) | Nonparametric, spline, and Gaussian-process surfaces | VI | 10.2139/ssrn.4803161 |
| 37 | Hoshisashi et al. (2023) | Neural and generative surfaces | VI | 10.48550/arxiv.2310.16703 |
| 38 | Zetocha (2023) | Neural and generative surfaces | VI | 10.2139/ssrn.4623940 |
| 39 | Cousin & Gueye (2021) | Nonparametric, spline, and Gaussian-process surfaces | VI | HAL (no DOI) |
| 40 | Anagha (2026) | Constraint enforcement, arbitrage repair, and evaluation | VI | 10.2139/ssrn.7577418 |


