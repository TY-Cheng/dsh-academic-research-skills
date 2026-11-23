# Coding Handbook for the 41-Row Evidence Ledger

**Purpose.** This handbook defines every field of the evidence ledger (Appendix B) operationally, so that a second analyst working only from the 41 frozen records and this document can reproduce the ledger row by row. It also fixes the reliability protocol (Section D.9) used for the stratified second-coder recheck reported in Section 3.4 of the manuscript.

**Unit of coding.** One row is one source as represented by the record that entered the corpus: its title, its retained abstract, and its bibliographic metadata. Nothing outside that record is coded. A claim that appears only in a full text, a proof, or a code repository is outside the unit, and its absence is coded as absence of a *reported* claim, never as absence of the property.

**Freeze.** The record set, the abstracts, and the search provenance were frozen on 2026-11-23. A re-application of this handbook to records retrieved later is a different coding, not a replication of this one, because the OpenAlex index behind the records is live.

### D.1 Family code

Each row receives exactly one family code, assigned from the mechanism named in the abstract:

- **P, parametric construction**: the constraint enters a parameter domain or a function class specified before fitting, so that every admitted parameter vector yields an admissible object.
- **N, penalty and constrained learning**: the constraint enters a training objective or an architectural regulariser, so compliance is approximate and conditional on a weight, a tolerance, and a stopping rule.
- **R, projection and repair**: a map is applied to a fitted or quoted object after the fact, so the certified object is the image of that map.
- **G, generation and filtering**: candidate surfaces, parameters, or prices are produced and then accepted, rejected, projected, or constrained, so the certified object is the accepted sample or the generator's model class.
- **C, conditions and evaluation**: the row states, detects, or reviews admissibility conditions without constructing or repairing a surface.
- **S, seminal baseline**: a pre-2015 construction included as declared baseline rather than as a window record.

**Tie-break.** Where two mechanisms are present, code the family of the **certified object**, not of the estimator: a gated network whose decoder is a deterministic convex architecture is P-shaped but is coded N when its abstract presents the constraint as a loss or architectural term of a learned estimator (N1), and is coded G when the object is a generated surface family. Rows that sit across borders are retained in one family and flagged in Appendix C rather than reassigned.

### D.2 Evidence status

The evidence-status field records what the abstract presents as support for the row's admissibility claim. It has three values and no ranking order.

- **Proof**: the abstract states a theorem, a closed-form characterisation, or a formal construction that establishes admissibility over a set, for all objects in that set. A convergence proof for an algorithm is a proof about the algorithm, not about the admissibility of a repaired surface; a repair whose projection map is proved to land in the admissible set is coded **proof for the map** and the manuscript states that object in the row note.
- **Numerical test**: the abstract reports a numerical result that it presents as supporting the admissibility claim, where that result is not a violation or residual statistic computed on the row's own output. Examples: a fit or pricing error, a coverage or inside-spread statistic, a Wasserstein distance, a comparative accuracy against a baseline, or a hedging result. A numerical test is never upgraded to a proof.
- **Assumption**: admissibility is asserted, inherited from a model class, or left implicit, with neither a theorem nor a numerical result presented as support.

**Precedence.** Proof > numerical test > assumption applies only to *classification order*, not to evidential strength: a penalty row that reports a residual is coded numerical test even when the reported rate is zero, and a row whose architecture is described as convex by design but whose abstract states no theorem is coded numerical test, not proof.

### D.3 Audit row (separate from evidence status)

**Definition.** An audit row is a row whose abstract reports a **violation, residual, or defect statistic computed on the row's own fitted, repaired, or generated output**. The statistic must be about the row's own construction; a comparative error against a baseline, a runtime, a coverage measure, or a hedging profit is not an audit statistic.

**Decision rule.** Code audit = Y only if all three hold:

1. the reported quantity is a violation rate, a count of violated conditions, a residual of an admissibility condition, or a pass rate on an admissibility test;
2. it is computed on output the row itself produced, not on a benchmark dataset or on another row's surface;
3. the abstract names, implicitly or explicitly, the conditions tested. Where the tolerance is not stated, the row is still an audit row, and the missing tolerance is recorded as a limitation of the row (this is why the manuscript says a rate without a tolerance is uninterpretable even within its own study).

**Not an audit.** A residual for a *method* rather than a surface (e.g. a convergence residual), an accuracy number, a spread-capture percentage, or a pass rate on a test set that is not the row's own output is coded N. Consistent with this rule, six rows are audit rows (N2, N6, R5, R7, G5, G6) and the other eleven numerical-test rows are not: N1, N3, N4, N5, R1, R9, G2, G4, C5, S2, S3. The ledger's Audit column carries the value for every row, so the eleven can be recounted rather than taken on trust.

**Independence from evidence status.** Audit is coded on its own axis and is not a value of the evidence-status field. A proof row can be an audit row (G6 is both) and a test row can fail to be one. This is the separation the manuscript's Section 3.2 states and Section 5.1 recounts.

### D.4 Time-axis engagement

**Definition.** Code time-axis engagement = **Y** where the abstract's *object* is indexed by calendar time: a date-indexed panel, a surface path or process, a time-indexed parameter or probability sequence, a state that evolves over dates, or a dynamics model of the surface family. Ten rows are Y (P8, R8, G1, G2, G3, G7, C2, C3, C5, S5).

**Exclusions.** The maturity axis of a single surface is **not** calendar engagement. A construction that enforces non-decreasing total variance across maturities (SC5) has made a static statement about one date's object and is coded N here, however the abstract labels it. A continuous-time *model* whose evaluated object is one date's surface (R9) is coded N: the model is dynamic in its class, but the coded object is not date-indexed. A VAR or factor model estimated on a panel is Y even where no admissibility condition is imposed (S5). Conversely, a panel used only as an evaluation sample is **not** engagement: R5 repairs one surface per trading day over 252 out-of-sample days, N2 fits across ten years of intraday quotes, and R7 reports year-by-year panels, but in each case the coded object remains a single date's surface and no claim is indexed by calendar time. Engagement is a property of the object or the claim, not of the sample size in the date direction.

**Why the axis is separate from dynamic enforcement.** Engagement measures the object's indexing; enforcement measures whether a process-level condition is stated and checked. The two are coded independently so that a row can engage time without enforcing anything (the common case) and so that the absence claim can be bounded exactly.

### D.5 Dynamic enforcement

**Definition of a dynamic condition.** A condition on the joint law of the surface family indexed by calendar time: the absence of predictable arbitrage opportunities across dates, or consistency of the date-indexed family with a martingale measure for a stated numéraire. A condition on one date's surface, including a maturity-monotonicity condition and including anything called "calendar arbitrage", is **static** (Section 2.1, SC5) and is never coded as dynamic enforcement.

**Coding values.**

- **D0, none**: the abstract states no process-level admissibility condition. This includes rows that construct a date-indexed object without an admissibility claim.
- **D1, declared or described, not checked**: the abstract discusses, names, or asserts a process-level condition, or reports a model-level diagnostic of it, without stating that the constructed, date-indexed family was checked against it.
- **D2, inherited from a model class**: the admissibility property follows from the class the model belongs to (for example a constrained state space, an SDE whose coefficients keep the surface static-admissible, or a decoder that cannot emit a violation), and no check of the fitted family over dates is reported.
- **D3, stated and checked**: the abstract states a process-level condition **and** reports that the constructed date-indexed family was checked against it over a path or sequence.

**The model-class rule (the rule Section 2.2 of the manuscript states).** A model-class inherited guarantee is **not** dynamic-constraint enforcement under this coding. It is coded D2 and reported as what it is: a property of the class, inherited by every member, unaccompanied by any reported check of the fitted family across dates. The rule is deliberately conservative and it is the rule on which the "0 of 41" count rests: the count is 0 rows at D3, and the manuscript states that count together with the D1 and D2 rows by ID, so a reader who rejects the rule can recompute the count from the ledger without leaving the manuscript.

**Result.** D3 = 0; D2 = G1, G7, C3; D1 = P8, C2, C5, R8; D0 = the remaining 34 rows. The manuscript states each of the four groups and names the rows.

### D.6 Static condition statement

The static predicate is SC1–SC5 as defined in Section 2.1 of the manuscript, with SC3 in its corrected form, c'' − c' ≥ 0, in log-moneyness for the normalised call price.

- A row that claims full admissibility without enumerating conditions is coded `SC1–SC5`: its claim is assessed against the whole predicate.
- A row whose abstract names a subset is coded with that subset, using the abbreviated range notation in the ledger (e.g. `SC1–3,5`).
- A row that states no admissibility condition at all (the two pre-constraint baselines) is coded `none`.
- `ns` is retained only for a row whose claim cannot be mapped onto the predicate without inference; the ledger as frozen uses it for no row, because a bare "arbitrage-free" claim is treated as a claim on the full predicate.

**SC3 dependency.** Any row whose coded subset contains SC3 is a row whose coding depends on the corrected butterfly condition. The re-examination reported in Appendix C applies to exactly those rows; where a row's subset does not contain SC3, the correction cannot change it.

### D.7 Comparability

- **DC, directly comparable**: the same dataset or panel, the same condition set and tolerance, the same metric and aggregation, and the same protocol. No row qualifies in this corpus.
- **RC, reported for context**: a number is reported that a reader can place beside another row's number but that does not license a comparison, because at least one of the four fields differs.
- **NC, not comparable**: a different object or metric, or no number at all.

Comparability is coded from the abstract and is deliberately conservative: where a required field is unstated, the row cannot be DC.

### D.8 Abstract coverage, peer review, and evidence level

- **Coverage**: `full` where a complete abstract was retrieved; `partial` where the retained text is truncated or reconstructed from fragments (R2, G3, C4, S1); `metadata-only` where no abstract was retrievable and the row is coded from title and metadata only (P4, P7, R4).
- **Metadata-only rule**: a metadata-only row is cited only for what its title asserts; it is counted in every structural count (family, evidence status, comparability, coverage, peer review) and is never counted as evidence *for* its own claim. The rule is applied identically in Sections 3.2, 5.1 and Appendix B.
- **Preprint**: tagged at every point of use where the record has no peer-reviewed version of record in this corpus. Eleven rows are preprints.
- **Evidence level VI/VII**: the seven-level source hierarchy used for appraisal. Level VI is a single descriptive, quantitative, or qualitative study; level VII is expert commentary or a narrative review. Forty rows are VI; C2 is VII. The level is not an evidence-status value and not a quality grade.
- **Appraisal grades A/B/C**: recorded in the corpus's earlier appraisal record (A 11, B 13, C 17) but not reproduced per row in the ledger and therefore not used as a recomputable count anywhere in the manuscript. The reason is stated in Appendix C: two of the six appraisal criteria are free-text judgements that the ledger fields do not carry, so printing the grades alongside the fields would present a judgement as a derivation.

### D.9 Reliability protocol

**Design.** A stratified second-coder recheck of a 16-row sample, drawn to exercise every family and every weak-coverage class rather than to estimate a population rate.

**Strata and sample.** Two rows per family, chosen to include the family's boundary and weakest-coverage rows, plus every metadata-only row:

| Stratum | Rows |
|---|---|
| P (3) | P1, P4 (metadata-only), P7 (metadata-only, preprint) |
| N (2) | N2, N5 |
| R (4) | R2 (partial), R3, R4 (metadata-only), R5 |
| G (2) | G6, G7 |
| C (3) | C3, C4 (partial), C5 |
| S (2) | S1 (partial), S2 |

The sample is 16 rows: all three metadata-only rows, three of the four partial-abstract rows, both families' known boundary cases (R3, G7), and the only proof-and-audit row (G6).

**Blindness.** The second coder receives the 16 records, this handbook, and the empty coding form. The first analyst's coded columns are withheld. No discussion occurs before the second coder returns the form.

**Fields re-coded.** Family; evidence status; audit; time-axis engagement; dynamic enforcement; comparability. Metadata fields (coverage, peer review, preprint tag, evidence level) are not re-coded because they are bibliographic rather than interpretive.

**Statistics.** Percentage agreement per field. For the three-level evidence-status field, Cohen's κ (unweighted) over the sampled rows. For the binary fields (audit, time-axis engagement) and the four-level dynamic field, percentage agreement, with the raw disagreement count reported. Disagreements are adjudicated by the first analyst with a one-line written reason per row, and the adjudication is reported, not hidden.

**Decision rule.** A field is treated as *stably coded* where agreement is at least 0.85 and, for evidence status, κ ≥ 0.70. Any field below the threshold triggers a restatement of the absence claims that depend on it at the observed stability, with the disagreement rows named. No field is reported as reliable on the strength of a design alone.

**Reporting.** The result is reported in Section 3.4 and the completed forms are retained with the coding records. The manuscript does not claim inter-rater agreement for any field that was not re-coded.

### D.10 Recomputation

Every structural count in the manuscript can be recomputed from the ledger columns:

| Count | Rule |
|---|---|
| Rows | 41, one per ID |
| Family totals | tally of the Family column |
| Evidence status | tally of the Evidence column; in-window/seminal split follows the ID letter |
| Audit rows | tally of Audit = Y (6) |
| Proof-and-audit overlap | rows with Evidence = proof and Audit = Y (1, G6) |
| Time-engaging rows | tally of Time = Y (10) |
| Dynamic enforcement | tally of Dyn by value: D3 = 0, D2 = 3, D1 = 4, D0 = 34 |
| Comparability | tally of Comp. column (0 DC, 30 RC, 11 NC) |
| Coverage | tally of Coverage column (34 full, 4 partial, 3 metadata-only) |
| Peer review | tally of the Peer-reviewed column (29 yes, 12 no; 11 preprints plus the practitioner article S3) |
| Peer review, no | 12 rows carry Peer-reviewed = no: the 11 preprints plus the practitioner-magazine outlet (S3) |
| Preprints | rows tagged [preprint] (11) |
| Evidence level | tally of Level column (40 VI, 1 VII) |

**Arithmetic checks.** Evidence status: 17 proof + 16 numerical test + 8 assumption = 41. Partition by audit: 1 proof-and-audit (G6) + 16 proof-only + 5 test-and-audit (N2, N6, R5, R7, G5) + 11 test-only + 8 assumption = 41. Audit rows: 5 test-and-audit + 1 proof-and-audit = 6. Dynamic codes: 0 (D3) + 3 (D2) + 4 (D1) + 34 (D0) = 41. Time engagement: the ten Time = Y rows contain all four D1 rows and all three D2 rows; the other three (G2, G3, S5) are D0, so they engage the time axis without making any dynamic claim. Composition: 29 peer-reviewed + 11 preprints + 1 practitioner = 41; 36 in-window + 5 seminal = 41.

### D.10 Second-coder recheck result (record stage 4)

The recheck was run on the 16-row sample in Section 3.4. Observed agreement: family 12/16, evidence status 10/16 (κ 0.47), audit 15/16, time-axis 16/16, dynamic 16/16, comparability 10/16; overall 79/96 (82.3%). Only the time-axis, dynamic and audit fields clear the D.9 bar on the pre-registered rule; the three failing fields' claims are restated at the observed stability in the manuscript. The 17 cell disagreements were adjudicated by the first analyst, keeping the ledger codes, with the reasons recorded in `stage4/reliability/adjudication.md`; the blind packet (handbook without results plus records) is `stage4/reliability/blind-handbook.md` and `stage4/second-coder-input.json`, and the second coder's return is `stage4/reliability/second-coder-form.json`.
