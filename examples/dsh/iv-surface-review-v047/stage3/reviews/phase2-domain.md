contract_role: domain
## Dimension Scores

### D1: methodology_rigor
score: not_assessed

### D2: domain_accuracy
score: warn
trigger: "domain imprecision or incomplete attribution that a specialist would flag and expect corrected in revision, without any single error overturning a claim the manuscript relies on"

### D3: argumentative_coherence
score: not_assessed

### D4: cross_disciplinary_relevance
score: not_assessed

### D5: writing_and_structure
score: not_assessed

### D6: venue_fit_and_contribution
score: not_assessed

## Review Body

### W1: SC3 states the log-moneyness inequality as the butterfly condition
**Severity**: Major
**Evidence Anchor**: text: "**SC3**, strike convexity, the butterfly or Durrleman condition, $\partial^{2} c/\partial k^{2}\ge 0$"

Durrleman's condition, which the sentence names, is convexity of the call price in strike, $\partial^{2} C/\partial K^{2}\ge 0$. With $C=F c(k)$ and $k=\log(K/F)$, that derivative is $(F/K^{2})(c''(k)-c'(k))$, so the condition is $c''-c'\ge 0$; the printed $c''\ge 0$ is a different inequality. Because SC2 already fixes $c'\le 0$, the printed form implies the true one and is strictly stronger, so it excludes surfaces that satisfy the butterfly condition. A central-difference check on the canonical Black–Scholes surface ($F=1$, $\sigma=0.2$, $\tau=1$) returns $c''\approx-0.53$ at $k=-0.5$ and $c''\approx-0.37$ at $k=-1.0$, while the butterfly quantity is $c''-c'\approx+0.07$ at $k=-0.5$: read literally, SC3 marks a plainly arbitrage-free surface as a violator. The printed SC3 also cannot hold on the zero-maturity slice that SC4 fixes, since $c''(k,0)=-e^{k}<0$ for $k<0$, so the five conditions are mutually inconsistent at the boundary they themselves impose.

The consequence is instrument-level. Appendix C states that each row was coded for the static condition set it expresses among SC1–SC5, and §2.1's "SC1–SC4 encode a non-negative risk-neutral density" is the sentence the instrument rests on, so every per-row coding that includes SC3 inherits the mistranslation. The repair is contained — correct the right-hand side to $c''-c'\ge 0$ in §2.1 and re-examine the rows coded as expressing SC3 — which is why the finding is Major rather than Critical: the review's central claim about the static/dynamic division does not depend on the exact inequality, but its coding of which static conditions each construction enforces does.

### W2: The dynamic-absence claim has no row-level evidence in the manuscript
**Severity**: Major
**Evidence Anchor**: absence: Appendix B and Appendix C — expected a per-row time-axis and dynamic-enforcement coding for the 41 sources; checked Section 2.2, Table 3 in Section 5.1, the Appendix B table body, and the Appendix C field list

The review's most load-bearing empirical claim is a negative: no included study enforces or tests dynamic no-arbitrage, and ten rows engage time (abstract; §2.2; §6.2). A specialist can only re-check that claim row by row, and the manuscript does not give the rows. Appendix B's eight columns carry family, evidence status, comparability, coverage, peer-review status and citation location, but no time-axis field and no dynamic-enforcement field. Appendix C says the eight fields were coded, while §5.3 says the per-row values are held with the stage 1 records rather than reproduced. Table 3 reports audits, not time engagement. §2.2 names four of the ten engaging rows (G7, C3, P8, C5) as illustrations; the remaining six and the classification of the other 29 construction rows are nowhere in the manuscript.

The gap matters beyond presentation because the review itself offers two readings of the result (§6.2): a genuine gap, and a retrieval and vocabulary effect. Neither the reviewer nor the reader can separate those readings from the artifact in hand, since the coding that would show why each row was judged not to test a process-level condition is unpublished. Supplying one appendix column and a short coding note — with the vocabulary that was searched and the reason each engaging row was judged static — would convert a claim the review asserts into a claim the review enables a reader to check, and would also give the second reading in §6.2 a test.

### W3: The dynamic formulation rests on one assumption-level preprint
**Severity**: Minor
**Evidence Anchor**: text: "filtered probability space on which the option-price process is a martingale under a measure consistent with the numéraire (Niu, 2015)"

§2.2 defines the dynamic condition by citing Niu (2015) alone, and the review itself codes that source at assumption level (Appendix B, C2) and describes it in §6.2 as a source that reviews the conditions without testing them. The static/dynamic distinction the paper relies on has a canonical peer-reviewed treatment: Bergman, Grundy and Wiener (1996) derive the model-independent restrictions on European option prices from which SC1–SC3 are drawn. That work is outside the declared 2015–2026 window and is not among the five seminal precursors, and §2.2 does not engage it.

This is an attribution gap, not an error: nothing in the definition contradicts the canonical statement. But resting the paper's operative definition on a single unrefereed source, when the distinction it uses is standard, makes the definition look idiosyncratic and makes it harder for a specialist to place the contribution. Adding the canonical reference alongside Niu in §1.1 and §2.2 is enough; no re-coding follows.

### W4: The abstract's source composition does not sum to the corpus
**Severity**: Minor
**Evidence Anchor**: text: "of which 29 are peer-reviewed and 11 are preprints"

The abstract states a corpus of 41 sources "of which 29 are peer-reviewed and 11 are preprints". That accounts for 40. Table 1 lists a practitioner magazine article alongside them, and §6.4 says so explicitly: "11 records are preprints, and one is a practitioner magazine article". A reader who reconciles the abstract against Table 1 meets an unexplained one.

The sentence is not strictly false — it does not say the two categories exhaust the corpus — but in a review whose contribution is a coding ledger, the abstract's composition should sum, and the omission hides the one non-peer-reviewed, non-preprint category that the review's own evidence taxonomy has to handle. Add the third category to the abstract, or make the clause explicitly non-exhaustive.

### W5: The metadata-only exclusion sentence contradicts the evidence table
**Severity**: Minor
**Evidence Anchor**: text: "Metadata-only rows are cited only for what their title asserts, and they are excluded from every evidence count."

§3.2 states that the three title-level rows (P4, P7, R4) are excluded from every evidence count. Appendix B codes all three as assumption-level evidence, and Table 1's distribution — 17 proof, 16 numerical test, 8 assumption — sums to 41, which can only be reached if they are counted. The eight assumption rows are P4, P7, R4, R8, G3, C2, S4 and S5; removing the three title-level rows would leave five and a total of 38.

Either the sentence or the coding is wrong, and the reader cannot tell whether those rows were used as evidence of assertion or only as citation support. The review's frankness about title-level evidence is a virtue here, so the fix is to say what was actually done: the three rows count as assumption rows because a title asserting admissibility is itself the assertion, and they carry no further evidentiary weight.

### S1: The static/dynamic boundary is drawn correctly
**Evidence Anchor**: text: "Once the term is fixed to process-level consistency, the dynamic count returns to zero"

SC5 is kept where it belongs — a static condition on the maturity axis of a single surface — and §2.2 diagnoses the terminological trap that generates most of the confusion in this literature: a calendar condition is routinely called "calendar arbitrage" and read as dynamic. The diagnosis is correct, and the sentence that fixes the term is the right test. §2.1 also gets the sufficient-versus-exact distinction right: Gatheral and Jacquier (2013) supply sufficient SVI conditions, Martini and Mingone (2022) an exact characterisation, and the review states the consequence — a sufficient condition can exclude admissible surfaces — that a specialist would draw. This is the part of the manuscript that survives the correction in W1 unchanged.

### S2: The enforcement triple and the four-locus taxonomy are usable instruments
**Evidence Anchor**: text: "the corpus's one clear paired measurement, and it runs against the claim that a stronger guarantee buys a better fit"

§2.3's mechanism/evidence/verification triple separates the things the phrase "arbitrage-free" fuses, and the four loci — parameter domain, objective, output image, sampler with acceptance test — partition the 31 construction rows without an obvious remainder; the boundary rows (R3, R6, N1, C3, G7) are argued rather than waved through. The treatment of G6 is the model of what the rest of the review should do: the one row that reports both a structural guarantee and a finite-sample audit is reported against the interest of the paper's own thesis, which is what makes the disjointness finding credible.

### S3: The nearest-neighbour attribution is accurate
**Evidence Anchor**: text: "constructs a state space of statically arbitrage-free prices and explicitly limits its claim to static, model-independent admissibility (Cohen et al., 2021)"

The characterisation of Cohen, Reisinger and Wang (2021) matches what that paper says about itself: a state space of prices free from static, model-independent arbitrage, with neural networks constrained so that no-arbitrage conditions are preserved. The manuscript's further claim in §4.4 and Appendix C that the row explicitly disclaims a dynamic guarantee is consistent with the source's own scope. Getting the nearest neighbour right matters more than usual here, because the review's negative depends on not over-reading such disclaimers, and this instance is handled correctly.
