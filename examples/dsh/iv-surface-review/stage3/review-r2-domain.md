# Stage 3 — Reviewer 2 (Domain)

**Recommendation:** Major Revision

## Summary

The paper covers the main construction families and makes a useful distinction between static and dynamic no-arbitrage. The domain coverage is uneven: the taxonomy is asserted rather than mapped source by source, and several important streams are outside the corpus without a clear scope statement.

## Strengths

- The SVI/SSVI/eSSVI discussion is accurate at the abstract level.
- The static/dynamic distinction is the right organizing move.
- The paper does not overclaim a method ranking.
- The decision guide is useful for practitioners.

## Major issues

**D1. Map the 40 sources to the taxonomy.** Table 2 gives representative sources per family, but the reader cannot see how each of the 40 was classified. Add Appendix D: source, method family, enforcement family, static test reported (Y/N/partial), dynamic test reported (Y/N), evidence level. This also exposes hybrids and ambiguous cases.

**D2. Dynamic no-arbitrage needs a dedicated evidence table.** Only four or five sources engage dynamic consistency. Add a table (source, mechanism, dynamic test, data, result) and state explicitly that the corpus cannot adjudicate dynamic superiority. The “frontier” label should be tied to the table.

**D3. State what is out of scope.** Rough-volatility models, stochastic-volatility calibration, American options beyond one source, crypto/FX surfaces, and reinforcement-learning approaches are not systematically covered. A short “scope and excluded streams” paragraph prevents the reader from assuming exhaustive coverage.

## Minor issues

- Distinguish “static arbitrage” (butterfly/calendar) from “dynamic arbitrage” in the first use; the paper does, but the abstract could be sharper.
- The 2026/2027 sources are very recent; note the online-first status.
- The “hard constraints” label covers both gated networks and constrained parametric families; define it once.
- The paper’s “seven dimensions” are a proposal; keep that label in Table 3 and the text.

## What would make it acceptable

Appendix D, a dynamic-evidence table, and a scope statement. The paper would then be a credible corpus-scoped map, not an exhaustive survey.
