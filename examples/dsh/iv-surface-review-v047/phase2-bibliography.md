# Phase 2 - Annotated Bibliography

**Research question.** How do parametric construction, penalty, projection-repair, and generation-filtering methods for constructing equity-index implied volatility surfaces enforce static and dynamic no-arbitrage constraints?

**Run context.** ARS v3.24.4 end-to-end validation, Stage 1 (deep-research, `full` mode), Phase 2 (INVESTIGATION). Abstract-level verification only; discovery date 2026-11-23. Companion report: `phase2-verification.md`. Machine-readable corpus: `search/selected_sources.json`. Screening log: `search/screening_log.json`.

**How to read the evidence status labels.** `proof` = the abstract states a theorem, construction or guarantee that is proved in the paper. `numerical test` = the abstract reports an empirical or synthetic evaluation of a method, but no arbitrage-freeness theorem. `assumption` = the abstract asserts or implies enforcement without a proof or a test that is visible at abstract level, or no abstract could be retrieved. A numerical test is never upgraded to a proof in this run, and a title-level claim is never treated as evidence.

## 1. Search strategy

**Databases and sources.** OpenAlex REST API (fresh discovery, no API key, anonymous rate limit of about one request per second; 31 queries x 25 relevance-ranked records, one of which returned no records after retry). Crossref REST API and Semantic Scholar Graph API were used only to recover abstracts that OpenAlex did not deposit - they did not contribute candidates. DOI resolution was checked against OpenAlex (all 41) and Crossref (the 4 records recovered from it).

**Date range.** 2015-01-01 to 2026-11-23 for the working corpus; pre-2015 only as flagged seminal baselines. **Last search:** 2026-11-23. **Language:** English.

**Queries (OpenAlex free-text search, one request per query, top 25 records kept per query).** OpenAlex relevance search is not a Boolean API, so the Boolean forms below describe the concept blocks the queries operationalise, not literal request syntax.

- **broad** (2): `arbitrage-free implied volatility surface`; `implied volatility surface arbitrage`
- **parametric** (6): `SVI stochastic volatility inspired [failed: HTTP 429]`; `SSVI implied volatility surface`; `shape constrained implied volatility surface`; `nonparametric implied volatility surface`; `arbitrage-free smoothing implied volatility surface`; `SABR arbitrage-free volatility`
- **penalty** (2): `penalty no-arbitrage implied volatility`; `arbitrage penalty optimization implied volatility`
- **projection-repair** (3): `projection arbitrage-free option prices`; `repair arbitrage option price surface`; `convexification option prices arbitrage`
- **generation-filtering** (6): `generative model implied volatility surface`; `variational autoencoder implied volatility surface`; `generative adversarial network implied volatility surface`; `diffusion model implied volatility surface`; `simulation arbitrage-free implied volatility surface`; `neural SDE volatility surface`
- **neural** (6): `neural network implied volatility surface`; `deep learning implied volatility surface`; `neural network option pricing arbitrage-free`; `hard constraint neural network no arbitrage`; `Gaussian process implied volatility surface`; `rough volatility calibration neural network`
- **dynamic** (3): `dynamic arbitrage implied volatility`; `calendar arbitrage implied volatility`; `butterfly arbitrage implied volatility`
- **evaluation** (3): `implied volatility surface survey`; `implied volatility surface interpolation no arbitrage`; `static arbitrage option prices`

**Boolean concept blocks used to organise the query set.**

- Broad: (`implied volatility surface` OR `volatility surface`) AND (`arbitrage` OR `arbitrage-free` OR `no-arbitrage`).
- Parametric: (`SVI` OR `SSVI` OR `SABR` OR `parametric volatility` OR `volatility parametrization`) AND (`arbitrage` OR `no-arbitrage`).
- Penalty: (`deep smoothing` OR `neural network` OR `machine learning` OR `penalty`) AND (`no-arbitrage` OR `arbitrage-free`) AND `implied volatility`.
- Projection/repair: (`projection` OR `repair` OR `Sinkhorn` OR `shape constrained` OR `arbitrage-free interpolation` OR `surface completion`).
- Generation/filtering: (`GAN` OR `VAE` OR `generative model` OR `diffusion` OR `flow matching` OR `neural SDE`) AND `implied volatility`.
- Dynamic/evaluation: (`dynamic arbitrage` OR `calendar spread` OR `static arbitrage` OR `no arbitrage conditions` OR `martingale` OR `detect` OR `test violation`) AND (`implied volatility` OR `option surface`).

**Inclusion criteria.** (IC1 topic) Implied-volatility or option-price surface construction and/or its no-arbitrage constraints. (IC2 asset scope) Equity-index listed options, or a method whose abstract makes the index application explicit; FX/rates/commodities/energy/crypto and single-name panels excluded. (IC3 window) 2015-2026 for the working corpus; pre-2015 records enter only as explicitly flagged seminal baselines (n=5, cap respected). (IC4 language) English. (IC5 publication status) Peer-reviewed research preferred; preprints eligible when directly on enforcement and graded; preprints <= 30% of corpus. (IC6 retrievability) OpenAlex record resolvable by DOI or title; abstract retrieved when available; missing abstracts are kept but never upgraded to abstract-level claims. (IC7 version rule) One record per study; peer-reviewed version preferred over preprint where both exist.

**Exclusion criteria and reason codes.** (OFF_TOPIC) Title lacks any implied-volatility/option-surface or no-arbitrage term, or is not a construction/condition study. (PRE_2015_BACKGROUND) Outside the 2015-2026 window; retained as background only. (RELEVANT_NOT_SELECTED) Topically relevant but lost to the 35-45 cap, family balance, recency or version precedence. (OUT_OF_SCOPE_ASSET) Underlying is FX, rates, commodities, energy, crypto, a single stock, or a non-financial domain. (PUBLICATION_TYPE) Dissertation, book, software/replication package, paratext or other ineligible type. (DUPLICATE_VERSION) Same study as another pool record (same DOI or near-identical title). (FORECASTING_OR_TRADING) Forecasting, hedging or trading application rather than a construction/enforcement method. (MODEL_CALIBRATION_PRICING) Stochastic-volatility model calibration/pricing without surface-construction enforcement.

## 2. Screening flow (PRISMA-style, not PRISMA-compliant)

```
Records identified through OpenAlex API (31 queries x 25 records/query; one query returned none after retry)
  pool after cross-query deduplication ......... 430
  excluded at title screening .................. 389
  included ..................................... 41
     abstracts read for confirmation ............ 41
     replaced during abstract-level reading ..... 2 (documented in the screening log)
```

| Reason code | n |
|---|---|
| OFF_TOPIC | 141 |
| PRE_2015_BACKGROUND | 86 |
| RELEVANT_NOT_SELECTED | 40 |
| OUT_OF_SCOPE_ASSET | 34 |
| PUBLICATION_TYPE | 32 |
| DUPLICATE_VERSION | 31 |
| FORECASTING_OR_TRADING | 21 |
| MODEL_CALIBRATION_PRICING | 4 |
| **Included** | **41** |

Screening was performed by one reviewer at title level for the whole pool, with abstract-level confirmation only for the included set; there was no dual screening, adjudication or kappa. Two candidates were replaced after abstract reading (old N2: neural-network IV computation with no enforcement claim; old C4: FX-oriented Delta conditions) and their replacements are recorded in the log through explicit overrides. The 40 `RELEVANT_NOT_SELECTED` records are a genuine cap/balance bucket and are disclosed as a selection-bias guard.

## 3. Corpus profile

| Dimension | Distribution |
|---|---|
| Family | Parametric construction 8 (19.5%); Penalty and constrained learning 6 (14.6%); Projection and repair 9 (22.0%); Generation and filtering 8 (19.5%); Constraint conditions and evaluation 5 (12.2%); Seminal pre-2015 baselines 5 (12.2%) |
| Evidence status | proof 17; numerical test 16; assumption 8 |
| Peer review | peer-reviewed 29 (70.7%); preprints 11 (26.8%); practitioner magazine 1; journal 23; conference 6 |
| Abstract retrieval | abstract 34; partial 4; metadata-only 3 |
| Time | pre-2015 (explicit seminal baselines) 5; 2015-2019 8; 2020-2022 8; 2023-2026 20 |

## 4.1 Parametric construction (n=8)

All eight works push the guarantee into the parametrisation itself: a restricted parameter domain (P1, P2), a global all-maturity construction (P3), a structural interpolation (P6), a widened admissible family (P5), or - per title only - a calibration constrained to the no-arbitrage region (P4, P7). Evidence is `proof` wherever an abstract exists; P4 and P7 are metadata-only, so their mechanism is a title-level indication only and is never used as an abstract-level claim. Only P2, P3 and S1 report market calibration in their abstracts, and none reports a finite-sample violation audit of the calibrated surface. No work in this family addresses dynamic arbitrage: the guarantee is per-surface (static), applied anew at each calibration time.

#### P1 - Guo et al. (2016)

**APA:** Guo, G., Jacquier, A., Martini, C., & Neufcourt, L. (2016). Generalized arbitrage-free SVI volatility surfaces. *SIAM Journal on Financial Mathematics*, *7*(1), 619–641. https://doi.org/10.1137/120900320

- **Family:** Parametric construction | **Evidence status:** `proof` | **Abstract:** full (OpenAlex) | **Quality level:** VI | **Peer-reviewed:** yes
- **Relevance:** Extends the SVI baseline: enforcement is a provable parameter-domain restriction, not a post-hoc repair.
- **Key findings:** Generalises Gatheral–Jacquier SVI to a broader class of explicit arbitrage-free parameterisations. Revisits the notion of arbitrage freeness using Roger Lee's moment formula and Roper's analysis, and exhibits an arbitrage-free surface outside Gatheral's SVI family. Enforcement is structural: the parameter domain itself carries the static no-arbitrage guarantee.
- **Method & evidence:** Abstract reports an explicit arbitrage-free parametrisation and an arbitrage-freeness discussion via Roper/Lee; no numerical test is reported in the abstract.
- **Method weaknesses:** Abstract-only; calibration accuracy and out-of-sample behaviour are not described, so empirical robustness is not assessed (read scope: abstract_only).
- **Comparability:** Analytical construction; no market-data fit is reported in the abstract, so fit quality is reported for context only, not comparable with empirical studies.

#### P2 - Martini & Mingone (2022)

**APA:** Martini, C., & Mingone, A. (2022). No arbitrage SVI. *SIAM Journal on Financial Mathematics*, *13*(1), 227–261. https://doi.org/10.1137/20m1351060

- **Family:** Parametric construction | **Evidence status:** `proof` | **Abstract:** full (OpenAlex) | **Quality level:** VI | **Peer-reviewed:** yes
- **Relevance:** Turns the SVI parameter domain into a fully characterised static no-arbitrage region usable by calibration.
- **Key findings:** Fully characterises the absence of butterfly arbitrage in the SVI total-variance formula. The route is Fukasawa's monotonicity condition on the inverse Black–Scholes $-d_1$ and $-d_2$ functions as functions of log-forward moneyness; rescaling the parameters and analysing the Durrleman condition yields simple range conditions. A least-squares calibration restricted to that domain is reported to fit the market data used in the paper while guaranteeing no butterfly arbitrage.
- **Method & evidence:** Full characterisation of butterfly-arbitrage absence plus range conditions on SVI parameters; a least-squares calibration on the no-arbitrage domain is also tested on market data.
- **Method weaknesses:** Abstract-only; only butterfly (not calendar) arbitrage is characterised in the abstract, and the data/period behind the fit are not identified (read scope: abstract_only).
- **Comparability:** Empirical fit on unnamed market data; fit metrics are not reported in the abstract and are not comparable with surface-generation metrics.

#### P3 - Mingone (2022)

**APA:** Mingone, A. (2022). No arbitrage global parametrization for the eSSVI volatility surface. *Quantitative Finance*, *22*(12), 2205–2217. https://doi.org/10.1080/14697688.2022.2117076

- **Family:** Parametric construction | **Evidence status:** `proof` | **Abstract:** full (OpenAlex) | **Quality level:** VI | **Peer-reviewed:** yes
- **Relevance:** Addresses the sequencing weakness of slice-by-slice SSVI calibration by calibrating all maturities jointly under an arbitrage-free constraint set.
- **Key findings:** Describes a global arbitrage-free parametrisation of eSSVI surfaces. The existing Zeliade calibration is sequential in expiry and therefore lacks a global view; the proposed calibration targets all maturities at once and is stated to guarantee an arbitrage-free fit of market data.
- **Method & evidence:** Global (all-maturity) arbitrage-free parametrisation; abstract states the calibration always guarantees an arbitrage-free fit, but reports no benchmark numbers.
- **Method weaknesses:** Abstract-only; the proof argument and the numerical comparison against the sequential calibration are not visible at abstract level (read scope: abstract_only).
- **Comparability:** No dataset or fit metrics are specified in the abstract; reported for context, not comparable.

#### P4 - Corbetta et al. (2019)

**APA:** Corbetta, J., Cohort, P., Laachir, I., & Martini, C. (2019). Robust calibration and arbitrage-free interpolation of SSVI slices. *Decisions in Economics and Finance*, *42*(2), 665–677. https://doi.org/10.1007/s10203-019-00249-8

- **Family:** Parametric construction | **Evidence status:** `assumption` | **Abstract:** metadata-only (no abstract) | **Quality level:** VI | **Peer-reviewed:** yes
- **Relevance:** Slice-level SSVI calibration with interpolation constraints; the sequential counterpart to the global eSSVI method.
- **Key findings:** [Title/metadata only — no abstract retrieved.] The title claims robust calibration together with arbitrage-free interpolation of SSVI slices. Its slice-by-slice SSVI scope makes it the natural sequential counterpart to Mingone (2022); whether that paper cites this specific work could not be verified from the available abstracts, and its enforcement mechanism and empirical support could not be checked.
- **Method & evidence:** No abstract available from OpenAlex, Crossref or Semantic Scholar; the enforcement claim and the calibration setting are inferred from the title only.
- **Method weaknesses:** Metadata-only record; no abstract, so neither the enforcement construction nor the empirical evidence can be assessed (read scope: abstract_only, abstract unavailable).
- **Comparability:** Not comparable: no abstract or result data available.
- **Flags:** metadata-only

#### P5 - Zaugg et al. (2025)

**APA:** Zaugg, N. F., Perotti, L., & Grzelak, L. A. (2025). Volatility parametrizations with random coefficients: Analytic flexibility for implied volatility surfaces. *SIAM Journal on Financial Mathematics*, *16*(4), 1374–1411. https://doi.org/10.1137/24m1713107

- **Family:** Parametric construction | **Evidence status:** `proof` | **Abstract:** full (OpenAlex) | **Quality level:** VI | **Peer-reviewed:** yes
- **Relevance:** Shows that parametric enforcement can be retained while widening admissible shapes, relaxing the rigidity critique of SVI/SABR families.
- **Key findings:** Lets the coefficients of a parametric implied-volatility formula be random, widening the admissible shape spectrum while preserving analyticity and computational efficiency. Demonstrates the construction on short-term index and equity options where standard parametrisations fail, including pre-earnings curves whose risk-neutral density is bimodal.
- **Method & evidence:** An arbitrage-free framework is proposed with an analytic guarantee (recorded as proof at abstract level) and demonstrated on short-term index and equity options; the demonstration itself is numerical.
- **Method weaknesses:** Abstract-only; the arbitrage-free guarantee is stated at framework level and the numerical checks are not detailed (read scope: abstract_only).
- **Comparability:** Short-maturity index/equity options with a specific event-driven use case; not comparable with full-surface calibration studies.

#### P6 - Le Floc’h (2025)

**APA:** Le Floc’h, F. (2025). The quadratic local variance gamma model: An arbitrage-free interpolation of class C3 for option prices. *The Journal of Derivatives*, *32*(4), 91–115. https://doi.org/10.3905/jod.2025.1.228

- **Family:** Parametric construction | **Evidence status:** `proof` | **Abstract:** full (OpenAlex) | **Quality level:** VI | **Peer-reviewed:** yes
- **Relevance:** Non-parametric-in-spirit interpolation with a hard arbitrage-free guarantee; a contrast to penalty-based smoothing.
- **Key findings:** Generalises the local variance gamma model to a piecewise-quadratic local variance function, encompassing the piecewise-linear Bachelier and Black local variance gamma models. The construction yields an arbitrage-free interpolation of class C3; the extra smoothness permits fewer knots when interpolating raw quotes and is presented as an alternative to regularisation at lower computational cost.
- **Method & evidence:** Arbitrage-free interpolation follows by construction from the piecewise-quadratic local variance function; smoothing/cost benefits are asserted rather than benchmarked in the abstract.
- **Method weaknesses:** Abstract-only; class-C3 claim and knot-reduction benefit are stated without numerical detail (read scope: abstract_only).
- **Comparability:** Interpolation of raw quotes; knot-count and cost comparisons are not quantified in the abstract, so not comparable.

#### P7 - Klassen (2016)

**APA:** Klassen, T. (2016). Necessary and sufficient no-arbitrage conditions for the SSVI/S3 volatility curve [Preprint]. *SSRN Electronic Journal*. https://doi.org/10.2139/ssrn.2725700

- **Family:** Parametric construction | **Evidence status:** `assumption` | **Abstract:** metadata-only (no abstract) | **Quality level:** VI | **Peer-reviewed:** no
- **Relevance:** Condition-level reference for the SSVI curve family used by several construction methods.
- **Key findings:** [Title/metadata only — no abstract retrieved.] The record claims necessary and sufficient no-arbitrage conditions for the SSVI/S3 volatility curve. It is included as a condition-level reference for the SSVI family, not as evidence of an implemented enforcement method.
- **Method & evidence:** Title claims necessary and sufficient conditions, but no abstract could be retrieved, so the result is unverified and recorded at title level only.
- **Method weaknesses:** Metadata-only preprint; the claimed necessity/sufficiency result is unverified at abstract level (read scope: abstract_only, abstract unavailable).
- **Comparability:** Not comparable: no abstract or result data available; preprint, not peer-reviewed.
- **Flags:** metadata-only

#### P8 - Barski & Wiśniewolski (2026)

**APA:** Barski, M., & Wiśniewolski, M. (2026). Implied volatility models without static arbitrage [Preprint]. *arXiv*. https://doi.org/10.48550/arxiv.2611.18937

- **Family:** Parametric construction | **Evidence status:** `proof` | **Abstract:** full (OpenAlex) | **Quality level:** VI | **Peer-reviewed:** no
- **Relevance:** Bridges dynamic surface models and static arbitrage: shows that plausible factor dynamics can carry positive arbitrage probability, and supplies conditions to remove it.
- **Key findings:** Derives explicit probabilities of calendar-spread, call-spread and butterfly arbitrage for Gaussian factor models, showing these probabilities are strictly positive under non-degeneracy. Develops a bounded-stochastic-factor framework with deterministic necessary and sufficient conditions (plus simpler sufficient conditions) for static arbitrage absence. Applies it to construct an arbitrage-free Jacobi-diffusion modification of the Cont–Vuletić model while preserving its empirical features.
- **Method & evidence:** Deterministic necessary and sufficient conditions are derived for bounded-factor models, and an arbitrage-free modification of an existing generative model is constructed.
- **Method weaknesses:** Preprint; the conditions are stated for bounded stochastic factors and the empirical preservation claim is not quantified in the abstract (read scope: abstract_only).
- **Comparability:** Theoretical results for factor models plus one model modification; not comparable with market-fit or generation-metric studies.

## 4.2 Penalty and constrained learning (n=6)

The six penalty/constrained-learning works trade guarantees for flexibility: soft penalties (N3, N4, N5), derivative-constrained losses (N6), architectural gates (N1) and operator learning (N2). N2's abstract is the most explicit ('adheres to critical no-arbitrage constraints'), N1 claims its architecture satisfies the constraints by construction, and N5's title already concedes that violations are only minimised. None of the abstracts reports a violation-rate distribution, so every entry here is a `numerical test`, not a guarantee, and the phase-3 synthesis must keep them in that bucket.

#### N1 - Cao et al. (2020)

**APA:** Cao, Y., Liu, X., & Zhai, J. (2020). Option valuation under no-arbitrage constraints with neural networks. *European Journal of Operational Research*, *293*(1), 361–374. https://doi.org/10.1016/j.ejor.2020.12.003

- **Family:** Penalty and constrained learning | **Evidence status:** `numerical test` | **Abstract:** full (Semantic Scholar) | **Quality level:** VI | **Peer-reviewed:** yes
- **Relevance:** Architectural/constraint-learning approach: enforcement lives in the network parameterisation rather than in a post-hoc projection.
- **Key findings:** Builds a hybrid gated neural network for option valuation that starts from no-arbitrage constraints: multiplicative hidden layers keep the model differentiable, and input-layer slopes and weights are selected to satisfy the constraints. A separate network predicts implied volatilities. On S&P 500 options the model is reported to outperform established alternatives in out-of-sample forecasting and hedging, attributed to better treatment of boundary options and analytic Greeks.
- **Method & evidence:** Constraints are imposed through the network structure (multiplicative hidden layers; slopes and weights selected to satisfy no-arbitrage) and evaluated empirically on S&P 500 options; no formal guarantee is claimed.
- **Method weaknesses:** Abstract-only; the constraint parameterisation is described but no violation audit is reported in the abstract (read scope: abstract_only).
- **Comparability:** S&P 500 options, forecasting/hedging metrics; not comparable with surface-fit or violation-rate metrics.

#### N2 - Wiedemann et al. (2025)

**APA:** Wiedemann, R., Jacquier, A., & Gonon, L. (2025). Operator deep smoothing for implied volatility. In *International Conference on Learning Representations (ICLR 2025)*. https://doi.org/10.48550/arxiv.2406.11520

- **Family:** Penalty and constrained learning | **Evidence status:** `numerical test` | **Abstract:** full (OpenAlex) | **Quality level:** VI | **Peer-reviewed:** yes
- **Relevance:** Tests whether a learned operator can replace instance-by-instance smoothing while respecting no-arbitrage constraints at scale.
- **Key findings:** Adapts a graph neural operator to map observed option data directly to smoothed implied-volatility surfaces, replacing instance-by-instance fitting with a single trained model. Evaluated on ten years of raw intraday S&P 500 options, the operator is reported to adhere to critical no-arbitrage constraints and to be robust to input subsampling. Benchmarks against classical neural networks and SVI are provided.
- **Method & evidence:** A single neural-operator model is trained on ten years of intraday S&P 500 options and reported to adhere to no-arbitrage constraints; the adherence is empirically evaluated, not proved.
- **Method weaknesses:** Abstract-only; which constraints are tested and at what tolerance is not visible, and the DOI resolves to the arXiv version of the ICLR paper (read scope: abstract_only).
- **Comparability:** S&P 500 intraday data; accuracy/robustness metrics are study-specific and not comparable with exact-construction guarantees.

#### N3 - Ackerer et al. (2019)

**APA:** Ackerer, D., Tagasovska, N., & Vatter, T. (2019). Deep smoothing of the implied volatility surface [Preprint]. *SSRN Electronic Journal*. https://doi.org/10.2139/ssrn.3402942

- **Family:** Penalty and constrained learning | **Evidence status:** `numerical test` | **Abstract:** full (OpenAlex) | **Quality level:** VI | **Peer-reviewed:** no
- **Relevance:** Canonical soft-penalty baseline, explicitly framed as a plug-in correction on classical IVS models.
- **Key findings:** Presents a neural-network approach to fitting and predicting implied-volatility surfaces with soft-constraint penalties intended to rule out arbitrage. The method is designed as a plug-in on top of standard IVS models, providing a correction when those models fail to replicate quotes, and is reported to be useful with sparse or erroneous data. The paper also quantifies prediction uncertainty in regions with few observations and studies network depth.
- **Method & evidence:** Arbitrage absence is pursued by penalising the loss with soft constraints; the paper reports empirical results but the penalty is not a guarantee.
- **Method weaknesses:** Preprint; the soft-constraint design cannot guarantee arbitrage absence and the abstract reports no violation rates (read scope: abstract_only).
- **Comparability:** No named market in the abstract; fit/generalisation metrics are not comparable with violation-rate studies.

#### N4 - Sidogi et al. (2022)

**APA:** Sidogi, T., Mongwe, W. T., Mbuvha, R., & Marwala, T. (2022). Creating synthetic volatility surfaces using generative adversarial networks with static arbitrage loss conditions. In *2022 IEEE Symposium Series on Computational Intelligence (SSCI)* (pp. 1423–1429). https://doi.org/10.1109/ssci51031.2022.10022219

- **Family:** Penalty and constrained learning | **Evidence status:** `numerical test` | **Abstract:** full (OpenAlex) | **Quality level:** VI | **Peer-reviewed:** yes
- **Relevance:** Penalty-augmented generation for a sparse index-option market; shows the penalty improves but is not a guarantee.
- **Key findings:** Proposes a data-driven GAN framework to generate synthetic volatility surfaces for the sparsely traded Johannesburg Stock Exchange All-share index (ALSI) options. Wasserstein distance against historical data is the performance metric, with a VAE benchmark; the vanilla GAN is reported to outperform the VAE. Incorporating static-arbitrage conditions during training improves the result even though the framework cannot directly learn the condition.
- **Method & evidence:** Static-arbitrage conditions enter as a loss term; the improvement is measured empirically and acknowledged as not directly learnable by the framework.
- **Method weaknesses:** Abstract-only; the residual arbitrage violation rate after the penalty is not reported (read scope: abstract_only).
- **Comparability:** ALSI (South African) index options; distributional metrics are market-specific and not comparable with SPX studies.

#### N5 - Na et al. (2023)

**APA:** Na, A., Zhang, M., & Wan, J. W. L. (2023). Computing volatility surfaces using generative adversarial networks with minimal arbitrage violations [Preprint]. *arXiv*. https://doi.org/10.48550/arxiv.2304.13128

- **Family:** Penalty and constrained learning | **Evidence status:** `numerical test` | **Abstract:** full (OpenAlex) | **Quality level:** VI | **Peer-reviewed:** no
- **Relevance:** Penalty-regularised GAN with a stated goal of minimal (not zero) arbitrage violations.
- **Key findings:** Proposes a GAN that learns volatility surfaces from training data while the generator is trained to satisfy no-arbitrage constraints through penalty terms used as regularisation. A discriminator checks whether generated volatility matches the target distribution, and shallow networks keep computational cost low. Experiments report better accuracy and runtime than ANN approaches for computing implied and local volatility surfaces.
- **Method & evidence:** No-arbitrage constraints are introduced as regularisation penalties; performance is compared numerically with ANN approaches, with violations minimised rather than eliminated.
- **Method weaknesses:** Preprint; the title itself concedes violations are only minimised, and the abstract gives no violation-rate distribution (read scope: abstract_only).
- **Comparability:** Benchmark against ANN/state-of-the-art; no named market in the abstract, so not comparable.

#### N6 - Hoshisashi et al. (2023)

**APA:** Hoshisashi, K., Phelan, C. E., & Barucca, P. (2023). No-arbitrage deep calibration for volatility smile and skewness [Preprint]. *arXiv*. https://doi.org/10.48550/arxiv.2310.16703

- **Family:** Penalty and constrained learning | **Evidence status:** `numerical test` | **Abstract:** full (OpenAlex) | **Quality level:** VI | **Peer-reviewed:** no
- **Relevance:** Penalty variant that targets the differential-inequality characterisation directly, including calendar-type terms.
- **Key findings:** Introduces a derivative-constrained neural network (DCNN), an MLP whose objective includes derivative terms, to generate a smooth surface satisfying no-arbitrage differential inequalities with respect to expiry and strike. Experiments train the model on prices generated by the SABR model to produce smile and skewness, and examine stability under different settings. The authors argue the derivative terms encode the necessary and sufficient no-arbitrage conditions.
- **Method & evidence:** A derivative-constrained network puts the no-arbitrage differential inequalities into the loss; numerical experiments on SABR-generated prices are reported.
- **Method weaknesses:** Preprint; the tests are synthetic and the abstract does not report violation rates away from training points (read scope: abstract_only).
- **Comparability:** Synthetic SABR-generated data; not comparable with market-data studies.

## 4.3 Projection and repair (n=9)

Projection/repair works restore admissibility after the fact: linear-program repairs inside bid-ask bounds (R1), entropic optimal transport (R2), construction-by-distortion (R3), joint call/put smoothing (R4), observation-anchored grid repair (R5), a strictly arbitrage-free non-parametric representation (R6), constrained Chebyshev bases with a post-fit correction (R7), transport-inspired surface transforms (R8) and Markov-chain approximations (R9). R1, R5 and R7 report explicit violation or coverage numbers; they are not comparable with each other because data, grid and tolerances differ. R2, R3 and R6 claim convergence or construction guarantees; R8 asserts arbitrage-freeness without a proof at abstract level.

#### R1 - Cohen et al. (2020)

**APA:** Cohen, S. N., Reisinger, C., & Wang, S. (2020). Detecting and repairing arbitrage in traded option prices. *Applied Mathematical Finance*, *27*(5), 345–373. https://doi.org/10.1080/1350486x.2020.1846573

- **Family:** Projection and repair | **Evidence status:** `numerical test` | **Abstract:** full (OpenAlex) | **Quality level:** VI | **Peer-reviewed:** yes
- **Relevance:** Canonical projection/repair method: minimal changes to prices within bid–ask bounds instead of smoothing or filtering.
- **Key findings:** Contrasts repair with arbitrage-free smoothing (changes nearly all data) and filtering (truncates data): the proposed method changes only what is necessary. The repair is a linear program that minimises price changes within bid–ask bounds subject to no-arbitrage constraints. Empirical studies report sparse perturbations, fast solution of large-scale problems, and improved calibration robustness and error after repair.
- **Method & evidence:** Repair is formulated as a linear program whose constraints are the no-arbitrage relations; empirical studies report sparse perturbations and improved calibration.
- **Method weaknesses:** Abstract-only; the precise arbitrage constraints and bid–ask data source are not specified in the abstract (read scope: abstract_only).
- **Comparability:** Traded option prices; calibration improvements are relative to the authors' setup and not comparable with surface-generation metrics.

#### R2 - De March & Henry-Labordère (2019)

**APA:** De March, H., & Henry-Labordère, P. (2019). Building arbitrage-free implied volatility: Sinkhorn's algorithm and variants [Preprint]. *SSRN Electronic Journal*. https://doi.org/10.2139/ssrn.3326486

- **Family:** Projection and repair | **Evidence status:** `proof` | **Abstract:** partial (Crossref) | **Quality level:** VI | **Peer-reviewed:** no
- **Relevance:** Projects bid–ask-consistent quotes onto an arbitrage-free surface via entropic optimal transport, with a convergence guarantee.
- **Key findings:** Formulates building an arbitrage-free implied-volatility surface from bid–ask quotes as a fast numerical procedure based on the Sinkhorn algorithm used for martingale optimal transport. The authors prove convergence of the procedure and present variants.
- **Method & evidence:** Convergence of the Sinkhorn-based numerical procedure is proved; the construction is a projection onto an arbitrage-free set.
- **Method weaknesses:** Preprint; abstract is partial (publisher-deposited snippet), so the precise constraint set and empirical performance are not visible (read scope: abstract_only, partial abstract).
- **Comparability:** No market data or fit metrics in the abstract; not comparable.
- **Flags:** partial-abstract

#### R3 - Bender & Thiel (2020)

**APA:** Bender, C., & Thiel, M. (2020). Arbitrage-free interpolation of call option prices. *Statistics & Risk Modeling*, *37*(1–2), 55–78. https://doi.org/10.1515/strm-2018-0026

- **Family:** Projection and repair | **Evidence status:** `proof` | **Abstract:** full (OpenAlex) | **Quality level:** VI | **Peer-reviewed:** yes
- **Relevance:** Construction-by-distortion: builds a smooth static-arbitrage-free curve per maturity and interpolates across maturities.
- **Key findings:** Introduces an interpolation method for call prices and implied volatilities in the strike dimension that first generates a smooth static-arbitrage-free implied-volatility curve, by distorting the call-price function of an arbitrage-free reference model. The method reproduces reference-model prices when market data are compatible with that model, and a full surface is obtained by one-dimensional interpolation per maturity followed by maturity interpolation. Kahalé's algorithm is recovered when Black–Scholes is the reference model.
- **Method & evidence:** Arbitrage-free interpolation follows by construction from distorting a reference arbitrage-free call-price function; Kahalé's algorithm appears as a special case.
- **Method weaknesses:** Abstract-only; the distortion construction's numerical stability is not discussed in the abstract (read scope: abstract_only).
- **Comparability:** Construction result; empirical performance is not reported in the abstract, so not comparable.

#### R4 - Yao et al. (2026)

**APA:** Yao, Y., Cui, Z., & Pan, Q. (2026). Joint arbitrage-free smoothing of American call and put options surfaces. *European Journal of Operational Research*, *336*(1), 388–404. https://doi.org/10.1016/j.ejor.2026.07.049

- **Family:** Projection and repair | **Evidence status:** `assumption` | **Abstract:** metadata-only (no abstract) | **Quality level:** VI | **Peer-reviewed:** yes
- **Relevance:** Extends repair/smoothing to American-style surfaces and to the joint call–put problem, a scope most static methods avoid.
- **Key findings:** [Title/metadata only — no abstract retrieved.] The title claims joint arbitrage-free smoothing of American call and put option surfaces. Included as a recent journal-level projection/smoothing work whose mechanism, data and results could not be checked.
- **Method & evidence:** No abstract available; the title claims joint arbitrage-free smoothing across calls and puts (American exercise), but the enforcement mechanism is unverified.
- **Method weaknesses:** Metadata-only record; enforcement construction and evidence cannot be assessed (read scope: abstract_only, abstract unavailable).
- **Comparability:** Not comparable: no abstract or result data available.
- **Flags:** metadata-only

#### R5 - Xiong & Liu (2026)

**APA:** Xiong, Y., & Liu, B. (2026). Observation-anchored arbitrage repair for sparse implied volatility surface completion. In *2026 IEEE Conference on Computational Intelligence for Financial Engineering & Economics (CIFEr)* (pp. 155–162). https://doi.org/10.1109/cifer67845.2026.11692406

- **Family:** Projection and repair | **Evidence status:** `numerical test` | **Abstract:** full (OpenAlex) | **Quality level:** VI | **Peer-reviewed:** yes
- **Relevance:** Separates completion from enforcement: repair is applied only to unobserved grid cells, after any backend.
- **Key findings:** Proposes a deterministic, observation-anchored two-step repair that enforces calendar constraints in total-variance space and butterfly constraints in normalised call-price space, modifying only unobserved grid cells. Evaluated on real SPX option data (OptionMetrics Ivy DB) over 252 out-of-sample days with five completion backends, calendar violation rates fall to near zero, while butterfly violations are reduced only partially, with an empirical floor around 5.4% attributed to finite-precision rounding. Cubic spline with repair achieves the lowest reconstruction error; repair and completion interact asymmetrically.
- **Method & evidence:** Deterministic post-hoc repair is evaluated on 252 out-of-sample SPX trading days across five completion backends; calendar violations fall to near zero, butterfly violations only partially.
- **Method weaknesses:** Abstract-only; the 5.4% butterfly floor is an empirical observation whose tolerance definition is not visible (read scope: abstract_only).
- **Comparability:** SPX/Ivy DB; violation rates depend on completion backends and tolerances, so not comparable with exact constructions.

#### R6 - Buehler et al. (2026)

**APA:** Buehler, H., Horvath, B. N., Kratsios, A., Limmer, Y., & Saqur, R. (2026). SANOS: Smooth strictly arbitrage-free non-parametric option surfaces [Preprint]. *arXiv*. https://doi.org/10.48550/arxiv.2601.11209

- **Family:** Projection and repair | **Evidence status:** `proof` | **Abstract:** full (OpenAlex) | **Quality level:** VI | **Peer-reviewed:** no
- **Relevance:** Non-parametric construction with a hard guarantee and low-dimensional optimisation; directly comparable in ambition to parametric SVI guarantees.
- **Key findings:** Presents a non-parametric construction of option price surfaces that are smooth and strictly arbitrage-free across time and strike, a smooth generalisation of linear interpolation. Calibration is a linear program that can incorporate bid–ask spreads through linear penalties or inequalities at materially lower cost than most IVS fitting routines. An equivalent parameterisation by strictly positive discrete local-volatility variables reduces the feasible set to positivity constraints; the approach is illustrated on S&P 500 index options.
- **Method & evidence:** Strict arbitrage-free smoothness is built into the representation; an equivalent strictly positive discrete-local-volatility parameterisation reduces constraints to positivity, with an LP calibration.
- **Method weaknesses:** Preprint; the strict-arbitrage-free proof is not visible at abstract level and the empirical illustration is not quantified (read scope: abstract_only).
- **Comparability:** S&P 500 illustration; computational-cost claims are not benchmarked in the abstract, so not comparable.

#### R7 - Alvarez (2025)

**APA:** Alvarez, R. J. (2025). Arbitrage-free option price surfaces via Chebyshev tensor bases and a Hamiltonian fog post-fit [Preprint]. *arXiv*. https://doi.org/10.48550/arxiv.2512.01967

- **Family:** Projection and repair | **Evidence status:** `numerical test` | **Abstract:** full (OpenAlex) | **Quality level:** VI | **Peer-reviewed:** no
- **Relevance:** Constrained-basis construction with explicit treatment of noisy/inconsistent quotes; quantifies residual violations instead of claiming exactness.
- **Key findings:** Represents the call-price surface in Chebyshev tensor bases on a warped log-moneyness/maturity rectangle, with static no-arbitrage requirements enforced as linear inequalities in a strictly convex quadratic program fitted to bid–ask bands. A local post-fit layer of risk-neutral-density 'fog' variables applies noise-aware corrections while preserving global static no-arbitrage. Reported inside-spread coverage is 98–99% in calm years with static violation rates below 1%; in stressed periods the fog allows controlled out-of-band leakage.
- **Method & evidence:** Static no-arbitrage is imposed as linear inequalities in a convex quadratic program; reported violation rates are below 1% rather than zero, and stressed periods allow controlled out-of-band leakage.
- **Method weaknesses:** Preprint; author metadata in OpenAlex is irregular ('Alvarez, Robert Jenkinson') and formatted as Alvarez, R. J.; the violation-rate measurement details are not in the abstract (read scope: abstract_only).
- **Comparability:** Equity option panels; violation percentages and coverage are study-specific and not comparable with exact-guarantee methods.
- **Flags:** author-string-irregular

#### R8 - Zetocha (2023)

**APA:** Zetocha, V. (2023). Volatility transformers: An optimal transport-inspired approach to arbitrage-free shaping of implied volatility surfaces [Preprint]. *SSRN Electronic Journal*. https://doi.org/10.2139/ssrn.4623940

- **Family:** Projection and repair | **Evidence status:** `assumption` | **Abstract:** full (Crossref) | **Quality level:** VI | **Peer-reviewed:** no
- **Relevance:** Frames enforcement as a transport map between surface distributions, covering extrapolation, skew changes and arbitrage removal.
- **Key findings:** Introduces a framework for arbitrage-free transformations of an implied-volatility surface based on optimal-transport maps between suitable distributions. Example tasks include time extrapolation, modification of skew or term structure, introduction of a market event, removal of arbitrage, and generation of surface dynamics. The authors position the approach as useful beyond volatility surfaces for synthetic market-data generation.
- **Method & evidence:** The abstract asserts arbitrage-free transformations based on optimal-transport maps but states neither a proof nor a numerical test.
- **Method weaknesses:** Preprint; the arbitrage-free property is claimed but no proof or test is reported at abstract level (read scope: abstract_only).
- **Comparability:** No market data or metrics in the abstract; not comparable.

#### R9 - Madan & Schoutens (2019)

**APA:** Madan, D. B., & Schoutens, W. (2019). Arbitrage free approximations to candidate volatility surface quotations. *Journal of Risk and Financial Management*, *12*(2), 69. https://doi.org/10.3390/jrfm12020069

- **Family:** Projection and repair | **Evidence status:** `numerical test` | **Abstract:** full (OpenAlex) | **Quality level:** VI | **Peer-reviewed:** yes
- **Relevance:** Model-free construction constrained to non-negative transition probabilities (hence arbitrage-free by construction), with an explicit speed caveat.
- **Key findings:** Argues that the growing breadth of traded strikes after 2008 complicates Fourier-inversion calibration and proposes continuous-time Markov-chain approximations instead. The approximations are reported as adequate, competitive and stable, though slow, and are general rather than restricted to independent-increment processes. Calibrations use 2,695 SPY options across 28 maturities as of 8 February 2018.
- **Method & evidence:** Continuous-time Markov-chain approximations are calibrated to quotes and illustrated on 2,695 SPY options; adequacy is empirical and the method is reported to be slow.
- **Method weaknesses:** Abstract-only; the arbitrage-free property of the chain approximation is asserted through the construction and not separately audited in the abstract (read scope: abstract_only).
- **Comparability:** SPY quotes on a single date; speed/accuracy claims are not comparable with other families' metrics.

## 4.4 Generation and filtering (n=8)

Generation works either sample inside a guaranteed-admissible parameter space (G1, G7, G8, and G6's architectural hard constraints) or train penalty-regularised generators (G2, G4, G5, N5). The guarantee, where it exists, is inherited from the parameterisation or architecture; penalty-based generators minimise violations without proving their absence. G5 is the most explicit about its empirical limit (90.8% of generated surfaces pass all tested static conditions), and G6 quantifies the accuracy cost of a hard guarantee. Dynamic arbitrage is not proved by any generator; the static constraints are applied surface by surface, including when surfaces are generated over time.

#### G1 - Ning et al. (2023)

**APA:** Ning, B., Jaimungal, S., Zhang, X., & Bergeron, M. (2023). Arbitrage-free implied volatility surface generation with variational autoencoders. *SIAM Journal on Financial Mathematics*, *14*(4), 1004–1027. https://doi.org/10.1137/21m1443546

- **Family:** Generation and filtering | **Evidence status:** `proof` | **Abstract:** full (OpenAlex) | **Quality level:** VI | **Peer-reviewed:** yes
- **Relevance:** Representative of 'generate in a guaranteed-admissible parameter space' rather than penalise violations.
- **Key findings:** Combines model-free VAEs with continuous-time SDE models (regime-switching and Lévy additive) by projecting historical surfaces onto the SDE parameter space and training the VAE on that parameter distribution. Arbitrage-free surfaces are generated by sampling latent states, decoding to SDE parameters and mapping them to IV surfaces. Conditional features are added and the method is presented as a data-augmentation tool for option-portfolio tail risk.
- **Method & evidence:** Arbitrage-freeness is inherited from the SDE model class: sampling generates parameters that map to arbitrage-free surfaces, so the guarantee is structural while generative quality is tested empirically.
- **Method weaknesses:** Abstract-only; the guarantee depends entirely on the chosen SDE classes and their calibration quality, which the abstract does not quantify (read scope: abstract_only).
- **Comparability:** Historical surfaces (market unspecified in abstract); generative out-of-sample metrics are not comparable with fit-based studies.

#### G2 - Vuletić & Cont (2024)

**APA:** Vuletić, M., & Cont, R. (2024). VolGAN: A generative model for arbitrage-free implied volatility surfaces. *Applied Mathematical Finance*, *31*(4), 203–238. https://doi.org/10.1080/1350486x.2025.2471317

- **Family:** Generation and filtering | **Evidence status:** `numerical test` | **Abstract:** full (OpenAlex) | **Quality level:** VI | **Peer-reviewed:** yes
- **Relevance:** Joint surface/underlying generator; shifts the evaluation target from static fit to dynamic realism and hedging.
- **Key findings:** Introduces VolGAN, trained on time series of implied-volatility surfaces and the underlying price, and capable of generating joint scenarios for surface and asset dynamics. On SPX data it is reported to learn the covariance structure of IV co-movements, reproduce non-Gaussian increments and time-varying correlations, and generate realistic VIX dynamics. The generated scenarios support data-driven hedging strategies that outperform Black–Scholes delta and delta–vega hedging.
- **Method & evidence:** Trained on SPX IV time series and evaluated through generated dynamics and hedging; the abstract does not specify the enforcement mechanism or a violation audit.
- **Method weaknesses:** Abstract-only; arbitrage-freeness is asserted in the title/abstract but the enforcement mechanism and violation rates are not described (read scope: abstract_only).
- **Comparability:** SPX; hedging-performance metrics are not comparable with arbitrage-violation or fit metrics.

#### G3 - Cont & Vuletić (2023)

**APA:** Cont, R., & Vuletić, M. (2023). Simulation of arbitrage-free implied volatility surfaces. *Applied Mathematical Finance*, *30*(2), 94–121. https://doi.org/10.1080/1350486x.2023.2277960

- **Family:** Generation and filtering | **Evidence status:** `assumption` | **Abstract:** partial (OpenAlex) | **Quality level:** VI | **Peer-reviewed:** yes
- **Relevance:** Dynamics-oriented generator; the partial record limits what can be claimed about enforcement.
- **Key findings:** Presents a computationally tractable method for simulating arbitrage-free implied-volatility surfaces, combinable with a data-driven model fitted to historical SPX implied volatilities. The approach is described as conciliating static arbitrage constraints with realistic statistical properties of IV co-movements. The retrieved abstract is partial, so the enforcement mechanism and validation are not visible.
- **Method & evidence:** Only a partial abstract was retrieved; it states that static constraints are reconciled with statistical properties but reports no proof or test detail.
- **Method weaknesses:** Partial abstract; enforcement and empirical validation cannot be assessed (read scope: abstract_only, partial abstract).
- **Comparability:** SPX historical data; no metrics available in the partial abstract, so not comparable.
- **Flags:** partial-abstract

#### G4 - Ginart Belmonte & Cole (2025)

**APA:** Ginart Belmonte, V., & Cole, T. (2025). Arbitrage-free implied volatility surface smoothing via generative adversarial networks. In *Proceedings of the ACM International Conference on AI in Finance (ICAIF)* (pp. 518–524). https://doi.org/10.1145/3768292.3771252

- **Family:** Generation and filtering | **Evidence status:** `numerical test` | **Abstract:** full (OpenAlex) | **Quality level:** VI | **Peer-reviewed:** yes
- **Relevance:** Learned projection/denoising: maps noisy arbitrage-violating surfaces to smooth arbitrage-free ones.
- **Key findings:** Proposes a GAN framework that smooths implied-volatility surfaces while enforcing arbitrage constraints, transforming noisy arbitrage-violating inputs into smooth arbitrage-free surfaces. The paper describes the architecture, synthetic noise generation and training strategy, and reports out-of-sample generalisation with lower mean squared error and runtime than traditional smoothing techniques.
- **Method & evidence:** A GAN denoiser is trained to output arbitrage-free surfaces and benchmarked on MSE/runtime against traditional smoothing; the claim is empirical.
- **Method weaknesses:** Abstract-only; the constraint mechanism and residual violation rate are not detailed (read scope: abstract_only).
- **Comparability:** No market named in the abstract; MSE/runtime comparisons are not comparable with violation-rate studies.

#### G5 - Bajalica et al. (2026)

**APA:** Bajalica, D., Brooks, O., & Ben Tahar, I. (2026). Latent flow matching for arbitrage-aware implied volatility surface generation. In *Proceedings of the ACM International Conference on AI in Finance (ICAIF)* (pp. 708–716). https://doi.org/10.1145/3858063.3858741

- **Family:** Generation and filtering | **Evidence status:** `numerical test` | **Abstract:** full (OpenAlex) | **Quality level:** VI | **Peer-reviewed:** yes
- **Relevance:** Penalty-based generation with an explicit, unusually honest satisfaction rate below 100%.
- **Key findings:** Compresses surfaces into a low-dimensional latent space using a VAE regularised by differentiable calendar-spread, call-spread and butterfly-arbitrage penalties, then trains a flow-matching model to transport a Gaussian prior to the empirical latent distribution. Evaluation uses Wasserstein distances, smile/skew diagnostics, quantile surfaces and static no-arbitrage tests. The model generates 90.8% of surfaces satisfying all tested static conditions while balancing distributional similarity and tail preservation.
- **Method & evidence:** Differentiable calendar-, call-spread- and butterfly-arbitrage penalties regularise a VAE latent space; evaluation reports 90.8% of generated surfaces satisfying all tested static conditions.
- **Method weaknesses:** Abstract-only; the 9.2% failure set and the tolerance used for the tests are not characterised (read scope: abstract_only).
- **Comparability:** Empirical surface distribution; the 90.8% satisfaction rate is not comparable with exact constructions or with studies using different tolerances.
- **Flags:** author-string-irregular

#### G6 - Anagha (2026)

**APA:** Anagha, S. (2026). Trainable hard constraints: Architectural enforcement of arbitrage-free implied volatility surfaces via automatic differentiation [Preprint]. *SSRN Electronic Journal*. https://doi.org/10.2139/ssrn.7577418

- **Family:** Generation and filtering | **Evidence status:** `proof` | **Abstract:** full (Crossref) | **Quality level:** VI | **Peer-reviewed:** no
- **Relevance:** Hard-constraint architecture, explicitly contrasted with parametric fits and soft penalties; reports the accuracy cost of the guarantee.
- **Key findings:** Builds convexity in log-moneyness and monotonicity in maturity directly into a neural total-variance surface through input-convex blocks gated by non-negative maturity ramps and output-scale calibration, keeping the network trainable by automatic differentiation. On synthetic rejection-sampled arbitrage-free SVI slices with Gaussian noise, the hard-constrained model records 0.00% convexity, Durrleman and calendar violations across 15 runs (tolerance 1e-4), versus soft-penalty and per-slice SVI baselines that violate. The guarantee costs accuracy: overall total-variance RMSE is higher than SSVI and the soft-penalty MLP.
- **Method & evidence:** Convexity in log-moneyness and monotonicity in maturity are guaranteed by the architecture; Durrleman's condition is audited empirically (0.00% violations on synthetic SVI data across 15 runs).
- **Method weaknesses:** Preprint; Durrleman's condition is only audited empirically, and the data are synthetic and well specified for SVI (read scope: abstract_only).
- **Comparability:** Synthetic SVI data, not market surfaces; RMSE comparisons across regimes are not comparable with market-fit studies.

#### G7 - Cohen et al. (2021)

**APA:** Cohen, S. N., Reisinger, C., & Wang, S. (2021). Arbitrage-free neural-SDE market models. *Applied Mathematical Finance*, *30*(1), 1–46. https://doi.org/10.1080/1350486x.2023.2257217

- **Family:** Generation and filtering | **Evidence status:** `proof` | **Abstract:** full (OpenAlex) | **Quality level:** VI | **Peer-reviewed:** yes
- **Relevance:** Dynamic SDE model whose admissible state space is exactly the static-arbitrage-free set; enforcement is architectural over time.
- **Key findings:** Develops a nonparametric model for the European options book that respects static (model-independent) arbitrage constraints and remains implementable. A state space of prices free from static arbitrage is derived, and neural networks approximate the drift and diffusion of the SDE system under constraints that preserve the no-arbitrage conditions. Methods to calibrate neural SDEs guaranteed to satisfy a set of linear inequalities are given and validated on data generated from a Heston stochastic local volatility model.
- **Method & evidence:** The neural networks are constrained so that the modelled price state satisfies the static no-arbitrage linear inequalities by construction; numerical experiments use Heston SLV-generated data.
- **Method weaknesses:** Abstract-only; the guarantee is for static arbitrage in the modelled state, not for dynamic (path-dependent) arbitrage beyond that state space (read scope: abstract_only).
- **Comparability:** Simulated Heston SLV data; calibration performance is not comparable with empirical market studies.

#### G8 - Yang et al. (2017)

**APA:** Yang, Y., Zheng, Y., & Hospedales, T. M. (2017). Gated neural networks for option pricing: Rationality by design. In *Proceedings of the AAAI Conference on Artificial Intelligence*, *31*(1). https://doi.org/10.1609/aaai.v31i1.10505

- **Family:** Generation and filtering | **Evidence status:** `proof` | **Abstract:** full (OpenAlex) | **Quality level:** VI | **Peer-reviewed:** yes
- **Relevance:** Early architectural-enforcement baseline: no-arbitrage encoded in network gates rather than penalised.
- **Key findings:** Introduces gated neural networks that learn to divide-and-conquer the pricing problem, then derives instantiations that are 'rational by design' by encoding a valid call-option surface enforcing no-arbitrage principles. The encoded inductive bias is reported to improve generalisation in pricing performance and to guarantee economically reasonable predictions, with the risk-neutral density available as a by-product.
- **Method & evidence:** The gated architecture is instantiated to encode a valid call-option surface satisfying no-arbitrage by design; pricing performance is evaluated empirically.
- **Method weaknesses:** Abstract-only; the specific set of enforced inequalities and the empirical violation checks are not detailed (read scope: abstract_only).
- **Comparability:** Pricing benchmarks; no surface-fit or violation-rate comparison in the abstract, so not comparable.

## 4.5 Constraint conditions and evaluation (n=5)

Constraint/evaluation works supply the condition vocabulary and the diagnostics the other families rely on: a review of static and dynamic conditions (C2, the only source that explicitly discusses dynamic arbitrage), a model-free static-arbitrage detector (C1), a path-dependent surface model whose static core is SSVI (C3), an asymptotic arbitrage-freeness result for BBR/SABR/rough-SABR formulas (C4), and a single-stock martingale-defect diagnostic (C5, scope-flagged). They are not construction methods, and their evidence status reflects that: proof for the two formal results, numerical test for the two empirical diagnostics, assumption for the narrative review.

#### C1 - Neufeld & Sester (2024)

**APA:** Neufeld, A., & Sester, J. (2024). Neural networks can detect model-free static arbitrage strategies. *Applied Mathematics & Optimization*, *90*(2), 41. https://doi.org/10.1007/s00245-024-10184-9

- **Family:** Constraint conditions and evaluation | **Evidence status:** `proof` | **Abstract:** full (Semantic Scholar) | **Quality level:** VI | **Peer-reviewed:** yes
- **Relevance:** Evaluation-side counterpart: provides a model-free test that a candidate surface admits static arbitrage.
- **Key findings:** Shows theoretically and numerically that neural networks can detect model-free static arbitrage opportunities whenever the market admits them, including markets with many traded securities. The key technical result is that a single neural network can approximately solve a class of convex semi-infinite programs; examples on real financial data demonstrate tractability and robustness.
- **Method & evidence:** Theoretical detection guarantee plus numerical examples on real financial data; this is a diagnostic, not a construction method.
- **Method weaknesses:** Abstract-only; detection guarantees depend on optimisation tolerances that the abstract does not discuss (read scope: abstract_only).
- **Comparability:** Detection task, not construction; results are not comparable with enforcement methods.

#### C2 - Niu (2015)

**APA:** Niu, Q. (2015). No arbitrage conditions and characters of implied volatility surface: A review for implied volatility modelers [Preprint]. *SSRN Electronic Journal*. https://doi.org/10.2139/ssrn.2672416

- **Family:** Constraint conditions and evaluation | **Evidence status:** `assumption` | **Abstract:** full (Crossref) | **Quality level:** VII | **Peer-reviewed:** no
- **Relevance:** Maps the condition space (static and dynamic) that construction methods are supposed to satisfy.
- **Key findings:** Reviews no-arbitrage restrictions on the implied-volatility surface and the relationships among conditions derived under different assumptions, motivated by modelers avoiding wrong models. Introduces general properties, presents sufficient and close-to-necessary conditions for no static arbitrage, and discusses no dynamic arbitrage. Recommends checking a final group of conditions that implies the other necessary conditions when building models.
- **Method & evidence:** A narrative review of conditions from the literature; it asserts no original proof or test of its own at abstract level.
- **Method weaknesses:** Review preprint; no reproducible search protocol is stated, and the condition claims are not independently checked (read scope: abstract_only).
- **Comparability:** Review; condition synthesis depends on cited works not inspected here, so not comparable.

#### C3 - Andrès et al. (2026)

**APA:** Andrès, H., Boumezoued, A., & Jourdain, B. (2026). The implied volatility surface (also) is path-dependent. *Quantitative Finance*, *26*(7), 1017–1047. https://doi.org/10.1080/14697688.2026.2637739

- **Family:** Constraint conditions and evaluation | **Evidence status:** `proof` | **Abstract:** full (OpenAlex) | **Quality level:** VI | **Peer-reviewed:** yes
- **Relevance:** Dynamic surface model that keeps an explicit static-arbitrage-free parametric core while adding path dependence.
- **Key findings:** Studies how vanilla implied volatility can be predicted from the past trajectory of the underlying and finds that a large part of ATM-forward IV movements (up to two years) is explained by past returns and their squares, with the feedback weakening at longer maturities. Fits a four-parameter SSVI surface and shows the two ATM-forward parameters are path-dependent. Proposes a joint model of surface and underlying using a path-dependent volatility model plus Ornstein–Uhlenbeck and Jacobi processes, producing realistic IV surface paths free from static arbitrage.
- **Method & evidence:** The simulated surface is constructed from a parsimonious SSVI parameterisation with Jacobi-driven parameters, so static arbitrage-freeness follows by construction; the path-dependence evidence is empirical.
- **Method weaknesses:** Abstract-only; dynamic (calendar) consistency over the simulated paths is not discussed beyond static arbitrage-freeness (read scope: abstract_only).
- **Comparability:** SPX/VIX-style equity-index evidence; the specific four-parameter SSVI restriction limits comparability with flexible-surface methods.

#### C4 - Fukasawa (2022)

**APA:** Fukasawa, M. (2022). On asymptotically arbitrage-free approximations of the implied volatility. *Frontiers of Mathematical Finance*, *1*(4), 525–537. https://doi.org/10.3934/fmf.2022006

- **Family:** Constraint conditions and evaluation | **Evidence status:** `proof` | **Abstract:** partial (OpenAlex) | **Quality level:** VI | **Peer-reviewed:** yes
- **Relevance:** Explains why widely used explicit smile formulas are only asymptotically arbitrage-free, a key limitation for parametric enforcement.
- **Key findings:** Following Fukasawa and Gatheral (2022), proves that the BBF formula, the SABR formula and the rough SABR formula provide asymptotically arbitrage-free approximations of implied volatility under, respectively, the local volatility model, the SABR model and the rough SABR model. The result is asymptotic rather than finite-strike, so it delimits the regime in which these parametric formulas can be treated as arbitrage-free.
- **Method & evidence:** Proves that the BBF, SABR and rough SABR formulas give asymptotically arbitrage-free approximations under the corresponding models.
- **Method weaknesses:** Abstract-only; the asymptotic regime and error bounds are not detailed in the abstract (read scope: abstract_only).
- **Comparability:** Asymptotic result; not comparable with finite-strike numerical violation studies.

#### C5 - Stahl & Blauth (2024)

**APA:** Stahl, P., & Blauth, J. (2024). Martingale defects in the volatility surface and bubble conditions in the underlying. *Review of Derivatives Research*, *27*(1), 85–111. https://doi.org/10.1007/s11147-023-09200-x

- **Family:** Constraint conditions and evaluation | **Evidence status:** `numerical test` | **Abstract:** full (OpenAlex) | **Quality level:** VI | **Peer-reviewed:** yes
- **Relevance:** Dynamic-arbitrage-adjacent diagnostic: links surface-implied martingale defects to bubble conditions in the underlying.
- **Key findings:** Builds on the result that the SABR model is a strict local martingale when its parameterisation implies positive correlation between stock and option prices, and operationalises martingale-defect conditions as bubble indicators. Analyses 2,576 stocks over 26 years: defects are absorbed quickly by options markets but identify permanent distributional changes, option activity, short interest and institutional ownership patterns. Defects cluster in periods of positive market development and are rare in corrections.
- **Method & evidence:** Operationalises SABR strict-local-martingale conditions and tests them on 2,576 stocks over 26 years; the evidence is empirical.
- **Method weaknesses:** Abstract-only; the SABR-based defect test is model-dependent and the single-stock panel does not directly evidence index-surface behaviour (read scope: abstract_only).
- **Comparability:** Single-stock panel, not equity-index surfaces; the empirical setting is out of the index scope and is flagged as such.
- **Flags:** scope-flag: single-stock panel

## 4.6 Seminal pre-2015 baselines (n=5)

The five pre-2015 baselines anchor the lineage: SVI calibration (S1), shape-constrained smoothing (S2), SABR density correction (S3), nonparametric inversion (S4) and a dynamic factor model (S5). S1 and S2 are directly relevant enforcement constructions; S3 shows that an explicit smile formula can be arbitrageable in finite strike, which is the tension that C4 later resolves asymptotically; S4 and S5 are pre-constraint baselines and are used only to frame what enforcement added. Currency is not penalised for these records because their role is foundational, not current-best-practice.

#### S1 - Gatheral & Jacquier (2013)

**APA:** Gatheral, J., & Jacquier, A. (2013). Arbitrage-free SVI volatility surfaces. *Quantitative Finance*, *14*(1), 59–71. https://doi.org/10.1080/14697688.2013.819986

- **Family:** Seminal pre-2015 baselines | **Evidence status:** `proof` | **Abstract:** partial (OpenAlex) | **Quality level:** VI | **Peer-reviewed:** yes
- **Relevance:** The reference parametric construction that later SVI/SSVI enforcement work extends or repairs.
- **Key findings:** Shows how to calibrate the widely used SVI parameterisation so that the absence of static arbitrage is guaranteed, exhibiting a large class of arbitrage-free SVI surfaces with a simple closed-form representation. Demonstrates high-quality SVI fits with a numerical example using recent SPX options data.
- **Method & evidence:** Exhibits a large class of SVI surfaces with a closed-form representation that guarantees absence of static arbitrage; a numerical SPX example demonstrates fit quality.
- **Method weaknesses:** Seminal baseline; conditions are sufficient for the SVI class rather than necessary, and later work (Martini & Mingone, 2022) completes the characterisation (read scope: abstract_only, partial abstract).
- **Comparability:** SPX fit example; fit quality is reported for context, not comparable with later methods' metrics.
- **Flags:** seminal, partial-abstract

#### S2 - Fengler (2009)

**APA:** Fengler, M. R. (2009). Arbitrage-free smoothing of the implied volatility surface. *Quantitative Finance*, *9*(4), 417–428. https://doi.org/10.1080/14697680802595585

- **Family:** Seminal pre-2015 baselines | **Evidence status:** `numerical test` | **Abstract:** full (OpenAlex) | **Quality level:** VI | **Peer-reviewed:** yes
- **Relevance:** Foundational constrained-smoothing baseline; frames the cost of non-arbitrage-free inputs (negative transition probabilities).
- **Key findings:** Argues that pricing accuracy of local-volatility models depends on an arbitrage-free implied-volatility surface, since a violating input can produce negative transition probabilities, mispricings and false Greeks. Proposes smoothing the implied-volatility smile in an arbitrage-free way using natural smoothing splines under suitable shape constraints, presented as simple, computationally cheap and well founded.
- **Method & evidence:** Proposes shape-constrained natural smoothing splines that produce arbitrage-free smiles; the justification is methodological and the evidence empirical.
- **Method weaknesses:** Seminal baseline; the shape constraints and their finite-sample behaviour are not detailed at abstract level (read scope: abstract_only).
- **Comparability:** Methodological baseline; no market results are given in the abstract, so not comparable.
- **Flags:** seminal

#### S3 - Hagan et al. (2014)

**APA:** Hagan, P. S., Kumar, D., Lesniewski, A. S., & Woodward, D. E. (2014). Arbitrage-free SABR. *Wilmott*, *2014*(69), 60–75. https://doi.org/10.1002/wilm.10290

- **Family:** Seminal pre-2015 baselines | **Evidence status:** `numerical test` | **Abstract:** full (OpenAlex) | **Quality level:** VI | **Peer-reviewed:** no
- **Relevance:** Shows that the popular explicit SABR formula itself can generate arbitrage at low strikes, and repairs it through the model's density.
- **Key findings:** Notes that the explicit SABR implied-volatility formulas are asymptotic and can produce arbitrage for low-strike options. Uses asymptotic techniques to reduce the two-dimensional SABR model to a one-dimensional forward equation for the probability density, solved numerically to obtain arbitrage-free option prices. The resulting implied volatilities closely match the explicit curves except at a very low-rate boundary layer, and a shifted-Fβ variant accommodates negative rates.
- **Method & evidence:** Replaces the asymptotic SABR implied-volatility formula with a numerically solved one-dimensional PDE for the density, yielding arbitrage-free prices; evidence is numerical.
- **Method weaknesses:** Practitioner magazine (editorially reviewed, not peer-reviewed); the numerical density solution's discretisation error is not discussed at abstract level (read scope: abstract_only).
- **Comparability:** Density-based model prices; not comparable with market-surface fit studies.
- **Flags:** seminal, not-peer-reviewed-outlet

#### S4 - Bodurtha & Jermakyan (1999)

**APA:** Bodurtha, J. N., & Jermakyan, M. (1999). Nonparametric estimation of an implied volatility surface. *The Journal of Computational Finance*, *2*(4), 29–60. https://doi.org/10.21314/jcf.1999.034

- **Family:** Seminal pre-2015 baselines | **Evidence status:** `assumption` | **Abstract:** full (OpenAlex) | **Quality level:** VI | **Peer-reviewed:** yes
- **Relevance:** Seminal nonparametric construction baseline, illustrating that early surface estimation did not enforce arbitrage constraints explicitly.
- **Key findings:** Given diffusion-based pricing assumptions and European option quotes, identifies a unique and stable set of diffusion coefficients by inverting option prices into a state- and time-dependent volatility function. The approach uses a small-parameter expansion and a finite-difference procedure building on Tikhonov-style integral-equation treatments, with an implementation on CBOE S&P 500 option data.
- **Method & evidence:** Abstract describes a finite-difference inversion of option prices into a state- and time-dependent volatility function; no explicit no-arbitrage enforcement is stated.
- **Method weaknesses:** Seminal baseline; the abstract makes no no-arbitrage enforcement claim, so its evidence status is assumption rather than proof or test (read scope: abstract_only).
- **Comparability:** CBOE S&P 500 data (1990s); dated and not comparable with modern violation-rate studies.
- **Flags:** seminal

#### S5 - Fengler et al. (2006)

**APA:** Fengler, M. R., Härdle, W. K., & Mammen, E. (2006). A semiparametric factor model for implied volatility surface dynamics. *Journal of Financial Econometrics*, *5*(2), 189–218. https://doi.org/10.1093/jjfinec/nbm005

- **Family:** Seminal pre-2015 baselines | **Evidence status:** `assumption` | **Abstract:** full (OpenAlex) | **Quality level:** VI | **Peer-reviewed:** yes
- **Relevance:** Seminal dynamic factor baseline for surface modelling, useful to show that statistical surface models historically did not enforce arbitrage.
- **Key findings:** Proposes a semiparametric factor model that approximates the implied-volatility surface in a finite-dimensional function space, tailored to the degenerate design of IVS data by fitting only in local neighbourhoods of design points and exploiting the expiry effect. Using DAX index option data, estimates nonparametric components and a low-dimensional latent factor time series, completed with vector autoregressive dynamics.
- **Method & evidence:** Abstract describes a semiparametric factor approximation and VAR dynamics; no no-arbitrage constraint is stated.
- **Method weaknesses:** Seminal baseline; abstract states no arbitrage-enforcement mechanism (read scope: abstract_only).
- **Comparability:** DAX index options; dated, and not comparable with modern constraint-focused studies.
- **Flags:** seminal

## 5. Coverage-distribution advisory

No single method family exceeds 70% of the corpus, so the family distribution does not trigger the distributional-skew rule on its own. The time distribution is the skew that matters: 20 of 41 sources (49%) are from 2023-2026 and only 5 are pre-2015, the latter by design (seminal baselines). This is a recency skew inherent to the search ranking plus the fast growth of ML-based surface methods; it is not evidence that older enforcement methods stopped working. Non-seminal sources older than five years at the search date (2020 or earlier): 11 / 41 (26.8%), within the <=30% guidance.

**Data provenance skew.** Of the 12 sources whose abstracts name a market that is not a simulation, 10 use US equity-index data (SPX/SPY/CBOE S&P 500) and 2 use non-US indices (DAX, JSE ALSI). US index data therefore account for about 83% of the known provenance, which crosses the 70% advisory threshold. Consequences: violation-rate and fit numbers in this corpus should not be read as field-wide properties, and evidence about non-US index surfaces is thin (one German study, DAX 2006; one South African study, JSE ALSI 2022). Geographic distribution of authors and venues was not collected, so no author-country skew is claimed.

**Venue-type skew.** Preprints are 26.8% (11/41), just inside the 30% ceiling, but they carry a disproportionate share of the most recent (2025-2026) evidence: 6 of the 11 preprints are from 2025-2026. The synthesis should therefore treat recent-generation claims as provisional until peer review.

## 6. Evidence-status ledger (Devil's Advocate fix 1)

Every source is listed with what it actually establishes at abstract level and what would be needed before its claim could be called arbitrage-free.

| ID | Enforcement mechanism (abstract) | Status | What would upgrade it |
|---|---|---|---|
| P1 | Parametrisation / parameter-domain restriction | proof | Full-text theorem check (abstract-only here) |
| P2 | Parametrisation / parameter-domain restriction | proof | Full-text theorem check (abstract-only here) |
| P3 | Parametrisation / parameter-domain restriction | proof | Full-text theorem check (abstract-only here) |
| P4 | Parametrisation / parameter-domain restriction | assumption | Retrieve the abstract/full text and identify a proof or a test |
| P5 | Parametrisation / parameter-domain restriction | proof | Full-text theorem check (abstract-only here) |
| P6 | Parametrisation / parameter-domain restriction | proof | Full-text theorem check (abstract-only here) |
| P7 | Parametrisation / parameter-domain restriction | assumption | Retrieve the abstract/full text and identify a proof or a test |
| P8 | Parametrisation / parameter-domain restriction | proof | Full-text theorem check (abstract-only here) |
| N1 | Penalty, constraint loss or architectural gate | numerical test | Explicit violation audit with tolerance and independent replication |
| N2 | Penalty, constraint loss or architectural gate | numerical test | Explicit violation audit with tolerance and independent replication |
| N3 | Penalty, constraint loss or architectural gate | numerical test | Explicit violation audit with tolerance and independent replication |
| N4 | Penalty, constraint loss or architectural gate | numerical test | Explicit violation audit with tolerance and independent replication |
| N5 | Penalty, constraint loss or architectural gate | numerical test | Explicit violation audit with tolerance and independent replication |
| N6 | Penalty, constraint loss or architectural gate | numerical test | Explicit violation audit with tolerance and independent replication |
| R1 | Post-hoc projection, repair or constrained construction | numerical test | Explicit violation audit with tolerance and independent replication |
| R2 | Post-hoc projection, repair or constrained construction | proof | Full-text theorem check (abstract-only here) |
| R3 | Post-hoc projection, repair or constrained construction | proof | Full-text theorem check (abstract-only here) |
| R4 | Post-hoc projection, repair or constrained construction | assumption | Retrieve the abstract/full text and identify a proof or a test |
| R5 | Post-hoc projection, repair or constrained construction | numerical test | Explicit violation audit with tolerance and independent replication |
| R6 | Post-hoc projection, repair or constrained construction | proof | Full-text theorem check (abstract-only here) |
| R7 | Post-hoc projection, repair or constrained construction | numerical test | Explicit violation audit with tolerance and independent replication |
| R8 | Post-hoc projection, repair or constrained construction | assumption | Retrieve the abstract/full text and identify a proof or a test |
| R9 | Post-hoc projection, repair or constrained construction | numerical test | Explicit violation audit with tolerance and independent replication |
| G1 | Guaranteed parameter space or penalty-regularised generator | proof | Full-text theorem check (abstract-only here) |
| G2 | Guaranteed parameter space or penalty-regularised generator | numerical test | Explicit violation audit with tolerance and independent replication |
| G3 | Guaranteed parameter space or penalty-regularised generator | assumption | Retrieve the abstract/full text and identify a proof or a test |
| G4 | Guaranteed parameter space or penalty-regularised generator | numerical test | Explicit violation audit with tolerance and independent replication |
| G5 | Guaranteed parameter space or penalty-regularised generator | numerical test | Explicit violation audit with tolerance and independent replication |
| G6 | Guaranteed parameter space or penalty-regularised generator | proof | Full-text theorem check (abstract-only here) |
| G7 | Guaranteed parameter space or penalty-regularised generator | proof | Full-text theorem check (abstract-only here) |
| G8 | Guaranteed parameter space or penalty-regularised generator | proof | Full-text theorem check (abstract-only here) |
| C1 | Condition statement or diagnostic | proof | Full-text theorem check (abstract-only here) |
| C2 | Condition statement or diagnostic | assumption | Retrieve the abstract/full text and identify a proof or a test |
| C3 | Condition statement or diagnostic | proof | Full-text theorem check (abstract-only here) |
| C4 | Condition statement or diagnostic | proof | Full-text theorem check (abstract-only here) |
| C5 | Condition statement or diagnostic | numerical test | Explicit violation audit with tolerance and independent replication |
| S1 | Baseline construction | proof | Full-text theorem check (abstract-only here) |
| S2 | Baseline construction | numerical test | Explicit violation audit with tolerance and independent replication |
| S3 | Baseline construction | numerical test | Explicit violation audit with tolerance and independent replication |
| S4 | Baseline construction | assumption | Retrieve the abstract/full text and identify a proof or a test |
| S5 | Baseline construction | assumption | Retrieve the abstract/full text and identify a proof or a test |

For the three metadata-only records (P4, P7, R4) the ledger status is `assumption` even where the title asserts a result; the TITLE is not evidence. For the four partial-abstract records (R2, G3, C4, S1) claims are limited to what the retrieved fragment states.

## 7. Comparability flags (Devil's Advocate fix 2)

The corpus uses the words 'arbitrage', 'violation' and 'fit' with different operational meanings. The following buckets are `reported for context, not comparable`:

- **Violation-rate bucket** (G6 synthetic SVI, tolerance 1e-4; G5 generated surfaces, all-tested-conditions pass rate; R5 SPX grid completion, butterfly floor about 5.4%; R7 equity panels, <1% with 98-99% inside spread). Different data, grids and tolerances; no ranking is implied.
- **Fit / forecasting / hedging bucket** (N1 out-of-sample forecasting and hedging; N2 accuracy and subsampling robustness; G2 hedging performance; R9 speed/adequacy; N4 Wasserstein distance to historical surfaces). These are not arbitrage metrics.
- **Exact-construction bucket** (P1, P2, P3, P5, P6, R2, R3, R6, G1, G7, G8, S1, C4). A guarantee is claimed by construction; no comparative metric is reported, so no cross-family comparison is possible.
- **Not evaluable bucket** (P4, P7, R4): metadata only.

## 8. Selection and recency guard (Devil's Advocate fix 3)

- The corpus is fresh (OpenAlex, 31 queries, 430 unique records) and does not reuse the previous example's 40 sources; overlap is incidental, not imported.
- Classical parametric baselines are deliberately over-sampled against the recency ranking: 5 pre-2015 seminal works plus the full 2015-2026 SVI/SSVI/SABR line.
- Every excluded candidate has a reason code or is counted in a documented bucket; the 40 `RELEVANT_NOT_SELECTED` records are disclosed rather than hidden.
- Preprints are capped under 30% and individually flagged; metadata-only records are flagged at every citation point.
- No citation counts are reported anywhere in these artifacts, because they were not used for selection or evaluation and would invite a spurious quality ranking.

## 9. Abstract-level method notes

This bibliography reflects what abstracts state, not what full texts show. Method weaknesses are therefore limited to: missing enforcement guarantees, missing data or tolerance detail, absent comparison baselines, and preprint status. Any inferential weakness (e.g. selection effects inside a study, robustness of a numerical scheme) is recorded as `not assessed (read scope: abstract_only)` rather than guessed.
