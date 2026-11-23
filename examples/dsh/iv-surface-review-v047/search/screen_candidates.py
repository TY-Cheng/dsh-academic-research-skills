#!/usr/bin/env python3
"""Title-level screening of the 430-record OpenAlex candidate pool.

This is a PRISMA-style flow, not a PRISMA-compliant one: screening was
performed by one reviewer (the research agent) at title level for the whole
pool, with abstract-level confirmation only for the 41 included records.
The per-record reason codes below are a transparent, reproducible
classification based on the title; each is labelled with the rule that fired.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
POOL = HERE / "openalex_candidates.json"
INDEX = HERE / "selected_index.json"

REASONS = {
    "INCLUDED": "Selected for the Phase 2 corpus.",
    "DUPLICATE_VERSION": "Duplicate/alternate version (same DOI or near-identical title) of another pool record.",
    "PRE_2015_BACKGROUND": "Published before 2015; outside the 2015-2026 window. Retained as background knowledge only (older seminal works enter the corpus only through the explicitly flagged baseline set).",
    "PUBLICATION_TYPE": "Dissertation, book, software/replication package, review, paratext or other grey-literature type not eligible as a peer-reviewed/preprint research source.",
    "NON_ENGLISH": "Not written in English.",
    "OUT_OF_SCOPE_ASSET": "Underlying is not an equity index (FX, rates, commodities, energy, crypto, single-name equity, or a non-financial domain).",
    "OFF_TOPIC": "Title is not about implied-volatility/option-price surface construction or its arbitrage constraints.",
    "FORECASTING_OR_TRADING": "Surface forecasting, hedging or trading application rather than a construction/enforcement method.",
    "MODEL_CALIBRATION_PRICING": "Stochastic-volatility model calibration, asymptotics or option pricing without surface-construction enforcement.",
    "RELEVANT_NOT_SELECTED": "Topically relevant at title level but not selected: corpus cap (35-45), family balance, recency/version precedence, or already represented by a stronger record in the same family.",
}

ASSET_PATTERNS = [
    r"\bfx\b", r"foreign exchange", r"currency", r"swaption", r"libor", r"cms\b",
    r"interest rate", r"term structure", r"fixed.income", r"commodit", r"crude",
    r"\boil\b", r"\bgas\b", r"electric", r"energy", r"power system", r"battery",
    r"wind power", r"solar", r"hydro", r"heating", r"grape", r"pavement",
    r"mammogram", r"barcode", r"weather", r"mercury", r"\bmoon\b", r"fmri",
    r"bitcoin", r"crypto", r"single stock", r"single-stock", r"equity-linked",
    r"kospi", r"taiex", r"nifty", r"ibex", r"shanghai", r"sh 50etf",
]

IVS_PATTERNS = [
    r"implied volatilit", r"volatility surface", r"volatility smile", r"volatility skew",
    r"option surface", r"option price surface", r"call price surface", r"call option prices",
    r"smile surface", r"\bsvi\b", r"\bssvi\b", r"e-ssvi", r"essvi", r"\bsabr\b",
    r"static arbitrage", r"butterfly arbitrage", r"calendar spread", r"no.arbitrage",
    r"arbitrage.free", r"arbitrage free", r"implied volatility function",
]

CONSTRUCTION_PATTERNS = [
    r"construct", r"interpolat", r"extrapolat", r"smooth", r"generat", r"reconstruct",
    r"inpaint", r"complet", r"repair", r"correct", r"projection", r"parametriz",
    r"parameteriz", r"calibrat", r"fit", r"approximat", r"surface completion",
]

FORECAST_PATTERNS = [
    r"forecast", r"predict", r"risk premium", r"trading strateg", r"hedg",
    r"portfolio", r"asset allocation", r"market timing", r"return",
]

MODEL_PATTERNS = [
    r"heston", r"rough volatility", r"rough heston", r"bergomi", r"jump",
    r"levy", r"l\u00e9vy", r"asymptotic", r"large deviation", r"small.time",
    r"model.calibration", r"calibrat.*model", r"parameter recovery",
]

TYPE_EXCLUDED = {"dissertation", "book", "software", "repository", "paratext",
                 "review", "reference", "editorial", "letter", "erratum", "peer-review"}

# Two records were screened out by hand after abstract-level reading, and the
# 41-source cap was filled by their replacements (Wiedemann et al. 2025 for N2,
# Fukasawa 2022 for C4). The overrides keep those decisions legible instead of
# letting the automated title rules mislabel them as OFF_TOPIC.
OVERRIDES = {
    "10.3390/risks7010016": (
        "RELEVANT_NOT_SELECTED",
        "Neural-network IV computation with no arbitrage-enforcement claim; "
        "replaced in the corpus by Wiedemann, Jacquier & Gonon (2025) for family fit.",
    ),
    "10.1016/j.najef.2018.08.011": (
        "OUT_OF_SCOPE_ASSET",
        "Delta-parameterised IVS conditions developed for FX options (EURUSD/USDJPY); "
        "excluded on asset scope and replaced by Fukasawa (2022).",
    ),
}


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", (text or "").lower()).strip()


def anypat(patterns, text: str) -> bool:
    return any(re.search(p, text) for p in patterns)


def main() -> None:
    pool = json.loads(POOL.read_text(encoding="utf-8"))
    records = pool["records"]
    selected = {r["openalex_id"]: r for r in json.loads(INDEX.read_text(encoding="utf-8"))}

    # duplicate detection over the whole pool
    seen_doi: dict[str, int] = {}
    seen_title: dict[str, int] = {}
    dup_of: dict[int, int] = {}
    for i, rec in enumerate(records):
        doi = (rec.get("doi") or "").lower()
        title = norm(rec.get("title"))
        if doi and doi in seen_doi:
            dup_of[i] = seen_doi[doi]
        elif title in seen_title:
            dup_of[i] = seen_title[title]
        else:
            if doi:
                seen_doi[doi] = i
            seen_title[title] = i
    # near-identical titles (capitalisation / trailing plural / leading article)
    for i, rec in enumerate(records):
        if i in dup_of:
            continue
        ti = norm(rec.get("title"))
        for j in range(i):
            if j in dup_of:
                continue
            tj = norm(records[j].get("title"))
            if abs(len(ti) - len(tj)) <= 8 and ti and tj:
                # cheap character-level ratio on the normalised names
                import difflib
                if difflib.SequenceMatcher(None, ti, tj).ratio() >= 0.95:
                    dup_of[i] = j
                    break

    log = []
    for i, rec in enumerate(records):
        title = rec.get("title") or ""
        low = title.lower()
        year = rec.get("year")
        rtype = (rec.get("type") or "").lower()
        lang = (rec.get("language") or "en").lower()
        note = ""
        if rec.get("openalex_id") in selected:
            code = "INCLUDED"
            note = f"family {selected[rec['openalex_id']]['family']}"
        elif i in dup_of:
            code = "DUPLICATE_VERSION"
            note = f"duplicate of pool record #{dup_of[i]}: {records[dup_of[i]]['title'][:80]}"
        elif year is not None and year < 2015:
            code = "PRE_2015_BACKGROUND"
        elif rtype in TYPE_EXCLUDED:
            code = "PUBLICATION_TYPE"
        elif lang != "en":
            code = "NON_ENGLISH"
        elif anypat(ASSET_PATTERNS, low):
            code = "OUT_OF_SCOPE_ASSET"
        elif not anypat(IVS_PATTERNS, low):
            code = "OFF_TOPIC"
        elif anypat(FORECAST_PATTERNS, low) and not anypat(
            [r"smooth", r"interpolat", r"reconstruct", r"generat", r"repair", r"projection", r"complet", r"construct"], low
        ):
            code = "FORECASTING_OR_TRADING"
        elif anypat(MODEL_PATTERNS, low) and not anypat(
            [r"surface", r"smile", r"arbitrage"], low
        ):
            code = "MODEL_CALIBRATION_PRICING"
        elif anypat(CONSTRUCTION_PATTERNS, low):
            code = "RELEVANT_NOT_SELECTED"
        else:
            code = "OFF_TOPIC"
        override = OVERRIDES.get((rec.get("doi") or "").lower())
        if override and code != "INCLUDED":
            code, note = override
        log.append(
            {
                "index": i,
                "openalex_id": rec.get("openalex_id"),
                "doi": rec.get("doi"),
                "title": title,
                "year": year,
                "venue": rec.get("venue"),
                "type": rtype,
                "query_hits": len(rec.get("queries") or []),
                "reason_code": code,
                "reason_note": note,
            }
        )

    counts: dict[str, int] = {}
    for row in log:
        counts[row["reason_code"]] = counts.get(row["reason_code"], 0) + 1

    (HERE / "screening_log.json").write_text(
        json.dumps({"criteria": REASONS, "records": log, "counts": counts}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(json.dumps(counts, indent=2))
    print("total", len(log))


if __name__ == "__main__":
    main()
