# Phase 1 — Literature Strategy and Evidence Map

**Run:** `iv-surface-review-v047` · **Stage 2, Phase 1** · **Agent role:** literature strategist · **Date:** 2026-11-23
**Inputs:** frozen Stage 1 records (`phase1-scoping.md`, `phase2-bibliography.md`, `phase2-verification.md`, `phase3-synthesis.md`, `phase6-final.md`, `search/selected_sources.json`).
**Mode:** corpus-first. No external search was run for this phase.
**Review-criteria binding status:** `criteria_binding_unavailable` (inherited from Phase 0; Phase 1 is not a binding consumer; no venue-fit claim).

## 1. Corpus-First Pre-Screen

The Stage 1 corpus is complete and frozen. Phase 1 therefore performs the corpus-first path: it re-checks the 41 records against the review's inclusion frame, maps each record to the planned paper, and allocates claims. It does not search, chain citations, forward-track, or add sources.

```text
PRE-SCREENED (corpus-first)
Adapter:            ARS Material Passport -> literature_corpus[] (41 records)
Snapshot:           examples/dsh/iv-surface-review-v047/search/selected_sources.json, frozen 2026-11-23
Included:           41
Excluded at Phase 1: 0 (no re-screening; Stage 1 exclusions remain reason-coded)
Skipped:            0
New search:         none
```

**Iron-rule attestation.** The same inclusion criteria were applied as in Stage 1; no record was silently skipped; the corpus was not mutated; no fallback search was triggered. The one disclosed scope exception is C5 (single-stock panel), retained from Stage 1 with its scope flag. The 3 metadata-only records (P4, P7, R4) are retained at title level only.

## 2. Inherited Search Strategy (reported, not re-run)

The paper's method section reports the Stage 1 search. Phase 1 does not re-execute it.

| Element | Record |
|---|---|
| Database | OpenAlex REST API (single database) |
| Query count | 31 free-text queries in 8 groups: broad 2, parametric 6, penalty 2, projection–repair 3, generation 6, neural 6, dynamic 3, evaluation 3 |
| Page size / window | 25 records per query; 2015-01-01 to 2026-11-23; English |
| Retrieval arithmetic | 775 requested; 750 returned; one query lost after HTTP 429 ("SVI stochastic volatility inspired"); 21 first-pass 429 responses, 20 recovered |
| Snowballing | one citation-chaining pass; no additional included source |
| Abstract recovery | Crossref and Semantic Scholar used only to recover abstracts, not to add records |
| Screening | 430 unique records after de-duplication; 389 excluded; 41 included |
| Exclusion codes | OFF_TOPIC 141; PRE_2015_BACKGROUND 86; RELEVANT_NOT_SELECTED 40; OUT_OF_SCOPE_ASSET 34; PUBLICATION_TYPE 32; DUPLICATE_VERSION 31; FORECASTING_OR_TRADING 21; MODEL_CALIBRATION_PRICING 4 |
| Final corpus | 41: 36 in-window (2015–2026) + 5 declared seminal precursors (1999–2014); 29 peer-reviewed, 11 preprints, 1 practitioner magazine |
| Conformity statement | "PRISMA-style, not PRISMA-compliant"; no PRISMA or PRISMA-ScR claim is made |

Four replacement decisions after abstract reading are inherited: N2 (Wiedemann et al. 2025) and C4 (Fukasawa 2022) replaced earlier candidates; 40 discretionary exclusions are disclosed in Stage 1. The paper reports these as design choices, not as concealment.

## 3. Coverage Distribution Advisory

Non-blocking; no quota was imposed. The numbers describe the corpus, not the field.

| Check | Result | Advisory |
|---|---|---|
| Family concentration | R 9/41 (22%) is the largest group; no known value reaches 70% | No `DISTRIBUTIONAL_SKEW_ADVISORY` for family |
| Recency | 20/41 (49%) from 2023–2026 | Disclosed; the paper reads recent work as a fast-moving evidence layer, not as the whole corpus |
| Older non-seminal work | 11/41 (26.8%) at or before 2020, excluding the 5 seminal rows | Within the 30% ceiling; no trigger |
| Preprints | 11/41 (26.8%); four from 2025–2026 (Alvarez 2025; Anagha 2026; Barski & Wiśniewolski 2026; Buehler et al. 2026) | Within the 30% ceiling; each is labelled and its strongest claims are flagged |
| Geographic provenance | US-index evidence in 10 of 12 rows with known provenance (83%) | `DISTRIBUTIONAL_SKEW_ADVISORY` (non-blocking); non-US evidence is S5 (DAX, 2006) and N4 (JSE ALSI, 2022) |
| Abstract coverage | 34 full / 4 partial (R2, G3, C4, S1) / 3 metadata-only (P4, P7, R4) | Partial rows are used only for what the abstract states; metadata-only rows at title level |
| Evidence status | 17 proof / 16 numerical test / 8 assumption; in-window 16 / 14 / 6 | Distribution reported; no upgrading of tests to proofs |

**Reading rule.** The corpus is an evidence base for a structured review, not a probability sample of the field. Absence statements are bounded to the 41 abstracts read, not to the literature at large.

## 4. Corpus Profile

| Group | n | Rows | Evidence status (proof / test / assumption) | Quality labels (A / B / C) |
|---|---|---|---|---|
| Parametric construction (P) | 8 | P1–P8 | 6 / 0 / 2 | 5 / 0 / 3 |
| Penalty / constrained learning (N) | 6 | N1–N6 | 0 / 6 / 0 | 0 / 3 / 3 |
| Projection–repair (R) | 9 | R1–R9 | 3 / 4 / 2 | 1 / 3 / 5 |
| Generation–filtering (G) | 8 | G1–G8 | 4 / 3 / 1 | 3 / 3 / 2 |
| Conditions / evaluation (C) | 5 | C1–C5 | 3 / 1 / 1 | 2 / 2 / 1 |
| Seminal baselines (S) | 5 | S1–S5 | 1 / 2 / 2 | 0 / 2 / 3 |
| **Total** | **41** | | **17 / 16 / 8** | **11 / 13 / 17** |

Quality labels are source-appraisal labels (peer review, method reporting, currency, COI retrieval). They are not performance ranks and are never used to order methods.

## 5. Evidence Map: 41 Sources to Planned Paper Sections

Sections refer to the outline in `phase2-outline.md`. Every source is assigned to at least one section. The "allocation" column states what the paper may use the source for; it does not license claims beyond the source's stated evidence.

| ID | Source (short) | Family | Evidence status | Grade | Planned section(s) | Allocation in the paper |
|---|---|---|---|---|---|---|
| P1 | Guo et al. (2016) | Parametric | proof | A | 2.1, 4.1 | Parameter-domain guarantee; structural no-arbitrage set; "by construction" claim |
| P2 | Martini & Mingone (2022) | Parametric | proof | A | 2.1, 4.1 | Exact butterfly characterisation via −d1/−d2 monotonicity; completes S1; calibration on the admissible set |
| P3 | Mingone (2022) | Parametric | proof | A | 4.1 | All-maturity joint eSSVI calibration; static guarantee across maturities, not dynamic consistency |
| P4 | Corbetta et al. (2019) | Parametric | assumption | C | 4.1 | Sequential slice-wise counterpart; metadata-only; title-level contrast with P3 |
| P5 | Zaugg et al. (2025) | Parametric | proof | A | 4.1 | Random-coefficient family; wider admissible shapes incl. bimodal short-dated densities |
| P6 | Le Floc'h (2025) | Parametric | proof | A | 4.1 | C3 interpolation as construction; fewer knots; construction rather than calibration |
| P7 | Klassen (2016) | Parametric | assumption | C | 2.1, 4.1 | Title-level necessary-and-sufficient SSVI/S3 claim; metadata-only; cannot corroborate the condition set |
| P8 | Barski & Wiśniewolski (2026) | Parametric | proof | C | 4.1, 6.2 | Gaussian-factor arbitrage probabilities; bounded-factor conditions; only time-indexed parametric row |
| N1 | Cao et al. (2020) | Penalty | numerical test | B | 4.2, 2.3 | Gated network with constraint-bearing slopes/weights; boundary case between penalty and architecture |
| N2 | Wiedemann et al. (2025) | Penalty | numerical test | B | 4.2, 5.3 | Graph neural operator; 10-year intraday SPX adherence report; no tolerance stated |
| N3 | Ackerer et al. (2019) | Penalty | numerical test | C | 4.2 | Soft penalties plus plug-in correction; sparse and erroneous data; residual handling |
| N4 | Sidogi et al. (2022) | Penalty | numerical test | B | 4.2, 6.3 | GAN with arbitrage loss on ALSI; explicit "cannot directly learn" limit of the penalty route |
| N5 | Na et al. (2023) | Penalty | numerical test | C | 4.2 | Penalty minimises violations; accuracy/runtime against an ANN; residual not a guarantee |
| N6 | Hoshisashi et al. (2023) | Penalty | numerical test | C | 4.2 | DCNN with derivative constraints; SABR-generated data; maturity-derivative term in the loss |
| R1 | Cohen et al. (2020) | Projection–repair | numerical test | B | 4.3 | LP repair; minimal price change inside the bid–ask; no cross-date enforcement |
| R2 | De March & Henry-Labordère (2019) | Projection–repair | proof | C | 4.3 | Sinkhorn/MOT projection; convergence proof; partial abstract; repair as projection |
| R3 | Bender & Thiel (2020) | Projection–repair | proof | A | 4.3, 2.3 | Arbitrage-free call-price interpolation by distortion; construction/repair boundary; Kahalé special case |
| R4 | Yao et al. (2026) | Projection–repair | assumption | C | 4.3 | Joint American call/put smoothing; metadata-only; title-level scope expansion |
| R5 | Xiong & Liu (2026) | Projection–repair | numerical test | B | 4.3, 5.3 | Observation-anchored repair; 252 OOS SPX days; ~5.4% butterfly floor; five backends; residual not zero |
| R6 | Buehler et al. (2026) | Projection–repair | proof | C | 4.3, 2.3 | SANOS strictly arbitrage-free non-parametric surfaces; LP calibration; positive discrete local vol; boundary |
| R7 | Alvarez (2025) | Projection–repair | numerical test | C | 4.3, 5.3 | Chebyshev tensor + QP + post-fit adjustment; <1% violations, 98–99% inside-spread coverage; stressed leakage |
| R8 | Zetocha (2023) | Projection–repair | assumption | C | 4.3 | OT-inspired transformations asserted; no proof or test; claim-discipline example |
| R9 | Madan & Schoutens (2019) | Projection–repair | numerical test | B | 4.3, 6.2 | Markov-chain approximations; 2,695 SPY options across 28 maturities; time axis present, no dynamic audit |
| G1 | Ning et al. (2023) | Generation–filtering | proof | A | 4.4, 2.3 | VAE over SDE parameters; arbitrage-free inherited from the SDE class; generation with structural guarantee |
| G2 | Vuletić & Cont (2024) | Generation–filtering | numerical test | B | 4.4, 6.2 | VolGAN; joint surface + underlying scenarios; hedging against BS delta; enforcement mechanism not described |
| G3 | Cont & Vuletić (2023) | Generation–filtering | assumption | C | 4.4 | Simulation of arbitrage-free surfaces; partial abstract; static constraints inside a generated process |
| G4 | Ginart Belmonte & Cole (2025) | Generation–filtering | numerical test | B | 4.4 | GAN denoiser; lower MSE/runtime; no guarantee; smoothing use case |
| G5 | Bajalica et al. (2026) | Generation–filtering | numerical test | B | 4.4, 5.1 | Latent flow matching; 90.8% of generated surfaces pass all tested static conditions; clearest pass-rate report |
| G6 | Anagha (2026) | Generation–filtering | proof | C | 4.4, 5.1, 5.3 | Trainable hard constraints; 0.00% at 1e-4 over 15 runs on synthetic SVI; higher RMSE; only row reporting both guarantee and audit |
| G7 | Cohen et al. (2021) | Generation–filtering | proof | A | 4.4, 2.2 | Neural-SDE state space of statically arbitrage-free prices; explicit no-dynamic-claim caveat |
| G8 | Yang et al. (2017) | Generation–filtering | proof | A | 4.4 | Gated network rational by design; early architectural guarantee; static call-surface encoding |
| C1 | Neufeld & Sester (2024) | Conditions/evaluation | proof | A | 5.2, 6.3 | NN detector of model-free static arbitrage; independent auditor; never applied to another corpus row |
| C2 | Niu (2015) | Conditions/evaluation | assumption | C | 2.2, 6.2 | Review of static and dynamic conditions; only sustained dynamic discussion; non-peer-reviewed |
| C3 | Andrès et al. (2026) | Conditions/evaluation | proof | A | 6.2 | Path-dependent IVS; SSVI + OU/Jacobi paths; static-free paths, not dynamic consistency |
| C4 | Fukasawa (2022) | Conditions/evaluation | proof | B | 2.2, 6.2 | Asymptotic arbitrage-free BBF/SABR/rough SABR; scale-relative guarantee |
| C5 | Stahl & Blauth (2024) | Conditions/evaluation | numerical test | B | 6.2 | Martingale defects and bubbles; SABR local-martingale conditions; single-stock panel; scope flag |
| S1 | Gatheral & Jacquier (2013) | Seminal | proof | B | 2.1, 4.1 | Sufficient SVI conditions; canonical baseline; proof-level static guarantee |
| S2 | Fengler (2009) | Seminal | numerical test | B | 4.3 | Shape-constrained smoothing splines; early demonstration that ignoring constraints matters |
| S3 | Hagan et al. (2014) | Seminal | numerical test | C | 1.1, 2.2 | SABR finite-strike arbitrage; 1-D PDE density fix; canonical failure and repair |
| S4 | Bodurtha & Jermakyan (1999) | Seminal | assumption | C | 1.1 | Nonparametric inversion without explicit enforcement; pre-constraint baseline |
| S5 | Fengler et al. (2006) | Seminal | assumption | C | 1.1, 6.2 | Semiparametric factor model on DAX; no enforcement; non-US seminal baseline |

**Boundary cases to keep visible in the paper.** R3 and R6 sit between construction and repair; N1 sits between penalty and architectural guarantee; G7 and C3 are model-level constructions whose guarantee is inherited, not learned. The outline flags each in the relevant section rather than forcing a clean family assignment.

## 6. Source-to-Claim Allocation

Ten claims carry the paper. Each is traceable to the Stage 1 final report or synthesis; citations are the sources that license the claim. Aggregate counts are the review's coding, not a source's claim.

| Claim | Planned claim | Licensing sources | Evidence shape | Planned section(s) |
|---|---|---|---|---|
| CL1 | Static no-arbitrage is enforceable in all four families, but each family enforces it on a different object | P1, P2, P3, P5, P6, P8; R1, R2, R3, R6; G1, G6, G7, G8; N1 | Proof and test mix; no family-level certificate | 2.1, 4.1–4.4, 6.1 |
| CL2 | Four enforcement loci — parameter domain, objective, output image, sampler/acceptance test — explain the family differences | P, N, R, G groups; boundary R3, R6, N1; S1 | Conceptual synthesis of coded rows | 2.3, 4, 6.1 |
| CL3 | Dynamic no-arbitrage is absent from the corpus, not merely unproven | all 41 rows (0 enforce or test); time rows P8, R9, G1, G2, G3, G7, R8, C2, C3, C5 | Bounded absence over 41 abstracts | 5.1, 6.2 |
| CL4 | Proof-level and audit-level evidence are nearly disjoint | 17 proof rows; audit rows N2, N6, R5, R7, G5, G6; G6 only both | Coding cross-tab | 5.1, 6.1 |
| CL5 | Cross-family comparison is not licensed, so no method ranking is possible | comparability 0 direct / 30 context / 11 not comparable; seven metric families | Comparability coding | 5.2, 6.1 |
| CL6 | The measured cost of a stronger guarantee is one-sided: fit or residual, rarely both | G5, R5, R7, G6 | Sparse paired measurements | 5.3, 6.3 |
| CL7 | Calendar conflation and asymptotic scale relativity inflate apparent dynamic coverage | C2, C3, C4, C5, G5, G6, G7, P8, R5, S3 | Definitional and scale analysis | 2.1, 2.2, 6.2 |
| CL8 | Generation evidence splits by where the guarantee is located: inherited model class vs penalised sampling | G1, G6, G7, G8, N1; G2, G4, G5 | Within-group comparison | 4.4, 5.1, 6.1 |
| CL9 | The claim that penalties or repair reduce fit error is unsupported; burden displacement is supported | N4, N5, R5, R7, G6 | Absence of paired tests; one contrary measurement | 4.2, 4.3, 5.3, 6.3 |
| CL10 | The enforcement framework resolves the apparent disagreement and yields a falsifiable seven-study agenda | framework (synthesis §5); Gaps 1–7 | Proposed framework; design propositions | 2.3, 6.1, 6.3, 7.1 |

## 7. Literature Matrix: Themes, Sources, and Evidential Status

| Theme | Sources | Status in corpus | Planned section(s) |
|---|---|---|---|
| TH1 Static certification is real but object-specific | P1–P8; N1–N6; R1–R9; G1–G8; S1–S2 | Strong: 41/41 coded on the static predicate; guarantees differ by locus | 2.1, 4.1–4.4 |
| TH2 Four loci, four meanings of one phrase | P, N, R, G groups; boundary R3, R6, N1; S1 | Strong conceptual fit; boundary cases disclosed | 2.3, 4, 6.1 |
| TH3 No dynamic enforcement or test | all 41 rows; 10 time-engaging rows; C2 | Strong bounded absence: 0/41, 0/36 in-window, 0/31 construction | 5.1, 6.2 |
| TH4 Proof and audit are disjoint channels | 17 proof rows; 6 audit rows; G6 only both | Strong cross-tab; G6 on synthetic data | 5.1, 6.1 |
| TH5 No direct comparability; fragmented metric vocabulary | 0/30/11; N1, N2, G2, G4, G5, N4, R5, R6, R7, R9, C1, G6 | Strong coding result; within-study baselines only | 5.2, 6.1 |
| TH6 The cost of a guarantee is rarely measured on both sides | G6, R5, R7, G5 | Emerging: one paired measurement, three residual/pass-rate reports | 5.3, 6.3 |
| TH7 Generation splits into inherited-guarantee and penalised-sampling branches | G1, G6, G7, G8, N1; G2, G4, G5 | Moderate: small branches; mechanism often under-described | 4.4, 5.1, 6.1 |

## 8. Identified Gaps and Framing

Seven gaps frame the paper's contribution and agenda. Each is an evidence absence in this corpus, bounded to the 41 abstracts; none is a claim about the whole field.

| Gap | What is absent | Where the paper uses it |
|---|---|---|
| Gap 1 Dynamic enforcement | 0/41 rows enforce or test a dynamic condition; 10 rows engage time; C2 reviews the question without testing it | 5.1, 6.2, 6.3 (agenda study 1) |
| Gap 2 Pre-registered head-to-head | 0/41 direct comparisons; within-study baselines only; no common dataset, condition set, tolerance, metric, or protocol | 5.2, 6.3 (agenda study 2) |
| Gap 3 Residual audit for proof constructions | 17 proof rows report no violation rate; 6 rows audit only; G6 is the only row reporting both, on synthetic data | 5.1, 6.3 (agenda study 3) |
| Gap 4 Test power and noise floor | No row estimates the power of its violation test or the noise floor of the data | 5.3, 6.3 (agenda study 4) |
| Gap 5 Data efficiency | No row reports violation rate or fit as a function of quote count, date count, or training-set size | 5.3, 6.3 (agenda study 5) |
| Gap 6 Index generality | 10 of 12 known-provenance rows use US indices; non-US evidence is a 2006 DAX study and a 2022 JSE study | 6.2, 6.4, 6.3 (agenda study 6) |
| Gap 7 Cost and interpretability | Computational cost is asserted in ~5 rows with no comparable measurement; interpretability appears in 0 rows | 5.3, 6.3 (agenda study 7) |

**Framing for Phase 2.** The paper does not ask "which family is best." It asks what each family's "arbitrage-free" claim is a claim about, what evidence backs it, and what cannot be compared. That framing turns the four-family taxonomy from a classification device into an evidential one.

## 9. Counter-Evidence and Scope Flags

Sources that qualify, rather than support, the thesis are retained and cited; none is suppressed.

| Source(s) | What qualifies the thesis | Planned treatment |
|---|---|---|
| N4, N5 | Penalty routes explicitly report residual violations and one states the condition cannot be directly learned | Confirms the locus distinction; not treated as a counterexample |
| G5 | 90.8% pass rate could be read as operational adequacy | Pass rate is not a guarantee; test power and tolerance are unknown |
| R5, R7 | Low residual rates suggest repair can be operationally adequate | Adequacy is not claimed; both are data- and tolerance-dependent |
| G2 | Joint surface + underlying generation with hedging evidence | Scenario generation, not certification; enforcement mechanism not described |
| C2 | A dynamic-condition review exists | Review, not test; supports the bounded-absence claim |
| C5 | Single-stock panel is dynamic-adjacent | Scope flag; no index-transfer claim |
| P8 | Time-indexed arbitrage probabilities | Parametric probabilities, not a path-level test |
| C3 | Path-dependent IVS construction | Static-free paths; no dynamic consistency |
| G7 | Neural SDE explicitly makes no dynamic claim | Confirms separation of static and dynamic claims |
| S3 | SABR arbitrage at finite strikes | Canonical failure and repair; not a counterexample |
| C4 | Asymptotic arbitrage-free approximation | Scale-relative; not a finite-strike certificate |

## 10. Handoffs

**To structure_architect (Phase 2).** Use the 41-row map and the ten-claim allocation unchanged. Counts for tables: 17/16/8 evidence status; 0/30/11 comparability; 34/4/3 abstract coverage; 11/13/17 quality labels; 0/41 dynamic. Every source must land in at least one section; the boundary cases (R3, R6, N1, G7, C3) must stay explicitly flagged.

**To argument_builder (Phase 3).** The seven sub-arguments derive from claims CL1–CL10. Sources tagged **supports** (static claims): P1, P2, P3, P5, P6, P8, R1, R2, R3, R6, G1, G6, G7, G8, N1, C1, C2, C4, S1, S2, S3. Sources tagged **qualifies/opposes** (dynamic or scope): N4, N5, G5, R5, R7, G2, C5, P8. P8 appears in both lists because it supports the static claim while qualifying the dynamic reading. Sources tagged **neutral/context**: P4, P7, N2, N3, N6, R4, R8, R9, G3, G4, C3, S4, S5. No source is tagged as supporting a ranking; none licenses one.

**To draft_writer (Phase 4).** Use the per-section source lists; label metadata-only rows at title level; mark preprints; keep C5's scope flag; never call a numerical test "arbitrage-free"; report aggregate counts as the review's coding. No new references.

## 11. No-New-Search Attestation

No database query, citation-chaining pass, forward-tracking pass, semantic search, or source addition was performed in Phase 1. The corpus is the frozen Stage 1 `search/selected_sources.json` (41 records). Any future source would be a scope change requiring a new search, a new verification pass, and a new configuration record.
