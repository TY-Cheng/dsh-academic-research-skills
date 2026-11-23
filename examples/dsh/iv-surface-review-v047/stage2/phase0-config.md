# Phase 0 — Paper Configuration Record

**Run:** `iv-surface-review-v047` · **Pipeline stage:** 2 (WRITE) · **Skill:** `academic-paper` v3.24.4, `full` mode, Mode A (orchestrator-driven)
**Phases in this artifact set:** 0–3 · **Date:** 2026-11-23 · **Mode:** unattended end-to-end validation run; operator preauthorized the checkpoints.
**Author:** TY-Cheng (Independent Researcher) · **Co-authors:** none.

> Status: frozen. The record below is the configuration baseline for Phases 1–3. No checkpoint prompt was issued: the operator's `确认` instruction covers the Phase 0 confirmation and the Phase 2 outline approval for this unattended run.

## 1. Paper Configuration Record

| Field | Value |
|---|---|
| Topic | Static and dynamic no-arbitrage enforcement in the construction of equity-index implied-volatility surfaces |
| Research Question | How do parametric construction, penalty, projection–repair, and generation–filtering methods for constructing equity-index implied-volatility surfaces enforce static and dynamic no-arbitrage constraints? |
| Sub-questions | **SQ1:** Which static conditions does each family enforce, by what mechanism, and at what evidence status (proof / numerical test / assumption)? **SQ2:** Which dynamic requirements are addressed, enforced, or merely tested? **SQ3:** What trade-offs appear across the review's evaluation dimensions? |
| Paper Type | Structured, corpus-scoped literature review with a framework contribution |
| Structure Type | `literature_review` (Schema-4 enum; reads the **Standard** abstract regime row) |
| Discipline | Finance / quantitative finance — derivatives, implied volatility |
| Target Journal | None specified. Target type: general academic journal / arXiv-style preprint |
| Venue Profile | Not declared. No author-confirmed venue metadata was supplied |
| Review Target Context | **Absent** — no target review, track, or article type confirmed. `criteria_binding_unavailable` (see §5) |
| Citation Format | APA 7.0 |
| Output Format | Markdown (Phase 7 format conversion deferred to pipeline Stage 5) |
| Format Profile | None — Markdown-only; intake Step 5 format profile skipped |
| Body Language | English |
| Abstract | Bilingual: English + Simplified Chinese. Standard regime: English 150–250 words; Chinese 300–500 characters (CJK count); 5–7 keywords per language |
| Output Language Pair | Requested: English + Simplified Chinese (`zh-Hans`). This is **not** a v3.24.4 registry token: the shipped registry carries `zh-tw-en` only. Recorded as a visible registry mismatch, not silently normalized to `zh-tw-en` and not converted to Traditional Chinese (see §8, finding V1) |
| Word Count Target | 7,400 body words |
| Word Ceiling | 8,000 body words (operator-declared upper bound; hard ceiling) |
| Existing Materials | Frozen Stage 1 records and the 41-source corpus (see §3); no new search, no new references |
| Corpus | 41 sources: 36 in-window 2015–2026 + 5 declared seminal precursors 1999–2014; 29 peer-reviewed, 11 preprints (26.8%), 1 practitioner magazine; frozen `search/selected_sources.json` |
| Style Profile | Not calibrated (optional Step 10 skipped; no sample supplied) |
| Domain Evidence Profile | `unknown_user_defined` — neutral default; no scholar-confirmed profile. The operator did not select a profile and finance / q-fin is not one of the four ship-ready values. No gate was loosened; the corpus is frozen, so the profile has no effect on inclusion in this run |
| Citation Verification | `advisory (mark only, default)`. Stage 1 resolved 41/41 DOIs; no further verification planned |
| Retraction Policy | `advisory (mark only, default)`. Stage 1 checked OpenAlex `is_retracted`; 0 retracted records |
| Operational Mode | `full`, Mode A. This task executes Phases 0–3 only; Phases 4–6 are not executed here |
| Funding | None |
| Conflict of Interest | None declared |
| Human Subjects | None — no human participants; public bibliographic records only |
| AI Use | Disclosed; bounded wording planned for Phase 4 (see §7) |
| Data Availability | Stage 1 corpus and coding records in the run directory; no new data were generated |
| Ethics / Dual Use | No ethics approval required. Dual-use Level None: no code, data, or implementable procedure; no deployment ranking; not advice |
| Retraction Check Result | 41/41 DOI resolution; 0 retracted; no independent retraction-database sweep |
| Prohibited Claims | No method ranking or league table; no PRISMA/PRISMA-ScR claim; no new sources; no venue-alignment claim; no field-wide absence claim from a corpus-scoped absence; no claim that a numerical test is a proof |

**Derivation notes.** The paper type fixes the abstract regime (Standard row) and the structure pattern (thematic literature review, adapted with a method section). The absence of a target venue fixes the review-criteria status at `criteria_binding_unavailable`; no `ReviewTargetContext` was invented from model memory. The word target is the midpoint of the operator's 6,000–8,000 range; section budgets sum to it exactly. Citation verification and retraction policy remain at their default advisory settings; Stage 1 already performed the checks, and no strict policy was requested.

## 2. Scope Statement

**In scope.** Equity-index listed options; construction and enforcement of implied-volatility or option-price surfaces; static no-arbitrage (strike convexity / butterfly, monotonicity of total variance in maturity) and dynamic no-arbitrage (process-level consistency of a surface family over calendar time); four focal method families (parametric construction, penalty / constrained learning, projection–repair, generation–filtering) plus two supporting groups (conditions / evaluation; seminal baselines); evidence status, comparability, and evaluation coverage; a proposed enforcement framework and a research agenda.

**Out of scope.** New literature search or new references; pricing-only, forecasting, hedging, or trading studies except where a source's own evaluation is reported; market-microstructure questions; FX, rates, commodities, energy, crypto, and single-name panels (one disclosed exception: C5's single-stock panel, retained with a scope flag); re-derivation of proofs, recomputation of reported numbers, or full-text retrieval; meta-analysis, effect sizes, vote counting, or any ranking of methods; PRISMA or PRISMA-ScR conformity; venue-fit or submission-readiness claims.

## 3. Handoff from Stage 1

The Stage 1 report is the authoritative claim source. Phase 1–3 artifacts may restate its claims and counts; they may not add evidence.

| Stage 1 artifact | Path | What this stage uses |
|---|---|---|
| Scoping record | `../phase1-scoping.md` | RQ, sub-questions, H1–H3, scope, frozen four-family taxonomy, evidence-status rules, DN/DA checkpoints, #921 record |
| Annotated bibliography | `../phase2-bibliography.md` | Search strategy, 31 queries, screening counts, annotated entries, evidence ledger, comparability flags |
| Verification report | `../phase2-verification.md` | DOI and retraction results, abstract coverage, A/B/C quality matrix, cross-source checks, flags |
| Synthesis report | `../phase3-synthesis.md` | 41-row evidence matrix, seven themes, eight tensions, seven gaps, proposed framework, seven-dimension matrix, DA Checkpoint 2 |
| Final Stage 1 report | `../phase6-final.md` | Final claims, structure, tables, numbers, limitations, declarations, 41 APA references — **primary trace target** |
| Revision log | `../phase6-revision-log.md` | 55 review items: 50 fixed, 4 partly fixed, 1 pushback; residual limitations |
| Machine-readable corpus | `../search/selected_sources.json` | 41 records: family, evidence status, constraints, key finding, comparability, flags, DOI |
| Screening provenance | `../search/screening_log.json`, `../search/openalex_candidates.json` | Reason-coded exclusions and candidate pool (read-only) |
| Run log | `../run-log.md` | Environment facts (Python, LaTeX present; pandoc absent), repo commit `19f11de` |

**Corpus constants carried unchanged.** 41 sources; 8 parametric / 6 penalty / 9 repair / 8 generation / 5 conditions / 5 seminal. Evidence status 17 proof / 16 test / 8 assumption; in-window 16 / 14 / 6; seminal 1 / 2 / 2. Abstract coverage 34 full / 4 partial (R2, G3, C4, S1) / 3 metadata-only (P4, P7, R4). Overall quality grades A 11 / B 13 / C 17 (quality labels, not performance ranks). Comparability 0 direct / 30 context / 11 not comparable. Dynamic no-arbitrage: 0 of 41 enforce or test; 10 rows engage time; 0 of 31 construction rows. Proof-and-audit overlap: G6 only, on synthetic data. Five cross-source clusters cover 19 sources; no claim independently replicated. No PRISMA claim.

**Word-count convention.** Stage 1 reports **5,596 body words** under its stated convention (Abstract → Responsible Use Statement, excluding headings, citation markers, references, tables, and appendices). The file is 8,542 whitespace-split words including references, tables, and appendices. The Stage 2 outline uses the body-word convention for its 7,400-word target and excludes the abstract, tables, figures, references, declarations, and appendices.

## 4. Review-Target Criteria Binding Status

```text
criteria_binding_unavailable
```

No author-confirmed `ReviewTargetContext` exists: no target journal, track, article type, or venue selection was supplied. Consequently:

- no `ReviewCriteriaBindingManifest` was initialized and no target review id exists;
- Phase 2 does **not** issue a FORMATIVE receipt and does not map criterion ids to planned sections;
- Phase 6a's INTERNAL receipt is not applicable in this task;
- this paper makes **no venue-alignment or submission-readiness claim**, and its review-criteria coverage is non-comparable to a venue-bound review;
- the status is carried verbatim into `phase2-outline.md` and `phase3-argument.md`; it is not reconstructed, replaced, or silently treated as satisfied.

## 5. Checkpoint Record

| Checkpoint | Rule | Status for this run | Record |
|---|---|---|---|
| Phase 0 → 1: user confirms PCR | SKILL.md Checkpoint Rule 1 (IRON RULE) | Satisfied by preauthorization | Operator preauthorized the pipeline; token `确认`; no interactive prompt issued |
| Phase 2 → 3: user approves outline | SKILL.md Checkpoint Rule 2 | Satisfied by preauthorization | Same `确认`; no restructuring requested; outline approval recorded in `phase2-outline.md` §11 |
| Phase 6 revision loops (max 2) | SKILL.md Checkpoint Rule 3 | Not reached (Phases 4–6 out of scope) | n/a |
| Phase 6 → 7 gating (#1087) | SKILL.md Checkpoint Rule 6 | Not reached | n/a |
| #921 review-form note | SKILL.md #921 block | Already answered in Stage 1 | Not re-shown; Stage 1 records the operator reply `确认` (continue current work; no separate review form; no PRISMA claim) |

## 6. Declarations and Compliance Plan

The drafted paper must include the mandatory declarations (IRON RULE): Data Availability Statement; Ethics Declaration; Author Contributions (CRediT); Conflict of Interest Statement; Funding Acknowledgment; AI-use disclosure; Limitations section. Where not applicable, state "not applicable" rather than omitting the item.

- **Ethics:** no human subjects, no animal subjects, no personal data; no ethics approval required.
- **Author contributions:** sole author; planned CRediT roles are Conceptualization, Methodology, Investigation, Data Curation, Writing – original draft, Writing – review & editing, Visualization. Final wording at Phase 4.
- **Funding:** none.
- **COI:** none declared.
- **Data availability:** the 41-source corpus and coding records are in the run directory; no new empirical data. Reported numbers are drawn from the frozen Stage 1 records.
- **AI use:** disclosed at Phase 4 with the bounded Stage 1 wording: ARS v3.24.4 pipeline; Claude-family agent operating within DeepSeek Harness (DSH) on 2026-11-23; exact model identifier/version not recorded in the run log; AI assistance covered search, screening, coding, synthesis, and drafting support; verification was limited to 41/41 DOI resolution and OpenAlex retraction flags — no theorem was checked and no reported number recomputed; screening and coding were single-analyst; human role was run authorization and checkpoint review. No claim of "all findings verified" or "human oversight throughout" is permitted.
- **Responsible use:** dual-use Level None; no code, data, or implementable procedure; no deployment ranking; not investment advice.

## 7. Validation Findings (for the end-to-end run record)

These are recorded because this is a validation run; none changes the Stage 2 deliverables.

1. **V1 — output-language registry mismatch.** The operator requested English + Simplified Chinese abstracts. The v3.24.4 registry (`shared/output_language_pair.md`) carries only `zh-tw-en` (Traditional Chinese L1 + English L2), and its contract says an unregistered token is a visible failure, not a silent fallback. This record preserves the author's declared languages (`en` + `zh-Hans`), applies the Standard CJK abstract regime (300–500 characters, 5–7 keywords), and flags the pair as unregistered. It does **not** substitute Traditional Chinese.
2. **V2 — no review target.** `criteria_binding_unavailable` is the intended degraded path, not an omission. No venue alignment is claimed.
3. **V3 — format conversion unavailable in this environment.** Stage 1's run log records that `pandoc` is not installed (DOCX conversion unavailable); `xelatex`/`pdflatex` are present. Phase 7 at pipeline Stage 5 must resolve the DOCX route or disclose its absence.
4. **V4 — skill provenance.** The installed plugin 0.4.6 is stale; this run reads the vendored v3.24.4 skill and agent files in the `fork` checkout (commit `19f11de`). The vendored text is authoritative.
5. **V5 — Stage 1 residuals carried forward.** Abstract-level only (34 full / 4 partial / 3 metadata-only); 11 preprints; single coder; English-only, OpenAlex-only retrieval; US-index dominance (10 of 12 known-provenance rows); one query lost after HTTP 429; no full text or proof check; no ranking; no PRISMA claim. These are disclosed in the paper's Limitations, not repaired.

## 8. Freeze and Handoff

Phase 0 is frozen. Phase 1 proceeds from the frozen corpus, with no external search and no source additions. The Phase 1 artifact is an evidence map and allocation, not a new literature search. Phase 2 inherits the seven-section structure and the `criteria_binding_unavailable` status. Phase 3 inherits the approved outline and may not add evidence.
