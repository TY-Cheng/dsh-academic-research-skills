# Methodology Review Report (Peer Reviewer 1)

### Reviewer Identity

**Seat.** R1 — Methodology (evidence synthesis and review-protocol specialist).

**Remit.** Review protocol and review type; search and selection reproducibility; screening, exclusion, and selection bias; evidence appraisal and grading; synthesis validity and coding reliability; claim–evidence alignment.

**Out of scope for this seat.** Literature completeness, citation accuracy, and taxonomy validity are R2's remit; practical and cross-disciplinary impact is R3's. Findings outside these boundaries are not scored here.

**Materials read.** `examples/dsh/iv-surface-review/stage5/paper-final.md` (v4.0, 603 lines); `examples/dsh/iv-surface-review/stage3-team/field-analysis.md`; and the reproducibility artifacts the paper itself cites (`examples/dsh/iv-surface-review/search/openalex_search.py`, `openalex_candidates.json`, `selected_sources.json`). I did not read any other seat report. No #683 C1–C5 criterion set was supplied, so criterion sources below are the role prompt's review protocol, the R1 configuration card, and the paper's own declared review type (§3.1), which the field analysis establishes as the yardstick for this article class.

### Overall Recommendation

**Major Revision.**

### Confidence Score

**4 / 5.** I reconciled the paper's counts against the frozen artifacts and read the executed discovery script line by line, so protocol-level judgements rest on primary evidence. I did not re-run the OpenAlex queries, and no full texts exist in the record, so I cannot verify what a widened retrieval or a full-text pass would have found; corpus-level conclusions are therefore bounded by the frozen metadata.

### Calibration Status

`NOT_CALIBRATED`

### Criterion-Bound Judgements

| Dimension / criterion | Criterion source | Judgement | Evidence anchors | Rationale | Uncertainty or scope limit | Decision bearing? |
|---|---|---|---|---|---|---|
| C1 Research-question–method alignment | Role prompt Review Protocol Step 1; R1 card remit 3 | MEETS | text: §1.3 | The three aims (organize by mechanism, assess evidence strength, identify gaps) are answered by the enforcement taxonomy (§2.6, §4.2), the evidence matrix (§3.5), and the gap agenda (§5.5) | None identified at design level; aim (b) instrumentation is judged separately under C5 | No |
| C2 Review-type declaration and protocol coherence | Role prompt Step 2; R1 card remit 3; paper §3.1 | MEETS | text: §3.1 | The type, non-claims, and screening vocabulary are stated before any corpus numbers appear and are repeated in §3.7 and Appendix C | None identified | No |
| C3 Search and selection reproducibility | Role prompt Step 3; R1 card remit 1 | PARTLY_MEETS | table: Appendix E | The query log reconciles exactly, but the executed parameters (sort, pagination, filters) and the post-retrieval ranking rule are not documented | Sort order and relevance ranking are untested here | Yes — Major W2, W6 |
| C4 Screening and exclusion transparency | Role prompt Step 3; R1 card remit 1–2 | PARTLY_MEETS | absence: Appendix C — expected a record-level excluded list or a sampled exclusion audit; checked §3.3, §3.7, Appendix A, Appendix C | Category-level counts only; no dual screening, no agreement statistic, no spot-check of the 311 non-advanced records | The paper explicitly disclaims a full audit, which limits but does not remove the inference risk | Yes — Major W4 |
| C5 Evidence appraisal and grading | Role prompt Steps 4–5; R1 card remit 2 | DOES_NOT_MEET | text: §3.5 | Level VI/VII grading is publication-type accounting; no appraisal items, no risk-of-bias or quality instrument, no within-level distinction | Abstract-level appraisal is plausible but is not the instrument used | Yes — Major W1 |
| C6 Claim–evidence alignment | Role prompt Step 5 | PARTLY_MEETS | text: §4.5 | Body hedges are precise and repeated; the abstract and the Finding 3 heading still generalize a retrieval artefact to the field | Reader-dependent: the hedge and the generalization sit one paragraph apart | Yes — Major W3, W5 |
| C7 Synthesis and coding reliability | Role prompt Step 5; R1 card remit 3 | PARTLY_MEETS | table: Table 5 | The convergence rule is stated; the tension counts in §4.7 contradict the table; two classification inconsistencies appear in Appendix D | No independent coder, so reliability cannot be estimated | No (peripheral to the core claim) |
| C8 Reproducibility of materials | Role prompt Step 6 | MEETS | dataset: §3.7 | Scripts, candidate pool, and frozen 40-record corpus all exist and reconcile; the 24-query log matches Appendix E with zero mismatches | No archival identifier or version pin was checked | No |
| C9 Descriptive-count integrity | Role prompt Step 4a (adapted: no inferential statistics) | PARTLY_MEETS | table: Table 1; Appendix B Level column; Appendix D | All declared totals reconcile on recount (40 = 30 + 10; 18 + 8 + 7 + 6 + 1 = 40; preprint rows = 10) except the currency split, which the frozen metadata renders 13/27 rather than 12/28 | Currency split depends on a citation-year convention that is applied inconsistently | Yes — Minor W8 |
| C10 Statistical reporting adequacy | Role prompt Step 4a | NOT_ASSESSED | absence: §3.5 and §4 — expected test statistics, means/SDs, p-values, or degrees of freedom to recompute; checked §4.1–§4.7, Tables 1–5 | The review reports no inferential statistics and performs no meta-analysis, so none of the four bounded recompute procedures has a value to operate on | Not applicable to a narrative synthesis | No |

**Note.** Do not total, weight, average, or mechanically map these judgements to the recommendation. Each row is an independent observation; the overall recommendation follows the decision-impact argument in Summary Assessment and Weaknesses.

### Summary Assessment

This is an unusually well-declared review: the type is named, the corpus is frozen, the search log reconciles with Appendix E, and the limitations are quantified and carried into the claim ceiling. Judged against its own declared class — a structured narrative review — the protocol is coherent and most conclusions stay inside the evidence. Three method commitments nevertheless fall short of what the paper's own aims require. First, aim (b), assessing the strength of evidence, is instrumented only by publication type (Level VI/VII), which is venue accounting rather than appraisal. Second, the reported 351→40 flow does not describe the executed selection: retrieval was capped at 25 records per query against match pools of 114 to 100,152, and a post-retrieval ranking by query multiplicity and citation count produced a 120-record shortlist that contains all 40 included records; the operative selection signal is therefore relevance and popularity, not a documented eligibility rule. Third, method-level coding rests on abstracts with no full-text validation subsample, so coding error is unmeasured while Table 4 reports uncounted frequency labels. Because the taxonomy is offered as a proposal and the headline claims are hedged, these are re-basing and documentation failures rather than fatal ones, and each is repairable within the declared scope; that is why the recommendation is Major Revision rather than Reject.

### Strengths

1. **The review type is declared before the apparatus, and the non-claims are specific.** §3.1 states the class and its limits in one paragraph, and §3.7 repeats them in operational terms. A reader cannot mistake this for a systematic review, which is the failure mode this genre usually has. Evidence anchor: text: §3.1 — "not a systematic review, not PRISMA-compliant, and not registered", with the flow immediately characterized as "a screening rationale, not a record-level audit".

2. **The executed search is genuinely re-runnable and reconciles with the printed log.** I checked `search/openalex_candidates.json` against Appendix E: 24 queries, all with 25 retrievals, match counts identical in all 24 cases, 600 records retrieved and 351 unique after deduplication. All 40 included records are present in the candidate pool (39 by DOI, 1 by title). The frozen corpus `selected_sources.json` carries the metadata the paper says it carries. Evidence anchor: table: Appendix E — 24 queries with match counts and retrievals, reconciled line by line against the stored query log.

3. **Descriptive counts reconcile across abstract, body, tables, and appendices.** On recount, 30 peer-reviewed plus 10 preprints; 18 + 8 + 7 + 6 + 1 = 40; Table 1's per-family peer-reviewed splits match the Appendix B Level column exactly (7 = 6 + 1; 6 = 4 + 2; 18 = 12 + 6; 8 = 7 + 1; 1 = 1 + 0); the 10 preprint rows enumerated in Appendix D's note are exactly the rows coded VII in Appendix B; 39 DOIs plus one HAL record; 39 abstracts present plus one absent. Evidence anchor: table: Table 1 against Appendix B (Level column) and Appendix D (method-family column) — all 40 rows reconcile.

4. **Limitations are quantified, not decorative, and they propagate into the claim ceiling.** The paper does not merely list limits; §5.5 converts them into an explicit statement of what the review cannot support, and the abstract carries a corpus-scoped qualifier. Six limitations are given with numbers, not adjectives. Evidence anchor: text: §5.5 — "It cannot support a method ranking, a claim that no benchmark exists anywhere, a regulatory determination, or a full-text assessment of method behaviour."

5. **The adversarial checkpoint is disclosed with its severity and its residual.** A Devil's Advocate pass is reported at the level of the issues it raised, not as a generic assurance, and one tension (CP-004) is left flagged unresolved rather than closed. This is the behaviour one wants from a review that cannot fully resolve its own tensions. Evidence anchor: text: §5.4 — "returned REVISE with five Major issues", followed by the five named issues and the statement that they were addressed by hedging rather than resolved.

6. **Eligibility is stated in operational terms and no record was hand-added.** The primary-study rule names the unit of analysis and the admissibility categories, and the artifacts show all 40 records trace to the documented query set rather than to snowballing. Evidence anchor: dataset: §3.7 — `search/selected_sources.json`, whose 40 records all appear in `search/openalex_candidates.json`; the rule itself is stated at §3.2 as sources with "a static/dynamic no-arbitrage contribution".

### Weaknesses

1. **Aim (b) is not instrumented: publication type is used as a proxy for evidential strength, and no appraisal was performed.**
   *Problem.* The review declares that it will "assess the strength of the evidence for each family at abstract level", then implements strength as a two-level venue label: Level VI for a peer-reviewed study, Level VII for a preprint, review, or working paper. No item assesses design, data, benchmark, baseline, or whether violations were tested; no source is downgraded for a weak test or upgraded for a replication.
   *Why it matters.* The paper repeatedly converts this label into strength claims — "strong evidence for the parametric construction" (§4.1), "The evidence is therefore moderate, not settled." (§4.3), "neural claims are weaker than the prose sometimes implies" (§5.4). Those sentences are evidence-appraisal conclusions drawn without an appraisal instrument, and a peer-reviewed paper with a single simulated dataset is graded above a preprint with out-of-sample tests. This is the gap between the review's declared aim and its method.
   *Improvement.* Either add a minimal abstract-level appraisal rubric (three anchors: data source, comparison baseline, reported violation test) and publish it as a per-source column with the level, or demote aim (b) to publication-type accounting and delete the strength adjectives.
   *Severity.* Major.
   *Evidence Anchor.* text: §3.5 — "Evidence levels follow the corpus grading: Level VI for a single peer-reviewed study and Level VII for a preprint, review, or working paper."
   *Confidence.* 5/5 — this is a direct comparison of the stated aim with the stated instrument; no inference about the underlying studies is required.

2. **The executed selection is a popularity-ranked slice, and the printed 351-record screening flow does not describe it.**
   *Problem.* `openalex_search.py` retrieves 25 records per query for all 24 queries, then sorts the 351 unique records by `(number of queries that surfaced the record, citation count)` and writes the top 120 to a shortlist file. All 40 included records sit inside that top 120 (ranks 1–116 of 351; 29 are in the top 60). Either selection was performed on the ranked shortlist, or the same two signals drove it; in both cases the effective selection rule is multi-query relevance plus citation count, and it is documented nowhere in the paper, which describes the operation instead as a 351-record title/abstract screen (§3.3) with the 311 remainder "not advanced". The pool is in any case itself a capped slice: every query returned 25 records regardless of whether OpenAlex reported 114 or 100,152 matches.
   *Why it matters.* This is selection bias with a known direction: highly cited, multiply-indexed work is privileged, which is exactly the work most likely to look "mature" and "well-characterized" — the paper's own narrative. It also means the reported 40/351 ratio is not a coverage estimate, and a reader who re-runs the procedure and screens all 351 records would not reproduce this corpus. The reported flow overstates how much of the candidate pool was actually screened.
   *Improvement.* Document the retrieval and ranking rule in §3.2, state the shortlist frame in the flow table, and run a retrieval-sensitivity check (three pages per query, and no citation ranking) to report how many of the 40 change. If the map is stable, say so; if not, the corpus claim needs to be stated as one draw from a ranked slice.
   *Severity.* Major.
   *Evidence Anchor.* table: Appendix E — 24 rows that each retrieve exactly 25 records against match counts from 114 to 100,152, with no ranking rule stated for the post-retrieval ordering.
   *Confidence.* 5/5 for the executed procedure (read from the script and the stored pool) and for the rank positions; 4/5 for the inference that the shortlist framed selection — the artifacts are consistent with that reading but do not prove intent.

3. **The under-coverage finding is diagnosed against the wrong mechanism, so the proposed remedy would not fix it and the abstract generalizes the artefact.**
   *Problem.* §4.4 attributes thin dynamic-arbitrage coverage to query vocabulary: "the 24 queries emphasized static-arbitrage vocabulary, and only a handful of records survived". But the log shows the 25-record retrieval cap binds for every query, including the four whose vocabulary is explicitly dynamic or violation-oriented (queries 12, 19, 20, and 16 with 30,236, 6,341, 651, and 3,700 matches respectively). Coverage was limited by retrieval depth, not mainly by wording, so the stated diagnosis is at best incomplete. The "frontier" label is then carried into the abstract as a field-level sentence ("Dynamic no-arbitrage is less standardized and less frequently evaluated") without the corpus qualifier that §4.4 attaches to it.
   *Why it matters.* A mis-specified diagnosis produces a mis-specified research agenda: §5.5's remedy is a full-text, multi-database review with dual screening, which fixes vocabulary and screening but not the retrieval cap that actually caused the under-sampling. And the abstract sentence is the part most readers will cite. A reading of the field derived from a ranking artefact should not leave the corpus.
   *Improvement.* State the mechanism correctly (retrieval depth plus static-heavy wording), widen retrieval or run a vocabulary-only comparison to separate the two effects, and restate the abstract sentence with its corpus scope attached.
   *Severity.* Major.
   *Evidence Anchor.* text: §4.4 — "the 24 queries emphasized static-arbitrage vocabulary, and only a handful of records survived".
   *Confidence.* 4/5 — the retrieval cap is verified, but I did not test how much a deeper retrieval would have added; the mechanism claim is an inference from the log, not a measurement.

4. **Method-level coding rests on abstracts with no validation subsample, so coding error is unmeasured.**
   *Problem.* Appendix D assigns every source an enforcement family, a static-test flag, and a dynamic-test flag; Table 4 assigns seven reporting frequencies; §2.2–§2.4 make method-level statements. All of this is extracted from abstracts, with four partial snippets and one title-level record, and there is no second coder, no pilot extraction, and no full-text validation of any code. The coding scheme also lacks a "not reported in the abstract" state distinct from a negative finding, so absence of evidence in an abstract is coded as absence of the test.
   *Why it matters.* The paper's most load-bearing negative claims — no shared benchmark, no common dynamic test, evaluation is fragmented — are statements about what the corpus does not report, and they are exactly the claims most vulnerable to abstract truncation. Without a validation subsample the size of that error is unknown, and the paper's own hedge ("abstract level") does not bound it.
   *Improvement.* Add a stratified full-text validation subsample of about ten sources and report agreement between abstract-level and full-text codes, with percent agreement or kappa; separate "no test reported" from "test not described in the abstract"; publish the extraction form. This converts an unquantified limitation into a measured one at modest cost.
   *Severity.* Major.
   *Evidence Anchor.* absence: §3.4 data extraction — expected a validation subsample or a coded not-reported state; checked §3.3, §3.4, §3.5, §5.4, Appendix C, Appendix D.
   *Confidence.* 5/5 — the absence is documented by the paper itself and by the frozen metadata, which contains only abstract text.

5. **Table 4's frequency labels are uncounted impressions, and the field-level claim built on them outruns the design.**
   *Problem.* The "Reporting in corpus" column gives "Common", "Common in constraint papers", "Rare", "Uneven", and "Method-specific" with no counts, no denominator, and no coding rule, for a corpus whose own coding table already permits counts on two of the seven dimensions. The prose then ranks the dimensions ("fit and static violations most often … cost and interpretability rarely") and draws a causal-incentive conclusion: "the field measures what is easy to compute, not what a risk manager needs."
   *Why it matters.* The seven-dimension matrix is one of the paper's three declared contributions, and its empirical column is the weakest evidence in the paper. A ranking of reporting frequencies is a quantitative claim and should be a count. The causal sentence is a claim about incentives in a research field, which a 40-source abstract-level corpus cannot support even if the counts were perfect.
   *Improvement.* Replace the labels with counts and denominators (Appendix D already yields 15/40 static and 4/40 dynamic flags), add a stated coding rule for the other five dimensions, and rewrite the causal sentence as a proposition to be tested by the benchmark agenda.
   *Severity.* Major.
   *Evidence Anchor.* table: Table 4 — the "Reporting in corpus" column, whose seven entries are frequency words with no count column, against Appendix D, whose Y/N coding supports counts for two of them.
   *Confidence.* 5/5 — the column and the missing counts are directly observable.

6. **The documented search parameters are not the executed search parameters.**
   *Problem.* §3.2 states a date range of 2015-01-01 to 2026-11-19 and an English-language criterion, and Appendix A states a core window of 2015–2026. The executed call is `params = {"search": query, "per-page": "25", "select": FIELDS}` with no date filter, no language filter, no type filter, no sort parameter, and no pagination. The window and the language rule are therefore post-hoc screening decisions applied to an unfiltered retrieval, and their application is not recorded anywhere.
   *Why it matters.* A re-runner who follows the methods section would get a different candidate set from a reader who follows the script, and would not know which rule was applied by hand. This is the most mechanical kind of reproducibility failure, and it is invisible from the paper alone; it also means the pre-2015 exceptions were judgment calls on unfiltered data rather than designed boundary cases.
   *Improvement.* State the executed parameters verbatim (sort, per-page, pagination, filters, API date), and either add the date and language filters to the script or relabel them as screening rules with their exception logic.
   *Severity.* Major.
   *Evidence Anchor.* dataset: `search/openalex_search.py` — the request parameters contain only `search`, `per-page`, and `select`, with no filter or sort keys, against §3.2's stated date range.
   *Confidence.* 5/5 — read directly from the executed script.

7. **A synthesis count in §4.7 contradicts Table 5.**
   *Problem.* §4.7 reports five resolved pairs, one unresolved, and one not applicable. Table 5 records four "Resolved in synthesis" (CP-001, CP-002, CP-003, CP-005), one "Flagged unresolved" (CP-004), and two "Not applicable" (CP-006, CP-007).
   *Why it matters.* The tension inventory is a declared synthesis output, and its summary sentence does not match its own table. The discrepancy is small in substance but signals that the prose counts were not generated from the coding table — the same drafting path that produces the uncounted Table 4 labels.
   *Improvement.* Correct the sentence and, going forward, generate all such counts from the coding sheet.
   *Severity.* Minor.
   *Evidence Anchor.* table: Table 5 — status column, four resolved, one flagged, two not applicable.
   *Confidence.* 5/5 — direct comparison of the sentence with the table.

8. **The composition gates are unsourced and one of them is threshold-sensitive in a way the frozen metadata does not support.**
   *Problem.* §3.3 checks the corpus against three unexplained thresholds: a 60% peer-reviewed floor, a 30% currency cap that "does not trigger an advisory", and a 70% single-method ceiling. No source, prior, or rationale is given, and because they are stated as pass/fail checks they read as targets rather than descriptors. The currency check does not reproduce: by the frozen metadata in `selected_sources.json`, 13 of 40 records predate 2021 (32.5%), and one record cited as 2021 carries an OpenAlex year of 2019, so the count depends on a citation-year convention that the paper states but does not apply consistently.
   *Why it matters.* Threshold-driven composition is a construction-bias risk: a corpus tuned to pass a 30% cap is a corpus whose composition was adjusted. And a gate that is reported as satisfied at exactly the boundary, using a count that the frozen data do not reproduce, is not auditable.
   *Improvement.* State the provenance of the three gates, show the counts and denominators that produce them, and either fix the year convention or drop the cap language.
   *Severity.* Minor.
   *Evidence Anchor.* text: §3.3 — "the currency distribution is at the 30% cap and does not trigger an advisory".
   *Confidence.* 5/5 — the 13/27 split is a count from the frozen corpus file; the 2021/2019 year mismatch is visible in the same file against the reference list.

9. **"No fabricated reference" overstates what a DOI-existence check establishes.**
   *Problem.* §3.4 and Appendix A report that no fabricated reference was found. The verified operation was DOI resolution through the OpenAlex endpoint plus a title/author check; that establishes existence, not correct attribution, and it cannot detect a real DOI attached to a different paper, a wrong year or venue, or a citation that does not support the sentence citing it.
   *Why it matters.* The phrase is an integrity assurance, and integrity assurance language should describe the operation actually performed. §5.4 does disclose that no full-text claim verification was done, so the paper is internally honest; the summary sentence is still stronger than the check.
   *Improvement.* Rewrite as "all 40 records resolved to a live DOI or a HAL record; attribution was checked against title/author metadata only; no claim-level verification was performed".
   *Severity.* Minor.
   *Evidence Anchor.* text: §3.4 — "no fabricated reference was found".
   *Confidence.* 4/5 — I can see the described procedure in the paper and the metadata fields in the frozen corpus, but not the manual title/author check itself.

10. **Method-family coding is inconsistent in two places, against the paper's own substantive descriptions.**
    *Problem.* Fengler (2009) is bucketed "Parametric surfaces" in Table 1, Appendix B, and Appendix D, while §1.1 lists it among nonparametric models, §2.1 says it "approaches the problem from constrained smoothing rather than a parametric family", and §2.2 calls it an early nonparametric benchmark. Separately, rows 6, 21, and 37 are coded enforcement family "Construction (calibration map)" while their static-test column is N, which contradicts Table 2's guarantee column ("Static, by construction") for the family they are assigned to.
    *Why it matters.* The taxonomy is the paper's integrating device, and its per-source mapping is the audit trail for the taxonomy. A bucket label that the paper itself argues against in two places, and a family assignment that its own guarantee column contradicts, weaken the mapping's credibility even where the taxonomy is sound.
    *Improvement.* Choose one family per source and state the rule, or add a hybrid category with its own guarantee description; reconcile the calibration-map rows with Table 2.
    *Severity.* Minor.
    *Evidence Anchor.* table: Appendix D — rows 3, 6, 21, and 37, read against Table 1 and §2.1–§2.2.
    *Confidence.* 4/5 — the textual inconsistency is direct; which coding is correct is R2's judgement.

11. **The eligibility rule is silent on secondary sources, and two surveys are admitted without an eligibility clause.**
    *Problem.* The unit of analysis is "a source that constructs, evaluates, or repairs an equity-index implied volatility surface", which does not admit reviews. Homescu (2011) and Ruf and Wang (2020) are included and coded in Appendix D as "Survey (no construction)" and "Survey/evaluation"; the second is the evidentiary basis for the corpus-wide negative about benchmarks.
    *Why it matters.* Either the rule needs a secondary-source clause or the two records need an explicit justification; as written, a reader cannot tell whether the inclusion rule was amended after retrieval. The substantive inclusion is defensible — a negative finding needs a review to anchor it — but the rule should say so.
    *Improvement.* Add an explicit secondary-source category with its permitted uses (background, negative-claim anchoring) and state that such records are not counted as construction evidence.
    *Severity.* Minor.
    *Evidence Anchor.* table: Appendix D — rows 4 and 8, coded "Survey (no construction)" and "Survey/evaluation", against the unit of analysis at §3.1.
    *Confidence.* 4/5 — the mismatch is textual; the admissibility question is a judgment call on the paper's own rule.

12. **Deduplication is identifier-based, so the candidate denominator counts versions rather than works.**
    *Problem.* Appendix A says records were "deduplicated by DOI or normalized title"; the script keys on DOI or the lowercased title only, with no normalization. The stored pool contains 19 duplicate-title groups (24 extra records) and four included titles appear more than once in the pool.
    *Why it matters.* The 351 denominator, and therefore the 40/351 figure, counts duplicate versions as separate records, and the screening step may have assessed the same work twice under different identifiers. The effect is small (roughly 7% of the pool) but it inflates the apparent candidate base and weakens the flow count.
    *Improvement.* Deduplicate on a normalized title key plus author-year, report the version-collapse count, and state whether version pairs were screened independently.
    *Severity.* Minor.
    *Evidence Anchor.* dataset: `search/openalex_candidates.json` — 19 duplicate-title groups and 24 extra records under the script's title key.
    *Confidence.* 5/5 — counted from the stored pool.

### Detailed Comments

**Research Questions & Hypotheses.** The research question is operational and answerable by the chosen design: which mechanism carries the guarantee, and what trade-offs are reported. The three aims decompose cleanly into §2.6 and §4.2 (organize), §3.5 (assess), and §5.5 (gaps). No formal hypotheses are stated, which is appropriate for a review, but the five findings are written in declarative form while Table 6's six propositions are the testable form; promoting the propositions to the primary output would make the review's epistemic status visible at the point of claim rather than only in the appendix-like §5.2. Aim (b) is the weak link (W1).

**Research Design.** A frozen-corpus structured narrative review, with a declared map-not-rank logic, is a coherent design for the question, and the design is maintained consistently in the body. Two departures from it matter: the causal sentence in §4.5 ("the field measures what is easy to compute") is an incentive claim a reporting survey cannot support, and the Finding 3 heading plus the abstract sentence are field-level statements about a retrieval artefact. Neither is a design failure so much as a claim-scope failure at the two most visible surfaces.

**Sampling Strategy.** The sample's population is the OpenAlex relevance surface, not a defined eligible population: 25 records per query, 24 queries, 600 retrieved, 351 unique, then a query-multiplicity/citation ranking whose top 120 contains all 40 included records. That is three successive selection steps, only the middle one documented in the paper. The design would be materially stronger with one cheap experiment: re-retrieve at three pages per query and report corpus overlap. If the overlap is high, the corpus claim becomes robust; if low, the paper's sentence becomes "one draw from a ranked slice", which is still publishable for a structured review but changes the confidence language throughout.

**Data Collection.** The extraction fields are listed and appropriate for abstract-level work; the four partial abstracts and the one title-level record are named individually, which is better than most reviews at this level. What is missing is procedural: no extraction form, no pilot pass, no second coder, no rule for what counts as a reported violation versus a mentioned one. The title-level record is admitted and used for a family classification, with a correct caveat that it is not used for a substantive dynamic claim; the caveat is honoured in §4.4 and Table 3.

**Analysis Methods.** The five-step synthesis is described in enough detail to be auditable in principle. The convergence rule (themes need at least three sources; silence noted below two) is stated but never instantiated in a table, so a reader cannot see which themes passed and which were suppressed. The contradiction analysis is the strongest analytic move in the paper — it distinguishes conditional from genuine tension — but the tension counts are reported inconsistently (W7). The most consequential gap is that no coding protocol exists for the two instruments the paper actually contributes: enforcement-family assignment (Appendix D) and the seven evaluation dimensions (Table 4). Without one, the matrix is a judgement display rather than a measurement, and inter-coder reliability is undefined.

**Results Presentation.** The descriptive counts are internally consistent (S3) and the abstract's headline numbers reproduce, which is rarer than it should be. Against that, §4.7's prose count contradicts its table, Table 4's frequency labels have no counts, and Table 3 includes a title-level row whose own note excludes it from the dynamic claim. None of these changes a finding; together they suggest the narrative layer was drafted with less arithmetic discipline than the tables.

**Reproducibility.** This is the paper's strongest protocol dimension and its weakest documented one. Strong: the query log reconciles exactly with Appendix E, the candidate pool and frozen corpus are stored, all 40 records trace to the documented queries, and the scripts exist. Weak: the executed request parameters are not the documented ones (W6), the ranking rule that frames selection is undocumented (W2), there is no archived snapshot or version pin for corpus and scripts, and no per-source query provenance in the paper — though the pool file already stores a `queries` field per record, so publishing a query-to-record table would be nearly free. Deduplication is identifier-based (W12).

**Methodological Fallacies Detected.** Selection bias is present and directional: the retrieval cap plus multi-query/citation ranking privileges well-cited, multiply-indexed work, which is the work most likely to support the review's "mature families are well-characterized" narrative (W2). Observational/ascertainment bias is present through abstract-only coding without a validation subsample, and it runs in the direction of under-recording method detail — that is, toward the paper's "evidence is thin" conclusions (W4). Publication-status conflation substitutes venue for quality (W1). Confirmation risk from a post hoc taxonomy is mitigated rather than eliminated: the taxonomy is declared interpretive and Table 6 supplies falsifiers, which is the right mitigation. HARKing is not evident, but the composition gates (W8) create a target-tuning risk that the paper does not discuss. Publication bias is partly addressed by including 10 preprints, though no analysis of direction is attempted. No evidence of selective reporting was found; the disclosed Devil's Advocate pass and the residual CP-004 flag cut against it.

### Questions for Authors

1. What `sort`, `filter`, and pagination parameters did OpenAlex apply to each query, and what does the corpus look like if each query retrieves three pages instead of one? Reporting corpus overlap at 25 versus 75 records per query would directly bound retrieval sensitivity.
2. `openalex_search.py` ranks candidates by query-hit count and citations and writes a 120-record shortlist; all 40 included records fall inside it (ranks 1–116). Was the 311-record exclusion made against the full 351, or against that shortlist? If the latter, how should §3.3's "title/abstract screening" sentence be read?
3. The pooled candidate file already stores which queries surfaced each record. Can you publish that query-to-record provenance as an appendix table, so the corpus can be reconstructed from the printed text alone?
4. Which year convention governs the 30% currency cap? The frozen metadata yields 13 pre-2021 records rather than 12, and one record cited as 2021 carries a 2019 OpenAlex year. Does the cap still hold under the paper's own online-first rule?
5. What is the provenance of the 60%, 30%, and 70% composition gates, and were they fixed before or after retrieval? If they were applied after the fact as acceptance checks, what would change if a gate failed?
6. Can you run a stratified ten-source full-text validation of the enforcement-family and static/dynamic-test codes, and report agreement with the abstract-level codes? This would turn the abstract-level limitation into a measured error bound and would substantiate or qualify the "no common dynamic test" finding.
7. For Table 4, what are the counts and denominators behind "Common", "Rare", "Uneven", and "Method-specific"? Appendix D already supports counts for the static and dynamic rows; can a stated coding rule produce the other five?

### Minor Issues

- §1.5 is separated from §1.4 by a horizontal rule (line 58), so it reads as a post-section block rather than as part of the introduction; the same pattern precedes the unnumbered "**Scope and excluded streams.**" block after §3.6, after which §3.7 resumes numbering. Either number the block or drop the rule.
- §3.3 uses undefined pipeline jargon as if it were a methods standard — "floor", "cap", "does not trigger an advisory". A reader outside the pipeline cannot tell whether these are journal requirements, internal audit thresholds, or the author's heuristics.
- Level VI and Level VII are used throughout without the rubric's provenance or the definitions of the levels above VI; only two levels of an apparent hierarchy appear, so the label reads as binary rather than graded.
- Table 4's column title "Reporting in corpus" asserts a measurement that the column does not report; if no counts are added, the honest label is "Impression from abstract-level extraction".
- Appendix A's "deduplicated by DOI or normalized title" should read "deduplicated by DOI or lowercased title", matching the executed script.
- §2.2's Fengler paragraph and Table 1's parametric bucket give a reader who checks one against the other an avoidable contradiction; see W10.
