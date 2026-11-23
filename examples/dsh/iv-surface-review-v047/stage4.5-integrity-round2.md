# Stage 4.5 — Final Integrity Verification, Round 2 (Mode 2)

| Field | Value |
|---|---|
| Stage | 4.5 — final integrity check after revision (gate to Stage 5), FAIL-loop round 2 of at most 3 |
| Mode | 2 — fresh from-scratch pass on the new bytes; round-1 verdicts reused only where explicitly carried |
| Target draft | `stage4-prime/paper-draft-v3.1.md` — v3.1, 737 lines, 124,057 bytes, 7,761 body words |
| Draft binding | sha256 `d05dd0508ef7ff38eea4f319a0a9883f76a94cd762939d8cc68263e805431009` |
| Round-1 target (preserved) | `stage4-prime/paper-draft-v3.md` — v3.0, sha256 `090a59925f385490f000f6ec78a7a7e9e2499b73f12278b9b899d01ccd36e3cc`; round-1 record `stage4.5-integrity.md` intact |
| Round-1 verdict | FAIL — 0 SERIOUS, 0 MEDIUM, 0 MAJOR_DISTORTION, 0 UNVERIFIABLE, 2 MINOR (F-MINOR-1, F-MINOR-2) |
| Round-2 verdict | **PASS WITH NOTES** — 0 SERIOUS, 0 MEDIUM, 0 MINOR, 0 MAJOR_DISTORTION, 0 UNVERIFIABLE (notes only) |
| Date / verifier | 2026-11-23 (Asia/Singapore) / independent verifier, not the Stage 2.5 author |

## 1. Scope and round-2 delta

The certified object is the new byte sequence `stage4-prime/paper-draft-v3.1.md` (sha256 `d05dd050…`). The manuscript was not modified by this verification; only `stage4.5-artifacts/round2/` and this report were written. v3.0 is byte-unchanged (sha256 `090a5992…`), so the round-1 record remains a valid audit of a distinct object.

A byte diff v3.0 → v3.1 shows exactly two body edits and no other change:

| # | Location | Round-1 finding | v3.1 text after correction | Verified |
|---|---|---|---|---|
| 1 | §2.1, line 52 | F-MINOR-1: printed `C″(K)=K⁻¹e^{−2k}(c″−c′)` (off by e^{−k}) | `C″(K)=K⁻¹e^{−k}(c″−c′)`; the same symbol fixed in `stage4/response-to-reviewers.md:95` and `stage4/revision-log.md:31` | Numeric Black–Scholes check (F=100, K=60.6531, k=−0.5, σ√τ=0.2): c′=−0.6015586, c″=−0.5336438, c″−c′=0.0679148; printed form 0.0018461164 vs direct finite-difference C″(K) 0.0018461108, relative error 3.0×10⁻⁶. The v3.0 form yields 0.0030437 = e^{−k}× the correct value (ratio 1.6487). Condition c″−c′≥0, SC4 tightness, the −0.53/+0.07 numbers and the 39-row SC3 coding are unaffected |
| 2 | Appendix A.1 note, line 462 | F-MINOR-2: note called the de-duplicated union the "750-record retrieval set" | "…is the 430-record unique set reported in Table 1 (750 records were returned before de-duplication)" | Consistent with Table 1 (750 returned; 430 unique after de-duplication), §3.1 (line 98), Figure 2 flow (line 123) and the A.2 arithmetic (line 466: 389 + 41 = 430). A repository-wide grep finds no remaining sentence that treats 750 as the post-de-duplication total; the only other "750" statements are the returned count |
| 3 | Run root | C4 condition (1) unmet: no declaration | `experiment-intake-declaration.json` (schema `experiment-intake-declaration/1.0`): `status: no_experiments_declared`, `declared_by: run operator (unattended e2e preauthorization)`, `declared_at: 2026-11-23`, `basis` present | C4 condition (1) closes: the declaration is present with the three required fields, no `experiment_provenance[]` exists (conditions 2–3 n/a), no own-experiment prose exists (condition 4 not met; re-checked: 0 first-person experiment verbs in v3.1), status is not `legacy_unknown` (condition 5 not met). EP-INV-5 lint note: `scripts/check_claim_audit_consistency.py:900` requires `declared_by == "scholar"`, so this artifact would be flagged by the lint (NOTE-8) |

Structure of v3.1 is unchanged from v3.0: 112 inline `<!--ref:ID-->` markers, 41 distinct IDs (sequence byte-identical), 112 anchors, 41 reference entries with 41 distinct DOIs, 11 preprint tags, 6 tables, 2 figures.

## 2. Scripts run (round 2)

All with the fork venv (`/Volumes/ExternalSSD/projects/dsh-academic-research-skills/fork/.venv/bin/python`), from the run directory; artifacts in `stage4.5-artifacts/round2/`.

| Script / command | Output | Exit | sha256 (first 16) |
|---|---|---|---|
| `round2/build_claim_registry.py stage4-prime/paper-draft-v3.1.md …` | `claim-registry.json` (202 claims) | 0 | `ccc31431f4266d23` |
| `scripts/claim_registry_coverage.py --draft … --registry … --output …` | `claim-registry-coverage.json` | 0 | `fe2243c59a6b917e` |
| `scripts/claim_registry_coverage.py --draft … --registry … --validate-report …` | `claim-registry coverage replay: PASS` | 0 | — |
| `round2/build_evidence_rows.py` | `evidence-rows.json` (112 rows), `evidence-rows-summary.json`, `evidence-sources/` (38) | 0 | `0912f3ed012b8304` / `5bf057654cddb183` |
| `round2/phase_a.py` (live DOI resolution, 41 GETs) | `phase-a-doi-checks.json` | 0 | `385d69ffddd85250` |
| `round2/phase_bd.py` (paragraph diff, citations, 8-gram test) | `phase-bd-checks.json` | 0 | `37ba4206602265af` |
| `round2/phase_c_recompute.py` (ledger, retrieval, reliability) | `phase-c-checks.json` | 0 | `64b36b30fcc869ca` |
| `scripts/check_revision_token_conservation.py pair` ×2 | `token-conservation-v1.3-v3.1.json`, `-v2-v3.1.json` | 0 | `c8134fdb9f85f17c`, `d621deabaf15c4fc` |

## 3. Phase A — Reference integrity (fresh, all 41)

All 41 DOIs were re-resolved live (no cache) against `https://api.openalex.org/works/doi:<DOI>` on 2026-11-23.

| Check | Result |
|---|---|
| HTTP status | 41/41 = 200 |
| Retraction flag (`is_retracted`) | 41/41 false (0 retracted) |
| DOI echo | 41/41 match the reference entry |
| Title | 41/41 normalized-equal; one display variant: R6 OpenAlex "SANOS Smooth strictly arbitrage-free non-parametric option surfaces" vs entry "SANOS: Smooth …" (colon dropped, not a bibliographic error) |
| Year | 41/41 match |
| First author | 41/41 surname match under the surname-token rule; display-form variants R7 "alvarez, robert jenkinson" and G6 "anagha s" are OpenAlex name-order forms, not mismatches |
| Listed ↔ cited ↔ corpus | 41 entries ↔ 112 markers / 41 IDs ↔ 41 corpus records, one-to-one; 0 dangling, 0 orphan, 0 unknown |
| Preprint tags | 11: P7, P8, N3, N5, N6, R2, R6, R7, R8, G6, C2 — matches the corpus convention |

**Verdict: PASS.** Disclosed limitation: no independent retraction-database sweep is possible from this environment; OpenAlex `is_retracted` is the only machine signal available.

## 4. Phase B — Citation context

| Check | Result |
|---|---|
| Body paragraphs (v3.1) | 79 |
| Paragraphs added or substantially modified v1.3 → v3.1 | 32 added + 39 substantially modified = 71 of 79 (89.9%), all audited (100% of the changed set) |
| Paragraphs unchanged v1.3 → v3.1 | 8 (byte-identical to v1.3; cross-checked in round 1) |
| v3.0 → v3.1 body edit | exactly 1 paragraph (§2.1, line 52); audited as changed by the round-2 delta rule (the similarity bucket calls it "unchanged" because the edit is ~0.5% of the paragraph's tokens) |
| Citation markers in body | 105 markers across 31 paragraphs (112 document-wide, 7 in appendix/captions) |
| Sensitive §2.1 paragraph | corrections verified; the five conditions SC1–SC5, the SC4-tightness argument and the Black–Scholes counterexample are unchanged and consistent with the corrected identity |
| Sensitive §5.1 paragraph | byte-identical to v3.0; partition 16+1+5+11+8 = 41 and 1+5 = 6 audit rows re-verified against Appendix B in round 1 and unchanged here |
| Overreach scan | all 59 citation-bearing claims re-checked or carried (see §7); no new overreach; NOTE-4 and NOTE-7 remain the two wording observations, neither false |

**Verdict: PASS WITH NOTES** (NOTE-4 G7 "explicitly disclaims"; NOTE-7 abstract pair-level comparability).

## 5. Phase C — Numbers and internal consistency

Every headline quantity was recomputed from the frozen ledger and logs on v3.1; all agree with the manuscript, the abstract, Tables 1–6, the appendices, the response letter and the revision log.

| # | Quantity | Stated / recomputed |
|---|---|---|
| 1 | Sources | 41 / 41 (36 in-window + 5 seminal) |
| 2 | Composition | 29 peer-reviewed + 11 preprints (26.83%) + 1 practitioner |
| 3 | Abstract coverage | 34 full / 4 partial (R2, G3, C4, S1) / 3 metadata-only (P4, P7, R4) |
| 4 | Evidence status | 17 proof / 16 test / 8 assumption; in-window 16/14/6; seminal 1/2/2 |
| 5 | Audit partition | 16+1+5+11+8 = 41; 1+5 = 6 audit rows (N2, N6, R5, R7, G5, G6); ∩proof = G6 |
| 6 | Time / dynamic | 10 time rows (P8, R8, G1, G2, G3, G7, C2, C3, C5, S5); D0 34 / D1 4 / D2 3 / D3 0 |
| 7 | Comparability | 0 direct / 30 context / 11 not comparable; every Table 3/Table 5 cell |
| 8 | Families | P8 N6 R9 G8 C5 S5; 31 construction rows (8+6+9+8) |
| 9 | Retrieval | 775 requested (31×25) / 750 returned / 430 unique / 389 excluded (141+86+40+34+32+31+21+4) / 41 included; 21 first-pass 429s, 20 recovered, 1 lost |
| 10 | Queries / exclusions | 31 strings in 8 groups (2+6+2+3+6+6+3+3); 40 discretionary exclusions (Table A2) |
| 11 | Reliability | 16-row sample, 96 cells, 79 agree (82.3%); family 12/16, evidence 10/16 (κ = 0.47), audit 15/16, time 16/16, dynamic 16/16, comparability 10/16; 17 adjudicated cells |
| 12 | Level | 40 Level VI / 1 Level VII (C2) |
| 13 | Body words | 7,761 (v3.1; §1 617 / §2 1153 / §3 1126 / §4 1198 / §5 1588 / §6 1303 / §7 776); v2 7,862; v1.3 7,641 |
| 14 | English abstract | 272 words (v3.1, unchanged); ZH 491 characters |
| 15 | Table A1 note | corrected: 430 unique, 750 returned before de-duplication — matches Table 1 |
| 16 | §2.1 identity | corrected prefactor; numerically verified to 3.0×10⁻⁶ relative error |

Abstract ↔ body: every abstract number and finding is stated in the body; the only abstract-only formulation remains the pair-level comparability clause (NOTE-7, unchanged and not contradicted). Tables ↔ body ↔ appendices: Table 1, Table 2, Tables 3–6, Appendix B ledger and Appendix D.10 arithmetic all recompute; Table 6's "about" counts remain declared approximations (not machine-recomputable). Response letter: body 7,862 (v2) ✓, tables 6, figures 2, references 41 ✓, reliability figures ✓; its English-abstract "249 words" remains unreproducible (NOTE-1). Revision log: the §2.1 row now records the corrected identity; the §4 body count 7,784 remains stale (NOTE-2).

Token-conservation audit (not a verdict, per protocol): `conserved: false` for both pairs. v2 → v3.1: citations and protected terms unchanged; number deltas are the documented edits (removed duplicated §3.1 paragraph and the old note's "750-record" framing; added 29 and 12 from the D.10 tally fix, 430 from the corrected note, 3.4 from the new §3.4 heading). v1.3 → v3.1: rewrite-scale (111 numbers added, 18 removed; 19 citation strings re-anchored/renumbered; no protected-term change), with no unexplained loss.

**Verdict: PASS** — the two round-1 numeric defects are corrected and no new inconsistency was introduced.

## 6. Phase D — Originality

| Check | Result |
|---|---|
| Paragraphs graded | 79/79 (100% of body paragraphs) |
| Grades | ORIGINAL 79; PARAPHRASE 0; CLOSE_MATCH 0; VERBATIM 0 |
| Shared 8-gram test vs the 38 held abstracts | 0 paragraphs with any shared 8-gram; longest shared token run = 5 tokens (source N5, one paragraph) |
| Prior drafts | v3.1 body is v2's body minus one duplicated paragraph; 8 paragraphs are byte-identical to v1.3 — cross-draft overlap expected and not self-plagiarism (only earlier drafts of this same text exist) |

**Verdict: PASS.**

## 7. Phase E — Claim verification (Mode 2 = ALL)

Registry: `claim-registry/1.0` for the exact v3.1 raw bytes (`draft_raw_sha256` = `d05dd050…`); 202 claims = 169 coverage-detector candidates + 33 explicitly registered absence/count statements; every `selection_tier` = `ALL`; every span decodes byte-exactly; schema validation PASS. Coverage sidecar: `candidate_unregistered_count: 0`; all 169 candidates `registry_span_matched`; `mixed_or_partial_registry_coverage` absent; 33 registered claims outside the detector classes; `semantic_extraction_coverage: not_machine_detectable`. The `--validate-report` replay prints `PASS`.

Only one registered claim's bytes changed between v3.0 and v3.1: CLM-X31 (§2.1 derivation, no cited source; its formula is verified in §5). Claims whose containing paragraph changed were re-audited even where their own span was unchanged.

Evidence rows (`evidence-rows.json`, schema `evidence-row/1.0`): 112 rows covering 59 citation-bearing claims and all 41 slugs; the remaining 143 registered claims are the review's own coding/ledger statements, verified in Phase C against the frozen ledger (no registered claim is unaudited).

| Level | VERIFIED | MINOR_DISTORTION | MAJOR_DISTORTION | UNVERIFIABLE | UNVERIFIABLE_ACCESS |
|---|---|---|---|---|---|
| Rows (112) | 109 | 0 | 0 | 0 | 3 |
| Claims (59) | 56 | 0 | 0 | 0 | 3 |

Freshly checked in round 2: 3 rows — CLM-008 × {G6, P2, S1}, the five-condition sentence inside the edited §2.1 paragraph (claim text unchanged; re-audited against the abstracts). Carried with explicit `carried_from` detail: 106 rows from round 1 (unchanged span text, refs and containing paragraph); the 3 UNVERIFIABLE_ACCESS rows are CLM-034/P4, CLM-036/P7, CLM-049/R4 (metadata-only records whose reference entries pin the version by DOI, so the label names that version rather than "version not identified").

**Verdict: PASS WITH NOTES** (3 UNVERIFIABLE_ACCESS notes; 0 MINOR/MAJOR_DISTORTION, 0 UNVERIFIABLE).

## 8. Delta from round 1

| Item | Round 1 | Round 2 |
|---|---|---|
| Target | v3.0 (`090a5992…`) | v3.1 (`d05dd050…`) |
| F-MINOR-1 (prefactor) | open | **resolved** — v3.1 line 52, response letter line 95, revision-log line 31; numerically verified |
| F-MINOR-2 (Table A1 note) | open | **resolved** — line 462 now 430 unique / 750 returned; consistent with Table 1, §3.1, Figure 2, A.2 |
| C4 condition (1) | formally unmet (no declaration) | **closed** — declaration persisted (status, declared_by, declared_at, basis); EP-INV-5 lint note added (NOTE-8) |
| Issues | 2 MINOR | 0 (0 SERIOUS, 0 MEDIUM, 0 MINOR, 0 MAJOR_DISTORTION, 0 UNVERIFIABLE) |
| Notes | NOTE-1…NOTE-7 | NOTE-1…NOTE-8 (NOTE-6 front-matter v2.0 persists; NOTE-8 new, non-blocking) |
| Verdict | FAIL | **PASS WITH NOTES** |
| Gate | NOT MET | **MET** |

## 9. Seven-mode AI-failure checklist

| Mode | Evidence | Verdict |
|---|---|---|
| 1. Implementation bug passing self-review | Declaration persisted: `status: no_experiments_declared`, declared_by/declared_at recorded; no implementation or executed experiment; Methods describe a literature search/screening procedure only | NOT APPLICABLE (declaration present — the round-1 limitation is closed) |
| 2. Hallucinated citation | 41/41 DOIs re-resolved live in round 2, 0 retracted, 0 dangling, 0 orphan; corpus one-to-one; marker sequence byte-identical | CLEAR |
| 3. Hallucinated experimental result | No experiments; every number recomputed from the run's own frozen logs on v3.1; no results attributed to the author | NOT APPLICABLE |
| 4. Shortcut reliance | Declared: abstract-level evidence, single database, 16-row recheck, title-level pool audit, single analyst; no undisclosed shortcut is presented as verified | CLEAR |
| 5. Implementation bug reframed as novel insight | No implementation, no bug-to-insight narrative | NOT APPLICABLE |
| 6. Methodology fabrication | No experiment run; every Methods number (31, 775/750/430/389/41, 16-row sample, 79/96) appears in the frozen records | NOT APPLICABLE |
| 7. Frame-lock at an early stage | Frame revised under R1/R2; claims explicitly bounded; §7.2 states falsifiable consequences | CLEAR |

No mode is SUSPECTED. The round-1 SUSPECTED-free status is preserved; the basis for NOT APPLICABLE now includes the persisted declaration rather than resting on the run brief alone.

## 10. Issues and notes

No issue is open: 0 SERIOUS, 0 MEDIUM, 0 MINOR, 0 MAJOR_DISTORTION, 0 UNVERIFIABLE. The round-1 corrections were re-verified against the new bytes and introduced no new inconsistency (checked: the §2.1 derivation, its downstream sentences, Appendix C.4, the abstract, Table A1 and its note, Table 1/Figure 2/A.2 arithmetic, the response letter and the revision log).

Notes (non-blocking; notes never gate):

| ID | Location | Finding | Fix |
|---|---|---|---|
| NOTE-1 | `stage4/response-to-reviewers.md:19` | English abstract stated as 249 words (limit 150–250); measured 272 (v3.1) / 259 (v2) / 231 (v1.3), so 249 is unreproducible and v3.1 exceeds the stated 250-word cap | Restate the measured count; trim if the 250-word limit is real |
| NOTE-2 | `stage4/revision-log.md:5, :70` | v2 body recorded as 7,784 with per-section 617/1153/1229/1170/1536/1303/776; measured v2 is 7,862 (617/1153/1227/1198/1588/1303/776), and the log's own Stage 4′ table says 7,862 → 7,761 | Restate the v2 count and section split |
| NOTE-3 | Abstract; §7.1 line 344 | Four certified-object kinds enumerated; §2.3 line 70 adds the fifth ("or … the class itself"; Table 2 inherited class, rows G1/G7/G8) | Add the class variant to the abstract and §7.1 enumerations |
| NOTE-4 | §4.4 line 210; §6.2 line 316; Appendix C.5 line 581 | Describes the G7 row as "explicitly disclaims" a dynamic guarantee; the held G7 abstract only says the state space is free from static (or model-independent) arbitrage | Tighten to "guarantees only static admissibility" or cite the paper's limitation |
| NOTE-5 | §3.1 line 100 | Elliptical "and a foreign-exchange delta-condition paper by Fukasawa (2022)" reads as if Fukasawa wrote the FX paper; A.3 shows the FX record was displaced and replaced by Fukasawa's equity-index asymptotics paper | Copyedit the sentence |
| NOTE-6 | Front matter line 5 | "**Version:** v2.0" while the object is v3.1 (round 2) | Relabel the version |
| NOTE-7 | Abstract EN line 12, ZH line 20 | "no two sources state data, metric and tolerance together" is a pair-level compression of §5.4's "one row states a tolerance and a loss together (G6)" and §5.2's four-field finding; no body sentence states the joint count | Mirror §5.2's four-field wording in the abstract, or add the joint count |
| NOTE-8 | `experiment-intake-declaration.json` | `declared_by: "run operator (unattended e2e preauthorization)"`; C4 condition (1) needs presence only, but the claim-audit lint EP-INV-5 (`scripts/check_claim_audit_consistency.py:900`) requires the literal value `scholar` | Set `declared_by: "scholar"` (the preauthorization is recorded in the run log) or record an explicit lint waiver at the Stage 5 entry checkpoint |

## 11. Advisories (advisory only — never gate)

| ID | Kind | Result |
|---|---|---|
| ADV-E4-1 | Scope-absence (E4) | No broadening: scope = equity-index listed options, 2015-01-01–2026-11-23, English, OpenAlex only, public metadata/abstracts, 5 declared seminal precursors |
| ADV-E5-1 | Novelty (E5) | §6.2 absence claim is SUPPORTED_WITHIN_SEARCH: wording is search-bounded ("to our knowledge"), databases and window match the documented strategy, the search date is recorded in `run-log.md:3` and §6.2, and the nearest prior work (Niu 2015) is acknowledged. Not a global-novelty claim. `search/retrieval_log.json` carries no machine `last_searched_at`, so the date is evidenced by the run log/manuscript |
| ADV-CACHE | Cache reuse | Not applicable — no cached research artifacts were consumed |
| E6 | Claim-strength drift | `[E6-SKIPPED: no revision evidence]` — no patch bundle, no patch sidecars, no Schema 7 roadmap (same #670 gap as `run-log.md`); artifact status `skipped_no_revision_evidence`, null bundle hash, empty findings |

## 12. Determinism and replay

Registry rebuild from the same v3.1 bytes is byte-identical (`ccc31431…`); the coverage rerun is byte-identical (`fe2243c5…`) and the replay validator prints PASS. Evidence rows reproduce all claim, verdict, excerpt and source fields byte-identically; only the runtime `captured_at` (UTC) and the dependent `row_sha256` differ between invocations. Phase A is live: a replay at another time may return updated OpenAlex metadata, so `round2/phase-a-doi-checks.json` is part of the record. Phase B/D and C scripts are pure functions of the frozen files. Carry is explicit in each row's `detail` text (`carried_from: stage4.5-integrity.md (round 1)`), not implicit.

## 13. Verdict rationale

The ladder (protocol lines 689–693) gives PASS at zero SERIOUS + zero MEDIUM + zero MAJOR_DISTORTION + zero UNVERIFIABLE; PASS WITH NOTES at those zeros plus only MINOR/MINOR_DISTORTION/notes; FAIL at any SERIOUS, MEDIUM, MAJOR_DISTORTION or UNVERIFIABLE (and at Stage 4.5 also any MINOR). Round 2 has **zero issues** at every level and eight notes, all non-blocking. "At Stage 4.5, PASS WITH NOTES carries notes only and clears the gate" (line 693), so the terminal PASS condition is met. The fail loop closes at round 2 of the permitted 3; no third round is needed. The two round-1 MINOR items were corrected in the certified object and re-verified numerically/exegetically, and the C4 declaration condition is now satisfied.

**Gate to Stage 5: MET.** The terminal PASS condition (zero issues at Stage 4.5) is satisfied by PASS WITH NOTES: 0 SERIOUS, 0 MEDIUM, 0 MINOR, 0 MAJOR_DISTORTION, 0 UNVERIFIABLE, with seven prior notes and NOTE-8 recorded. The certified object is `stage4-prime/paper-draft-v3.1.md` at sha256 `d05dd0508ef7ff38eea4f319a0a9883f76a94cd762939d8cc68263e805431009`; any further edit creates a new object requiring a new registry binding and a new Stage 4.5 check. Remaining non-blocking items: NOTE-1…NOTE-8 (documentation/copyediting, and the EP-INV-5 declaration-label lint), plus the Stage 5 entry advisories (#660, #672) which belong to the next checkpoint, not this stage.
