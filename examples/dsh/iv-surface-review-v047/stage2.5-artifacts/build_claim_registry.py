"""Build claim-registry/1.0 for Stage 2.5 E1: bounded detector candidates + explicit high-impact claims."""
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
tmp = pathlib.Path('/tmp/e1-reg0.json'); tmp.write_text(json.dumps({"schema_version": "claim-registry/1.0", "draft_raw_sha256": sha, "claims": []}))
cov = pathlib.Path('/tmp/e1-cov0.json')
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
    hi = 'Six rows audit their own output' in t
    claims.append({"claim_id": f"CLM-{i:03d}", "claim_text": t,
                   "draft_span": {"start_byte": c['start_byte'], "end_byte": c['end_byte']},
                   "claim_kinds": kinds,
                   "ref_slugs": sorted(set(re.findall(r'<!--ref:([A-Za-z0-9]+)-->', t))),
                   "writer_anchors": sorted(set(re.findall(r'<!--anchor:([^>]+)-->', t))),
                   "paper_section": sec.get(c['line'], 'Abstract'),
                   "selection_tier": 'HIGH-IMPACT' if hi else 'PENDING',
                   **({"high_impact_basis": ["numerical"]} if hi else {})})
EXTRA = [
 ("The corpus is 41 sources", ["headline_conclusion", "numerical"]),
 ("Seventeen sources assert their guarantee at proof level", ["numerical", "headline_conclusion"]),
 ("As reported in the abstracts, the certified object in all 41 rows", ["headline_conclusion"]),
 ("Proof-level and test-level evidence come from almost disjoint", ["headline_conclusion"]),
 ("no study in this corpus tests it", ["headline_conclusion"]),
 ("The corpus contains no such test", ["headline_conclusion"]),
 ("Ten rows engage time; none states a path-level condition", ["numerical"]),
 ("Retrieval requested 775 records and returned 750", ["methods_critical"]),
 ("21 first-pass responses were rate-limited", ["methods_critical"]),
 ("De-duplication left 430 unique records", ["methods_critical"]),
 ("Screening excluded 389", ["methods_critical"]),
 ("Forty-one studies were included", ["numerical", "headline_conclusion"]),
 ("All 41 records were resolved to a DOI-bearing index record", ["methods_critical"]),
 ("34 records were read in full abstract", ["methods_critical"]),
 ("The corpus splits into 17 proof-level rows", ["numerical"]),
 ("The cross-tabulation is the finding", ["numerical", "disputed"]),
 ("The comparability coding returns 0 direct", ["numerical", "headline_conclusion"]),
 ("zero of six rows are proof-level", ["numerical"]),
 ("six of eight rows are proof-level", ["numerical"]),
 ("Seventeen rows are proof-level and only one reports", ["headline_conclusion", "numerical"]),
 ("0 of 41 abstracts, 0 of 36 in-window records", ["numerical", "headline_conclusion"]),
 ("static no-arbitrage is coded for all 41 rows", ["numerical"]),
 ("the evidence is abstract-level, single-analyst", ["methods_critical"]),
 ("the conditions group carries the largest share of not-comparable rows", ["numerical"]),
]
for j, (pat, basis) in enumerate(EXTRA, 1):
    hits = [s for s in sents if pat in s['text']]
    assert len(hits) == 1, (pat, len(hits))
    s = hits[0]
    sb = len(text[:s['start']].encode()); eb = len(text[:s['end']].encode())
    claims.append({"claim_id": f"CLM-X{j:02d}", "claim_text": draft[sb:eb].decode(),
                   "draft_span": {"start_byte": sb, "end_byte": eb},
                   "claim_kinds": ["categorical"] + (["quantitative"] if re.search(r'\d', s['text']) else []),
                   "ref_slugs": sorted(set(re.findall(r'<!--ref:([A-Za-z0-9]+)-->', s['text']))),
                   "writer_anchors": sorted(set(re.findall(r'<!--anchor:([^>]+)-->', s['text']))),
                   "paper_section": sec.get(s['line'], 'Abstract'),
                   "selection_tier": "HIGH-IMPACT", "high_impact_basis": basis})
hi = [c for c in claims if c['selection_tier'] == 'HIGH-IMPACT']
rest = [c for c in claims if c['selection_tier'] == 'PENDING']
rest.sort(key=lambda c: hashlib.sha256(c['claim_id'].encode()).hexdigest())
k = min(10, max(3, (len(rest) + 9) // 10))
for c in rest[:k]: c['selection_tier'] = 'RANDOM'
for c in rest[k:]: c['selection_tier'] = 'NOT-SELECTED'
reg_path.write_text(json.dumps({"schema_version": "claim-registry/1.0", "draft_raw_sha256": sha, "claims": claims}, indent=1, ensure_ascii=False) + "\n", encoding='utf-8')
print('claims', len(claims), 'HIGH', len(hi), 'RANDOM', k, 'NOT', len(rest) - k)
