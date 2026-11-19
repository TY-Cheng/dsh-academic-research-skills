# Phase 5a — Citation Compliance Check

**Paper:** `paper-draft.md` (v1.2)

## Result

**Pass with advisories.**

| Check | Result |
|---|---|
| Reference entries | 40 |
| Unique `src-01..src-40` citation keys in text | 40 |
| Uncited references / orphans | 0 |
| Dangling citations (key without reference) | 0 |
| DOI present | 39/40 |
| No DOI (HAL record) | 1 (Guo et al., 2016) |
| Retraction flag | 0 flagged |
| Fabricated reference | 0 (OpenAlex/DOI resolution) |
| Preprints | 10/40 (25%) |
| Title-level-only source | 1 (Horvath et al., 2021) |
| In-text citation style | APA 7.0 author–date |
| Reference list style | APA 7.0, alphabetical |

## Method

1. Extracted every `src-XX` key from the body and the appendices.
2. Compared the key set with the 40-entry reference list and with `../search/selected_sources.json`.
3. Checked every visible author–date citation against the reference list.
4. Checked DOI strings for the 39 DOI-bearing entries; the one HAL record has a URL, not a DOI.
5. Checked OpenAlex `is_retracted` flags at selection time; none were flagged.
6. Did not perform full-text quotation checks; all evidence is metadata/abstract-level.

## Advisories

- Horvath et al. (2021) is title-level only; it is cited only in the scope/dynamic discussion, not for a substantive numerical claim.
- The 10 preprints are retained and labeled; they are not equivalent to peer-reviewed evidence.
- The Chinese abstract contains no reference list; its citations are the English abstract's claims, not new sources.
- No plagiarism scan was performed. The integrity report must disclose this.
