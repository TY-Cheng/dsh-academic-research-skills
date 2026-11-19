## Domain Review Report (Peer Reviewer 2)

**Target-binding status:** `criteria_binding_unavailable` — no author-confirmed #683 `ReviewTargetContext` or Target Criteria Brief was supplied with this dispatch; no venue, track, or article-type criterion is bound, and no venue-alignment claim is made below.

**Review scope.** This report assesses domain accuracy, literature coverage, and taxonomy validity. The search and screening procedure is Reviewer 1's remit and is not scored here; where the corpus boundary has domain consequences I say so explicitly rather than re-reviewing the method.

### Reviewer Identity

Senior professor of mathematical finance specializing in implied-volatility-surface construction and arbitrage-free parameterizations (SVI/SSVI/eSSVI and constrained smoothing), with publications in *Quantitative Finance* and the *SIAM Journal on Financial Mathematics*; teaches calibration and model validation and referees for the main derivatives and financial-mathematics journals (field_analyst Reviewer Configuration Card #3).

### Overall Recommendation

**Major Revision**

### Confidence Score

**4/5** — High confidence on the no-arbitrage mathematics, the SVI/SSVI/eSSVI literature, and the taxonomy mapping, all of which I checked directly against the manuscript. Lower confidence on the publication status of individual 2026 records and on any source claim that would require the full texts; neither was available to this seat, and the paper itself discloses abstract-level evidence.

Confidence is an uncertainty/scope disclosure only; it never changes consensus counts, severity, decision bearing, or arbitration.

### Calibration Status

`NOT_CALIBRATED`

Seat reports always emit `NOT_CALIBRATED`: the final actual panel topology is not knowable until every seat has completed. A candidate profile never upgrades the seat report.

### Criterion-Bound Judgements

| Dimension / criterion | Criterion source | Judgement | Evidence anchors | Rationale | Uncertainty or scope limit | Decision bearing? |
|---|---|---|---|---|---|---|
| Literature completeness and attribution accuracy | Reviewer Configuration Card #3 (field-analysis.md), focus 1 | PARTLY_MEETS | `absence: References — expected the dynamic market-model strand (Schönbucher, 1999; Schweizer & Wissel, 2008); checked §2.4 and the reference list`; `text: References — "Ackerer, D., Tagasovska, N., & Vatter, T. (2019). Deep Smoothing of the Implied Volatility Surface"` | The static-arbitrage core is accurate and well chosen, but the primary static-arbitrage foundations and the dynamic market-model literature are absent, and at least one preprint record is misclassified. | The corpus is frozen and abstract-level; I did not verify every 2026 record's current publication status. | yes — drives W3 and W6 and the Major revision recommendation. |
| Taxonomy and classification validity | Reviewer Configuration Card #3, focus 2 | PARTLY_MEETS | `table: Appendix D, "Enforcement family" column, rows 11, 12, 19 ("None/soft")`; `table: Table 1, "Family" column, "Constraints / evaluation" row (N = 8)` | The four-family enforcement taxonomy is a genuine idea but is not a partition of the mapped corpus; Table 1 mixes method families with topic categories; two canonical sources are misassigned. | The mapping is interpretive by the author's own admission; alternative mappings are legitimate, but the paper's own labels are off-taxonomy. | yes — drives W1 and W4. |
| Technical precision of the static/dynamic no-arbitrage framing | Reviewer Configuration Card #3, focus 3; role prompt Step 3 | PARTLY_MEETS | `text: §2.4 — "joint martingale condition"`; `text: §1.1 — "calendar (maturity-monotonicity)"` | Static conditions are broadly right but imprecisely stated; dynamic no-arbitrage is never defined and one sentence is technically wrong for a single surface. | The paper's corpus-scoped hedges are materially better than the abstract; the defect is the mismatch between hedge and claim. | yes — drives W2 and W5. |
| Contribution and positioning in the field | Reviewer Configuration Card #3, focus 3; role prompt Step 4 | PARTLY_MEETS | `text: §1.5 — "The contribution is deliberately modest"`; `text: §6 — "choose the guarantee before the model"` | The enforcement taxonomy and seven-dimension matrix are genuine, useful contributions; the dynamic "frontier" claim and missing literature weaken the positioning. | No venue binding; no target criteria against which to weigh the contribution. | yes — supports Major Revision rather than Reject. |

Do not total, weight, average, or mechanically map these judgements to the recommendation.

### Summary Assessment

This is a careful, candidly scoped structured review of a large and fast-moving literature, and its central interpretive move — asking which mechanism carries the no-arbitrage guarantee rather than whether a surface is "arbitrage-free" — is the best idea in the paper. The static parametric core is handled faithfully: SVI/SSVI/eSSVI are correctly characterized as explicit admissibility conditions with a conditional guarantee, and the paper is careful not to claim that the construction problem is closed. The evidence grading and the limitations section are unusually transparent. The problem is that the paper's two most ambitious contributions do not survive their own mapping. The four-family enforcement taxonomy is not a partition of the corpus: Appendix D assigns 11 of 40 sources to "None/soft", "Survey", or "Evaluation/detection", and three more to "construction" via a calibration map whose guarantee is inherited from a parent model rather than carried by the network. The static/dynamic distinction is right in spirit but stated imprecisely — the claim that a single static-arbitrage-free surface can be "inconsistent with a joint model" is technically wrong — and the dynamic "frontier" finding is a corpus artifact stated at field scope while the canonical dynamic-arbitrage literature is absent. These are repairable but load-bearing; the paper needs a substantial revision of §2.4–§2.6 and §4.2–§4.5, not copy-editing. I recommend Major Revision.

### Strengths

1. **S1 A genuinely useful organizing question.** The shift from "is the surface arbitrage-free?" to "which mechanism carries the guarantee?" is the paper's best idea and is stated cleanly; it gives a reader a way to compare methods that is not another method list. *Evidence Anchor:* `text: §1.2 — "These are not equivalent guarantees."`
2. **S2 Faithful, compact treatment of the static parametric core.** The SVI/SSVI/eSSVI strand is correctly characterized as explicit admissibility conditions with a conditional guarantee, and the paper avoids claiming the construction problem is solved. *Evidence Anchor:* `text: §2.1 — "the surface is arbitrage-free by construction"`.
3. **S3 Auditable evidence grading.** Appendix B's per-source level (VI for peer-reviewed, VII for preprint) and the abstract-coverage disclosure let a reader see the evidential basis of each claim. *Evidence Anchor:* `table: Appendix B, "Level" column, rows 1–40`.
4. **S4 Epistemic care with thin sources.** The title-level Horvath et al. (2021) record is explicitly quarantined from the dynamic claim and Table 3 is candid that it is thin by design; this is the right treatment. *Evidence Anchor:* `text: §4.4 — "its findings are not used for a substantive dynamic claim"`.
5. **S5 A testable agenda with falsifiers.** Table 6 pairs each proposition with what would support and what would falsify it, and §5.5 states what the review can and cannot support; this is review writing at its best. *Evidence Anchor:* `table: Table 6, "What would falsify it" column`.
6. **S6 The practitioner framing is memorable and correct in the aggregate.** "Choose the guarantee before the model" is a useful decision heuristic for model-risk readers, and Table 7 is appropriately labelled as an aid, not a validated selection rule. *Evidence Anchor:* `text: §6 — "choose the guarantee before the model"`.

### Weaknesses

1. **W1 The four-family enforcement taxonomy is not a partition of the corpus it maps.** The paper's first declared contribution is a taxonomy of where the constraint enters the pipeline (construction, penalty, projection/repair, generation plus filtering). Its own source-level mapping, Appendix D, does not use those four families consistently. Eleven of the 40 sources receive labels that are outside the taxonomy: "None/soft" (rows 11, 12, 14, 19, 28, 34, 36, 39), "Survey (no construction)" (row 4), "Survey/evaluation" (row 8), and "Evaluation/detection" (row 26). Three further sources (rows 6, 21, 37) are labelled "Construction (calibration map)": here the surface is produced by a neural surrogate of a rough-volatility model, so the guarantee is inherited from the parent model, not carried by the network, which is a different mechanism from the parametric/gated construction the taxonomy describes. "None/soft" is not a category the reader can interpret: for Avellaneda et al. (2020), Appana et al. (2024), Cousin and Gueye (2021), Luo and Yu (2023), and Zhuang and Wu (2026) no mechanism carries any guarantee, while for Ackerer et al. (2019), Cao et al. (2020), and Zhang et al. (2022) a soft penalty does part of the work. The taxonomy therefore needs at least a fifth, "no explicit enforcement," category and a distinct treatment of model-inherited guarantees, and Appendix D, Table 2, and the counts must be re-derived. *Improvement:* add the missing category (or two), state that some sources are classified by the guarantee inherited from a parent model, and re-map Appendix D and Table 2; the central claim of §2.6 should be restated as covering the sources that have an enforcement mechanism. **Severity:** Major | **Evidence Anchor:** `table: Appendix D, "Enforcement family" column, rows 4, 8, 11, 12, 14, 19, 21, 26, 28, 34, 36, 37, 39` | **Confidence:** 5 — I counted every label in Appendix D and know these method families.
2. **W2 The static/dynamic distinction is stated with a technical inaccuracy and is never defined operationally.** The paper's second contribution is that static and dynamic no-arbitrage are different layers. The distinction is right in spirit, but §2.4 carries it with a sentence a domain reader will catch: "A surface can pass butterfly and calendar checks and still be inconsistent with a joint model of the underlying and the surface." Read as a statement about a single surface at a single date, this is wrong. Under the standard martingale-coupling result, call prices that are convex, monotone, bounded, and calendar-consistent are consistent with at least one martingale joint law for the underlying whose marginals match the surface (Strassen, 1965; Kellerer, 1972). The genuine dynamic problem concerns a *surface process*: each time slice can be static-arbitrage-free while the family of conditional marginal laws is inconsistent with any joint martingale model, which is the object Cont and Vuletić (2023) and Cohen et al. (2023) formalize. The paper never states this process formulation, never defines "dynamic arbitrage" (for example a self-financing strategy across dates with zero initial cost and non-negative payoff), and repeats the "necessary but not sufficient" sentence in the abstract and conclusion without a proof or a primary source. A second conflation is path-dependence (Andrès et al., 2026), which is an empirical and modelling property of implied-volatility dynamics (cf. Guyon & Lekeufack, 2023), not a no-arbitrage condition; Appendix D nevertheless records "Dynamic test: Y" for Andrès while Table 3 says "Conceptual; no joint test." *Improvement:* define the three objects separately (static admissibility of a slice; existence of a martingale joint law; absence of dynamic arbitrage for a surface process), state and cite the relation, and rewrite §2.4, Table 3, and the abstract/conclusion accordingly. **Severity:** Major | **Evidence Anchor:** `text: §2.4 — "A surface can pass butterfly and calendar checks and still be inconsistent with a joint model of the underlying and the surface"` | **Confidence:** 5 — measure-theoretic finance and martingale coupling.
3. **W3 The "dynamic no-arbitrage is the frontier" finding is corpus-scoped but stated at field scope, and the corpus omits the canonical dynamic-arbitrage literature.** Section 4.4 is commendably explicit that the "frontier" label is "a statement about this corpus, not a universal claim about the field," and §3.7 discloses that the queries may under-cover dynamic no-arbitrage. The abstract then says "Dynamic no-arbitrage is less standardized and less frequently evaluated," and the conclusion calls it "a separate and under-tested layer" — field-level claims that this corpus cannot support. The omission is not only a scope choice. The dynamic-arbitrage/market-model strand is missing: Schönbucher (1999) introduced the stochastic-implied-volatility market model; Cont and da Fonseca (2002) studied implied-volatility-surface dynamics; Buehler (2006) developed consistent variance-curve models; Schweizer and Wissel (2008) characterized absence of arbitrage for term structures of implied volatilities and proved existence results. These are precisely the sources that formalize what the paper calls dynamic no-arbitrage, and the paper's own §3.2 inclusion rule admits pre-2015 seminal work that defines a construction or constraint used by later work — so the omission is checkable against the manuscript's stated criteria, not merely a corpus-expansion request. A domain reader will read the "frontier" claim as an artifact of a corpus built to under-represent it. *Improvement:* either add this strand (a handful of sources would transform §2.4 and Table 3) or, if the corpus stays frozen, restrict the abstract and conclusion to the corpus and name the excluded literature and the direction in which it would change the finding. This is a Major item because the dynamic layer is one of the three declared contributions. **Severity:** Major | **Evidence Anchor:** `text: Abstract — "Dynamic no-arbitrage is less standardized and less frequently evaluated"; §4.4 — "a statement about this corpus, not a universal claim about the field"` | **Confidence:** 4 — the hedge exists in §4.4, so I score the mismatch and the coverage gap, not the corpus boundary itself.
4. **W4 The method-family table and the corpus-composition statements are not method-family classifications.** Table 1 labels its rows "Family," but two rows — "Constraints / evaluation" (N = 8) and "Dynamics" (N = 1) — are topic and enforcement categories, not method families, and the "Neural / generative" row (N = 18) bundles calibration surrogates (Bayer & Stemper, 2018; Bayer et al., 2025; Hoshisashi et al., 2023), forecasting networks (Medvedev & Wang, 2021; Zheng et al., 2021), neural-SDE market models (Cohen et al., 2023), and true generative models (Ning et al., 2023; Vuletić & Cont, 2025). The parametric row includes Fengler (2009), which §2.1 and §2.2 describe as constrained smoothing rather than a parametric family, and the parametric count of 7 includes Homescu (2011), a survey with "no construction" in Appendix D. Consequently "neural/generative 45%" is not a method-family share, "dynamics 1 (2.5%)" contradicts the four dynamic sources in §4.4 and Table 3, and §2.4's "most neural papers evaluate static violations only" contradicts Appendix D, where most neural sources record no explicit static test ("N (soft)" or "N"). *Improvement:* relabel Table 1 as topic buckets (and say so in the caption) and add a separate method-family table, or reclassify the rows; fix the Fengler and Homescu assignments; reconcile the dynamic count and the "most neural papers" sentence with Appendix D. **Severity:** Minor | **Evidence Anchor:** `table: Table 1, "Family" column, rows "Constraints / evaluation" (N = 8) and "Dynamics" (N = 1); "Parametric" row representative Fengler (2009)` | **Confidence:** 5 — direct comparison of Table 1, Appendix B, and Appendix D.
5. **W5 Static-arbitrage conditions are stated with avoidable imprecision.** Section 1.1 glosses calendar arbitrage as "maturity-monotonicity," which invites the false reading that implied volatility must increase with maturity. The no-calendar condition is on total implied variance, w(k,T) = σ²(k,T)T, at fixed log-moneyness k (equivalently, call prices non-decreasing in maturity at fixed strike, with rates and dividends handled consistently), not on σ itself. Section 2.1's "in the maturity dimension, total implied variance must be non-decreasing" needs the fixed-moneyness qualifier, and the strike side needs the monotonicity and bound conditions (C ≥ (F − K)+, decreasing in K) in addition to convexity; the density/non-negativity condition is the Breeden–Litzenberger result and is used without attribution. *Improvement:* state the conditions in one precise display with the fixed-moneyness qualifier and cite Breeden and Litzenberger (1978) and Gatheral and Jacquier (2014). **Severity:** Minor | **Evidence Anchor:** `text: §1.1 — "violations of butterfly (strike-convexity) or calendar (maturity-monotonicity) conditions"` | **Confidence:** 5.
6. **W6 At least one source's publication status and evidence level are misstated.** Appendix B records Ackerer et al. (2019) as an SSRN preprint (level VII), and the paper counts 10 preprints. "Deep Smoothing of the Implied Volatility Surface" appeared in the NeurIPS 2020 proceedings (Advances in Neural Information Processing Systems 33). If the frozen record deliberately cites the 2019 SSRN version, the review should say so and keep the level; if not, the 30/10 peer-reviewed/preprint split and the level-VII grading are wrong for that source. The same check should be applied to the other preprint records, for example Hoshisashi et al. (2023), Appana et al. (2024), and Wiedemann et al. (2024). This is a metadata and attribution issue, not a fabrication issue: the paper's "no fabricated reference" claim is not in doubt. *Improvement:* record which version of each source was assessed and update the counts and levels. **Severity:** Minor | **Evidence Anchor:** `text: References — "Ackerer, D., Tagasovska, N., & Vatter, T. (2019). Deep Smoothing of the Implied Volatility Surface"` | **Confidence:** 4 — I verified the NeurIPS 2020 proceedings version; I cannot confirm from the frozen corpus which version the author assessed.
7. **W7 The single American-options source is outside the review's equity-index European scope.** The title, inclusion criteria, and §1.3 target equity-index implied-volatility surfaces, which in this corpus means European-style SPX and US index options. Yao et al. (2026) smooth American call and put surfaces; American early exercise changes the static-arbitrage conditions (early-exercise premium, put–call parity with dividends, exercise boundaries), so its inclusion as a representative nonparametric construction source in §2.2 and §4.6 is a domain mismatch. The paper discloses "American options beyond one source" as not covered, but that does not explain why the one source is used to support a family-level claim. *Improvement:* either exclude Yao et al. from the family claims or add a paragraph on how the American constraints differ and why the method transfers. **Severity:** Minor | **Evidence Anchor:** `text: §2.2 — "joint cubic-spline quadratic program for American call and put surfaces"` | **Confidence:** 4.
8. **W8 Foundational static-arbitrage and arbitrage-free-interpolation references are absent.** The review's static-arbitrage framework uses the density/butterfly and calendar conditions without citing their primary sources: Breeden and Litzenberger (1978) for the risk-neutral density from call prices; Dupire (1994) for the local-volatility link and the static-arbitrage conditions on the surface; Carr and Madan (2005) for sufficient conditions for no arbitrage; Andreasen and Huge (2011) for arbitrage-free interpolation, which is exactly the construction and repair family the review maps. The paper's own §3.2 admission rule for pre-2015 seminal work makes these checkable omissions, not merely corpus-expansion requests. *Improvement:* add a short "excluded foundational literature" paragraph with citations, or incorporate the sources into §2.1–§2.2. **Severity:** Minor | **Evidence Anchor:** `absence: §2.1–§2.2 and References — expected the primary static-arbitrage sources (Breeden & Litzenberger, 1978; Dupire, 1994; Carr & Madan, 2005; Andreasen & Huge, 2011); checked §2.1, §2.2, §2.6, §3.2, and the reference list` | **Confidence:** 4.

### Detailed Comments

#### Literature Review

- **Coverage**: The static parametric core is well covered and correctly characterized: SVI/SSVI/eSSVI, the Gatheral–Jacquier admissibility conditions, Guo et al.'s generalization, and the Martini–Mingone/Mingone no-arbitrage parameterizations are all in the right places, and the review does not overstate them. The coverage is much weaker at the foundations and at the dynamic end. The primary static-arbitrage sources (Breeden–Litzenberger, Dupire, Carr–Madan) and the arbitrage-free interpolation literature (Andreasen–Huge) are absent, and the dynamic-arbitrage/market-model strand (Schönbucher, Cont–da Fonseca, Buehler, Schweizer–Wissel) is absent, which matters because the review's second contribution is the static/dynamic distinction. The SPX/US concentration is disclosed and is a legitimate corpus-scope decision; it is not the problem I am flagging.
- **Integration quality**: This is genuine synthesis, not enumeration. The enforcement taxonomy, the static/dynamic split, and the tension inventory give the review an argument. The integration is nevertheless at abstract level and does not distinguish sub-method variants (for example raw SVI versus SSVI versus eSSVI conditions, or model-based versus architecture-based guarantees), which is consistent with the stated evidence level but limits the domain value for a specialist reader.
- **Research gap argument**: The "no shared benchmark" gap is persuasive as a corpus-scoped observation and is properly hedged to "the retrieved abstracts." The "dynamic no-arbitrage is the frontier" gap is not persuasive at field scope because the corpus was not built to test it, and the review itself says so in §4.4 while the abstract and conclusion do not. The gap argument would be stronger if it separated "no shared benchmark/protocol" from "no common dataset" and if it named the excluded foundational streams.

#### Theoretical Framework

- **Appropriateness**: The enforcement taxonomy is appropriate to the research question and is the best conceptual move in the paper. The static/dynamic separation is the right axis for a review of this literature, and the "which guarantee?" framing is more useful than a method-family list.
- **Application depth**: The framework is applied unevenly. The four families are used as labels in Appendix D but not as a partition, which is why the off-taxonomy "None/soft" and "Survey" labels appear; a taxonomy that cannot classify a quarter of its own corpus is under-specified. The static/dynamic distinction is asserted rather than defined, and the necessary/not-sufficient relation is not proved or cited. The §5.2 remark that a projection "assumes the repair map is idempotent and stable" is imprecise: idempotence is definitional for a projection operator; the substantive assumptions are that the admissible set is closed/convex, that the projection exists and is unique, and that it is stable under perturbations.
- **Alternative frameworks**: A more standard organization would be by the object that is constrained (option prices, implied-volatility surface, local volatility, or joint law) or by guarantee type (model-free versus model-based, static versus dynamic), with enforcement mechanism as a second axis. The paper's approach is defensible, but a two-axis matrix (mechanism × guarantee scope) would solve the "None/soft" problem and would make the "calibration map" cases interpretable as model-inherited guarantees.

#### Academic Argument Quality

- **Factual accuracy**: The SVI/SSVI/eSSVI attributions and characterizations are generally accurate, and the static-arbitrage conditions are broadly right. The problematic sentence is §2.4's claim that a single surface can pass butterfly and calendar checks and still be "inconsistent with a joint model"; the correct statement concerns a surface process, not a single surface. The Fengler classification (parametric in Table 1, constrained smoothing in §2.1–§2.2) is an internal factual inconsistency. The Ackerer et al. publication-status issue is a metadata inaccuracy that should be corrected or explained.
- **Argument logic**: The corpus-scoped hedges are strong in the body and dropped in the abstract and conclusion for the dynamic claim, which is a scope inference the evidence does not license. The use of Ruf and Wang (2020) is also a category transfer: Ruf and Wang review neural option pricing and hedging and find no common benchmark there, which is relevant context but not direct evidence of a benchmark gap in implied-volatility-surface construction and evaluation; the paper's own corpus-scoped claim is the better support and should stand alone.
- **Terminology precision**: "Dynamic arbitrage," "joint martingale model," "calibration map," "None/soft," and "maturity-monotonicity" all need definitions or corrections. "Static admissibility is necessary but not sufficient" needs the object specified (surface versus surface process). The term "arbitrage-free" is used with care in most of the paper, which is why the §2.4 sentence stands out.

#### Contribution to the Field

- **Incremental contribution**: The enforcement taxonomy is a genuine teaching and analysis device, the seven-dimension matrix is a practical proposal for benchmark design, and the static/dynamic separation is valuable even if under-formalized. The paper is honest that it is not a new theory, estimator, or validated benchmark, and that framing is appropriate.
- **Positioning**: The comparison with Homescu (2011) and Ruf and Wang (2020) is apt, but the paper does not position itself against the dynamic market-model literature it excludes. A short "excluded streams" paragraph with four or five citations would make the positioning defensible and would protect the "frontier" claim.
- **Overclaiming**: The main overclaim is the field-scope dynamic claim in the abstract and conclusion. The "for regulators ... may warrant supervisory attention" line in §5.3 is also unsupported by anything in the review, even though it is immediately hedged; I would delete or soften it. The "no shared benchmark" claim itself is properly scoped to the retrieved abstracts.

#### Missing Key References

- **Breeden and Litzenberger (1978)** — the primary source for obtaining the risk-neutral density from call prices; the density/butterfly condition in §2.1 is used without attribution.
- **Dupire (1994)** — the local-volatility construction and the static-arbitrage conditions on the surface; directly relevant to the construction/repair families.
- **Carr and Madan (2005)** — sufficient conditions for no arbitrage on option prices; the natural citation for §2.1's static conditions.
- **Andreasen and Huge (2011)** — arbitrage-free interpolation; a canonical construction method that the four-family taxonomy under-represents.
- **Schönbucher (1999)** — the stochastic-implied-volatility market model; the missing dynamic strand.
- **Cont and da Fonseca (2002)** — the empirical/dynamic study of implied-volatility-surface dynamics.
- **Buehler (2006)** — consistent variance-curve models; the dynamic-consistency counterpart for variance instruments.
- **Schweizer and Wissel (2008)** — absence of arbitrage and existence results for term structures of implied volatilities; the formal dynamic-arbitrage reference.
- **Guyon and Lekeufack (2023)** — path-dependent volatility and implied-volatility dynamics; the proper context for the Andrès et al. (2026) claim.
- **Strassen (1965) and Kellerer (1972)** — the martingale-coupling result behind the §2.4 correction; the paper should cite it if it keeps the necessary/not-sufficient claim in its corrected (surface-process) form.

~~~yaml suggested-references
- title: "Prices of state-contingent claims implicit in option prices"
  authors: ["Breeden, D. T.", "Litzenberger, R. H."]
  year: "1978"
  doi: null
  arxiv_id: null
- title: "Pricing with a smile"
  authors: ["Dupire, B."]
  year: "1994"
  doi: null
  arxiv_id: null
- title: "A note on sufficient conditions for no arbitrage"
  authors: ["Carr, P.", "Madan, D. B."]
  year: "2005"
  doi: "10.1016/j.frl.2005.04.004"
  arxiv_id: null
- title: "Volatility interpolation"
  authors: ["Andreasen, J.", "Huge, B."]
  year: "2011"
  doi: null
  arxiv_id: null
- title: "A market model for stochastic implied volatility"
  authors: ["Schönbucher, P. J."]
  year: "1999"
  doi: "10.1098/rsta.1999.0418"
  arxiv_id: null
- title: "Dynamics of implied volatility surfaces"
  authors: ["Cont, R.", "da Fonseca, J."]
  year: "2002"
  doi: "10.1088/1469-7688/2/1/304"
  arxiv_id: null
- title: "Consistent variance curve models"
  authors: ["Buehler, H."]
  year: "2006"
  doi: null
  arxiv_id: null
- title: "Term structures of implied volatilities: Absence of arbitrage and existence results"
  authors: ["Schweizer, M.", "Wissel, J."]
  year: "2008"
  doi: "10.1111/j.1467-9965.2007.00323.x"
  arxiv_id: null
- title: "Volatility is (mostly) path-dependent"
  authors: ["Guyon, J.", "Lekeufack, J."]
  year: "2023"
  doi: "10.1080/14697688.2023.2221281"
  arxiv_id: null
- title: "The existence of probability measures with given marginals"
  authors: ["Strassen, V."]
  year: "1965"
  doi: null
  arxiv_id: null
- title: "Markov-Komposition und eine Anwendung auf Martingale"
  authors: ["Kellerer, H. G."]
  year: "1972"
  doi: "10.1007/BF01432281"
  arxiv_id: null
~~~

### Questions for Authors

1. How do you define dynamic arbitrage, and can you state the necessary/not-sufficient relation precisely for a surface process rather than a single surface? Which primary source do you regard as establishing it?
2. Why are Fengler (2009) and Homescu (2011) counted in the parametric family in Table 1 and Appendix B when your own prose classifies Fengler as constrained smoothing and Appendix D calls Homescu a survey with no construction? What are the corrected family counts?
3. Appendix D leaves 11 sources outside the four families ("None/soft", "Survey", "Evaluation/detection"). Is "no explicit enforcement" a fifth family, and if so, does the §2.6 claim that the taxonomy organizes the literature by where the constraint enters the pipeline survive? What happens to the counts if the sources without a mechanism are excluded?
4. For the "calibration map" sources (Bayer & Stemper, 2018; Bayer et al., 2025; Hoshisashi et al., 2023), is the guarantee inherited from the parent rough-volatility model or carried by the network? How should the taxonomy represent inherited guarantees?
5. Does Andrès et al. (2026) establish a dynamic-arbitrage condition or an empirical path-dependence property of the implied-volatility surface? If the latter, why is it in Table 3's dynamic-consistency evidence, and how do you reconcile Appendix D's "Dynamic test: Y" with Table 3's "no joint test"?
6. Would you extend the "dynamic no-arbitrage is the frontier" claim to the field, given the stochastic-implied-volatility and market-model literature (Schönbucher, 1999; Schweizer & Wissel, 2008; Buehler, 2006) that the corpus does not contain? If not, will you restore the corpus qualifier in the abstract and conclusion?
7. On the calendar condition: do you intend total implied variance non-decreasing in maturity at fixed log-moneyness, with call prices non-decreasing in maturity at fixed strike? The "maturity-monotonicity" shorthand should be corrected to avoid implying that implied volatility itself is monotone in maturity.

### Minor Issues

- §3.1's "in `deep-research` full mode" and §3.3's "does not trigger an advisory" are internal pipeline jargon; replace them with plain descriptions or move them to the AI-use statement.
- §2.2's "probabilistic scoring rule" should be "proper scoring rule."
- §5.2's "a projection assumes the repair map is idempotent and stable": idempotence is definitional for a projection operator; the substantive assumptions are closedness/convexity of the admissible set, existence and uniqueness of the projection, and stability under perturbations.
- §2.2 calls Fengler's constrained least-squares smoother an "early benchmark"; nonparametric implied-volatility estimation predates it by more than a decade, so either soften "early" or cite the earlier work.
- The reference list lowercases the arXiv DOI prefix (for example `10.48550/arxiv.1810.03399`, `10.48550/arxiv.2509.01743`). DOIs are case-insensitive, but the canonical arXiv prefix is `arXiv`; use the canonical form consistently.
- SSRN records are formatted with italic *SSRN* as if it were a journal; APA 7 preprint style would add a working-paper or preprint designator, and consistency with the arXiv entries would help.
- Table 7's SVI/SSVI/eSSVI row says a static guarantee holds "if parameters are in the admissible region," which glosses over the fact that the calendar-arbitrage constraints couple maturities in SSVI/eSSVI rather than acting per slice; one sentence in the caption would prevent misreading.
- The "American options beyond one source" scope note and Yao et al. (2026) inclusion should be reconciled (see W7).
