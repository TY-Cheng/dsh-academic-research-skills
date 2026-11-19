# Editorial Decision — ARS Panel

**Manuscript:** *Arbitrage-Free Implied Volatility Surface Construction: A Structured Literature Review of Parametric, Nonparametric, and Neural Approaches*
**Manuscript file:** `examples/dsh/iv-surface-review/stage5/paper-final.md`
**Panel:** Journal-Fit + R1 (methodology) + R2 (domain) + R3 (perspective) + Devil's Advocate; field analysis; editorial synthesis by the lead.
**Decision:** **Major Revision**

## 1. Decision and consensus

All five seats independently recommended **Major Revision**. No seat recommended Accept, Minor Revision only, or Reject; no seat identified a Critical issue. The core contribution survives, the paper's disclosures are unusually honest, and the required changes are achievable within the declared structured-narrative-review type without new data collection. The panel's concerns are load-bearing but repairable: the paper needs a substantial revision of its originality claim, its selection account, its taxonomy coverage, its evaluation matrix, and the scope of two headline findings. Copy-editing alone would not be sufficient.

This is a Major Revision, not a Reject, because the guarantee-family reframing is genuinely useful, the static/dynamic distinction is correct in substance, the corpus and its limits are disclosed, and the appendices provide an audit trail that most narrative reviews lack. The revision must preserve those assets rather than retreat from them.

## 2. Basis of the decision

The seats converge on six major issues. They are stated here as an editorial synthesis; the seat reports remain the authoritative source for each reviewer's wording and evidence.

### M1 — Originality and positioning are asserted, not demonstrated

The paper names Homescu (2011) as the closest prior survey and credits it with making "the constraint taxonomy explicit", then claims three differences without comparing the two taxonomies. The Journal-Fit seat calls this the decision-bearing originality gap; the Devil's Advocate calls the contribution potentially "a relabeling of standard constrained-estimation classes". The paper does not need to abandon the contribution, but it must show the delta: what Homescu's categories are, how the four enforcement families overlap or refine them, and what the seven-dimension matrix adds over prior evaluation checklists. The article-type/venue positioning also needs to be reconciled with the corpus and apparatus actually carried.

### M2 — The selection account is not reproducible at the record level

R1's central finding is that the reported 351 → 40 flow describes a rationale, not the executed selection. Retrieval was capped at 25 records per query against much larger match pools; a post-retrieval ranking by query multiplicity and citation count produced a 120-record shortlist containing all 40 included records; the 311 non-advanced records were not retained or individually coded. The operative selection signal is therefore relevance and popularity, not a documented eligibility rule. The paper should either (a) add the 120-record shortlist, the ranking rule, and a record-level exclusion log or (b) describe the selection as purposive and scoped, removing "reproducible" from the corpus claim while keeping it for query execution. The Devil's Advocate adds that the 24-query vocabulary pre-selects guarantee-claiming papers, so the corpus cannot test whether guarantee ambiguity is field-wide.

### M3 — The four-family taxonomy is not a partition of the corpus

R2 and the Devil's Advocate both find that the taxonomy covers 29 of 40 sources as printed. Eleven rows carry no enforcement family (eight "None/soft" and three survey/evaluation/detection rows); three calibration surrogates are coded "Construction (calibration map)" with no static test, although the paper's own definition says construction carries the admissible region in the model. The paper needs a fifth category — "no guarantee claimed / evaluation only" — a corrected calibration-map coding, and a reported coverage rate. The taxonomy should be presented as an interpretive primary-mechanism classification, not as an exhaustive partition.

### M4 — The seven-dimension matrix is not yet an operational instrument, and its evidence is not coded

R3's strongest finding is that Table 4 names dimensions and representative metrics but supplies no measurand, unit, sampling/filtering convention, tolerance, or pass/fail rule. Three dimensions are conceded to have no accepted metric. The table's "reporting in corpus" column is not backed by source-level coding. R3 and the Devil's Advocate both ask for a specification layer: a proposed measurand and protocol per dimension, a report-or-declare template, and a source-level coding matrix (or at least per-dimension counts). Alternatively, the paper should relabel the matrix as a proposal and remove the phrase "minimum reporting standard" until the measurement layer exists.

### M5 — Two headline findings escape their corpus scope, and one static/dynamic sentence is technically wrong

The abstract and conclusion promote "dynamic no-arbitrage is less standardized and less frequently evaluated" and the absence of a shared benchmark to field-level claims, while §4.4 concedes that the queries emphasized static-arbitrage vocabulary and that dynamic coverage may be under-sampled. §5.3 then turns the corpus absence into a supervisory implication. The qualifier is stated once and overridden later. The static/dynamic discussion also contains a technically wrong sentence — that a single static-arbitrage-free surface can be "inconsistent with a joint model" — which should be corrected. The abstract, findings, conclusion, and §5.3 must carry the corpus scope consistently; the supervisory sentence should be deleted or re-scoped.

### M6 — The practical instrument contradicts the organizing claim and the benchmark agenda is under-specified

Table 7 is described as a decision guide "by guarantee family" but is organized by method families and makes unanchored comparative claims about interpretability and cost. A reader following it chooses a method family, not a guarantee. The shared-benchmark agenda also lacks the two binding constraints R3 names: the input pipeline (forward/discount curves, quote filters, de-Americanization, moneyness grid) and data access/governance (SPX licensing, ownership, funding, versioning). The table should be rebuilt on the enforcement axis with corpus anchors, or cut; the benchmark agenda needs an input specification and a governance paragraph.

## 3. Minor issues

The panel identified a consistent set of bookkeeping and consistency defects that should be fixed in the same revision:

- The abstract's six-gap list does not match §5.5/Table 8 (cross-market evidence vs head-to-head enforcement).
- §4.7's tension counts disagree with Table 5 (five/four resolved; one/two not applicable).
- Appendix D codes dynamic tests for Andrès et al. (2026) and Vuletić and Cont (2025) that conflict with Table 3 and §4.4.
- Fengler (2009) is double-bucketed as parametric and nonparametric.
- Table 1 is labelled "method family" but contains pipeline-role buckets; "Constraints/evaluation" includes neural work.
- Table 3 includes the title-level Horvath et al. (2021) row while §4.4 says it is not used for a substantive dynamic claim.
- The 60% peer-reviewed, 30% currency, and 70% concentration thresholds lack provenance.
- "Reproducible" is used for both query execution and the purposive corpus.
- Table 4's "interpretability" conflates auditability/verifiability with explainability.
- The proposition count and the Table 7 caption/headers need reconciliation.

## 4. Strengths to preserve

- The guarantee-family reframing — "which mechanism carries the claim?" — is the paper's best idea and should survive revision.
- The static/dynamic separation and the explicit finding that most neural evidence is static-only are correct and operationally important.
- The disclosure of the corpus limits (no full texts, ten preprints, four partial abstracts, one title-level record, 311 uncoded records, HTTP 429 failures) is exceptional and should not be softened.
- Appendices B, D, and E provide a source-level audit trail; the revision should use it rather than replace it.
- The propositions with explicit falsifiers and the "what would change this map" paragraph are the right posture for a review agenda.
- The "what this review can and cannot support" paragraph is a model of claim bounding and should survive.

## 5. Calibration and panel note

All seats report `NOT_CALIBRATED`. The field analysis reports `criteria_binding_unavailable`: no author-confirmed `ReviewTargetContext` or target-journal criteria were supplied, so no seat makes a venue-alignment claim; venue remarks are advisory. Role separation here is a division of review labour and prompts, not a claim of independent error processes or statistical independence. The editorial decision is a synthesis of five seat reports and the field analysis; it does not rewrite any seat verdict and is not an arithmetic average of them.

## 6. Required action

Revise against the roadmap in `examples/dsh/iv-surface-review/stage3-team/revision-roadmap.md`. The six major items are required for a re-review; the minor items are required for copy-editing before the next decision. No new literature search is required for this revision, and the declared structured-narrative-review type should be retained. A re-review should verify each roadmap item against the revised text and the appendices, not against the author's response letter alone.
