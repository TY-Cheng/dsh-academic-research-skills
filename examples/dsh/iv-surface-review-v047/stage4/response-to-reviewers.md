# Response to Reviewers

**Manuscript:** IVSURF-2026-11-23 — *Four Loci of Enforcement: Static and Dynamic No-Arbitrage in Equity-Index Implied-Volatility Surfaces, 2015–2026*
**Round:** 1 · **Decision answered:** Major Revision
**Revised manuscript:** `paper-draft-v2.md` (version 2.0)

---

## Preliminary notes

1. **Location references.** This letter points to numbered sections, subsections, tables, figure captions, and appendix items, not to page or line numbers. The revised manuscript is not typeset, so pagination does not yet exist; citing it would have meant inventing it.

2. **Reference list is frozen.** The corpus is fixed at 41 sources by construction (Section 3.1; Appendix B). The reference list is therefore unchanged: 41 entries, no additions, no removals, no substitutions, no new DOIs. Every reviewer request that would have required a new citation has been answered from inside those 41 sources, or declined — the single clear instance is Suggested item S6, answered under its own heading.

3. **No machine gate is claimed here.** The word-count report, the citation checker, and the acronym checker were run on the revised file and their output is reported in the accompanying `revision-log.md`. No other gate is claimed.

4. **Reliability figures now reported.** Section 3.4 carries the measured figures: a 16-row sample across six interpretive fields, 79 of 96 field codes in agreement. Evidence status agreed on 10/16 (Cohen's κ = 0.47), family on 12/16, comparability on 10/16, audit on 15/16, and time-axis and dynamic enforcement on 16/16 each. The pre-registered threshold is met only by the time-axis, dynamic and audit fields; the claims resting on the three failing fields are restated at the observed stability in Sections 3.3, 4 and 5.1, and the 17 cell disagreements are adjudicated row by row in the reliability record.

5. **Word count.** Body: 7,862 words (limit 6,000–8,000; internal target ≤7,800; 62 over target, within limit). English abstract: 249 words (limit 150–250). Chinese abstract: 491 characters (limit 300–500). Tables: 6. Figures: 2. References: 41.

---

## Required revisions

### R1 — Abstract asserts one certified object for all 41 rows `must_fix`

**Location.** English Abstract; Chinese Abstract; Section 7.1 (first takeaway); Section 2.3; Table 2; Appendix B (Family and Evidence columns).

**What changed.** The certified-object sentence is now scoped to the 31 construction rows and names what each group certifies. The abstract says that within the 31 construction rows the certified object is, as reported, a single date's surface — an admitted parameter set, an evaluated sample, an image, or an accepted sample — that the five condition-and-evaluation rows state or detect conditions without certifying a surface, and that the five seminal baselines certify none. The Chinese abstract carries the same three-way scope. Section 7.1 repeats the same three-way sentence rather than the universal claim, and the family summary in Table 2 now reports the certified object per family instead of implying one object corpus-wide.

**Evidence.** The claim is now consistent with Section 2.3's four loci and with the `Family`/`Evidence` columns of Appendix B: P/N/R/G rows construct or repair a single date's surface, C rows (C1–C5) state, detect, or review conditions, and S rows (S1–S5) are baselines. Section 5.1's audit recount and Section 3.2's evidence-status definitions use the same three-way grouping.

**Status.** Fully addressed.

### R2 — Proof and audit counts were not re-derivable; the 17/6/1 partition was not reproducible; G6 contradicted the universal negative `must_fix`

**Location.** Section 3.2 (paragraphs 2–3); Section 5.1 (recomputation paragraph); Table 3 and its note; Section 7.1 (fourth takeaway); Appendix B (`Evidence`, `Audit` columns); Appendix D.2, D.3, D.10.

**What changed.** Three things.

(a) *The two definitions are separated.* Section 3.2 now defines evidence status (proof / numerical test / assumption) and, in a separate paragraph, the audit row: a violation, residual, or defect statistic computed on the row's own fitted, repaired, or generated output, naming the conditions tested. The merged definition that let a numerical test and an audit count be read off the same sentence is gone.

(b) *The partition is recomputed from the ledger.* Section 5.1 now reports: 16 proof rows audit nothing, 1 proof row audits its own output (G6), 5 test rows audit their own output, 11 test rows report a numerical result that is not a violation statistic on their own output, and 8 assumption rows audit nothing — 16 + 1 + 5 + 11 + 8 = 41 rows, and 1 + 5 = 6 audit rows. Table 3's columns are now `Proof / Test / Assumption / Total / Audit rows / Time-axis rows` per family, and every one of those numbers is a tally of Appendix B rows.

(c) *The G6 overlap is disclosed from both sides.* Section 5.1 states that one of the six audit rows is also proof-level and that one of the 17 proof rows reports a violation rate on its own output, and says explicitly that these are the same fact stated from either side — the earlier 17 / 6 / 1 partition was that fact, not a third count. The universal negative ("will not find the pair") is gone from Section 7.1; the replacement states that proof and audit are nearly disjoint, that exactly one row is both, and that the one paired measurement is G6's on synthetic data.

**Evidence.** Section 3.2 (definitions); Section 5.1 (paragraph 2, `16 + 1 + 5 + 11 + 8 = 41`, `1 + 5 = 6`); Table 3 (six-column tally whose per-family rows sum to 41 and 6); Table 3 note (G6 named as the only dual-coded row); Appendix B (`Audit` column: Y for N2, N6, R5, R7, G5, G6 and N for the other 35; `Evidence` column: G6 = proof); Appendix D.10 (recomputation table listing each identity).

**Status.** Fully addressed.

### R3 — Coding reliability was not reported and absence claims were stated above the support `must_fix`

**Location.** Section 3.3 (final paragraph); Section 3.4 (new subsection, "Reliability of the Coding"); Appendix D.9 (reliability protocol); Appendix D.10.

**What changed.** Four additions.

(a) *A testable manual.* Section 3.3 now points to a coding handbook — Appendix D, reproduced in full in the manuscript and also shipped as `coding-handbook.md` — and states the three coding disciplines that the handbook makes reproducible (a proof about a projection map is proof for the map, not for repaired behaviour over dates; an architectural constraint is proof for its model class, not for sampled output; a reported violation rate without a structural guarantee is a numerical test even at zero). Appendix D defines every ledger field operationally (D.1–D.8), including the audit-row rule (D.3), time-axis engagement (D.4), dynamic enforcement D0–D3 with the model-class rule (D.5), and the metadata-only rule (D.8).

(b) *A stratified second-coder recheck.* Section 3.4 reports a 16-row stratified sample — two rows per family plus the four boundary cases — drawn as P1, P4, P7, N2, N5, R2, R3, R4, R5, G6, G7, C3, C4, C5, S1, S2. The second coder recoded six interpretive fields blind to the first coder's ledger: family, evidence status, audit, comparability class, time-axis engagement, and dynamic-enforcement code. Agreement is decided by a stated rule (≥0.85 overall agreement and Cohen's κ ≥ 0.70 for evidence status; below either threshold, the disagreements are adjudicated row by row and the affected claims are restated). The measured counts are reported in Section 3.4 and the cell-level adjudication is recorded with the coding records.

(c) *The single-coder limitation stays explicit.* Section 3.4 ends with the limitation in its own paragraph: 16 rows are a designed sample, not a random one, so the recheck measures the handbook's reproducibility rather than a population; the remaining 25 rows, and every row's interpretation against its full text, rest on one analyst. The absence claims in Sections 5.1 and 6.2 are stated at that strength — claims about how this corpus was coded under a published rule.

(d) *Scope of the claim.* No inter-rater agreement is claimed for the fields outside the six, and the six are reported at their measured agreement.

**Evidence.** Section 3.3 (last paragraph); Section 3.4 (whole subsection); Appendix D.9 (sample design, blinding, fields, thresholds, adjudication rule); Appendix D.10 (recomputation table).

**Status.** Fully addressed: the measured agreement figures are reported in Section 3.4 (evidence status 10/16, Cohen's κ = 0.47; family 12/16; comparability 10/16; audit 15/16; time-axis and dynamic enforcement 16/16 each), the threshold rule is applied in the text, and the 17 disputed cells are adjudicated row by row in the coding records.

### R4 — The search was not reproducible from the manuscript `must_fix`

**Location.** Section 3.1 (paragraphs 1–4); Appendix A.1 (Table A1, 31 queries); Appendix A.2 (Table A2, 40 discretionary exclusions); Appendix A.3 (the two replacements); Figure 2 (retrieval and screening flow).

**What changed.** Table A1 reproduces all 31 query strings, verbatim and in stratum order, with the eight strata and the record counts. Table A2 lists the 40 `RELEVANT_NOT_SELECTED` records by log index, year, and title, with the recorded reason for each and a column stating where the row is discussed. The log records a written reason for one of the 40 (log index 42, the displaced neural-network pricing record); for the other 39 the log carries the code but no free-text note, and Table A2 says so per row rather than inventing a rationale. Table A2's introduction states that these are discretionary selection judgements (corpus cap, family balance, recency, version precedence, stronger record in the same family), not eligibility failures.

The two post-screening replacements now have one account, used identically in Section 3.1 and Appendix A.3: both were replaced after abstract-level reading because the retained abstract did not fit the frozen inclusion rule (one had no enforcement claim; one was a foreign-exchange delta-condition paper outside equity-index scope), and neither failed metadata resolution or abstract reconstruction — no included record did, since all 41 resolve to a DOI-bearing index record with a full title match.

**Evidence.** Appendix A.1 (31 rows; matches `search/openalex_search.py` line for line); Appendix A.2 (40 rows; each with log index, year, title, code and the "not recorded" marker where applicable); Appendix A.3 (single replacement account, also summarized in Section 3.1); Figure 2 (775 requested → 750 returned → 430 unique → 389 excluded across eight codes → 41 included → 36 + 5 and 29 + 11 + 1).

**Status.** Partially addressed. A third party can rerun the 31 strings; it cannot reproduce the 40 discretionary selections from the log because free-text notes were retained for one of the 40 rows, and the manuscript says so per row in Table A2 and in Section 6.4. The residual is record-level rationales for the remaining 39 rows.

### R5 — The fit-error clause was adjudicated in Table 4 but was not in the declared H2 `must_fix`

**Location.** Section 1.2 (H2 statement); Table 4 (H2 row and its residual-uncertainty cell); Section 5.1 (hypothesis adjudication paragraph).

**What changed.** The clause is moved into the declared hypothesis rather than withdrawn. Section 1.2 now declares H2 with both clauses: that penalty and repair routes may displace rather than remove the constraint burden, absorbing it into weights, tolerances, and repair steps, **and** that they may fail to lower fit error relative to constrained constructions on the same data. The same sentence discloses that the second clause was added after the first coding pass, when one paired measurement (G6) made it checkable, and is disclosed as post hoc rather than pre-registered. Table 4's H2 row now states the fit-error clause and carries "formulated after the first coding pass (§1.2)" in its residual-uncertainty cell, and the Section 5.1 paragraph adjudicates both clauses (burden-displacement supported; fit-error clause unsupported) because no penalty or repair row reports a lower fit error than a constrained baseline on the same data and the one paired measurement reports a higher one.

**Evidence.** Section 1.2; Table 4 (H2 row, both clauses, post-hoc note); Section 5.1 (paragraph 4). The three statements are now mutually consistent.

**Status.** Fully addressed.

### R6 — SC3 was stated as c″ ≥ 0 instead of c″ − c′ ≥ 0 `must_fix`

**Location.** Section 2.1 (SC3 statement, derivation, and the two boundary relations); Appendix C.4 (the correction and the rows it touches); Appendix B (`Static` column); Appendix D.6.

**What changed.** Section 2.1 now states the butterfly condition in the Durrleman form: on the normalised call price c(k) in log-moneyness, no static arbitrage on strikes requires c″ − c′ ≥ 0, and the risk-neutral density is proportional to that expression via C″(K) = K⁻¹e^{−k}(c″ − c′), so the two printed forms coincide only where the first-order term vanishes. Two relations are stated. Relative to **SC2**, the corrected SC3 is not implied by non-negative implied variance: the printed older form was strictly stronger than needed, so a family satisfying SC2 could fail the printed SC3 while remaining admissible. Relative to **SC4**, the τ = 0 slice in the limit is tight for the corrected form and violated by the printed one: the corrected condition reduces to the density condition on the single slice, whereas c″ ≥ 0 fails there — for a Black–Scholes slice at k = −0.5 with σ√τ = 0.2, the computed values are c″ ≈ −0.53 and c″ − c′ ≈ +0.07, so the surface is admissible while failing the printed form. The boundary inconsistency the reviewer identified is therefore resolved by correction, not by disclosure.

Appendix C.4 records the correction and its re-examination: 39 of 41 rows state a condition subset containing SC3 (S4 and S5 claim no admissibility condition and are the two exceptions); all 39 were re-read against the corrected form; and no row's evidence status, audit code, time-axis code, dynamic code, or comparability code changes, because none of those columns was assigned from the algebraic form — a residual at a stated tolerance is a numerical test under either form, and a parameter domain that admits only admissible vectors is a proof under either form. The seven rows whose abstracts name conditions in the corrected family are named in C.4 (N6, G6, R5, G5, S2, R7, R6).

**Evidence.** Section 2.1 (SC3 statement, derivation, relations to SC2 and SC4 with the Black–Scholes numbers); Appendix C.4 (correction record and re-examination); Appendix B (`Static` column re-checked for all 41 rows); Appendix D.6 (coding rule for "the subset of SC1–SC5 the row's claim expresses").

**Status.** Fully addressed.

### R7 — Appendix B lacked per-row time-axis and dynamic-enforcement coding; the "0 of 41" claim was not tied to a rule `must_fix`

**Location.** Section 2.2 (D0–D3 rule, the model-class rule, the ten named rows); Appendix B (`Time`, `Dyn` columns, all 41 rows); Table 3 (`Time-axis` column); Section 5.1 (dynamic paragraph); Section 6.2 (last sentence); Appendix D.4, D.5.

**What changed.** The enforcement rule is stated once in Section 2.2 and applied in Appendix B. Dynamic enforcement is coded D0 (none), D1 (declares a process-level condition without checking it), D2 (inherits a model-class property), or D3 (states a process-level condition and reports checking it). The model-class rule is explicit: an inherited guarantee is coded D2 and never as enforcement, because a property of a stated model class is not a reported check of a dynamic condition. The result is D3 = 0, D2 = 3 (G1, G7, C3), D1 = 4 (P8, C2, C5, R8), D0 = 34.

All ten time-engaging rows are named in the body — P8, R8, G1, G2, G3, G7, C2, C3, C5, S5 — with the per-family split in Table 3 (P 1, N 0, R 1, G 4, C 3, S 1). The absence claim is stated exactly as strongly as the rule licenses: Section 5.1 says "0 of 41 rows at D3 — 0 of the 36 in-window records and 0 of the 31 construction rows", with the three D2 and four D1 rows named, and Section 6.2 restates that the three model-class rows are coded inherited rather than enforcement, so the count does not rest on a reader's intuition about what "the model is arbitrage-free" implies.

**Evidence.** Section 2.2 (rule, model-class rule, ten rows); Appendix B (`Time` = Y for the ten rows and N for 31; `Dyn` = D2 for G1, G7, C3; D1 for P8, C2, C5, R8; D0 for the remaining 34); Table 3 (`Time-axis` column sums to 10); Section 5.1 (paragraph 3); Appendix D.4–D.5.

**Status.** Fully addressed as a coding and reporting matter. A reader who codes differently can now see the rule and disagree with it pointwise; the rule itself is not claimed to be the only defensible one.

### R8 — Residual rates were read as findings without an acceptance criterion `must_fix`

**Location.** Section 5.4 (new subsection, "From Residual to Acceptance Criterion"); Table 6 (cost and coverage rows); Section 5.3; Section 6.3 (the agenda's first study).

**What changed.** Section 5.4 turns the residuals into a specification. A frequency becomes a validation grade only when five inputs are supplied: a loss function (fraction of quoted strikes in violation, maximum violation in price units, a surface-level maximum over a day, and the day-aggregation rule are different losses with different rates); a tolerance (numerical or exact); test power (the probability of detecting a violation of a stated size, which requires a stated alternative); regime coverage (which markets, tenors, strikes, years, and stress periods the test covers); and an independent check (whether the test was run by someone other than the constructor, on data not used to fit). The subsection then states what the corpus supplies: one row (G6) states a tolerance and a loss together, on synthetic data, over 15 runs, so it supplies two of five inputs and no power estimate; one row (R5) reports a rate over a real panel with a stated protocol but no tolerance; no row estimates test power or a noise floor; no row runs an independent check on the constructor's output. The count is therefore stated explicitly: zero of the six audit rows supply three or more of the five inputs, and zero of the 41 rows supply all five. The concrete consequence follows: no number in Sections 4 and 5 is a grade, and the agenda's first study is a power-and-noise-floor study precisely because four of the five inputs depend on it.

**Evidence.** Section 5.4 (paragraphs 1–3); Table 6 (`Computational cost` row: about five assertions, none comparable); Section 5.3 (the one paired measurement); Section 6.3 (study 1, dependencies named).

**Status.** Fully addressed.

### R9 — Cost and build-or-buy claims exceeded what the corpus licenses `must_fix`

**Location.** Section 7.2 (payoff paragraph); Section 5.3 (cost paragraph); Table 6 (`Computational cost`); Section 7.1 (ranking paragraph).

**What changed.** Section 7.2 now separates what the corpus **establishes** from what it **asserts**, in that order and with the same words used in Section 5.3. Established: four enforcement loci, four evidence types, the near-disjointness of proof and audit, and one paired measurement in which the stronger guarantee carried the higher fit error (G6). Asserted: cost — about five rows state a computational cost, none measures one on a common grid, and no row's claim is reproducible as a comparison. For a build-or-buy decision the manuscript now says what the corpus actually offers: it does not price a method and does not identify a best one; it tells a decision-maker which guarantee a candidate's evidence carries, what that evidence omits, and where the omission would have to be closed before two candidates' numbers could be compared. The earlier phrasing that the triple identifies "what each method's guarantee is worth and what it costs" is withdrawn by name in the same paragraph as an overclaim the findings do not license.

**Evidence.** Section 7.2 (payoff paragraph, established/asserted split, explicit withdrawal); Section 5.3 (cost paragraph: one-sided measurement, "about five" assertions); Table 6 (cost row: asserted, 0 comparable).

**Status.** Fully addressed.

---

## Suggested revisions

### S1 — Abstract composition did not sum to 41 `should_fix`

**Location.** English Abstract; Chinese Abstract.

**What changed.** The composition is now exhaustive and sums: 29 peer-reviewed articles or proceedings papers, 11 preprints, and one practitioner magazine article, against 41 sources (36 in-window plus 5 seminal precursors). Both abstracts carry the same three-term composition, and Section 3.1's corpus paragraph uses the same figures, so the abstract no longer fails to decompose the total.

**Evidence.** English Abstract; Chinese Abstract (含29篇同行评审论文、11篇预印本与1篇业界杂志文章); Section 3.1 (paragraph 3); Appendix D.10 (composition identity 29 + 11 + 1 = 41).

**Status.** Fully addressed.

### S2 — Replace ASCII exhibits with final figures; remove stage labels and production placeholders `should_fix`

**Location.** Front matter; Figure 1 (Section 2.3); Figure 2 (Section 3.1); Appendix C.2; Appendix D.8.

**What changed.** The front matter now carries the version line `v2.0` with author and date, and no pipeline stage labels remain anywhere in the manuscript (no "Stage 2.5", no "Phase 7", no "to be typeset"). Figure 1 is now a labelled conceptual schematic of the enforcement triple and the four loci, with a caption that describes what it shows and what it does not; Figure 2 is a labelled schematic of the retrieval and screening flow with the eight exclusion codes and their counts, likewise captioned. Both are conceptual figures — block-diagram schematics rather than rendered plots — and the captions say so, so a typesetter knows they are re-drawn artwork rather than data graphics. Appendix C.2 describes the earlier eight-axis instrument without stage numbering, and Appendix D.8 refers to "the corpus's earlier appraisal record".

**Evidence.** Front matter (lines 1–6 of the file); Figure 1 caption; Figure 2 caption; Appendix C.2; Appendix D.8.

**Status.** Fully addressed as content. The two figures are conceptual schematics; if the journal requires vector artwork, they are the two that must be redrawn, and the captions are written so that redrawing changes no claim.

### S3 — Define or delete the VI/VII labels `should_fix`

**Location.** Section 3.2 (paragraph 3); Appendix B (`Level` column); Appendix D.8.

**What changed.** The labels are defined rather than deleted. Section 3.2 defines Level VI (a single descriptive, quantitative, or qualitative study) and Level VII (expert commentary or a narrative review) on the seven-level appraisal hierarchy, states the corpus split (40 Level VI, one Level VII — Niu, 2015), and prints the level per row in Appendix B, with the operational definition in Appendix D.8.

**Evidence.** Section 3.2 (paragraph 3); Appendix B (`Level`: VII for C2, VI for the other 40); Appendix D.8.

**Status.** Fully addressed.

### S4 — Make the metadata-only rule consistent across Section 3.1/3.2, Section 5.1 and Appendix B `should_fix`

**Location.** Section 3.2 (paragraph 3); Section 5.1 (paragraph 4); Appendix B (intro and `Coverage` column); Appendix D.8.

**What changed.** The rule is now stated once, in one sentence, and applied identically in three places: a metadata-only row is cited only for what its title asserts, **is** counted in every structural tally — it is one of the eight assumption rows — and is never counted as evidence that its own claim holds. Section 3.2 states the rule; Section 5.1 applies it to the assumption-row tally; Appendix B's introduction and `Coverage` column mark the three metadata-only rows (P4, P7, R4); Appendix D.8 defines it.

**Evidence.** Section 3.2 (paragraph 3); Section 5.1 (paragraph 4); Appendix B (intro; `Coverage` column: metadata-only for P4, P7, R4); Appendix D.8.

**Status.** Fully addressed.

### S5 — Complete Appendix B so that body counts are recomputable `should_fix`

**Location.** Appendix B (13 columns); Appendix C.5; Appendix D.10.

**What changed.** Appendix B now carries, per row: ID, source, family, evidence status, audit, static-condition subset, time-axis engagement, dynamic-enforcement code, evidence level, comparability class, coverage, peer-review status, and the sections that cite the row. The two fields the earlier version lacked (time axis, dynamic enforcement) are now per-row values rather than body prose. The composite A/B/C quality grade is **withdrawn** rather than printed, for the reason stated in Appendix C.5: two of its six criteria were free-text judgements the ledger does not carry, so no reader could recompute a grade from Appendix B, and printing the rows would present a judgement as a derivation. Every count the body reports is now a tally of Appendix B columns, and Appendix D.10 prints each identity (17 + 16 + 8 = 41; 16 + 1 + 5 + 11 + 8 = 41; 1 + 5 = 6 audit rows; 0 + 3 + 4 + 34 = 41 dynamic codes; 12 = 11 + 1 non-peer-reviewed; 29 + 11 + 1 = 41; 36 + 5 = 41).

**Evidence.** Appendix B (13-column table, 41 rows); Appendix C.5 (withdrawal rationale); Appendix D.10 (recomputation table).

**Status.** Fully addressed, with the A/B/C column deliberately withdrawn rather than completed — see C.5 for why that is the only recomputable option.

### S6 — Cite the canonical dynamic-consistency source `should_fix` — **declined**

**Location.** Section 2.2; Section 6.2; Appendix D.5.

**Why declined.** The reference list is frozen at the 41 corpus sources for this revision (Section 3.1; Appendix B); adding the canonical source would change the frozen set and invalidate every count in the paper. The request is therefore declined, and the manuscript answers it as far as the freeze allows: Section 2.2 states the dynamic condition in prose and defines the D0–D3 codes so that the absence claim does not depend on the missing citation, Section 6.2 records that the only corpus source that discusses dynamic conditions at any length (Niu, 2015) does not test them, and Section 6.4 states the resulting limitation — the corpus has no canonical statement of dynamic consistency, so the review's dynamic predicate is its own operational definition, published in Appendix D.5 for exactly that reason.

**Status.** Declined under the frozen-reference constraint; limitation disclosed in the manuscript rather than hidden.

### S7 — Name the audiences outside the research core and the competence each needs `consider`

**Location.** Section 6.4 (third paragraph).

**What changed.** A paragraph now names three adjacent audiences that are neither claimed as served nor excluded, each with its competence: model validators and supervisors, who would need the acceptance-criterion inputs of Section 5.4 and the competence to supply the power and regime fields themselves; model-risk and audit functions, whose competence is operational back-testing rather than surface construction and who need deployment evidence this corpus does not carry; and end investors, for whom neither the conditions nor the rates are decision-relevant without an intermediated summary, and whose required competence is reading a validation report rather than a surface.

**Evidence.** Section 6.4 (paragraph 3).

**Status.** Fully addressed.

### S8 — State the agenda's dependency order, data access, and ownership `consider`

**Location.** Section 6.3 (studies 1–7 and the closing paragraph).

**What changed.** The seven studies are now ordered by dependency, and each carries three fields: what it depends on, what data access it needs, and who could own it. The power-and-noise-floor study is first, because four of the five Section 5.4 inputs depend on it; the dynamic enforcement test depends on the first study's power estimates and needs a data-holding group (exchange or vendor quote archive); the pre-registered head-to-head needs frozen protocols and a single index panel; the residual audit for proof constructions needs only published constructions and a reviewer with no stake in them; the remaining studies are scoped by the same three fields, with the one structural constraint stated explicitly — the head-to-head (study 3) cannot precede the dynamic test (study 2), and study 6 cannot precede study 3.

**Evidence.** Section 6.3 (studies 1–7, each with dependency, data access, owner).

**Status.** Fully addressed.

### S9 — Audit the 40 discretionary exclusions for dynamic tests `should_fix`

**Location.** Section 6.2 (excluded-pool audit paragraph); Appendix A.2 (Table A2, discussion column).

**What changed.** The excluded pool was audited at title level. Eight of the 40 titles carry temporal or martingale vocabulary; all eight are recorded under the same code (`RELEVANT_NOT_SELECTED`), so their exclusion is a discretionary selection judgement rather than an eligibility failure, and five of the eight are forecasting or hedging papers while the other three model or reconstruct surfaces from martingale structure without announcing a path-level test. The paragraph is explicit about what this can and cannot support: it is a title-level finding — the excluded records were never read at abstract level — so the excluded pool cannot support the void claim and cannot by itself overturn it; what it does show is that the review did not knowingly discard a record whose title announced the test it reports as absent. Table A2's discussion column carries the same eight markers so the audit is checkable.

**Evidence.** Section 6.2 (audit paragraph, eight titles by log index); Appendix A.2 (40 rows with the discussion column); Section 6.4 (limitation paragraph restating the title-level bound).

**Status.** Fully addressed at the strength the audit permits.

### S10 — Analyse the cost and incidence of the reporting triple `should_fix`

**Location.** Section 7.2 (incidence paragraph).

**What changed.** A paragraph now states the cost and who bears it: the triple costs about three sentences of prose per construction and one table row per family, with no new dataset, computation, or notation; the author bears it; the reviewer or editor enforces it at no cost beyond asking; the reader receives a checkable claim rather than a validation; and the model validator, who needs the five Section 5.4 inputs, bears a cost the triple does not remove. The proposal is then marked with its incidence stated and its effects unmeasured: no study in the corpus reports what a reporting standard changed, so the claim that publication norms would follow is asserted rather than established.

**Evidence.** Section 7.2 (incidence paragraph); Section 5.4 (why the validator's cost is not removed).

**Status.** Fully addressed.

### S11 — Weaken "no ranking is possible" to what the corpus licenses `should_fix`

**Location.** Section 7.1 (fourth takeaway); Section 7.2 (closing).

**What changed.** The universal negative is replaced by a bounded claim. Section 7.1 now says that the corpus's reported numbers do not license a ranking — no row reports a common protocol, a shared tolerance, and a common metric on the same data, so a league table would compare different objects — and that a common protocol would produce a ranking, which is why the third agenda study is a pre-registered head-to-head. Section 7.2's closing repeats the weaker form: the framework is not a ranking and does not license one, and the useful question is which admissibility claim a construction licenses, at what tolerance, and how it was checked.

**Evidence.** Section 7.1 (fourth takeaway); Section 6.3 (study 3); Section 7.2 (closing paragraph).

**Status.** Fully addressed.


---

## Stage 4′ addendum (v2.0 → v3.0)

The verification re-review (Stage 3′) returned Minor Revision with five editing corrections, all applied in v3.0 without new evidence: (1) a duplicated corpus-construction paragraph in Section 3.1 was removed; (2) Appendix D.10's peer-review tally corrected from "30 yes, 11 no" to "29 yes, 12 no" to match Appendix B (11 preprints plus the practitioner article); (3) the AI Use Disclosure sentence that described the recheck inputs as "marked for completion" now states that the figures are reported in Section 3.4 and the adjudication is recorded; (4) the abstract's "proof-level and test-level … nearly disjoint" sentence now states the corrected proof/audit finding (one of the six audit rows is also proof-level), matching Sections 1.1, 5.1 and 7.1; (5) the response letter and revision log no longer describe the reliability figures as left to the operator. The body is 7,761 words in v3.0; the reference list, tables, figures and every count are unchanged.
