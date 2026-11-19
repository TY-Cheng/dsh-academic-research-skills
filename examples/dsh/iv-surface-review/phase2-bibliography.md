# Phase 2 — Annotated Bibliography

**Review:** Arbitrage-Free Implied Volatility Surface Construction: A Structured Literature Review of Parametric, Nonparametric, and Neural Approaches

**Stage:** `deep-research` full, Phase 2 (bibliography + source verification). **Date:** 2026-11-19 (Asia/Singapore).

**Review-form note:** the author's reply “确认” kept the current work; no separate review form was selected. This is a structured literature review in `deep-research` full mode. It is **not** claimed to be a PRISMA-compliant systematic review, and no PRISMA/PRISMA-ScR compliance is asserted.

## 1. Search Strategy

### Databases and tools

| Source | Role | Result |
|---|---|---|
| OpenAlex | Primary discovery, full-text search | 24 queries × 25 records; 351 unique after DOI/title dedup |
| Crossref | Metadata, DOI, abstract cross-check | 10 targeted lookups; 4 abstracts recovered; one HTTP 429 |
| Semantic Scholar | Title/DOI verification and abstract fill | 10 requests; all HTTP 429; no data returned |
| arXiv / SSRN / publisher pages | Spot checks for missing abstracts | 5 snippets/abstracts recovered; 1 still unavailable |

No Web of Science, Scopus, or institutional database access was available. No full text was read; assessment is metadata/abstract-level.

### Keywords and Boolean logic

The 24 OpenAlex full-text queries are recorded verbatim in `search/openalex_search.py`. The conceptual Boolean string was:

```text
("implied volatility surface" OR "volatility surface")
AND ("arbitrage-free" OR "no-arbitrage" OR "static arbitrage"
     OR "calendar arbitrage" OR "butterfly arbitrage")
AND ("SVI" OR "SSVI" OR "parametric" OR "nonparametric"
     OR "neural network" OR "deep learning" OR "generative"
     OR "Gaussian process")
```

### Date range and last search

- **Date range:** 2015-01-01 to 2026-11-19; pre-2015 seminal works were admitted only when they define a construction or constraint used by later work (Gatheral & Jacquier, 2014; Fengler, 2009; Homescu, 2011).
- **Last searched:** 2026-11-19 (Asia/Singapore).

### Inclusion and exclusion

**Included:** equity-index/option implied-volatility-surface construction; static or dynamic no-arbitrage constraints; parametric, nonparametric, neural, or generative methods; evaluation/repair of arbitrage; English-language; 2015–2026 or explicitly seminal; peer-reviewed articles/conference papers or credible preprints.

**Excluded:** pure option-pricing papers with no surface construction; local/stochastic-volatility calibration with no surface/arbitrage contribution; crypto/FX applications unless the method is directly transferable; practitioner blogs, vendor notes, and non-reproducible commentary; papers with no arbitrage or surface-construction focus.

### Coverage distribution advisory

- **Size:** 40 sources (target 30–50). **Peer-reviewed:** 30/40 (75.0%) — above the 60% floor. **Preprints:** 10/40 (25.0%).
- **Currency:** 28/40 (70.0%) from 2021–2026; 12/40 (30.0%) pre-2021 — at the 30% cap, including seminal pre-2015 work. No currency advisory is triggered.
- **Method mix:** neural/generative 18/40 (45%), constraints/evaluation 8/40 (20%), parametric 7/40 (17.5%), nonparametric 6/40 (15%), dynamics 1/40 (2.5%). No single method exceeds 70%.
- **Market/data concentration:** the empirical corpus is SPX/US-equity-index heavy; several neural papers use simulated or synthetic surfaces. Cross-market and non-US evidence is limited; the synthesis must not treat SPX results as universal.

## 2. Screening Flow (PRISMA-style; not a PRISMA-compliant review)

```text
Records identified via OpenAlex (24 queries × 25)          351
  duplicates removed (DOI/title)                             0 (dedup already applied)
Unique records screened at title/abstract                  351
  not advanced (off-topic, duplicate, no surface/arbitrage,  311
  non-English, outside scope)
Full-text assessed                                            0
Metadata/abstract assessed                                   40
  excluded at metadata/abstract stage                          0
Included in the annotated corpus                             40
  peer-reviewed                                              30
  preprints                                                  10
```

The 40 included records were selected from the ranked candidate pool; the remaining 311 were not advanced. No full-text screening was performed, so this flow is **not** a PRISMA-compliant identification/screening record.

## 3. Annotated Sources (N=40)

Each entry gives the APA 7.0 citation, relevance to the RQ, abstract-level key findings, an evidence level (I–VII), and a method-weakness note following the #916 checklist. “Abstract-only” means the full text was not read; “reader-inferred” marks a weakness the authors did not acknowledge.

### 3.1 Parametric surfaces (7)

#### [P1] Gatheral & Jacquier (2014)

**Citation.** Gatheral, J., & Jacquier, A. (2014). Arbitrage-free SVI volatility surfaces. *Quantitative Finance*. https://doi.org/10.1080/14697688.2013.819986

**Relevance.** Parametric construction/calibration with explicit arbitrage control; a direct benchmark for the static no-arbitrage constraints in the RQ.

**Key findings (abstract-level).** In this article, we show how to calibrate the widely used SVI parameterization of the implied volatility smile in such a way as to guarantee the absence of static arbitrage. In particular, we exhibit a large class of arbitrage-free SVI volatility surfaces with a simple closed-form representation. We demonstrate the high quality of typical SVI fits with a numerical example using recent SPX options data.

**Quality.** Level VI (single empirical study; peer-reviewed).

**Method weakness.** Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

#### [P2] Guo et al. (2016)

**Citation.** Guo, G., Jacquier, A., Martini, C., & Neufcourt, L. (2016). Generalized Arbitrage-Free SVI Volatility Surfaces. *SIAM Journal on Financial Mathematics*. https://doi.org/10.1137/120900320

**Relevance.** Parametric construction/calibration with explicit arbitrage control; a direct benchmark for the static no-arbitrage constraints in the RQ.

**Key findings (abstract-level).** Generalizes the arbitrage-free SVI construction to a broader class of surfaces, formalizes arbitrage freeness using Roger Lee's moment formula and Roper's analysis, and exhibits an arbitrage-free surface outside Gatheral's SVI family.

**Quality.** Level VI (single empirical study; peer-reviewed).

**Method weakness.** Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

#### [P3] Fengler (2009)

**Citation.** Fengler, M. R. (2009). Arbitrage-free smoothing of the implied volatility surface. *Quantitative Finance*. https://doi.org/10.1080/14697680802595585

**Relevance.** Parametric construction/calibration with explicit arbitrage control; a direct benchmark for the static no-arbitrage constraints in the RQ.

**Key findings (abstract-level).** The pricing accuracy and pricing performance of local volatility models depends on the absence of arbitrage in the implied volatility surface. An input implied volatility surface that is not arbitrage-free can result in negative transition probabilities and consequently mispricings and false greeks. We propose an approach for smoothing the implied volatility smile in an arbitrage-free way.

**Quality.** Level VI (single empirical study; peer-reviewed).

**Method weakness.** Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

#### [P4] Homescu (2011)

**Citation.** Homescu, C. (2011). Implied Volatility Surface: Construction Methodologies and Characteristics. *arXiv*. https://doi.org/10.48550/arxiv.1107.1834

**Relevance.** Parametric construction/calibration with explicit arbitrage control; a direct benchmark for the static no-arbitrage constraints in the RQ.

**Key findings (abstract-level).** Surveys IVS construction methodologies, including arbitrage-free conditions in strike and time, extrapolation, calibration choices, dynamics, and asymptotics.

**Quality.** Level VII (narrative review/survey; preprint).

**Method weakness.** Preprint (not peer-reviewed). Narrative review/survey, not a systematic review; coverage/selection rules are not reproducible; the abstract does not state a systematic search (reader-inferred); absence of a cited study is bounded by coverage; checklist (fit, arbitrage, dynamics, OOS, cost) is narrative; full text not read.

#### [P5] Zaugg et al. (2025)

**Citation.** Zaugg, N. F., Perotti, L., & Grzelak, L. A. (2025). Volatility Parametrizations with Random Coefficients: Analytic Flexibility for Implied Volatility Surfaces. *SIAM Journal on Financial Mathematics*. https://doi.org/10.1137/24m1713107

**Relevance.** Parametric construction/calibration with explicit arbitrage control; a direct benchmark for the static no-arbitrage constraints in the RQ.

**Key findings (abstract-level).** Proposes volatility parametrizations with random coefficients, combining model-inspired structure with additional analytic flexibility; directly relevant to the parametric-versus-flexibility trade-off.

**Quality.** Level VI (single empirical study; peer-reviewed).

**Method weakness.** Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

#### [P6] Martini & Mingone (2022)

**Citation.** Martini, C., & Mingone, A. (2022). No Arbitrage SVI. *SIAM Journal on Financial Mathematics*. https://doi.org/10.1137/20m1351060

**Relevance.** Parametric construction/calibration with explicit arbitrage control; a direct benchmark for the static no-arbitrage constraints in the RQ.

**Key findings (abstract-level).** We fully characterize the absence of butterfly arbitrage in the stochastic volatility inspired (SVI) formula for implied total variance proposed by Gatheral in 2004. The main ingredient is an intermediate characterization of the necessary condition for no arbitrage obtained for any model by Fukasawa in 2012 that the inverse functions of the $-d_1$ and $-d_2$ of the Black--Scholes formula, viewed as functions of the log-forward moneyness, should be increasing.

**Quality.** Level VI (single empirical study; peer-reviewed).

**Method weakness.** Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

#### [P7] Mingone (2022)

**Citation.** Mingone, A. (2022). No arbitrage global parametrization for the eSSVI volatility surface. *Quantitative Finance*. https://doi.org/10.1080/14697688.2022.2117076

**Relevance.** Parametric construction/calibration with explicit arbitrage control; a direct benchmark for the static no-arbitrage constraints in the RQ.

**Key findings (abstract-level).** Provides a global arbitrage-free parametrization of eSSVI surfaces that calibrates all maturities jointly rather than sequentially, and guarantees absence of static arbitrage.

**Quality.** Level VI (single empirical study; peer-reviewed).

**Method weakness.** Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

### 3.2 Nonparametric, spline, and Gaussian-process surfaces (6)

#### [N1] Avellaneda et al. (2020)

**Citation.** Avellaneda, M., Healy, B., Papanicolaou, A. C., & Papanicolaou, G. (2020). PCA for Implied Volatility Surfaces. *Journal of Financial Data Science*. https://doi.org/10.3905/jfds.2020.1.032

**Relevance.** Nonparametric, spline, or Gaussian-process construction; directly relevant to the flexibility-versus-constraint trade-off.

**Key findings (abstract-level).** Principal component analysis (PCA) is a useful tool when trying to construct factor models from historical asset returns. For the implied volatilities of US equities, there is a PCA-based model with a principal eigenportfolio whose return time series lies close to that of an overarching market factor. The authors show that this market factor is the index resulting from the daily compounding of a weighted average of implied-volatility returns, with weights based on the options’ open interest and Vega.

**Quality.** Level VI (single empirical study; peer-reviewed).

**Method weakness.** Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

#### [N2] Zhuang & Wu (2026)

**Citation.** Zhuang, J., & Wu, X. (2026). SABR-informed multitask Gaussian process: A synthetic-to-real framework for implied volatility surface construction. *Journal of Computational Science*. https://doi.org/10.1016/j.jocs.2026.102818

**Relevance.** Nonparametric, spline, or Gaussian-process construction; directly relevant to the flexibility-versus-constraint trade-off.

**Key findings (abstract-level).** SABR-informed multitask Gaussian process: synthetic SABR surfaces are the source task and market quotes the target; the method stabilizes sparse wings and corrects SABR misspecification.

**Quality.** Level VI (single empirical study; peer-reviewed).

**Method weakness.** Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

#### [N3] Yao et al. (2026)

**Citation.** Yao, Y., Cui, Z., & Pan, Q. (2026). Joint arbitrage-free smoothing of American call and put options surfaces. *European Journal of Operational Research*. https://doi.org/10.1016/j.ejor.2026.07.049

**Relevance.** Nonparametric, spline, or Gaussian-process construction; directly relevant to the flexibility-versus-constraint trade-off.

**Key findings (abstract-level).** Joint cubic-spline quadratic program for arbitrage-free smoothing of American call/put surfaces, with two calibration schemes for parametric models.

**Quality.** Level VI (single empirical study; peer-reviewed).

**Method weakness.** Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

#### [N4] Luo & Yu (2023)

**Citation.** Luo, J., & Yu, C. L. (2023). The Application of Symbolic Regression on Identifying Implied Volatility Surface. *Mathematics*. https://doi.org/10.3390/math11092108

**Relevance.** Nonparametric, spline, or Gaussian-process construction; directly relevant to the flexibility-versus-constraint trade-off.

**Key findings (abstract-level).** One important parameter in the Black–Scholes option pricing model is the implied volatility. Implied volatility surface (IVS) is an important concept in finance that describes the variation of implied volatility across option strike price and time to maturity. Over the last few decades, economists and financialists have long tried to exploit the predictability in the IVS using various parametric models, which require deep understanding of financial practices in the area.

**Quality.** Level VI (single empirical study; peer-reviewed).

**Method weakness.** Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

#### [N5] Appana et al. (2024)

**Citation.** Appana, T., Carranti, A., Koshal, A., Moszczyński, A., & Thomas, M. (2024). Gaussian Processes for Implied Volatility Estimation. *SSRN*. https://doi.org/10.2139/ssrn.4803161

**Relevance.** Nonparametric, spline, or Gaussian-process construction; directly relevant to the flexibility-versus-constraint trade-off.

**Key findings (abstract-level).** The accurate modeling of the implied volatility surface holds great importance in option pricing, trading, and hedging. Significant research has been devoted to this task, ranging from mathematical models to machine-learning solutions. However, these approaches generate point estimates based on imperfect market data, which can lead to inaccurate and misleading models. Gaussian Processes, a Bayesian nonparametric method, have addressed this challenge.

**Quality.** Level VI (single empirical study; preprint).

**Method weakness.** Preprint (not peer-reviewed). Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

#### [N6] Cousin & Gueye (2021)

**Citation.** Cousin, A., & Gueye, D. (2021). Kriging for implied volatility surface. *HAL*. https://openalex.org/W3184266889

**Relevance.** Nonparametric, spline, or Gaussian-process construction; directly relevant to the flexibility-versus-constraint trade-off.

**Key findings (abstract-level).** Implied volatility surface is of crucial interest for risk management and exotic option pricing models. Its construction is usually carried out in accordance with the arbitrage-free principle. This condition leads to shape restrictions on the option prices such as monotonicity with respect to maturities and convexity with respect to strike prices. In this paper, we propose a new arbitrage-free construction method that extends classical spline techniques by additionally allowing for quantification of uncertainty.

**Quality.** Level VI (single empirical study; preprint).

**Method weakness.** Preprint (not peer-reviewed). Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

### 3.3 Neural and generative surfaces (18)

#### [M1] Ackerer et al. (2019)

**Citation.** Ackerer, D., Tagasovska, N., & Vatter, T. (2019). Deep Smoothing of the Implied Volatility Surface. *SSRN*. https://doi.org/10.2139/ssrn.3402942

**Relevance.** Neural or generative surface construction/dynamics; directly relevant to fitting, generalization, and constraint-enforcement trade-offs.

**Key findings (abstract-level).** We present a neural network (NN) approach to fit and predict implied volatility surfaces (IVSs). Atypically to standard NN applications, financial industry practitioners use such models equally to replicate market prices and to value other financial instruments. In other words, low training losses are as important as generalization capabilities. Importantly, IVS models need to generate realistic arbitrage-free option prices, meaning that no portfolio can lead to risk-free profits.

**Quality.** Level VI (single empirical study; preprint).

**Method weakness.** Preprint (not peer-reviewed). Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

#### [M2] Bayer & Stemper (2018)

**Citation.** Bayer, C., & Stemper, B. (2018). Deep calibration of rough stochastic volatility models. *arXiv*. https://doi.org/10.48550/arxiv.1810.03399

**Relevance.** Neural or generative surface construction/dynamics; directly relevant to fitting, generalization, and constraint-enforcement trade-offs.

**Key findings (abstract-level).** Sparked by Alòs, León, and Vives (2007); Fukasawa (2011, 2017); Gatheral, Jaisson, and Rosenbaum (2018), so-called rough stochastic volatility models such as the rough Bergomi model by Bayer, Friz, and Gatheral (2016) constitute the latest evolution in option price modeling. Unlike standard bivariate diffusion models such as Heston (1993), these non-Markovian models with fractional volatility drivers allow to parsimoniously recover key stylized facts of market implied volatility surfaces such as the exploding power-law behaviour of the at-the-money...

**Quality.** Level VI (single empirical study; preprint).

**Method weakness.** Preprint (not peer-reviewed). Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

#### [M3] Ning et al. (2023)

**Citation.** Ning, B., Jaimungal, S., Zhang, X., & Bergeron, M. (2023). Arbitrage-Free Implied Volatility Surface Generation with Variational Autoencoders. *SIAM Journal on Financial Mathematics*. https://doi.org/10.1137/21m1443546

**Relevance.** Neural or generative surface construction/dynamics; directly relevant to fitting, generalization, and constraint-enforcement trade-offs.

**Key findings (abstract-level).** We propose a hybrid method for generating arbitrage-free implied volatility (IV) surfaces consistent with historical data by combining model-free variational autoencoders (VAEs) with continuous time stochastic differential equation (SDE) driven models. We focus on two classes of SDE models: regime switching models and Lévy additive processes. By projecting historical surfaces onto the space of SDE model parameters, we obtain a distribution on the parameter subspace faithful to the data on which we then train a VAE.

**Quality.** Level VI (single empirical study; peer-reviewed).

**Method weakness.** Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

#### [M4] Horvath et al. (2021)

**Citation.** Horvath, B. N., Muguruza, A., & Tomas, M. (2021). Deep Learning Volatility. *Quantitative Finance*. https://doi.org/10.1080/14697688.2020.1817974

**Relevance.** Neural or generative surface construction/dynamics; directly relevant to fitting, generalization, and constraint-enforcement trade-offs.

**Key findings (abstract-level).** Abstract not retrieved; title-level only. The title indicates a deep-learning approach to volatility-surface construction/calibration, but no finding is asserted here beyond that title-level relevance.

**Quality.** Level VI (single empirical study; abstract unavailable).

**Method weakness.** Design: single empirical study. Failure condition: cannot be appraised without an abstract/full text. Author-acknowledged vs reader-inferred: neither available. Bounded absence: no reported failure is not evidence of absence. Fixed aspect checklist (fit, static arbitrage, dynamics, out-of-sample, cost): unassessed. Abstract-only: no abstract retrieved.

#### [M5] Zhang et al. (2022)

**Citation.** Zhang, W., Li, L., & Zhang, G. (2022). A two-step framework for arbitrage-free prediction of the implied volatility surface. *Quantitative Finance*. https://doi.org/10.1080/14697688.2022.2135454

**Relevance.** Neural or generative surface construction/dynamics; directly relevant to fitting, generalization, and constraint-enforcement trade-offs.

**Key findings (abstract-level).** In this study, we propose a two-step framework to predict the implied volatility surface (IVS) in a manner that excludes static arbitrage. First, we select features to represent the surface and predict them. Second, we use the predicted features to construct the IVS using a deep neural network (DNN) model by incorporating constraints that can prevent static arbitrage. We consider three methods to extract features from the implied volatility data: principal component analysis, variational autoencoder, and sampling the surface.

**Quality.** Level VI (single empirical study; peer-reviewed).

**Method weakness.** Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

#### [M6] Vuletić & Cont (2025)

**Citation.** Vuletić, M., & Cont, R. (2025). VolGAN: A Generative Model for Arbitrage-Free Implied Volatility Surfaces. *Applied Mathematical Finance*. https://doi.org/10.1080/1350486x.2025.2471317

**Relevance.** Neural or generative surface construction/dynamics; directly relevant to fitting, generalization, and constraint-enforcement trade-offs.

**Key findings (abstract-level).** We introduce VolGAN, a generative model for arbitrage-free implied volatility surfaces. The model is trained on time series of implied volatility surfaces and underlying prices and is capable of generating realistic scenarios for joint dynamics of the implied volatility surface and the underlying asset. We illustrate the performance of the model by training it on SPX implied volatility time series and show that it is able to learn the covariance structure of the co-movements in implied volatilities and generate realistic dynamics for the (VIX)...

**Quality.** Level VI (single empirical study; peer-reviewed).

**Method weakness.** Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

#### [M7] Cont & Vuletić (2023)

**Citation.** Cont, R., & Vuletić, M. (2023). Simulation of Arbitrage-Free Implied Volatility Surfaces. *Applied Mathematical Finance*. https://doi.org/10.1080/1350486x.2023.2277960

**Relevance.** Neural or generative surface construction/dynamics; directly relevant to fitting, generalization, and constraint-enforcement trade-offs.

**Key findings (abstract-level).** We present a computationally tractable method for simulating arbitrage-free implied volatility surfaces.We illustrate how our method may be combined with a data-driven model based on historical SPX implied volatility data to generate dynamic scenarios for arbitrage-free implied volatility surfaces.Our approach conciliates static arbitrage constraints with a realistic representation of statistical properties of implied volatility co-movements.

**Quality.** Level VI (single empirical study; peer-reviewed).

**Method weakness.** Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

#### [M8] Cohen et al. (2023)

**Citation.** Cohen, S. N., Reisinger, C., & Wang, S. (2023). Arbitrage-Free Neural-SDE Market Models. *Applied Mathematical Finance*. https://doi.org/10.1080/1350486x.2023.2257217

**Relevance.** Neural or generative surface construction/dynamics; directly relevant to fitting, generalization, and constraint-enforcement trade-offs.

**Key findings (abstract-level).** Modelling joint dynamics of liquid vanilla options is crucial for arbitrage-free pricing of illiquid derivatives and managing risks of option trade books. This paper develops a nonparametric model for the European options book respecting underlying financial constraints and while being practically implementable. We derive a state space for prices which are free from static (or model-independent) arbitrage and study the inference problem where a model is learnt from discrete time series data of stock and option prices.

**Quality.** Level VI (single empirical study; peer-reviewed).

**Method weakness.** Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

#### [M9] Medvedev & Wang (2021)

**Citation.** Medvedev, N., & Wang, Z. (2021). Multistep forecast of the implied volatility surface using deep learning. *Journal of Futures Markets*. https://doi.org/10.1002/fut.22302

**Relevance.** Neural or generative surface construction/dynamics; directly relevant to fitting, generalization, and constraint-enforcement trade-offs.

**Key findings (abstract-level).** We contribute to the literature by modeling the entire IVS using convolutional long‐short‐term memory (ConvLSTM) and long‐short‐term memory (LSTM) neural networks to produce multivariate and multistep forecasts of the S&P 500 IVS. Using daily SPX options data (2002–2019), we find that both LSTM and ConvLSTM fit the training data extremely well with mean absolute percentage error (MAPE) being 3.56% and 3.88%, respectively.

**Quality.** Level VI (single empirical study; peer-reviewed).

**Method weakness.** Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

#### [M10] Zheng et al. (2021)

**Citation.** Zheng, Y., Yang, Y., & Chen, B. (2021). Incorporating Prior Financial Domain Knowledge into Neural Networks for Implied Volatility Surface Prediction. *Proceedings of the 27th ACM SIGKDD Conference on Knowledge Discovery and Data Mining*. https://doi.org/10.1145/3447548.3467115

**Relevance.** Neural or generative surface construction/dynamics; directly relevant to fitting, generalization, and constraint-enforcement trade-offs.

**Key findings (abstract-level).** In this paper we develop a novel neural network model for predicting implied volatility surface. Prior financial domain knowledge is taken into account. A new activation function that incorporates volatility smile is proposed, which is used for the hidden nodes that process the underlying asset price. In addition, financial conditions, such as the absence of arbitrage, the boundaries and the asymptotic slope, are embedded into the loss function.

**Quality.** Level VI (single empirical study; peer-reviewed).

**Method weakness.** Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

#### [M11] Bayer et al. (2025)

**Citation.** Bayer, C., Horvath, B. N., Muguruza, A., Stemper, B., & Tomas, M. (2025). On Deep Calibration of (rough) Stochastic Volatility Models. *Journal of FinTech*. https://doi.org/10.1142/s2705109925500051

**Relevance.** Neural or generative surface construction/dynamics; directly relevant to fitting, generalization, and constraint-enforcement trade-offs.

**Key findings (abstract-level).** Advocates a two-step deep-calibration approach: learn the pricing map from model parameters to prices/implied volatilities, then use traditional calibration; compares approximation choices.

**Quality.** Level VI (single empirical study; peer-reviewed).

**Method weakness.** Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

#### [M12] Ginart Belmonte & Cole (2025)

**Citation.** Ginart Belmonte, V., & Cole, T. (2025). Arbitrage-Free Implied Volatility Surface Smoothing via Generative Adversarial Networks. *Proceedings of the ACM International Conference on AI in Finance*. https://doi.org/10.1145/3768292.3771252

**Relevance.** Neural or generative surface construction/dynamics; directly relevant to fitting, generalization, and constraint-enforcement trade-offs.

**Key findings (abstract-level).** Implied volatility surfaces play a fundamental role in the pricing and risk management of financial derivatives. However, as a result of estimation noise, they often contain arbitrage violations which need to be corrected to allow for effective pricing. Traditional smoothing techniques struggle to scale efficiently and usually need to be manually re-fitted to enforce no-arbitrage conditions.

**Quality.** Level VI (single empirical study; peer-reviewed).

**Method weakness.** Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

#### [M13] Bajalica et al. (2026)

**Citation.** Bajalica, D., Brooks, O., & Ben Tahar, I. (2026). Latent Flow Matching for Arbitrage-Aware Implied Volatility Surface Generation. *Proceedings of the ACM International Conference on AI in Finance*. https://doi.org/10.1145/3858063.3858741

**Relevance.** Neural or generative surface construction/dynamics; directly relevant to fitting, generalization, and constraint-enforcement trade-offs.

**Key findings (abstract-level).** We propose an arbitrage-aware latent flow-matching framework for unconditional implied volatility surface generation. The method first compresses high-dimensional surfaces into a low-dimensional latent space using a variational autoencoder regularized by differentiable calendar-spread, call-spread and butterfly-arbitrage penalties. A flow-matching model then learns to transport a Gaussian prior toward the empirical latent distribution, and generated latent samples are decoded back into volatility surfaces.

**Quality.** Level VI (single empirical study; peer-reviewed).

**Method weakness.** Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

#### [M14] Wang et al. (2025)

**Citation.** Wang, J., Liu, S., & Vuik, C. (2025). Controllable Generation of Implied Volatility Surfaces with Variational Autoencoders. *arXiv*. https://doi.org/10.48550/arxiv.2509.01743

**Relevance.** Neural or generative surface construction/dynamics; directly relevant to fitting, generalization, and constraint-enforcement trade-offs.

**Key findings (abstract-level).** This paper presents a deep generative modeling framework for controllably synthesizing implied volatility surfaces (IVSs) using a variational autoencoder (VAE). Unlike conventional data-driven models, our approach provides explicit control over meaningful shape features (e.g., volatility level, slope, curvature, term-structure) to generate IVSs with desired characteristics. In our framework, financially interpretable shape features are disentangled from residual latent factors.

**Quality.** Level VI (single empirical study; preprint).

**Method weakness.** Preprint (not peer-reviewed). Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

#### [M15] Hoshisashi et al. (2024)

**Citation.** Hoshisashi, K., Phelan, C. E., & Barucca, P. (2024). Whack-a-mole Online Learning: Physics-Informed Neural Network for Intraday Implied Volatility Surface. *Proceedings of the ACM International Conference on AI in Finance*. https://doi.org/10.1145/3677052.3698601

**Relevance.** Neural or generative surface construction/dynamics; directly relevant to fitting, generalization, and constraint-enforcement trade-offs.

**Key findings (abstract-level).** Calibrating the time-dependent Implied Volatility Surface (IVS) using sparse market data is an essential challenge in computational finance, particularly for real-time applications. This task requires not only fitting market data but also satisfying a specified partial differential equation (PDE) and no-arbitrage conditions modelled by differential inequalities. This paper proposes a novel Physics-Informed Neural Networks (PINNs) approach called Whack-a-mole Online Learning (WamOL) to address this multi-objective optimisation problem.

**Quality.** Level VI (single empirical study; peer-reviewed).

**Method weakness.** Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

#### [M16] Wiedemann et al. (2024)

**Citation.** Wiedemann, R., Jacquier, A., & Gonon, L. (2024). Operator Deep Smoothing for Implied Volatility. *arXiv*. https://doi.org/10.48550/arxiv.2406.11520

**Relevance.** Neural or generative surface construction/dynamics; directly relevant to fitting, generalization, and constraint-enforcement trade-offs.

**Key findings (abstract-level).** We devise a novel method for nowcasting implied volatility based on neural operators. Better known as implied volatility smoothing in the financial industry, nowcasting of implied volatility means constructing a smooth surface that is consistent with the prices presently observed on a given option market. Option price data arises highly dynamically in ever-changing spatial configurations, which poses a major limitation to foundational machine learning approaches using classical neural networks.

**Quality.** Level VI (single empirical study; preprint).

**Method weakness.** Preprint (not peer-reviewed). Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

#### [M17] Hoshisashi et al. (2023)

**Citation.** Hoshisashi, K., Phelan, C. E., & Barucca, P. (2023). No-Arbitrage Deep Calibration for Volatility Smile and Skewness. *arXiv*. https://doi.org/10.48550/arxiv.2310.16703

**Relevance.** Neural or generative surface construction/dynamics; directly relevant to fitting, generalization, and constraint-enforcement trade-offs.

**Key findings (abstract-level).** Volatility smile and skewness are two key properties of option prices that are represented by the implied volatility (IV) surface. However, IV surface calibration through nonlinear interpolation is a complex problem due to several factors, including limited input data, low liquidity, and noise. Additionally, the calibrated surface must obey the fundamental financial principle of the absence of arbitrage, which can be modeled by various differential inequalities over the partial derivatives of the option price with respect to the expiration time and...

**Quality.** Level VI (single empirical study; preprint).

**Method weakness.** Preprint (not peer-reviewed). Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

#### [M18] Zetocha (2023)

**Citation.** Zetocha, V. (2023). Volatility Transformers: an optimal transport-inspired approach to arbitrage-free shaping of implied volatility surfaces. *SSRN*. https://doi.org/10.2139/ssrn.4623940

**Relevance.** Neural or generative surface construction/dynamics; directly relevant to fitting, generalization, and constraint-enforcement trade-offs.

**Key findings (abstract-level).** We introduce a framework for generating arbitrage-free transformations of an implied volatility surface based on optimal transport maps between suitable distributions. We exemplify our approach by solving standard tasks related to volatility surface alterations like time extrapolation, modification of skew or term structure of volatility, introduction of a market event, removal of arbitrage and generation of volatility surface dynamics.

**Quality.** Level VI (single empirical study; preprint).

**Method weakness.** Preprint (not peer-reviewed). Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

### 3.4 Constraint enforcement, arbitrage repair, and evaluation (8)

#### [C1] Yang et al. (2017)

**Citation.** Yang, Y., Zheng, Y., & Hospedales, T. M. (2017). Gated Neural Networks for Option Pricing: Rationality by Design. *Proceedings of the AAAI Conference on Artificial Intelligence*. https://doi.org/10.1609/aaai.v31i1.10505

**Relevance.** Constraint enforcement, arbitrage detection/repair, or evaluation; central to how the RQ operationalizes no-arbitrage.

**Key findings (abstract-level).** We propose a neural network approach to price EU call options that significantly outperforms some existing pricing models and comes with guarantees that its predictions are economically reasonable. To achieve this, we introduce a class of gated neural networks that automatically learn to divide-and-conquer the problem space for robust and accurate pricing. We then derive instantiations of these networks that are 'rational by design' in terms of naturally encoding a valid call option surface that enforces no arbitrage principles.

**Quality.** Level VI (single empirical study; peer-reviewed).

**Method weakness.** Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

#### [C2] Ruf & Wang (2020)

**Citation.** Ruf, J., & Wang, W. (2020). Neural Networks for Option Pricing and Hedging: A Literature Review. *Journal of Computational Finance*. https://doi.org/10.21314/jcf.2020.390

**Relevance.** Constraint enforcement, arbitrage detection/repair, or evaluation; central to how the RQ operationalizes no-arbitrage.

**Key findings (abstract-level).** Comprehensive review comparing neural option-pricing/hedging papers by input features, output variables, benchmark models, performance measures, data partitions, and underlying assets.

**Quality.** Level VII (narrative review/survey).

**Method weakness.** Narrative review/survey, not a systematic review; coverage/selection rules are not reproducible; the abstract does not state a systematic search (reader-inferred); absence of a cited study is bounded by coverage; checklist (fit, arbitrage, dynamics, OOS, cost) is narrative; full text not read.

#### [C3] Cao et al. (2020)

**Citation.** Cao, Y., Liu, X., & Zhai, J. (2020). Option valuation under no-arbitrage constraints with neural networks. *European Journal of Operational Research*. https://doi.org/10.1016/j.ejor.2020.12.003

**Relevance.** Constraint enforcement, arbitrage detection/repair, or evaluation; central to how the RQ operationalizes no-arbitrage.

**Key findings (abstract-level).** Publisher/web snippet: the paper proposes a hybrid graph neural network (hGNN) for option valuation that incorporates economic constraints and yields analytical expressions for European option Greeks, emphasizing interpretability relative to black-box neural models. (Partial snippet; full abstract not retrieved.)

**Quality.** Level VI (single empirical study; peer-reviewed).

**Method weakness.** Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

#### [C4] Cohen et al. (2020)

**Citation.** Cohen, S. N., Reisinger, C., & Wang, S. (2020). Detecting and Repairing Arbitrage in Traded Option Prices. *Applied Mathematical Finance*. https://doi.org/10.1080/1350486x.2020.1846573

**Relevance.** Constraint enforcement, arbitrage detection/repair, or evaluation; central to how the RQ operationalizes no-arbitrage.

**Key findings (abstract-level).** Option price data are used as inputs for model calibration, risk-neutral density estimation and many other financial applications. The presence of arbitrage in option price data can lead to poor performance or even failure of these tasks, making pre-processing of the data to eliminate arbitrage necessary. Most attention in the relevant literature has been devoted to arbitrage-free smoothing and filtering (i.e., removing) of data.

**Quality.** Level VI (single empirical study; peer-reviewed).

**Method weakness.** Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

#### [C5] Liu et al. (2019)

**Citation.** Liu, S., Oosterlee, C. W., & Bohté, S. M. (2019). Pricing Options and Computing Implied Volatilities using Neural Networks. *Risks*. https://doi.org/10.3390/risks7010016

**Relevance.** Constraint enforcement, arbitrage detection/repair, or evaluation; central to how the RQ operationalizes no-arbitrage.

**Key findings (abstract-level).** This paper proposes a data-driven approach, by means of an Artificial Neural Network (ANN), to value financial options and to calculate implied volatilities with the aim of accelerating the corresponding numerical methods. With ANNs being universal function approximators, this method trains an optimized ANN on a data set generated by a sophisticated financial model, and runs the trained ANN as an agent of the original solver in a fast and efficient way.

**Quality.** Level VI (single empirical study; peer-reviewed).

**Method weakness.** Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

#### [C6] Neufeld & Sester (2024)

**Citation.** Neufeld, A., & Sester, J. (2024). Neural Networks Can Detect Model-Free Static Arbitrage Strategies. *Applied Mathematics & Optimization*. https://doi.org/10.1007/s00245-024-10184-9

**Relevance.** Constraint enforcement, arbitrage detection/repair, or evaluation; central to how the RQ operationalizes no-arbitrage.

**Key findings (abstract-level).** Demonstrates theoretically and numerically that neural networks can detect model-free static arbitrage when it exists, including high-dimensional markets and real data; proves a single network can approximately solve a class of convex semi-algebraic problems.

**Quality.** Level VI (single empirical study; peer-reviewed).

**Method weakness.** Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

#### [C7] Xiong & Liu (2026)

**Citation.** Xiong, Y., & Liu, B. (2026). Observation-Anchored Arbitrage Repair for Sparse Implied Volatility Surface Completion. *IEEE Conference on Computational Intelligence for Financial Engineering & Economics*. https://doi.org/10.1109/cifer67845.2026.11692406

**Relevance.** Constraint enforcement, arbitrage detection/repair, or evaluation; central to how the RQ operationalizes no-arbitrage.

**Key findings (abstract-level).** Completing dense implied volatility surfaces (IVS) from sparse option quotes is central to derivatives pricing and risk management. A financially admissible surface must satisfy calendar and butterfly no-arbitrage conditions, yet existing completion methods do not enforce these constraints while preserving observed market quotes. We propose a deterministic, observation-anchored two-step repair algorithm enforcing calendar constraints in total-variance space and butterfly constraints in normalized call-price space, modifying only unobserved grid cells.

**Quality.** Level VI (single empirical study; peer-reviewed).

**Method weakness.** Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

#### [C8] Anagha (2026)

**Citation.** Anagha, S. (2026). Trainable Hard Constraints: Architectural Enforcement of Arbitrage-Free Implied Volatility Surfaces via Automatic Differentiation. *SSRN*. https://doi.org/10.2139/ssrn.7577418

**Relevance.** Constraint enforcement, arbitrage detection/repair, or evaluation; central to how the RQ operationalizes no-arbitrage.

**Key findings (abstract-level).** Builds convexity in log-moneyness and monotonicity in maturity into a neural total-variance surface by architecture, using automatic differentiation; a proof-of-concept on the accuracy cost.

**Quality.** Level VI (single empirical study; preprint).

**Method weakness.** Preprint (not peer-reviewed). Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

### 3.5 Surface dynamics and path dependence (1)

#### [D1] Andrès et al. (2026)

**Citation.** Andrès, H., Boumezoued, A., & Jourdain, B. (2026). The implied volatility surface (also) is path-dependent. *Quantitative Finance*. https://doi.org/10.1080/14697688.2026.2637739

**Relevance.** Surface dynamics and path dependence; relevant to the dynamic no-arbitrage side of the RQ.

**Key findings (abstract-level).** Proposes a path-dependent model for joint simulation of the implied-volatility surface and the underlying; past returns explain much of the ATM-forward IV movement up to two years.

**Quality.** Level VI (single empirical study; peer-reviewed).

**Method weakness.** Single-study design; failure condition = generalization beyond the reported market/period is untested; out-of-sample/robustness not reported (reader-inferred); no reported failure is bounded absence; checklist (fit, arbitrage, dynamics, OOS, cost) abstract-level; full text not read.

## 4. Search Limitations

- **Discovery:** OpenAlex full-text search only; no Web of Science/Scopus, no citation chaining beyond the query pool, no hand search of conference proceedings.
- **Selection:** 40 records selected from a 351-record pool; the 311 not advanced were not individually screened, so selection bias cannot be excluded.
- **Coverage:** English-language, 2015–2026, equity-index-heavy; market microstructure, crypto, and non-US evidence are underrepresented.
- **Verification:** Semantic Scholar returned HTTP 429 for every request; Crossref returned one 429 and several empty abstracts; no full text was read; no formal risk-of-bias tool or double screening was used.
- **Preprints:** 10/40 records are preprints (SSRN, arXiv, HAL); they are flagged in the annotated entries and should not carry central claims without peer-reviewed corroboration.
- **No PRISMA claim:** the screening flow is PRISMA-style only. The review-form note was not answered with a systematic-review choice.

## 5. Corpus Index

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
