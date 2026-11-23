# Second-Coder Recheck: Adjudication Record

**Sample.** 16 of 41 rows: P1, P4, P7, N2, N5, R2, R3, R4, R5, G6, G7, C3, C4, C5, S1, S2 (two per family, the boundary/weakest-coverage row of each included, plus every metadata-only row).
**Blindness.** The second coder received only `reliability/blind-handbook.md` (definitions D.1–D.8 with the first coder's tallies removed) and `stage4/second-coder-input.json` (title, metadata, abstract). The first coder's ledger columns were withheld; no discussion preceded the return.
**Measure.** Agreement counts and Cohen's κ on the 16 rows; threshold from handbook D.9: accepted where agreement ≥ 0.85 and, for evidence status, κ ≥ 0.70.

| Field | Agreement | κ | Threshold | Outcome |
|---|---|---|---|---|
| Family | 12/16 (0.750) | — | 0.85 | below |
| Evidence status | 10/16 (0.625) | 0.47 | 0.85 / 0.70 | below |
| Audit | 15/16 (0.938) | — | 0.85 | clears agreement |
| Time-axis engagement | 16/16 | — | 0.85 | stable |
| Dynamic enforcement | 16/16 | — | 0.85 | stable |
| Comparability | 10/16 (0.625) | — | 0.85 | below |
| All cells | 79/96 (0.823) | — | 0.85 | below |

## Adjudication (first analyst; one line per cell)

| Row | Field | First | Second | Decision and reason |
|---|---|---|---|---|
| P7 | family | P | C | Kept P: the title's necessary-and-sufficient conditions characterise the admissible SSVI/S3 parameter domain — a parameter-domain result used to fit — which is P under D.1; C is recorded as the live alternative for a metadata-only row. |
| G6 | family | G | N | Kept G: the certified object is a generated surface family, the D.1 tie-break's G clause; the constraint is architectural, but the paper's contribution is the sampler, not a fitted estimator. |
| G7 | family | G | N | Kept G: the row derives a model class that generates admissible surface paths over dates; N would fit a single-date estimator. |
| C3 | family | C | P | Kept C: the coded contribution is the statement that static admissibility constrains the joint (surface, price) dynamics, not a fitted parametric surface; P is recorded as the alternative reading. |
| R2 | evidence | proof | assumption | Kept proof: the abstract proves convergence of a procedure built on martingale optimal transport, whose image is the admissible set; it is proof for the map, as D.2 requires. |
| R3 | evidence | proof | assumption | Kept proof: admissibility is established by construction from an arbitrage-free reference model; the abstract states the construction, not merely an assertion. |
| G6 | evidence | proof | numerical test | Kept proof: admissibility is structural (enforced for every output by the architecture), with the tests corroborating; D.2's "statement of a construction" reading applies. |
| G7 | evidence | proof | numerical test | Kept proof: the abstract derives the constraint-respecting state space; the numerical validation is secondary to the derivation. |
| C3 | evidence | proof | assumption | Kept proof: the SSVI parameterisation fixes static admissibility of every simulated slice by construction. |
| S2 | evidence | numerical test | assumption | Kept numerical test: the abstract presents the method's fit/pricing behaviour as support; the second coder's no-number reading is recorded as the stricter alternative. |
| N2 | audit | Y | N | Kept Y: the abstract reports adherence statistics on its own fitted and smoothed output over the evaluation panel; the second coder read the same quantities as accuracy benchmarks. |
| N2 | comparability | RC | NC | Kept RC: a reported rate is placeable for context even without a common protocol; NC is recorded. |
| N5 | comparability | RC | NC | Kept RC for the same reason (reported comparative behaviour); NC recorded. |
| R2 | comparability | RC | NC | Kept RC; NC recorded. |
| G7 | comparability | RC | NC | Kept RC; NC recorded. |
| C3 | comparability | RC | NC | Kept RC; NC recorded. |
| S1 | comparability | RC | NC | Kept RC: the row reports a fit-quality demonstration; NC recorded. |

**No ledger change.** The adjudication kept the first analyst's code in every cell, so Appendix B and the Table 3 tallies are unchanged. The recheck's finding is therefore not a corrected ledger but a measured stability: time-axis and dynamic enforcement reproduce; family, evidence status, and comparability do not reach the threshold, and the claims that depend on them are restated at that strength in Sections 3.3, 3.4, 4 and 5.1.

**Limitation.** Sixteen rows are a designed sample; the agreement measures the handbook's reproducibility among two coders on this sample, not a population, and the second coder had only abstracts and titles (as did the first).
