# Named maintainer and maintenance commitments

## Maintainer

**TY-Cheng** — [@TY-Cheng](https://github.com/TY-Cheng)

Repository: https://github.com/TY-Cheng/dsh-academic-research-skills

This statement is also recorded in the repository
[`README.md`](../../README.md) attribution block, [`NOTICE.md`](../../NOTICE.md),
`manifest.json.maintainer`, and [`SYNC_POLICY.md`](../../SYNC_POLICY.md).

## What I will do

I will keep this DSH sibling distribution in sync with ARS minor releases on the
roughly six-week upstream cadence, and triage DSH-specific issues:

1. Watch upstream tags/releases; open a sync issue in this repository.
2. Run `node tooling/sync-upstream.mjs <clean-upstream-checkout>` against the
   target commit.
3. Review the vendored diff; local edits are allowed only in the porting layer
   (`lib/`, `cordis.patch.yml`, `tooling/`, docs, CI), never in `skills/`,
   `scripts/`, `shared/`, or `agents/`.
4. Run `npm run verify`, the Python AST check, the package-contents check, and
   the DSH registration smoke test.
5. Update the package version and release notes; commit; tag `vX.Y.Z`.
6. Keep the README's ARS version, the manifest pin, and the e2e evidence in
   agreement.

The full procedure, drift check, and release rules are in
[`SYNC_POLICY.md`](../../SYNC_POLICY.md). The upstream commit and per-file
hashes are in [`manifest.json`](../../manifest.json).

## Issue triage

- **DSH-specific issues** (registration, path resolution, DSH packaging,
  command wrappers, this port's docs) → this repository's
  [issue tracker](https://github.com/TY-Cheng/dsh-academic-research-skills/issues).
- **Upstream ARS content issues** (prompt semantics, IRON RULE text, integrity
  protocols, handoff schemas, skill behavior independent of DSH) → redirect to
  the upstream repository, not this port.
- **Security or licensing concerns** → open an issue or contact me via GitHub;
  do not post secrets.

## What I am not claiming

- I am the **only** named maintainer; no backup owner is claimed.
- This is **not** a locale pack. The e2e's zh-CN abstract is an operator choice;
  ARS's default pair is English + zh-TW. The upstream locale-pack rule requiring
  two owners is therefore not invoked.
- I am not asking the upstream to maintain this port. Platform expertise,
  post-merge maintenance, and DSH-specific bug triage stay with me.

## Maintainer changes

If I stop maintaining this port, I will update this file and the repository
README and notify the upstream maintainer in the recognition thread. I will not
transfer the repository silently while it is listed as a sibling distribution.
