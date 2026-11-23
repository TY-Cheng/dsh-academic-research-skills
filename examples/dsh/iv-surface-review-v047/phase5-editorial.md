# Phase 5 — Editor-in-Chief Verdict

**Manuscript.** "Enforcing No-Arbitrage in Equity-Index Implied Volatility Surfaces: A Structured Review of Four Method Families, 2015–2026" (`phase4-report.md`, 342 lines; 41-source corpus; 5,247 words by the author's count).

**Run context.** ARS `deep-research` full-mode pipeline, Stage 1, Phase 5 (Editorial). Inputs: `phase1-scoping.md`, `phase2-bibliography.md`, `phase2-verification.md`, `phase3-synthesis.md`, `phase4-report.md`. The manuscript is a Phase 4 draft, not a submission package; this verdict is an editorial gate for the pipeline, not a journal decision.

**Scope of this review.** Finance/econometrics journal standards on originality, methodological rigor, evidence sufficiency, argument coherence and writing quality, with explicit attention to whether the report stays inside its stated RQ (static vs. dynamic no-arbitrage enforcement across four construction families; evidence status; comparability) and its declared abstract-level read scope. I did not re-run searches, re-code the corpus, or verify DOIs. I did not adjudicate research-ethics or disclosure compliance; the AI-disclosure sentence is assessed only for internal accuracy (m12). No ranking of construction methods is offered in this review, and none should be added in revision.

---

## 1. Verdict

**MAJOR REVISION**

The report is an unusually disciplined evidence audit with a real, well-motivated question: it changes the unit of analysis from method to evidence and exploits that shift to show that proof-level and audit-level support come from nearly disjoint parts of the literature (`phase4-report.md` §4.3, L159) and that the field's static and dynamic vocabulary is conflated (§4.4, L177). The scope discipline is genuinely good — abstract-only declared up front (L10), no PRISMA claim (L17, L115), no ranking (L17, L205), absence of a reported audit explicitly not treated as absence of an audit (L115). But the report is not yet publishable in the form that exists. Its closing typology contradicts its own Table 3 (M1); the sentence supporting the central "ten engage time" count enumerates eight (M2); the abstract-level ledger does not reconcile — three different partial-abstract classifications coexist (M3); the abstract attaches the review's own aggregate counts to single sources (M4); two advertised analytical instruments (hypothesis adjudication and the condition/tolerance coding) are never delivered (M5); the search flow overstates retrieved records and leaves the snowballing yield unaccounted (M6); and §4.3 corroborates a cost claim with numbers the report's own protocol forbids comparing (M7). None of these defects requires new data, a new search or a re-analysis, which is why the verdict is MAJOR REVISION rather than REJECT; but they touch the abstract, the headline counts and the conclusion, so the revision is substantial and must be verified against the recorded artefacts.

**Dimension scores.** Scores are 1–5; weights and verdict mapping follow `skills/deep-research/agents/editor_in_chief_agent.md`.

| Dimension | Weight | Score | Justification |
|---|---:|---:|---|
| Originality | 20% | 3 | The four-locus taxonomy organises a familiar literature; the distinct contributions are the evidence-status coding and the refusal to rank. No new theory, data or metric; novelty is diagnostic and architectural, not substantive. Phase 1's own FINER novelty score was 3/5. |
| Methodological rigor | 25% | 3 | Protocol is pre-specified and the limitations are disclosed (L103, L107, L115, L199). Against that: the retrieval arithmetic does not close (M6), the read-status ledger does not reconcile (M3), the planned double-coding calibration was not performed and is not reported as a deviation (m16), and the rubric description omits a grading floor (m10). |
| Evidence sufficiency | 25% | 3 | Claims are hedged to what abstracts report (L115, L199) and the retrieval-artefact confound is stated (L191). Held at 3 rather than 2 because the defects are reconcilable bookkeeping/re-use errors; but §4.3 compares numbers the protocol forbids comparing (M7), and the dynamic absence claim rests on abstract-level silence. If M3 or M7 proves unreconcilable, this drops to 2. |
| Argument coherence | 15% | 2 | The concluding typology contradicts Table 3 (M1); the dynamic count and enumeration disagree (M2); the hypotheses are promised and never adjudicated (M5); one negative claim is untraceable (m14); §4.1 repeats its own conclusion (m6). These are load-bearing, not cosmetic. |
| Writing quality | 15% | 3 | Dense, clear, low-hype; the abstract is 182 words, within the 150–250 requirement; tables carry real information. Local problems: jargon not used in the body (m18), a sentence falsified by its own paragraph (m7), duplicate sentences (m6), reference-year inconsistency (m11). |

Weighted total: (3 × 0.20) + (3 × 0.25) + (3 × 0.25) + (2 × 0.15) + (3 × 0.15) = 0.60 + 0.75 + 0.75 + 0.30 + 0.45 = **2.85**, which falls in the 2.0–2.9 band → **MAJOR REVISION**.

---

## 2. Strengths

1. **The report changes the right variable.** Coding each row by evidence status (proof / numerical test / assumption) and by family is the most useful artefact in the run, because it shows where confidence comes from rather than which method "wins" (Table 3, L121–L137; 17 / 16 / 8 over 41). The coding is applied consistently, including the important caveat that status is "the status reported by the source, not a quality grade" (L137).

2. **Claim discipline is unusually good.** The abstract-only read scope is declared before any finding (L10, L115), no PRISMA compliance is claimed (L17, L115), no citation counts or COI statements are invented (L199), and the report explicitly refuses the inference from "no reported audit" to "no audit" (L115). For a review of this corpus, that posture is exactly right.

3. **The verification trail is documented rather than implied.** Forty-one DOI resolutions and zero retractions, the abstract reconstruction path, the one failed query, the single-coder limitation and the five verification conditions are all disclosed (L103, L107, L115, L199). Most reviews this size hide this layer; here it is auditable and mostly traceable.

4. **The alternative-explanation paragraph is the intellectual high point.** §5.1 (L191) states the proof/audit asymmetry, then immediately tests it against a retrieval-artefact explanation and concedes that the two readings cannot be separated within the read scope. That is the difference between a finding and a story, and it is the paragraph a referee will remember.

5. **The definitional-conflation finding is a genuine contribution.** §4.4 (L177) shows that "calendar arbitrage" conflates maturity monotonicity within a date with cross-date consistency, which inflates apparent dynamic coverage and makes static violation rates look broader than they are. It is specific, checkable and independent of any method ranking.

6. **The agenda is cost-ordered and concrete, and the closing contract is correct.** §6.1 (L205) proposes residual audits, test-power measurement and a dynamic panel in order of cost; §6.2 (L209) ends by describing the result as "a claim about the evidence, not about the quality of any method". The abstract's final sentence matches that contract.

7. **Writing and structure are serviceable.** The abstract is 182 words and answers the RQ; sections have clear functions; tables are informative rather than decorative. The revision required below is about accuracy, not about rewriting the prose.

---

## 3. Major Issues

### M1. The closing typology contradicts the evidence table.

**Location:** §6.2 (L209), with §§4.2–4.3 (L143–L161) and Table 3 (L123–L137).

**Problem:** "Parametric construction offers proof without audit, repair offers audit without proof, penalty methods offer neither, and generation-filtering offers either" cannot be reconciled with the report's own findings. (i) Repair is 3 proof / 4 test / 2 assumption (Table 3), and §4.2 describes three repair-family proofs — Sinkhorn convergence (L147), the interpolation construction (L147), the strict finite-grid form (L147) — so "without proof" is false for the family as coded. (ii) Penalty is six numerical tests that report adherence or residuals (L145) and "six rows report residuals" (L159), so "neither" is false if audit means numerical checking; it is true only if "audit" is silently narrowed to an independent finite-sample audit with a stated tolerance, a distinction the sentence does not make. (iii) Generation is 4 proof / 3 test / 1 assumption, which "either" flattens. The sentence then asserts "That division is the finding" (L209), so the contradiction is not local: it is the paper's conclusion that fails.

**Required change:** Either (a) make the tetrad precise and entailed by Table 3 — e.g., "proof without an independent residual audit" (parametric), "residual audit without a theorem" (penalty), "repair carrying both a theorem and post-hoc violation counts" (repair), "proof or sample acceptance depending on branch" (generation) — and add the per-cell counts; or (b) drop the tetrad and state the finding as the two asymmetries the evidence supports: proof-level and audit-level evidence come from nearly disjoint source sets (L159), and no row certifies dynamic consistency (L181). Do not replace the tetrad with a method ranking.

### M2. The dynamic-engagement count and its enumeration disagree.

**Location:** §4.5 (L181); Table 2 (dynamic row, "10"); Appendix C has no time-engagement field.

**Problem:** "Ten rows engage time at all:" is followed by exactly eight names — P8, R9, G1, G2, G3, C3, C2, C5. Phase 3's Theme 1 lists ten, adding G7 (Cohen et al., 2021) and R8 (Zetocha, 2023); both are described in the report itself as time-engaging: G7's "constrained state space in a neural SDE" (L149) and R8's "surface dynamics" (L147). The 0-of-41 conclusion survives either way, but the sentence that supports it does not: a reader who counts the names finds eight. Table 2 repeats "10" without a coded column, so the number cannot be audited from the ledger either.

**Required change:** List all ten rows (add Cohen et al., 2021; Zetocha, 2023) or justify the reduction explicitly and change Table 2 to eight; add a "time engagement" column to the Appendix C ledger so the count and the enumeration are the same object; add "as reported in the abstracts" to the abstract's "only ten engage time at all" (L17).

### M3. The abstract-level ledger does not reconcile.

**Location:** L10; §3.3 (L107); §5.3 (L199); Appendix C L311 (R2), L321 (G3), L328 (C2), L330 (C4), L332 (S1); L338 note.

**Problem:** Three different classifications coexist. §3.3 says "34 full abstracts, four partial ones and three metadata-only records". Appendix C marks five partial rows — R2, G3, C2, C4 and S1 — which implies 33 full + 5 partial + 3 metadata. §5.3 lists four partials (De March & Henry-Labordère; Cont & Vuletić; Niu; Fukasawa), omitting S1. Phase 2's partial set was R2, G3, C4 and S1 (phase2-verification.md L71) and did not include C2. So C2 (Niu, 2015) was reclassified from full to partial and S1 (Fengler, 2009) was dropped from the §5.3 list, with no stated reason. In addition, the front matter's "abstract-level for all 41 sources" (L10) is false for the three metadata-only rows, which the report itself says can be cited only at title level (L199). This matters beyond bookkeeping: partial status triggers the "cannot be graded above B" floor (phase2-verification.md L13), and C2 is the row the abstract cites for the dynamic finding (L17), so its read depth is material to the paper's second headline claim.

**Required change:** Adopt one classification and show it as a reconciliation table (41 = 33 full + 5 partial + 3 metadata, or 34 + 4 + 3 with C2 restored to full), state which is correct and why C2's status changed; correct §5.3's list; replace L10 with "38 abstracts (33 full, 5 partial) + 3 title/metadata records" using the reconciled numbers; make every downstream count (17/16/8; 0/30/11; family totals) derive from that table.

### M4. The abstract attributes the review's own coding results to single sources.

**Location:** Abstract (L17), three parenthetical citations.

**Problem:** "17 sources assert their guarantee at proof level, 16 report a numerical test, and 8 assert admissibility without either (Anagha, 2026)"; "only ten engage time at all, and none enforces or tests dynamic no-arbitrage (Niu, 2015)"; "no two studies share data, metric and tolerance, so zero rows are directly comparable (Xiong & Liu, 2026)". These are aggregate results of the report's own coding. As rendered, the citations imply that one row is the source of each count. That is not defensible: Niu (C2) is a review of dynamic conditions, not evidence that nothing in the corpus tests dynamic arbitrage; Xiong & Liu (R5) is one repair row, not the comparability coding; Anagha (G6) is one of the 17 proof rows. The in-text `<!--ref:...-->` markers look like automatic emission tags, but the abstract is read without them.

**Required change:** Remove the three parenthetical citations from the own-count sentences and point the reader to Table 2/Table 3 and Appendix C in the body; if exemplars are wanted, use "e.g." in the body, never in the abstract. The abstract's counts must be attributable to the report itself.

### M5. Two advertised analytical instruments are never delivered.

**Location:** §1.2 (L29, "Those questions become the coding instrument used in Section 4"); §1.3 (L37, "Each hypothesis is assessed explicitly in Section 4"); §3.5 (L115, coded triple = model class, enforcement operator, verification mode); Sections 4–6.

**Problem:** The hypotheses do not reappear after L37; there is no H1/H2/H3 adjudication anywhere in §§4–6. The evidence actually disconfirms parts of them, which makes the omission a suppression rather than a shortcut: H1's second clause says dynamic consistency is "asserted or tested rather than proved", while L181 says none even tests it — a half-disconfirmation the report never states; H2's first clause says penalty and repair methods "reduce fit error", while §4.3's one measured direction is that a tighter constraint buys fewer violations at a higher fit error (L161) — again, never stated. Separately, §1.2 promises the three questions (which condition / at what tolerance / verified how) as the coding instrument, but §3.5 codes model class, enforcement operator and verification mode. Tolerance is not a field in the ledger, and §4.6 complains that tolerances are "frequently unstated" (L185): the instrument cannot deliver what §1.2 promised. Phase 3 had a hypothesis-status table (phase3-synthesis.md L101–L103); the Phase 4 draft dropped it.

**Required change:** Add a compact hypothesis-status table (H1–H3, status, row anchors, one-line evidence) at the end of §4 or in §5.1, using Phase 3's adjudications and matching the report's evidence; state explicitly that H1's dynamic clause is disconfirmed and H2's fit-error clause is not supported. Either add condition-set and tolerance fields to the ledger (with "not stated" as a value) and report their distribution, or reword L29 to say the three questions "structure the analysis" (as they do at L195) rather than constitute the coding instrument.

### M6. The search flow does not close.

**Location:** §3.1 (L99); §3.2 (L103); Appendices A–B (L261–L288).

**Problem:** (i) "The 31 queries yielded 775 records" (L103) equals 31 × 25 exactly, yet L99 says one query "returned nothing after a transient rate-limit"; if that query is included in 775, then 775 is records *requested* and the number *returned* is 750. (ii) The snowballing pass "supplemented the queries" but is absent from the flow 775 → 430 → 389 → 41, and no yield is given, so a reader cannot tell whether it added records or was absorbed in de-duplication. (iii) "Two records were replaced during abstract reading" (L103) does not say from which pool or by what rule, so the 41 included records are not a clean subset of the 430. (iv) "between 2026-01-01 and 2026-11-23" (L99) reads as a search-execution window but sits next to corpus-window language; say which it is. None of this changes the synthesis, but it is exactly the accounting a review of this kind is selling.

**Required change:** Report returned vs requested (750 / 775); add the snowballing yield and the two replacement records to Appendix B with their source queries; separate the query-execution dates from the corpus window (2015 onward plus the five flagged baselines); end Appendix B with a closure check (41 + 389 = 430; 430 ≤ 750).

### M7. The report compares numbers across studies in three places, contrary to its own condition (iv).

**Location:** §3.3 (L107); §4.2 (L147); §4.3 (L161); condition (iv) at L107 ("violation, fit and hedging numbers may not be compared across studies"; cf. phase2-verification.md L7).

**Problem:** (a) "the penalty cluster disagrees on violation magnitudes" (L107) treats incomparable magnitudes as substantive disagreement; Phase 2's verification found them "not comparable" across different data, metrics and tolerances, not contradictory. (b) "consistent with the repair floors reported elsewhere (Xiong & Liu; Alvarez)" (L161) uses Xiong's residual butterfly floor and Alvarez's <1% static violation rate to corroborate Anagha's fit-error cost of tightening a structural constraint. These are different constructs, measured on different data with different tolerances; the report's own condition forbids the comparison, and an editor should not accept a corroboration that the protocol rules out. (c) L147 gives "a butterfly floor of about 5.4 percent" while the source attributes that floor to finite-precision rounding (phase2-bibliography.md L294; phase3-synthesis.md L37). Dropping the attribution turns a numerical artefact into a substantive repair cost and makes (b) look stronger than it is.

**Required change:** Delete the corroboration sentence or replace it with "the direction is observed once (Anagha) and is not corroborated elsewhere in the corpus"; restore the rounding attribution in §4.2; restate §3.3 as "the reported magnitudes are not comparable across rows (different panels, metrics and tolerances)". If the intended point is that the field lacks a common measurement, say that — it is stronger than a false comparison.

---

## 4. Minor Issues

1. **m1 — Corpus window (L8; title L1).** The front matter and title date the corpus "2015–2026", but Table 3 and Appendix C include five pre-2015 rows: S1 (Gatheral & Jacquier, 2013), S2 (Fengler, 2009), S3 (Hagan et al., 2014), S4 (Bodurtha & Jermakyan, 1999), S5 (Fengler et al., 2006). State "36 in-window studies + 5 flagged seminal baselines" in the front matter, or narrow the title and window claim.

2. **m2 — "Seven-dimension" versus eight (L70, L72, L199).** The §2.3 heading is "The Seven-Dimension Evaluation Matrix", the first body sentence says "Eight evaluation dimensions were declared", Table 2 has eight rows, and §5.3 repeats "the seven-dimension matrix". Rename the heading and L199 to eight, or restore the seven-dimension set and delete the extra row.

3. **m3 — Preprint recency count (L199).** "six of them from 2025–2026" cannot be right: of the 11 preprints (P7, P8, N3, N5, N6, R2, R6, R7, R8, G6, C2), only four are 2025–2026 (P8 2026, R6 2026, R7 2025, G6 2026); if 2023–2026 is intended, the count is seven. Recompute from the reference years.

4. **m4 — Double-coded loci (L68).** Table 1's note says "three studies are coded under two loci", but Appendix C assigns exactly one family per row and Table 3's family counts sum to 41. Change to "three studies sit between two loci; each is assigned one family in Appendix C".

5. **m5 — The Klassen necessity claim (L93).** "the only necessary-and-sufficient statement is a metadata-only preprint (Klassen, 2016)" sits two clauses after Martini and Mingone's "exact characterisation" of the butterfly requirement, which the bibliography describes as fully characterising the problem (P2). Qualify the claim (e.g., the only closed-form necessary-and-sufficient statement for SSVI/S3) or explain how the two results differ; do not let a title-level metadata row anchor a "only" claim.

6. **m6 — Duplicated and overstated assumption-row sentence (L121).** "The assumption rows cluster in exactly the families that also carry the metadata-only records" repeats the preceding sentence and overstates: assumption rows also occur in generation (G3), conditions (C2) and seminal baselines (S4, S5), none of which carries a metadata-only record. Delete the duplicate and replace "exactly" with "concentrate in".

7. **m7 — The second-branch sentence (L149).** "Only the second branch measures anything, and only on synthetic data" is falsified by its own paragraph: the denoiser "reports lower error and runtime" (G4), and the realism-driven models are judged on hedging behaviour (G2). G5's pass rate is on generated surfaces, not necessarily synthetic. Write: "Only the penalised-sampling branch audits arbitrage compliance, and only Anagha (2026) states the tolerance at which it does so (on synthetic SVI slices)."

8. **m8 — Unnamed "two rows" (L145).** "The two rows that report adherence do so without stating a tolerance" does not name them. Either name them (Wiedemann et al., 2025; Cao et al., 2020) or delete the sentence; as written it is uncheckable.

9. **m9 — Preprint flags are inconsistent at point of use (L141, L143, L147, L149).** Only N3 and R8 carry a `[preprint]` tag, although 11 rows are preprints and Phase 2's condition (ii) requires preprint status to be "labelled as such in every synthesis claim" (phase2-verification.md L7). The list at L141 is a global disclosure, not a point-of-use flag: claims drawn from P8, R7, G6 and others appear unqualified. Tag all 11 at first use, or add a status column and cite it.

10. **m10 — Incomplete rubric description (L111).** §3.4 lists the floors but omits "a partial abstract cannot be graded above B" (phase2-verification.md L13). Without that floor the reported A/B/C distribution (11/13/17) is not reproducible from the stated rules; add it and show which rows it binds.

11. **m11 — Reference year/volume/DOI mismatches (L228, L233, L235, L251).** Cohen et al. (2021) is given volume 30(1) (2023) with a 2023 DOI; Fengler et al. (2006) is given JFE 5(2) with a 2007-issue DOI (`nbm005`); Gatheral & Jacquier (2013) is given Quantitative Finance 14(1) (2014); Vuletić & Cont (2024) is given a 2025 DOI. Align in-text and list years with the version of record (APA 7), or add online-first notes consistently, and update the in-text citations that depend on the changed years.

12. **m12 — AI-disclosure overstatement (L213).** "All findings were verified against cited sources" cannot be squared with L199 ("no theorem was checked, no residual was recomputed") or with the declared abstract-only scope. Write: "Every claim was checked against the retrieved abstract or metadata record; no full text was consulted." (This review takes no position on disclosure compliance itself.)

13. **m13 — "Solved" (L191).** "the field has solved it in four distinct ways" overclaims under an abstract-only read and is immediately qualified two sentences later. Use "has established static admissibility in four distinct ways within the reviewed families".

14. **m14 — Untraceable negative claim (L185).** "No row in the corpus fixes more than two" of the four comparability fields cannot be checked: Appendix C has no columns for panel, condition set with tolerance, metric/aggregation, or residual-reporting format. Add a small coding table for the four fields, or soften to "few rows fix more than two, and none fixes all four" with examples.

15. **m15 — Three kinds for four families (L55).** §2.2 says "a theorem, an optimisation residual and an acceptance test are the best each family can produce", while §1.2 (L29) correctly lists four kinds: theorem, optimisation residual, repaired point, accepted sample. Repair produces theorems (R2, R3, R6), so the three-kind list is both arithmetically and factually short. Use the four-kind list.

16. **m16 — Planned reliability procedure not reported as a deviation (L115, L199).** Phase 1 planned the coding scheme "applied twice to a calibration subset; disagreements adjudicated ... counts reported" (phase1-scoping.md, validity plan). The report discloses single-analyst coding but never says the calibration was not performed. Add one sentence: the planned second coding was not executed; consequently no agreement statistic is available and construct-level judgements are single-coded.

17. **m17 — "The cost of doing so" (L175).** In "Enlarging the admissible set is ... demonstrated in two constructions (Zaugg; Alvarez), but the cost of doing so is measured in one row only", "doing so" is enlarging, but the one measurement is G6's cost of *tightening* (as §4.3/L161 says), and R5 reports a residual floor, not the cost of added flexibility. Rewrite: "…demonstrated in two constructions; neither measures the cost of the added flexibility, and the cost of tightening is measured once (Anagha)."

18. **m18 — Abstract vocabulary (L17).** "certified object" and "audit-level" have no counterpart in the body, which uses "numerical test" and "reports" (L115, Table 3). Use the body's terms in the abstract or define these terms in §1.2.

19. **m19 — "Uniformly structural" (L143).** "Six of the eight parametric rows are proof-level, and the guarantee is uniformly structural: the parameter map is chosen so that the admissible set is the image of the parameter domain" — the same sentence then cites Barski and Wiśniewolski, who derive explicit arbitrage probabilities for Gaussian factor models, not a parameter-map guarantee. Change to "typically structural" and state the exception.

---

## 5. Line Feedback

| # | Anchor | Quote (snippet) | Issue | Suggested fix |
|---:|---|---|---|---|
| 1 | L8 (and L1) | "41 sources ... 2015–2026" | Five pre-2015 baselines (S1–S5) are counted in the 41 | "36 in-window studies + 5 flagged seminal baselines" or narrow the title |
| 2 | L10 | "abstract-level for all 41 sources" | False for the three metadata-only rows, which are title-level only (L199) | "38 abstracts (33 full, 5 partial) + 3 title/metadata records" — after reconciliation |
| 3 | L17 | "(Anagha, 2026)" after "17 ... 16 ... 8" | Aggregate coding result attributed to a single row | Delete the parenthetical; cite Table 3 / Appendix C in the body |
| 4 | L17 | "only ten engage time at all" | §4.5 (L181) enumerates eight; Table 2 repeats ten | One list and one count; add the missing rows or change both numbers |
| 5 | L17 | "Proof-level and audit-level evidence" | "audit-level" is undefined and not used in the body | Use "numerical test"/"reports", or define the term in §1.2 |
| 6 | L29 | "Those questions become the coding instrument used in Section 4" | Tolerance and condition identity are never coded (L115 codes model class, enforcement operator, verification mode) | Add the fields to the ledger or reword to "structure the analysis" |
| 7 | L37 | "Each hypothesis is assessed explicitly in Section 4" | No H1/H2/H3 adjudication appears anywhere in §§4–6 | Add a hypothesis-status table; state the H1 dynamic and H2 fit-error disconfirmations |
| 8 | L55 | "a theorem, an optimisation residual and an acceptance test" | Three kinds for four families; repair produces theorems (§4.2) | Use the four-kind list from L29 |
| 9 | L68 | "three studies are coded under two loci" | Appendix C assigns one family per row; Table 3 totals sum to 41 | "sit between two loci; each is assigned one family" |
| 10 | L93 | "the only necessary-and-sufficient statement is a metadata-only preprint" | Tension with the adjacent "exact characterisation" (Martini & Mingone) | Qualify the claim to the SSVI/S3 closed-form statement |
| 11 | L103 | "The 31 queries yielded 775 records" | One query returned nothing; 775 = 31 × 25 = requested, not returned (returned = 750) | "750 returned of 775 requested"; close the flow in Appendix B |
| 12 | L107 | "the penalty cluster disagrees on violation magnitudes" | Condition (iv) forbids the comparison; incomparability is not disagreement | "magnitudes are not comparable across rows (panels, metrics, tolerances)" |
| 13 | L121 | "cluster in exactly the families that also carry the metadata-only records" | Duplicates the preceding sentence and overstates (G3, C2, S4, S5 are assumption rows without metadata-only) | Delete the duplicate; "concentrate in" |
| 14 | L141 | "Eleven of the rows are preprints" | Only N3 and R8 are tagged `[preprint]`; condition (ii) requires point-of-use labelling | Tag all 11, or add a status column cited at each claim |
| 15 | L145 | "The two rows that report adherence" | The two rows are never named | Name Cao et al. and Wiedemann et al., or delete the sentence |
| 16 | L147 | "a butterfly floor of about 5.4 percent" | The source attributes this floor to finite-precision rounding | Restore the attribution |
| 17 | L149 | "Only the second branch measures anything" | False in its own paragraph: G4 reports error/runtime, G2 hedging; G5 is on generated surfaces | "Only the penalised-sampling branch audits compliance; only Anagha states a tolerance" |
| 18 | L161 | "consistent with the repair floors reported elsewhere" | Corroborates a fit-error cost with violation floors from different data and tolerances | Delete the corroboration; it is a one-row observation |
| 19 | L175 | "the cost of doing so is measured in one row only" | The cited rows measure the cost of tightening (G6) or a residual floor (R5), not the cost of enlarging | Rewrite the antecedent; separate tightening cost from flexibility benefit |
| 20 | L181 | "Ten rows engage time at all:" then eight names | Missing G7 (Cohen et al., 2021) and R8 (Zetocha, 2023) | Add both, or justify the reduction and change Table 2 |
| 21 | L185 | "No row in the corpus fixes more than two" | No ledger field records the four comparability fields | Add the four-field coding appendix or soften with examples |
| 22 | L199 | "four abstracts are partial (…)" | Ledger marks five partial (adds S1, L332); Phase 2's set was R2/G3/C4/S1 | One classification and one list, consistent with Appendix C |
| 23 | L199 | "six of them from 2025–2026" | Only four preprints are 2025–2026 (P8, R6, R7, G6) | Recompute (four; or seven for 2023–2026) |
| 24 | L199 | "the seven-dimension matrix" | Table 2 has eight dimensions | "eight-dimension matrix" |
| 25 | L209 | "repair offers audit without proof, penalty methods offer neither" | Repair has 3 proof rows; penalty rows report residuals (L145, L159) | Qualify "independent audit" and derive each claim from Table 3, or drop the tetrad |
| 26 | L213 | "All findings were verified against cited sources" | Contradicts L199 ("no theorem was checked, no residual was recomputed") | Narrow to the abstract/metadata-level verification actually performed |
| 27 | L228, L233, L235, L251 | Cohen 2021 / 30(1) 2023; Fengler 2006 / 5(2); Gatheral 2013 / 14(1); Vuletić 2024 / 2025 DOI | APA year does not match volume/DOI year | Align to the version of record or add online-first notes; update in-text years |

---

## 6. What Would Change My Verdict

**To MINOR REVISION.** All seven majors corrected as specified, with a reconciliation table showing that every body count derives from Appendix C, and no new inconsistency introduced. Concretely: (i) the ledger reconciles 41 = full + partial + metadata, and L10, §3.3, §5.3 and the front matter use that split; (ii) §4.5 lists the ten coded rows (or eight with a stated rule) and Table 2 agrees; (iii) §6.2's typology is either entailed by Table 3 with per-cell counts or replaced by the two asymmetries; (iv) the abstract's own-count sentences carry no single-source citations; (v) a hypothesis-status table states H1's dynamic clause as disconfirmed and H2's fit-error clause as unsupported; (vi) Appendix B reports 750/775, the snowballing yield and the two replacements, and closes arithmetically; (vii) §4.3's cross-study corroboration is removed and the 5.4% rounding attribution restored. If the fixes stay inside these locations and the numbers close, the study's substance can stand.

**To ACCEPT.** On top of the above: (a) an independent second coder on a 10–15-row calibration subset with a reported agreement statistic (or at least a documented adjudication log), because the paper is a coding exercise and single coding is its largest structural limitation; (b) a full-text check of the five load-bearing rows — G6 (Anagha), R5 (Xiong & Liu), P2 (Martini & Mingone), G2 (Vuletić & Cont), G7 (Cohen et al., 2021) — confirming that the abstract-level readings hold; the report itself names this as the highest-value next step, and it would lift the central absence claims from "what abstracts report" to "what the corpus shows"; (c) point-of-use status flags for preprints and partials; (d) reference metadata aligned with the version of record. ACCEPT does not require expanding the corpus, adding full-text coding of all 41 rows, or adding a method ranking.

**To REJECT (downgrade).** If the body counts cannot be reproduced from Appendix C and the search artefacts — i.e., if the errors prove not to be bookkeeping but evidence that the numbers were never derived from the recorded ledger — then the review's core value proposition (auditability) fails and no revision can repair it. A second downgrade path: if, after adding G7 and R8 and correcting the ledger, the proof/audit asymmetry no longer holds across families, the paper's central finding is gone and it needs re-framing, not revision. A third: if the 5.4% figure cannot be corrected without collapsing §4.3, the cost claim must be withdrawn; a withdrawn claim is acceptable, an unsupported one is not.

**What would not move me.** Adding a ranking of construction methods, expanding to a full PRISMA systematic review, or adding citation counts. The first exceeds the stated scope and would damage the coherence that is already the weakest dimension; the second and third are different papers. A revision that "fixes" the typology by asserting a winner has misread this report's contribution.

---

## 7. Closing Note

On resubmission, the report should be accompanied by a one-page reconciliation memo listing every count in the front matter, abstract, §§3–6 and Appendices A–C, with its source rows — the 17/16/8 split by family, the 0/30/11 comparability split, the 33+5+3 or 34+4+3 read-status split, and the 750/775 retrieval split. I will check that memo first, because the report's distinctive claim is not that it has the right answer about implied-volatility surfaces but that it can show its work. At present it can show most of it; the revision needs to show all of it.

*Review boundary: this review assesses the manuscript only. It does not adjudicate research-ethics or disclosure compliance (a separate lane), does not re-run the searches, and does not re-code the corpus. Upstream phase artefacts were consulted only to test whether the report's statements about its own evidence are consistent.*
