# Phase 1 — Scoping and Methodology: Arbitrage-Free Implied Volatility Surfaces

**Run:** DSH ARS end-to-end validation, Stage 1 (`deep-research`, `full` mode), Phase 1 (SCOPING), 2026-11-23; workspace `examples/dsh/iv-surface-review-v047/`; topic: arbitrage-free implied volatility surface construction for equity-index options, 2015–2026.  
**Instruction source:** vendored ARS v3.24.4 files read directly from this fork (`skills/deep-research/SKILL.md`, the three Phase 1 agent files, and the two references named in §2); the installed 0.4.6 plugin text was not followed.  
**Status:** Phase 1 complete; Devil's Advocate verdict **PASS**; three Major fixes carried into Phase 2. **No literature was searched or cited in this phase** — model and search-string names below are domain vocabulary, not references.

## 1. Research Question Brief

### Topic Area

Construction of arbitrage-free implied volatility surfaces for listed equity-index options, 2015–2026, compared across four constraint-enforcement families: parametric construction, penalty, projection-repair, and generation-filtering.

### Primary Research Question

How do parametric construction, penalty, projection-repair, and generation-filtering methods for constructing equity-index implied volatility surfaces enforce static and dynamic no-arbitrage constraints?

### Hypotheses / Expectations (to be tested in Phase 3, not findings)

- **H1.** Static constraints are mostly established *by construction* in the parametric family, while dynamic consistency is usually asserted or tested numerically rather than proved.
- **H2.** Penalty and projection-repair families report lower fit error but move the constraint burden into a tolerance, weight, or repair step that is rarely validated out of sample.
- **H3.** Generation-filtering methods claim arbitrage compliance from finite-sample acceptance tests, so "arbitrage-free" there means "not rejected on this sample", not "guaranteed".

### FINER Assessment

| Criterion | Score (1–5) | Justification |
|---|---:|---|
| Feasible | 4 | Secondary literature only; discovery and abstract-level verification fit an unattended run; no proprietary data or estimation needed. |
| Interesting | 4 | The families promise materially different things about the same constraint, and proof-versus-practice is a live model-risk question. |
| Novel | 3 | IVS surveys exist, but a constraint-centred four-family comparison for 2015–2026 that separates proof, test, and assumption is incremental rather than wholly new. |
| Ethical | 5 | No human subjects; public sources; no trading or financial advice; standard AI and citation-integrity disclosure applies. |
| Relevant | 4 | Bears on pricing, risk management, model validation, and regulatory use of surfaces. |
| **Average** | **4.0/5** | Threshold met (average ≥ 3.0; no criterion < 2). |

### Scope Boundaries

| Axis | In scope | Out of scope |
|---|---|---|
| Domain | Mathematical finance; equity-index option pricing; volatility-surface construction; static and dynamic no-arbitrage | Pure pricing without surface construction; IV forecasting or trading signals; high-frequency microstructure; exotic or variance-swap pricing as the primary object |
| Timeframe | 2015–2026 | Pre-2015 work, except seminal background explicitly flagged and excluded from core evidence |
| Geography | Global listed equity-index options (e.g. SPX, SX5E, FTSE 100, NKY); English-language literature | Non-English literature; single-market regulatory description without method content |
| Population | Listed equity-index option surfaces (not human subjects) | Single-stock, FX, commodity, and crypto surfaces unless the constraint treatment transfers and is flagged |
| Evidence type | Peer-reviewed articles, plus preprints and working papers graded explicitly | Vendor notes, undated web material, predatory venues, duplicate reports |

**Key assumptions:** papers state the enforced constraint precisely enough to code; "static" and "dynamic" can be standardized across families; reported metrics are not directly comparable across datasets; residual-violation results are less likely to be published than successes.

### Sub-questions

1. Which static conditions (butterfly / strike-convexity and calendar / total-variance monotonicity) does each family enforce, by what mechanism, and at what evidence status — proof, numerical test, or assumption?
2. Which dynamic requirements (consistent surface evolution, no calendar arbitrage across dates, model-implied dynamics) are addressed, and are they enforced or merely tested?
3. What trade-offs are reported across fit accuracy, temporal stability, extrapolation and wing behaviour, computational cost, interpretability, and reproducibility?

### Sub-question Bindings

1. inherits: domain=equity-index IVS construction; timeframe=2015–2026; geography=global listed indices; population=listed equity-index option surfaces. deviations: none.
2. inherits: all four axes above. deviations: none.
3. inherits: all four axes above. deviations: none.

### Candidate Questions Considered

| # | Candidate | FINER avg | Decision |
|---|---|---:|---|
| 1 | How do the four families enforce static and dynamic no-arbitrage constraints? | 4.0 | Selected |
| 2 | Do neural IVS methods beat parametric methods out of sample? | 3.2 | Rejected: empirical horse-race needing reconstructed data, not constraint-centred |
| 3 | How do exchanges and regulators define an acceptable surface? | 3.0 | Rejected: policy scope, thin method content |

## 2. Methodology Blueprint

### Research Paradigm

**Pragmatist, with positivist treatment of reported numerical evidence.** The object is what each enforcement mechanism actually delivers; reported errors and violation counts are observable evidence, while the comparison across them is interpretive. A wholly positivist framing would over-read reported metrics as validation of arbitrage-freeness, so the evidence-status field below exists to prevent that.

### Method

**Type and specific method:** mixed-methods evidence synthesis — a structured literature review with a comparative, constraint-centred design, reported as a **narrative/integrative synthesis**. Qualitative coding of enforcement mechanisms is combined with structured extraction of reported evaluation figures. **No PRISMA or PRISMA-ScR claim is made**; no meta-analysis and no original estimation, because datasets, maturities, error metrics, and out-of-sample protocols are too heterogeneous to pool. The RQ asks how constraints are enforced, a comparative-descriptive question; an empirical horse-race would require a different RQ and unavailable data.

### Data Strategy

**Type:** secondary, public metadata and abstracts.

- **Discovery — OpenAlex.** Works search on the string below, DOI lookup for candidate records, and one snowballing round through `referenced_works` and citation links where available. Recorded per record: OpenAlex work ID, DOI, title, year, venue, authors, cited-by count.
- **Screening.** Title/abstract/venue/year against the criteria; every exclusion logged with a reason code.
- **Verification — abstract level.** Abstracts reconstructed from the OpenAlex inverted abstract index. Read scope is `abstract_only` for all sources, so method weaknesses are recorded as `not assessed (read scope: abstract_only)` and never inferred.

```text
("implied volatility surface" OR "volatility surface" OR "IVS")
AND ("no-arbitrage" OR "arbitrage-free" OR "static arbitrage" OR "calendar arbitrage")
AND ("parametric" OR "SVI" OR "SSVI" OR "nonparametric" OR "neural" OR "deep learning" OR "penalty" OR "projection" OR "repair" OR "generative")
```

**Inclusion:** equity-index options; full-surface construction or fitting; explicit static or dynamic no-arbitrage treatment; a described method and at least one evaluation dimension; English; 2015–2026; peer-reviewed or graded preprint; resolvable DOI or OpenAlex record. **Exclusion:** pricing without surface construction; forecasting or trading studies; microstructure; non-equity-index surfaces unless flagged as transferable; no no-arbitrage treatment; non-English; predatory venue; duplicate report. **Sampling:** exhaustive within scope rather than convenience; planning target 40–60 records screened and 25–40 included, with actual counts reported in Phase 2. Pre-2015 seminal work is background only and is not counted as core evidence.

### Analytical Framework

**Four-family enforcement taxonomy**, frozen before extraction and used as the coding scheme:

| Family | Enforcement locus | Typical mechanism | What it can establish | Typical failure mode |
|---|---|---|---|---|
| Parametric construction | Functional form and parameter domain | Parameter restrictions make each slice convex in strike and total variance monotone in maturity | Static conditions by construction, where the parameter map is closed under them | Restrictions too tight at the wings; fit loss; dynamic consistency still unproven |
| Penalty | Objective function | Violation terms (butterfly, calendar) added to the fit loss with weights | Approximate compliance at best, conditional on weight and tolerance | Residual violations; weight sensitivity; no guarantee |
| Projection-repair | Post-fit output | Project the raw surface onto the admissible set (convexification, monotone rearrangement, price projection) | Static conditions at the repaired point, if the projection is correctly specified | Repair distorts fit; repeated repair drifts; no cross-date enforcement |
| Generation-filtering | Candidate generation plus acceptance test | Generate candidates and accept or reject them against arbitrage tests | Compliance only on the accepted finite sample | A passed test is not a proof; rejection cost; test power unknown |

**Procedure:** (1) code source into a family and constraint row; (2) record evidence status per row as `proof`, `numerical test`, or `assumption`, never upgrading a test to a proof; (3) extract evaluation figures with dataset, sample period, maturities, metric, and comparability flag; (4) synthesize convergence and divergence by family; (5) run gap analysis over constraints no family enforces. **Evaluation dimensions:** static arbitrage compliance; dynamic consistency; fit accuracy; temporal stability; extrapolation and wing behaviour; computational cost; interpretability; reproducibility (code and data availability). No league table, no vote-counting: results are reported as ranges and conditions, never as a single winner.

### Validity and Reliability Criteria

| Criterion | Strategy |
|---|---|
| Coverage | Reproducible query string, OpenAlex query log, exclusion reason codes, one snowballing round |
| Construct | Frozen taxonomy and one fixed evidence-status field; identical constraint names across families |
| Verification | Abstract-level claims only within the declared read scope; no claim beyond the abstract |
| Coding reliability | Scheme applied twice to a calibration subset; disagreements adjudicated and the scheme amended before full extraction; counts reported |
| Triangulation and reproducibility | Multiple sources per claim, contradictions reported rather than smoothed; search log, extraction table, coding scheme, and source list retained in this workspace |

### Limitations, Ethics, and Reporting

Abstract-only reading limits method-level assessment and can hide constraint details that appear only in full text. English-language and OpenAlex-indexed coverage bias. Publication bias favours positive results. Heterogeneous metrics prevent pooling. Generation-filtering literature moves fast, so 2026 is a snapshot boundary. H1–H3 were declared before reading so disconfirming evidence can be sought. The review assesses *reported* enforcement and cannot prove arbitrage-freeness.

No human subjects and no identifiable personal data, so no ethics review or consent process applies. Public secondary sources only; AI-assisted discovery and coding are disclosed in the report; every reference must resolve to a real OpenAlex record or DOI, and unverifiable items are excluded rather than hedged. No trading, investment, or financial advice; no dual-use concern beyond ordinary financial research. Reporting is a narrative/integrative synthesis with a documented search, screening, and coding trail — **no PRISMA 2020 or PRISMA-ScR claim**. Preregistration is not required for this design, OSF is optional and not planned, and PROSPERO does not apply because this is not a systematic review.

## 3. Devil's Advocate — Checkpoint 1

**Verdict: PASS.** No Critical issue. Three Major issues must be fixed inside the Phase 2 protocol, not deferred to review.

### Vulnerabilities Checked

| Check | Finding | Result |
|---|---|---|
| RQ clarity and answerability | Single sentence, single inquiry, answerable from published method descriptions at abstract level | Pass |
| Method appropriateness | Comparative synthesis fits a "how is X enforced" question; an empirical comparison would answer a different one | Pass |
| Scope breadth | 2015–2026, equity-index only, four families — broad enough to matter, bounded enough to screen exhaustively | Pass, within the stated axes |
| Paradigm and bias assumptions | Positivist reading of reported numbers is the hidden assumption, countered by the evidence-status field; H1–H3 could steer coding toward "non-parametric methods overclaim", countered by a disconfirming-evidence pass | Pass |

### Major Issues (required fixes)

1. **"Arbitrage-free" is not one claim.** Papers prove, test, assume, or merely assert it, and some enforce only one of the two static conditions. Comparing these as equals would manufacture a false consensus. *Fix:* evidence status on every constraint row; never describe a numerically tested method as arbitrage-free.
2. **Comparability of reported performance.** Datasets, maturities, weighting, and out-of-sample protocols differ, and abstract-level reading may not even name the metric. *Fix:* comparability flags plus a "reported for context, not comparable" bucket; ranges and conditions only; no ranking.
3. **Selection and recency bias.** The generation-filtering literature is recent, loud, and preprint-heavy, while parametric baselines are undercited and negative results rarely published. *Fix:* explicitly search and include classical parametric baselines, grade preprints, and log every exclusion with a reason code.

### Minor Issues and Gaps

- The 2015 cutoff excludes foundational parametric work (keep as flagged background); abstract-only reading cannot settle whether a dynamic claim is enforced or tested, so such claims are downgraded to "not determinable at abstract level".
- "Construction" in the title could overclaim a new method; the deliverable catalogues enforcement, it does not build one.
- Still missing until Phase 2: whether any source reports *residual* violations after enforcement — the most informative evidence for H2 and H3. Dynamic no-arbitrage is also model-specific, so surface-level static arbitrage and dynamic model consistency must stay separate constructs.

### Strongest Counter-Argument

"A review of abstracts cannot establish arbitrage-freeness, and a taxonomy imposed from outside may not match how these papers frame their constraints. The result may be a tidy table that validates nothing."

**Response:** the claim is about reported enforcement and evidence status, not about proving arbitrage-freeness; the taxonomy is amended against the calibration subset before full extraction, and read scope is declared per source.

### Stress Tests

| Test | Result |
|---|---|
| Remove the strongest source — does the argument hold? | Yes by design (multi-source claims); testable in Phase 3 |
| Flip the RQ — is the opposing view credible? | Yes: unconstrained fits may be more stable and constraints may cost accuracy; must be reported |
| Different context, and "so what?" | Generalization not claimed (single-stock and FX surfaces out of scope); significance rests on model risk, pricing, and validation depending on what "arbitrage-free" means |

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

**Unattended-run record.** This is an unattended end-to-end validation run: the operator preauthorized the pipeline, and the recorded author reply to be used is “确认” (continue current work). No separate review form is therefore selected, the current `deep-research` `full` mode continues unchanged, and no PRISMA or PRISMA-ScR claim will be made.

## 5. Readiness for Phase 2

Phase 1 is complete and internally consistent: one answerable RQ, three bound sub-questions, a frozen four-family taxonomy, declared abstract-level read scope, and no blocking Devil's Advocate finding. **Phase 2 may start and must deliver:** the OpenAlex query log; the screened corpus with exclusion reason codes; an annotated bibliography in APA 7.0; per-source verification and grading against `references/source_quality_hierarchy.md`; and explicit `abstract_only` read-scope labels. It must apply the three Major fixes in §3 and must not claim PRISMA coverage, full-text verification, or synthesis — those belong to later phases or are not claimed at all.

**Carried forward, not resolved:** H1–H3 remain untested expectations; dynamic no-arbitrage definitions remain to be coded from the sources; final corpus size is unknown until the query runs. Contract coverage: RQ brief and FINER (§1), scope axes and sub-question bindings (§1), methodology blueprint with paradigm/method/data/framework/validity/ethics (§2), Devil's Advocate Checkpoint 1 (§3), review-form note #921 (§4), readiness (§5).
