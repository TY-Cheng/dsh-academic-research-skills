contract_role: perspective
## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: not_assessed

### D3: argumentative_coherence
score: not_assessed

### D4: cross_disciplinary_relevance
score: warn
trigger: "Some terms or empirical conventions need specialist knowledge and the practical or adjacent-field implications are stated without enough translation for readers outside the subfield."

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

My checks are those of an outside stakeholder. I ask whether the reported tolerances can become validation acceptance criteria, whether the enforcement burden and the excluded audiences are identified, and whether the seven-study agenda could be commissioned by a validation team as scoped. I do not audit derivations, statistical validity, or literature coverage; those belong to the seats that own them.

### S1: The enforcement triple is a portable instrument for adjacent readers

The mechanism-evidence-verification triple, and the mapping of the four loci onto the parameter set, the evaluated sample, the output image, and the accepted sample, gives a reader from model risk, audit, or applied data science a way to see what a given guarantee quantifies over. This is the part of the paper most usable outside the originating subfield: it turns an ambiguous adjective into a question a non-specialist can ask, and it survives the paper's refusal to rank methods.

**Evidence Anchor**: text: §2.3 "a theorem over a set, a reported residual on a sample, or an assumption inherited from a model class"

### S2: Limits and corpus composition are disclosed rather than buried

The paper states what its evidence cannot carry: abstract-level reading, single-analyst coding, English- and OpenAlex-only retrieval, non-PRISMA screening, eleven preprints, and the US dominance of known-provenance rows. These limits appear in the abstract, §3.3, and §6.4, so a non-specialist can calibrate the counts without hunting for the caveat. The disclosure is unusually direct for a review that is itself making a coverage argument.

**Evidence Anchor**: text: §3.3 "Those limits are not repaired anywhere in the paper; they are stated once here and carried into Section 6.4."

### S3: The review declines to rank methods and says what each guarantee is worth in kind

The explicit refusal to produce a league table, and the insistence that a theorem, a residual, a projection, and a pass rate are different evidence objects, gives validation readers something more useful than a ranking: a way to audit the claim attached to a particular surface. The closing question of §7.2, which claim, at what tolerance, checked how, is portable to a model-risk review even when the underlying methods are not.

**Evidence Anchor**: text: §7.2 "the corpus does not identify a best method"

### W1: The residuals never become a validation acceptance criterion

The manuscript reports a 5.4% butterfly violation floor over 252 out-of-sample SPX days (§4.3), under-1% static violations with stressed-year leakage (§4.3), a 90.8% pass rate (§4.4), and 0.00% at 1e-4 on synthetic data (§4.4). It correctly says in §5.2 that these numbers differ in data, definitions, tested conditions, and tolerance. What it never supplies is the step a validation team needs: for each number, the threshold, the test power, the regime coverage, and the independent check that would make it usable as an acceptance criterion. §5.3 names a loss function and a tolerance as missing, and the fourth agenda proposal addresses power, but neither converts a reported residual into an accept or reject decision, nor says that no number in the corpus is offered as a threshold. A short bounded statement of which inputs are still absent, and what evidence would license each, would make the paper's practical claim checkable rather than only honest.

**Severity**: Major

**Evidence Anchor**: text: §5.3 "whether any reported residual is operationally adequate is not assessable without a loss function and a tolerance that the corpus does not supply"

**Confidence**: 4 — validation and model-risk perspective applied to the reported residuals and the coverage matrix.

### W2: The practitioner sentence offers a cost input the corpus cannot measure

§6.1 addresses authors, reviewers and editors, and readers, all academic roles. §7.2 then tells practitioners that the review identifies what each method's guarantee is worth and what it costs, and calls that a more useful input to a build-or-buy decision than an unqualified label. The cost half is the weak half for that reader: §5.3 records that computational cost is asserted in about five rows with no comparable measurement, and the burden-displacement result in §5.1 relocates constraint work into weights, tolerances, repair steps, and acceptance thresholds without naming the practising role that now owns those choices. A build-or-buy reader therefore cannot use the sentence as written. Separating what the review establishes, the guarantee type and its evidence mode, from what it does not, cost, operating point, and ownership, and naming the roles would make the implication usable without changing the underlying findings.

**Severity**: Major

**Evidence Anchor**: text: §7.2 "it identifies what each method's guarantee is worth and what it costs"

**Confidence**: 4 — stakeholder and operational reading of the practitioner-facing claims.

### W3: Audiences outside the research core are neither named nor excluded

The limitations disclose corpus composition well: 10 of 12 known-provenance rows on US indices, non-US evidence resting on a 2006 DAX study and a 2022 JSE study, one practitioner magazine article, and abstract-level coverage. They do not say whether supervisory or regulatory users, model-validation functions, or end investors are outside the intended audience. §1.1 invites that readership by saying a fitted surface can in principle propagate into risk numbers, margin, and capital, and then flags the propagation as a premise; §6.1 contains no such user; §7.2 assumes a build-or-buy decision without naming the firm-side roles. A validation or supervisory reader consequently cannot tell a scoping choice from an oversight. One limitations sentence naming the excluded users, and the competence or evidence each would require, would close the gap.

**Severity**: Minor

**Evidence Anchor**: absence: §6.4 and §7.2 — expected named supervisory and end-investor users and the competence each would require; checked §1.1, §5.1, §6.1, §6.4, §7.2, Appendix A

**Confidence**: 3 — cross-disciplinary audience analysis; document claims only.

### W4: The seven-study agenda lacks the dependencies, data access, and ownership a validation team would need

Each proposal in §6.3 names a measurable outcome and a claim it would falsify, which is the right construction. What a team asked to run them lacks is the implementation view: which study is a prerequisite for which, what panel or detector each requires, what compute and personnel it implies, and who owns the result. The ordering is also consequential. The dynamic test and the pre-registered head-to-head come first; the residual audit for proof constructions and the test-power and noise-floor study, the two that would make any reported residual usable, are third and fourth; the evaluation of cost, interpretability, and data efficiency is split across the fifth and seventh proposals. Cost, interpretability, and data efficiency are reasonable dimensions, but they are not first targets for acceptance use, because power and the noise floor determine whether a threshold can be set at all. A short dependency table, with the data access each study needs, would let the agenda be commissioned rather than admired.

**Severity**: Minor

**Evidence Anchor**: absence: §6.3 — expected dependency order, data access, and resource or owner requirements for the seven studies; checked §6.3, §6.4, Table 6

**Confidence**: 3 — research-operations and implementation perspective.
