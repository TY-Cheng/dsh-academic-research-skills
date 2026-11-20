# DSH Academic Pipeline — End-to-End Evidence

**Plugin:** `dsh-academic-research-skills` v0.3.0 (full ARS v3.24.2 content parity)  
**Platform:** DSH desktop profile, `/Users/tycheng/.dsh/profiles/desktop/node_modules/dsh-academic-research-skills`  
**Date:** 2026-11-19 (Asia/Singapore)  
**Author/operator:** TY-Cheng  
**Purpose:** run the complete `academic-pipeline` on one real topic and record the evidence for a future official sibling-distribution submission. This is an e2e test, not a claim of official endorsement.

## Result

A 40-source structured literature review on arbitrage-free implied volatility surface construction, carried from research question to a 6,804-word final paper with 40 references, 8 tables, and five appendices.

**Final paper:** [`stage5/paper-final.md`](stage5/paper-final.md) · [PDF](stage5/paper-final.pdf) · [DOCX](stage5/paper-final.docx) · [LaTeX](stage5/paper-final.tex)

The paper is corpus-scoped. It does not rank methods, does not claim a universal benchmark, and does not make a regulatory determination. The review contributes a four-family enforcement taxonomy (construction, penalty, projection/repair, generation/filtering) and a seven-dimension evaluation matrix; both are proposed, not validated.

## Pipeline verdicts

| Stage | Artifact | Verdict |
|---|---|---|
| 1. Deep research | `phase1-scoping.md` … `phase6-final.md` | Phase 6 final; 5,341-word Stage 1 report |
| 2. Academic paper | `stage2/` | Internal peer review: Major Revision → v1.2 (6,315 words) |
| 2.5 Integrity | `stage2.5-integrity.md` | PASS, bounded coverage; 5 advisories |
| 3. Review | `stage3/` | 5-seat panel + editorial: **Major Revision**; 6 major issues |
| 4. Revision | `stage4/paper-v2.md`, `stage4/response-to-reviewers.md` | 6,804 words; Appendix D/E; Tables 7/8 |
| 3′. Re-review | `stage3-prime/re-review.md` | **Minor Revision**; 2 copy-edits |
| 4′. Copy-edit | `stage4-prime/paper-v3.md` | Tables renumbered 1–8; year note |
| 4.5 Final integrity | `stage4.5-integrity.md` | **PASS**, bounded coverage; 7 advisories |
| 5. Finalize | `stage5/` | Final MD/DOCX/TeX/PDF; APA 7.0 used |
| 6. Process summary | — | Not run (author stopped at Stage 5) |

The user authorized the run through Stage 5 in advance. Both integrity checks and both reviews ran and are recorded. The bundle does not record separate user replies to the Stage 3 or Stage 3′ review decisions or to the Stage 5 entry gate (confirmation to proceed and citation-style choice), so those user checkpoints were not validated. Both integrity checks reported PASS; the path where the user decides what to do after three unsuccessful fix-and-recheck rounds was not exercised.

## What the e2e actually exercised

- **Full ARS content:** 5 skills, 16 commands, root `scripts/`, `shared/`, `agents/`, and `MODE_REGISTRY.md` were installed. The core Python tool layer was smoke-tested; the e2e workflow itself used the skills, the custom search scripts, and the format builder.
- **DSH adapter:** path note (`DSH_ARS_ROOT` / package root), 21 registrations, command generation, and Python execution via the profile-local `.venv`.
- **Deep research:** RQ Brief + methodology + DA checkpoint; OpenAlex discovery; abstract/DOI verification; synthesis; report compiler; editorial, ethics, and DA review; revision.
- **Academic paper:** config, outline, argument blueprint, draft, citation compliance, bilingual abstract, internal peer review; integrity; 5-seat review; revision; re-review; final integrity; format conversion.
- **Bounded coverage:** the review is abstract-level; 10 of 40 sources are preprints; one source is title-level; no full text, plagiarism scan, or full COI audit was possible.

## Corpus and evidence

- **Search:** 24 OpenAlex full-text queries on 2026-11-19; 25 records/query; 351 unique after DOI/title deduplication; 40 included after title/abstract screening.
- **Composition:** 30 peer-reviewed / 10 preprints; 7 parametric, 6 nonparametric, 18 neural/generative, 8 constraints/evaluation, 1 dynamics; 28 from 2021–2026, 12 earlier (including three seminal pre-2015 works).
- **Verification:** 40/40 OpenAlex records; 39 DOI + 1 HAL; 0 fabricated; 0 retracted per OpenAlex; 35 full abstracts, 4 partial, 1 title-level; 0 predatory venues identified.
- **No PRISMA claim.** The flow is PRISMA-style, not PRISMA-compliant; 311 non-advanced records were not individually coded. Appendix C discloses this.

## Artifact map

| Path | Contents |
|---|---|
| `phase1-scoping.md` | RQ Brief, methodology blueprint, DA checkpoint 1, review-form note |
| `phase2-bibliography.md`, `phase2-verification.md` | 40 annotated sources; quality matrix; verification |
| `phase3-synthesis.md` | 40-row matrix, 5 themes, 7 tensions, 6 gaps, DA checkpoint 2 |
| `phase4-report.md`, `phase5-*.md`, `phase6-final.md` | Stage 1 report through final report |
| `stage2/` | Config, outline, argument, citation/abstract checks, internal review, paper draft |
| `stage2.5-integrity.md` | Pre-review integrity pass |
| `stage3/` | Field analysis, five seat reviews, editorial decision, revision roadmap |
| `stage4/` | Paper v2, point-by-point response |
| `stage3-prime/re-review.md` | Verification re-review |
| `stage4-prime/` | Paper v3, copy-edit response |
| `stage4.5-integrity.md` | Fresh final integrity pass |
| `stage5/` | Final paper, formats, build script, format README |
| `search/` | OpenAlex search, selection, abstract fill, selected corpus JSON/Markdown |

## Reproduce

```bash
# 1. Verify the installed content and registrations
cd ~/.dsh/profiles/desktop/node_modules/dsh-academic-research-skills
npm run verify

# 2. Python tool layer (profile-local venv; not the bare system python)
.venv/bin/python scripts/check_pipeline_integrity.py --help
.venv/bin/python skills/sr-screener/scripts/prepare_records.py --help

# 3. Re-run discovery (open network; the 2026-11-19 corpus is frozen)
cd examples/dsh/iv-surface-review
python3 search/openalex_search.py
python3 search/fetch_selected.py

# 4. Rebuild final formats (bundled Python has python-docx; xelatex required)
/Users/tycheng/.dsh/dsh-runtimes/dsh-primary-runtime/dependencies/python/bin/python3 \
  stage5/build_formats.py
```

Pandoc is not installed in this environment; `stage5/build_formats.py` is a deterministic fallback, not a journal typesetter. The PDF is a working `ctex` + `xelatex` build (35 pages, letter); the DOCX is a structural conversion.

## Official-recognition relevance and limits

This directory is the **platform e2e evidence** the upstream `CONTRIBUTING.md` asks for: a complete `academic-pipeline` run on a real topic, with artifacts, verdicts, and disclosed limits. It does **not** by itself establish official sibling-distribution status.

The submission package is at [`docs/sibling-submission/`](../../../docs/sibling-submission/README.md): it contains the claims–evidence table, the model-portability note, the named-maintainer statement, and the design-issue record. The design issue is open at [#1126](https://github.com/Imbad0202/academic-research-skills/issues/1126); the recognition request is the next step after maintainer feedback. The binary-format question (link the PDF/DOCX or only Markdown + reports) is asked in the design issue.

The known limits are not hidden: abstract-level evidence, 10 preprints, one title-level source, no full-text verification, no plagiarism scan, no full COI audit, S2 rate-limited at search time, no dual screening, and 311 non-advanced records not individually coded. The paper and the integrity reports state each one.
