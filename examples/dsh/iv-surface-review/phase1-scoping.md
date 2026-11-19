# Phase 1 — Scoping and Methodology

**Status:** Phase 1 confirmed by the author on 2026-11-19. Review-form note: the author's reply “确认” kept the current work; no separate review form was selected. Current mode continues: `deep-research` full, structured literature review; no PRISMA/PRISMA-ScR claim.
**Run:** DSH ARS e2e, 2026-11-19. Plugin 0.3.0; ARS v3.24.2 (upstream pin `6d93886`); profile `desktop`.
**Artifacts:** `examples/dsh/iv-surface-review/`.

## 0. Confirmation Record

- Phase 1 RQ Brief and Methodology: confirmed by the author, 2026-11-19. Exact reply: “确认”.
- Review-form note: the author did not name a review form; the reply kept the current work. Recorded as the “skip / continue current work” path in § Review-form note. No PRISMA or PRISMA-ScR claim is made.
- Phase 2 is authorized to start.

## 1. Research Question Brief

### Topic Area

Arbitrage-free implied volatility surface (IVS) construction for equity-index options, 2015–2026, across parametric, nonparametric, and neural approaches.

### Primary Research Question

How do parametric, nonparametric, and neural methods for constructing equity-index implied volatility surfaces enforce static and dynamic no-arbitrage constraints?

### FINER Assessment

| Criterion | Score (1–5) | Justification |
|---|---:|---|
| Feasible | 4 | 30–50 public sources are available; no proprietary data are required; full texts are mostly accessible. Some methods lack code or data, but reported constraints can still be compared. |
| Interesting | 4 | No-arbitrage is a central theoretical and model-risk issue; the comparison across parametric, nonparametric, and neural families is contested in both theory and practice. |
| Novel | 3 | IVS surveys exist, but a constraint-centered, cross-family synthesis for 2015–2026 that separates proof, numerical test, and assumption is incremental rather than wholly new. |
| Ethical | 5 | No human subjects; public literature; no financial advice; standard AI-use and citation-integrity disclosures apply. |
| Relevant | 4 | Informs model risk, pricing, risk management, and regulatory use of arbitrage-free surfaces. |

**Average:** 4.0/5. No criterion is below 2.

### Scope Boundaries

| Axis | In scope | Out of scope |
|---|---|---|
| Domain | Mathematical finance; derivatives pricing; volatility modeling; static and dynamic no-arbitrage | Interest-rate, credit, commodity, FX, and crypto surfaces unless directly transferable; exotic pricing; variance swaps; pure IV forecasting; high-frequency microstructure |
| Timeframe | 2015–2026 | Pre-2015 work except seminal background explicitly identified as such |
| Geography | Global equity-index options (e.g., SPX, SX5E, FTSE 100, NKY); English-language literature | Non-English literature; single-market regulatory descriptions without method content |
| Population | Equity-index option implied volatility surfaces (not human subjects) | Single-stock, FX, commodity, and crypto surfaces; surfaces without an equity-index application |

**Key assumptions:** published methods report enough detail to compare; no-arbitrage definitions can be standardized for coding; reported performance metrics are not directly comparable across datasets; publication bias exists.

### Sub-questions

1. Which static no-arbitrage conditions (butterfly/vertical and calendar) are enforced, and by what mechanism (parameterization, constrained optimization, penalty, post-processing)?
2. Which dynamic no-arbitrage conditions (consistent evolution, absence of calendar arbitrage across time, model-implied dynamics) are enforced, and what evidence (proof, numerical test, simulation) supports them?
3. What trade-offs are reported across fit accuracy, surface stability, extrapolation, computational cost, and interpretability?

The primary question is deliberately narrower than the original compound wording. The trade-off question is retained as sub-question 3, so the original scope is preserved while the primary question remains a single answerable question.

### Sub-question Bindings

| Sub-question | Domain | Timeframe | Geography | Population | Deviation |
|---|---|---|---|---|---|
| 1 | Mathematical finance / volatility | 2015–2026 | Global equity-index options | Equity-index IVS | None |
| 2 | Mathematical finance / volatility | 2015–2026 | Global equity-index options | Equity-index IVS | None |
| 3 | Mathematical finance / volatility | 2015–2026 | Global equity-index options | Equity-index IVS | None |

### Candidate Questions Considered

| # | Candidate | FINER average | Decision |
|---|---|---:|---|
| 1 | How do the three method families enforce static and dynamic no-arbitrage constraints, and what trade-offs are reported? | 4.0 | Selected |
| 2 | Do neural IVS methods outperform parametric methods out-of-sample? | 3.4 | Not selected: an empirical horse-race, data-dependent, and not constraint-centered |
| 3 | How do accounting and regulatory standards define an arbitrage-free surface? | 3.2 | Not selected: policy scope; too narrow for a method review |

## 2. Methodology Blueprint

**Status:** provisional until the author chooses a review form. The review-form choice changes the protocol and reporting checklist, not the RQ or scope.

### Research Paradigm

**Pragmatist, with positivist elements for reported numerical evidence.** The review evaluates methods against the practical goal of producing an arbitrage-free surface. Reported numerical results are treated as observable evidence, not as proof of arbitrage-freeness. The synthesis itself is interpretive.

### Method

**Type:** mixed-methods evidence synthesis.

**Specific method:** structured literature review with a comparative, constraint-centered design. It combines qualitative coding of enforcement mechanisms with quantitative extraction of reported performance metrics. No original empirical estimation and no meta-analysis are planned, because datasets, maturities, metrics, and out-of-sample protocols are heterogeneous.

**Justification:** the RQ asks how methods enforce constraints and what trade-offs they report. A structured comparative synthesis fits that question. An empirical horse-race would require a different RQ and proprietary or reconstructed data.

### Data Strategy

**Data type:** secondary.

**Sources:** Scopus, Web of Science, SSRN, arXiv (q-fin), RePEc, Google Scholar; publisher and author pages; backward and forward snowballing from seminal papers.

**Search string (starting point, to be logged and refined):**

```text
("implied volatility surface" OR "volatility surface" OR "IVS")
AND ("no-arbitrage" OR "arbitrage-free" OR "static arbitrage" OR "calendar arbitrage")
AND ("parametric" OR "SVI" OR "SSVI" OR "eSSVI" OR "nonparametric" OR "neural" OR "deep learning" OR "PINN")
```

**Inclusion criteria:** equity-index options; construction or fitting of an IVS; explicit treatment of static or dynamic no-arbitrage; method description and at least one evaluation dimension; English; 2015–2026; peer-reviewed article or high-quality working paper/preprint; full text available.

**Exclusion criteria:** pure option-pricing papers without surface construction; pure forecasting or trading studies; high-frequency microstructure; exotic pricing without surface construction; surfaces outside equity indices unless directly transferable; no-arbitrage not addressed; non-English; predatory venues; duplicate reports.

**Sampling:** 30–50 core sources, selected exhaustively within the stated scope rather than by convenience. Seminal pre-2015 work may be cited as background but is not counted as core evidence.

### Analytical Framework

1. **Taxonomy:** parametric, nonparametric, and neural families; static versus dynamic constraints.
2. **Constraint matrix:** condition, formal definition, enforcement mechanism, evidence status (proof / numerical test / assumption), reported violations, and limitations.
3. **Evaluation matrix:** fit accuracy, stability, extrapolation, computational cost, interpretability; metric, dataset, sample period, result, and a comparability flag.
4. **Evidence grading:** peer-reviewed versus preprint; citation impact; code/data availability; reproducibility; risk of bias.
5. **Thematic synthesis:** convergence and divergence across families; mechanisms that recur; conditions under which claims hold.
6. **Gap analysis:** underexplored constraints, missing comparisons, and open problems.

No league table and no vote-counting. The review will report ranges and conditions, not a single winner.

### Validity Criteria

| Criterion | Strategy |
|---|---|
| Coverage | Reproducible search strings; inclusion/exclusion log; snowballing; 30–50 core sources |
| Source quality | Peer-reviewed priority; explicit grading of preprints; verification of cited claims |
| Triangulation | Multiple sources per claim; contradictions reported rather than smoothed |
| Reflexivity | Assumptions stated; devil's-advocate checkpoint; no claim of neutral ranking |
| Reproducibility | Search log, extraction table, coding scheme, and source list retained in the e2e artifacts |

### Limitations

English-language bias; publication bias; heterogeneous metrics and datasets; no original empirical validation; fast-moving neural literature; preprint quality; no proprietary data; the review can assess reported enforcement, not prove arbitrage-freeness.

### Ethical Considerations

No human subjects. Standard AI-use disclosure and citation-integrity checks apply. No financial advice is given. No dual-use concern beyond general financial research.

### Reporting Standard

The choice follows the author's review-form decision:

- **Systematic review:** PRISMA 2020; PROSPERO registration strongly recommended; dual screening where possible.
- **Scoping review:** PRISMA-ScR; protocol and checklist remain with the author because ARS has no separate scoping mode.
- **Narrative or integrative review:** documented search and selection; SANRA may be used as an optional appraisal guide; no PRISMA claim.
- **Rapid review:** report the shortened steps and their implications.
- **No formal review:** no coverage claim.

### Preregistration

- Systematic review: PROSPERO strongly recommended.
- Otherwise: not required; an OSF preregistration is optional.

### Human Subjects

None.

## 3. Devil's Advocate — Checkpoint 1

**Verdict: PASS.** No Critical issue. Three Major issues must be carried into the Phase 2 protocol.

### Critical

None.

### Major

1. **Operationalizing “no-arbitrage.”** Static and dynamic conditions are defined differently across papers; some prove them, some test them numerically, and some assume them. Without a coding scheme and an evidence-status field, the review would compare unlike claims. *Required action:* define the constraint taxonomy and the proof / numerical-test / assumption coding before extraction; do not label a method “arbitrage-free” when the evidence is only numerical.
2. **Comparability.** Datasets, maturities, error metrics, and out-of-sample protocols differ. A ranking would be invalid. *Required action:* use an evidence table with comparability flags; report ranges and conditions; no league table.
3. **Selection and publication bias.** Neural and preprint literature is growing quickly; classical benchmarks may be undercited, and negative results are rarely published. *Required action:* include classical benchmarks, grade sources, search both peer-reviewed and preprint literature, and document exclusions.

### Minor

- The 2015 cutoff excludes seminal SVI/SSVI work; include it as background, not as core evidence.
- The equity-index scope excludes single-stock evidence; justify the boundary or admit directly transferable evidence.
- The title “Arbitrage-Free … Construction” could overclaim; the review catalogs enforcement and evidence, not a new construction.

### Strongest Counter-argument

“A literature review cannot establish arbitrage-freeness. Reported constraints may be necessary but not sufficient, and numerical tests are not proofs. The review may catalog claims without validating them.”

**Response:** the review's claim is about reported enforcement and evidence status, not about proving arbitrage-freeness. It will distinguish proof, numerical test, and assumption, and will state that distinction in the paper's claims.

### What Is Missing

Dynamic no-arbitrage is often model-specific. The review must distinguish surface-level static arbitrage from dynamic model consistency, and must check whether papers test both.

### Stress Tests

- **Remove the strongest source:** the synthesis should still hold through multiple sources; testable in Phase 3.
- **Flip the RQ:** unconstrained fits may be more stable; the review must report this counter-evidence rather than assume constraints always improve practice.
- **Different context:** single-stock surfaces are out of scope; note the boundary and any transferable evidence.
- **So what:** the practical stakes are model risk, pricing, and regulatory use of surfaces; the paper must state them.

## 4. Review-form Note (#921)

> **Before the review starts: which form of literature review?**
> ARS does not choose this for you. There is no default and no recommendation, and the order below is not a ranking.
>
> - **Systematic review**: answers a focused question with a search and screening plan fixed in advance, with two people screening independently where possible. Months to more than a year for a team of several people, often with a registered protocol. In ARS: `systematic-review` mode.
> - **Scoping review**: maps what has been studied on a topic, the main concepts, and the gaps, using a systematic approach. The work grows with the breadth of the topic. ARS has no separate mode for it.
> - **Narrative or integrative review**: builds an argument or a framework from the literature. In a narrative review the author chooses the sources; an integrative review documents its search and evaluation and can combine different study designs. The work depends on the scope the author sets. In ARS: `lit-review` mode.
> - **Rapid review**: a systematic review with some steps shortened or left out to deliver sooner, typically within weeks to a few months. ARS has no separate mode for it.
> - **No formal review**: background from the sources at hand, for example for an introduction. It does not claim to cover the literature.
>
> Reply with the form you want, or reply "skip" to continue as you are. Either reply is your decision, and this note will not appear again in this project.

## 5. Phase 1 Checkpoint

Please confirm or revise the RQ Brief and Methodology Blueprint, and reply with the review form you want (systematic / scoping / narrative or integrative / rapid / no formal / skip). Phase 2 will not start until you reply.
