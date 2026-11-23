# Phase 2 — Paper Outline and Evidence Map

**Run:** `iv-surface-review-v047` · **Stage 2, Phase 2** · **Agent role:** structure architect · **Date:** 2026-11-23
**Inputs:** `phase0-config.md`; `phase1-literature.md`; frozen Stage 1 records (`phase3-synthesis.md`, `phase6-final.md`, `search/selected_sources.json`).
**Status:** outline approved under the operator's preauthorized `确认` (see §11). No restructuring requested.

**Review-criteria binding status:**

```text
criteria_binding_unavailable
```

No author-confirmed `ReviewTargetContext` exists; no `ReviewCriteriaBindingManifest` was initialized; no FORMATIVE receipt is issued. The paper makes no venue-alignment or submission-readiness claim. The status is inherited unchanged from `phase0-config.md` §4.

## 1. Structure Pattern and Overview

**Pattern.** Thematic literature review (Pattern 2), adapted with a full method section. The adaptation is deliberate: the review is corpus-scoped and auditable, so the search, screening, verification, and coding decisions must be visible in the body rather than compressed into a paragraph. The thematic core is §4–§5; §2 supplies the analytical vocabulary, §3 the evidence protocol, and §6 the interpretation and agenda.

**Thesis in one sentence.** The four method families are not competing answers to one question: each makes a different kind of "arbitrage-free" claim, backed by a different kind of evidence, and the corpus contains almost no dynamic enforcement and almost no directly comparable evidence.

**Sections at a glance.**

| § | Section | Body words | Primary sources | Tables / figures |
|---|---|---|---|---|
| 1 | Introduction | 700 | S3, S4, S5, C2 | — |
| 2 | Theoretical framework: what "arbitrage-free" must mean | 1,100 | S1, P1, P2, P8, C2, C3, C4, C5, G7, R3, R6, N1 | Figure 1 |
| 3 | Method: corpus, verification, and comparability | 900 | corpus-level; C5 scope flag | Table 1; Figure 2 (optional) |
| 4 | Findings I: how each family enforces static admissibility | 1,500 | P1–P8, N1–N6, R1–R9, G1–G8 | Table 2 |
| 5 | Findings II: evidence status, comparability, and evaluation coverage | 1,250 | representative rows from all groups | Tables 3, 4, 5, 6 |
| 6 | Discussion: four meanings, the dynamic void, and an agenda | 1,300 | C1–C5, P8, G1–G5, G7, R1, R5–R7, N2, N4, N5, P2, P6, S5 | — |
| 7 | Conclusion | 650 | synthesis only; no new sources | — |
| | **Total** | **7,400** | 41 references | 6 tables, 2 figures |

## 2. Title and Abstract Plan

### 2.1 Title

**Four Loci of Enforcement: Static and Dynamic No-Arbitrage in Equity-Index Implied-Volatility Surfaces, 2015–2026**

*Subtitle:* A structured, corpus-scoped review and a proposed framework for enforcement claims.

The title names the contribution (four loci), the object (static and dynamic no-arbitrage), the asset class, and the window. "Four loci" is defined in §2.3 and used throughout; it is not a ranking.

### 2.2 Abstract Plan (Standard regime)

**English abstract — target 200 words (range 150–250).** Five components, no citations, no undefined abbreviations:

| Component | Planned content | Target words |
|---|---|---|
| Context | Implied-volatility surfaces are central to pricing and risk; "arbitrage-free" is routinely used as a completion label | 35 |
| Problem | The label conflates static admissibility with dynamic consistency, and a theorem with a finite-sample audit | 35 |
| Purpose and method | Structured, corpus-scoped review of 41 sources (2015–2026 plus seminal precursors); coding of enforcement locus, evidence status, and comparability; no meta-analysis | 45 |
| Findings | Four enforcement loci; static admissibility is enforceable but object-specific; no source enforces or tests a dynamic condition; proof and audit evidence are nearly disjoint; direct cross-family comparison is unavailable | 55 |
| Implications | State the condition, the tolerance, and the verification mode; seven-study agenda for dynamic enforcement, head-to-head comparison, and residual audits | 30 |

**Chinese abstract (Simplified) — target 420 characters (range 300–500).** Independently written, not a translation; same five components; no citations; 6 keywords. The Chinese text will use established terms (隐含波动率曲面, 静态无套利, 动态无套利, 证据状态, 可比性) and will not introduce English abbreviations without expansion.

**Keywords (6 each).**
- English: implied volatility surfaces; no-arbitrage constraints; static arbitrage; dynamic arbitrage; model-free constraints; structured literature review.
- Chinese: 隐含波动率曲面；无套利约束；静态套利；动态套利；模型无关约束；结构化文献综述。

**Abstract consistency rule.** Both abstracts report the same findings at the same granularity. They do not report a number that the body does not support, and they do not attribute corpus aggregates to individual sources.

## 3. Review Criteria Coverage Plan

| Criterion ID | Planned section(s) | Evidence need / unresolved check | Dimension |
|---|---|---|---|
| `criteria_binding_unavailable` | n/a | No author-confirmed target review context; no registry criteria selected; no FORMATIVE receipt issued | n/a |

**Explanation.** The Phase 0 record contains no target journal, track, article type, or venue selection. Under #684, the degraded path applies: the review discloses `criteria_binding_unavailable`, makes no venue-alignment claim, and treats its criteria coverage as non-comparable to a venue-bound review. No criterion ids are invented, no registry prose is copied, and no receipt is created. Phase 6a's INTERNAL receipt is likewise not applicable in this task.

## 4. Detailed Outline

### 4.1 Section 1 — Introduction (700 words)

**Purpose.** Establish the practical and conceptual problem, state the research question and hypotheses, and delimit the contribution.

**Serves:** all sub-questions; frames H1–H3.

**1.1 Context and Problem (280 words).**
- Implied-volatility surfaces are a working object in pricing, risk, and model validation; interpolation and completion are routine.
- The completion literature has a long record of surfaces that looked smooth but violated static constraints: S3's finite-strike SABR arbitrage is the canonical failure; S4 and S5 are pre-constraint constructions that did not enforce admissibility.
- Practice labels a completed surface "arbitrage-free" without saying which condition was checked, at what tolerance, or by what mode (theorem, test, or assumption).
- Preview the corpus and the finding that the label hides four different claims.
- **Sources:** S3, S4, S5, C2.
- **Trace:** `phase6-final.md` §1.1–1.2; `phase3-synthesis.md` §1–2.

**1.2 Purpose, Research Questions, and Contribution (260 words).**
- State the RQ verbatim from Phase 0 and the three sub-questions (SQ1 static conditions and mechanisms; SQ2 dynamic requirements; SQ3 trade-offs).
- Pre-declare H1–H3: static enforcement is mostly by construction; dynamic requirements are asserted or tested rather than proved; penalty/repair routes may displace rather than remove the constraint burden; generation-filtering's "arbitrage-free" often means "not rejected on this sample."
- Contributions: a 41-source evidence map; the four-locus framework; the proof/audit gap; the dynamic void; a comparability discipline that forbids ranking; a seven-study agenda.
- **Sources:** none new.
- **Trace:** `phase6-final.md` §1.3; `phase1-scoping.md` H1–H3.

**1.3 Scope and Organization (160 words).**
- Boundaries: equity-index listed options; 2015–2026 plus five seminal precursors; four focal families plus two supporting groups; English-language records; abstract-level evidence.
- One disclosed exception: C5's single-stock panel, retained with a scope flag and never generalized to index surfaces.
- Roadmap: framework (§2), method (§3), family findings (§4), cross-family evidence (§5), discussion and agenda (§6), conclusion (§7).
- **Sources:** C5 (scope flag only).
- **Trace:** `phase6-final.md` §1.5; `phase1-scoping.md` scope.

**Transition to §2.** The introduction uses "arbitrage-free" loosely on purpose; §2 replaces the loose phrase with explicit static and dynamic conditions.

### 4.2 Section 2 — Theoretical Framework: What "Arbitrage-Free" Must Mean (1,100 words)

**Purpose.** Define the static object, the dynamic requirement, and the enforcement triple that organizes the findings. This section supplies the vocabulary; it does not re-derive proofs.

**Serves:** SQ1 and SQ2 conceptually.

**2.1 Static Admissibility: Conditions SC1–SC5 (420 words).**
- Define the normalized call price `c(k, τ)` and total implied variance `w(k, τ)`; state the no-arbitrage restrictions used in the corpus.
- **SC1:** nonnegative time value, `c(k,τ) ≥ max(1 − e^k, 0)`.
- **SC2:** monotone decreasing call price in strike, `∂c/∂k ≤ 0`.
- **SC3:** strike convexity (Durrleman's condition), `∂²c/∂k² ≥ 0`.
- **SC4:** the zero-maturity limit matches the intrinsic value.
- **SC5:** calendar monotonicity of total variance in maturity, `∂w/∂τ ≥ 0` (equivalently, non-decreasing total variance across maturities at fixed moneyness).
- Distinguish sufficient from necessary conditions; note that S1's closed-form SVI conditions are sufficient, P2's characterisation via −d1/−d2 monotonicity is exact for the SVI slice, and P1's parameter-domain construction guarantees admissibility on the admitted set.
- **Scale note:** conditions are checked in specific units (price, total variance, moneyness); a guarantee at one scale is not automatically a guarantee at another. S3 and C4 are the running examples.
- **Sources:** S1, P1, P2, P8; operationalized by R5, G5, G6.
- **Trace:** `phase6-final.md` §2.1; `phase3-synthesis.md` §5.1.

**2.2 Dynamic Admissibility: What a Process-Level Guarantee Requires (320 words).**
- A static condition constrains one surface; a dynamic condition constrains a family of surfaces indexed by calendar time, usually through a filtered probability space and a martingale representation.
- State what would count as a dynamic test: a process-level property (e.g., absence of predictable arbitrage across dates, consistency of the surface with a martingale measure) checked over a path, not a within-surface condition.
- The corpus contains no such test. C2 reviews the question; G7 explicitly limits its claim to static admissibility; C3 builds path-dependent surfaces that are statically free but does not test dynamic consistency; P8 reports time-indexed arbitrage probabilities for parametric models; C5's single-stock panel is dynamic-adjacent but scope-flagged.
- **Terminology guard:** a calendar (maturity-monotonicity) condition is static. It is not evidence of dynamic consistency. The paper will say so every time the ambiguity appears.
- **Sources:** C2, G7, P8, C3, C5, C4, S3.
- **Trace:** `phase6-final.md` §2.1, §4.5; `phase3-synthesis.md` §2.2, §5.1.

**2.3 The Enforcement Triple and the Four Loci (360 words).**
- Define the triple: **mechanism** (where the constraint enters), **evidence** (what the row licenses), **verification** (what was actually checked on the output). Figure 1 presents the triple and the four loci.
- Four loci: parameter domain (P); objective/loss (N); output image after a map (R); sampler plus acceptance test (G).
- Three propositions: (i) when the guarantee is inherited from a deterministic decoder, the method is parametric in logical shape, whatever its learning apparatus; (ii) a penalty is a sampling device, so its compliance is conditional on weight and tolerance; (iii) construction and repair differ in what is observed — an admitted parameter set versus a transformed surface — so their guarantees are not the same object.
- Boundary cases (R3, R6, N1) are flagged rather than forced into a family; G7 and C3 are model-level constructions whose guarantee is inherited.
- **Sources:** all four family groups; R3, R6, N1, G1, G6, G7, G8.
- **Trace:** `phase3-synthesis.md` §5.2–5.3; `phase6-final.md` §2.2.

**Transition to §3.** With the object and the loci defined, §3 explains how the 41-row evidence base was assembled and graded.

### 4.3 Section 3 — Method: Corpus, Verification, and Comparability (900 words)

**Purpose.** Make the review reproducible and bound its claims.

**Serves:** all sub-questions; establishes the evidence rules used in §4–§5.

**3.1 Corpus Construction (360 words).**
- OpenAlex REST; 31 free-text queries in eight groups; 25 records per query; window 2015-01-01 to 2026-11-23; English.
- Retrieval: 775 requested, 750 returned; one query lost after HTTP 429 ("SVI stochastic volatility inspired"); 21 first-pass 429 responses, 20 recovered; one citation-chaining pass with no additional included source.
- Screening: 430 unique after de-duplication; 389 excluded under eight reason codes; 41 included (36 in-window + 5 seminal).
- Inclusion frame: index options; construction/enforcement object; static or dynamic constraint; English; retrievable abstract; one record per study.
- **Conformity:** "PRISMA-style, not PRISMA-compliant"; no PRISMA or PRISMA-ScR claim. Figure 2 (optional) shows 750 → 430 → 389 excluded → 41, explicitly labeled not a PRISMA diagram.
- **Sources:** corpus-level; C5 scope exception.
- **Trace:** `phase6-final.md` §3.1–3.2; `phase2-bibliography.md`.

**3.2 Verification and Evidence Grading (300 words).**
- 41/41 DOI resolution; 0 retracted per OpenAlex `is_retracted`; no independent retraction-database sweep.
- Abstract coverage: 34 full, 4 partial (R2, G3, C4, S1), 3 metadata-only (P4, P7, R4). Metadata-only rows are used at title level only.
- Evidence levels VI (40) and VII (1, C2); overall quality labels A 11 / B 13 / C 17. Quality labels are appraisal labels, not performance ranks.
- **Evidence status** is coded per row as **proof** (a theorem or formal construction), **numerical test** (a reported residual/violation check on the row's own output), or **assumption** (asserted or inherited without proof or test). A test is never upgraded to a proof.
- Preprints: 11/41 (26.8%), each labeled; four from 2025–2026.
- No theorem was checked and no reported number recomputed in this review.
- **Sources:** verification records; no individual source claims.
- **Trace:** `phase6-final.md` §3.3–3.4; `phase2-verification.md`.

**3.3 Comparability Coding and Analytic Boundaries (240 words).**
- Three comparability codes: **direct** (same dataset/panel, same condition set and tolerance, same metric and aggregation, same protocol), **context** (reported for background; not comparable), **not comparable** (different object or metric).
- Result: 0 direct / 30 context / 11 not comparable. Within-study baselines (e.g., G6 against SSVI and a soft-penalty MLP) are the only licensed comparisons.
- Consequences: no league table, no vote counting, no method ranking; results are reported as ranges and conditions.
- Limits: single analyst; abstract-level evidence; no full text, proof, or code retrieval.
- **Sources:** corpus-level.
- **Trace:** `phase6-final.md` §3.4–3.5, §4.6.

**Transition to §4.** The evidence rules are now fixed; §4 applies them family by family.

### 4.4 Section 4 — Findings I: How Each Family Enforces Static Admissibility (1,500 words)

**Purpose.** Answer SQ1 for each family: which static conditions, by what mechanism, at what evidence status.

**Serves:** SQ1; H1; CL1, CL2, CL8.

**4.1 Parametric Construction (380 words).**
- Mechanism: restrict the parameter domain so every admitted parameter vector yields an admissible surface. Literature: P1 (generalized SVI), P2 (exact butterfly characterisation), P3 (global eSSVI across maturities), P5 (random-coefficient family), P6 (C3 interpolation), P8 (bounded-factor conditions). P4 and P7 are title-level only.
- Evidence: 6 of 8 rows proof; no row reports a residual audit on observed quotes; no row tests a dynamic condition.
- Cost: the guarantee can tighten wings or reduce fit; the corpus does not pair the guarantee with a fit-cost measurement (see §5.3), so any cost is stated qualitatively rather than measured.
- Boundary: R3's interpolation-by-distortion and R6's LP construction show that a proof-bearing constructor and a repair can share the same observable; P1's parameter set is the cleanest "by construction" case.
- **Sources:** P1–P8, S1; cross-reference R3, R6.
- **Table 2** introduced at the start of 4.1.
- **Trace:** `phase6-final.md` §4.2, Table 4; `selected_sources.json`.

**4.2 Penalty and Constrained Learning (380 words).**
- Mechanism: add a violation term (or a differentiable constraint surrogate) to the training objective; compliance is approximate and conditional on weight, tolerance, and early stopping.
- Literature: N1 (gated network with constraint-bearing slopes/weights), N2 (graph neural operator, 10-year intraday SPX adherence report), N3 (soft penalties plus plug-in correction), N4 (GAN with arbitrage loss on ALSI), N5 (penalty minimization vs an ANN), N6 (DCNN with derivative constraints on SABR-generated data).
- Evidence: 0 of 6 proof; all six are numerical tests; N4 states the condition cannot be directly learned; residual violations persist.
- Boundary: N1's gate is architectural, so it is a penalty/architecture hybrid; the paper flags it rather than claiming the penalty route alone explains the result.
- **Sources:** N1–N6.
- **Trace:** `phase6-final.md` §4.2; `selected_sources.json`.

**4.3 Projection and Repair (380 words).**
- Mechanism: fit first, then map the output onto an admissible set (LP projection, Sinkhorn/MOT, distortion of a reference function, observation-anchored adjustment, Chebyshev + QP).
- Literature: R1 (LP repair), R2 (Sinkhorn/MOT with convergence proof), R3 (distortion of an arbitrage-free reference), R4 (joint American smoothing; title-level), R5 (observation-anchored repair; 252 OOS SPX days; ~5.4% butterfly floor), R6 (SANOS strict construction), R7 (Chebyshev + QP; <1% violations; 98–99% inside-spread coverage), R8 (asserted transformations), R9 (Markov-chain approximations).
- Evidence: 3 proof / 4 test / 2 assumption; the proofs are about the map or the reference construction, not about the repaired surface's dynamic behavior.
- Cost: repair can distort the fit; R5 and R7 report residual floors; none reports a cross-date enforcement test.
- Boundary: R3 and R6 sit between construction and repair; the paper retains both and explains why the boundary is real.
- **Sources:** R1–R9; S2 as the early spline baseline.
- **Trace:** `phase6-final.md` §4.2; `selected_sources.json`; `phase2-verification.md` flags.

**4.4 Generation and Filtering (360 words).**
- Mechanism: generate candidate surfaces (or parameters) and accept, reject, project, or constrain them; the guarantee may be inherited from the generator's model class or enforced by a penalty/acceptance test.
- Literature: G1 (VAE over SDE parameters; inherited), G6 (trainable hard constraints; 0.00% at 1e-4 over 15 runs on synthetic SVI), G7 (neural-SDE state space; static-only claim), G8 (gated network rational by design); G2 (VolGAN; enforcement not described), G3 (simulation; partial abstract), G4 (GAN denoiser), G5 (flow matching; 90.8% pass rate).
- Evidence: 4 proof / 3 test / 1 assumption; the split tracks the locus: inherited guarantees look parametric in logical shape, while penalized sampling reports pass rates.
- Cost: G6 is the only row reporting both a structural guarantee and an audit, on synthetic data, with higher RMSE; G5's 90.8% is a pass rate, not a guarantee.
- Boundary: G7 is a model-level construction, not a data-driven generator; C3 is adjacent but classified under conditions.
- **Sources:** G1–G8; N1, C3 for boundaries.
- **Trace:** `phase6-final.md` §4.2, §4.3; `selected_sources.json`.

**Transition to §5.** The family accounts show different mechanisms; §5 asks what evidence they jointly license and what can be compared.

### 4.5 Section 5 — Findings II: Evidence Status, Comparability, and Evaluation Coverage (1,250 words)

**Purpose.** Answer SQ1's evidence-status clause and SQ3's trade-off clause, and establish the limits of cross-family inference.

**Serves:** SQ1, SQ3; H1–H3; CL3–CL6.

**5.1 Evidence Status and the Proof–Audit Gap (420 words).**
- Report the distribution: 17 proof / 16 numerical test / 8 assumption; in-window 16 / 14 / 6; per family P 6/0/2, N 0/6/0, R 3/4/2, G 4/3/1, C 3/1/1, S 1/2/2. **Table 3.**
- The key cross-tab: among 17 proof rows, no row reports a violation rate; among 6 rows that audit their own output (N2, N6, R5, R7, G5, G6), only G6 also reports a structural guarantee, and it does so on synthetic SVI data. **Table 4** adjudicates H1–H3.
- H1: the static clause is supported (all 41 rows are coded on a static predicate; 6 of 8 parametric rows are proof-level); the dynamic clause is disconfirmed as stated — dynamic enforcement is absent, not asserted-and-tested (0 of 36 in-window rows).
- H2: the "lower fit error" clause is unsupported (no penalty/repair row reports a lower fit error than a constrained parametric baseline on the same data; G6 reports a cost); the burden-displacement clause is supported (tolerance, weight, repair, and acceptance-test choices absorb the constraint).
- H3: supported for the penalized-sampling branch (G5's 90.8% pass rate); disconfirmed for the inherited-guarantee branch (G1, G6, G7, G8 are structural, not sample-filtered).
- Metadata-only rows are not counted as evidence for their claims; preprints are labeled.
- **Sources:** evidence-status rows across all groups; audit rows N2, N6, R5, R7, G5, G6; G1, G7, G8.
- **Trace:** `phase6-final.md` §4.1, §4.3, Table 1; `phase1-literature.md` §6.

**5.2 Comparability and the Metric Vocabulary (380 words).**
- Report 0 direct / 30 context / 11 not comparable; **Table 5** breaks it down by family (P 0/4/4; N 0/6/0; R 0/6/3; G 0/8/0; C 0/2/3; S 0/4/1).
- Four fields are required for a direct comparison: same dataset/panel; same condition set and tolerance; same metric and aggregation; same protocol. No row reports all four; tolerance is the most frequently missing.
- Seven metric families appear (price-space, volatility-space, total-variance, bid–ask spread, Wasserstein, hedging P&L, runtime). A reported number is context unless the protocol matches.
- Within-study baselines are the only licensed comparisons (G6 vs SSVI and a soft-penalty MLP; N4 vs a VAE; N5 vs an ANN; R5 across five backends). They compare implementations, not families.
- Consequence: no ranking; the paper reports ranges and conditions, not a league table.
- **Sources:** N1, N2, G2, G4, G5, N4, R5, R6, R7, R9, C1, G6.
- **Trace:** `phase6-final.md` §4.6; `phase3-synthesis.md` §5.5.

**5.3 Evaluation Coverage: Seven Dimensions (450 words).**
- Report the seven-dimension matrix (**Table 6**): static no-arbitrage (41/41 coded; 17 proof / 16 test / 8 assumption; tolerances rarely stated); dynamic consistency (10 rows engage time; 0 enforce or test; unpopulated); fit accuracy (~8 rows; datasets disjoint; partial, not comparable); interpolation and stability (~8 rows; thin, no boundary audit); computational cost (~5 claims; 0 comparable; asserted); interpretability (0 rows; unpopulated); data efficiency (0 learning curves; unpopulated).
- Distinguish **coverage** (whether a dimension is measured) from **performance** (whether a method is good). The matrix is a coverage map, not a scorecard.
- The pattern: the static dimension is populated; the dynamic, interpretability, and data-efficiency dimensions are empty; fit and interpolation are partial; cost is asserted. This is the empirical basis for the agenda in §6.3.
- **Consistency note for the draft writer:** `phase6-final.md` Table 3 reports eight coverage axes (it adds extrapolation/wings and reproducibility and treats data efficiency in the agenda). The manuscript uses the seven-axis frame specified for Stage 2 and records the reconciliation in Appendix C. No count and no claim changes.
- **Sources:** representative rows: P1, P2, P3, P5, P6, P8, R2, R3, R5, R6, R7, G1, G5, G6, G7, G8, N2, N6, C1, C4, S1–S5.
- **Trace:** `phase3-synthesis.md` §5.4; `phase6-final.md` §4.3, §4.5.

**Transition to §6.** The findings establish what the corpus licenses; §6 interprets why the disagreement is verbal and what would resolve it.

### 4.6 Section 6 — Discussion: Four Meanings, the Dynamic Void, and an Agenda (1,300 words)

**Purpose.** Interpret the findings, answer the RQ, and convert the gaps into a falsifiable research agenda.

**Serves:** all sub-questions; CL7, CL9, CL10.

**6.1 Four Meanings of One Word (320 words).**
- "Arbitrage-free" in this corpus means one of: a theorem over a parameter set; a penalty minimized to a tolerance; an output mapped onto an admissible set; an accepted sample that passed a test. These are four claims, not four degrees of the same claim.
- The reporting remedy is a triple: state the condition (which of SC1–SC5 or a dynamic condition), the tolerance (numerical or exact), and the verification mode (proof, test, assumption). A surface is "admissible under condition X at tolerance Y by mode Z," not "arbitrage-free."
- Implications: authors should report the enforcement locus and verification mode; reviewers should ask for the missing element; readers should not compare numbers across modes.
- **Sources:** P, N, R, G groups; G6 as the only row reporting all three elements (on synthetic data); N4/N5 as penalty concessions.
- **Trace:** `phase6-final.md` §5.1–5.2; `phase3-synthesis.md` §5.2.

**6.2 The Dynamic Void and Calendar Conflation (300 words).**
- The absence is not a proof that the field ignores dynamics; it is a bounded finding about 41 abstracts. Two explanations are possible: a genuine gap, or a retrieval/vocabulary effect (papers may test dynamics under different labels). The review cannot distinguish them, and says so.
- The calendar conflation is the main reason the gap is easy to miss: a maturity-monotonicity condition is static, but it is often described as "calendar arbitrage," which sounds dynamic. G5, G6, and R5 use calendar conditions in the static sense; G7 explicitly disclaims dynamics; C2 is the only sustained dynamic discussion; C3 and P8 construct time-indexed objects without a dynamic test.
- Scale relativity: S3's finite-strike SABR arbitrage and C4's asymptotic arbitrage-free approximation are compatible only in the asymptotic regime; a guarantee at one scale is not a guarantee at another.
- **Sources:** C2, C3, C4, C5, P8, G5, G6, G7, R5, S3.
- **Trace:** `phase6-final.md` §4.5, §5.1; `phase3-synthesis.md` §5.1–5.3.

**6.3 A Priced-Trade-Off Research Agenda (480 words).**
Seven studies, each tied to a gap and to a measurable outcome. All are proposals; none is reported as done.

| # | Study | Design sketch | What it resolves |
|---|---|---|---|
| 1 | Dynamic enforcement test | Take a surface family with a stated process (starting from C3/P8); define a path-level admissibility test; run it over a multi-year index panel | Gap 1; turns "dynamic" from a label into a testable condition |
| 2 | Pre-registered head-to-head | One index panel (SPX plus one non-US index); common condition set, tolerance, metric, and aggregation; freeze the protocol before fitting | Gap 2; licenses the first direct comparison |
| 3 | Residual audit for proof constructions | Apply C1's detector to proof-bearing P and R rows; report violations at a stated tolerance on observed quotes | Gap 3; tests whether proofs survive finite-sample implementation |
| 4 | Test power and noise floor | Simulation plus observed data; estimate the false-positive/false-negative rate of the violation tests; separate data noise from method error (R5's 5.4% floor is the motivating case) | Gap 4; makes "passed the test" interpretable |
| 5 | Data-efficiency curves | Violation rate and fit as a function of quote count, date count, and training size | Gap 5; informs sparse-data use |
| 6 | Cross-market replication | Three indices, including at least one non-US market; same protocol as study 2 | Gap 6; tests index generality |
| 7 | Measured cost and interpretability | Wall-clock/memory on a fixed grid; parameter/density interpretability rubric | Gap 7; prices the trade-off |

- Each study names the claim it would falsify; none is a call for "more research" in general.
- The agenda is the framework's test: if the loci are real, the studies should produce different evidence types for different families, not a single ranking.
- **Sources:** C1, G5, R5, P8, C3, C4, S3, plus the gap map in `phase1-literature.md` §8.
- **Trace:** `phase6-final.md` §6.1; `phase3-synthesis.md` §4.3.

**6.4 Limitations (200 words).**
- Abstract-level only (34 full / 4 partial / 3 metadata-only); 11 preprints; single analyst; English-only, OpenAlex-only retrieval; US-index dominance (10 of 12 known-provenance rows); one query lost after HTTP 429; no full text, proof, or code check; no theorem re-derived and no number recomputed.
- The four-family taxonomy and the seven-dimension matrix are proposed instruments, not validated ones; boundary cases are disclosed rather than resolved.
- The review makes no PRISMA claim, no field-wide absence claim, and no ranking.
- C5's single-stock panel is a disclosed scope exception, not index evidence.
- **Trace:** `phase6-final.md` §5.3, §7; `phase6-revision-log.md` residual limitations.

**Transition to §7.** The limitations bound the conclusion; §7 states what survives them.

### 4.7 Section 7 — Conclusion (650 words)

**7.1 Key Takeaways (380 words).**
- Answer the RQ in four moves: static admissibility is enforceable but on four different objects; dynamic admissibility is not enforced or tested anywhere in the corpus; proof and audit evidence are nearly disjoint; direct comparison is unavailable, so no ranking is possible.
- Restate the framework: mechanism, evidence, verification; four loci; the claim triple (condition, tolerance, mode).
- State the bounded absence carefully: 0 of 41 abstracts, 0 of 36 in-window, 0 of 31 construction rows; not a claim about the field.
- **Sources:** synthesis only; no new citations.

**7.2 Implications and Closing (270 words).**
- For authors: report the condition, tolerance, and verification mode; report an audit even when the construction is a proof; state whether the claim is static or dynamic.
- For reviewers and editors: ask for the missing element; do not accept "arbitrage-free" as a complete description.
- For practitioners: the corpus does not identify a best method; it identifies what each method's guarantee is worth and what it costs.
- Closing line: the question is not whether a surface is arbitrage-free, but which admissibility claim its construction licenses and how that claim was checked.
- **Sources:** none new.

## 5. Word Count Summary

| Section | Subsections | Words | % of body |
|---|---|---|---|
| 1 Introduction | 1.1 (280) + 1.2 (260) + 1.3 (160) | 700 | 9.5% |
| 2 Theoretical framework | 2.1 (420) + 2.2 (320) + 2.3 (360) | 1,100 | 14.9% |
| 3 Method | 3.1 (360) + 3.2 (300) + 3.3 (240) | 900 | 12.2% |
| 4 Findings I | 4.1 (380) + 4.2 (380) + 4.3 (380) + 4.4 (360) | 1,500 | 20.3% |
| 5 Findings II | 5.1 (420) + 5.2 (380) + 5.3 (450) | 1,250 | 16.9% |
| 6 Discussion | 6.1 (320) + 6.2 (300) + 6.3 (480) + 6.4 (200) | 1,300 | 17.6% |
| 7 Conclusion | 7.1 (380) + 7.2 (270) | 650 | 8.8% |
| **Total** | | **7,400** | **≈100%** |

**Tolerance:** the draft may land anywhere in 7,030–7,770 body words (target ±5%); the skill's external tolerance is ±10%; the PCR ceiling of 8,000 words is hard and is never exceeded. No section falls below 200 words; the lowest heading (6.4, 200) meets the 150-word minimum. Word counts exclude the title, abstract, keywords, tables, figure captions, references, declarations, and appendices.

## 6. Tables and Figures Plan

| ID | Item | Placement | Content | Status |
|---|---|---|---|---|
| T1 | Corpus profile | §3.1 | Search, screening, composition, abstract coverage, evidence status, comparability, quality labels | Required |
| T2 | Four-family evidence summary | §4.1 | Six rows: four focal families + conditions/evaluation + seminal baselines; locus, object, guarantee shape, evidence licensed, verification reported, row ids | **Required** |
| T3 | Evidence-status distribution | §5.1 | proof / test / assumption by family; in-window and seminal splits; audit rows | **Required** |
| T4 | Hypothesis adjudication | §5.1 | H1–H3 verdicts and basis | Required |
| T5 | Comparability matrix | §5.2 | direct / context / not comparable by family; required fields | **Required** |
| T6 | Seven-dimension evaluation matrix | §5.3 | dimension, operationalization, coverage, status, sources | **Required** |
| F1 | Enforcement triple and four loci | §2.3 | Mechanism–evidence–verification; four loci; boundary cases | Core |
| F2 | Corpus flow | §3.1 | 750 returned / 775 requested → 430 → 389 excluded → 41; explicitly not a PRISMA diagram | Optional |

**Table 2 detail.** Rows: parametric (P, n=8), penalty/constrained learning (N, n=6), projection–repair (R, n=9), generation–filtering (G, n=8), conditions/evaluation (C, n=5), seminal baselines (S, n=5). Columns: Family; n; Enforcement locus; Object claimed "arbitrage-free"; Guarantee shape; Evidence licensed; Verification reported; Rows. The four focal families are the paper's subject; C and S are supporting groups and are marked as such in the table. This keeps the required four-family summary without hiding the rest of the corpus.

**Skeletons for the four required tables (planning values, to be typeset in Phase 4).**

*Table 2 — Four-family evidence summary.*

| Family | n | Enforcement locus | Object claimed "arbitrage-free" | Guarantee shape | Evidence licensed | Verification reported | Rows |
|---|---|---|---|---|---|---|---|
| Parametric (P) | 8 | Parameter domain | Admitted parameter set | Universal over the admitted set | Proof (6); assumption/title-level (2); no residual audit | None in abstract | P1–P8 |
| Penalty (N) | 6 | Objective / loss | Evaluated sample at finite weight | Conditional on weight and tolerance | Residual rate; no guarantee | Residual or pass rate | N1–N6 |
| Projection–repair (R) | 9 | Output image | Surface after a map | Conditional on the projection | Proof (3), test (4), assumption (2); distortion plus residual | Residual floor | R1–R9 |
| Generation–filtering (G) | 8 | Sampler / acceptance | Accepted sample or inherited class | Within test power or model support | Proof (4), test (3), assumption (1); pass rate or architecture argument | Pass rate or proof | G1–G8 |
| Conditions / evaluation (C) | 5 | Diagnostic | Neither constructor nor repair | Detector or condition set | Proof (3), test (1), assumption (1); detection result or review | Detection / review | C1–C5 |
| Seminal baselines (S) | 5 | Pre-2015 baseline | Pre-constraint construction | No guarantee claim | Baseline only (1 proof, 2 test, 2 assumption) | None | S1–S5 |

*Table 3 — Evidence-status distribution.*

| Family | Proof | Numerical test | Assumption | Total | Audit rows |
|---|---|---|---|---|---|
| P | 6 | 0 | 2 | 8 | 0 |
| N | 0 | 6 | 0 | 6 | 2 (N2, N6) |
| R | 3 | 4 | 2 | 9 | 2 (R5, R7) |
| G | 4 | 3 | 1 | 8 | 2 (G5, G6) |
| C | 3 | 1 | 1 | 5 | 0 |
| S | 1 | 2 | 2 | 5 | 0 |
| **Total** | **17** | **16** | **8** | **41** | **6** |

In-window split: 16 proof / 14 test / 6 assumption (36 rows). Seminal split: 1 / 2 / 2 (5 rows). Audit rows report a residual or violation check on the row's own output; G6 is the only row that also reports a structural guarantee.

*Table 5 — Comparability matrix.*

| Family | Direct | Context | Not comparable | Total |
|---|---|---|---|---|
| P | 0 | 4 | 4 | 8 |
| N | 0 | 6 | 0 | 6 |
| R | 0 | 6 | 3 | 9 |
| G | 0 | 8 | 0 | 8 |
| C | 0 | 2 | 3 | 5 |
| S | 0 | 4 | 1 | 5 |
| **Total** | **0** | **30** | **11** | **41** |

A direct comparison requires the same dataset/panel, the same condition set and tolerance, the same metric and aggregation, and the same protocol. No row reports all four; tolerance is the most frequently missing field.

*Table 6 — Seven-dimension evaluation matrix (coverage, not performance).*

| Dimension | Operationalization | Coverage | Status |
|---|---|---|---|
| Static no-arbitrage | Condition set (SC1–SC5), tolerance, verification mode | 41/41 coded; 17 proof / 16 test / 8 assumption | Populated; tolerances rarely stated |
| Dynamic consistency | Path-level condition and test over time | 10 rows engage time; 0 enforce or test | Unpopulated |
| Fit accuracy | IV or total-variance error on held-out data | ~8 rows; datasets disjoint | Partial; not comparable |
| Interpolation and stability | Held-out strikes/maturities; repeated runs/subsamples | ~8 rows | Thin; no boundary audit |
| Computational cost | Wall-clock or memory on a fixed grid | ~5 claims | Asserted; 0 comparable |
| Interpretability | Density, wing, parameter recoverability | 0 rows | Unpopulated |
| Data efficiency | Fit/violations vs quote, date, or training size | 0 learning curves | Unpopulated |

The table is a coverage map, not a scorecard; no column orders methods. The reconciliation with the Stage 1 eight-axis coverage table is recorded in Appendix C.

## 7. References Plan

- **Count:** 41 — P 8, N 6, R 9, G 8, C 5, S 5. No additions, no deletions.
- **Style:** APA 7.0; alphabetical by first author; hanging indent; DOI where available; preprint labels; metadata-only rows flagged; version notes for the four entries whose published version differs (Cohen et al. 2021; Fengler et al. 2006; Gatheral & Jacquier 2013; Vuletić & Cont 2024).
- **Coverage:** every one of the 41 sources is cited at least once in §1–§7; Appendix B maps each id to its sections. The three metadata-only rows (P4, P7, R4) are cited at title level only.
- **No new references:** the corpus is frozen. Any addition would be a scope change and a new verification pass.
- **Checks:** Phase 5a citation compliance will verify in-text/reference correspondence, DOI formatting, and zero orphans. Self-citation ratio is 0% (sole author has no cited work). No citation counts are used as quality evidence.
- **Reference anchor:** `phase6-final.md` contains the 41-entry APA list; Phase 4 should reuse it, checking each entry against `selected_sources.json`.

## 8. Appendices Plan

| Appendix | Content | Why it is needed |
|---|---|---|
| A | Search and screening record: 31 queries by group; retrieval arithmetic (775 requested / 750 returned); exclusion codes and counts; two replacements; 40 discretionary exclusions; no-PRISMA statement | Reproducibility without claiming PRISMA conformity |
| B | Evidence ledger: 41 rows with id, family, evidence status, constraint axis, quality label, comparability, sections, flags, abstract coverage | Makes the evidence map auditable; supports the "no new sources" attestation |
| C | Coding protocol and reconciliation: static condition definitions; dynamic definition; evidence-status rules; comparability rules; quality-label rules; boundary cases; single-analyst limitation; seven-axis vs eight-axis reconciliation; aggregate counts are review coding | Defines the instruments and discloses their limits |

## 9. Evidence Map by Section

| Section | Sources | Claims served | Tables / figures |
|---|---|---|---|
| 1 Introduction | S3, S4, S5, C2 | Context; C7 setup | — |
| 2 Framework | S1, P1, P2, P8, C2, C3, C4, C5, G7, R3, R6, N1 | CL1, CL2, CL7 | F1 |
| 3 Method | corpus-level; C5 scope flag | Evidence protocol; C5 discipline | T1; F2 optional |
| 4 Findings I | P1–P8, N1–N6, R1–R9, G1–G8 | CL1, CL2, CL8 | T2 |
| 5 Findings II | P1–P3, P5–P6, P8, R2, R3, R5–R7, G1, G5–G8, N2, N6, C1, C4, S1–S5 | CL3–CL6 | T3, T4, T5, T6 |
| 6 Discussion | C1–C5, P8, G1–G5, G7, R1, R5–R7, N2, N4, N5, P2, P6, S5, N1 | CL7, CL9, CL10 | — |
| 7 Conclusion | none new | Synthesis | — |

**Coverage check.** All 41 sources appear at least once: 31 in §4, 4 in §1 (S3, S4, S5, C2), 4 new in §2 (S1, C3, C4, C5), 2 new in §5 (S2, C1). The map is complete and no source is orphaned.

## 10. Quality Gate Self-Check

| Check | Result |
|---|---|
| Recognized structure pattern | Yes — Pattern 2, adapted with a method section; adaptation explained in §1 |
| Every section has a purpose and a sub-question mapping | Yes — §4.1–§4.7 include Purpose and Serves |
| Word budgets sum to target within ±5% | Yes — 7,400 exactly; target 7,400 |
| Every Phase 1 source assigned to ≥1 section | Yes — 41/41 in §9 |
| Transitions at every section boundary | Yes — one transition per section |
| Heading depth and minimum content | Two heading levels (H2/H3); no lowest heading below 150 words (minimum 160 in §1.3; 6.4 is 200) |
| Abstract regime | Standard; EN 150–250 (target 200); zh-Hans 300–500 characters (target 420); 6 keywords each |
| References | 41; APA 7.0; no new sources |
| Review criteria | `criteria_binding_unavailable` disclosed; no venue claim; no receipt |
| Anti-patterns | No ranking; no PRISMA claim; no fabricated evidence; no scope creep; no field-wide absence claim |
| Approval before Phase 3 | Preauthorized `确认`; recorded in §11 |

## 11. Handoff and Approval Record

**Approval.** The operator preauthorized both checkpoints for this unattended run with `确认`: the Phase 0 record and this outline. No interactive approval prompt was issued; no restructuring was requested.

**Handoff to argument_builder (Phase 3).** The approved outline fixes the seven-section structure, the word budgets, the ten-claim allocation, the six tables, and the two figures. Phase 3 may specify argument chains, counter-arguments, and strength assessments; it may not add sources, change the thesis silently, or convert a proposed framework into a finding. The review-criteria status remains `criteria_binding_unavailable`; no FORMATIVE receipt exists to reuse, and no venue-fit claim may be made.

**Handoff to draft_writer (Phase 4).** Draft within the budgets; keep the boundary cases visible; label metadata-only and preprint rows; use "reports" for what a source did and "the review codes" for aggregate counts; never call a numerical test a proof. The abstract plan, declarations, and appendices are fixed here.
