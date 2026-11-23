# Phase 6 Revision Log — Response to Editorial, Ethics and Devil's Advocate Reviews

**Run:** ARS v3.24.4 end-to-end validation, Stage 1 (`deep-research`, `full` mode), example `iv-surface-review-v047`
**Revised document:** `phase6-final.md` (5,596 body words by the stated convention; 41 references; Abstract → Responsible Use Statement, excluding headings, citation-emission markers, references and appendices)
**Inputs reviewed:** `phase4-report.md`; `phase5-editorial.md` (MAJOR REVISION: 7 major / 19 minor / 27 line rows); `phase5-ethics.md` (CONDITIONAL: C1–C7); `phase5-da-checkpoint3.md` (REVISE: 0 critical / 7 major / 10 minor). Canonical records consulted for every factual change: `phase2-bibliography.md`, `phase2-verification.md`, `phase3-synthesis.md`, `search/selected_sources.json`, `search/screening_log.json`, `search/openalex_candidates.json`.
**Loop:** revision loop 1 of the maximum 2 permitted by SKILL.md Phase 6. Nothing outside `phase6-final.md` and this log was modified.

## 1. Disposition Summary

| Source | Items | Fixed | Partly fixed | Pushed back |
|---|---:|---:|---:|---:|
| Editorial — majors (M1–M7) | 7 | 7 | 0 | 0 |
| Editorial — minors (m1–m19) | 19 | 18 | 1 (m14) | 0 |
| Editorial — line-feedback rows | 27 | 26 | 1 | 0 |
| Ethics — conditions (C1–C7) | 7 | 7 | 0 | 0 |
| Ethics — advisory (A1–A5) | 5 | 4 | 0 | 1 (A5) |
| Devil's advocate — majors (M1–M7) | 7 | 7 | 0 | 0 |
| Devil's advocate — minors (m1–m10) | 10 | 7 | 3 (m8, m9, m10) | 0 |
| **Total (excluding the 27 line rows, which restate M/m items)** | **55** | **50** | **4** | **1** |

No finding was silently ignored. The one pushback (ethics A5) is recorded with evidence in §6; the four partial dispositions are explained per item below. Table numbering in `phase6-final.md` differs from `phase4-report.md` because the hypothesis-status adjudication demanded by editorial M5 and DA M3 became a new **Table 1**; the former Tables 1–3 are now **Tables 2–4**. Locations below use the revised numbering.

## 2. Editorial Majors (7/7 fixed)

| ID | Severity | Decision | Location in `phase6-final.md` | Evidence / change |
|---|---|---|---|---|
| M1 — §6.2 typology contradicts the evidence table (repair does report proofs; penalty does report tests) | Major | Fixed | §6.2, L222–224 | Tetrad removed. §6.2 now gives per-family counts (parametric 6 proof of 8 and 0 audits; penalty 0 proof / 6 tests; repair 3 proof / 4 tests, "they simply come from different rows"; generation 4 proof / 3 tests / 1 assertion) and defines "audit" as a reported residual or violation check on the method's own output. Counts match Table 4 row-for-row. |
| M2 — "ten rows engage time at all" then names eight; count unsupported | Major | Fixed | §4.5, L194–196; Table 3 row "Dynamic consistency"; Appendix C "Time" column | All ten named: P8, R9, G1, G2, G3, G7, R8, C2, C3, C5 — the Phase 3 set (`phase3-synthesis.md` L71), which adds G7 and R8 to the eight the draft listed. Appendix C now marks exactly those ten rows "T" (C5 "T†"), so the claim is checkable from the ledger. |
| M3 — read-status ledger inconsistent (§3.3 34/4/3; Appendix C 33/5/3; §5.3 four partials omitting S1; front matter "all 41 at abstract level") | Major | Fixed | Front matter L10; §3.3 L122; §5.3 L214; Appendix C note L363 | Canonical Phase 2 ledger adopted everywhere: 34 full / 4 partial (R2, G3, C4, S1) / 3 metadata-only (P4, P7, R4). Appendix C C2 changed from Partial to **Full** (its abstract is full — `phase2-verification.md` L71, `phase2-bibliography.md` L453–460). Appendix C note now states the reconciliation explicitly; §5.3 names R2, G3, C4, S1 and adds that Niu (2015) supplied a full abstract that a short snippet made look partial. |
| M4 — abstract attributes the review's own aggregate counts to individual sources | Major | Fixed | Abstract L18 | The parentheticals to Anagha, Niu and Xiong & Liu are gone. The abstract reports 17/16/8 and 0 of 36 (0 of 31) as "Coding of an evidence matrix (Table 4; Appendix C)", and comparability as judged "from the abstracts". No source is credited with an aggregate it did not report. |
| M5 — two advertised instruments never delivered (H1–H3 not adjudicated; three-question instrument ≠ coding triple; no tolerance field) | Major | Fixed | New Table 1, L40–52; §1.2 L30; §1.3 L34–38; §3.5 L128–130 | Table 1 records H1 (static clause supported; dynamic clause disconfirmed as stated — "absent, not asserted-and-tested"), H2 (fit-error clause unsupported; burden-displacement clause supported) and H3 (supported for the penalised-sampling branch, disconfirmed for the inherited-guarantee branch), following the Phase 3 adjudications (`phase3-synthesis.md` L97–103). §1.2 now says the three questions "structure the analysis" while condition and tolerance are annotations; §3.5 states which fields the ledger does and does not code. |
| M6 — search flow does not close (775 vs 750; snowballing yield absent; replacements unsourced; dates ambiguous) | Major | Fixed | §3.1 L114; §3.2 L118; Appendix A note L299; Appendix B note | Reported honestly: 31 queries submitted on 2026-11-23, each requesting 25 (775 requested); first pass hit HTTP 429 on 21 queries, retry recovered 20, one string ("SVI stochastic volatility inspired") remained unusable → **750 returned**. Deduplication removed 320, leaving 430; title screening excluded 389 under eight codes (now listed in Appendix B), leaving 41; "430 − 389 = 41". One snowballing pass added no record that survived screening, and all 41 included rows have at least one direct query hit. Replacements named: Wiedemann et al. (2025) for a neural-network pricing paper; Fukasawa (2022) for an FX delta-condition paper. Query date and corpus window (2015-01-01 to 2026-11-23) are now separate statements. |
| M7 — three cross-study comparisons contrary to verification condition (iv) | Major | Fixed | §3.3 L122 (condition iv); §4.2 repair L162; §4.3 L176; §4.4 L190 | (a) "penalty cluster disagrees on violation magnitudes" is gone; the cluster is described as not comparable instead. (b) The §4.3 corroboration of the Anagha fit-cost result via Xiong & Liu and Alvarez is removed and replaced by an explicit non-corroboration statement ("observed once, on synthetic data … their magnitudes are not comparable with a fit-error change"). (c) The finite-precision-rounding attribution for the 5.4 percent Xiong & Liu floor is restored, with the reported scale (252 out-of-sample SPX days). |

## 3. Editorial Minors (18 fixed, 1 partly fixed)

| ID | Decision | Location | Change |
|---|---|---|---|
| m1 five pre-2015 rows inside a "2015–2026" corpus | Fixed | Front matter L8; §3.1 L114; Appendix B | Corpus stated as 36 in-window + 5 declared precursors (1999–2014) "never counted as window hits"; the precursor status is repeated wherever totals appear. |
| m2 seven- vs eight-dimension matrix | Fixed | §2.3 L85; §5.3; §3.5 | Heading, body and cross-references all "eight"; the eight dimensions are those in Table 3. |
| m3 "six preprints from 2025–2026" | Fixed | §5.3 L214 | Corrected to four (Alvarez 2025; Anagha 2026; Barski & Wiśniewolski 2026; Buehler et al. 2026), verified against the 11-preprint set in `phase2-verification.md`. |
| m4 "three studies coded under two loci" vs one family each in Appendix C | Fixed | §2.2 L70; Table 2 note L83 | Restated as an analytical note: Buehler et al. (2026), Bender & Thiel (2020) and Cao et al. (2020) sit between two loci but "each is assigned one family in Appendix C". |
| m5 Klassen necessity claim | Fixed | §2.4 L108 | Qualified: the only closed-form necessary-and-sufficient statement **for the SSVI/S3 curve** found in this corpus; states that the exact characterisation of Martini & Mingone (2022) is a statement about the SVI family, not a necessity claim for the wider class. |
| m6 duplicated assumption-row sentence and "concentrate in" | Fixed | §4.1 L136 | Duplicate deleted; the surviving sentence says assumption rows "include all three metadata-only records and two pre-constraint baselines". |
| m7 "Only the second branch measures anything" | Fixed | §4.2 generation L164 | Replaced: "Only the penalised-sampling branch audits arbitrage compliance, and only Anagha states a tolerance and reports the fit cost", with G4 (error/runtime) and G2 (hedging) mentioned separately. |
| m8 unnamed "two rows that report adherence" | Fixed | §4.2 penalty L160 | Named: Cao et al. (2020) and Wiedemann et al. (2025); the sentence adds that neither states a tolerance, so their audits are hard to reproduce. |
| m9 preprint flags inconsistent at point of use | Fixed | §2.1 L66; §2.2 L70; §3.3 L122; §4.2 L156–164; §5.3 L214 | A convention sentence in §3.3 defines `[preprint]` and `[title/metadata only]`; tags added at first body use for G6, C2, R6, P7, P8, N5, N6, R2, R7, R8. |
| m10 missing floor: partial abstract cannot exceed B | Fixed | §3.4 L126 | Floor added and its effect stated: it binds C4 and S1, both graded B. |
| m11 reference metadata mismatches | Fixed | References, L238–282 | Online-first issue years marked in brackets for Cohen et al. (2021→2023), Fengler et al. (2006→2007), Gatheral & Jacquier (2013→2014) and Vuletić & Cont (2024→2025), with a note on versions; 41 entries retained. |
| m12 AI-disclosure overstatement | Fixed | AI Disclosure L228 | Rewritten (see ethics C1): no "all findings were verified", no "human oversight throughout". |
| m13 "solved" → "established" | Fixed | §5.1 L206 | "Static admissibility is … established by the four families in four ways"; the epistemic ceiling is stated rather than claimed away. |
| m14 "No row fixes more than two" comparability fields untraceable | **Partly fixed** | §4.6 L200 | Softened to "No row shows more than two of the four in its abstract", which is verifiable from the abstracts; a per-row four-field table was not added because it would require reconstruction the abstract-level read cannot support. The four fields themselves are defined in the same paragraph. |
| m15 three kinds listed for four families | Fixed | §2.2 L70 | The four-kind list (theorem, optimisation residual, repaired point, accepted sample) now matches four families. |
| m16 planned calibration-subset double coding not reported as deviation | Fixed | §5.3 L214 | Recorded as an unexecuted deviation, together with the unexecuted full-text retrieval of G6, R5, P2, G2 and G7 recommended at the Phase 3 checkpoint. |
| m17 "cost of doing so" antecedent | Fixed | §4.4 L190 | "but the cost of enlarging it is measured in one row only" — the antecedent is now the enlargement of the admissible set. |
| m18 "certified object"/"audit-level" undefined | Fixed | §1.2 L30; §6.2 L224 | §1.2 defines *audit*, *dynamic* and *certified object*; §6.2 defines "audit" again at the point where the term carries the argument. |
| m19 "uniformly structural" false for Barski & Wiśniewolski | Fixed | §4.2 parametric L158 | "typically structural", with the explicit arbitrage-probability derivation noted as the exception. |

Line-feedback table: all 27 rows are restatements or instances of the items above; 26 are resolved by the corresponding fix and 1 (the comparability-field row) by m14's partial fix. The editor's rejection triggers were checked: every count in the body is reproducible from Appendix C; the proof/audit asymmetry is retained (and is now stated with per-cell counts rather than as a slogan); and the 5.4 percent figure is corrected to its reported scale with the rounding attribution restored.

## 4. Ethics Conditions (7/7 fixed)

| ID | Severity | Decision | Location | Change |
|---|---|---|---|---|
| C1 — AI disclosure must name stages, model and limit of verification; remove overclaims | Condition (required) | Fixed | AI Disclosure L228 | Replaced with the bounded paragraph supplied at `phase5-ethics.md:221`: ARS v3.24.4, 31 OpenAlex queries, 750 returned of 775 requested, 41 included, 34 full / 4 partial / 3 metadata-only, coding and A/B/C grading, synthesis and drafting; model recorded as "a Claude-family agent operating within DeepSeek Harness (DSH), on 2026-11-23; the exact model identifier and version were not recorded in the run log"; verification limited to 41/41 DOI resolution with no retractions, no theorem checked and no number recomputed; single-analyst screening and coding; human role limited to run authorization and Phase 1–4 checkpoint review, with no claim-level verification recorded; explicit list of AI limitations. "All findings were verified" and "Human oversight was applied throughout" are gone. |
| C2 — do not attribute the report's own counts to sources | Condition (required) | Fixed | Abstract L18; §4.1 L136; §3.4 L126 | Counts attributed to this review's coding of the 41-row ledger (Table 4; Appendix C); sources are cited only for what they report. |
| C3 — "explicitly declines" overstates Cohen et al. (2021) | Condition (required) | Fixed | §2.1 L66; §4.4 L184 | The abstract gives a static, model-independent linear-inequality guarantee and states no dynamic claim; the text now says the review codes it as making none rather than quoting a decline. |
| C4 — truncated quotation from Sidogi et al. (2022) | Condition (required) | Fixed | §4.2 penalty L160 | Quotation restored as "cannot directly learn the static arbitrage condition" (matches `phase2-bibliography.md` L205–219). |
| C5 — preprint/metadata-only tags at point of use (Phase 2 condition ii) | Condition (required) | Fixed | §2.1, §2.2, §3.3, §4.2, §5.3; Appendix C | Tags added at first body use for G6, C2, R6, P7, P8, N5, N6, R2, R7, R8; `[title/metadata only]` on P4, P7, R4 where used. The abstract no longer makes source-specific claims, so no abstract tag is needed; §3.3 states the convention. |
| C6 — author competing interests and funding | Condition (required) | Fixed | Front matter L11; §Competing Interests and Funding L230–232 | "None declared … no external funding was received", with AI assistance disclosed and cross-referenced. |
| C7 — single-stock C5 scope contradiction | Condition (required) | Fixed | §3.1 L114; §4.5 L196; Appendix C L363 | Exclusion is now stated as "from scope-focused selection, with one disclosed exception"; C5 is retained with a scope flag at every use and marked "T†" in Appendix C. |

Advisory items: A1 (seven/eight-dimension) fixed at L85; A2 (Bodurtha "not admissible in any stated sense") fixed in §2.4 — "stated no admissibility condition"; A3 covered by the C1 rewrite; A4 (dual-use) fixed by the new Responsible Use Statement (L234–236: Level None, no code, data or implementable procedure, no deployment ranking, not advice). **A5 pushed back — see §6.**

## 5. Devil's Advocate (7/7 majors fixed; 7 minors fixed, 3 partly fixed)

| ID | Severity | Decision | Location | Change |
|---|---|---|---|---|
| M1 — corpus composition (pre-2015 rows inside the window; single-stock C5) | Major | Fixed | Front matter L8; §3.1 L114; §4.1 L136; §4.5 L196 | Corpus stated as 41 = 36 in-window + 5 seminal precursors; in-window subtotal 16/14/6, construction subtotal 13/13/5; dynamic count given as 0 of 41 as reported, 0 of 36 in-window, 0 of 31 construction rows; C5 disclosed and flagged. |
| M2 — zero counts presented as study facts rather than abstraction results | Major | Fixed | Abstract L18; §3.3 L122; §4.5 L196; §6.2 L224 | "As reported in the abstracts" added at every zero-count claim; §3.3 states that 38 of 41 rows are abstract-assessable and three are metadata-only; "the literature" replaced by "this corpus". |
| M3 — dynamic-gap claim not auditable | Major | Fixed | §4.5 L196; Table 1; Appendix C note | The ten rows are named and individually characterised; the partial-abstract set is canonical; Niu (2015) is recorded as a full abstract and as the one level-VII review; Cohen (2021) is coded as making no dynamic claim; Table 1 records H1's dynamic clause as disconfirmed as stated. |
| M4 — closing typology contradicts Table 3 | Major | Fixed | §6.2 L222–224 | Per-family counts replace the slogan; "audit" defined; the two asymmetries (proof vs audit source disjointness; no row pairing a static theorem with a dynamic test) are stated as the finding. |
| M5 — AI disclosure overstates verification | Major | Fixed | AI Disclosure L228 | Same rewrite as C1. |
| M6 — uncited harm premise; benign alternative ignored; policy recommendation outruns evidence | Major | Fixed | §1.1 L26; §5.1 L206; §5.2 L210 | Harm propagation labelled a premise ("no study in this corpus tests it"); the retrieval-effect reading is stated as equally consistent; the journal suggestion is narrowed and explicitly not supported by evidence that it would improve practice. |
| M7 — abstract attributes own counts to single sources | Major | Fixed | Abstract L18 | Same fix as editorial M4. |

| Minor | Decision | Location | Note |
|---|---|---|---|
| m1 seven/eight-dimension heading | Fixed | §2.3 L85 | Heading and text agree. |
| m2 775 requested vs 750 retrieved | Fixed | §3.1 L114; §3.2 L118; Appendix A note L299 | Both numbers reported with the retry history. |
| m3 generation branches misdescribed | Fixed | §4.2 L164 | G5's 90.8 percent pass rate, G2's hedging results and G4's error/runtime comparison are each described as what they are. |
| m4 "5.4 percent" without unit or denominator | Fixed | §4.2 L162 | "about 5.4 percent on the reported scale—252 out-of-sample SPX days". |
| m5 "six preprints 2025–2026" and "twelve rows with known provenance" | Fixed | §5.3 L214 | Four preprints named; the provenance count is de-numbered because the underlying field is not tabulated. |
| m6 unexecuted double coding and full-text retrieval not flagged | Fixed | §5.3 L214 | Both recorded as deviations. |
| m7 A/B/C grades reported but unused | Fixed | §3.4 L126 | Grades are explained as quality labels (A/B/C) distinct from evidence status (proof/test/assumption) and are not used as a ranking. |
| m8 Appendix C lacks comparability code and (M, E, V) triple | **Partly fixed** | Appendix C note L363 | The ledger carries ID, family, evidence status, abstract status, level, time engagement, peer review and scope flag; comparability and the triple are stated to be read off the design-level coding rather than stored per row. Adding both as columns would require a 41-row re-coding not supported at abstract level; the note makes the derivation explicit instead. |
| m9 taxonomy may be partly constitutive; no falsification condition | **Partly fixed** | §2.2 L70; §2.2 note L83; §5.3 L214 | Boundary cases are disclosed (three rows between loci), the taxonomy is stated as provisional and unvalidated in §5.3, and each row is force-assigned to one family. An explicit falsification clause was not added; the adequacy condition is left implicit in the assignment rule. |
| m10 hybrid evidence-status precedence rule implicit | **Partly fixed** | §3.4 L126; Table 4 note L152 | State: the label records what the abstract reports, and a row that both proves and audits keeps the higher status (G6 is coded proof while its audit is described in the text). A per-row precedence rule was not tabulated. |

## 6. Pushback (1)

**Ethics A5 — "the preprint cap of C for quality grades conflicts with proof-level status, inverting the evidence hierarchy."** Not accepted as stated. The A/B/C scale grades *quality of the record as evidence for this review* (six criteria: design, data, validation, reporting, provenance, reproducibility), while the proof/test/assumption label records *what the source reports*. Phase 2 fixes these as separate axes with explicit floors (`phase2-verification.md` L13, L88): "a numerical test cannot receive A; … a preprint … cannot exceed C". A preprint can therefore legitimately report a proof and still be graded C; the report says exactly this in §3.4 ("the preprint cap explains the C grades of …") and Appendix C shows P8 as "Proof … C". Collapsing the two axes to remove the apparent inversion would itself violate verification condition (ii), which requires preprint status to be flagged wherever a claim draws on it. The revised text therefore keeps both axes and states their independence explicitly; no change was made to the grading rule.

## 7. Verification Performed on the Revised Report

| Check | Result |
|---|---|
| Body word count (Abstract → Responsible Use Statement; headings, citation markers, references and appendices excluded) | 5,596 words, inside the 5,200–5,600 target. `phase4-report.md`'s own 5,247 does not reproduce under the same metric (measures 5,213); the revised count is reported fresh rather than carried forward. |
| References | 41 entries (Ackerer … Yao), unchanged in count; four online-first years marked in brackets with a note on versions. |
| Read-status reconciliation | 34 + 4 + 3 = 41 in §3.3, Appendix C note and front matter; partial set R2, G3, C4, S1; metadata-only P4, P7, R4. |
| Evidence-status reconciliation | 17 + 16 + 8 = 41; in-window 16 + 14 + 6 = 36; baselines 1 + 2 + 2 = 5; Table 4 row subtotals match. |
| Retrieval arithmetic | 30 queries × 25 = 750 returned of 775 requested; 750 − 320 = 430; 430 − 389 = 41; ten time-engagement rows marked in Appendix C. |
| Stale strings | No occurrences of "seven-dimension", "31 queries yielded 775", "explicitly declines", "All findings were verified", "Human oversight … throughout", "six [preprints] from 2025–2026", "no row fixes more than two", "PRISMA compliance is claimed", "excluded by design". |
| Prohibited claims | No ranking of methods; no PRISMA/PRISMA-ScR compliance claim; no new references. |

## 8. Residual Acknowledged Limitations (not fixed, and why)

These remain true of the Stage 1 report and are stated in it (§5.3 and the AI Disclosure) rather than repaired:

1. **No full text, proof or code was read.** The read scope is abstracts; no theorem was checked and no reported number recomputed. Full-text retrieval of G6, R5, P2, G2 and G7 was recommended at the Phase 3 checkpoint and is recorded as an unexecuted deviation. It is out of Phase 6's authority (it would require a new Phase 3 loop).
2. **Single-analyst screening and coding.** No second coder, adjudication or kappa; the same analyst wrote the synthesis. A second coder on 10–15 rows is the editor's ACCEPT-level condition and cannot be retrofitted honestly at this stage.
3. **No PRISMA conformity and no PRISMA flow diagram.** The report claims none; the flow is documented in Appendices A and B instead.
4. **Unvalidated instruments.** The four-family taxonomy, the eight-dimension matrix and the A/B/C rubric are proposed and applied but not validated; calibration of the rubric against external raters is future work.
5. **40 discretionary exclusions** ("relevant but not selected") are the largest judgement call in screening and remain visible rather than audited.
6. **Coverage limits.** One discovery query failed after retry; the pool is not exhaustive. Three rows are metadata-only and three source abstracts are partial-plus. English-only, single-index (OpenAlex) retrieval and US-dominated data bound generality; provenance is not quantified per row.
7. **Derived, not stored, coding.** Comparability codes and the (M, E, V) triple are read off the family and evidence-status columns rather than tabulated per row (DA m8); the precedence rule for hybrid rows stays implicit (DA m10); the taxonomy has no explicit falsification clause (DA m9).
8. **No ranking or effect sizes by design.** The report deliberately stops at a diagnostic and an agenda; it does not estimate family performance differences, and the corpus does not support doing so.

Two cross-cutting conclusions of the reviews are accepted as correct and are now part of the report: the proof/audit asymmetry is real but must be stated as per-cell counts rather than as a slogan, and no row in this corpus converts an engagement with time into a dynamic guarantee or test.

---

*Revision produced 2026-11-23 under the ARS v3.24.4 Phase 6 protocol; AI-assisted, as disclosed in the report.*
