#!/usr/bin/env python3
"""Assemble stage4/paper-draft-v2.md from the drafted parts and generated appendices.

Inputs (all read-only):
  _build/part1.md .. part3.md      drafted body/references
  ../search/openalex_search.py     the 31 query strings (parsed with ast, never exec'd)
  ../search/screening_log.json     the 40 discretionary exclusions
  ../search/selected_sources.json  labels, family, coverage, level for the ledger
  ../coding-handbook.md            reproduced verbatim as Appendix D

Output: ../paper-draft-v2.md
"""
import ast
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGE4 = HERE.parent
CASE = STAGE4.parent
SEARCH = CASE / "search"

# ---------------------------------------------------------------- ledger coding
# id: (audit, static-subset, time-axis, dynamic code)
CODING = {
    "P1": ("N", "SC1–4 (+SC5 sep)", "N", "D0"), "P2": ("N", "SC1–4", "N", "D0"),
    "P3": ("N", "SC1–5", "N", "D0"), "P4": ("N", "SC1–5", "N", "D0"),
    "P5": ("N", "SC1–5", "N", "D0"), "P6": ("N", "SC1–5", "N", "D0"),
    "P7": ("N", "SC1–5", "N", "D0"), "P8": ("N", "SC1–3, 5", "Y", "D1"),
    "N1": ("N", "SC1–5", "N", "D0"), "N2": ("Y", "SC1–5", "N", "D0"),
    "N3": ("N", "SC1–5", "N", "D0"), "N4": ("N", "SC1–5", "N", "D0"),
    "N5": ("N", "SC1–5", "N", "D0"), "N6": ("Y", "SC2, 3, 5", "N", "D0"),
    "R1": ("N", "SC1–5", "N", "D0"), "R2": ("N", "SC1–5", "N", "D0"),
    "R3": ("N", "SC1–5", "N", "D0"), "R4": ("N", "SC1–5", "N", "D0"),
    "R5": ("Y", "SC3, 5", "N", "D0"), "R6": ("N", "SC1–5", "N", "D0"),
    "R7": ("Y", "SC1–3", "N", "D0"), "R8": ("N", "SC1–5", "Y", "D1"),
    "R9": ("N", "SC1–5", "N", "D0"),
    "G1": ("N", "SC1–5", "Y", "D2"), "G2": ("N", "SC1–5", "Y", "D0"),
    "G3": ("N", "SC1–5", "Y", "D0"), "G4": ("N", "SC1–5", "N", "D0"),
    "G5": ("Y", "SC1–3, 5", "N", "D0"), "G6": ("Y", "SC2, 3, 5", "N", "D0"),
    "G7": ("N", "SC1–5", "Y", "D2"), "G8": ("N", "SC1–5", "N", "D0"),
    "C1": ("N", "SC1–5", "N", "D0"), "C2": ("N", "SC1–5", "Y", "D1"),
    "C3": ("N", "SC1–5", "Y", "D2"), "C4": ("N", "SC1–3", "N", "D0"),
    "C5": ("N", "SC1–5", "Y", "D1"),
    "S1": ("N", "SC1–4 (+SC5 sep)", "N", "D0"), "S2": ("N", "SC1–3, 5", "N", "D0"),
    "S3": ("N", "SC3", "N", "D0"), "S4": ("N", "none", "N", "D0"),
    "S5": ("N", "none", "Y", "D0"),
}
# comparability carried unchanged from the v1.3 ledger
NC = {"P1", "P4", "P7", "P8", "R3", "R4", "R8", "C2", "C4", "C5", "S2"}

CLUSTER = re.compile(
    r"\)(<!--ref:[^>]*--><!--anchor:[^>]*-->); \(",
)
REF_SEC = re.compile(r"<!--ref:([A-Za-z0-9]+)[^>]*--><!--anchor:section:([\d.]+)-->")
AUDIT_OF = {k: v[0] for k, v in CODING.items()}


def esc(s):
    return re.sub(r"\s+", " ", str(s)).replace("|", "\\|").strip()


def queries():
    src = (SEARCH / "openalex_search.py").read_text(encoding="utf-8")
    tree = ast.parse(src)
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(t, ast.Name) and t.id == "QUERIES" for t in node.targets
        ):
            return [tuple(x) for x in ast.literal_eval(node.value)]
    raise SystemExit("QUERIES literal not found")


def cited_sections(body):
    seen = {}
    for slug, sec in REF_SEC.findall(body):
        seen.setdefault(slug, [])
        if sec not in seen[slug]:
            seen[slug].append(sec)
    out = {}
    for slug, secs in seen.items():
        out[slug] = ", ".join(sorted(secs, key=lambda s: [int(p) for p in s.split(".")]))
    return out


def main():
    body = "\n\n".join(
        (HERE / f"part{i}.md").read_text(encoding="utf-8").rstrip() for i in (1, 2, 3)
    )
    n_fixed = len(CLUSTER.findall(body))
    while True:
        new = CLUSTER.sub(r"\1; ", body)
        if new == body:
            break
        body = new
    cited = cited_sections(body)

    rows = {r["id"]: r for r in json.loads((SEARCH / "selected_sources.json").read_text())}
    log = json.loads((SEARCH / "screening_log.json").read_text())

    # ---- Table A1
    a1 = ["| **#** | **Group** | **Query string** |", "|---|---|---|"]
    for i, (group, q) in enumerate(queries(), 1):
        a1.append(f"| {i} | {group} | `{q}` |")
    a1 = "\n".join(a1)

    # ---- Table A2
    audit_re = re.compile(r"dynamic|martingale|forecast|multi-step|chain-consistent|wiener",
                          re.I)
    pool = [r for r in log["records"] if r["reason_code"] == "RELEVANT_NOT_SELECTED"]
    assert len(pool) == 40, len(pool)
    a2 = ["| **Log idx** | **Year** | **Title as retrieved** | **Reason recorded** | **Discussed in** |",
          "|---|---|---|---|---|"]
    audit_rows = []
    for r in sorted(pool, key=lambda x: x["index"]):
        note = (r.get("reason_note") or "").strip()
        if r["index"] == 42:
            reason = "code only; replacement note (A.3)"
            where = "Section 3.1; A.3"
        elif audit_re.search(r["title"]):
            reason = "code only; no record-level note"
            where = "Section 6.2 audit"
            audit_rows.append((r["index"], r["title"]))
        else:
            reason = "code only; no record-level note"
            where = "A.2 only"
        a2.append(f"| {r['index']} | {r['year']} | {esc(r['title'])} | {reason} | {where} |")
    a2 = "\n".join(a2)

    # ---- Table B
    b = ["| **ID** | **Source** | **Family** | **Evidence** | **Audit** | **Static** | "
         "**Time** | **Dyn** | **Level** | **Comp.** | **Coverage** | **Peer-reviewed** | "
         "**Cited in Section** |",
         "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for rid in CODING:
        r = rows[rid]
        audit, static, time, dyn = CODING[rid]
        cov = {"abstract": "full", "partial": "partial", "metadata-only": "metadata-only"}[
            r["abstract_status"]]
        pr = "yes" if r["peer_reviewed"] else (
            "no [preprint]" if "preprint" in r["flags"] else "no [practitioner outlet]")
        b.append(
            f"| {rid} | {esc(r['label'])} | {r['family_abbr'] if r['family_abbr'] in 'PNRGCS' else r['family']} "
            f"| {r['evidence_status']} | {audit} | {static} | {time} | {dyn} "
            f"| {r['quality_level']} | {'NC' if rid in NC else 'RC'} | {cov} | {pr} "
            f"| {cited.get(rid, '—')} |"
        )
    b = "\n".join(b)

    # ---- counts, used in the appendix notes and asserted
    n_audit = sum(1 for v in AUDIT_OF.values() if v == "Y")
    n_time = sum(1 for v in CODING.values() if v[2] == "Y")
    n_dyn = {c: sum(1 for v in CODING.values() if v[3] == c) for c in ("D0", "D1", "D2", "D3")}
    assert (n_audit, n_time, n_dyn["D2"], n_dyn["D1"], n_dyn["D0"]) == (6, 10, 3, 4, 34)

    handbook = (STAGE4 / "coding-handbook.md").read_text(encoding="utf-8")
    handbook = handbook.split("\n", 1)[1].strip()  # drop its own H1 title

    appendix = """
## Appendix A. Search and Screening Record

### A.1 The 31 query strings

The corpus was frozen before this manuscript was drafted and no new search was run for it. Retrieval targeted OpenAlex (English metadata and abstracts only) on 2026-11-23, using the 31 free-text queries below, each requesting up to 25 records over two pages, restricted to English-language records dated 2015-01-01 to 2026-11-23. The strings are reproduced verbatim from the retrieval script, one row per string, so that a third party can rerun the search and compare the included set.

@@A1@@

**Table A1 note.** The eight groups correspond to the eight strata in Section 3.1: broad (2), parametric construction (6), penalty and constrained learning (2), projection and repair (3), generation and filtering (6), neural and learning (6), dynamic and time-indexed (3), and evaluation and conditions (3). Each query returned up to 25 records; the union, de-duplicated by DOI and then by normalised title, is the 750-record retrieval set reported in Table 1.

### A.2 The 40 discretionary exclusions

Screening excluded 389 of the 430 unique records under eight mutually exclusive reason codes: off-topic (141), pre-2015 background (86), relevant but not selected (40), out-of-scope asset (34), publication type (32), duplicate version (31), forecasting or trading (21), and model-calibration or pricing (4). The arithmetic is checkable: 141 + 86 + 40 + 34 + 32 + 31 + 21 + 4 = 389, and 389 + 41 = 430. The 40 rows below are the discretionary class: records judged topically relevant at title level and not selected, under the frozen rule that caps the corpus at 35–45 sources, balances the families, and prefers the more recent or stronger record where two represent the same family.

The screening log records the reason code for every one of these 40 rows but records a record-level rationale for only one of them. Where no rationale is recorded, the table says so rather than reconstructing one; the coder's working notes for the remaining 39 rows were not retained in the frozen artifacts, so the only recoverable statement is the class-level rule above.

@@A2@@

**Table A2 note.** "Log idx" is the row's position in the frozen screening log, not a count; the log is retained with the run artifacts so a reader can resolve any index to its DOI. "Discussed in" names the section where the row is used, if anywhere: eight titles use time, forecasting, martingale, or chain-consistency vocabulary and were re-read at title level for the audit in Section 6.2, and every other row appears in this table only. Titles are given as retrieved, including any irregularity. No excluded record is cited in the manuscript, and none appears in the reference list.

### A.3 The two post-screening replacements

Two records were replaced after abstract-level reading, and both replacements were made for the same reason: the retrieved abstract did not fit the frozen inclusion rule, although the title had matched a query. The first, log index 42, priced options and computed implied volatilities with neural networks and made no arbitrage-enforcement claim; it was replaced by Wiedemann et al. (2025), whose abstract states an adherence result. The second, log index 89, derived no-arbitrage conditions for a delta-parameterised volatility surface estimated on foreign-exchange options and fell outside the equity-index asset scope; it was replaced by Fukasawa (2022), whose subject is the equity-index implied-volatility asymptotics. Neither record failed metadata resolution or abstract reconstruction: every one of the 41 included records resolved to a DOI-bearing index record, with a DOI lookup status of 200 and a title match of 1.0, and the abstract coverage reported in Table 1 is the coverage those records actually had. The two replacement decisions are recorded in the frozen screening log at the indices named, and the earlier draft's attribution of the replacements to resolution failure is withdrawn here as inaccurate.

## Appendix B. Evidence Ledger

Each row records the review's coding of one source, with the field definitions of Appendix D. **Evidence** is the status of the no-arbitrage claim as reported: proof, numerical test, or assumption. **Audit** is the independent property defined in D.3: whether the row reports a violation, residual, or defect statistic on its own output. **Static** names the subset of SC1–SC5 stated in Section 2.1 that the row's claim expresses, or `none` where no admissibility condition is claimed; a row that claims admissibility without enumerating conditions is coded SC1–5, because the claim is then the full predicate. **Time** is time-axis engagement as defined in D.4 (Y where the row's coded object is date-indexed). **Dyn** is the dynamic-enforcement code of D.5: D0 none, D1 declares a process-level condition without checking it, D2 inherits a model-class property, D3 states and checks a dynamic condition. **Level** is the evidence level of D.8: VI single study, VII expert commentary or narrative review. **Comp.** is the comparability class: DC directly comparable, RC reported for context, NC not comparable. **Coverage** is the abstract coverage available to the coder. **Cited in Section** lists the sections that cite the row, as coded in the text.

@@B@@

**Appendix B note.** The columns are the review's own coding; no row was re-coded for this version except that the two interpretive columns this version adds (Audit, Time, Dyn) were coded from the same frozen records under the rules in Appendix D, and the Static column states what earlier versions kept in the coding records only. The counts are recomputable from the columns: 17 proof + 16 numerical test + 8 assumption = 41; 6 audit rows (N2, N6, R5, R7, G5, G6), of which one is proof-level (G6); 10 Time = Y rows (P8, R8, G1, G2, G3, G7, C2, C3, C5, S5); dynamic codes D3 = @@D3@@, D2 = @@D2@@ (G1, G7, C3), D1 = @@D1@@ (P8, C2, C5, R8), D0 = @@D0@@; comparability 0 DC, 30 RC, 11 NC; coverage 34 full, 4 partial (R2, G3, C4, S1), 3 metadata-only (P4, P7, R4); peer review 29 yes and 12 no, the 12 comprising 11 preprints and the practitioner-magazine outlet S3; evidence level 40 VI and one VII (C2).

## Appendix C. Instrument Reconciliation, Boundary Cases, and Correction Record

### C.1 What was coded

The interpretive fields were coded from title, abstract, and bibliographic metadata under the operational definitions now printed in full as Appendix D: family; evidence status; audit; the static condition subset expressed; time-axis engagement; dynamic enforcement; evidence level; the market or dataset named; the fit or accuracy metric reported; and the comparability class. A claim is coded as evidence only where the record states it. A title-level claim is coded as unverified and is not used as evidence for any finding. The metadata-only rule, the preprint convention, and the evidence-level definitions are D.8; the recomputation table for every count the manuscript reports is D.10.

### C.2 Instrument reconciliation: the seven-axis and eight-axis frames

An earlier version of this study used an eight-axis evaluation instrument that added extrapolation and reproducibility to the seven axes of Table 6. This manuscript uses the seven-axis frame for two reasons: extrapolation and reproducibility were sparsely and inconsistently codeable at abstract level, and the seven-axis frame maps one-to-one onto the dimensions the corpus actually reports. The two instruments were compared row by row during the appraisal stage; the seven-axis frame is the aggregation of the eight-axis coding, the reconciliation is recorded with the coding records, and no count, verdict, or claim in this manuscript changes between them.

### C.3 Boundary cases

Five rows sit across family borders and are retained with the friction disclosed rather than reassigned. R3 is a repair built on an admissible reference function, so its mechanism is closer to construction; it stays in R because the repair locus is defined by the certified object, and R3 certifies its output. R6 claims a strict guarantee through parameter positivity, which is architecturally parametric, but its object is a completed surface, and it anchors the repair family's strict end. N1 enforces constraints architecturally, like the G-family rows, but its output is a single fitted surface rather than a generative model, which keeps it in N. G7 satisfies its constraints on a modelled state space and explicitly disclaims a dynamic-arbitrage guarantee, which is why it is coded D2 rather than D3. C3 builds a path-dependent model whose surfaces are static-admissible but whose dynamic consistency is not discussed, so it is coded D2 as well. A sixth row, C5, is a single-stock panel retained as a disclosed exception; it is the only longitudinal dynamic-adjacent evidence in the corpus and is never counted as index evidence.

### C.4 The SC3 correction and the rows it touches

The earlier version of Section 2.1 printed SC3 as $\\partial^{2} c/\\partial k^{2}\\ge 0$. The butterfly condition is $c''-c'\\ge 0$ on the normalised call price in log-moneyness, and Section 2.1 now states it that way with the derivation and the two boundary relations. The correction is to the review's predicate, not to any row's claim, and the re-examination therefore takes the following form.

Thirty-nine of the 41 rows state a condition subset that includes SC3; S4 and S5 claim no admissibility condition and are the two exceptions. Every one of the 39 was re-read against the corrected form. No row's evidence status, audit code, time-axis code, dynamic code, or comparability code changes, because each of those columns records the mode of verification, the object coded, or the reporting protocol, and none of them was assigned from the algebraic form of the condition: a row that reports a residual at a stated tolerance is a numerical test whether the condition it tests is written as $c''\\ge 0$ or as $c''-c'\\ge 0$, and a row whose parameter domain guarantees every admissible vector is a proof under either form. The rows whose abstracts name conditions in the corrected family are N6 and G6 (convexity of the call price in log-moneyness together with non-negative maturity ramps), R5, G5 and S2 (calendar monotonicity with call-spread or butterfly conditions), and R7 and R6 (call-spread and butterfly conditions as linear inequalities); all seven are coded as before, and the two rows whose abstracts describe convexity in log-moneyness terms (G6 and S3) are unchanged, because the stronger printed form was sufficient for the claim each paper makes about its own construction. What changed is the review's statement of the predicate and its consistency with SC4; what did not change is any count, verdict, or family assignment.

### C.5 Withdrawal of the A/B/C appraisal grades

The earlier version reported a composite appraisal grade (A 11, B 13, C 17) per row. The grade is withdrawn from this version. Two of its six criteria were free-text judgements that the frozen ledger does not carry, so a reader could not recompute a single grade from Appendix B, and printing them would present a judgement as a derivation. The evidence-level label of D.8 is retained instead, because it is a published hierarchy level rather than a composite, it is defined in the manuscript, and it can be checked against the record. No finding in Sections 4 and 5 used the composite grade: the family distributions in Tables 3, 5 and 6 are tallies of evidence status, comparability, and coverage, and the one place the grade appeared in the body was a description of the appraisal instrument, which now describes the evidence-level axis instead.

## Appendix D. Coding Handbook

The handbook below is the operational definition of every ledger field. It was written so that a second analyst working only from the 41 frozen records and this document can reproduce Appendix B row by row, and it fixes the reliability protocol used for the stratified second-coder recheck reported in Section 3.4.

@@HAND@@
"""
    for tok, val in (("@@A1@@", a1), ("@@A2@@", a2), ("@@B@@", b), ("@@HAND@@", handbook),
                     ("@@D0@@", str(n_dyn["D0"])), ("@@D1@@", str(n_dyn["D1"])),
                     ("@@D2@@", str(n_dyn["D2"])), ("@@D3@@", str(n_dyn["D3"]))):
        appendix = appendix.replace(tok, val)
    out = body.rstrip() + "\n" + appendix
    (STAGE4 / "paper-draft-v2.md").write_text(out, encoding="utf-8")
    print(f"citation clusters normalised: {n_fixed}")
    print(f"appendix audit rows (temporal titles): {[i for i, _ in audit_rows]}")
    print(f"ledger: audit={n_audit} time={n_time} dyn={n_dyn}")
    print(f"rows without a body citation: {[k for k in CODING if k not in cited]}")
    print(f"wrote {STAGE4 / 'paper-draft-v2.md'} ({len(out)} chars)")


if __name__ == "__main__":
    main()
