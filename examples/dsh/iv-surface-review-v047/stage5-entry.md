# Stage 5 Entry Gate (MANDATORY checkpoint)

**From:** Stage 4.5 PASS WITH NOTES, round 2 — `stage4.5-integrity-round2.md`
**Accepted draft:** `stage4-prime/paper-draft-v3.1.md`, sha256 `d05dd0508ef7ff38eea4f319a0a9883f76a94cd762939d8cc68263e805431009`, 7,761 body words
**Gate result:** proceed to Stage 5 (preauthorized for the unattended e2e — the operator preauthorized Stages 1–5 at the run start; recorded reply: continue).

## Finalization decisions recorded at this gate

- **Citation style:** APA 7.0 (decided at Phase 0, unchanged).
- **Requested outputs:** Markdown (always) + PDF through LaTeX. DOCX was requested conditional on Pandoc availability; Pandoc is not installed, so per ARS v3.24.4 the run records instructions instead of substituting a converter (see `stage5/README.md`). The `.tex` source is kept as the PDF build input.
- **Content confirmation:** deferred to the Stage 5 completion checkpoint inside Stage 5 execution, as the protocol specifies.

## Advisories bound to this exact draft (run #660 first, #672 second)

Both bind the identical accepted draft ID/sha (`d05dd050…`).

1. **#660 tortured-phrase advisory** — `stage5/artifacts/tortured-phrase-advisory.json`.
   Status `not_checked`, reason `SNAPSHOT_NOT_PROVIDED` (no curated phrase-list snapshot or detached manifest was supplied, and the path ships no native phrase list). Report layer `HEURISTIC-ADVISORY` / `UNMEASURED`; it neither changes the Stage 4.5 PASS nor blocks Stage 5.
2. **#672 cross-document consistency advisory** — contract/runtime failure, no artifact written: `ADVISORY_UNAVAILABLE:SOURCE_MANIFEST_INVALID` from `scripts/build_cross_document_consistency_advisory.py finalize`. The manuscript has no preregistration to compare against (its preregistration handoff is `status: not_provided`, `stage5/artifacts/preregistration-artifact.json`), so there is no valid source manifest and no observation draft for the hermetic comparator; fabricating one would violate the no-silent-substitution rule. Recorded as the bounded unavailability the protocol allows.

Both results are advisory only. Neither delays, blocks, or changes the Stage 5 routing after the checkpoint confirmation recorded above.
