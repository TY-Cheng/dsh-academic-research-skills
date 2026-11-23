# Phase 5 — Research-Integrity and Ethics Review

**Artifact under review:** `phase4-report.md` — "Enforcing No-Arbitrage in Equity-Index Implied Volatility Surfaces: A Structured Review of Four Method Families, 2015–2026" (TY-Cheng, Independent researcher, 2026-11-23; 5,247 words; 41 sources).
**Run:** `examples/dsh/iv-surface-review-v047/`, Stage 1, Phase 5 — ARS v3.24.4 end-to-end validation run (repo commit `19f11de` per `run-log.md:4`).
**Reviewer:** the vendored `ethics_review_agent` role (v3.24.4), executed as an AI agent. The installed desktop plugin (0.4.6) was **not** used; only vendored v3.24.4 agent and checklist text was applied.
**Inputs read:** `phase1-scoping.md`, `phase2-verification.md`, `phase3-synthesis.md`, `phase4-report.md`, `run-log.md`, and the run's stored retrieval artifacts (`search/fetch_results.json`, `search/selected_sources.json`, `search/crossref_abstracts.json`).
**Review date:** 2026-11-23.

This is an AI-assisted research-integrity self-check of the kind the vendored agent defines: a pre-flight before a human editorial or ethics process, not a substitute for one. It evaluates the four Phase 5 items — AI disclosure compliance, attribution integrity, dual-use screening, fair representation — plus the human-subjects administrative status that the Phase 5 skill reports separately. It makes no institutional determination and authorizes nothing.

## 1. Integrity verdict

**CONDITIONAL — 7 conditions.**

The report passes the blocking tests: it contains no fabricated or ghost reference (41 references, all cited, all resolved to an indexing record in Phase 2), it carries an AI disclosure section, it does not plagiarize or pass off AI text as human-authored, it does not systematically misrepresent sources (25 of 26 claim-level checks agree substantively with the source abstracts), it contains no harm-enabling operational content, and no human-subjects activity occurs. None of the vendored agent's Critical conditions is met, so BLOCKED is not warranted and this review does not stop the run.

It is also not CLEARED. Seven defects are real and fixable, and two of them sit in the disclosure section itself: the disclosure asserts that "all findings were verified against cited sources" and that "human oversight was applied throughout the process," while §3.3 and §5.3 of the same report state that three records are citable only at title level, four abstracts are partial, "no theorem was checked, no residual was recomputed," and coding was single-analyst. A reader who reads only the disclosure would infer a verification and oversight standard the run did not meet. Separately, the abstract attaches three corpus-level counts to single sources, one source is described as "explicitly declining" a claim its abstract does not decline, one quotation drops interior words without an ellipsis, and preprint status is flagged at only two of its body points of use.

Because the report itself discloses the limits at §5.3, these are accuracy and completeness defects rather than concealment, and each is a text edit that does not require redoing the search, retrieval, or coding. The verdict is therefore CONDITIONAL: proceed to Phase 6 after the seven fixes in §8 are applied.

### 1.1 Authority-bound reporting status (what this review does and does not report)

The run directory contains **no** resolved-context registry with bound digests, **no** citation-gate (#651) output, **no** submission-packet manifest (#667), **no** review-pathway rule trace (#669), and **no** content-coverage advisory (#681). This review therefore does not report human-subjects requirement IDs, actor/consumer scope per requirement, packet structure, coverage status, or retraction-status fields, and does not simulate replays it cannot perform. Specifically:

- **#666 resolved context:** unavailable. Without an exactly bound context, a `validate_resolved_context` replay, and a downstream gate, no profile-dependent result may be reported. This review does not claim that replay and emits no requirement IDs. The bounded ID list in `references/ethics_checklist.md` §8 is a pointer set, not an applicable set for this run.
- **#667 submission packet:** not applicable and not supplied. No packet structure is reported; nothing here records packet DOCUMENTED or ACCEPTANCE_UNVERIFIED status.
- **#669 rule trace:** unavailable. No candidate rule trace is displayed.
- **#681 content coverage:** unavailable. Had an advisory existed it would be reported as LLM-ADVISORY with efficacy UNMEASURED; no coverage status is claimed.
- **#651 bibliographic signals:** unavailable. The report's "none is flagged retracted" (`phase4-report.md:107`) is an OpenAlex-flag statement; this review does not independently label any record as retracted or clear.

Nothing in this review is a replay-validated artifact, an authorization, a clearance, or an approval.

## 2. Checklist and dimension assessment

Status vocabulary: **PASS** (requirement met); **PASS WITH NOTE** (met, with a bound stated); **CONDITION** (must be fixed, see §8); **ADVISORY** (recommended, see §2.1); **N/A** (requirement does not apply); **NOT VERIFIABLE** (evidence for a pass was not supplied).

### Dimension 1 — AI disclosure

| Item | Status | Evidence location |
|---|---|---|
| Disclosure section present and visible | PASS | `phase4-report.md:211-213`; metadatum `:342` |
| AI tools/systems named, with version and date | CONDITION C1 | `:213` names only "AI-assisted research tools"; the workflow (ARS v3.24.4) is named at `:342`, no model is named |
| Scope covers all AI-executed stages | CONDITION C1 | `:213` names search, "source verification", synthesis, drafting; screening (775→41), matrix coding (41 rows), and grading (A/B/C) are AI-executed per `:99-115` and Appendices A–C but are not disclosed |
| Human oversight documented (who reviewed what, at which stage) | CONDITION C1 | `:213` is a generic sentence; `run-log.md:6` records operator preauthorization of an unattended run and checkpoint replies, not claim-level review |
| AI limitations acknowledged | CONDITION C1 | absent from `:211-213`; the real limits appear only at `:199` and `:107` |
| Disclosure accurate against the report's own method | CONDITION C1 | `:213` vs `:107` (five conditions, 3 metadata-only, 4 partial) and `:199` (single analyst, no theorem checked) |
| Nothing AI-generated passed off as human-authored | PASS | dedicated section; human author identified at `:3-4` |

### Dimension 2 — Attribution and citation integrity

| Item | Status | Evidence location |
|---|---|---|
| Reference list complete and usable | PASS | `:217-257`, 41 entries, preprints tagged `[Preprint]` |
| Every reference cited; no ghost or orphan reference | PASS | all 41 ref IDs appear in the body; Appendix C ledger `:292-338` |
| Reference identity resolves | PASS (recorded in Phase 2, not re-run here) | `phase2-verification.md:7`, `:12` — 41/41 DOI lookups resolved, 0 flagged retracted, no hand-repaired DOIs |
| Claims match the cited source | PASS WITH NOTE | 26/41 (63.4%) spot-checked against stored abstracts; 25 substantively agree, 1 unsupported (C3), and one of the 25 carries an imprecise quotation (C4) |
| Quotation exactness | CONDITION C4 | `:145` vs the N4 abstract |
| Corpus-level counts attributed correctly | CONDITION C2 | `:17` |
| Metadata-only sources handled honestly | PASS | `:93`, `:143`, `:147`, `:199`; `phase2-verification.md:73` |
| Preprint status flagged at the point of use | CONDITION C5 | `phase2-verification.md:7(ii)`; `:141` covers §4.2 only; untagged at `:17`, `:93`, `:111`, and inconsistently within `:143-149` |
| Self-citation rate | PASS | independent author (`:3-4`); no author-affiliated source identifiable in the corpus |
| Retraction status via the canonical gate | NOT VERIFIABLE | no #651 artifact supplied; `:107` is an index-flag statement only |

### Dimension 3 — Dual-use

| Item | Status | Evidence location |
|---|---|---|
| Harm-enabling operational specificity in the report | PASS (Level None) | construction-level descriptions only across §2–§4; no code, dataset, parameter set, or step-by-step procedure |
| Financial dual-use note present in the artifact | ADVISORY A4 | `phase1-scoping.md:119` declares none; the report has no statement |
| Responsible Use Statement required | N/A — threshold not met | `references/ethics_checklist.md` §3 triggers it at Moderate or above |

### Dimension 4 — Fair representation

| Item | Status | Evidence location |
|---|---|---|
| Method families and dissenting positions represented | PASS | `:143-149` (four family subsections), `:169-177` (tensions), `phase3-synthesis.md` §3 |
| Preprints graded and disclosed | PASS WITH NOTE | `:141`, `:199`, Appendix C; grading-cap tension is A5 |
| Metadata-only sources represented fairly | PASS | as in Dimension 2 |
| Language, index, and US concentration bias disclosed | PASS | `:199` (English-only, single index, "ten of the twelve rows with known provenance (approximately 83 percent)") |
| Declared-scope consistency | CONDITION C7 | C5 is a 2,576-stock panel (`:181`) while §3.1 says single-name equities "were excluded by design" (`:99`); `phase1-scoping.md:41` allows them only if flagged, and `phase2-verification.md:75` flagged it — the report does not |
| Precision of source characterization | ADVISORY A2 | `:93` "not admissible in any stated sense" |
| Vulnerable groups, stigmatizing or discriminatory language | N/A — no human populations in scope | full body review |

### Dimension 5 — Data ethics

| Item | Status | Evidence location |
|---|---|---|
| Personal or identifiable data | N/A — none | `phase1-scoping.md:119`; corpus is bibliographic and market data |
| Access and use basis for sources | PASS | public OpenAlex/Crossref/Semantic Scholar APIs, `:99-105` |

### Dimension 6 — Conflicts of interest

| Item | Status | Evidence location |
|---|---|---|
| Review's own competing interests and funding declared | CONDITION C6 | absent from `:1-8`, `:211-213`, `:340-342` |
| Source COI handling | PASS | `:199`; `phase2-verification.md:19` — "n/a means not retrieved, never none declared" |
| Predatory-venue screening | PASS WITH NOTE | `phase2-verification.md:79` — structural only, no live Beall/DOAJ/COPE check |

### Dimension 7 — Human subjects

| Item | Status | Evidence location |
|---|---|---|
| Human-subjects activity in the run | N/A — none | `phase1-scoping.md:30`, `:41`, `:119`; no recruitment, consent, intervention, or identifiable-data access in any artifact |
| Administrative status reporting | Reported separately in §7 | no #666 artifact supplied |

### Reproducibility (checklist §7)

| Item | Status | Evidence location |
|---|---|---|
| Search and screening trail reproducible | PASS WITH NOTE | `:99-115`, Appendices A–B; `search/retrieval_log.json`, `search/screening_log.json`; one failed query (`:99`), single screener |

### 2.1 Advisory notes (recommended, not conditions)

- **A1 — Referred editorial defect.** §2.3 is headed "The Seven-Dimension Evaluation Matrix" (`:70`), the text says "Eight evaluation dimensions were declared" (`:72`), Table 2 has eight rows, and §5.3 says "seven-dimension matrix" (`:199`). Editorial, not integrity; referred to Phase 5 editorial review.
- **A2 — Source characterization.** `:93` says the Bodurtha & Jermakyan baseline "was not admissible in any stated sense." Prefer "stated no admissibility condition," which is what the source supports and what the surrounding argument needs.
- **A3 — Phase 1 wording.** `phase1-scoping.md:119` says "No human subjects and no identifiable personal data, so no ethics review or consent process applies." The human-subjects statement is correct; the inference is not, because it conflates human-subjects review with the pipeline's research-integrity review. Reword to "no human-subjects review, recruitment, consent process, or identifiable-data access applies."
- **A4 — Add the dual-use assessment sentence.** One sentence in §5.3 stating that the review releases no code, data, or operational procedure and that the financial methods are described at construction level would satisfy the checklist's "brief note in limitations" for a None/Low level.
- **A5 — Reconcile the grading cap with the evidence axis.** The rubric caps any preprint at C (`:111`), so a proof-level preprint (P8) is graded below a peer-reviewed numerical test (B), inverting the report's own evidence hierarchy. State that the cap is a conservative venue rule applied uniformly, or report venue and evidence status as separate axes.

## 3. AI disclosure assessment

| Verification question | Result |
|---|---|
| Is an AI disclosure present? | Yes — dedicated section, `:211-213`, and listed in the document metadata, `:342` |
| Is the disclosed scope accurate? | Partly. It names search, "source verification", synthesis, and drafting. It omits screening, coding, grading, query construction, and appendix generation, all of which the report's method and artifacts show were AI-executed. |
| Are AI limitations acknowledged? | No. The disclosure contains no limitation sentence; the real limits live at `:107` and `:199`. |
| Is human oversight documented (who, what, which stage)? | No. One generic sentence. `run-log.md:6` records operator preauthorization of an unattended run, checkpoint replies ("确认" / continue), and no per-claim human review; `:199` records single-analyst coding. |
| Is anything AI-generated presented as human-authored? | No. The author is identified (`:3-4`) and the disclosure names AI assistance. |
| Is a model name/version/date given? | No model is named; the workflow version (ARS v3.24.4) appears only at `:342`, and it identifies the protocol, not the generator. |

Two sentences are materially inaccurate against the rest of the artifact. "All findings were verified against cited sources" is contradicted by `:107` (the verification result was a *conditional pass* with five conditions, including that three metadata-only rows are citable only at title level and four abstracts are partial) and by `:199` ("no theorem was checked, no residual was recomputed"). "Human oversight was applied throughout the process" is not supported by any run artifact: the recorded human role is authorization of an unattended run and review at checkpoints, which is oversight of the process, not of the findings. The disclosure should state the bounded verification standard the report actually met. C1 supplies a replacement paragraph.

## 4. Attribution and citation integrity

### 4.1 Reference integrity check

| Check | Result |
|---|---|
| References in the list | 41 (`:217-257`) |
| Reference entries cited in the body | 41 of 41; no orphan entry |
| Body citations without a reference entry (ghost citations) | 0 observed |
| Fabricated or unresolvable references | 0 found; Phase 2 records 41/41 DOI resolutions (`phase2-verification.md:7`, `:12`), not re-run in this review |
| Claim-level spot checks (enhanced threshold: ≥50%) | 26 of 41 (63.4%), against abstracts stored in `search/fetch_results.json` |
| Spot-checked rows | P2, P5, P6, P8, R1, R3, R5, R6, R7, R8, R9, N1, N2, N3, N4, C1, C5, G1, G2, G3, G4, G5, G6, G7, G8, S2 |
| Substantively consistent | 25 of 26 (one with an imprecise quotation) |
| Unsupported characterization | 1 — G7, "explicitly declines" (C3) |
| Imprecise quotation | 1 — N4, interior words dropped without ellipsis (C4) |
| Self-citations | 0 identifiable |
| Metadata-only handling | correct — P4, P7, R4 labelled `[Title/metadata only]` (`:143`, `:147`), citable only at title level (`:199`), graded `assumption` |
| Retraction status | not verified via a canonical gate; no #651 artifact supplied |

### 4.2 Findings

**Traceability is good and unusually transparent.** All 41 sources are listed, all are cited, the reference list distinguishes preprints, Appendix C carries an abstract-coverage column and a peer-review column for every row, and the body reports what each family leaves unmeasured. Numeric claims checked against stored abstracts agree: R5's ~5.4% butterfly floor over 252 SPX days, G5's 90.8% pass rate, R9's 2,695 SPY options across 28 maturities, R7's 98–99% inside-spread coverage, C5's 2,576 stocks over 26 years, N2's ten years of intraday S&P 500 data, and G6's zero violations at tolerance 10⁻⁴ across 15 synthetic runs all match their abstracts.

**Three corpus-level counts are attributed to single sources** (`:17`). The abstract's 17/16/8 evidence split cites Anagha (2026), the "ten engage time / none enforces or tests dynamic no-arbitrage" claim cites Niu (2015), and the "zero rows are directly comparable" claim cites Xiong & Liu (2026). Each is this review's own coding, reproducible from Table 3 and Appendix C; no named source reports the corpus total. The parentheticals read as support citations, so they misstate provenance even though the underlying counts are internally consistent. C2.

**One source is described as declining a claim its abstract does not decline** (`:51`, `:169`). The G7 abstract derives a state space free of *static* (model-independent) arbitrage and gives calibration methods "guaranteed to satisfy a set of linear inequalities"; it contains no sentence declining a dynamic statement. At the report's declared abstract-level read scope, "explicitly declines to claim it" attributes an explicit act to authors that the retrieved record does not show. The coding conclusion — that the model's guarantee is static-only — is supportable; the word "explicitly" is not. C3.

**One quotation is truncated without an ellipsis** (`:145`). The report quotes Sidogi et al. (2022) as "cannot directly learn the condition"; the abstract reads "the framework cannot directly learn the static arbitrage condition." Meaning is preserved but the quotation is not exact. C4.

**Metadata-only sources are handled honestly.** P4, P7, and R4 are labelled at title level in the findings (`:143`, `:147`), in the coverage column, and in the limitations (`:199`); P7 is introduced as "the only necessary-and-sufficient statement is a metadata-only preprint (Klassen, 2016)" and immediately bounded by "its result cannot be inspected at abstract level" (`:93`). This satisfies Phase 2 condition (i) and the checklist's title-level rule. It is the handling the ethics checklist asks for.

**Preprint flagging is the weakest attribution control.** Phase 2 condition (ii) requires the 11 preprints to be "labelled as such in every synthesis claim" (`phase2-verification.md:7`). The report satisfies this only partly: a blanket sentence at `:141` lists all 11 and declares their claims provisional, which covers §4.2; but only N3 (`:145`) and R8 (`:147`) carry inline tags, P8, N5, N6, R2, R6, and G6 are untagged in the same section, and the Abstract (`:17`, G6 and C2), §2.1 (`:51`, G6 and C2), §2.2 (`:55`, R6), §2.4 (`:93`, R6), and §3.4 (`:111`, C2 as the single level-VII review) cite preprints with no status flag. Appendix C and the reference list are not points of use. C5.

**No self-citation problem:** the author is an independent researcher with no identified affiliation or corpus paper. Retraction status cannot be verified because the canonical gate artifact was not supplied; the report correctly frames its own statement as an index-flag check (`:107`) rather than a retraction verification.

## 5. Dual-use screening and Responsible Use

| Screening question (checklist §3) | Answer |
|---|---|
| Does the output provide specific operational detail enabling misuse? | No. Repair methods are described at construction level ("a linear program that changes prices minimally inside bid–ask bounds", `:147`); no code, parameters, datasets, execution sequence, or circumvention guidance appears. |
| Could the material be misused? | Theoretically, any arbitrage-enforcement method inverts into a detector, and the corpus is explicitly about arbitrage. That property belongs to the published literature, not to this review, which adds no enabling specificity. |
| Is the topic itself a reason to escalate? | No. The vendored agent is explicit that subject matter alone — including politically or institutionally sensitive finance — never blocks. |
| Residual risk level | **None** (concrete enabling specifics absent). A Low residual remains only in the sense that the review summarizes methods whose source papers are executable by others. |

**Responsible Use Statement: not required.** The vendored table triggers a statement at Moderate or above; the report sits at None. Should a Phase 6 revision add operational detail — code, parameter values, a worked arbitrage-extraction procedure, or co-mingled market data — the level rises and a statement becomes required. A one-sentence note (A4) would make the assessment visible in the artifact, which is the checklist's recommendation for None/Low.

## 6. Fair representation

**Families and positions.** The review does not rank families and does not reduce them to a horse race. Each of the four families receives a findings subsection that states both what its rows establish and what they leave unmeasured (`:143-149`), §4.4 reports four genuine tensions rather than resolving them by fiat (`:169-177`), and §4.6 explains why numerical comparisons are not made (`:185`). Critical statements are tied to evidence: "the two rows that report adherence do so without stating a tolerance" (`:145`) is a source-level observation, not a dismissal. Hypothesis status is carried forward from synthesis (`phase3-synthesis.md` §2), including themes labelled "Emerging single-source". The corpus's recency skew — the strictest claims in the 2025–2026 preprints — is disclosed (`:199`) rather than smoothed.

**Preprints are graded, not hidden.** All 11 are identified by ID (`:141`), tagged in the reference list, counted in Appendix C, and capped at C by a disclosed protocol rule (`:111`). The cap is conservative and uniform, which is defensible; the tension is that a venue property is being used as an evidence-strength ceiling, so a proof-level preprint (P8) grades below a peer-reviewed numerical test. The report does not reconcile the two axes. A5 asks for a sentence, not a regrade.

**Metadata-only sources are not over-read.** Three rows are held to title level, excluded from proof claims, and named in the limitations.

**Language and geography.** The report states the corpus is English-only, drawn from a single index, and US-dominated (10 of 12 rows with known provenance, "approximately 83 percent"), naming the two exceptions (DAX 2006, JSE 2022). That is adequate disclosure; a consequence sentence — that non-English surface literature may be systematically underrepresented — would complete it but is not an integrity failure. The 83% figure traces to the dataset column in `phase3-synthesis.md` §1.

**Declared scope.** The one inclusion inconsistency is C5, a single-name stock panel admitted without the flag that Phase 1 requires and Phase 2 applied. §3.1 says single-name equities were excluded by design (`:99`), so the corpus contradicts its own stated criterion; the panel is described accurately at the point of use, so no reader is misled about the data, but the departure is undisclosed. C7.

**Inclusive language and vulnerable groups.** No human populations, no demographic claims, no stigmatizing or discriminatory framing. The 2,576-stock panel and index studies are described in neutral, technical terms. This dimension is effectively not engaged.

## 7. Human-subjects administrative status

**No human-subjects activity occurs in this run.** No recruitment, consent process, intervention, identifiable-data access, or data collection from persons appears in any Phase 1–4 artifact or in the retrieval logs; the corpus is bibliographic metadata and aggregated market data (`phase1-scoping.md:30`, `:41`, `:119`). This factual observation is not a readiness determination, an authorization, or an approval.

| Field | Value | Basis |
|---|---|---|
| `submission_readiness` | `unresolved` | No #666 resolved-context artifact (bound context, replay evidence, downstream gate) exists in the run. The vendored rule requires `unresolved` when the authority selection, bound input, replay evidence, or gate is missing — regardless of the absence of human-subjects activity. |
| `authorization_status` | `not_provided` | No authorization document exists in the run. None was expected, because no human-subjects activity occurs; the field reports artifact status only and does not infer approval. |
| `review_pathway` | `institutional determination required` | Reported unconditionally. No IRB, committee, or ethics-board pathway is engaged for this artifact. |
| `authority_context` | unavailable | No resolved context, registry, or bound digests were supplied; this review cannot and does not simulate `validate_resolved_context`. |
| `profile_dependent_result_allowed` | `false` | No resolved context or downstream gate; no profile-dependent row is reported. |
| Candidate rule trace | unavailable | No #669 artifact, no replay-validated trace, no `check_review_pathway_output.py` lint result. |
| Applicable requirement IDs | none emitted | The bounded #666 pointer set in `references/ethics_checklist.md` §8 could apply only through a resolved context, which is absent. |
| Actor / consumer scope per requirement | not applicable | No requirement is bound, so there is no actor or consumer scope to report. |
| Requirement and authority-anchor pointers | none bound | These would come from the resolved context; none exists. |

Readiness is `unresolved` because the authority artifacts are absent, not because a human-subjects gap was found. No institutional determination is made or implied.

## 8. Conditions

**Critical:** none. **Conditional:** C1–C7 below. **Advisory:** A1–A5 (§2.1).

### C1 — Rewrite the AI disclosure so it is accurate and complete

*Location:* `phase4-report.md:211-213`; contradiction points `:107`, `:199`; oversight evidence `run-log.md:6`.
*Defect:* "All findings were verified against cited sources" is contradicted by the report's own conditional-pass result (`:107`) and by "no theorem was checked, no residual was recomputed" (`:199`). "Human oversight was applied throughout the process" is not supported: the run log records operator preauthorization of an unattended run and checkpoint replies, not claim-level review. The disclosure also omits the AI system/model and version, the screening/coding/grading stages, an explicit AI-limitations statement, and any description of who reviewed what at which stage.
*Required fix:* replace the paragraph with bounded text that states (a) the stages AI executed, including screening, coding, and grading; (b) the model/system name, version, and date; (c) the verification standard actually met — abstract level, 34 full / 4 partial / 3 metadata-only abstracts, no full-text or proof checking; (d) the human role actually recorded — author/operator authorization and checkpoint review, no claim-level verification; (e) the AI limitations the report already concedes at `:199`. Author-supplied text follows; the model name and any claim-level human verification must be supplied by the author, not asserted by this review:

> *AI Disclosure: This report was produced with AI-assisted research tools operating under the ARS v3.24.4 deep-research protocol. The pipeline used AI for query construction and literature search (31 OpenAlex queries), screening (775 records to 41), source abstraction (34 full, 4 partial and 3 missing abstracts), coding of the 41-row evidence matrix and its grading, synthesis, and drafting. The generative model used was [model name and version], on [date]. Verification was abstract-level: all 41 records were resolved to an indexing record and none was flagged retracted, but no theorem was checked and no reported number was recomputed, and the three metadata-only rows are cited at title level only. Screening and coding were single-analyst, without dual screening or adjudication. Human oversight consisted of the operator's authorization of the run and review at the Phase 1–Phase 4 checkpoints recorded in the run log; no claim-level human verification of the 41 coded rows is recorded in the run artifacts. AI limitations: the pipeline could not read full texts, proofs or code, depends on third-party metadata and abstract reconstruction, and can introduce retrieval, quotation and coding errors that §5.3 bounds but does not eliminate.*

If a named human has in fact reviewed the coded rows, state that instead of (d), and record it in the run log.

### C2 — Attribute the abstract's corpus counts to the review's own coding

*Location:* `phase4-report.md:17`.
*Defect:* three sentences report the review's own coding totals (17/16/8 evidence split; ten rows engaging time and none enforcing dynamic no-arbitrage; zero directly comparable rows) but attach a single-source citation, which reads as support from that source. No named source reports those corpus totals; they are Appendix C / Table 3 counts.
*Required fix:* cite the coding artifact rather than a source, keeping the named sources as exemplars if useful. For example: "Coding of an evidence matrix (Table 3; Appendix C) shows that 17 sources assert their guarantee at proof level, 16 report a numerical test, and 8 assert admissibility without either; the one row that both certifies and audits at proof level is Anagha (2026)<!--ref:G6-->." Apply the same change to the ten-rows sentence and the zero-comparability sentence. Do not delete the source citations; re-scope them.

### C3 — Remove the "explicitly declines" attribution to Cohen et al. (2021)

*Location:* `phase4-report.md:51`, `:169`.
*Defect:* the cited abstract establishes a static (model-independent) arbitrage state space and "methods to calibrate neural SDE models which are guaranteed to satisfy a set of linear inequalities." It contains no statement declining a dynamic claim, and the report elsewhere declares an abstract-level read scope (`:199`), so the attribution cannot be made at the declared scope.
*Required fix:* replace "explicitly declines to claim it" with the supported formulation: "states its guarantee only for static, model-independent arbitrage (a set of linear inequalities), so the review codes it as making no dynamic claim." If a quoted declining sentence exists in the full text, add the quotation, its location, and a note that this one claim exceeds the abstract-level read scope.

### C4 — Make the Sidogi quotation exact

*Location:* `phase4-report.md:145`.
*Defect:* the report quotes "cannot directly learn the condition"; the source abstract reads "the framework cannot directly learn the static arbitrage condition." Interior words are removed without an ellipsis, so the quotation is not character-exact.
*Required fix:* restore the clause — "the framework cannot directly learn the static arbitrage condition" — or mark the elision — "cannot directly learn … the condition." No other change to the sentence is needed.

### C5 — Flag preprint status at every point of use

*Location:* `phase4-report.md:17` (G6, C2), `:51` (G6, C2), `:55` (R6), `:93` (R6), `:111` (C2), and inconsistent tags within `:143-149` (P8 at `:143`, N5/N6 at `:145`, R2/R6 at `:147`, G6 at `:149` are untagged while N3 and R8 are tagged).
*Defect:* Phase 2 condition (ii) requires the 11 preprints to be "labelled as such in every synthesis claim" (`phase2-verification.md:7`). The blanket sentence at `:141` covers §4.2, but the Abstract, §2.4, and §3.4 cite preprints with no status flag, and tagging inside §4.2 is inconsistent.
*Required fix:* add `[preprint]` at the first body use of each preprint — G6 and C2 in the Abstract, G6 and C2 at `:51`, R6 at `:55` and `:93`, C2 at `:111` — and make §4.2 consistent (tag P8, N5, N6, R2, G6 as N3 and R8 already are). A tag on every citation is not required; first use per section is sufficient if §3.3 states the convention.

### C6 — Declare the author's competing interests and funding

*Location:* `phase4-report.md:1-8`, `:211-213`, `:340-342`.
*Defect:* the report records that no COI or funding statement was retrieved for any of the 41 sources (`:199`) but makes no declaration for its own author. Checklist §6 requires the review's own declaration; readers cannot otherwise assess independence.
*Required fix:* add one line to the front matter, with content supplied by the author: "Competing interests: [none declared / specify]. Funding: [none / specify]." This review does not supply or infer that determination.

### C7 — Reconcile the inclusion statement with the corpus

*Location:* `phase4-report.md:99` (§3.1: "single-name equities, foreign exchange, rates and crypto underlyings were excluded by design"), `:181` (C5 described as a "2,576-stock, 26-year panel"), `phase1-scoping.md:41`, `phase2-verification.md:75`.
*Defect:* §3.1 states that single-name equity surfaces were excluded by design, but C5 is a single-name stock panel. Phase 2 admitted C5 only "with a scope flag: its panel is single stocks, not an equity index" (`phase2-verification.md:75`); Phase 4 describes the panel accurately at `:181` but drops the flag, so the corpus contradicts its own stated inclusion criterion without disclosing the exception.
*Required fix:* at `:181`, after "2,576-stock, 26-year panel (Stahl & Blauth, 2024)", add "(scope flag: single-name panel, not an index; retained because the constraint-diagnostic transfers)"; and in §3.1, after "were excluded by design", add "with one disclosed exception (C5), a single-name panel retained for its arbitrage diagnostic". Removing C5 instead would change Table 3, Appendix C, and the 17/16/8 counts; it is not recommended, because C5 contributes no enforcement claim and the flag fully repairs the disclosure.

## 9. Ethics clearance notes

- CONDITIONAL is not a veto. Under the vendored agent, this verdict permits the run to proceed to Phase 6 once the seven conditions are applied; it does not block, suspend, or retract anything.
- This review is not an IRB, ethics committee, or institutional review, and it makes no institutional determination. A human committee, editor, or institution supersedes it.
- The operator's preauthorization (`run-log.md:6`) is execution authorization for the validation run. It is not an ethics authorization, and this review does not treat it as one.
- No human-subjects activity occurs, so the #666 pathway is not engaged on the facts. Readiness is `unresolved` only because the authority artifacts were not supplied; that status must not be read as a finding of a gap.
- No artifact in this run is a replay-validated authorization, a packet manifest, a rule trace, or a coverage advisory, and none is reported as one.

## 10. Ethics decision log

No CONDITIONAL or BLOCKED item has been acted on: this review is the first Phase 5 pass and the run log records no ethics decision for it. No user reasoning is invented.

| Condition | Item | User decision recorded | Status |
|---|---|---|---|
| C1 | AI disclosure accuracy and completeness | none recorded | open |
| C2 | Abstract corpus-count attribution | none recorded | open |
| C3 | "Explicitly declines" attribution (G7) | none recorded | open |
| C4 | Sidogi quotation exactness | none recorded | open |
| C5 | Preprint status at point of use | none recorded | open |
| C6 | Author COI and funding declaration | none recorded | open |
| C7 | Inclusion statement vs corpus (C5) | none recorded | open |

## 11. Limitations of this review

1. **No independent re-resolution of references.** DOI identity rests on Phase 2's recorded 41/41 resolutions (`phase2-verification.md:12`) and on the stored DOI/title pairs; this review did not query OpenAlex or Crossref itself and did not check for newer versions of any preprint.
2. **Claim-level checks are abstract-level only, like the report.** 26 of 41 rows were checked (63.4%) against stored abstracts; the remaining 15 were not. No full text, proof, dataset, or code was read, so this review cannot say whether the mathematics is correct, only whether the report's statements match what the abstracts say.
3. **Three metadata-only and four partial abstracts were not independently retrievable.** P4, P7, and R4 (metadata-only) and R2, G3, C2, C4 (partial) could not be checked beyond what the run stored; this is the same ceiling the report discloses.
4. **No canonical retraction gate.** Without a #651 `bibliographic_integrity_signals[]` artifact, retraction status is unverified. The report's "none is flagged retracted" (`:107`) is an OpenAlex-flag statement, and this review neither confirms nor upgrades it.
5. **No human-subjects authority artifacts.** No #666 resolved context, #667 manifest, #669 trace, or #681 advisory was supplied, so no requirement IDs, actor/consumer scope, packet structure, rule trace, or coverage status is reported. Those absences are stated, not simulated; nothing here is a replay-validated authorization.
6. **Author and source COI are not verified.** Affiliations were not checked and no source COI statement was retrievable; undeclared interests cannot be excluded.
7. **Single reviewer, one pass.** The ethics coding itself has no inter-rater reliability. The 26-of-41 spot-check set was chosen for claim stakes (numbers, quotations, and the "explicitly" characterizations), not sampled at random, so the issue rate is not an unbiased estimate.
8. **Editorial and domain quality are out of scope.** Argument quality, the taxonomy's soundness, and the financial-economics claims were not assessed; the seven/eight-dimension inconsistency (A1) is referred, not adjudicated.
9. **Process documentation is stale.** `run-log.md:14` still records Phase 3 as "in progress" although Phase 3 and Phase 4 artifacts exist, and the run log does not record who reviewed what. This limits any reconstruction of the human-oversight chain and is one reason C1's oversight sentence cannot be verified as written. The log was not modified by this review.
10. **Scope of inputs.** Only the vendored v3.24.4 agent and checklist text was applied; the installed 0.4.6 plugin text was ignored as instructed. The review was performed on the Phase 4 artifact as written on 2026-11-23 and does not bind any later revision.

> **Human-subjects boundary:** This output does not authorize recruitment, consent, access to identifiable data, intervention, or data collection.
