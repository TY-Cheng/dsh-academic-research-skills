# Phase 6b — Evaluator Review

**Manuscript:** `paper-draft.md` (v1.1, 7,573 body words, 6 tables, 2 figures, 41 references), read in full: front matter, both abstracts, §1–§7, Tables 1–6, Figures 1–2, Declarations, References, Appendices A–C.
**Contract:** `academic_paper/evaluator_full/v1` (baseline v3.6.6). **Criteria binding:** `criteria_binding_unavailable` — no author-confirmed `ReviewTargetContext`; no venue-fit judgement is made or implied. **Calibration status:** `NOT_CALIBRATED` (single-model evaluator, no human calibration set).

## Dimension Scores

### D1: originality — pass

The Introduction names a specific gap and the contribution is not a container for 41 summaries. §1.2 states the gap as a claim-inflation problem ("a tested method read as proved, a static guarantee as dynamic", §1.1) and then commits to five deliverables, of which the four-locus framework (§2.3) and the proof–audit disjointness finding (§5.1) are genuinely new arrangements of the corpus rather than restatements. The Discussion engages rather than lists: §6.1 assigns each family a different quantifier and names the two penalty rows that concede their route's limit (Na et al., 2023; Sidogi et al., 2022), §6.2 sets the author's own absence claim beside the two readings that could overturn it, and §6.3's agenda is organised as falsification targets rather than future work. The paper also declines the obvious over-claim — it does not assert field-wide absence and does not produce a league table, both of which would have been the easier originality claim. No block or warn trigger from my Phase 6a plan is met.

### D2: methodological rigor — pass

The method is named, matched to the question, and reproducible at the level the design claims. §3.1 gives database (OpenAlex), query count and grouping (31 in 8 groups), window (2015-01-01 to 2026-11-23), language (English), retrieval arithmetic (775 requested, 750 returned, 430 unique, 389 excluded), and the eight exclusion codes with counts; the inclusion frame is stated; the PRISMA status is stated negatively and correctly ("PRISMA 2020-style, not PRISMA-compliant", §3.1, and Appendix A "What this is not"). Coding rules are specified before the findings and are decision-grade: §3.2 defines the three evidence statuses so that "a test is never upgraded to a proof", §3.3 defines the four-field comparability rule and states the consequence (no ranking), and Appendix C states the eight coded fields and the rule that a claim is evidence only where the abstract states it. Appendix B gives the 41-row ledger with per-row evidence, comparability, coverage and section map, so the analysis is re-derivable from the manuscript alone. Limitations are engaged, not mentioned: §6.4 and Appendix C's single-analyst note each convert a limitation into a statement about what a second coder could and could not reproduce, and §6.2 declines to choose between the gap reading and the retrieval-effect reading rather than resolving it by assertion. The design is appropriate to a corpus-scoped review: it does not claim systematic-review status and does not apply meta-analytic machinery the data could not support.

### D3: evidence sufficiency — warn

Core claims are fully evidenced: all 41 sources are cited (112 citation markers, 0 orphans), every reported number is attributed to the row that reports it (e.g. the 5.4% butterfly floor, §4.3; 90.8% pass rate, §4.4; 0.00% at $10^{-4}$, §4.4), and the Discussion's inferences stay inside the corpus — the dynamic absence is bounded three ways (0 of 41; 0 of 36 in-window; 0 of 31 construction, §7.1, §6.2) and the one inference that exceeds a single abstract is explicitly marked as a premise rather than a measurement (§1.1). Two secondary claims, however, are not traceable from the manuscript's own apparatus, which is what puts this dimension at warn rather than pass:

1. **§3.1, line 103:** "Four records were included after abstract reading in preference to earlier candidates", while Appendix A line 413 states "Two records initially retained failed both metadata resolution and abstract reconstruction and were replaced". The two statements describe the same adjustment with different counts, and neither the text nor the appendix reconciles them. The appendix's number is the one that matches the Stage 1 provenance, which names two replacements.
2. **§5.3, line 264:** three coverage counts that feed Table 6 — "roughly eight rows report an error on held-out data", "about eight rows report held-out strike or maturity behaviour", "asserted in about five rows" — carry no per-row pointer. Appendix B's "Coverage" column is abstract coverage (full/partial/metadata-only), not evaluation coverage, so a reader cannot recover which rows the counts aggregate. The counts are hedged, but they are load-bearing for Table 6 and for the paper's claim that fit accuracy is "partial" rather than absent.

Neither defect reaches the block criteria: no core claim lacks evidence, no single source is over-relied upon (the most-cited row, R5, appears in eight sections but never alone in support of a finding), and no inference exceeds the corpus. The warn trigger I pre-committed to — "core claims have evidence but some secondary claims lack support" — is met by these two items.

### D4: argument coherence — warn

The research question of §1.2 is answered in §7.1 point by point, the thesis is stable across Abstract, Introduction and Conclusion (four loci, proof–audit disjointness, dynamic void, no ranking), and the section transitions are explicit rather than left to the reader (§2.3 "they are tested in Section 4", §3.3 "carried into Section 6.4", §5.3 "what the agenda in Section 6.3 responds to"). One reader-visible inconsistency survives:

**§4.2, lines 179–185**, states that "Six rows occupy this locus, and none is proof-level" and "zero of six rows are proof-level", while line 181 describes N1 as a network whose "option-price function is frictionless and convex by design", line 185 calls its constraint "structural rather than a soft term", and Appendix C line 473 says N1 "enforces constraints architecturally, like the G-family rows". Table 3 then codes all six N rows as numerical test (line 228). A reader holding §4.2 line 181 and Table 3 line 228 side by side is asked to believe that an "arbitrage-free by design" architecture is not proof-level, and the manuscript never supplies the coding rule that makes that consistent. The defect is local and repairable in one sentence, and the paper's own framework supplies the vocabulary for the repair; it is not a logical gap between sections, so it stays at warn rather than block.

### D5: writing quality — pass

Register is consistently academic, third person, and active where the argument allows it; citation format is internally consistent (APA 7, verified in Phase 5a, 41/41 entries, no orphans); every table and figure is called out in the prose and captioned to stand alone (Table 1 §3.1, Table 2 §4.1, Table 3 and Table 4 §5.1, Table 5 §5.2, Table 6 §5.3, Figure 1 §2.3, Figure 2 §3.1), and the notes under Tables 2–6 do real work rather than restating the caption. Two small items do not meet the "several grammar or word-choice issues" threshold but should be fixed when the manuscript is next touched: §4.1 line 155 says "Table 2 summarises the six families" when Table 2 is the four-family summary with two supporting groups (its own caption, line 165, is correct), and the paragraph at §3.1 lines 97–99 runs long without a break. Neither affects comprehension, so the dimension passes.

## Failure Condition Checks

### F1 — any mandatory dimension (D2, D3) scored block → not fired

D2 = pass, D3 = warn. No mandatory dimension is at block, so `request_revision` is not triggered by this condition. Dimensions involved: none.

### F2 — one or more mandatory dimensions scored warn → FIRED

D3 (evidence_sufficiency, mandatory) is at warn, on the two traceability items above. Severity 70; this condition sets the decision to `request_revision` and outranks F3, F4 and F6. Dimensions involved: D3.

### F3 — any high-priority dimension scored block → not fired

D1 = pass, D4 = warn. No high-priority dimension is at block. Dimensions involved: none.

### F6 — any normal-priority dimension scored block → not fired

D5 = pass. Dimensions involved: none.

### F4 — own scoring plan triggers warn on a high or normal dimension, with no mandatory block or warn → not fired (suppressed)

D4 (high) does meet a warn trigger, but F4 applies only when no mandatory dimension is at block or warn; D3's warn at F2 suppresses it. Recorded here so the precedence is auditable rather than silent. Dimensions involved: D4.

### F5 — round 2 still shows a mandatory block after a writer revise attempt → not fired

No writer revision has yet been attempted in this pair, and no mandatory block exists. Dimensions involved: none.

### F0 — every mandatory dimension pass and no dimension at block → not fired

D3 is at warn, so the antecedent ("every mandatory pass") is false. Dimensions involved: D3.

## Review Body

**What the paper gets right, in one paragraph, because the decision turns on what is left.** The strongest single move is the framework's discipline: §2.3's enforcement triple (mechanism, evidence, verification) is defined before any findings and then used unchanged as the reporting instrument in §4–§6, so the family accounts are not free-standing summaries but applications of one instrument. The second strongest is the refusal to rank: §5.2 does not merely note that metrics differ, it shows that the apparently comparable violation-rate family (90.8%, 5.4%, under 1%, 0.00%) differs in data, definitions, tested conditions and tolerance, which is the correct and harder argument. Third, the proof–audit cross-tabulation in §5.1 (seventeen proof rows, none auditing; six auditing rows, one also structural) is the paper's most quotable finding and it is presented as a cross-tabulation rather than as an anecdote, which makes it falsifiable.

**Finding 1 (D3, warn, must be fixed). Contradictory selection counts.** §3.1 line 103 reports four records included after abstract reading "in preference to earlier candidates"; Appendix A line 413 reports two retained records replaced. The manuscript's arithmetic is otherwise exact — 430 − 389 = 41 closes in §3.1 and in Appendix A, and Table 1 line 112 repeats the same numbers — which is precisely why the unreconciled pair of counts is damaging: a reader who checks the flow will find one number that does not appear anywhere else. The Stage 1 record names exactly two replacements (a neural-network pricing paper replaced by Wiedemann et al., 2025, and a foreign-exchange delta-condition paper by Fukasawa, 2022). *Fix:* state two, name the mechanism consistently with Appendix A, and let the appendix carry the detail.

**Finding 2 (D3, warn, must be fixed). Load-bearing Table 6 counts without a per-row pointer.** §5.3 line 264 gives "roughly eight rows" (held-out error), "about eight rows" (held-out strike or maturity behaviour) and "about five rows" (cost asserted). These three numbers determine the "partial" and "thin" and "asserted" statuses in Table 6 (lines 277–279) and therefore §6.3's agenda priorities. The manuscript's own traceability apparatus does not reach them: Appendix B's "Coverage" column is abstract coverage, Appendix C defines the metric field but never aggregates it, and the appendix does not list which rows report an error on held-out data. *Fix:* one sentence stating that the per-row metric and evaluation coding is the seventh field defined in Appendix C and is recorded in the Stage 1 coding records held with the run artifacts, with the aggregate counts in §5.3 being this review's aggregation of that field. That keeps the claim at the strength it currently has (hedged, coded) while making it checkable.

**Finding 3 (D4, warn, must be fixed). The N1 architecture/coding tension.** §4.2 line 181 describes N1's option-price function as "frictionless and convex by design", line 185 groups it as a hybrid whose "constraint is structural rather than a soft term", Appendix C line 473 places it with "the G-family rows" on architecture, and Table 3 line 228 codes it numerical test — supporting the sentence "zero of six rows are proof-level" (line 183). Each statement is defensible alone; together they read as a contradiction, and the resolution the paper actually uses (evidence is coded at the level the abstract reports it, so a structural guarantee is proof only where the abstract states it as a theorem over the admitted set) appears nowhere in §4. The paper therefore asks its reader to infer a coding rule that it applies consistently everywhere else — a coherence cost it does not need to pay. *Fix:* add the coding rule to §4.2 in the paper's own vocabulary and point it at the same rule in Appendix C, so the architecture description and the test coding are visibly consistent rather than apparently opposed.

**Finding 4 (D5, minor, fix while touching the manuscript). "Six families" for a four-family table.** §4.1 line 155: "Table 2 summarises the six families on the review's dimensions and marks the two supporting groups." Table 2's caption (line 165) says "Four-family evidence summary (two supporting groups shown for completeness)", and the paper's framework is four loci throughout. The sentence conflates the six rows of Table 2 with the four families the review is about. *Fix:* "summarises the four focal families, with the two supporting groups shown for completeness."

**On the evidence-level limits of the corpus (no finding, recorded because it shapes what the review may claim).** The paper is honest that it is an abstract-level, single-analyst, English-only, OpenAlex-only review with no full-text or proof check (§3.2, §3.3, §6.4), and it converts that honesty into bounded claims rather than into a disclaimer: the dynamic absence is stated three ways, the framework is called "proposed, not validated" (§6.4, §7.2), and the two reading hypotheses for the void are left open (§6.2). That is the correct treatment of a corpus it does not control, and it is why I do not score D2 down for the absence of dual screening or inter-coder agreement — those are disclosed design choices with stated consequences, not undisclosed weaknesses. A reader who wants kappa will not find one; a reader who wants to know what the absence of kappa licenses will find it in §6.4 and Appendix C.

**On the abstract pair (checked against the body, no finding).** The English abstract's 225 words and the Chinese abstract's 425 characters carry the same five components, the same counts (17 / 16 / 8; 0 of 41; 0 of 31 construction) and the same corpus-scoped hedge as §5.1, §7.1 and §6.2. The Chinese text does not convert the corpus-scoped absence into a field-wide claim (没有任何一篇, not 文献中没有), and neither abstract carries a citation. The pair is consistent with the body as written.

**Scope of this review.** Five dimensions, seven failure conditions, all decisions traceable to the Phase 6a scoring plan fixed before the manuscript was read. No venue-alignment judgement is made, because `criteria_binding_unavailable` leaves no target to align to; the absence of a review target is not scored against the paper.

## Evaluator Decision

`evaluator_decision=request_revision`

Derivation: D3 (mandatory) = warn fires F2 (severity 70), the highest-severity fired condition; F1, F3, F6, F0 do not fire, and F4 is suppressed by F2. D4's warn is recorded and repaired in the same round, but it is not the condition that sets the decision. The revision is bounded: three substantive items (Findings 1–3) and one word-choice item (Finding 4), all local, none requiring new sources or new analysis. The writer may apply them in a single round; `max revision rounds = 2` remains available.

Decision as first emitted: `request_revision` (F2). Post-revision confirmation and round accounting are recorded in `phase6-review.md`.
