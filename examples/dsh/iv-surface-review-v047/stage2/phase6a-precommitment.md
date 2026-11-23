# Phase 6a — Evaluator Pre-Commitment (paper-blind)

> **Blindness declaration.** This turn sees the `evaluator_full` contract JSON, the paper metadata (`title`, `field` = Finance, `word_count` = 7,400), the writer's `<phase4a_output>`, and the pointer-only #684 criteria authority. It has not seen the Abstract, the Draft Body, the outline, the argument blueprint, the bibliography, or any Phase 4b or Phase 5 artifact. No dimension below is scored; the scoring plan is fixed before any manuscript text exists.

## Contract Paraphrase

### D1: originality

The paper has to name a specific gap in the introduction and make the Discussion do real work against prior studies rather than list them. In a review, this dimension is won or lost on whether the framing is a contribution or a container: a themed summary of 41 sources restates what is already known, while a paper that reorganises how the field's evidence fits together has added something. The Literature Review has to identify the gap the paper fills, and the Discussion has to engage the cited work substantively — agreement, disagreement, and the reason for each — not merely cite it. A contribution that is asserted but weakly differentiated from cited prior work sits at warn; a contribution that is vague, absent, or a pure re-description of an existing claim sits at block.

### D2: methodological rigor

The method must be named, matched to the research question, and described far enough that a reader could repeat it: what corpus, chosen how, on what inclusion rules, coded how, with what evidence grading, and read to what depth. Data sources must suit the question — for a corpus-scoped review, that means a documented search and screening record rather than an appeal to familiarity. Analysis steps must be reproducible from the text, and the limitations must be stated and then actually engaged, not disposed of in one sentence. A design flaw that undercuts the question, or a method that cannot be followed, is a block; a sound method that is thin on detail or that mentions limitations without working through them is a warn.

### D3: evidence sufficiency

Every factual claim needs a citation, and the cited sources must be of a quality the field would accept. In this domain that means separating what a source proves from what it tests numerically and from what it merely assumes, and never sliding a test up to a proof. Inferences in the Discussion must stay inside what the corpus supports: a corpus-scoped absence is not a field-wide absence, and an abstract-level read cannot certify a full text's data or tolerance. Multiple core claims without evidence, reliance on a single source, or favourable-evidence cherry-picking block; a sound core with unevenly supported secondary claims warns. A novelty claim whose support is a stated bounded search is judged as a properly limited absence claim, not as an unevidenced assertion.

### D4: argument coherence

The research question posed in the Introduction has to be answered in the Conclusion, the sections have to hand off to one another, and the thesis has to be the same thesis in the Abstract, the Introduction, and the Conclusion. In a structured review the risk is drift: a claim introduced as one thing in a framework section and used as another thing in the findings. Logical gaps between sections, a conclusion that does not answer the opening question, or passages that contradict each other block; overall sound logic with forced transitions or minor cross-section inconsistency warns.

### D5: writing quality

The register has to stay academic throughout, grammar errors should be rare, citation format has to be internally consistent, and every figure and table must be called out in the prose and interpretable on its own. Long undivided paragraphs, colloquial phrasing, or a citation style that changes mid-manuscript are defects; unintelligibility or pervasive grammatical failure is a block.

## Scoring Plan

### D1: originality

- **dimension_id:** D1
- **what_to_look_for:** Introduction's contribution statement names a specific gap; Discussion engages prior work substantively (not list-citation); Literature Review identifies the gap the paper fills.
- **what_triggers_block:** Contribution statement is vague or absent; Discussion lists prior work without engagement; paper restates known conclusions in a new context with no added evidence.
- **what_triggers_warn:** Contribution exists but is weakly differentiated from cited prior work; Discussion engagement is uneven across cited sources.

### D2: methodological rigor

- **dimension_id:** D2
- **what_to_look_for:** Method is named and justified against the research question; sample / data sources are appropriate; analysis steps are described in enough detail for replication; limitations are explicit.
- **what_triggers_block:** Method does not match the research question; significant design flaws; limitations are not discussed; analysis cannot be replicated from the description.
- **what_triggers_warn:** Method is fundamentally sound but insufficiently detailed; some choices lack justification; limitations are mentioned but not engaged with.

### D3: evidence sufficiency

- **dimension_id:** D3
- **what_to_look_for:** Every factual claim carries a citation; cited sources are appropriate quality for the field; inferences in Discussion stay within what the data supports.
- **what_triggers_block:** Multiple core claims lack evidence; over-reliance on a single source; Discussion inferences exceed what the data supports; cherry-picking of favorable evidence.
- **what_triggers_warn:** Core claims have evidence but some secondary claims lack support; citation density is uneven across sections.

### D4: argument coherence

- **dimension_id:** D4
- **what_to_look_for:** Introduction's research question is answered in the Conclusion; section-to-section transitions are present; thesis statement is consistent across Abstract, Introduction, and Conclusion.
- **what_triggers_block:** Multiple logical gaps between sections; conclusion disconnected from the introduction's research question; self-contradictory passages.
- **what_triggers_warn:** Overall logic holds but some transitions feel forced; minor inconsistencies between section claims.

### D5: writing quality

- **dimension_id:** D5
- **what_to_look_for:** Register is consistently academic; grammar errors are rare; citation format is internally consistent; figures and tables are referenced in text.
- **what_triggers_block:** Difficult to understand; numerous grammar errors; colloquial register; citation format inconsistent across the manuscript.
- **what_triggers_warn:** Readable but with several grammar or word-choice issues; some paragraphs overly long; minor citation format inconsistencies.

**Criteria authority (pointer-only, #684):** `criteria_binding_unavailable` — no author-confirmed `ReviewTargetContext` exists for this run, so no `ReviewCriteriaBindingManifest` was initialized and no FORMATIVE or INTERNAL receipt is attached. This scoring plan binds only to `shared/contracts/evaluator/full.json` (`academic_paper/evaluator_full/v1`, baseline v3.6.6) and to the paper metadata above. Consequence for Phase 6b: the review will not claim venue alignment, will not infer an unnamed target, and will not treat an absent target as an evaluative fault. The writer's `<phase4a_output>` commits to the same seven writer dimensions (D1 section_completeness, D2 citation_density, D3 argument_blueprint_fidelity, D4 total_word_count, D5 per_section_word_count, D6 paragraph_structure, D7 register_consistency) with mandatory status on D1–D3; those are writer-side acceptance checks, not evaluator dimensions, and they will be reported to the writer as feedback rather than scored here.

[PRE-COMMITMENT-ACKNOWLEDGED]
