# Devil's Advocate Report — Checkpoint 3

**Target:** `phase4-report.md` — Stage 1, Phase 4 draft, ARS v3.24.4 validation run
**Checkpoint definition:** `skills/deep-research/agents/devils_advocate_agent.md` § CHECKPOINT 3; `skills/deep-research/SKILL.md` Phase 5 / Checkpoint Rules
**Inputs read:** `phase1-scoping.md`, `phase2-bibliography.md` (spot-checked), `phase2-verification.md`, `phase3-synthesis.md`, `phase4-report.md`, `run-log.md`
**Review scope:** full text of all six files; no external retrieval; no re-derivation of the 41-row matrix. Arithmetic and cross-document counts were checked against the phase files.
**Date:** 2026-11-23

---

## 1. Verdict

### REVISE

**Counts: 0 Critical · 7 Major · 10 Minor.**

No fatal flaw was found. The report's core thesis survives the scan within its declared read scope: the corpus certifies static admissibility and does not enforce or test dynamic no-arbitrage *as reported in abstracts*. The 41 DOIs resolve, no source is fabricated, and the static/dynamic separation is defined before coding and applied consistently. What fails is the packaging around the thesis: the 41-row denominator includes work the report's own scope rules exclude; the abstract and conclusion state abstract-level coding results as facts about "the literature"; one concluding sentence contradicts Table 3; and two integrity statements (AI disclosure, abstract citations) claim more than the pipeline performed. All are repairable by revision, without a new search, a new source, or a change to the core finding.

The severity calibration rule applied here: a Critical is a flaw that invalidates the core argument or methodology. The strongest candidates — the "0 of 41 dynamic" claim and the four-family taxonomy — survive in bounded form because the report itself states the bound in §5.1 and §5.3. The defects are in the edges, not the load-bearing analysis. Hence REVISE, not BLOCK.

### Finding register

| ID | Severity | Finding | Primary location |
|---|---|---|---|
| M1 | Major | Corpus composition contradicts the report's own scope labels: 5 pre-2015 baselines are counted inside a "2015–2026" corpus; C5 is a single-stock panel counted despite "single-name equities excluded by design" | Header L8; §3.1 L99; Table 2 L80; Table 3 L127–135; §4.5 L181; §5.3 L199; Appendix C L327–336 |
| M2 | Major | The two zero counts and "all 41 rows" are stated as study-level facts, not abstract-level coding results; the abstract and conclusion then generalize to "the literature" | Abstract L17; §3.5 L115; §4.3 L155; §4.5 L181; §4.6 L185; §5.1 L191; §6.2 L209 |
| M3 | Major | The dynamic-gap section is not internally auditable: ten rows claimed but eight named; the partial-abstract set differs across Phase 2, §3.3, §5.3 and Appendix C; the closest cases are not individually adjudicated | Table 2 L81; §4.5 L181; §3.3 L107; §5.3 L199; Appendix C L328 |
| M4 | Major | The concluding epigram contradicts Table 3: "repair offers audit without proof; penalty methods offer neither" is false for the report's own counts | §6.2 L209 vs Table 3 L127–135; §4.2 L143–149; §4.3 L159 |
| M5 | Major | The AI disclosure overstates verification and human oversight; both claims are contradicted by §5.3 and by the unattended-run record | AI Disclosure L211–213; Phase 1 L173; §5.3 L199 |
| M6 | Major | Significance rests on an uncited harm premise; the benign alternative (static-only certification may be economically sufficient) is never considered; the journal-policy recommendation outruns the evidence | §1.1 L25; §1.4 L41; §5.2 L195; §6.1 L205 |
| M7 | Major | The abstract attributes the report's own aggregate counts to single sources (Anagha, Niu, Xiong & Liu) | Abstract L17 |
| m1 | Minor | §2.3 heading says "Seven-Dimension" but the text declares eight and Table 2 has eight rows | L71–72; Table 2 L80–87 |
| m2 | Minor | "The 31 queries yielded 775 records" is the requested count, not the retrieved count: one query returned nothing, so 750 were retrieved | §3.2 L103; Appendix A L261–274 |
| m3 | Minor | The generation-family paragraph misdescribes which branch measures what and on which data | §4.2 L149 |
| m4 | Minor | The "5.4 percent" butterfly floor has no defined denominator or unit | §4.2 L147; §4.3 L161 |
| m5 | Minor | §5.3's "six [preprints] from 2025–2026" is four by the report's own reference years; the "12 known-provenance" denominator is not reproducible and includes an out-of-index row | §5.3 L199 |
| m6 | Minor | Two pre-declared process steps were not executed and are not flagged as deviations: the calibration-subset double coding and CP2's targeted full-text retrieval | Phase 1 L112; Phase 2 L97; Phase 3 L268; Phase 4 L10, L199 |
| m7 | Minor | The A/B/C rubric grades (11/13/17) are reported but never used analytically, contrary to Phase 3's claim that C-graded sources carry their grade into themes | §3.4 L111; §4; Phase 3 L292 |
| m8 | Minor | Appendix C does not carry the comparability code or the (M, E, V) triple described in §3.5, so the claim that every body number traces to a recorded artefact is not met | L45; §3.5 L115; Appendix C L294–338 |
| m9 | Minor | The four-family taxonomy's evidence mapping is partly constitutive; "four loci, four meanings" is presented as a finding without a falsification condition | §2.2 L55; §4.3 L157; §5.3 L199 |
| m10 | Minor | The evidence-status rule for hybrid rows is implicit: G6 is proof plus audit; N1 is architecturally enforced but coded penalty/test | §3.4 L111; §4.2 L143–145; §4.3 L159 |

---

## 2. Findings

### Critical issues

**None.**

A Critical finding would have to do one of three things: show that the corpus is fabricated or misrepresented, show that the central claim is contradicted by the report's own evidence, or show that the method cannot answer the research question. None of these holds. All 41 DOI lookups resolved (Phase 2 L11), no record is flagged retracted (Phase 2 L11), the 17/16/8 split is arithmetically consistent across Table 3 and Appendix C, and the ten-row dynamic list in Phase 3 supports the zero-dynamic result once G7 and R8 are restored to the enumeration. The attacks that land (below) narrow the claim's scope; they do not falsify it.

### Major issues

#### M1 — The corpus composition contradicts the report's own scope labels

- **Type:** Scope / Evidence base / Traceability
- **Location:** Header L8 ("Corpus: 41 sources ... 2015–2026, equity-index options"); §3.1 L99 ("pre-2015 work was admitted only as flagged seminal background"; "single-name equities ... excluded by design"); §4.5 L181; Table 2 L80; Table 3 L127–135; Appendix C L327–336; §5.3 L199.
- **Problem:** Two composition rules are stated and then broken. First, five of the 41 rows are pre-2015: S1 Gatheral & Jacquier 2013, S2 Fengler 2009, S3 Hagan et al. 2014, S4 Bodurtha & Jermakyan 1999, S5 Fengler et al. 2006. Phase 1 L90 said pre-2015 work is "background only and is not counted as core evidence"; Phase 3 L282 already called the five "flag-exempt seminal rows." They are nevertheless counted in every headline total — 41 sources, the 17/16/8 split, 41/41 static coverage, 0/41 dynamic, 0/41 comparable. Second, C5's panel is 2,576 single stocks, which Phase 2 L75 explicitly scope-flagged; §3.1 says single-name equities were "excluded by design," and the Phase 4 limitations never repeat the flag. The report therefore says "2015–2026, equity-index only" while counting five pre-2015 rows and one single-stock row.
- **Impact:** The headline N is inflated by 12% background work, and one row violates the asset-scope claim. Removing the five baselines and C5 does not change the direction of the dynamic finding (0 remains 0), but it changes the numbers a reader will quote, and it weakens the two flagship zero counts (M2). A hostile reviewer can show that the corpus label and the corpus contents disagree without reading beyond the report's own header and Appendix C.
- **Recommendation:** Report the corpus as "36 core 2015–2026 rows + 5 seminal background rows = 41," or keep the 41-row ledger and add the core subtotal (36 rows: 16 proof / 14 test / 6 assumption) and the construction subtotal (31 rows: 13/13/5). Recompute the headline percentages on the core set: "0 of 36 core (0 of 31 construction rows; 5 background rows separate)." Add one sentence to §3.1 or §5.3 disclosing that C5 is a flagged single-stock exception, or drop C5. Do not change the conclusion.

#### M2 — The two zero counts are stated as facts about studies, then generalized to "the literature"

- **Type:** Evidence / Generalization / Hasty generalization
- **Location:** Abstract L17; §3.5 L115; §4.3 L155; §4.5 L181; §4.6 L185; §5.1 L191; §6.2 L209.
- **Problem:** Four distinct overstatements compound. (a) "In all 41 rows the certified object is a single date's surface" cannot be asserted for the three metadata-only rows (P4, P7, R4), which the report itself says cannot be assessed beyond title (§4.2 L143, L147; Appendix C). The assessable denominator is 38. (b) §3.5 promises that "the verb 'reports' is used deliberately throughout," but the load-bearing absence sentences drop it: the abstract says "none enforces or tests"; §4.3 says "is enforced in none"; §4.5 says "the number is 0 of 41"; §6.2 says "the literature answers." (c) "No two studies share data, metric and tolerance" (L17) is an ontological claim about studies; the evidence supports only "no two rows can be shown comparable from the abstracts," and §4.6 admits tolerances are "frequently unstated," so the 0/41 is partly driven by missing reporting. (d) "The literature answers the static question and leaves the dynamic one open" (L17, repeated at L209) is a field-level claim from 41 OpenAlex abstracts, one failed query, an English-only corpus, a 2015–2026 window, and a design that excludes pre-2015 dynamic-arbitrage theory.
- **Impact:** This is the report's central claim. The body's §5.1 and §5.3 are careful; the abstract and conclusion are not. The finding survives in the narrowed form ("this corpus, as abstracted"), but not in the broad form ("the literature"). The mismatch is exactly what a hostile reviewer will quote.
- **Recommendation:** Add "as reported in abstracts" to every absence sentence; state the assessable denominator (38; 36 core; 31 construction) in the abstract and §4.5; replace "the literature" with "this corpus" at L17 and L209; for comparability, say "no two rows can be shown comparable from what the abstracts report" and add a one-line sensitivity count under a looser criterion (same metric family and overlapping market), or explain why not.

#### M3 — The dynamic-gap section is not internally auditable

- **Type:** Evidence accounting / Traceability
- **Location:** Table 2 L81 ("Dynamic consistency | 10"); §4.5 L181; §3.3 L107; §5.3 L199; Appendix C L328.
- **Problem:** Three accounting defects sit under the report's most quoted number. (a) §4.5 says "Ten rows engage time at all" but names only eight: P8, R9, G1, G2, G3, C3, C2, C5. G7 and R8 are missing, although Phase 3's list of ten includes them (Phase 3 Theme 1). A reader cannot audit the flagship count from the report. (b) The partial-abstract set is inconsistent: Phase 2 L71 records the four partials as R2, G3, C4, S1; §5.3 L199 lists R2, G3, C2, C4; Appendix C marks five rows Partial (R2, G3, C2, C4, S1), which would make 33 full + 5 partial + 3 metadata = 41, not the stated 34 + 4 + 3. Phase 3 L289 says "4 partial and 3 metadata-only." The report never resolves which set is right. This matters because C2 (Niu 2015) is the conceptual backbone for the dynamic condition and the only review of it; §2.1 L51 says "No source in the corpus states a testable version of the dynamic condition," but if C2's abstract is partial, that categorical sentence is not fully supported. (c) The closest cases — P8's time-indexed arbitrage probabilities, R9's continuous-time Markov chain, C3's path-dependent surface paths — are described but not individually adjudicated. Phase 3 does the adjudication; Phase 4 compresses it out, so the reader cannot see why none counts as dynamic.
- **Impact:** The 0/41 claim is the report's most quoted result; its enumeration and its source-read accounting must be exact. As written, a hostile reviewer can show that the report's own appendix contradicts its own §3.3 and §5.3, and that the one dynamic review's read depth is undetermined.
- **Recommendation:** Name all ten rows (add G7 and R8) or correct the count; reconcile the partial-abstract set to one list and use it consistently in §3.3, §5.3, Appendix C, and the "7 of 41" bound; add one sentence per closest case (P8, R9, C3) explaining the coding decision; state C2's read depth and whether it changes L51's categorical sentence.

#### M4 — The concluding epigram contradicts Table 3

- **Type:** Logic / Internal consistency
- **Location:** §6.2 L209 vs Table 3 L127–135; §4.2 L143–149; §4.3 L159.
- **Problem:** §6.2 says: "Parametric construction offers proof without audit, repair offers audit without proof, penalty methods offer neither, and generation-filtering offers either, depending on how the generator is built." Table 3 codes 3 repair rows as proof-level (R2, R3, R6) and 4 as numerical test; it codes 0 penalty rows as proof and 6 as numerical test. §4.3's "six rows reporting residuals" includes N2 and N6, so penalty rows do report audits. "Repair offers audit without proof" erases three proof-level repair rows; "penalty offers neither" ignores six reported tests. The clean four-way epigram is a rhetorical simplification that the report's own table does not support.
- **Impact:** The conclusion is the most-read paragraph after the abstract; a reader who checks Table 3 sees a contradiction. The underlying thesis ("four kinds of claim") can survive, but only if stated as a tendency with the counts.
- **Recommendation:** Rewrite L209 to match the table: parametric = 6/8 proof, no audits; penalty = 0 proof, 6 tests; repair = 3 proof / 4 test / 2 assumption; generation = 4 proof / 3 test / 1 assumption. Keep "four kinds of claim" as the interpretation, not as a clean partition. Define "audit" (a reported residual/violation test) explicitly, because the "neither" clause depends on it. Do not add a ranking.

#### M5 — The AI disclosure overstates verification and human oversight

- **Type:** Integrity / Attribution
- **Location:** AI Disclosure L211–213; compare §3.3 L107, §5.3 L199, Phase 1 L173, run-log L6.
- **Problem:** "All findings were verified against cited sources" is contradicted by §5.3 ("no theorem was checked, no residual was recomputed") and by the abstract-level read scope; verification was DOI resolution plus abstract reconstruction. "Human oversight was applied throughout the process" is contradicted by the pipeline record: the run is an "unattended end-to-end validation run" with preauthorized checkpoint replies (Phase 1 L173; run-log L6), and Phase 3 L282 notes there was "no independent second reader before Phase 4." The disclosure does not say what the human actually did, and it does not disclose the abstract-level limitation that is central to every finding.
- **Impact:** This is the one place the report claims more verification than the pipeline performed. It does not invalidate the findings, but it undermines the report's credibility on the dimension the disclosure is meant to establish. It is also the kind of statement an ethics/integrity check exists to catch.
- **Recommendation:** Replace with a precise statement: "Verification was abstract-level: 41/41 DOIs resolved and abstracts were reconstructed from OpenAlex, Crossref and Semantic Scholar; no full text, theorem, or residual was checked. The run was unattended under operator preauthorization; checkpoint replies were recorded; coding was single-analyst with no independent second reader." If the operator did review the draft, say what was reviewed and when.

#### M6 — The significance claim rests on an uncited harm premise, and the benign alternative is not considered

- **Type:** Significance / Unsupported premise / Scope creep
- **Location:** §1.1 L25; §1.4 L41; §5.2 L195; §6.1 L205.
- **Problem:** L25 asserts that an arbitrageable fitted surface "propagates into risk numbers, margin and capital; it is not a cosmetic defect in a plot." No source in the corpus measures that propagation. The corpus's own numbers are at least as consistent with the benign reading: R1 changes prices minimally inside bid–ask bounds; R7 reports below 1% static violations with 98–99% inside-spread coverage; R5's 5.4% floor is a residual, not a demonstrated loss. The report never considers that static admissibility may be what single-date pricing and risk consumers actually need, and that dynamic enforcement may be a scientific gap rather than an operational emergency. The journal-policy recommendation in §5.2 ("requiring a machine-readable enforcement statement") is the furthest outrun of the evidence.
- **Impact:** The "so what" is adequate at the methodological level (validation vocabulary, benchmark design) but not at the economic level. The practical recommendations are stronger than the evidence. The strongest hostile reading — "this is an agenda for a problem no desk has" — is not answered.
- **Recommendation:** Either cite/argue the harm mechanism or mark it as an assumption; add one paragraph on the benign alternative and why the report still recommends the dynamic agenda; soften or drop the journal-policy sentence. Keep the methodological significance, which is well supported.

#### M7 — The abstract attributes the report's own aggregate counts to single sources

- **Type:** Attribution / Citation integrity
- **Location:** Abstract L17.
- **Problem:** "Coding of an evidence matrix shows that 17 sources ... 8 assert admissibility without either (Anagha, 2026)"; "none enforces or tests dynamic no-arbitrage (Niu, 2015)"; "zero rows are directly comparable (Xiong & Liu, 2026)." These are the report's coding results, not findings of the cited papers. Anagha (G6) is the one proof-plus-audit row, not the source of the 17/16/8 distribution; Xiong & Liu (R5) is one repair row, not the comparability analysis. The parentheticals are probably citation-emission anchors, but they read as scholarly support in the abstract, which is the most-read text.
- **Impact:** Misattribution in the abstract is a citation-integrity problem. It also makes the aggregate claims look sourced when they are the report's own judgement, which is the opposite of the transparency the rest of the report practices.
- **Recommendation:** Remove the three parenthetical source citations from the aggregate sentences; if a pointer is needed, say "(this report's coding; Appendix C)" or cite the Phase 3 matrix. Keep source citations where they belong: on the individual rows.

### Minor issues

- **m1 — Dimension-count heading error.** §2.3 is titled "The Seven-Dimension Evaluation Matrix" but the first sentence declares "Eight evaluation dimensions" and Table 2 has eight rows (L71–72, L80–87). Phase 1 declared eight; the heading is a Phase 3 carryover (Phase 3 §5.4 used seven). Fix the heading to "Eight-Dimension."
- **m2 — 775 is requested, not retrieved.** §3.2 L103 says "The 31 queries yielded 775 records"; Appendix A L261 says each returned 25 and one returned nothing after a 429. 31 × 25 = 775 requested; 30 × 25 = 750 retrieved. Reword to "requested 775; one query returned nothing, so 750 were retrieved."
- **m3 — Generation-family branch description is muddled.** §4.2 L149 says "Only the second branch measures anything, and only on synthetic data." G5 (penalised-sampling branch) reports a 90.8% pass rate on an empirical surface distribution, not synthetic; G2 reports hedging and VIX realism on SPX. The sentence misdescribes both branches. Rewrite to distinguish the architectural branch (G6, synthetic) from the penalised-sampling branch (G5, empirical).
- **m4 — "5.4 percent" has no unit.** The butterfly floor reported by R5 (L147, repeated at L161) is described as a percentage without a denominator: 5.4% of grid cells, of days, or of price? State the unit or drop the number.
- **m5 — Limitations arithmetic.** §5.3 L199 says "six of them [the 11 preprints] from 2025–2026"; by the report's own reference years the count is four (P8 2026, R6 2026, R7 2025, G6 2026). The same paragraph's "ten of the twelve rows with known provenance" does not identify the 12; the denominator includes C5, which is a single-stock panel out of the index frame, so "US index data" is not accurate for the numerator. List the 12 or drop the percentage.
- **m6 — Two pre-declared process steps are not carried out or flagged.** Phase 1 L112 promised the coding scheme applied twice to a calibration subset with counts reported; Phase 2 L97 records "no dual review or calibration." Phase 3 L268 recommended retrieving 3–5 full texts (G6, R5, P2, G2, G7) in Phase 4 to test the absence claim; Phase 4 L10/L199 says abstract-level throughout. Add one sentence to §5.3 recording both as declined deviations and why.
- **m7 — A/B/C grades are decorative.** The rubric grades (A 11, B 13, C 17; §3.4 L111) are reported but never used in the findings, contrary to Phase 3 L292 ("C-graded sources contribute to themes with their grade attached"). Either attach grades at point of use or state that the grades are a verification artefact, not an analytic variable.
- **m8 — Appendix C does not reproduce the coding instrument.** The ledger (L294–338) lacks the comparability code and the (M, E, V) triple described in §3.5, so the claim that "every number in the body can be traced to a recorded artefact" (L45) is not met for the 0/30/11 comparability split or the enforcement/verification coding. Add two columns or point explicitly to the Phase 3 matrix.
- **m9 — The taxonomy's evidential mapping is constitutive.** Families are defined by enforcement locus, and "a theorem, an optimisation residual and an acceptance test are the best each family can produce" (L55) is entailed by that definition. §4.3's "Four loci, four meanings" is then presented as a finding. The report already calls the taxonomy a proposed instrument (L199; Phase 3 §5.5); add one sentence stating what would falsify the locus→evidence mapping, and label the mapping as framework, not discovery.
- **m10 — The hybrid evidence-status rule is implicit.** G6 reports both a guarantee and an audit but is coded "Proof"; N1 enforces through a gated architecture but is coded "Penalty / numerical test." §3.4 does not state the precedence rule, and §4.3's "only Anagha both guarantees and audits" depends on it. State the rule (strongest claim in the abstract, with audit noted separately) in §3.4.

---

## 3. Strongest Counter-Arguments

### CA-1 — The dynamic void is an artefact of a strict coding rule, a narrow retrieval frame, and a single coder

**The attack.** The report defines dynamic no-arbitrage as a property of the joint law of a surface family, with no self-financing strategy in the option panel. That is a stringent object; almost no applied surface-construction paper attempts it. The corpus then (i) covers only 2015–2026, excluding the foundational dynamic-arbitrage theory; (ii) uses OpenAlex only, English only, with one failed query; (iii) selects on "an enforcement claim," which may exclude papers that audit dynamics without claiming enforcement; and (iv) was coded by one analyst with no reliability check. The strongest form: *you have not shown that the field lacks dynamic enforcement; you have shown that 41 abstracts, selected by an enforcement-claim criterion, do not report it.*

**The report's best rebuttal.** The definition was fixed before coding (§2.1, §3.5); the ten time-engaging rows are named; G7 explicitly declines the dynamic claim (§2.1, §4.4); the retrieval-artefact reading is stated as the most consequential alternative (§5.1); and the absence claim is bounded in §3.5 and §5.3. The body's claim is corpus-level and survives.

**Assessment.** The rebuttal works for the body but not for the abstract and conclusion, which say "the literature." It also does not answer the selection-rule effect, and it does not resolve C2's read depth (M3), even though C2 is the one review that could state a testable dynamic condition. The finding should be narrowed, not withdrawn: "0 of 38 assessable abstracts in this corpus report enforcing or testing dynamic no-arbitrage" is defensible; "the literature has not posed the dynamic question" is not.

`[DA-DECISION: Score 4/5 | ACTION: Hold (narrow, not withdraw) | REASON: body is properly bounded; abstract/conclusion outrun it, and C2's read depth is unresolved.]`

### CA-2 — The four-family taxonomy is constitutive, so "four loci, four meanings" is analytic, not empirical

**The attack.** The families are defined by where enforcement acts: parameter domain, objective, post-fit output, sampler. The evidence kind is a mechanical consequence of the locus: a parameter-domain guarantee can be stated as a theorem; a penalty can only report a residual; a projection can only report a repaired point; an acceptance test can only report a pass rate. The report then presents "four loci, four meanings" as a finding. A hostile reviewer: *you have rediscovered that theory papers produce theorems and empirical papers produce tests.* The taxonomy also does not organise the second half of the RQ: dynamics is orthogonal to the enforcement locus (C3, G2, G7 cross the cut), so a taxonomy of static enforcement loci cannot illuminate the dynamic question.

**The report's best rebuttal.** The taxonomy is a proposed instrument, not a validated finding (§5.3; Phase 3 §5.5); the mapping is not mechanical — N1 is architecturally enforced but coded penalty, and R3/R6 straddle loci (§2.2); Table 3's distribution could have come out otherwise; the boundary friction is disclosed rather than hidden. The taxonomy earns its place by making the evidence distribution legible and by exposing the boundary cases.

**Assessment.** The rebuttal defeats "tautology" but not "analytic claim presented as empirical." The report should say the locus→evidence mapping is constitutive and state what would falsify it (a penalty paper that proves admissibility; a parametric paper that reports a residual audit). It should also admit that the taxonomy organises the static half of the RQ well and the dynamic half poorly, because dynamics is not a locus. As written, §4.3's "Four loci, four meanings" is a framework statement, not a finding.

`[DA-DECISION: Score 3/5 | ACTION: Hold | REASON: boundary cases show the taxonomy is not mechanical, but the evidential mapping is still entailed by the coding scheme, and the dynamic half is not organised by it.]`

### CA-3 — Both zero counts are guaranteed by definitional strictness

**The attack.** "Directly comparable" requires identical data, metric and tolerance. Almost no empirical literature meets that bar; the report itself says tolerances are "frequently unstated," so the 0/41 is partly a missing-data result, not a property of the field. "Dynamic" requires a process-level guarantee or test; applied papers do not attempt it. Both zeros are true by construction and therefore uninformative about the literature.

**The report's best rebuttal.** The definitions were fixed before coding; comparability is "deliberately conservative" (§3.4); 30 rows are "reported for context," so near-comparability is visible; the conclusion is explicitly about "kinds of evidence," not performance; and the no-ranking stance follows from the evidence rather than from a preference.

**Assessment.** The rebuttal is good on intent but incomplete. The abstract states "no two studies share data, metric and tolerance" as an ontological fact, and "zero rows are directly comparable" is used to justify the agenda. A sensitivity count under a looser criterion (same metric family, overlapping market) and a statement that missing tolerances drive the result would make the zero informative. The report should also say explicitly that 0/41 is a property of the corpus under a strict coding, not a discovery about the field.

`[DA-DECISION: Score 3/5 | ACTION: Hold | REASON: the strict definitions are disclosed, but the abstract states the result as a fact about studies and no sensitivity count is given.]`

### CA-4 — The proof/audit asymmetry may be a genre effect, and the grading is self-reported

**The attack.** Theory papers do not report violation rates; empirical papers do not prove theorems. The "proof and audit come from disjoint source sets" finding is what a genre split looks like from a distance. The evidence-status grading is self-reported by abstracts, single-coded, and the one overlapping row (G6) is a preprint on synthetic data, so the "guarantee plus audit" instance is thin. A hostile reviewer: *your central evidential finding is a publication norm.*

**The report's best rebuttal.** G6 exists; G5 and N5's own abstracts concede the residual framing; Alternative Explanation 2 states the venue-norm reading (§5.1); the asymmetry is still a gap for a practitioner choosing a method; and the theme is labelled Moderate (Phase 3 Theme 3), not Strong.

**Assessment.** The rebuttal holds for the practitioner-facing claim, and the report is candid. But it does not test the selection-rule version of the artefact — papers that audit without claiming enforcement may be excluded by the inclusion criterion — and the "only G6 both" sentence depends on a hybrid coding call (m10). The finding should be stated as "the corpus, as abstracted, contains no theorem-plus-market-audit row" rather than "proof and audit come from disjoint source sets," which sounds field-level.

`[DA-DECISION: Score 3/5 | ACTION: Hold | REASON: venue-norm alternative is disclosed; the selection-rule alternative and the hybrid coding are not.]`

---

## 4. Cherry-Picking and Motivated-Reasoning Check

| Check | What was tested | Result |
|---|---|---|
| Hypothesis disconfirmation | H1–H3 were declared in Phase 1; are any disconfirmed? | **Pass.** H1's second clause is disconfirmed in direction (dynamic is absent, not asserted-and-tested); H2's first clause is not supported (no penalty/repair row reports lower fit error against a constrained baseline); H3 is split. This is the strongest evidence against motivated reasoning. (Phase 1 §1; Phase 3 §2 hypothesis table) |
| Source balance | 8 parametric / 6 penalty / 9 repair / 8 generation / 5 conditions / 5 baselines | **Pass.** No family is privileged: the parametric family gets 17 proofs and is charged with zero audits; generation gets the only overlap and is charged with the weakest enforcement descriptions. (Phase 3 §6.2; Table 3) |
| Preprint handling | Are the 11 preprints flagged at point of use? | **Pass with a minor arithmetic error.** Preprints are flagged; the strictest claims are disclosed as clustering there. "Six … from 2025–2026" is four by the reference years (m5). (L141, L199) |
| Single-source dependency | Does Theme 4 or the "only G6" sentence rest on one study? | **Partial, disclosed.** Theme 4 is labelled Emerging and restricted to G6's within-study comparison; the "only G6 both" claim is disclosed. The abstract's 17/16/8 split does not depend on G6, but the overlap sentence does. (L159, L161) |
| Negative results | Did the search find any study reporting failure? | **Not retrievable; disclosed.** The report states that negative results were not retrieved and that prevalence of reported success may be overstated. This is a genuine limitation, not a concealment. (L199) |
| Selection rule vs thesis | Does "an enforcement claim" inclusion select against audit-only work and manufacture the proof/audit asymmetry? | **Not tested — the main unaddressed risk.** The 40 "relevant but not selected" records are the largest discretionary decision; the report reports the bucket separately but does not examine whether it contains audits. (L103) |
| Citation attribution | Are aggregate counts attributed to sources? | **Fail.** The abstract's 17/16/8, 0-dynamic and 0-comparable sentences carry single-source parentheticals. (L17; M7) |
| Non-ranking stance | Is there an implicit league table or winner? | **Pass.** No league table, no vote count; within-study baselines only; the report explicitly declines ranking. (L111, §4.6) |

**Assessment.** No evidence of deliberate cherry-picking. The report reports disconfirming evidence for its own hypotheses, which is the behaviour a confirmation-seeking synthesis would not produce. Two structural risks remain: the enforcement-claim inclusion rule (untested) and the abstract's aggregate citations (a fixable error). The first is a threat to the proof/audit theme; the second is a citation-integrity defect, not a selection effect.

---

## 5. Alternative Explanations

| # | Alternative explanation | Considered by the report? | Adequacy |
|---|---|---|---|
| 1 | **Retrieval/vocabulary artefact.** Dynamic-arbitrage work uses different terms and may not match the Phase 2 queries. | Yes — §5.1, first alternative; §5.3. | Adequate as a disclosure; not tested. This is the report's own "most consequential unanswered question." |
| 2 | **Publication/venue norm.** Theory journals publish theorems; empirical venues publish violation rates. | Yes — §5.1, second alternative; Phase 3 alternative 2. | Adequate. It explains the asymmetry without dissolving the practitioner-facing gap. |
| 3 | **Noise floor/measurement model.** The 90.8% and 0.00% pass rates may reflect different noise and tolerances, not different method quality. | Yes — §4.4 (quote noise vs test rejection); Phase 3 T5. | Adequate: the report says the rates cannot be separated without a noise floor and test power, and no row estimates either. |
| 4 | **Selection-rule effect.** The inclusion criterion "an enforcement claim" may exclude audit-only studies, manufacturing the proof/audit asymmetry. | **No.** | **Unaddressed.** This is the strongest alternative for Theme 3. The 40 "relevant but not selected" records could contain audits; the report does not check. |
| 5 | **Benign neglect/economic sufficiency.** Static admissibility may be what single-date pricing and risk consumers actually need; dynamic enforcement may be a scientific gap, not an operational one. | **No.** | **Unaddressed.** This is the strongest alternative for the "so what" claim (M6). The report's own R1/R5/R7 numbers are consistent with small static violations. |
| 6 | **Pre-2015 dynamic theory excluded by the date cut.** The dynamic no-arbitrage literature is older than 2015; the report's window excludes it. | Partially — the 2015 cut is disclosed as a scope boundary, but not discussed as a threat to "the literature" claim. | **Incomplete.** The report should say the field-level claim is about 2015–2026, not about the literature as a whole. |
| 7 | **Abstract under-reporting.** Abstracts may omit audits that exist in full texts. | Yes — §5.1; §5.3; m6. | Adequate as a disclosure. The unexecuted CP2 full-text recommendation (m6) leaves it unresolved. |

**Assessment.** The report considers four of seven alternatives and handles them fairly. The two unaddressed alternatives — selection-rule effect and benign neglect — map directly onto its two central claims (proof/audit asymmetry; significance). They are the strongest counter-arguments in this review, and neither requires new data to address: one is a coding check on the 40 excluded records, the other is a paragraph of argument.

---

## 6. Vulnerability Scan

| Vulnerability | Test applied | Result | Evidence | Severity |
|---|---|---|---|---|
| Central absence claim (0/41 dynamic) | Robustness to coding rule, retrieval, read depth | **Partial** — survives in bounded form; enumeration and C2 read depth are not auditable | §4.5 L181; §2.1 L51; M3 | Major |
| "All 41 rows" static predicate | Can metadata-only rows support it? | **Fail** — 3 rows cannot; assessable N = 38 | §4.3 L155; Appendix C; M2 | Major |
| Field-level generalization ("the literature") | Is the claim bounded to the corpus? | **Fail** — abstract and §6.2 use "the literature" | L17, L209; M2 | Major |
| 0/41 comparability | Is the triple-match bar informative? | **Partial** — true under a strict, disclosed definition; missing tolerances drive it; no sensitivity count | §3.4 L111; §4.6 L185; M2/CA-3 | Major |
| Corpus composition | 2015–2026 and equity-index-only? | **Fail** — 5 pre-2015 rows counted; C5 single stocks | L8, L99, L181; M1 | Major |
| Conclusion vs Table 3 | Does §6.2 match the counts? | **Fail** — repair/penalty epigram contradicted | L209 vs L127–135; M4 | Major |
| Dynamic section enumeration | Are the ten rows named? | **Fail** — 8 named; G7/R8 missing | L181; M3 | Major |
| Abstract coverage accounting | Do the partial sets agree? | **Fail** — Phase 2 {R2,G3,C4,S1}; §5.3 {R2,G3,C2,C4}; Appendix C 5 rows | L107, L199, L328; M3 | Major |
| Four-family taxonomy | Is the evidence mapping falsifiable? | **Partial** — useful instrument, but the mapping is constitutive and the dynamic half is not organised by it | L55, L157; m9/CA-2 | Minor |
| Evidence-status grading | Are hybrid rows handled by a stated rule? | **Partial** — G6/N1 labels carry the "only row both" and "penalty 0 proof" claims; rule implicit | L111, L159; m10 | Minor |
| Cherry-picking | Source balance, disconfirmation, negative results | **Partial** — no deliberate cherry-picking; selection rule and 40 discretionary exclusions untested; no negative results (disclosed) | §3.2 L103; Section 4 | Minor (risk) |
| Motivated reasoning | Are hypotheses disconfirmed? | **Pass** — H1b and H2a disconfirmed; H3 split | Phase 1 §1; Phase 3 §2 | Observation |
| Alternative explanations | How many of the plausible set are considered? | **Partial** — 4 of 7; selection-rule and benign-neglect unaddressed | §5.1 L191; Section 5 | Major (for M6) |
| Scope creep | Do recommendations outrun evidence? | **Partial** — journal-policy sentence; otherwise the agenda is within scope | L195; M6 | Minor |
| "So what" | Is significance established? | **Partial** — methodological yes, economic no | L25, L195; Section 9 | Major |
| AI disclosure | Adequate and accurate? | **Fail** — verification and oversight overstated | L211–213; M5 | Major |
| Citation integrity | Are aggregate counts correctly attributed? | **Fail** — three abstract parentheticals | L17; M7 | Major |
| Traceability | Do Appendix C and the body agree? | **Partial** — comparability/M,E,V missing; partial-set mismatch; 10-vs-8 | L45, L294–338; M3/m8 | Major |

---

## 7. Fatal vs Limitation Classification

| Classification | Items | Why |
|---|---|---|
| **Fatal / Critical** | None | No source fabrication (41/41 DOIs resolved, 0 retracted); no data re-analysis to falsify; the static/dynamic distinction is coherent and applied consistently; the 0-dynamic result survives removal of the weakest rows. The closest thing to a fatal flaw would be a false central claim; the surviving challenge is to the claim's scope, not its truth. |
| **Major (must fix in revision)** | M1–M7 | The denominator includes out-of-scope rows; the two zero counts are stated as study-level facts; the dynamic section cannot be audited from the report; the conclusion contradicts Table 3; the AI disclosure overstates verification and oversight; the significance rests on an uncited harm premise; the abstract misattributes its own counts. Each is repairable by editing, without new search or new sources. |
| **Genuine limitations (properly disclosed)** | Abstract-only read; 11 preprints; 3 metadata-only; single coder; English/OpenAlex/US skew; one failed query; no COI/funding retrieval; no negative results; no PRISMA claim; taxonomy unvalidated; no ranking | Each is stated in §5.3 and bounds the claims. The report does not use them to excuse a stronger claim, with the two exceptions listed next. These are limitations, not flaws, and should be retained. |
| **Performative or under-specified limitations** | "All findings were verified"; "Human oversight was applied throughout"; "six [preprints] from 2025–2026"; "every number ... traced to a recorded artefact" | Contradicted by the pipeline record or the appendix. These should be corrected, not merely disclosed. (M5, m5, m8) |
| **Genuine but under-emphasized** | The 17 "proof-level" rows are self-reported, not checked; the abstract says "assert," which is careful, but §4.2's "proof-level" is unqualified; the CP2 full-text recommendation was not executed | The report says "no theorem was checked" in §5.3, but the headline uses "proof-level" more prominently than the caveat. Add "reported" at first use in §4.2 and record the declined CP2 step in §5.3. (m6) |

---

## 8. Required Fixes (REVISE)

These are the minimum edits needed to move the report from REVISE to PASS. None requires a new search, a new source, or a change to the core finding. None recommends a ranking; the non-ranking stance is correct and should be preserved.

| # | Fix | Exact locations | Minimal edit |
|---|---|---|---|
| **R1** | Correct the corpus composition and denominators (M1) | Header L8; §3.1 L99; Table 2 L80; Table 3 L127–135; §4.5 L181; §4.6 L185; §5.3 L199; Appendix C L294–338 | State "36 core 2015–2026 rows + 5 seminal background rows = 41"; add core subtotal 16/14/6 and construction subtotal 13/13/5; change "0 of 41" to "0 of 36 core (0 of 31 construction rows)"; add a C5 scope-flag sentence in §3.1 or §5.3, or drop C5; add a Scope column to Appendix C. |
| **R2** | Bound the zero counts and replace "the literature" (M2) | Abstract L17; §3.5 L115; §4.3 L155; §4.5 L181; §4.6 L185; §6.2 L209 | "As reported in abstracts"; "38 assessable rows (3 metadata-only unassessable)"; "no two rows can be shown comparable from the abstracts"; "this corpus," not "the literature"; add the one-line sensitivity count for comparability. |
| **R3** | Make the dynamic section auditable (M3) | Table 2 L81; §4.5 L181; §3.3 L107; §5.3 L199; Appendix C L328 | Name all ten rows (add G7, R8); reconcile the partial-abstract set to Phase 2's {R2, G3, C4, S1} or explain the C2/S1 swap; add one sentence per closest case (P8, R9, C3); state C2's read depth and whether L51 changes. |
| **R4** | Align the conclusion with Table 3 (M4) | §6.2 L209; Table 3 L127–135 | Rewrite the epigram with the counts: parametric 6/8 proof, no audits; penalty 0 proof, 6 tests; repair 3 proof/4 test/2 assumption; generation 4 proof/3 test/1 assumption. Define "audit." Keep the "four kinds of claim" interpretation, not a clean partition. |
| **R5** | Correct the AI disclosure (M5) | AI Disclosure L211–213; §5.3 L199 | State abstract-level verification, 41/41 DOI resolution, no full text/theorem/residual checked; state that the run was unattended under preauthorization and coding was single-analyst. |
| **R6** | Ground or narrow the significance claim (M6) | §1.1 L25; §1.4 L41; §5.2 L195; §6.1 L205 | Mark the propagation sentence as an assumption or cite it; add one paragraph on the benign alternative; soften or drop the journal-policy recommendation; keep the methodological significance. |
| **R7** | Fix the abstract attributions (M7) | Abstract L17 | Remove the three parenthetical source citations from the aggregate sentences; point to "this report's coding, Appendix C" if needed. |

**Non-blocking fixes** (recommended in the same revision, not gating): m1 heading; m2 775/750; m3 generation branches; m4 5.4% unit; m5 limitations arithmetic; m6 process-deviation note; m7 grades unused; m8 Appendix C coding columns; m9 taxonomy falsification sentence; m10 hybrid-status rule.

---

## 9. "So What?" Significance Judgment

**Qualified pass.**

The report answers "so what" at the methodological level, and that answer is good. For a validation team, the contribution is usable: it converts "arbitrage-free" from a label into three questions — which condition, at what tolerance, verified how — and it shows that the corpus's evidence cannot support a method ranking. For a benchmark designer, the four-field comparability proposal (panel, condition set with tolerance, metric with aggregation, residual reporting format) is actionable. The agenda's first three items — a residual audit for proof-level constructions, test-power estimation, and a dynamic panel — are cheap, well-motivated, and follow directly from the gaps. That is a real contribution and it does not depend on the report's weaker claims.

The report does not answer "so what" at the economic level, and it should stop implying that it does. The sentence that an arbitrageable surface "propagates into risk numbers, margin and capital" (L25) is uncited, and no study in the corpus measures that propagation. The corpus's own repair numbers — R1's minimal price changes inside bid–ask bounds, R7's below-1% static violations with 98–99% inside-spread coverage, R5's 5.4% floor — are at least as consistent with the benign reading that static violations are small and static enforcement is what single-date consumers actually need. The journal-policy recommendation (L195) is the furthest outrun of the evidence: the report has shown that the literature's vocabulary is loose and its benchmarks are incomparable, not that journals should mandate a machine-readable enforcement statement.

**Judgment.** Adequate for a methodological review; insufficient for the practical-emergency framing and the journal-policy recommendation. The strongest defensible "so what" is: *the field's evidence cannot currently support the claims its vocabulary invites, and the three-question protocol plus the first three agenda items are the cheapest way to fix that.* That is worth publishing. The claim that dynamic enforcement is an operational necessity is not established by this corpus, and the report should either establish it or present it as a scientific gap.

---

## 10. Strengths Acknowledged

- **The static/dynamic separation is the report's best conceptual move.** It is defined before coding (§2.1), applied consistently, and it does real work: it explains why the corpus's "arbitrage-free" claims are not interchangeable. The report does not blur the two conditions even when its sources do.
- **The refusal to rank is principled and well executed.** No league table, no vote count, no citation metric; within-study baselines are used only as internal orderings. This is the correct response to 0 directly comparable rows, and it is rare in reviews of this literature.
- **The report reports disconfirming evidence for its own hypotheses.** H1's second clause and H2's first clause are reported as unsupported; H3 is split. A confirmation-seeking synthesis would have smoothed these into support. This is the strongest evidence that the report is not motivated reasoning.
- **The preprint, metadata-only and partial-abstract disclosures are unusually thorough.** The report flags preprints at point of use (L141), names the metadata-only rows, and states the read-scope bound repeatedly. The problem is that the abstract and conclusion do not always follow the discipline the body establishes.
- **The three-question protocol and the comparability proposal are usable contributions.** They are the parts a practitioner can apply tomorrow, and they do not depend on the report's weaker claims.
- **The agenda is ordered by cost.** Residual audits and test-power estimation can run on existing panels; the dynamic-panel and cross-market studies need new data. That is the right ordering for a research agenda.

---

## 11. Checkpoint 3 Question Checklist

| CP3 question | Result | Basis |
|---|---|---|
| Does the conclusion follow from the evidence, or overstep? | **Oversteps in §6.2 and the abstract; the body follows.** | M2, M4 |
| What is the strongest counter-argument to the main thesis? | The dynamic void is a coding/retrieval artefact; the taxonomy is constitutive; the zero counts are definitional; the proof/audit gap is a genre effect. | Section 3 |
| Would a hostile reviewer find fatal flaws? | **No fatal flaw.** The most damaging findings are the denominator (M1) and the field-level generalization (M2); both are repairable. | Section 7 |
| Is the "so what?" adequately answered? | **Qualified yes** — methodological, not economic. | Section 9 |
| Are limitations genuine or performative? | **Mostly genuine; two performative** (AI disclosure; "six preprints"). | Section 7 |
| Is the AI disclosure adequate? | **No** — overstates verification and oversight. | M5 |

---

*End of Checkpoint 3 report. No other file was modified.*
