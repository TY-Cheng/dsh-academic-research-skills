<!-- Intended issue title: Design: DSH sibling distribution for ARS (v0.3.0; content parity + e2e) -->

## Context

I maintain [`dsh-academic-research-skills`](https://github.com/TY-Cheng/dsh-academic-research-skills),
a **DeepSeek Harness (DSH) sibling distribution** of ARS. This issue is the
design step requested in `CONTRIBUTING.md` § *Platform ports* → *Sibling
distribution*, before any recognition request.

The sibling shape is:

- Separate repository; ARS `v3.24.2` pinned at
  [`6d93886`](https://github.com/Imbad0202/academic-research-skills/commit/6d9388674de1ad0437ad95db3d52f92b92204d84)
  (`v3.24.2-3-g6d93886`) in
  [`manifest.json`](https://github.com/TY-Cheng/dsh-academic-research-skills/blob/main/manifest.json).
- Written sync policy:
  [`SYNC_POLICY.md`](https://github.com/TY-Cheng/dsh-academic-research-skills/blob/main/SYNC_POLICY.md)
  (six-week cadence, offline drift check, immutable release tags).
- **1,006 vendored files** kept byte-identical: 199 skill files, 644 root
  `scripts/` files, 155 `shared/` files, 4 root `agents/` files, and 4 root
  files (`MODE_REGISTRY.md`, `THIRD_PARTY.md`, two requirements files).
  `npm run verify` checks the per-file SHA-256 and 21 registrations; CI
  [`verify-vendor`](https://github.com/TY-Cheng/dsh-academic-research-skills/actions/runs/44530710616)
  passes on `main`.
- DSH-specific code is confined to the outer adapter: `lib/startup.js`,
  `cordis.patch.yml`, `tooling/*.mjs`, generated `commands/`, docs, and CI.
  `commands/` is generated from the upstream `commands/ars-*.md`; no upstream
  `skills/`, `scripts/`, `shared/`, or `agents/` file is edited.
- Hooks are not ported; DSH has no hook system. Write protection is the DSH
  file sandbox.

## E2E evidence

The required full `academic-pipeline` run is committed at
[`examples/dsh/iv-surface-review/`](https://github.com/TY-Cheng/dsh-academic-research-skills/blob/main/examples/dsh/iv-surface-review/README.md)
(commit [`40b7e77`](https://github.com/TY-Cheng/dsh-academic-research-skills/commit/40b7e77c836273687de424c757fd2a1ae9d4ef9a)).

- Topic: arbitrage-free implied volatility surface construction; 40 sources;
  24 OpenAlex queries → 351 unique → 40 included; 30 peer-reviewed / 10
  preprints; 39 DOI + 1 HAL; 0 fabricated; abstract-level evidence.
- Pipeline: Stage 1 research → Stage 2 paper (internal Major Revision → v1.2)
  → Stage 2.5 integrity PASS (bounded) → Stage 3 five-seat Major Revision →
  Stage 4 revision → Stage 3′ Minor Revision → Stage 4′ copy-edit → Stage 4.5
  PASS (bounded) → Stage 5 final. Stage 6 was not run, per the operator.
- Result: a 6,804-word review paper with 40 references, 8 tables, and five
  appendices; Markdown, DOCX, LaTeX, and a 35-page PDF. The PDF/DOCX are
  deterministic fallbacks (Pandoc absent), not journal typesetting.
- Limits are disclosed in the paper and integrity reports: abstract-level
  evidence, 10 preprints, one title-level source, no full text, no plagiarism
  scan, no complete COI audit, S2 rate-limited (HTTP 429), no dual screening,
  311 non-advanced records not individually coded, and no PRISMA claim.

## Model portability and locale

- The e2e ran on DSH desktop, DSH CLI `0.2.2-rc.5`, with the runtime's
  `deepseek-flash` model. **No Claude model was used.** The role prompts ran
  inline in one session; the five review seats were role-separated prompts,
  not independent subagents. The full note is
  [`model-portability.md`](https://github.com/TY-Cheng/dsh-academic-research-skills/blob/main/docs/sibling-submission/model-portability.md).
- The paper's abstract is in Simplified Chinese (`zh-CN`) for the operator's
  convenience. ARS's default pair is English + Traditional Chinese (`zh-TW`).
  This is **not** a locale pack; no two-owner locale-pack arrangement is
  claimed.

## Maintainer and license

- Named maintainer: **TY-Cheng** ([@TY-Cheng](https://github.com/TY-Cheng)),
  stated in the repository README and
  [`maintainer.md`](https://github.com/TY-Cheng/dsh-academic-research-skills/blob/main/docs/sibling-submission/maintainer.md).
  I will keep the port in sync on the six-week cadence and triage DSH issues;
  platform expertise stays with me.
- All vendored content and the porting layer are **CC-BY-NC-4.0**, with the
  upstream and original-port attribution in `NOTICE.md`. No relicensing is
  claimed.
- A claim-by-claim evidence table is at
  [`claims-evidence.md`](https://github.com/TY-Cheng/dsh-academic-research-skills/blob/main/docs/sibling-submission/claims-evidence.md).

## What I am asking

1. Is this sibling shape acceptable for official recognition? If not, what
   structural change would you want?
2. What is the preferred recognition path: a PR to the upstream README /
   `THIRD_PARTY.md`, an issue, or both? I have not opened a recognition PR.
3. For the e2e evidence, do you prefer the Markdown bundle + reports only, or
   is it useful to link the 35-page PDF/DOCX as well?
4. The model-portability note is one non-Claude run with no Claude baseline.
   Does sibling recognition require a Claude-run e2e or a model matrix before
   listing, or is the disclosed one-run evidence acceptable at this stage?
5. Should the e2e for recognition use the default English + `zh-TW` abstract
   rather than the operator's `zh-CN` choice?
6. Any naming, attribution, or listing constraints for the sibling repo?

## What I am not asking

- I am not asking for changes to ARS core content, IRON RULE text, or review
  protocols.
- I am not claiming official sibling status, endorsement of the paper, model
  parity with Claude, a `zh-CN` locale pack, or independent five-agent review.
- The e2e is one platform run with disclosed limits, not a benchmark.

Thank you for maintaining ARS and for the detailed porting contract.
