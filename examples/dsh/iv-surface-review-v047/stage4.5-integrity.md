# Stage 4.5 — Final Integrity Verification (Mode 2)

| Field | Value |
|---|---|
| Stage | 4.5 — final integrity check after revision (gate to Stage 5) |
| Mode | 2 — final check, run from scratch; Stage 2.5 verdicts reused only where explicitly carried |
| Target draft | `stage4-prime/paper-draft-v3.md` — v3.0, 737 lines, 124,011 bytes, 7,761 body words |
| Draft binding | sha256 `090a59925f385490f000f6ec78a7a7e9e2499b73f12278b9b899d01ccd36e3cc` |
| Protocol | ARS v3.24.4 `skills/academic-pipeline/agents/integrity_verification_agent.md`; `references/claim_verification_protocol.md`; `references/ai_research_failure_modes.md` |
| Verdict | **FAIL** — 0 SERIOUS, 0 MEDIUM, 0 MAJOR_DISTORTION, 0 UNVERIFIABLE, **2 MINOR** |
| Date / verifier | 2026-11-23 (Asia/Singapore) / independent verifier, not the Stage 2.5 author |

## 1. Scope and materials

Read in full before judging: the manuscript under test; predecessors `stage4/paper-draft-v2.md` (v2.0) and `stage2/paper-draft.md` (v1.3) for drift; `stage4/reliability/second-coder-form.json` and `adjudication.md`; `stage4/coding-handbook.md` (D.9, D.10); `stage4/response-to-reviewers.md`; `stage4/revision-log.md`; `stage3/editorial-decision.md`, `author-letter.md`, `review-panel-provenance.json`; `stage3-prime/re-review.md`; `stage2.5-integrity.md` and `stage2.5-artifacts/`; evidence corpus `search/selected_sources.json`, `fetch_results.json`, `crossref_abstracts.json`, `openalex_candidates.json`, `screening_log.json`, `retrieval_log.json`; Stage 1 records `phase2-verification.md`, `phase3-synthesis.md`.

The manuscript was not modified. Only `stage4.5-artifacts/` and this report were written. Every count below was recomputed from the frozen records or is marked as not recomputable; none was copied from Stage 2.5 without the carry check in §7.

Archive boundary (unchanged from Stage 2.5 and disclosed rather than repaired): no full text, proof, or code was retrieved, so Phase E reads abstracts only (38 held abstracts; P4, P7, R4 are metadata-only); no independent retraction-database sweep is possible here (OpenAlex `is_retracted` only); the run has no passport, hence no `experiment_intake_declaration`; semantic claim-extraction completeness is not machine-detectable; the review's own coding decisions are checked for internal consistency, not against external truth.

## 2. Scripts run

All with the fork venv (`/Volumes/ExternalSSD/projects/dsh-academic-research-skills/fork/.venv/bin/python`), from the run directory; artifacts in `stage4.5-artifacts/`.

| Script / command | Output | Exit | sha256 (first 16) |
|---|---|---|---|
| `build_claim_registry.py stage4-prime/paper-draft-v3.md stage4.5-artifacts/claim-registry.json` | `claim-registry.json` (202 claims) | 0 | `20d6169cb7ecad0f` |
| `scripts/claim_registry_coverage.py --draft … --registry … --output …` | `claim-registry-coverage.json` | 0 | `d4f63d2742c5e7e2` |
| `scripts/claim_registry_coverage.py --validate-report …` | `claim-registry coverage replay: PASS` | 0 | — |
| `build_evidence_rows.py` | `evidence-rows.json` (112 rows), `evidence-rows-summary.json`, `evidence-sources/` (38) | 0 | `bcb23db21c6d41a1` / `6631d07f3716504e` |
| `phase_bd.py` (paragraph diff, citations, 8-gram test) | `phase-bd-checks.json` | 0 | `f761df5d9ee78e5e` |
| `phase_c_recompute.py` (ledger, retrieval, reliability) | `phase-c-checks.json` | 0 | `64b36b30fcc869ca` |
| `phase_a.py` (live DOI resolution, 41 GETs) | `phase-a-doi-checks.json` | 0 | `385d69ffddd85250` |
| `scripts/check_revision_token_conservation.py pair` ×2 | `token-conservation-v2-v3.json`, `-v1.3-v3.json` | 0 | `ccf13db863ef9201`, `0d4c8c3991e2b880` |
| `claim-verdicts.json` (per-claim table) | 59 claims | — | `a3bc60e2619173f7` |

## 3. Phase A — Reference integrity (fresh, all 41)

| Check | Result |
|---|---|
| DOIs resolved live via `https://api.openalex.org/works/doi:<DOI>` | 41 / 41, HTTP 200 |
| DOI echo matches reference entry | 41 / 41 |
| Title (normalised) matches | 41 / 41 |
| Year matches | 41 / 41 |
| First author matches | 41 / 41 |
| Retraction flag raised | 0 / 41 |
| References listed ↔ corpus (`selected_sources.json`) one-to-one | 41 / 41 |
| Inline `<!--ref:ID-->` markers / distinct IDs | 112 / 41 |
| Dangling citations (cited, not listed) | 0 |
| Orphan references (listed, not cited) | 0 |
| Preprint tags | 11 = P7, P8, N3, N5, N6, R2, R6, R7, R8, G6, C2 |
| Years | 5 seminal (1999–2014) + 36 in-window (2015–2026) |

**Verdict: VERIFIED.** The only metadata deltas between reference entries and corpus records are the bracketed `[Preprint]` title suffixes, a stated corpus convention. A2 audit trail exists for every reference (`phase-a-doi-checks.json`: DOI, resolved title, year, first author, retraction flag). Tool limitation: resolution is by DOI through OpenAlex, not an independent web search, and no independent retraction list was swept.

## 4. Phase B — Citation context

Coverage: 79 body paragraphs; 71 were added (32) or substantially modified (39) between v1.3 and v3 — **100% audited** (threshold 100% of modified); 79/79 = 100% of all body paragraphs examined (threshold ≥50%). 31 body paragraphs carry 105 citation markers; 7 more sit in appendix prose/captions (112 document-wide). 112 (claim, source) contexts checked against the held abstract.

| Check | Result |
|---|---|
| Contexts checked | 112 / 112 registered pairs |
| Severe misrepresentation (SERIOUS) | 0 |
| Citation-context deviation (MEDIUM) | 0 |
| Imprecise but correct (MINOR) | 0 issues; 2 notes (NOTE-4, NOTE-5) |
| Sensitive paragraph §2.1 (corrected butterfly condition) | content and SC3/SC4 reasoning verified; the displayed prefactor is wrong → **F-MINOR-1** (Phase C) |
| Sensitive paragraph §5.1 (proof/audit partition) | verified: 16+1+5+11+8=41, 1+5=6 audit, audit∩proof = G6 only, "one of 17 proof rows reports a violation rate" = G6, three of six audit rows preprints (N6, R7, G6) |

**Verdict: PASS** (two precision notes, no distortion).

## 5. Phase C — Numbers and internal consistency

| # | Quantity | Stated | Recomputed | Result |
|---|---|---|---|---|
| 1 | Sources | 41 | 41 | match |
| 2 | In-window + seminal | 36 + 5 | 36 + 5 | match |
| 3 | Composition | 29 peer-reviewed, 11 preprints (26.8%), 1 practitioner | 29/11/1; 26.83% | match |
| 4 | Abstract coverage | 34 full / 4 partial / 3 metadata-only | 34/4/3 (R2,G3,C4,S1 / P4,P7,R4) | match |
| 5 | Evidence status | 17 proof / 16 test / 8 assumption | 17/16/8; in-window 16/14/6; seminal 1/2/2 | match |
| 6 | Audit partition | 16+1+5+11+8 = 41; 1+5 = 6 | same; audit rows N2,N6,R5,R7,G5,G6; ∩proof = G6 | match |
| 7 | Time axis | 10 rows; D3 0 / D2 3 / D1 4 / D0 34 | same rows (P8,R8,G1,G2,G3,G7,C2,C3,C5,S5) | match |
| 8 | Comparability | 0 direct / 30 context / 11 not comparable | same; every Table 5 cell | match |
| 9 | Families / construction rows | P8 N6 R9 G8 C5 S5; 31 construction rows | same; 8+6+9+8 = 31 | match |
| 10 | Evidence level | 40 VI / 1 VII (C2) | same | match |
| 11 | Retrieval | 775 requested (31×25) / 750 returned / 430 unique / 389 excluded / 41 included | 775/750/430/389/41; 21 first-pass 429s, 20 recovered, 1 lost | match |
| 12 | Query strings | 31 in 8 groups | 2+6+2+3+6+6+3+3 = 31 (Table A1) | match |
| 13 | Discretionary exclusions | 40 rows (Table A2) | 40 rows; log indices match the screening log | match |
| 14 | Reliability | 12/16, 10/16 (κ 0.47), 15/16, 16/16, 16/16, 10/16; 79/96; 17 adjudicated | 96 cells, 79 agree; family 12, evidence 10 (κ 0.47), audit 15, time 16, dynamic 16, comparability 10; 17 disputes | match |
| 15 | Body words | v3 7,761; v2 7,862 (letter) | 7,761 (v3), 7,862 (v2) | match |
| 16 | Revision log v2 count | 7,784 | 7,862 | **NOTE-2** |
| 17 | English abstract | letter: 249 words (limit 150–250) | 272 (v3) / 259 (v2) | **NOTE-1** |
| 18 | §2.1 second-derivative identity | `C″(K)=K⁻¹e^{−2k}(c″−c′)` | `(F/K²)(c″−c′)=K⁻¹e^{−k}(c″−c′)=e^{−2k}/F·(c″−c′)` | **F-MINOR-1** |
| 19 | Table A1 note (de-dup union) | "de-duplicated … is the 750-record retrieval set" | Table 1: 750 returned, 430 unique after de-duplication | **F-MINOR-2** |

Table 6's three "about" entries (fit ≈8, interpolation ≈8, cost ≈5) are declared approximations and the ledger codes no dimension counts, so they are not machine-recomputable; they are consistent with §5.3/§5.4 prose and are treated as approximate labels, not counts. Abstract ↔ body: every abstract number and finding is stated in the body (§5.1, §5.4, §7.1); the only abstract-only wording is the pair-level comparability clause (NOTE-7).

Token-conservation audit (not a verdict, per protocol): `check_revision_token_conservation.py pair` returns `conserved: false` for both v2→v3 and v1.3→v3. For v2→v3 the number deltas (removed: 2015, 2026, 11, 23, 6×3, 31×2, 2×2, 3×3, 25×2, 01×2, 775, 750, 429, 30; added: 29, 3.4, 12) are exactly the documented Stage 4′ edits — the removed duplicated §3.1 corpus-construction paragraph (second occurrences of the retrieval numerals) and the D.10 peer-review tally corrected to 29 yes / 12 no; citations and protected terms are unchanged. The v1.3→v3 run is a rewrite-scale delta (111 numbers added, 18 removed; citation strings re-anchored/renumbered; no protected-term change), with no unexplained loss.

**C4 — experiment provenance.** The run carries no passport (a `passport*` search of the run directory is empty), so the D7 declaration-anchored anti-skip cannot be positively satisfied. The rule is fail-closed: only a passport with positive proof of `repro_lock.ars_version` < 3.12.0 is legacy; everything else is treated as post-#260, which ARS v3.24.4 (≥ 3.12.0) makes unavoidable here. For a treated-as-post-#260 run the absent `experiment_intake_declaration` is formally FAIL condition (1) — a literature-only run still needs `status: no_experiments_declared`, `declared_by`, `declared_at`. There is, however, no evidence distortion in the certified object: the Methods describe a literature search and screening procedure only, and the manuscript contains no author-run experiment, run setting, or Results-section first-person outcome (the Stage 2.5 heuristic likewise found no first-person experiment verb), so condition (4) is not met. The declaration gap is a run-artifact / authority-chain item — the same #670-class gap recorded in `run-log.md` — not a manuscript issue; it does not change any Phase A–E finding and is carried to the Stage 5 entry checkpoint with the fix stated in §13.

**Verdict: FAIL** — two MINOR issues (F-MINOR-1, F-MINOR-2); no SERIOUS/MEDIUM/UNVERIFIABLE numeric defect; plus the C4 declaration artifact condition above (non-manuscript).

## 6. Phase D — Originality

Coverage: 79/79 body paragraphs graded (100%, threshold ≥50%); 71/71 revised paragraphs graded (100%).

| Grade | Paragraphs |
|---|---|
| ORIGINAL | 79 |
| COMMON_KNOWLEDGE | 0 |
| PARAPHRASE | 0 |
| CLOSE_MATCH | 0 |
| VERBATIM (20+ identical unquoted words) | 0 |

Shared 8-gram test against all 38 held source abstracts: **zero shared 8-grams**; longest shared token run is 5 tokens (source N5). Cross-draft overlap (v3 body is v2's body minus one removed paragraph; 8 paragraphs survive from v1.3) is expected and is not self-plagiarism — only earlier drafts of this same text exist and no other author text was used.

**Verdict: PASS.**

## 7. Phase E — Claim verification (Mode 2 = ALL)

Registry: `claim-registry/1.0`, bound to the v3 raw sha256 above; 202 claims = 169 coverage-detector candidates + 33 explicitly registered absence/count statements; every `selection_tier` = `ALL`; every span decodes byte-exactly to its claim text; schema validation PASS (`claim_registry.schema.json`). Coverage sidecar: `claim-registry-coverage.json` — `candidate_unregistered_count: 0`; all 169 candidates `registry_span_matched`; `mixed_or_partial_registry_coverage` absent; 33 registered claims lie outside the detector classes; `semantic_extraction_coverage: not_machine_detectable` (a clean report does not certify completeness). Replay with `--validate-report` prints `PASS`.

Evidence rows (`evidence-rows.json`, schema `evidence-row/1.0`): one row per (claim, source) pair; 112 rows covering 59 citation-bearing claims and all 41 slugs; the remaining 143 registered claims are the review's own coding/ledger statements, which have no cited source and are verified in Phase C against the frozen ledger instead (no registered claim is left unaudited).

| Level | VERIFIED | MINOR_DISTORTION | MAJOR_DISTORTION | UNVERIFIABLE | UNVERIFIABLE_ACCESS |
|---|---|---|---|---|---|
| Rows (112) | 109 | 0 | 0 | 0 | 3 |
| Claims (59) | 56 | 0 | 0 | 0 | 3 |

The three UNVERIFIABLE_ACCESS rows are CLM-034/P4, CLM-036/P7, CLM-049/R4: metadata-only records whose reference entries pin the cited version by DOI, so the label names that version rather than saying "version not identified". Carried from Stage 2.5: exactly one row, `EVR-CLM-079-C2` (byte-identical span, same ref, unchanged paragraph); the other nine byte-identical ref-bearing claims sit inside paragraphs modified by Stage 4/4′ and were freshly checked, as were all 111 other rows.

**Verdict: PASS WITH NOTES** (3 UNVERIFIABLE_ACCESS notes; 0 MINOR/MAJOR_DISTORTION, 0 UNVERIFIABLE).

## 8. Revision drift (v1.3 → v2 → v3)

| Transition | Added | Substantially modified | Unchanged | Removed |
|---|---|---|---|---|
| v1.3 (76 paragraphs) → v3 (79) | 32 | 39 | 8 | 29 of v1.3's paragraphs have no counterpart (superseded) |
| v2 (80 paragraphs) → v3 (79) | 0 | 0 | 79 | 1 |

The single v2→v3 removal is the duplicated §3.1 corpus-construction paragraph ("The corpus was assembled from the OpenAlex … API with 31 free-text queries in eight groups …"), which duplicates Appendix A.1 — the Stage 4′ log's first edit. The v3 abstract rewrites the proof/audit sentence (the log's fourth edit), and D.10's tally is corrected to 29 yes / 12 no (second edit); the AI-disclosure sentence is replaced (third edit). No count, table, or reference changed in v3, as the log claims and as Phase C confirms. The §2.1 prefactor error entered in v2 (v2 line 52 is byte-identical to v3 line 52), was reproduced in the response letter (line 95), and re-review marked R6 "Fully Addressed" on that derivation — the drift is one of verification depth, not of strength of claims. E6 drift is skipped (below): this run has no revision patch bundle, no patch sidecars, and no Schema 7 roadmap, so there is no claim-strength drift record to compare (same #670 gap as `run-log.md`); no bundle was reconstructed.

## 9. Seven-mode AI-failure checklist

| Mode | Evidence | Verdict |
|---|---|---|
| 1. Implementation bug passing self-review | No implementation or executed experiment in this paper; no `experiment_intake_declaration` exists (no passport), and the Methods describe a literature search/screening procedure only | NOT APPLICABLE (declaration absent — limitation recorded, not a pass) |
| 2. Hallucinated citation | 41/41 DOIs resolved live, 0 retracted, 0 dangling, 0 orphan; corpus one-to-one | CLEAR |
| 3. Hallucinated experimental result | No experiments; every number recomputed from the run's own frozen logs; no results attributed to the author | NOT APPLICABLE |
| 4. Shortcut reliance | Declared: abstract-level evidence, single database, 16-row recheck, title-level pool audit, single analyst; no undisclosed shortcut is presented as verified | CLEAR |
| 5. Implementation bug reframed as novel insight | No implementation, no bug-to-insight narrative | NOT APPLICABLE |
| 6. Methodology fabrication | No experiment run; every Methods number (31 queries, 775/750/430/389/41, 16-row sample, 79/96) appears in the frozen records | NOT APPLICABLE |
| 7. Frame-lock at an early stage | Frame revised under R1/R2; claims explicitly bounded; §7.2 states falsifiable consequences | CLEAR |

No mode is SUSPECTED; no mode found SUSPECTED at Stage 2.5 survives here.

## 10. Issues

| ID | Severity | Location | Finding | Fix |
|---|---|---|---|---|
| F-MINOR-1 | MINOR | §2.1, line 52 | The displayed identity is off by a factor e^{−k}: it prints `C″(K)=K⁻¹e^{−2k}(c″−c′)`; the correct second derivative of C(K)=F·c(log(K/F)) is `(F/K²)(c″−c′)=K⁻¹e^{−k}(c″−c′)=e^{−2k}/F·(c″−c′)`. Numeric Black–Scholes check (F=100, K=60.6531, k=−0.5, σ√τ=0.2): printed-form 0.0030369 vs true 0.0018420, ratio e^{−k}=1.6487; finite difference 0.0018461. The sign condition c″−c′≥0, the SC4-tightness argument, the −0.53/+0.07 numbers and the 39-row SC3 coding are unaffected, and no count changes. The same expression appears in `stage4/paper-draft-v2.md:52` and `stage4/response-to-reviewers.md:95` | Replace e^{−2k} with e^{−k} (or write (F/K²)(c″−c′)); correct the response letter if it is resubmitted |
| F-MINOR-2 | MINOR | Appendix A.1, Table A1 note, line 462 | The note says the union "de-duplicated by DOI and then by normalised title, is the 750-record retrieval set"; Table 1 states 750 **returned** and 430 unique **after** de-duplication, so the note contradicts Table 1 and §3.1 | Reword: "the 750 returned records de-duplicate to 430 unique records (Table 1)" |

Notes (non-blocking; notes never gate):

| ID | Location | Finding | Fix |
|---|---|---|---|
| NOTE-1 | `stage4/response-to-reviewers.md:19` | Says the English abstract is 249 words (limit 150–250); measured 272 (v3) and 259 (v2); the Chinese 491 characters matches | Restate the count and, if 250 is a hard cap, trim the abstract |
| NOTE-2 | `stage4/revision-log.md` (header and §4) | States v2 body = 7,784 words with per-section 617/1153/1229/1170/1536/1303/776; measured v2 = 7,862 = 617/1153/1227/1198/1588/1303/776; the log's own Stage 4′ table says 7,862 → 7,761 | Restate 7,862 and the per-section figures |
| NOTE-3 | §7.1, line 344; Abstract, line 12 | Enumerates four certified-object kinds but Table 2 and §2.3 add "the inherited class" (model-class rows G1, G7, C3) | Add "or the model class itself" to §7.1 (and abstract if space allows) |
| NOTE-4 | §6.2, line 316; §4.4, line 210; Appendix C.5, line 581 | Says the neural-SDE row "explicitly disclaims dynamics"; the held abstract guarantees only freedom from static (or model-independent) arbitrage and contains no literal dynamic disclaimer (wording already in v1.3) | Tighten to "guarantees only static admissibility"; evidence row stays VERIFIED |
| NOTE-5 | §3.1, CLM-021 | "…and a foreign-exchange delta-condition paper by Fukasawa (2022)" reads as if Fukasawa wrote the FX paper; A.3 shows the FX record was displaced and replaced by Fukasawa's equity-index asymptotics paper | Copyedit to "…was replaced by Fukasawa (2022), whose subject is equity-index implied-volatility asymptotics" |
| NOTE-6 | `stage4-prime/paper-draft-v3.md:5` | Front matter says "Version: v2.0" while the pipeline and revision log call this file v3.0 | Update to v3.0 |
| NOTE-7 | Abstract EN line 12, ZH line 20 | "no two sources state data, metric and tolerance together" is a pair-level compression of §5.4's "one row states a tolerance and a loss together (G6)" and §5.2's four-field finding; no body sentence states the joint count and Appendix B has no field-presence column, so a reader cannot recompute the pair claim | Mirror §5.2's four-field wording in the abstract (both languages) or add the joint count to §5.2. Not contradicted by the body |

Open access notes: 3 claims/rows are UNVERIFIABLE_ACCESS (P4, P7, R4 metadata-only; their cited versions are pinned by DOI, so this is access, not version ambiguity). All other 38 cited abstracts are held and were read, including N1 (838 chars) and C1 (820 chars) — the Stage 2.5 "bibliographic only" status for those two is superseded and CLM-073/C1 is now freshly verified rather than carried. No independent retraction-list sweep is possible from this environment; no passport and no `experiment_intake_declaration` exist (see C4 in §5); Table 6's "about" counts are declared approximations.

## 11. Advisories (advisory only — never gate)

| ID | Kind | Result |
|---|---|---|
| ADV-E4-1 | Scope-absence (E4) | No broadening: scope = equity-index listed options, 2015-01-01–2026-11-23, English, OpenAlex only, public metadata/abstracts, 5 declared seminal precursors; every absence claim stays inside it |
| ADV-E5-1 | Novelty (E5) | §6.2 absence claim is SUPPORTED_WITHIN_SEARCH: wording is search-bounded ("to our knowledge"), the databases and date window match the documented strategy (OpenAlex, 2015-01-01–2026-11-23), the search date (2026-11-23) is recorded in `run-log.md:3` and manuscript §6.2, and the nearest prior work (Niu 2015) is acknowledged. Not a global-novelty claim. Disclosure: `search/retrieval_log.json` carries no machine `last_searched_at` field, so the date is evidenced by the run log and manuscript, not by a timestamp in the retrieval log |
| ADV-CACHE | Cache reuse | Not applicable — no cached research artifacts were consumed |
| E6 | Claim-strength drift | `[E6-SKIPPED: no revision evidence]` — no patch bundle, no patch sidecars, no Schema 7 roadmap in this run (same #670 gap as `run-log.md`); the artifact records status `skipped_no_revision_evidence`, null bundle hash, empty findings |

## 12. Determinism and replay

Registry rebuild from the same draft is byte-identical (sha256 `20d6169c…`); coverage rerun is byte-identical (`d4f63d2742…`) and the replay validator prints PASS. Evidence rows reproduce all claim, verdict, excerpt and source fields byte-identically; only the runtime `captured_at` (UTC) and the dependent `row_sha256` differ between invocations (112 rows) — content is deterministic. Phase A resolution is live: a replay at another time may return updated OpenAlex metadata, so `phase-a-doi-checks.json` is part of the record. Phase B/D and C scripts are pure functions of the frozen files (hashes above). The Stage 2.5 carry is explicit in row detail text (`carried_from: stage2.5-integrity.md`) rather than implicit.

## 13. Verdict rationale

The ladder (protocol lines 689–693) gives PASS only at zero SERIOUS + zero MEDIUM + zero MAJOR_DISTORTION + zero UNVERIFIABLE; PASS WITH NOTES at those zeros plus only MINOR/MINOR_DISTORTION/notes; FAIL at any SERIOUS, any MEDIUM, any MAJOR_DISTORTION, any UNVERIFIABLE — "and at Stage 4.5 also any MINOR or MINOR_DISTORTION" (the output template marks MINOR as "Recommended Fix at Stage 2.5; Must Fix at Stage 4.5"). Here there are **2 MINOR issues** and nothing above MINOR: the verdict is therefore **FAIL**, and PASS WITH NOTES is unavailable by construction, even though every note and advisory is non-blocking. This is the same ladder Stage 2.5 applied; both MINOR items were introduced by the v2 revision (the v1.3 text has neither), and the Stage 3′ re-review accepted the equation as an addressed issue.

Both corrections are local and change no count, table, or claim: F-MINOR-1 is one symbol in one sentence (plus the same symbol in the response letter); F-MINOR-2 is one clause in one table note. Neither touches the corpus, the ledger, the reliability figures, or any evidence-row verdict. Independently of them, C4 condition (1) is formally unmet because no declaration exists (see §5); that is a run-artifact condition, carried as correction item (3), and it is not counted in the issue table.

**Fail loop (round 1 of at most 3).** Correction list, severity-sorted: (1) F-MINOR-1 — fix the prefactor in §2.1 and in `stage4/response-to-reviewers.md:95`; (2) F-MINOR-2 — fix the Table A1 note; (3) the non-manuscript artifact item — persist `experiment_intake_declaration` (`status: no_experiments_declared`, `declared_by`, `declared_at`) or record an explicit operator decision, so C4 condition (1) is closed at the Stage 5 entry checkpoint (no new registry binding is needed for this item). Then re-run Stage 4.5: re-verify both corrected items and re-run C2 over §2.1 (equation text changed) and over the abstract if NOTE-1/NOTE-7 are also addressed. If the corrected text passes with no new issue, the verdict becomes PASS (notes only) and the Stage 5 gate opens. If issues remain, round 2 follows; after round 3 the orchestrator must notify the user with the unresolved list, and Stage 5 may start only on PASS or an explicit recorded user decision.

**Gate to Stage 5: NOT MET.** The terminal PASS condition (zero issues at Stage 4.5) is not satisfied: F-MINOR-1 and F-MINOR-2 are open, and the C4 declaration artifact is unrecorded. The certified object is `stage4-prime/paper-draft-v3.md` at sha256 `090a59925f385490f000f6ec78a7a7e9e2499b73f12278b9b899d01ccd36e3cc`; a corrected draft is a new object and needs a new registry binding and a Stage 4.5 rerun.
