#!/usr/bin/env python3
"""Build the Phase 2 deliverables from the artifacts produced in search/.

Inputs (search/):
  openalex_candidates.json  the 430-record fresh discovery pool with queries
  selected_index.json       the 41 selected records (id, family, doi, ...)
  fetch_results.json        OpenAlex/Crossref/S2 metadata + abstract per record
  retrieval_log.json        per-record retrieval status
  screening_log.json        per-record title-screening reason codes + counts
  annotations.py            reviewer-authored annotations (single source of truth)

Outputs:
  search/selected_sources.json   canonical corpus (required Phase 2 schema + extras)
  search/selected_sources.md     flat corpus listing
  search/screening_summary.md    PRISMA-style flow, criteria, reason codes
  phase2-bibliography.md
  phase2-verification.md

The script never invents data: every field comes from the fetched records or
from annotations.py, and abstract_status/abstract_source are carried through
so the prose can state where each abstract came from.
"""
from __future__ import annotations

import json
import re
from collections import Counter, OrderedDict
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
RUN = HERE.parent

import sys

sys.path.insert(0, str(HERE))
from annotations import A, FAMILIES, ORDER  # noqa: E402

POOL = json.loads((HERE / "openalex_candidates.json").read_text(encoding="utf-8"))
INDEX = json.loads((HERE / "selected_index.json").read_text(encoding="utf-8"))
FETCH = {x["id"]: x for x in json.loads((HERE / "fetch_results.json").read_text(encoding="utf-8"))}
RLOG = {x["id"]: x for x in json.loads((HERE / "retrieval_log.json").read_text(encoding="utf-8"))}
SCREEN = json.loads((HERE / "screening_log.json").read_text(encoding="utf-8"))

LAST_SEARCH = date.fromisoformat(POOL["generated_at"][:10]).isoformat()

# ---------------------------------------------------------------- helpers


def apa_authors(authors: str) -> str:
    return authors


def surnames(authors: str) -> list[str]:
    segs = [s.strip() for s in re.split(r",\s*&\s*|\s*&\s*", authors) if s.strip()]
    out: list[str] = []
    for seg in segs:
        parts = [p.strip() for p in seg.split(",") if p.strip()]
        for i in range(0, len(parts) - 1, 2):
            out.append(parts[i])
    return out


def label_for(sid: str) -> str:
    a = A[sid]
    names = surnames(a["authors"])
    if len(names) >= 3:
        return f"{names[0]} et al. ({a['year']})"
    if len(names) == 2:
        return f"{names[0]} & {names[1]} ({a['year']})"
    return f"{names[0] if names else '?'} ({a['year']})"


def apa_citation(sid: str) -> str:
    a = A[sid]
    venue = a["venue_md"]
    doi = (FETCH[sid]["record"].get("doi") or a.get("doi") or "").strip()
    doi_url = f" https://doi.org/{doi}" if doi else ""
    if a["kind"] == "preprint":
        return f"{a['authors']} ({a['year']}). {a['title']} [Preprint]. {venue}.{doi_url}"
    if a["kind"] == "conference":
        return f"{a['authors']} ({a['year']}). {a['title']}. In {venue}.{doi_url}"
    return f"{a['authors']} ({a['year']}). {a['title']}. {venue}.{doi_url}"


def plain_venue(sid: str) -> str:
    a = A[sid]
    v = a["venue_md"].replace("*", "")
    v = re.sub(r"\s*\(pp\..*?\)$", "", v).strip()
    return v


def biblio_str(sid: str) -> str:
    b = FETCH[sid]["record"].get("biblio") or {}
    v, i, p1, p2 = b.get("volume"), b.get("issue"), b.get("first_page"), b.get("last_page")
    bits = []
    if v:
        bits.append(str(v) + (f"({i})" if i else ""))
    if p1:
        bits.append(str(p1) + (f"–{p2}" if p2 else ""))
    return ", ".join(bits)


def abstract_source_label(sid: str) -> str:
    st = FETCH[sid]["abstract_status"]
    src = FETCH[sid].get("abstract_source")
    names = {"openalex": "OpenAlex", "crossref": "Crossref", "semanticscholar": "Semantic Scholar", None: "none"}
    if st == "abstract":
        return f"full ({names.get(src, src)})"
    if st == "partial":
        return f"partial ({names.get(src, src)})"
    return "metadata-only (no abstract)"


def md_table(headers: list[str], rows: list[list[str]]) -> str:
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out)


def counts_md(counter: Counter, order: list[str] | None = None) -> list[str]:
    keys = order or sorted(counter, key=lambda k: (-counter[k], str(k)))
    return [f"- {k}: {counter[k]}" for k in keys if counter[k]]


# ---------------------------------------------------------------- corpus

FAM_ORDER = OrderedDict(
    [
        ("P", "Parametric construction"),
        ("N", "Penalty and constrained learning"),
        ("R", "Projection and repair"),
        ("G", "Generation and filtering"),
        ("C", "Constraint conditions and evaluation"),
        ("S", "Seminal pre-2015 baselines"),
    ]
)

corpus = []
for sid in ORDER:
    a = A[sid]
    rec = FETCH[sid]["record"]
    idx_item = next(x for x in INDEX if x["id"] == sid)
    assert idx_item["family"] == sid[0], (sid, idx_item["family"])
    evidence = a["evidence"]
    if sid in ("P4", "P7", "R4"):  # metadata-only: never grade the claim as verified
        evidence = "assumption"
    corpus.append(
        {
            "id": sid,
            "label": label_for(sid),
            "family_abbr": sid[0],
            "family_code": FAMILIES[sid[0]][1],
            "family": FAMILIES[sid[0]][0],
            "title": a["title"],
            "authors": a["authors"],
            "year": a["year"],
            "venue": plain_venue(sid),
            "venue_short": a["venue_short"],
            "venue_kind": a["kind"],
            "doi": rec.get("doi"),
            "type": rec.get("type"),
            "biblio": biblio_str(sid),
            "peer_reviewed": bool(a["peer"]),
            "evidence_status": evidence,
            "evidence_note": a["evidence_note"],
            "abstract_status": FETCH[sid]["abstract_status"],
            "abstract_source": FETCH[sid].get("abstract_source"),
            "quality_level": a["level"],
            "constraints": a["constraints"],
            "key_finding": a["finding"],
            "relevance": a["relevance"],
            "comparability": a["comparability"],
            "method_weakness": a["weakness"],
            "flags": a["flags"],
            "openalex_id": rec.get("openalex_id"),
            "deposited_title": rec.get("title"),
            "retrieval": RLOG.get(sid, {}),
        }
    )
CORP = {c["id"]: c for c in corpus}

# ---------------------------------------------------------------- screening summary

screen_counts = SCREEN["counts"]
flow_rows = [
    ["OpenAlex records retrieved (31 queries x top 25, deduplicated)",
     str(len(POOL["records"])), "Fresh discovery, not the prior example corpus"],
    ["Excluded at title level", str(sum(v for k, v in screen_counts.items() if k != "INCLUDED")),
     "Reason codes in the table below"],
    ["Included in the corpus", str(screen_counts.get("INCLUDED", 0)), "Target 35-45; all four families covered"],
]
reason_rows = []
for code, note in SCREEN["criteria"].items():
    if code == "INCLUDED":
        continue
    reason_rows.append([code, str(screen_counts.get(code, 0)), note])

prisma_style = "\n".join(
    [
        "```",
        "Records identified through OpenAlex API (31 queries x 25 records/query; one query returned none after retry)",
        f"  pool after cross-query deduplication ......... {len(POOL['records'])}",
        f"  excluded at title screening .................. {sum(v for k, v in screen_counts.items() if k != 'INCLUDED')}",
        f"  included ..................................... {screen_counts.get('INCLUDED', 0)}",
        "     abstracts read for confirmation ............ 41",
        "     replaced during abstract-level reading ..... 2 (documented in the screening log)",
        "```",
    ]
)

screening_md = f"""# Phase 2 screening summary (PRISMA-style, not PRISMA-compliant)

Run directory: `examples/dsh/iv-surface-review-v047/`. Discovery date: {LAST_SEARCH}.
Screening level: title for the full pool, abstract for the included set only.
Reviewer model: a single research agent (no dual screening, no kappa).

## Flow

{prisma_style}

Two records were replaced after abstract-level reading, because the title
matched the topic but the abstract did not fit the research question:

- N2 (old): Liu, Oosterlee & Bohte (2019), *Pricing options and computing
  implied volatilities using neural networks* (Risks) - no arbitrage-enforcement
  claim; replaced by Wiedemann, Jacquier & Gonon (2025). Reason code in the log:
  `RELEVANT_NOT_SELECTED` with the replacement note.
- C4 (old): Wang, Zhao & Bao (2018), *Arbitrage-free conditions for implied
  volatility surface by Delta* - FX-market empirics, outside the equity-index
  scope; replaced by Fukasawa (2022). Reason code: `OUT_OF_SCOPE_ASSET`.

The log stores the post-replacement state; both removed records remain visible
with their overrides rather than being silently reclassified by the generic
title rules.

## Reason codes and counts

{md_table(["Reason code", "n", "Meaning"], reason_rows)}

The {screen_counts.get('RELEVANT_NOT_SELECTED', 0)} `RELEVANT_NOT_SELECTED`
records are a real cap-and-balance bucket, not noise: they are topically
relevant titles that lost to corpus-size limits (35-45), family balance or
version precedence. They are disclosed as a selection-bias guard in the
bibliography and are the first place to look if the corpus is expanded.

## Screening limitations

- Title-level decisions use keyword rules; they are reproducible but not
  semantic, so some off-topic titles may sit in `OFF_TOPIC` for the wrong
  sub-reason.
- No dual screening, no adjudication, no inter-rater reliability; this is
  PRISMA-*style* reporting only.
- One discovery query failed even after retry (`SVI stochastic volatility
  inspired`, transient OpenAlex 429), so the pool is not exhaustive.
- OpenAlex language tags were unreliable (two English papers are tagged `it`), so language was checked at title/abstract level; the one Korean record was already outside the 2015-2026 window. No translation screening.
"""
(HERE / "screening_summary.md").write_text(screening_md, encoding="utf-8")

# ---------------------------------------------------------------- selected sources

(HERE / "selected_sources.json").write_text(
    json.dumps(corpus, indent=2, ensure_ascii=False), encoding="utf-8"
)

ss_md = [
    "# Selected sources (canonical corpus)",
    "",
    f"41 records, fresh discovery via OpenAlex on {LAST_SEARCH}. "
    "Machine-readable companion: `selected_sources.json`.",
    "",
    md_table(
        ["ID", "Label", "Family", "Year", "Venue", "Evidence", "Abstract"],
        [
            [c["id"], c["label"], c["family"], c["year"], c["venue_short"],
             c["evidence_status"], c["abstract_status"]]
            for c in corpus
        ],
    ),
]
(HERE / "selected_sources.md").write_text("\n".join(ss_md) + "\n", encoding="utf-8")

# ---------------------------------------------------------------- shared corpus stats

fam_counts = Counter(c["family"] for c in corpus)
ev_counts = Counter(c["evidence_status"] for c in corpus)
abs_counts = Counter(c["abstract_status"] for c in corpus)
peer_yes = sum(1 for c in corpus if c["peer_reviewed"])
preprint_n = sum(1 for c in corpus if c["venue_kind"] == "preprint")
magazine_n = sum(1 for c in corpus if c["venue_kind"] == "magazine")
journal_n = sum(1 for c in corpus if c["venue_kind"] == "journal")
conf_n = sum(1 for c in corpus if c["venue_kind"] == "conference")
old_n = sum(1 for c in corpus if c["year"] < 2015)
new_recent = sum(1 for c in corpus if c["year"] >= 2021)

year_buckets = OrderedDict(
    [
        ("pre-2015 (explicit seminal baselines)", sum(1 for c in corpus if c["year"] < 2015)),
        ("2015-2019", sum(1 for c in corpus if 2015 <= c["year"] <= 2019)),
        ("2020-2022", sum(1 for c in corpus if 2020 <= c["year"] <= 2022)),
        ("2023-2026", sum(1 for c in corpus if c["year"] >= 2023)),
    ]
)

# studies whose abstracts name a market (hand-checked, abstract text only)
MARKETS = {
    "N1": "S&P 500 options",
    "N2": "S&P 500 intraday options",
    "N4": "JSE ALSI index options (South Africa)",
    "R5": "SPX options",
    "R6": "S&P 500 index options",
    "R9": "SPY options",
    "G2": "SPX options",
    "G3": "SPX options",
    "G7": "Heston SLV simulated data (no market)",
    "C3": "S&P 500 / VIX context",
    "S1": "SPX options",
    "S4": "CBOE S&P 500 options",
    "S5": "DAX index options",
}
known_market_n = sum(1 for v in MARKETS.values() if "simulated" not in v)
us_market_n = sum(1 for v in MARKETS.values() if "simulated" not in v and ("S&P" in v or "SPX" in v or "SPY" in v))

# ---------------------------------------------------------------- bibliography

QUERY_GROUPS: OrderedDict[str, list[dict]] = OrderedDict()
for q in POOL["queries"]:
    QUERY_GROUPS.setdefault(q["stratum"], []).append(q)

query_lines = []
for stratum, qs in QUERY_GROUPS.items():
    qstrs = [q["query"] + (" [failed: HTTP 429]" if q.get("error") else "") for q in qs]
    query_lines.append(f"- **{stratum}** ({len(qs)}): " + "; ".join(f"`{s}`" for s in qstrs))

inclusion_rows = [
    ["IC1 topic", "Implied-volatility or option-price surface construction and/or its no-arbitrage constraints."],
    ["IC2 asset scope", "Equity-index listed options, or a method whose abstract makes the index application explicit; FX/rates/commodities/energy/crypto and single-name panels excluded."],
    ["IC3 window", "2015-2026 for the working corpus; pre-2015 records enter only as explicitly flagged seminal baselines (n=5, cap respected)."],
    ["IC4 language", "English."],
    ["IC5 publication status", "Peer-reviewed research preferred; preprints eligible when directly on enforcement and graded; preprints <= 30% of corpus."],
    ["IC6 retrievability", "OpenAlex record resolvable by DOI or title; abstract retrieved when available; missing abstracts are kept but never upgraded to abstract-level claims."],
    ["IC7 version rule", "One record per study; peer-reviewed version preferred over preprint where both exist."],
]
exclusion_rows = [
    ["OFF_TOPIC", "Title lacks any implied-volatility/option-surface or no-arbitrage term, or is not a construction/condition study."],
    ["PRE_2015_BACKGROUND", "Outside the 2015-2026 window; retained as background only."],
    ["RELEVANT_NOT_SELECTED", "Topically relevant but lost to the 35-45 cap, family balance, recency or version precedence."],
    ["OUT_OF_SCOPE_ASSET", "Underlying is FX, rates, commodities, energy, crypto, a single stock, or a non-financial domain."],
    ["PUBLICATION_TYPE", "Dissertation, book, software/replication package, paratext or other ineligible type."],
    ["DUPLICATE_VERSION", "Same study as another pool record (same DOI or near-identical title)."],
    ["FORECASTING_OR_TRADING", "Forecasting, hedging or trading application rather than a construction/enforcement method."],
    ["MODEL_CALIBRATION_PRICING", "Stochastic-volatility model calibration/pricing without surface-construction enforcement."],
]

bib: list[str] = []
bib.append("# Phase 2 - Annotated Bibliography")
bib.append("")
bib.append("**Research question.** How do parametric construction, penalty, projection-repair, and "
           "generation-filtering methods for constructing equity-index implied volatility surfaces "
           "enforce static and dynamic no-arbitrage constraints?")
bib.append("")
bib.append(f"**Run context.** ARS v3.24.4 end-to-end validation, Stage 1 (deep-research, `full` mode), "
           f"Phase 2 (INVESTIGATION). Abstract-level verification only; discovery date {LAST_SEARCH}. "
           "Companion report: `phase2-verification.md`. Machine-readable corpus: "
           "`search/selected_sources.json`. Screening log: `search/screening_log.json`.")
bib.append("")
bib.append("**How to read the evidence status labels.** `proof` = the abstract states a theorem, "
           "construction or guarantee that is proved in the paper. `numerical test` = the abstract "
           "reports an empirical or synthetic evaluation of a method, but no arbitrage-freeness "
           "theorem. `assumption` = the abstract asserts or implies enforcement without a proof or "
           "a test that is visible at abstract level, or no abstract could be retrieved. A numerical "
           "test is never upgraded to a proof in this run, and a title-level claim is never treated "
           "as evidence.")
bib.append("")
bib.append("## 1. Search strategy")
bib.append("")
bib.append("**Databases and sources.** OpenAlex REST API (fresh discovery, no API key, anonymous "
           "rate limit of about one request per second; 31 queries x 25 relevance-ranked records, one of which "
           "returned no records after retry). "
           "Crossref REST API and Semantic Scholar Graph API were used only to recover abstracts "
           "that OpenAlex did not deposit - they did not contribute candidates. DOI resolution was "
           "checked against OpenAlex (all 41) and Crossref (the 4 records recovered from it).")
bib.append("")
bib.append(f"**Date range.** 2015-01-01 to {LAST_SEARCH} for the working corpus; pre-2015 only as "
           "flagged seminal baselines. **Last search:** " + LAST_SEARCH + ". **Language:** English.")
bib.append("")
bib.append("**Queries (OpenAlex free-text search, one request per query, top 25 records kept per query).** "
           "OpenAlex relevance search is not a Boolean API, so the Boolean forms below describe the "
           "concept blocks the queries operationalise, not literal request syntax.")
bib.append("")
bib.extend(query_lines)
bib.append("")
bib.append("**Boolean concept blocks used to organise the query set.**")
bib.append("")
bib.append("- Broad: (`implied volatility surface` OR `volatility surface`) AND (`arbitrage` OR `arbitrage-free` OR `no-arbitrage`).")
bib.append("- Parametric: (`SVI` OR `SSVI` OR `SABR` OR `parametric volatility` OR `volatility parametrization`) AND (`arbitrage` OR `no-arbitrage`).")
bib.append("- Penalty: (`deep smoothing` OR `neural network` OR `machine learning` OR `penalty`) AND (`no-arbitrage` OR `arbitrage-free`) AND `implied volatility`.")
bib.append("- Projection/repair: (`projection` OR `repair` OR `Sinkhorn` OR `shape constrained` OR `arbitrage-free interpolation` OR `surface completion`).")
bib.append("- Generation/filtering: (`GAN` OR `VAE` OR `generative model` OR `diffusion` OR `flow matching` OR `neural SDE`) AND `implied volatility`.")
bib.append("- Dynamic/evaluation: (`dynamic arbitrage` OR `calendar spread` OR `static arbitrage` OR `no arbitrage conditions` OR `martingale` OR `detect` OR `test violation`) AND (`implied volatility` OR `option surface`).")
bib.append("")
bib.append("**Inclusion criteria.** " + " ".join(f"({r[0]}) {r[1]}" for r in inclusion_rows))
bib.append("")
bib.append("**Exclusion criteria and reason codes.** " + " ".join(f"({r[0]}) {r[1]}" for r in exclusion_rows))
bib.append("")
bib.append("## 2. Screening flow (PRISMA-style, not PRISMA-compliant)")
bib.append("")
bib.append(prisma_style)
bib.append("")
bib.append("| Reason code | n |")
bib.append("|---|---|")
for code in ["OFF_TOPIC", "PRE_2015_BACKGROUND", "RELEVANT_NOT_SELECTED", "OUT_OF_SCOPE_ASSET",
             "PUBLICATION_TYPE", "DUPLICATE_VERSION", "FORECASTING_OR_TRADING", "MODEL_CALIBRATION_PRICING"]:
    bib.append(f"| {code} | {screen_counts.get(code, 0)} |")
bib.append(f"| **Included** | **{screen_counts.get('INCLUDED', 0)}** |")
bib.append("")
bib.append("Screening was performed by one reviewer at title level for the whole pool, with abstract-level "
           "confirmation only for the included set; there was no dual screening, adjudication or kappa. "
           "Two candidates were replaced after abstract reading (old N2: neural-network IV computation with "
           "no enforcement claim; old C4: FX-oriented Delta conditions) and their replacements are recorded "
           "in the log through explicit overrides. The 40 `RELEVANT_NOT_SELECTED` records are a genuine "
           "cap/balance bucket and are disclosed as a selection-bias guard.")
bib.append("")
bib.append("## 3. Corpus profile")
bib.append("")
bib.append(md_table(
    ["Dimension", "Distribution"],
    [
        ["Family", "; ".join(f"{k} {v} ({v/len(corpus)*100:.1f}%)" for k, v in fam_counts.items())],
        ["Evidence status", "; ".join(f"{k} {v}" for k, v in ev_counts.most_common())],
        ["Peer review", f"peer-reviewed {peer_yes} ({peer_yes/len(corpus)*100:.1f}%); "
                        f"preprints {preprint_n} ({preprint_n/len(corpus)*100:.1f}%); "
                        f"practitioner magazine {magazine_n}; "
                        f"journal {journal_n}; conference {conf_n}"],
        ["Abstract retrieval", "; ".join(f"{k} {v}" for k, v in abs_counts.most_common())],
        ["Time", "; ".join(f"{k} {v}" for k, v in year_buckets.items())],
    ],
))
bib.append("")

# family sections
FAMILY_SYNTH = {
    "P": "All eight works push the guarantee into the parametrisation itself: a restricted parameter "
         "domain (P1, P2), a global all-maturity construction (P3), a structural interpolation (P6), "
         "a widened admissible family (P5), or - per title only - a calibration constrained to the "
         "no-arbitrage region (P4, P7). Evidence is `proof` wherever an abstract exists; P4 and P7 are "
         "metadata-only, so their mechanism is a title-level indication only and is never used as an "
         "abstract-level claim. Only P2, P3 and S1 report market calibration in their abstracts, "
         "and none reports a finite-sample violation audit of the calibrated surface. No work in this "
         "family addresses dynamic arbitrage: the guarantee is per-surface (static), applied anew at "
         "each calibration time.",
    "N": "The six penalty/constrained-learning works trade guarantees for flexibility: soft penalties "
         "(N3, N4, N5), derivative-constrained losses (N6), architectural gates (N1) and operator "
         "learning (N2). N2's abstract is the most explicit ('adheres to critical no-arbitrage "
         "constraints'), N1 claims its architecture satisfies the constraints by construction, and N5's "
         "title already concedes that violations are only minimised. None of the "
         "abstracts reports a violation-rate distribution, so every entry here is a `numerical test`, "
         "not a guarantee, and the phase-3 synthesis must keep them in that bucket.",
    "R": "Projection/repair works restore admissibility after the fact: linear-program repairs inside "
         "bid-ask bounds (R1), entropic optimal transport (R2), construction-by-distortion (R3), joint "
         "call/put smoothing (R4), observation-anchored grid repair (R5), a strictly arbitrage-free "
         "non-parametric representation (R6), constrained Chebyshev bases with a post-fit correction "
         "(R7), transport-inspired surface transforms (R8) and Markov-chain approximations (R9). "
         "R1, R5 and R7 report explicit violation or coverage numbers; they are not comparable with "
         "each other because data, grid and tolerances differ. R2, R3 and R6 claim convergence or "
         "construction guarantees; R8 asserts arbitrage-freeness without a proof at abstract level.",
    "G": "Generation works either sample inside a guaranteed-admissible parameter space (G1, G7, G8, "
         "and G6's architectural hard constraints) or train penalty-regularised generators (G2, G4, "
         "G5, N5). The guarantee, where it exists, is inherited from the parameterisation or "
         "architecture; penalty-based generators minimise violations without proving their absence. "
         "G5 is the most explicit about its empirical limit (90.8% of generated surfaces pass all "
         "tested static conditions), and G6 quantifies the accuracy cost of a hard guarantee. Dynamic "
         "arbitrage is not proved by any generator; the static constraints are applied surface by "
         "surface, including when surfaces are generated over time.",
    "C": "Constraint/evaluation works supply the condition vocabulary and the diagnostics the other "
         "families rely on: a review of static and dynamic conditions (C2, the only source that "
         "explicitly discusses dynamic arbitrage), a model-free static-arbitrage detector (C1), a "
         "path-dependent surface model whose static core is SSVI (C3), an asymptotic arbitrage-freeness "
         "result for BBR/SABR/rough-SABR formulas (C4), and a single-stock martingale-defect diagnostic "
         "(C5, scope-flagged). They are not construction methods, and their evidence status reflects "
         "that: proof for the two formal results, numerical test for the two empirical diagnostics, "
         "assumption for the narrative review.",
    "S": "The five pre-2015 baselines anchor the lineage: SVI calibration (S1), shape-constrained "
         "smoothing (S2), SABR density correction (S3), nonparametric inversion (S4) and a dynamic "
         "factor model (S5). S1 and S2 are directly relevant enforcement constructions; S3 shows that "
         "an explicit smile formula can be arbitrageable in finite strike, which is the tension that "
         "C4 later resolves asymptotically; S4 and S5 are pre-constraint baselines and are used only "
         "to frame what enforcement added. Currency is not penalised for these records because their "
         "role is foundational, not current-best-practice.",
}

for code, full in FAM_ORDER.items():
    members = [c for c in corpus if c["family_code"] == FAMILIES[code][1]]
    bib.append(f"## 4.{list(FAM_ORDER).index(code)+1} {full} (n={len(members)})")
    bib.append("")
    bib.append(FAMILY_SYNTH.get(code, ""))
    bib.append("")
    for c in members:
        a = A[c["id"]]
        bib.append(f"#### {c['id']} - {c['label']}")
        bib.append("")
        bib.append(f"**APA:** {apa_citation(c['id'])}")
        bib.append("")
        bib.append(
            f"- **Family:** {c['family']} | **Evidence status:** `{c['evidence_status']}` | "
            f"**Abstract:** {abstract_source_label(c['id'])} | **Quality level:** {c['quality_level']} | "
            f"**Peer-reviewed:** {'yes' if c['peer_reviewed'] else 'no'}"
        )
        bib.append(f"- **Relevance:** {a['relevance']}")
        bib.append(f"- **Key findings:** {a['finding']}")
        bib.append(f"- **Method & evidence:** {a['evidence_note']}")
        bib.append(f"- **Method weaknesses:** {a['weakness']}")
        bib.append(f"- **Comparability:** {a['comparability']}")
        flags = [f for f in a["flags"] if f not in ("preprint",)]
        if flags:
            bib.append(f"- **Flags:** {', '.join(flags)}")
        bib.append("")

bib.append("## 5. Coverage-distribution advisory")
bib.append("")
bib.append("No single method family exceeds 70% of the corpus, so the family distribution does not "
           "trigger the distributional-skew rule on its own. The time distribution is the skew that "
           f"matters: {year_buckets['2023-2026']} of {len(corpus)} sources "
           f"({year_buckets['2023-2026']/len(corpus)*100:.0f}%) are from 2023-2026 and only "
           f"{old_n} are pre-2015, the latter by design (seminal baselines). This is a recency skew "
           "inherent to the search ranking plus the fast growth of ML-based surface methods; it is not "
           "evidence that older enforcement methods stopped working. Non-seminal sources older than "
           f"five years at the search date (2020 or earlier): {sum(1 for c in corpus if c['year'] <= int(LAST_SEARCH[:4]) - 6 and 'seminal' not in c['flags'])}"
           f" / {len(corpus)} "
           f"({sum(1 for c in corpus if c['year'] <= int(LAST_SEARCH[:4]) - 6 and 'seminal' not in c['flags'])/len(corpus)*100:.1f}%), "
           "within the <=30% guidance.")
bib.append("")
bib.append("**Data provenance skew.** Of the 12 sources whose abstracts name a market that is not a "
           f"simulation, {us_market_n} use US equity-index data (SPX/SPY/CBOE S&P 500) and 2 use non-US "
           "indices (DAX, JSE ALSI). US index data therefore account for about "
           f"{us_market_n/known_market_n*100:.0f}% of the known provenance, which crosses the 70% "
           "advisory threshold. Consequences: violation-rate and fit numbers in this corpus should not "
           "be read as field-wide properties, and evidence about non-US index surfaces is thin "
           "(one German study, DAX 2006; one South African study, JSE ALSI 2022). Geographic distribution of "
           "authors and venues was not collected, so no author-country skew is claimed.")
bib.append("")
bib.append("**Venue-type skew.** Preprints are 26.8% (11/41), just inside the 30% ceiling, but they "
           "carry a disproportionate share of the most recent (2025-2026) evidence: 6 of the 11 "
           "preprints are from 2025-2026. The synthesis should therefore treat recent-generation "
           "claims as provisional until peer review.")
bib.append("")

bib.append("## 6. Evidence-status ledger (Devil's Advocate fix 1)")
bib.append("")
bib.append("Every source is listed with what it actually establishes at abstract level and what would "
           "be needed before its claim could be called arbitrage-free.")
bib.append("")
bib.append(md_table(
    ["ID", "Enforcement mechanism (abstract)", "Status", "What would upgrade it"],
    [
        [c["id"],
         {
             "P": "Parametrisation / parameter-domain restriction",
             "N": "Penalty, constraint loss or architectural gate",
             "R": "Post-hoc projection, repair or constrained construction",
             "G": "Guaranteed parameter space or penalty-regularised generator",
             "C": "Condition statement or diagnostic",
             "S": "Baseline construction",
         }[c["family_abbr"]],
         c["evidence_status"],
         {"proof": "Full-text theorem check (abstract-only here)",
          "numerical test": "Explicit violation audit with tolerance and independent replication",
          "assumption": "Retrieve the abstract/full text and identify a proof or a test"}[c["evidence_status"]],
         ]
        for c in corpus
    ],
))
bib.append("")
bib.append("For the three metadata-only records (P4, P7, R4) the ledger status is `assumption` even "
           "where the title asserts a result; the TITLE is not evidence. For the four partial-abstract "
           "records (R2, G3, C4, S1) claims are limited to what the retrieved fragment states.")
bib.append("")

bib.append("## 7. Comparability flags (Devil's Advocate fix 2)")
bib.append("")
bib.append("The corpus uses the words 'arbitrage', 'violation' and 'fit' with different operational "
           "meanings. The following buckets are `reported for context, not comparable`:")
bib.append("")
bib.append("- **Violation-rate bucket** (G6 synthetic SVI, tolerance 1e-4; G5 generated surfaces, "
           "all-tested-conditions pass rate; R5 SPX grid completion, butterfly floor about 5.4%; R7 "
           "equity panels, <1% with 98-99% inside spread). Different data, grids and tolerances; no "
           "ranking is implied.")
bib.append("- **Fit / forecasting / hedging bucket** (N1 out-of-sample forecasting and hedging; N2 "
           "accuracy and subsampling robustness; G2 hedging performance; R9 speed/adequacy; N4 "
           "Wasserstein distance to historical surfaces). These are not arbitrage metrics.")
bib.append("- **Exact-construction bucket** (P1, P2, P3, P5, P6, R2, R3, R6, G1, G7, G8, S1, C4). "
           "A guarantee is claimed by construction; no comparative metric is reported, so no "
           "cross-family comparison is possible.")
bib.append("- **Not evaluable bucket** (P4, P7, R4): metadata only.")
bib.append("")

bib.append("## 8. Selection and recency guard (Devil's Advocate fix 3)")
bib.append("")
bib.append("- The corpus is fresh (OpenAlex, 31 queries, 430 unique records) and does not reuse the "
           "previous example's 40 sources; overlap is incidental, not imported.")
bib.append("- Classical parametric baselines are deliberately over-sampled against the recency "
           "ranking: 5 pre-2015 seminal works plus the full 2015-2026 SVI/SSVI/SABR line.")
bib.append("- Every excluded candidate has a reason code or is counted in a documented bucket; the "
           "40 `RELEVANT_NOT_SELECTED` records are disclosed rather than hidden.")
bib.append("- Preprints are capped under 30% and individually flagged; metadata-only records are "
           "flagged at every citation point.")
bib.append("- No citation counts are reported anywhere in these artifacts, because they were not "
           "used for selection or evaluation and would invite a spurious quality ranking.")
bib.append("")

bib.append("## 9. Abstract-level method notes")
bib.append("")
bib.append("This bibliography reflects what abstracts state, not what full texts show. Method "
           "weaknesses are therefore limited to: missing enforcement guarantees, missing data or "
           "tolerance detail, absent comparison baselines, and preprint status. Any inferential "
           "weakness (e.g. selection effects inside a study, robustness of a numerical scheme) is "
           "recorded as `not assessed (read scope: abstract_only)` rather than guessed.")
bib.append("")

(RUN / "phase2-bibliography.md").write_text("\n".join(bib), encoding="utf-8")

# ---------------------------------------------------------------- verification

def grade_peer(c: dict) -> str:
    if c["peer_reviewed"]:
        return "A"
    if c["venue_kind"] == "preprint":
        return "C"
    return "D"


def grade_method(c: dict) -> str:
    if c["abstract_status"] == "metadata-only":
        return "C"
    return {"proof": "A", "numerical test": "B", "assumption": "C"}[c["evidence_status"]]


def grade_currency(c: dict) -> str:
    if "seminal" in c["flags"]:
        return "A"
    y = c["year"]
    now = int(LAST_SEARCH[:4])
    if y >= now - 2:
        return "A"
    if y >= now - 5:
        return "B"
    if y >= now - 10:
        return "C"
    return "D"


GRADE_VAL = {"A": 1, "B": 2, "C": 3, "D": 4}
VAL_GRADE = {v: k for k, v in GRADE_VAL.items()}


def overall(c: dict) -> str:
    grades = sorted([GRADE_VAL[grade_peer(c)], GRADE_VAL[grade_method(c)], GRADE_VAL[grade_currency(c)]])
    med = grades[1]
    caps = [GRADE_VAL[grade_method(c)]]
    if not c["peer_reviewed"]:
        caps.append(3)
    if c["abstract_status"] == "metadata-only":
        caps.append(3)
    if c["abstract_status"] == "partial":
        caps.append(2)
    return VAL_GRADE[max([med] + caps)]


overall_counts = Counter(overall(c) for c in corpus)
level_counts = Counter(c["quality_level"] for c in corpus)

ver = []
ver.append("# Phase 2 - Source Verification Report")
ver.append("")
ver.append(f"**Scope.** 41 sources selected in Phase 2 (INVESTIGATION) of the ARS v3.24.4 validation "
           f"run, verified at metadata and abstract level on {LAST_SEARCH}. No full texts were read; "
           "no author contact, no retraction-database sweep beyond OpenAlex flags, no live "
           "predatory-journal list check.")
ver.append("")
ver.append("## Overall assessment")
ver.append("")
ver.append("**Conditional pass.** The corpus is bibliographically sound (41/41 DOI lookups resolved, "
           "0 retracted records) and sufficient for a Phase 3 synthesis that is explicit about "
           "evidence status and comparability. It is not a field census, and the following conditions "
           "must travel with any downstream use: (i) three metadata-only records (P4, P7, R4) may be "
           "cited only at title/metadata level and are graded `assumption`; (ii) 11 preprints (26.8%) "
           "are flagged and must be labelled as such in every synthesis claim; (iii) no source is "
           "described as 'arbitrage-free' when its evidence status is `numerical test`; (iv) "
           "violation-rate, fit and hedging numbers are not comparable across studies; (v) dynamic "
           "arbitrage is essentially unverified in this corpus - only C2 reviews the conditions and "
           "no construction method proves dynamic no-arbitrage.")
ver.append("")
ver.append("## Method")
ver.append("")
ver.append("- **Existence and identity.** Each selected DOI was looked up through the OpenAlex "
           "`/works/doi:` endpoint (41/41 HTTP 200). Title-search fallback was available but not "
           "needed. DOI strings were cross-checked against Crossref for the 4 records whose abstracts "
           "were recovered there. No DOI was invented or repaired by hand.")
ver.append("- **Abstract retrieval.** OpenAlex inverted-index reconstruction first, then Crossref "
           "(JATS tag stripping) and Semantic Scholar for records still missing or partial. Final "
           "coverage: 34 full, 4 partial, 3 metadata-only, 0 title-level.")
ver.append("- **Quality grading.** Two axes are kept separate, following "
           "`references/source_quality_hierarchy.md`: the evidence-hierarchy level (I-VII) and a "
           "six-criterion A-F rubric. Because the corpus is methods/simulation literature, the "
           "conventional level is VI (single study); VII is reserved for the one narrative review "
           "(C2). The matrix below grades Peer review, Method and Currency at metadata level, with "
           "COI `n/a` (no statement retrieved - not a finding of none). Overall is the median of "
           "those three grades, with integrity floors: a numerical test cannot be graded A; a "
           "claim-only or abstract-unavailable source, a preprint, a practitioner outlet or a "
           "metadata-only record cannot be graded above C; a partial abstract cannot be graded "
           "above B. Author-credibility checks were limited to "
           "whether author names are attached to the OpenAlex record; no affiliation verification "
           "was performed.")
ver.append("- **Cross-source checks.** Five claim clusters were read across sources: SVI/SSVI "
           "condition family (S1, P1, P2, P3, C2, P7); SABR asymptotics (S3 vs C4); penalty "
           "violation rates (N3, N4, N5, N6, G5, G6); repair violation floors (R5, R7); architectural "
           "guarantees (G1, G7, G8, G6). That covers 19 of 41 sources at least once. No claim was "
           "independently replicated; cross-checks establish consistency with the literature's own "
           "statements, not truth.")
ver.append("- **Not checked.** Full-text methods and proofs; conflict-of-interest and funding "
           "statements; author affiliations; journal indexing (Scopus/DOAJ/COPE); predatory-journal "
           "lists; retraction databases beyond OpenAlex `is_retracted`; citation counts (deliberately "
           "excluded).")
ver.append("")
ver.append("## Source quality matrix")
ver.append("")
ver.append("Level = evidence-hierarchy level (VI single study, VII review). Peer = A peer-reviewed "
           "journal/conference, C SSRN/arXiv preprint, D practitioner magazine. Method = A formal "
           "result reported in abstract, B numerical test reported, C claim-only or abstract "
           "unavailable. Currency = A 2024-2026 or seminal, B 2021-2023, C 2016-2020, D pre-2016 "
           "non-seminal. COI = n/a (no statement retrieved). Overall applies the caps described above.")
ver.append("")
matrix_rows = []
for c in corpus:
    matrix_rows.append(
        [c["id"], c["venue_short"], c["quality_level"], grade_peer(c), grade_method(c),
         grade_currency(c), "n/a", overall(c)]
    )
ver.append(md_table(["ID", "Venue", "Level", "Peer", "Method", "Currency", "COI", "Overall"], matrix_rows))
ver.append("")
ver.append("Distribution of overall grades: " + "; ".join(
    f"{g} {overall_counts[g]}" for g in "ABCD" if overall_counts[g]) +
    ". Evidence-hierarchy levels: " + "; ".join(f"{k} {v}" for k, v in sorted(level_counts.items())) +
    ". No source was graded F; the integrity floors described in Method were applied.")
ver.append("")
ver.append("## Flagged sources")
ver.append("")
ver.append("**Preprints (11; 26.8%).** " + ", ".join(
    f"{c['id']} {c['label']}" for c in corpus if c["venue_kind"] == "preprint"))
ver.append("")
ver.append("**Partial abstracts (4).** " + ", ".join(
    f"{c['id']} ({FETCH[c['id']]['abstract_status']}, {len(FETCH[c['id']]['abstract'])} chars)" for c in corpus
    if c["abstract_status"] == "partial") + ". Claims are limited to the retrieved fragment; R2's "
    "fragment is a publisher-deposited snippet, G3's is truncated mid-argument, C4's and S1's are "
    "short but state their result explicitly.")
ver.append("")
ver.append("**Metadata-only (3).** P4, P7, R4. No abstract in OpenAlex, Crossref or Semantic Scholar. "
           "P7 is a preprint whose title asserts necessary and sufficient conditions; the claim is "
           "recorded as `assumption` and must never be cited as a proof. R4 (EJOR 2026) and P4 are "
           "peer-reviewed but unverifiable at abstract level.")
ver.append("")
ver.append("**Other flags.** S3 is published in *Wilmott*, an editorially reviewed practitioner "
           "magazine, not a peer-reviewed journal; it is graded D on Peer review and C overall. R9 is "
           "in JRFM (MDPI, open access, APC model) - not predatory on the evidence available, but "
           "different from the society/Elsevier journals. N2 is an ICLR 2025 paper whose DOI is the "
           "arXiv version (10.48550/arxiv.2406.11520); it is graded as peer-reviewed on the venue but "
           "the DOI resolves to the preprint. N5 and N6 are arXiv-DOI records whose OpenAlex primary "
           "location points at RePEc; the venue is recorded as arXiv because the DOI prefix is arXiv "
           "and the abstract is the arXiv abstract. R7's OpenAlex author string is irregular "
           "('Alvarez, Robert Jenkinson'); the citation uses the initialed form and is flagged. C5 is "
           "included with a scope flag: its panel is single stocks, not an equity index.")
ver.append("")
ver.append("## Predatory-journal screening result")
ver.append("")
ver.append("No predatory red flag was identified in the venue set at structural level: 23 journal "
           "articles in established finance, mathematics, operations-research and econometrics "
           "journals, 6 peer-reviewed conference papers (ICLR, AAAI, IEEE SSCI, IEEE CIFEr, ACM "
           "ICAIF), 11 preprints on SSRN/arXiv (which are not journals), and 1 practitioner "
           "magazine. Two caveats: (a) no live check against Beall's list, DOAJ or COPE membership "
           "was performed - the assessment is structural only; (b) JRFM is an APC-based open-access "
           "journal and publication there is noted, not penalised. This result is 'no red flags "
           "found under a limited check', not 'verified non-predatory'.")
ver.append("")
ver.append("## COI disclosures")
ver.append("")
ver.append("No conflict-of-interest or funding statement was retrieved for any of the 41 records, "
           "because abstracts and metadata do not carry them. `n/a` in the matrix means 'not "
           "retrieved', never 'none declared'. Several sources are authored by current or former "
           "industry practitioners (notably S3 and R9); affiliations were not verified, so no COI "
           "conclusion is drawn.")
ver.append("")
ver.append("## Cross-source consistency checks")
ver.append("")
ver.append("- **SVI conditions.** S1 gives sufficient conditions for static-arbitrage-free SVI; P2 "
           "completes the butterfly characterisation; P1 generalises the family; C2's review is "
           "consistent. P7 claims necessity and sufficiency at title level only and cannot be used as "
           "confirmation.")
ver.append("- **SABR asymptotics.** S3 reports that the explicit SABR implied-volatility formula can "
           "produce arbitrage at low strikes, while C4 proves the SABR formula is asymptotically "
           "arbitrage-free. The two are compatible only in the asymptotic regime C4 states; the "
           "finite-strike tension is a real constraint on how SABR-based surfaces may be used and is "
           "carried into Phase 3.")
ver.append("- **Violation-rate claims.** G6 (synthetic, tolerance 1e-4), G5 (90.8% pass rate), R5 "
           "(about 5.4% butterfly floor on SPX) and R7 (<1%) are mutually consistent as evidence that "
           "residual violations persist, but their magnitudes are not comparable and were not pooled.")
ver.append("- **Architectural guarantees.** G1, G7, G8 and G6 all place the guarantee in the network "
           "structure; their abstracts agree that the guarantee is static, not dynamic.")
ver.append("")
ver.append("## Verification limitations")
ver.append("")
ver.append("- Abstract-level verification only; method quality beyond what abstracts state is `not "
           "assessed`.")
ver.append("- No full-text, appendix or replication-material inspection; no check that proofs are "
           "correct.")
ver.append("- No COI, funding or affiliation retrieval; no author-credibility assessment beyond "
           "name-to-record attachment.")
ver.append("- Single-reviewer screening and grading; no dual review or calibration; PRISMA-style, "
           "not PRISMA-compliant.")
ver.append("- One discovery query failed with a transient 429 and was not re-run successfully; the "
           "pool is not exhaustive.")
ver.append("- Abstract augmentation depended on Crossref and Semantic Scholar availability; arXiv "
           "API was rate-limited and unusable during the run.")
ver.append("- Citation counts were deliberately not used or reported.")
ver.append("")
ver.append("## Recommendation")
ver.append("")
ver.append("**Proceed to Phase 3 (synthesis) under the conditional pass above.** Keep the four-family "
           "structure, label every claim with its evidence status, keep the three metadata-only "
           "records at title level, and do not let the recency of the 2023-2026 half of the corpus "
           "silently crowd out the parametric baselines. If a Phase 2 revision is possible, the "
           "highest-value additions are: full-text retrieval for P4/P7/R4, a second screener for a "
           "reliability check, and one discovery pass with a fixed-rate OpenAlex key to close the "
           "failed SVI query.")
ver.append("")

(RUN / "phase2-verification.md").write_text("\n".join(ver), encoding="utf-8")

print("written:")
for p in [HERE / "selected_sources.json", HERE / "selected_sources.md", HERE / "screening_summary.md",
          RUN / "phase2-bibliography.md", RUN / "phase2-verification.md"]:
    print(" ", p, p.stat().st_size, "bytes")
print("families:", dict(fam_counts))
print("evidence:", dict(ev_counts))
print("abstract:", dict(abs_counts))
print("overall grades:", dict(overall_counts))
print("peer yes/no:", peer_yes, len(corpus) - peer_yes)
