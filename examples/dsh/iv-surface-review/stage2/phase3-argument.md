# Phase 3 — Argument Blueprint

## Thesis

“Arbitrage-free” is not a single property. It names a family of guarantees, and the useful question is which mechanism carries the guarantee — construction, penalty, projection/repair, or generation plus filtering — under which static/dynamic test and with which evidence. A corpus-scoped map of those commitments is more useful than a method ranking.

## Claims and evidence

| # | Claim | Evidence | Status |
|---|---|---|---|
| C1 | Parametric SVI/SSVI/eSSVI provide explicit static-arbitrage conditions; the guarantee is conditional on the admissible parameter region. | Gatheral & Jacquier (2014); Guo et al. (2016); Martini & Mingone (2022); Mingone (2022); Zaugg et al. (2025) | Strong, abstract-level |
| C2 | Nonparametric/GP/spline methods trade a uniform guarantee for flexibility and, in GP/kriging cases, uncertainty. | Fengler (2009); Avellaneda et al. (2020); Appana et al. (2024); Cousin & Gueye (2021); Zhuang & Wu (2026); Yao et al. (2026) | Moderate, abstract-level |
| C3 | Neural/generative methods multiply enforcement mechanisms (hard architecture, soft penalty, two-step projection, generation + filter) and are rarely tested dynamically. | Yang et al. (2017); Ackerer et al. (2019); Cohen et al. (2020); Ning et al. (2023); Vuletić & Cont (2025); 18 neural/generative sources | Moderate; 10 preprints |
| C4 | Dynamic no-arbitrage is a separate, under-tested layer; static admissibility is necessary but not sufficient. | Cont & Vuletić (2023); Cohen et al. (2023); Andrès et al. (2026); Vuletić & Cont (2025) | Emerging; corpus under-sampled |
| C5 | Evaluation is fragmented; no shared benchmark was identified in the retrieved abstracts. | Ruf & Wang (2020); Cohen et al. (2020); Neufeld & Sester (2024); Xiong & Liu (2026); Table 3 | Strong for the corpus; not a global claim |
| C6 | The four-family taxonomy and seven-dimension matrix are interpretive proposals, not validated instruments. | Synthesis; DA checkpoints 1–3 | Scope condition |

## Contribution

1. A guarantee-based taxonomy that cuts across method families.
2. A static/dynamic separation that treats dynamic consistency as a distinct layer.
3. A seven-dimension evaluation matrix and a corpus-scoped evidence map.
4. A research agenda with six testable directions.

The contribution is deliberately a map, not a theory, estimator, or benchmark. The paper says so in §1.5, §5.4, §5.5, and §6.

## Counterarguments and responses

| Counterargument | Response | Where |
|---|---|---|
| The taxonomy is post hoc and unfalsifiable. | It is interpretive, and the paper says so; its value is diagnostic, not causal. The propositions in §5.2 are testable. | §2.6, §5.2 |
| The corpus is too small/abstract-level to support the claims. | The claims are corpus-scoped and hedged; the 40/351 selection and abstract-level evidence are disclosed. | §3.7, §5.4 |
| “No shared benchmark” is an overclaim. | Qualified to “identified in the retrieved abstracts”; no global absence claim. | §4.5, §5.3 |
| Hard constraints are not shown to be superior. | The paper explicitly avoids ranking; hard/soft/projection are different commitments with different failure modes. | §4.3, §5.1, §5.3 |
| The paper is a survey, not a contribution. | The contribution is the cross-family guarantee map, the static/dynamic separation, and the evaluation matrix; the paper states this modest scope. | §1.5, §6 |

## Reader takeaway

Choose the guarantee before choosing the model. Report the guarantee family, the static and dynamic tests, and the evaluation dimensions. Do not read the corpus as a ranking.
