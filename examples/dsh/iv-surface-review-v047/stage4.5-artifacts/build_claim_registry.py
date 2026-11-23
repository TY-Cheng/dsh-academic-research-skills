"""Build claim-registry/1.0 for Stage 4.5 Mode 2 E1: bounded detector candidates + explicit high-impact claims.

All rows carry selection_tier ALL (Mode 2 audits the full registry).
The registry is bound to the exact raw bytes of stage4-prime/paper-draft-v3.md.
"""
import json, hashlib, re, subprocess, pathlib, sys
FORK = '/Volumes/ExternalSSD/projects/dsh-academic-research-skills/fork'
draft_path = pathlib.Path(sys.argv[1]); reg_path = pathlib.Path(sys.argv[2])
draft = draft_path.read_bytes(); text = draft.decode('utf-8'); sha = hashlib.sha256(draft).hexdigest()
SB = re.compile(r'(?<=[.!?。！？])\s+')

def sentences():
    out = []; abschar = 0; fence = False
    for ln, raw in enumerate(text.splitlines(keepends=True), 1):
        content = raw.rstrip('\r\n'); st = content.strip()
        if st.startswith('```'):
            fence = not fence; abschar += len(raw); continue
        if fence or not st or st.startswith('#'):
            abschar += len(raw); continue
        bstart = len(content) - len(content.lstrip()); bend = len(content.rstrip())
        body = content[bstart:bend]; seg = 0
        for m in list(SB.finditer(body)) + [None]:
            end = m.start() if m else len(body); segtext = body[seg:end]
            left = len(segtext) - len(segtext.lstrip()); right = len(segtext.rstrip())
            if right > left:
                out.append({'line': ln, 'text': segtext[left:right],
                            'start': abschar + bstart + seg + left, 'end': abschar + bstart + seg + right})
            if m is None:
                break
            seg = m.end()
        abschar += len(raw)
    return out

sents = sentences()
tmp = pathlib.Path('/tmp/e1-reg45.json'); tmp.write_text(json.dumps({"schema_version": "claim-registry/1.0", "draft_raw_sha256": sha, "claims": []}))
cov = pathlib.Path('/tmp/e1-cov45.json')
r = subprocess.run([FORK + '/.venv/bin/python', FORK + '/scripts/claim_registry_coverage.py',
                    '--draft', str(draft_path), '--registry', str(tmp), '--output', str(cov)], capture_output=True, text=True)
assert r.returncode == 0, r.stderr
cands = json.loads(cov.read_text())['candidates']
lines = text.splitlines(); sec = {}; cur = 'Abstract'
for i, l in enumerate(lines, 1):
    m = re.match(r'#{2,4}\s+(.*)', l.strip())
    if m:
        t = m.group(1); mm = re.match(r'(\d+\.\d+)\s', t)
        if mm: cur = mm.group(1)
        elif t.startswith('Appendix'): cur = t.split('.')[0]
        elif t.lower().startswith('references'): cur = 'References'
        else: cur = 'Abstract'
    sec[i] = cur
claims = []
for i, c in enumerate(cands, 1):
    t = c['text']; kinds = []
    if 'quantitative_sentence' in c['candidate_kinds']: kinds.append('quantitative')
    if 'citation_bearing_sentence' in c['candidate_kinds']: kinds.append('categorical')
    claims.append({"claim_id": f"CLM-{i:03d}", "claim_text": t,
                   "draft_span": {"start_byte": c['start_byte'], "end_byte": c['end_byte']},
                   "claim_kinds": kinds,
                   "ref_slugs": sorted(set(re.findall(r'<!--ref:([A-Za-z0-9]+)-->', t))),
                   "writer_anchors": sorted(set(re.findall(r'<!--anchor:([^>]+)-->', t))),
                   "paper_section": sec.get(c['line'], 'Abstract'),
                   "selection_tier": 'ALL'})
EXTRA = [
 ("The corpus is 41 sources", ["headline_conclusion", "numerical"]),
 ("Seventeen sources assert their guarantee at proof level", ["numerical", "headline_conclusion"]),
 ("no study in this corpus tests it", ["headline_conclusion"]),
 ("Ten rows engage time", ["numerical"]),
 ("Retrieval requested 775 records and returned 750", ["methods_critical"]),
 ("Screening excluded 389", ["methods_critical"]),
 ("34 records were read in full abstract", ["methods_critical"]),
 ("The corpus splits into 17 proof-level rows", ["numerical"]),
 ("Seventeen rows are proof-level and only one reports", ["headline_conclusion", "numerical"]),
 ("0 of 41 abstracts, 0 of 36 in-window records", ["numerical", "headline_conclusion"]),
 ("the conditions group carries the largest share of not-comparable rows", ["numerical"]),
 ("No source states and checks a dynamic condition", ["headline_conclusion"]),
 ("Proof-level evidence and audit evidence come from nearly disjoint sets", ["headline_conclusion", "numerical"]),
 ("Dynamic admissibility is neither stated nor checked", ["headline_conclusion"]),
 ("Dynamic consistency is empty", ["headline_conclusion"]),
 ("Ten rows engage the time axis", ["numerical"]),
 ("none states a path-level condition", ["headline_conclusion"]),
 ("No row reports all four", ["numerical", "headline_conclusion"]),
 ("A direct comparison requires the four fields", ["numerical"]),
 ("Proof and audit are nearly disjoint", ["headline_conclusion", "numerical"]),
 ("Hence 16 + 1 + 5 + 11 + 8 = 41 rows", ["numerical", "methods_critical"]),
 ("Zero of six audit rows supply three or more of the five inputs", ["numerical", "headline_conclusion"]),
 ("The corpus codes 17 proof, 16 numerical test, and 8 assumption", ["numerical"]),
 ("The result is 0 direct, 30 context, and 11 not comparable", ["numerical"]),
 ("Comparability coding returns 0 direct, 30 context, and 11 not comparable", ["numerical"]),
 ("Static no-arbitrage is populated", ["headline_conclusion"]),
 ("The evidence is abstract-level (34 full, 4 partial, 3 metadata-only)", ["numerical", "methods_critical"]),
 ("On the 16-row sample the second coder agreed", ["numerical", "methods_critical"]),
 ("The 17 cell disagreements were adjudicated", ["numerical", "methods_critical"]),
 ("A field is stably coded where agreement is at least 0.85", ["methods_critical"]),
 ("Within the 31 construction rows the certified object is, as reported", ["headline_conclusion"]),
 ("SC3 is stated in the corrected form", ["methods_critical"]),
 ("The partition recomputes from the Audit column of Appendix B", ["numerical"]),
 ("Thirty-nine of the 41 rows state a condition subset that includes SC3", ["numerical"]),
 ("Ten rows engage the time axis under the same discipline", ["numerical"]),
]
added = 0; seen = {(c['draft_span']['start_byte'], c['draft_span']['end_byte']) for c in claims}
for pat, basis in EXTRA:
    hits = [s for s in sents if pat in s['text']]
    if len(hits) == 0:
        print('EXTRA-MISS', pat); continue
    for s in hits:
        sb = len(text[:s['start']].encode()); eb = len(text[:s['end']].encode())
        if (sb, eb) in seen:
            continue
        seen.add((sb, eb))
        claims.append({"claim_id": f"CLM-X{added+1:02d}", "claim_text": draft[sb:eb].decode(),
                       "draft_span": {"start_byte": sb, "end_byte": eb},
                       "claim_kinds": ["categorical"] + (["quantitative"] if re.search(r'\d', s['text']) else []),
                       "ref_slugs": sorted(set(re.findall(r'<!--ref:([A-Za-z0-9]+)-->', s['text']))),
                       "writer_anchors": sorted(set(re.findall(r'<!--anchor:([^>]+)-->', s['text']))),
                       "paper_section": sec.get(s['line'], 'Abstract'),
                       "selection_tier": 'ALL', "high_impact_basis": basis})
        added += 1
reg_path.write_text(json.dumps({"schema_version": "claim-registry/1.0", "draft_raw_sha256": sha, "claims": claims}, indent=1, ensure_ascii=False) + "\n", encoding='utf-8')
print('claims', len(claims), 'detector', len(cands), 'extra_added', added)
