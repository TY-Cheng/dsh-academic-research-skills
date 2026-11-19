# Phase 3 — Synthesis Report

**Project:** Arbitrage-Free Implied Volatility Surface Construction: A Structured Literature Review of Parametric, Nonparametric, and Neural Approaches  
**Stage:** `deep-research` full — Phase 3 (synthesis)  
**Corpus:** 40 sources (30 peer-reviewed, 10 preprints; 2013–2026)  
**Artifact:** `examples/dsh/iv-surface-review/phase3-synthesis.md`  
**Date:** 2026-11-19  
**Author:** TY-Cheng (DSH e2e run)

**Research question.** How do parametric, nonparametric, and neural methods for constructing equity-index implied volatility surfaces enforce static and dynamic no-arbitrage constraints, and what trade-offs do they report across fit, stability, extrapolation, computational cost, and interpretability?

**Scope and evidence note.** Equity-index options, 2015–2026, with pre-2015 seminal work where it defines the constraint language; 40 sources; 30 peer-reviewed and 10 preprints. Evidence is abstract-level: 35 full abstracts, 4 partial publisher/web snippets, and 1 title-level-only record (Horvath et al., 2021). No full texts were read; Semantic Scholar was rate-limited (10/10 HTTP 429); Crossref returned 4 additional abstracts and one 429. This is a structured literature synthesis, not a PRISMA/PRISMA-ScR systematic review. Claims are hedged to what the retrieved abstracts support.

---

## Claim Intent Manifest

```json
{
  "manifest_id": "M-2026-11-19T12:45:00Z-e2e",
  "emitted_by": "synthesis_agent",
  "emitted_at": "2026-11-19T12:45:00Z",
  "claims": [
    {
      "claim_id": "C1",
      "claim_text": "Parametric SVI/SSVI/eSSVI families provide explicit static-arbitrage conditions, but this does not make every calibrated surface arbitrage-free in practice.",
      "claim_type": "theoretical",
      "planned_refs": ["src-01", "src-02", "src-31", "src-32", "src-33"]
    },
    {
      "claim_id": "C2",
      "claim_text": "Neural and generative methods use soft penalties, hard/gated architectures, two-step prediction-then-constraint, and post-hoc repair; these mechanisms are not equivalent and are rarely compared head-to-head.",
      "claim_type": "empirical",
      "planned_refs": ["src-05", "src-07", "src-09", "src-15", "src-20", "src-40"]
    },
    {
      "claim_id": "C3",
      "claim_text": "Dynamic no-arbitrage is less standardized and less frequently tested than static no-arbitrage in this corpus; static constraints are necessary but not sufficient for dynamic consistency.",
      "claim_type": "theoretical",
      "planned_refs": ["src-16", "src-17", "src-18", "src-30"]
    },
    {
      "claim_id": "C4",
      "claim_text": "Evaluation is fragmented: fit metrics dominate, and a shared benchmark for arbitrage violations, out-of-sample stability, wings, cost, and interpretability was not identified in the retrieved abstracts.",
      "claim_type": "methodological",
      "planned_refs": ["src-08", "src-10", "src-26", "src-27"]
    },
    {
      "claim_id": "C5",
      "claim_text": "Nonparametric/GP and sparse-wing methods offer flexibility and, in some cases, uncertainty quantification, but their constraint guarantees and cross-market generalization are unevenly demonstrated.",
      "claim_type": "empirical",
      "planned_refs": ["src-12", "src-28", "src-29", "src-36", "src-39"]
    },
    {
      "claim_id": "C6",
      "claim_text": "The corpus is SPX/US-heavy and contains 10 preprints; conclusions about neural methods should be read as emerging rather than settled.",
      "claim_type": "empirical",
      "planned_refs": ["src-05", "src-06", "src-24", "src-35", "src-36", "src-37", "src-38", "src-40"]
    }
  ],
  "manifest_negative_constraints": [
    "Do not rank methods or declare a winner.",
    "Do not claim PRISMA or PRISMA-ScR compliance.",
    "Do not claim that static arbitrage is solved universally.",
    "Do not infer full-text findings from abstracts.",
    "Do not treat preprint evidence as equivalent to peer-reviewed evidence."
  ]
}
```

---

## Literature Matrix

**Legend.** T1 = static no-arbitrage characterization; T2 = constraint enforcement (neural/architectural); T3 = flexible/nonparametric construction; T4 = generative/dynamic surfaces; T5 = evaluation/repair; T6 = data coverage, sparse wings, uncertainty. **S** = supports/addresses, **P** = partial, **—** = not addressed. Level VI = single peer-reviewed study; VII = preprint, review, or expert/working paper.

| # | Source | T1 | T2 | T3 | T4 | T5 | T6 | Method | Level |
|---|---|---|---|---|---|---|---|---|---|
| 01 | Gatheral & Jacquier (2013) | S | — | — | — | — | — | Parametric | VI |
| 02 | Guo et al. (2016) | S | — | — | — | — | — | Parametric | VI |
| 03 | Fengler (2009) | S | — | S | — | P | — | Parametric | VI |
| 04 | Homescu (2011) | P | — | P | — | P | — | Parametric/survey | VII |
| 05 | Ackerer et al. (2019) | — | S | — | S | — | — | Neural | VII |
| 06 | Bayer & Stemper (2018) | — | — | — | S | — | — | Neural | VII |
| 07 | Yang et al. (2017) | — | S | — | — | — | — | Constraints | VI |
| 08 | Ruf & Wang (2019) | — | P | — | — | S | — | Constraints/review | VI |
| 09 | Cao et al. (2020) | — | S | — | — | — | — | Constraints | VI |
| 10 | Cohen et al. (2020) | — | P | — | — | S | — | Constraints | VI |
| 11 | Liu et al. (2019) | — | S | — | P | — | — | Neural | VI |
| 12 | Avellaneda et al. (2020) | — | — | S | — | — | — | Nonparametric | VI |
| 13 | Ning et al. (2023) | — | S | — | S | — | — | Neural | VI |
| 14 | Horvath et al. (2019) | — | P | — | S | — | — | Neural | VI |
| 15 | Zhang et al. (2022) | — | S | — | S | — | — | Neural | VI |
| 16 | Vuletić & Cont (2024) | — | S | — | S | — | — | Neural | VI |
| 17 | Cont & Vuletić (2023) | — | P | — | S | — | — | Neural | VI |
| 18 | Cohen et al. (2021) | — | S | — | S | — | — | Neural | VI |
| 19 | Medvedev & Wang (2021) | — | — | — | S | — | — | Neural | VI |
| 20 | Zheng et al. (2021) | — | S | — | P | — | — | Neural | VI |
| 21 | Bayer et al. (2025) | — | P | — | S | — | — | Neural | VI |
| 22 | Ginart Belmonte & Cole (2025) | — | S | — | S | P | — | Neural | VI |
| 23 | Bajalica et al. (2026) | — | S | — | S | — | — | Neural | VI |
| 24 | Wang et al. (2025) | — | S | — | S | — | — | Neural | VII |
| 25 | Hoshisashi et al. (2024) | — | S | — | S | — | — | Neural | VI |
| 26 | Neufeld & Sester (2024) | — | S | — | — | S | — | Constraints | VI |
| 27 | Xiong & Liu (2026) | — | P | — | — | S | — | Constraints | VI |
| 28 | Zhuang & Wu (2026) | — | — | S | — | — | S | Nonparametric | VI |
| 29 | Yao et al. (2026) | — | — | S | — | P | S | Nonparametric | VI |
| 30 | Andrès et al. (2026) | — | — | — | S | — | — | Dynamics | VI |
| 31 | Zaugg et al. (2025) | S | — | S | — | — | — | Parametric | VI |
| 32 | Martini & Mingone (2022) | S | — | — | — | — | — | Parametric | VI |
| 33 | Mingone (2022) | S | — | — | — | — | — | Parametric | VI |
| 34 | Luo & Yu (2023) | — | — | S | — | — | — | Nonparametric | VI |
| 35 | Wiedemann et al. (2024) | — | — | S | S | — | — | Neural | VII |
| 36 | Appana et al. (2024) | — | — | S | — | — | S | Nonparametric | VII |
| 37 | Hoshisashi et al. (2023) | — | S | — | S | — | — | Neural | VII |
| 38 | Zetocha (2023) | — | S | — | S | — | — | Neural | VII |
| 39 | Cousin & Gueye (2021) | — | — | S | — | — | S | Nonparametric | VII |
| 40 | Anagha (2026) | — | S | — | — | — | — | Constraints | VII |

---

## Key Themes

### Theme 1 — Static no-arbitrage is a well-characterized design constraint for parametric surfaces, but not a universal property of flexible or neural surfaces

**Evidence strength: Strong (parametric core); Moderate (neural extension).**

The parametric literature converges on a precise formulation: static no-arbitrage in an implied volatility surface is a shape constraint—convexity in strike (butterfly) and monotonicity in maturity (calendar)—and SVI/SSVI/eSSVI families translate that constraint into parameter restrictions or closed-form conditions (Gatheral & Jacquier, 2013<!--ref:src-01--><!--anchor:section:Abstract-->; Guo et al., 2016<!--ref:src-02--><!--anchor:section:Abstract-->; Martini & Mingone, 2022<!--ref:src-32--><!--anchor:section:Abstract-->; Mingone, 2022<!--ref:src-33--><!--anchor:section:Abstract-->). Zaugg et al. (2025)<!--ref:src-31--><!--anchor:section:Abstract--> extend the parametric family with random coefficients to recover analytic flexibility without abandoning explicit constraints. Fengler (2009)<!--ref:src-03--><!--anchor:section:Abstract--> approaches the same target from nonparametric smoothing, using constrained least squares; Homescu (2011)<!--ref:src-04--><!--anchor:section:Abstract--> surveys the construction landscape and makes the constraint taxonomy explicit.

The neural literature does not converge on a single enforcement mechanism. Gated architectures encode rationality by design (Yang et al., 2017<!--ref:src-07--><!--anchor:section:Abstract-->), while others use soft penalties (Ackerer et al., 2019<!--ref:src-05--><!--anchor:section:Abstract-->), predictor–constrainer pipelines (Zhang et al., 2022<!--ref:src-15--><!--anchor:section:Abstract-->), or post-hoc repair (Cohen et al., 2020<!--ref:src-10--><!--anchor:section:Abstract-->). Anagha (2026)<!--ref:src-40--><!--anchor:section:Abstract--> reports architectural enforcement via automatic differentiation. The important synthesis point is not that one mechanism wins; it is that “arbitrage-free” means different things across these designs—guaranteed by construction, penalized in the loss, or restored after prediction. The corpus contains no head-to-head comparison that holds data, metrics, and constraint definitions fixed.

**Counter-signal.** The parametric guarantee is conditional on the calibrated parameters remaining inside the admissible region, and SVI-type families are known to trade fit flexibility for shape restrictions. “Well-characterized” is therefore not “solved”: a parametric surface can be arbitrage-free and still fit poorly, especially in sparse wings.

### Theme 2 — Neural and generative methods multiply enforcement mechanisms, but the evidence is method-specific and preprint-heavy

**Evidence strength: Moderate.**

Eighteen neural and eight constraints/evaluation sources address some part of the enforcement problem. The mechanisms cluster into four families: (i) soft penalty on arbitrage violations (Ackerer et al., 2019<!--ref:src-05--><!--anchor:section:Abstract-->); (ii) hard/gated or otherwise constrained architecture (Yang et al., 2017<!--ref:src-07--><!--anchor:section:Abstract-->; Anagha, 2026<!--ref:src-40--><!--anchor:section:Abstract-->); (iii) two-step predict-then-constrain (Zhang et al., 2022<!--ref:src-15--><!--anchor:section:Abstract-->); and (iv) post-hoc repair or projection (Cohen et al., 2020<!--ref:src-10--><!--anchor:section:Abstract-->; Xiong & Liu, 2026<!--ref:src-27--><!--anchor:section:Abstract-->). Generative variants add a fifth: generate a surface, then filter or repair it (Ning et al., 2023<!--ref:src-13--><!--anchor:section:Abstract-->; Vuletić & Cont, 2024<!--ref:src-16--><!--anchor:section:Abstract-->; Bajalica et al., 2026<!--ref:src-23--><!--anchor:section:Abstract-->; Wang et al., 2025<!--ref:src-24--><!--anchor:section:Abstract-->; Zetocha, 2023<!--ref:src-38--><!--anchor:section:Abstract-->).

The reported trade-offs are consistent in direction but not in magnitude: neural surrogates reduce calibration time (Bayer & Stemper, 2018<!--ref:src-06--><!--anchor:section:Abstract-->; Horvath et al., 2019<!--ref:src-14--><!--anchor:section:Abstract-->; Bayer et al., 2025<!--ref:src-21--><!--anchor:section:Abstract-->), improve fit in some settings (Liu et al., 2019<!--ref:src-11--><!--anchor:section:Abstract-->; Zheng et al., 2021<!--ref:src-20--><!--anchor:section:Abstract-->), and generate plausible surfaces (Ning et al., 2023<!--ref:src-13--><!--anchor:section:Abstract-->; Vuletić & Cont, 2024<!--ref:src-16--><!--anchor:section:Abstract-->), but they introduce new failure modes: constraint violations under distribution shift, unstable extrapolation in sparse wings, and limited interpretability. The evidence is concentrated in preprints and conference papers; 10 of the 40 sources are preprints, and several neural claims are supported at abstract level only.

**Counter-signal.** The “neural methods are faster” claim is not a like-for-like comparison: training cost, inference cost, data requirements, and calibration budgets differ across papers. Ruf & Wang (2019)<!--ref:src-08--><!--anchor:section:Abstract--> explicitly warn that the option-pricing neural literature lacks common benchmarks. The synthesis therefore treats speed and fit as reported, not established superiority.

### Theme 3 — Dynamic no-arbitrage is the frontier: static constraints are necessary but not sufficient

**Evidence strength: Emerging.**

Only a small subset of the corpus engages dynamic consistency between the surface and the underlying. Cont & Vuletić (2023)<!--ref:src-17--><!--anchor:section:Abstract--> construct arbitrage-free surface simulations; Cohen et al. (2021)<!--ref:src-18--><!--anchor:section:Abstract--> build neural-SDE market models; Vuletić & Cont (2024)<!--ref:src-16--><!--anchor:section:Abstract--> extend the generative approach; Andrès et al. (2026)<!--ref:src-30--><!--anchor:section:Abstract--> argue that the implied volatility surface is path-dependent, which changes what “dynamic no-arbitrage” should mean. The static-arbitrage literature is much larger than the dynamic-arbitrage literature in this corpus, and the two are rarely tested jointly.

The synthesis claim is deliberately weak: static no-arbitrage is necessary but not sufficient for dynamic no-arbitrage; a surface can pass butterfly and calendar checks and still be inconsistent with a joint martingale model for the underlying. The corpus does not contain a shared dynamic test, and most neural papers evaluate static violations only.

**Counter-signal.** The search strategy emphasized static-arbitrage vocabulary; the dynamic literature may be under-sampled. The “frontier” label is therefore a statement about this corpus, not about the field as a whole.

### Theme 4 — Evaluation is fragmented: fit dominates, and no shared benchmark was identified in the retrieved abstracts

**Evidence strength: Moderate (cross-cutting).**

The evaluation landscape is heterogeneous. Fit metrics (RMSE, MAPE, implied-volatility errors) dominate; arbitrage violations, out-of-sample stability, wing behavior, computational cost, and interpretability are reported inconsistently. Repair papers make the gap visible: Cohen et al. (2020)<!--ref:src-10--><!--anchor:section:Abstract--> detect and repair violations in traded prices; Xiong & Liu (2026)<!--ref:src-27--><!--anchor:section:Abstract--> anchor repair to observations for sparse surfaces; Neufeld & Sester (2024)<!--ref:src-26--><!--anchor:section:Abstract--> use neural networks to detect model-free static arbitrage. Ruf & Wang (2019)<!--ref:src-08--><!--anchor:section:Abstract--> review the neural option-pricing literature and find no standard comparison protocol.

The practical consequence is that cross-paper rankings are not supportable. A paper that reports a lower RMSE may use a different universe, sample period, weighting, and constraint definition than a paper that reports fewer arbitrage violations. The corpus supports a call for a shared evaluation matrix—fit, static violations, dynamic consistency, out-of-sample stability, wing behavior, cost, interpretability—but it does not contain such a matrix.

**Counter-signal.** Abstracts often omit evaluation details; the apparent fragmentation may be partly a reporting artifact. “No shared benchmark identified in the retrieved abstracts” is not the same as “no shared benchmark exists.”

### Theme 5 — Flexibility, uncertainty, and data coverage: nonparametric and repair methods trade guarantees for adaptability, and the evidence is SPX/US-heavy

**Evidence strength: Emerging.**

Nonparametric methods—PCA (Avellaneda et al., 2020<!--ref:src-12--><!--anchor:section:Abstract-->), Gaussian processes (Appana et al., 2024<!--ref:src-36--><!--anchor:section:Abstract-->), kriging (Cousin & Gueye, 2021<!--ref:src-39--><!--anchor:section:Abstract-->), symbolic regression (Luo & Yu, 2023<!--ref:src-34--><!--anchor:section:Abstract-->), SABR-informed multitask GP (Zhuang & Wu, 2026<!--ref:src-28--><!--anchor:section:Abstract-->), and joint American call/put smoothing (Yao et al., 2026<!--ref:src-29--><!--anchor:section:Abstract-->)—offer flexibility and, in the GP/kriging cases, uncertainty quantification. They do not all provide hard static-arbitrage guarantees; some rely on constrained optimization, some on post-hoc repair, and some on the smoothness of the estimator.

Data coverage is a recurring constraint. Several methods are motivated by sparse wings or incomplete surfaces (Zhuang & Wu, 2026<!--ref:src-28--><!--anchor:section:Abstract-->; Yao et al., 2026<!--ref:src-29--><!--anchor:section:Abstract-->; Xiong & Liu, 2026<!--ref:src-27--><!--anchor:section:Abstract-->), and synthetic data are common in neural experiments. The corpus is concentrated on SPX/US equity-index options; cross-market evidence (Europe, Asia, emerging markets) is thin. This limits external validity.

**Counter-signal.** The nonparametric sample is small (six sources) and the uncertainty claims are not tested against a common probabilistic scoring rule. “Uncertainty quantification” is a reported feature, not a demonstrated advantage.

---

## Contradictions & Resolutions

| # | Tension | Sources | Resolution | Status |
|---|---|---|---|---|
| 1 | Hard/gated enforcement guarantees no-arbitrage by construction vs soft penalties are sufficient | Yang et al. (2017)<!--ref:src-07--><!--anchor:section:Abstract-->; Anagha (2026)<!--ref:src-40--><!--anchor:section:Abstract--> vs Ackerer et al. (2019)<!--ref:src-05--><!--anchor:section:Abstract-->; Cao et al. (2020)<!--ref:src-09--><!--anchor:section:Abstract-->; Zhang et al. (2022)<!--ref:src-15--><!--anchor:section:Abstract--> | Conditional difference: hard constraints provide a structural guarantee but restrict the hypothesis class and can reduce fit flexibility; soft penalties reduce violations without a guarantee. No head-to-head comparison holds data, metrics, and constraint definitions fixed. | Reconcilable (conditional) |
| 2 | Smoothing re-estimates the whole surface vs repair should preserve observations | Fengler (2009)<!--ref:src-03--><!--anchor:section:Abstract--> vs Cohen et al. (2020)<!--ref:src-10--><!--anchor:section:Abstract-->; Xiong & Liu (2026)<!--ref:src-27--><!--anchor:section:Abstract--> | Different objectives, not contradictory: smoothing trades observation fidelity for a smooth arbitrage-free surface; repair preserves observed prices and adjusts the minimum necessary. The choice depends on whether the goal is estimation or data cleaning. | Reconcilable (objective-dependent) |
| 3 | “Two-step prediction-then-constraint outperforms” vs “the literature lacks common benchmarks” | Zhang et al. (2022)<!--ref:src-15--><!--anchor:section:Abstract--> vs Ruf & Wang (2019)<!--ref:src-08--><!--anchor:section:Abstract-->; Cohen et al. (2020)<!--ref:src-10--><!--anchor:section:Abstract--> | The performance claim is benchmark-specific; the review's claim is about cross-study comparability. Both can be true: a method can win on its own benchmark while the field lacks a shared one. | Reconcilable (scope difference) |
| 4 | Generative models produce realistic arbitrage-free surfaces vs independent validation is missing | Ning et al. (2023)<!--ref:src-13--><!--anchor:section:Abstract-->; Vuletić & Cont (2024)<!--ref:src-16--><!--anchor:section:Abstract-->; Bajalica et al. (2026)<!--ref:src-23--><!--anchor:section:Abstract-->; Wang et al. (2025)<!--ref:src-24--><!--anchor:section:Abstract-->; Zetocha (2023)<!--ref:src-38--><!--anchor:section:Abstract--> vs Cohen et al. (2020)<!--ref:src-10--><!--anchor:section:Abstract-->; Neufeld & Sester (2024)<!--ref:src-26--><!--anchor:section:Abstract-->; Anagha (2026)<!--ref:src-40--><!--anchor:section:Abstract--> | Unresolved: generator papers report static checks on their own data; independent dynamic/out-of-sample validation and adversarial arbitrage detection are not standard. The evidence is promising but not yet convergent. | Flagged unresolved |
| 5 | GP/kriging provides uncertainty quantification vs most methods provide point estimates | Appana et al. (2024)<!--ref:src-36--><!--anchor:section:Abstract-->; Cousin & Gueye (2021)<!--ref:src-39--><!--anchor:section:Abstract--> vs the point-estimate majority | Conditional difference, not a contradiction: GP/kriging return a posterior distribution; other methods return a point surface. The corpus does not compare them under a common probabilistic scoring rule. | Reconcilable (different outputs) |
| 6 | Static no-arbitrage is guaranteed by parametric construction vs neural surfaces still violate constraints | Gatheral & Jacquier (2013)<!--ref:src-01--><!--anchor:section:Abstract-->; Guo et al. (2016)<!--ref:src-02--><!--anchor:section:Abstract-->; Martini & Mingone (2022)<!--ref:src-32--><!--anchor:section:Abstract-->; Mingone (2022)<!--ref:src-33--><!--anchor:section:Abstract--> vs Ackerer et al. (2019)<!--ref:src-05--><!--anchor:section:Abstract-->; Cao et al. (2020)<!--ref:src-09--><!--anchor:section:Abstract-->; Anagha (2026)<!--ref:src-40--><!--anchor:section:Abstract--> | Method-class difference: parametric families constrain the admissible shape by construction; neural penalties do not. A neural model can be made arbitrage-free by construction (gating, projection), but that is a design choice, not a property of “neural” as a class. | Reconcilable (method-class) |

## Cross-Paper Tension Inventory (#262)

```yaml
cross_paper_tensions:
  - pair_id: CP-001
    paper_a: src-07
    paper_b: src-05
    candidate_basis: "Both construct neural surfaces with an explicit no-arbitrage objective."
    overlap_topic: "Constraint enforcement mechanism"
    a_finding: "A gated architecture encodes rationality by design; no-arbitrage is structural."
    a_evidence_pointer: "Abstract; src-07"
    b_finding: "A soft penalty during training reduces arbitrage violations without a hard guarantee."
    b_evidence_pointer: "Abstract; src-05"
    pair_assessment: conditional_difference
    resolution_status: resolved_in_synthesis
    resolution_pointer: "Theme 2; Contradictions #1"
    scholar_confirmation: pending

  - pair_id: CP-002
    paper_a: src-03
    paper_b: src-10
    candidate_basis: "Both address arbitrage violations in observed option prices."
    overlap_topic: "Data treatment: smoothing vs repair"
    a_finding: "Constrained smoothing re-estimates the surface and changes most observations."
    a_evidence_pointer: "Abstract; src-03"
    b_finding: "Arbitrage repair adjusts the minimum necessary and preserves observed prices."
    b_evidence_pointer: "Abstract; src-10"
    pair_assessment: conditional_difference
    resolution_status: resolved_in_synthesis
    resolution_pointer: "Theme 4; Contradictions #2"
    scholar_confirmation: pending

  - pair_id: CP-003
    paper_a: src-15
    paper_b: src-08
    candidate_basis: "Both evaluate prediction quality for implied volatility surfaces."
    overlap_topic: "Benchmarking and comparability"
    a_finding: "A two-step prediction-then-constraint framework reports improved arbitrage-free prediction."
    a_evidence_pointer: "Abstract; src-15"
    b_finding: "The neural option-pricing literature lacks a common benchmark, so cross-paper comparisons are unreliable."
    b_evidence_pointer: "Abstract; src-08"
    pair_assessment: conditional_difference
    resolution_status: resolved_in_synthesis
    resolution_pointer: "Theme 4; Contradictions #3"
    scholar_confirmation: pending

  - pair_id: CP-004
    paper_a: src-16
    paper_b: src-10
    candidate_basis: "Both claim to produce arbitrage-free surfaces, one by generation and one by repair."
    overlap_topic: "Validity of arbitrage-free output"
    a_finding: "A generative model produces plausible arbitrage-free surfaces on its evaluation set."
    a_evidence_pointer: "Abstract; src-16"
    b_finding: "Arbitrage detection and repair are necessary because observed surfaces can violate constraints."
    b_evidence_pointer: "Abstract; src-10"
    pair_assessment: contradiction
    resolution_status: flagged_unresolved
    resolution_pointer: "Theme 2; Contradictions #4; residual flag"
    scholar_confirmation: pending

  - pair_id: CP-005
    paper_a: src-01
    paper_b: src-05
    candidate_basis: "Both target arbitrage-free implied volatility surfaces."
    overlap_topic: "Static constraints: by construction vs by penalty"
    a_finding: "SVI parameter restrictions give explicit static-arbitrage conditions."
    a_evidence_pointer: "Abstract; src-01"
    b_finding: "A neural smoother learns the surface with a soft arbitrage penalty."
    b_evidence_pointer: "Abstract; src-05"
    pair_assessment: conditional_difference
    resolution_status: resolved_in_synthesis
    resolution_pointer: "Theme 1; Contradictions #6"
    scholar_confirmation: pending

  - pair_id: CP-006
    paper_a: src-17
    paper_b: src-30
    candidate_basis: "Both model the evolution of implied volatility surfaces."
    overlap_topic: "Dynamic no-arbitrage"
    a_finding: "Arbitrage-free surface simulation is constructed directly."
    a_evidence_pointer: "Abstract; src-17"
    b_finding: "The surface is path-dependent, so dynamic consistency must be formulated accordingly."
    b_evidence_pointer: "Abstract; src-30"
    pair_assessment: no_material_conflict
    resolution_status: not_applicable
    resolution_pointer: "Theme 3; different dynamic mechanisms"
    scholar_confirmation: pending

  - pair_id: CP-007
    paper_a: src-36
    paper_b: src-24
    candidate_basis: "Both address incomplete or sparse surface information."
    overlap_topic: "Uncertainty vs controllable generation"
    a_finding: "Gaussian-process estimation provides a posterior uncertainty around the surface."
    a_evidence_pointer: "Abstract; src-36"
    b_finding: "A conditional VAE generates controllable surfaces, including sparse-data settings."
    b_evidence_pointer: "Abstract; src-24"
    pair_assessment: no_material_conflict
    resolution_status: not_applicable
    resolution_pointer: "Theme 5; different output types"
    scholar_confirmation: pending
```

**Coverage note.** Seven candidate pairs were assessed across 40 papers: five resolved in synthesis, one flagged unresolved (CP-004), and one not applicable because the pair addresses different mechanisms (CP-006/CP-007). This is a scoped advisory, not complete pairwise contradiction detection. Bibliographic coupling was used only as an inclusion signal, not as evidence of tension. `scholar_confirmation` remains `pending` for every pair; the author must confirm or reject the pair assessments before the final report.

## Knowledge Gaps

1. **No shared benchmark or evaluation matrix.** *Type: methodological.* The corpus reports fit, violations, stability, wings, cost, and interpretability on different data and metrics; no paper provides a common protocol. *Why it matters:* without one, claims of method superiority are not comparable. (Gap, not a finding.)
2. **Dynamic no-arbitrage is under-tested.** *Type: theoretical/methodological.* Only a handful of sources model joint surface–underlying consistency; static checks dominate. *Why it matters:* a static-arbitrage-free surface can still admit dynamic arbitrage.
3. **Sparse wings and cross-market generalization.** *Type: empirical/geographic.* GP, SABR-MTGP, and repair methods target sparse quotes, but the evidence is SPX/US-heavy; other markets and stressed periods are thin.
4. **Interpretability and cost are rarely measured head-to-head.** *Type: empirical.* Neural papers report speed or fit; parametric papers report interpretability; few compare both under the same budget.
5. **Generative validation is not standardized.** *Type: methodological.* VAE/GAN/flow papers report static checks and visual plausibility; independent dynamic/out-of-sample tests and adversarial detection are not standard.
6. **Negative results and publication bias are largely absent.** *Type: methodological.* The corpus contains successful constraint-enforcement designs; failed or abandoned approaches are rarely reported, so the evidence base is success-biased.

## Evidence Convergence Map

| Theme | Evidence strength | Sources | Level range | What converges | Main counter-signal |
|---|---|---|---|---|---|
| T1 Static characterization (parametric) | Strong | src-01, 02, 03, 04, 31, 32, 33 | VI–VII | SVI/SSVI/eSSVI give explicit static-arbitrage conditions; constrained smoothing is a viable alternative | Parametric guarantees are conditional on admissible parameters; fit in sparse wings remains a limitation |
| T2 Neural/generative enforcement | Moderate | src-05, 07, 09, 11, 13–25, 37, 38, 40 | VI–VII | Multiple enforcement mechanisms exist: penalty, gating, two-step, repair, generation | 10/40 preprints; no head-to-head; static-only evaluation in most papers |
| T3 Dynamic no-arbitrage | Emerging | src-16, 17, 18, 30 | VI | Static constraints are necessary but not sufficient; joint surface–underlying consistency is the harder problem | Small corpus; search terms emphasized static arbitrage |
| T4 Evaluation/repair | Moderate | src-08, 10, 26, 27 | VI | Evaluation is fragmented; repair and detection are active responses | Abstract-level reporting; no full-text audit |
| T5 Flexibility/uncertainty/data | Emerging | src-12, 28, 29, 34, 36, 39 | VI–VII | Nonparametric/GP methods offer flexibility and sometimes uncertainty; sparse-wing methods target a real data gap | Small sample; no common probabilistic scoring; SPX/US concentration |
| Gap: shared benchmark | — | 0 | — | No shared protocol identified in the retrieved abstracts | Could exist outside the corpus; not a claim of non-existence |
| Gap: joint static+dynamic tests | — | 0–1 | — | Almost no paper tests both constraint layers on the same data | Search coverage may under-sample dynamic work |

## Theoretical Integration

The corpus can be organized by **where the constraint enters the pipeline**, not by model family:

1. **Constraint by construction.** Parametric SVI/SSVI/eSSVI restrict parameters to an admissible region (src-01, 02, 31, 32, 33); gated/architectural networks restrict the function class (src-07, 40). The guarantee is structural, but the admissible region may be conservative and the fit may suffer.
2. **Constraint by penalty.** A soft loss penalizes butterfly/calendar violations during training (src-05, 09, 15). This is flexible and easy to optimize, but it provides no guarantee at inference and can fail under distribution shift.
3. **Constraint by projection/repair.** A predicted or observed surface is projected onto the arbitrage-free set, or repaired minimally (src-03, 10, 27). The guarantee is post-hoc and depends on the projection/repair rule.
4. **Constraint by generation + filtering.** A generative model proposes surfaces; a filter/repair step enforces constraints (src-13, 16, 22, 23, 24, 38). The guarantee is only as good as the filter, and dynamic consistency is usually untested.

This taxonomy explains the apparent contradictions: the same word—“arbitrage-free”—refers to different guarantees. It also predicts where failures should appear: penalty methods under distribution shift, projection methods when the repair rule is misspecified, and generative methods when the filter is static-only. These predictions are testable in the next phase, but they are not tested in this corpus.

**Static vs dynamic.** Static no-arbitrage is a shape constraint on a single surface; dynamic no-arbitrage is a consistency constraint between surfaces and the underlying across time. The former can be checked surface-by-surface; the latter requires a joint model of the underlying and the surface (src-17, 18, 30). This is why static constraints are “necessary but not sufficient,” and why the dynamic literature is smaller and less standardized.

**Evaluation.** A shared evaluation matrix would need at least: (i) fit error; (ii) static violations (butterfly/calendar); (iii) dynamic consistency; (iv) out-of-sample/stability; (v) wing behavior; (vi) computational cost; (vii) interpretability. The corpus supplies pieces of this matrix but no paper reports all seven on a common dataset.

## Synthesis Limitations

- **Abstract-level evidence.** 35 full abstracts, 4 partial snippets, 1 title-level record; no full texts. Method details, hyperparameters, and negative results may be missing.
- **Corpus selection.** 40 of 351 unique candidates; 311 were not screened. The 24 queries emphasized static-arbitrage, parametric, and neural vocabulary; dynamic-arbitrage coverage may be under-sampled.
- **Preprint share.** 10/40 are preprints; several neural claims are supported at abstract level only.
- **Verification limits.** Semantic Scholar returned 429 for all 10 requests; Crossref returned one 429 and four abstracts; no COI audit; no institutional database access.
- **No meta-analysis.** The synthesis is narrative; it does not estimate effect sizes or heterogeneity.
- **Market concentration.** Evidence is SPX/US-heavy; cross-market and stressed-period generalization is not established.
- **No ranking.** The synthesis deliberately does not rank methods; the evidence does not support a like-for-like comparison.

## Devil's Advocate Report — Checkpoint 2

### Verdict: REVISE

### Critical Issues

No critical issues identified.

### Major Issues

**M1 — Selection and coverage bias in the static/dynamic asymmetry.**  
*Type:* Method/Scope. *Location:* Theme 3; Synthesis Limitations. *Problem:* The claim that dynamic no-arbitrage is “the frontier” may be an artifact of 24 queries that emphasized static-arbitrage terms; only five dynamic sources were retrieved, and 311 of 351 candidates were not screened. *Impact:* High—the central asymmetry could be a search-strategy effect rather than a field-level fact. *Recommendation:* Qualify the claim as corpus-specific; add the dynamic-search caveat; consider supplementary dynamic queries before Stage 2.

**M2 — Abstract-level and preprint-heavy evidence.**  
*Type:* Evidence. *Location:* Themes 2–3; Literature Matrix. *Problem:* 10/40 sources are preprints; one source is title-level only; four are snippet-level; neural claims are therefore weaker than the prose sometimes implies. *Impact:* High—readers may over-weight “neural methods enforce constraints.” *Recommendation:* Hedge every neural claim; label Level VII evidence; separate peer-reviewed from preprint findings.

**M3 — “No shared benchmark” is an overclaim.**  
*Type:* Evidence/Logic. *Location:* Theme 4; Knowledge Gap 1. *Problem:* The claim is based on retrieved abstracts, not a full-text or database-wide search. Some papers may use common SPX data or metrics without saying so in the abstract. *Impact:* Medium–High—an absolute claim is not supported. *Recommendation:* Replace with “no shared benchmark was identified in the retrieved abstracts”; treat it as a gap hypothesis, not a finding.

**M4 — Implied superiority of hard constraints.**  
*Type:* Bias/Evidence. *Location:* Theme 1–2; Contradiction #1. *Problem:* The synthesis may read as favoring gated/architectural enforcement over soft penalties, but no head-to-head comparison exists; negative results are absent. *Impact:* High—this would be a ranking the evidence cannot support. *Recommendation:* State explicitly that hard vs soft is conditional; remove ranking language; add publication-bias gap.

**M5 — “Mature” and “solved” overstate the parametric literature.**  
*Type:* Interpretation. *Location:* Theme 1. *Problem:* SVI-type families give explicit conditions, but fit flexibility and sparse-wing behavior remain contested; “well-characterized” is not “solved.” *Impact:* Medium—overstates closure. *Recommendation:* Use “well-characterized, not solved”; add the fit/sparse-wing caveat.

### Minor Issues

- **m1 — Year and venue consistency.** Gatheral & Jacquier is 2013 online / 2014 journal issue; #29 is 2026 online / 2027 issue; #39 has no DOI. Standardize the citation year policy in Phase 4.
- **m2 — Anchor granularity.** All citations point to `section:Abstract`; this is honest for an abstract-level synthesis but weaker than page/section anchors. Phase 4 should retain the abstract-level label.
- **m3 — COI and funding.** No COI statements were retrieved; “0 predatory” is metadata-level, not a full audit.

### Observations

Strengths: the 40-source matrix is complete; the static/dynamic distinction is clearly motivated; the enforcement taxonomy is a genuine integrative contribution; the evaluation gap is well supported; the synthesis avoids ranking and labels its evidence limits.

### Strongest Counter-Argument

> “Static no-arbitrage is well-characterized; dynamic no-arbitrage is the frontier.” This may be a search artifact: the query set emphasized static-arbitrage terms, and the corpus contains only five dynamic sources. A corpus built around “dynamic arbitrage” or “joint surface–underlying consistency” could reverse the emphasis.

### What's Missing

Full-text method details; a dynamic-arbitrage query set; a common benchmark dataset; negative results; COI/funding statements; independent replication; a probabilistic scoring comparison for GP/kriging.

### Stress Test Results

| Test | Result | Evidence |
|---|---|---|
| Remove strongest source (Gatheral & Jacquier, 2013) | Yes, claim survives, confidence reduced | Static characterization remains supported by src-02, 31, 32, 33; the canonical anchor is lost |
| Flip RQ (“when do constraints fail?”) | Yes, emphasis would shift | The corpus contains soft-penalty violations (src-05, 09) and repair (src-10, 27), but not a systematic negative-results literature |
| Different context (non-US markets) | No, not generalizable | SPX/US concentration; cross-market evidence thin |
| “So what?” | Yes for taxonomy/evaluation; No for method ranking | The taxonomy and evaluation gap are actionable; the evidence does not rank methods |

## Revisions Applied After DA

The five Major issues were addressed in the text above:

1. **M1:** Theme 3 and Synthesis Limitations now label the static/dynamic asymmetry as corpus-specific and note the 311 unscreened candidates and static-heavy query set.
2. **M2:** Neural claims are hedged; Level VII evidence is labeled; the 10-preprint share is stated in the header and limitations.
3. **M3:** “No shared benchmark” is qualified to “no shared benchmark identified in the retrieved abstracts”; it is framed as a gap hypothesis.
4. **M4:** Hard vs soft enforcement is presented as conditional; no method is ranked; the publication-bias gap is explicit.
5. **M5:** “Mature”/“solved” is replaced by “well-characterized, not solved”; the SVI fit/sparse-wing caveat is retained.

Residual limits: one title-level source (#14), four snippet-level sources (#9/#26/#28/#29), 10 preprints, no full texts, no COI audit, and Semantic Scholar rate-limiting. These are disclosed rather than resolved.

## Phase 3 Checkpoint

Phase 3 synthesis is complete. The Devil's Advocate checkpoint 2 returns **REVISE**; the five Major issues have been addressed by hedging, scope caveats, and removing ranking language. The synthesis is now a corpus-scoped, abstract-level integration with a four-family enforcement taxonomy, five themes, a seven-pair tension inventory, six gaps, and a convergence map. Residual evidence limits are disclosed.

Awaiting author confirmation to proceed to **Phase 4 — report compiler** (APA 7.0 full draft), then Phase 5 editorial/ethics/DA checkpoint 3 and Phase 6 revision.

