# Phase 5 — Ethics Review

**Manuscript:** Arbitrage-Free Implied Volatility Surface Construction: A Structured Literature Review of Parametric, Nonparametric, and Neural Approaches  
**Reviewer role:** Ethics Review Agent (AI-assisted research integrity; not an IRB)  
**Date:** 2026-11-19  
**Input:** `phase4-report.md` (Phase 4 draft)

## Ethics Review Report

### AI-Assisted Research-Integrity Verdict: CONDITIONAL

**Scope:** This verdict covers AI-assisted research integrity only. It is not human-subjects clearance, authorization, or an institutional determination.

### Dimension Assessment

| Dimension | Status | Notes |
|-----------|--------|-------|
| AI Disclosure | warn | Disclosure is present with the required pipeline language, but “All findings were verified against cited sources” overstates an abstract-level review. Add a metadata/abstract qualifier. |
| Attribution Integrity | warn | 40 references; 20/40 (50%) metadata spot-checked; 0 title/author/year/DOI mismatches; no fabricated reference. One claim-use concern: Horvath et al. (2021) is cited for calibration speed while the record is title-level only. |
| Dual-Use Screening | pass | Risk Level: Low. The review is a literature map; it provides no operational trading, calibration, or exploit recipe. No Responsible Use statement required. |
| Fair Representation | pass | The corpus is SPX/US-equity-index heavy, and the manuscript discloses this in §5.4 and §4.6. No vulnerable populations, stigmatization, or contested community representation issues. |
| Data Ethics | pass | Public metadata and abstracts only; no personal data, no human-subjects data, no identifiable records, no data collection. |
| Conflict of Interest | warn | No funding or COI statement was retrieved from the sources or supplied for the review. The limitation is disclosed; add an explicit funding/COI line. |
| Human Subjects Ethics | see separate status | No human-subjects activity. The administrative fields below are reported for completeness, not as a readiness finding. |

### Human-Subjects Administrative Status

| Field | Value |
|-------|-------|
| submission_readiness | no_listed_gaps_located |
| authorization_status | not_provided |
| review_pathway | institutional determination required |
| authority_context | unavailable — no human-subjects authority context supplied |
| profile_dependent_result_allowed | false |
| candidate rule trace | unavailable — no validated trace |
| applicable consent/information requirement IDs | unavailable — no human-subjects authority selection |
| actor and consumer scope per requirement | n/a — no human-subjects activity |
| requirement and authority-anchor pointers | n/a — no human-subjects activity |

These fields are independent: submission readiness must never update authorization status. `no_listed_gaps_located` is not approval, clearance, or evidence that any human-subjects activity may begin. The manuscript reports no human-subjects activity; the unresolved authority context is therefore not a readiness gap for this review.

### Issues Found

#### Critical (Blocks Delivery)

No critical issues. No fabricated reference, no missing AI disclosure, no plagiarism detected in sampled text, no systematic source misrepresentation, and no harm-enabling operational detail.

#### Conditional (Must Fix)

1. **AI disclosure scope.** The disclosure says “All findings were verified against cited sources.” The review is metadata/abstract-level; full texts were not read. Add: “Verification was performed at the metadata/abstract level; full-text verification and a full conflict-of-interest audit were not performed.” Keep the required disclosure sentence; add the qualifier rather than replacing it.
2. **Horvath et al. (2021) citation use.** The record is title-level only in this review, but it is cited in §2.3 and §4.3 for reduced calibration time. Remove it from those speed claims or label it explicitly as a title-level record that is not used as substantive evidence. The manuscript already says in §4.4 that it is title-level; make the rest consistent.

#### Advisory (Recommended)

- Add a funding/COI line: “Funding: none. Conflict of interest: none declared. A full COI audit was not possible from the retrieved metadata.”
- Keep the SPX/US concentration caveat in §5.4 and §4.6; consider adding it to the abstract as a one-clause scope note.
- State explicitly that no plagiarism scan and no full-text claim verification were performed; the current limitations imply this but do not name the plagiarism check.

### AI Disclosure Verification

- [x] Disclosure statement present: Yes.
- [ ] Scope accurate: No — the “All findings were verified” sentence needs the metadata/abstract qualifier.
- [x] Limitations noted: Yes — §5.4.

### Reference Integrity Check

- Total references cited: 40.
- Spot-checked: 20 / 40 (50%), at title/author/year/venue/DOI level against the Phase 2 verification matrix.
- Issues found:
  - 0 metadata mismatches (title, author, year, venue, DOI).
  - 0 fabricated references; 0 retracted records flagged.
  - 1 claim-support concern: Horvath et al. (2021) used for calibration speed despite title-level-only status.
  - No full-text claim verification; no plagiarism scan; no retraction-authority query beyond the Phase 2 metadata check.

### Responsible Use Statement

Not required. Dual-use risk is Low: the manuscript synthesizes public research on implied-volatility surface construction and does not provide operational trading instructions, proprietary data, exploit code, or harm-enabling specifics.

### Ethics Clearance Notes

This is a no-human-subjects, public-metadata review. The two conditions are transparency and citation-use fixes, not integrity failures. If the Phase 6 revision adds the disclosure qualifier, fixes the Horvath citation use, and adds the funding/COI line, the integrity verdict can move to CLEARED. The residual limits — abstract-level evidence, 10 preprints, no full-text, no COI audit — should remain in the report’s limitations rather than being presented as resolved.

### Ethics Decision Log

| Item | Verdict | User decision | Reasoning |
|------|---------|---------------|-----------|
| AI disclosure scope | CONDITIONAL | pending Phase 6 | Add metadata/abstract qualifier; required disclosure sentence retained. |
| Horvath et al. (2021) citation use | CONDITIONAL | pending Phase 6 | Remove from calibration-speed claims or label title-level and non-substantive. |
| Funding/COI statement | advisory | pending Phase 6 | Add explicit “none declared; full audit not possible” line. |

> **Human-subjects boundary:** This output does not authorize recruitment, consent, access to identifiable data, intervention, or data collection.

---

**Phase 5 note:** This ethics review is one of three parallel Phase 5 inputs. The editorial review and Devil's Advocate checkpoint 3 are separate artifacts; their findings should be combined in Phase 6.
