# Phase 4b — Writer Record

**Artifact:** `paper-draft.md` (`## Draft Body`, sections 1–7, Tables 1–6, Figures 1–2, Declarations, References, Appendices A–C)
**Contract:** `academic_paper/writer_full/v1` (baseline v3.6.6), re-injected for this call with `<phase4a_output>` = `phase4a-precommitment.md` and the upstream artifacts.
**Section-order note for the four-section lint:** `## Draft Body` is in `paper-draft.md`; `## Dimension Scores`, `## Failure Condition Checks`, and `## Writer Decision` are in this record file, in that order. The lint applies to the pair.

**Measured word count (canonical, `stage2/measure_words.py`):** 7,573 body words (target 7,400; +2.3%). §1 725, §2 1,144, §3 925, §4 1,716, §5 1,299, §6 1,190, §7 574. Allocations: 700 / 1,100 / 900 / 1,500 / 1,250 / 1,300 / 650.

**Pre-commitment fidelity.** Phase 4a named seven dimensions and the escalation path before any drafting artifact was visible. Nothing in the draft required a re-negotiation of that paraphrase. One author-side discrepancy is recorded rather than silently resolved: `draft_writer_agent.md:425` labels writer D6 `acknowledged_limitations`, while `shared/contracts/writer/full.json` declares D6 = `paragraph_structure`. The contract JSON governs (the lint cites it as the baseline), so D6 is scored as `paragraph_structure` here.

## Dimension Scores

### D1: section_completeness
**pass.** All seven outline sections are written, at the approved structure: §1 introduction with the framework positioning and the three sub-questions, §2 conditions and the four-loci argument, §3 corpus construction, §4 the four families, §5 evidence status and evaluation coverage, §6 discussion, §7 conclusion. All six required tables are present and cited in text (T1 §3.1, T2 §4.1, T3 and T4 §5.1, T5 §5.2, T6 §5.3), both planned figures are present (F1 §2.3, F2 §3.1), and the Declarations block carries the seven required statements. No `[MATERIAL GAP]` placeholder remains. Appendices A–C supply the search record, the 41-row ledger, and the coding protocol.

### D2: citation_density
**pass.** Every factual claim in §2–§6 carries a corpus citation; the 41-source freeze holds, with 41 distinct IDs cited and 41 reference entries, no orphan entries, and no unknown slug. Bounded absence phrasing is used where the claim is an absence (§5.1 dynamic count, §6.2 dynamic void), each accompanied by the nearest prior work (C2) or by the explicit absence-of-adjacent-work statement, plus the `#548` bounded search provenance emitted as `<!--protected-hedges: ...-->` on the final Draft Body line. Eleven preprints carry `[preprint]` at first mention; S3 is a practitioner venue and is labelled as such in §7/§2.1 text rather than as a preprint. Two rows are cited at title level only (P4, P7, plus R4) and are explicitly marked unverified in §4.1 and Appendix C; they are never used as evidence for a finding, which is the disclosed limitation rather than an uncited claim.

### D3: argument_blueprint_fidelity
**pass.** All seven blueprint chains are realised in the intended sections: SA-1 (four objects) in §1.2 and §4.1–§4.4, SA-2 (dynamic absence) in §1.3, §2.2, §5.1, §6.2 and §7.1, SA-3 (proof/audit disjointness) in §2.3, §5.1 and §7.1, SA-4 (0 direct comparability, therefore no ranking) in §3.3, §5.2, §5.3, §6.3 and Table 6, SA-5 (one-sided cost, fit-error clause unsupported) in §5.3 and §6.1, SA-6 (calendar conflation and scale relativity) in §1.1, §2.1 and §6.2, and SA-7 (framework plus falsifiable agenda) in §2.3 and §6.3, closing in §7.2. Each topic sentence states its chain's claim, evidence cites the assigned sources, and the explanation returns to the section purpose. No forbidden move is committed: no fabricated citation, no source outside the 41, no field-wide absence claim, no league table, no test upgraded to a proof, no preprint presented as peer-reviewed, no metadata-only row used as evidence, no calendar condition described as dynamic, no claim that H2's fit clause is supported, and no claim that the framework is validated.

### D4: total_word_count
**pass.** 7,573 against a 7,400 target is +2.3%, inside the ±10% band, and 427 words below the 8,000 ceiling. No section needed a ceiling trim; one near-draft trim pass (four clauses) was made for §4 headroom rather than for the total.

### D5: per_section_word_count
**pass, at the edge on §4.** Deviations from allocation: §1 +3.6%, §2 +4.0%, §3 +2.8%, §4 +14.4%, §5 +3.9%, §6 −8.5%, §7 −11.7%. §4 sits 0.6 percentage points inside the ±15% bound after a deliberate trim pass; §7's shortfall reflects a compressed closing rather than a missing element, and both are flagged here so the evaluator can test the reading against the text rather than against the count.

### D6: paragraph_structure
**pass, with a known cost.** Paragraphs are point-first with cited support and an explicit linkage sentence in most cases; section-to-section transitions are carried by closing sentences that name the next question (§1.3→§2, §2.4→§3, §3.3→§4, §4.4→§5, §5.3→§6, §6.4→§7). The cost is density: the enumerative paragraphs in §4 and §5.3 run 150–220 words and carry five to seven citations each, which serves the evidential requirement but slows a skim reader. No paragraph is left unsupported, and no paragraph exists only to transition.

### D7: register_consistency
**pass.** Third-person formal register throughout, no first-person framing except the author's own disclosures, consistent hedging for uncertain claims ("suggests", "is consistent with", "the corpus cannot distinguish"), no colloquial register mixing. Numbers are reported with their source's conditions attached (dataset, tolerance, protocol) rather than as bare rankings. The Appendix B codes (DC/RC/NC, proof/test/assumption) are used consistently with the body text.

## Failure Condition Checks

### F1 (severity 90) — any mandatory dimension `block`
**Did not fire.** D1, D2, and D3 are scored `pass`; no mandatory dimension is scored `block`, so `writer_decision=escalate_to_evaluator` is not triggered.

### F4 (severity 75) — any mandatory dimension `warn`
**Did not fire.** No mandatory dimension is scored `warn`. D2 was the closest candidate, on the title-level rows, but the bounded-absence exception and the explicit unverified marking satisfy the dimension without a warning.

### F2 (severity 60) — any high-priority dimension `block`
**Did not fire.** D4 and D5 are both scored `pass`. §4's +14.4% is inside the ±15% bound.

### F3 (severity 40) — any high-priority dimension `warn`
**Did not fire.** Both high-priority dimensions are `pass`. The §4 margin is recorded under D5 as a note, not as a warning, because the contract's test is the ±15% band and the section is inside it.

### F0 (severity 10) — every mandatory dimension `pass`
**Fired.** D1, D2, and D3 are all `pass`; no dimension of any priority is scored `block`. F0 fires by severity precedence, and the next-lower unfired condition is F3.

## Writer Decision

writer_decision=accept

The highest-severity fired condition is F0 (severity 10), so the contract resolves the decision to `accept` rather than to `revise_in_phase_4b` or `escalate_to_evaluator`. Two items are handed to Phase 5 rather than fixed here: the `[preprint]` marking policy is applied at first mention only, and the reference list was carried over from Stage 1 unchanged, so Phase 5 owns the in-text-to-reference cross-check.

**Mechanical checks run on this draft.**

| Check | Command | Result |
|---|---|---|
| Acronym check (#849, body scope) | `scripts/check_acronyms.py --input paper-draft.md --scopes body` | exit 0; 12 definitions present in a form the checker does not parse; 14 residual flags, all proper names or codes defined in prose (TY, FTSE, JSE, ETF, SPDR, DAX, CRediT, DC/RC/NC, VolGAN, SQ1–SQ3) |
| Three-layer citation lint (v3.7.3) | `scripts/check_v3_7_3_three_layer_citation.py paper-draft.md` | PASSED, 1 file scanned, exit 0 |
| Citation coverage | 41 corpus IDs vs 41 `<!--ref:-->` slugs | 41 cited, 0 uncited, 0 unknown, 0 orphan reference entries |
| Body word count | `stage2/measure_words.py paper-draft.md --per-section` | 7,573 total; per-section as reported under D5 |
