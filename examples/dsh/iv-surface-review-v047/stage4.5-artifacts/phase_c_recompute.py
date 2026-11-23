"""Stage 4.5 Phase C recomputation: ledger tallies, retrieval arithmetic, reliability,
word counts, and the §2.1 displayed-derivative check. Writes phase-c-checks.json.

Read-only on the manuscript; mechanical recomputation only.
"""
import json, re, math, hashlib, pathlib
RUN = pathlib.Path('/Volumes/ExternalSSD/projects/dsh-academic-research-skills/fork/examples/dsh/iv-surface-review-v047')
raw = (RUN / 'stage4-prime/paper-draft-v3.md').read_text(encoding='utf-8')
out = {}

# ---- ledger ----
sec = raw.split('## Appendix B. Evidence Ledger')[1].split('## Appendix C')[0]
rows = {}
for l in sec.splitlines():
    if l.startswith('| ') and not l.startswith('| **') and not l.startswith('|---'):
        c = [x.strip() for x in l.strip('|').split('|')]
        if len(c) == 13 and re.match(r'^[PNRGSC]\d$', c[0]):
            rows[c[0]] = dict(family=c[2], evidence=c[3], audit=c[4], time=c[6],
                              dyn=c[7], level=c[8], comp=c[9], coverage=c[10], peer=c[11])
assert len(rows) == 41, len(rows)
tally = {
    'total': len(rows),
    'evidence': {k: sum(1 for r in rows.values() if r['evidence'] == k) for k in ('proof', 'numerical test', 'assumption')},
    'audit': sorted(k for k, r in rows.items() if r['audit'] == 'Y'),
    'time': sorted(k for k, r in rows.items() if r['time'] == 'Y'),
    'dyn': {k: sum(1 for r in rows.values() if r['dyn'] == k) for k in ('D0', 'D1', 'D2', 'D3')},
    'comp': {k: sum(1 for r in rows.values() if r['comp'] == k) for k in ('DC', 'RC', 'NC')},
    'coverage': {k: sum(1 for r in rows.values() if r['coverage'] == k) for k in ('full', 'partial', 'metadata-only')},
    'level': {k: sum(1 for r in rows.values() if r['level'] == k) for k in ('VI', 'VII')},
    'peer': {'yes': sum(1 for r in rows.values() if r['peer'] == 'yes'),
             'preprint': sum(1 for r in rows.values() if 'preprint' in r['peer']),
             'practitioner': sum(1 for r in rows.values() if 'practitioner' in r['peer'])},
    'family_n': {f: sum(1 for r in rows.values() if r['family'] == f) for f in 'PNRGSC'},
}
audit_proof = [k for k in tally['audit'] if rows[k]['evidence'] == 'proof']
audit_test = [k for k in tally['audit'] if rows[k]['evidence'] == 'numerical test']
audit_assumption = [k for k in tally['audit'] if rows[k]['evidence'] == 'assumption']
tally['audit_evidence'] = {'proof': audit_proof, 'test': audit_test, 'assumption': audit_assumption}
tally['audit_partition'] = {'16+1+5+11+8': 17 + 5 + 11 + 8, '1+5': len(audit_proof) + len(audit_test)}
out['ledger'] = tally

# ---- per-family evidence / audit / time (Table 3) ----
fam = {}
for f in 'PNRGSC':
    sub = {k: r for k, r in rows.items() if r['family'] == f}
    fam[f] = {'proof': sum(1 for r in sub.values() if r['evidence'] == 'proof'),
              'test': sum(1 for r in sub.values() if r['evidence'] == 'numerical test'),
              'assumption': sum(1 for r in sub.values() if r['evidence'] == 'assumption'),
              'audit': sum(1 for r in sub.values() if r['audit'] == 'Y'),
              'time': sum(1 for r in sub.values() if r['time'] == 'Y'),
              'comp': {k: sum(1 for r in sub.values() if r['comp'] == k) for k in ('DC', 'RC', 'NC')}}
out['families'] = fam

# ---- seminal / in-window split ----
src = json.loads((RUN / 'search/selected_sources.json').read_text())
year = {s['id']: s['year'] for s in src}
seminal = sorted(k for k, y in year.items() if y < 2015)
out['seminal'] = {'ids': seminal, 'n': len(seminal), 'in_window': 41 - len(seminal),
                  'year_min': min(year.values()), 'year_max': max(year.values())}
sem_ev = {k: sum(1 for s in seminal if rows[s]['evidence'] == k) for k in ('proof', 'numerical test', 'assumption')}
out['seminal']['evidence'] = sem_ev
out['seminal']['in_window_evidence'] = {k: tally['evidence'][k] - sem_ev[k] for k in sem_ev}

# ---- retrieval / screening ----
cand = json.loads((RUN / 'search/openalex_candidates.json').read_text())
q = cand['queries']
retr = {'queries': len(q), 'requested': 25 * len(q), 'returned': sum(x.get('returned', 0) for x in q),
        'still_failed': sum(1 for x in q if 'error' in x), 'recovered_note': cand.get('retry_note'),
        'unique_records': len(cand['records'])}
scr = json.loads((RUN / 'search/screening_log.json').read_text())
cnt = scr['counts']
retr['screening_counts'] = cnt
retr['excluded'] = sum(v for k, v in cnt.items() if k != 'INCLUDED')
retr['included'] = cnt['INCLUDED']
retr['records_sum_check'] = retr['excluded'] + retr['included']
retr['preprint_pct'] = round(100 * tally['peer']['preprint'] / 41, 2)
out['retrieval'] = retr

# ---- reliability ----
sc = {r['id']: r for r in json.loads((RUN / 'stage4/reliability/second-coder-form.json').read_text())['rows']}
fields = [('family', 'family'), ('evidence', 'evidence_status'), ('audit', 'audit'),
          ('time', 'time_axis'), ('dyn', 'dynamic'), ('comp', 'comparability')]
dispute = []; agree = {}
for rid, r in rows.items():
    if rid not in sc:
        continue
    for lf, sf in fields:
        agree.setdefault(lf, 0)
        if str(r[lf]) == str(sc[rid][sf]):
            agree[lf] += 1
        else:
            dispute.append([rid, lf, r[lf], sc[rid][sf]])
n = len(sc)
a = [rows[r]['evidence'] for r in sc]; b = [sc[r]['evidence_status'] for r in sc]
cats = sorted(set(a) | set(b)); po = sum(1 for x, y in zip(a, b) if x == y) / n
pe = sum((a.count(c) / n) * (b.count(c) / n) for c in cats)
out['reliability'] = {'sample': n, 'agree': agree, 'cells': n * 6,
                      'total_agree': sum(agree.values()), 'disputes': len(dispute),
                      'kappa_evidence': round((po - pe) / (1 - pe), 3), 'dispute_rows': dispute}

# ---- word counts ----
def measure(path):
    t = pathlib.Path(path).read_text(encoding='utf-8')
    s = t.split('## Draft Body', 1)[1].split('## Declarations', 1)[0]
    s = re.sub(r'<!--.*?-->', '', s)
    words = 0
    for line in s.splitlines():
        st = line.strip()
        if not st or st.startswith('#') or st.startswith('|') or st.startswith('```') or re.match(r'^\*\*(Table|Figure)', st):
            continue
        words += len(st.split())
    return words

wc = {}
for name, p in [('v1.3', 'stage2/paper-draft.md'), ('v2.0', 'stage4/paper-draft-v2.md'), ('v3.0', 'stage4-prime/paper-draft-v3.md')]:
    wc[name] = measure(RUN / p)
out['word_counts'] = wc
ab = raw.split('### English Abstract')[1].split('### Chinese Abstract')[0]
zh = raw.split('### Chinese Abstract')[1].split('## Draft Body')[0]
out['abstract'] = {'en_words': len(ab.split()), 'zh_chars': len(re.findall(r'[\u4e00-\u9fff]', zh)),
                   'tables': len(re.findall(r'\*\*Table \d\.', raw)), 'figures': len(re.findall(r'\*\*Figure \d\.', raw)),
                   'references': len(re.findall(r'^- .*?\(\d{4}\)\.', raw.split('## References')[1].split('## Appendix A')[0], re.M))}

# ---- §2.1 displayed-derivative check ----
def bs_c(k, s):
    d1 = -k / s + s / 2; d2 = d1 - s
    N = lambda x: 0.5 * (1 + math.erf(x / math.sqrt(2)))
    return N(d1) - math.exp(k) * N(d2)

k0, s0, F = -0.5, 0.2, 100.0
h = 1e-5
c0 = bs_c(k0, s0); cp = (bs_c(k0 + h, s0) - bs_c(k0 - h, s0)) / (2 * h)
cpp = (bs_c(k0 + h, s0) - 2 * c0 + bs_c(k0 - h, s0)) / h ** 2
K0 = F * math.exp(k0)
true_pref = (1 / K0) * math.exp(-k0)
printed_pref = (1 / K0) * math.exp(-2 * k0)
Cpp_num = (F * bs_c(k0 + h, s0) - 2 * F * c0 + F * bs_c(k0 - h, s0)) / (K0 * h) ** 2
out['formula'] = {
    'c': c0, 'c_prime': cp, 'c_second': cpp, 'c_second_minus_c_prime': cpp - cp,
    'K': K0, 'true_prefactor': true_pref, 'printed_prefactor': printed_pref,
    'prefactor_ratio_printed_over_true': printed_pref / true_pref,
    'true_C_second': true_pref * (cpp - cp), 'printed_C_second': printed_pref * (cpp - cp),
    'numeric_C_second_central': Cpp_num,
    'printed_matches_numeric': abs(printed_pref * (cpp - cp) - Cpp_num) / abs(Cpp_num) < 0.01,
    'true_matches_numeric': abs(true_pref * (cpp - cp) - Cpp_num) / abs(Cpp_num) < 0.01,
}

# ---- abstract/table cross-checks ----
out['stated_vs_recomputed'] = {
    '41 = 36+5': (41, 36 + 5),
    '29 yes + 11 preprint + 1 practitioner': (29 + 11 + 1, 41),
    '34/4/3 coverage': ((tally['coverage']['full'], tally['coverage']['partial'], tally['coverage']['metadata-only']), (34, 4, 3)),
    '17/16/8 evidence': ((tally['evidence']['proof'], tally['evidence']['numerical test'], tally['evidence']['assumption']), (17, 16, 8)),
    'audit 6': (len(tally['audit']), 6),
    'offset 16+1+5+11+8': (17 + 5 + 11 + 8, 41),
    'time 10': (len(tally['time']), 10),
    'dyn 34/4/3/0': ((tally['dyn']['D0'], tally['dyn']['D1'], tally['dyn']['D2'], tally['dyn']['D3']), (34, 4, 3, 0)),
    'comp 0/30/11': ((tally['comp']['DC'], tally['comp']['RC'], tally['comp']['NC']), (0, 30, 11)),
    'retrieval 775/750/430/389/41': ((retr['requested'], retr['returned'], retr['unique_records'], retr['excluded'], retr['included']), (775, 750, 430, 389, 41)),
    'preprint pct 26.8': (round(100 * 11 / 41, 1), 26.8),
    'table3 fam': tuple(tuple(fam[f][x] for x in ('proof', 'test', 'assumption')) for f in 'PNRGSC'),
    'table5 fam': tuple(tuple(fam[f]['comp'][x] for x in ('DC', 'RC', 'NC')) for f in 'PNRGSC'),
    'seminal 5 (1999-2014)': (out['seminal']['n'], 5),
    'in-window 36': (out['seminal']['in_window'], 36),
    'in-window evidence 16/14/6': (tuple(out['seminal']['in_window_evidence'][k] for k in ('proof', 'numerical test', 'assumption')), (16, 14, 6)),
    'seminal evidence 1/2/2': (tuple(out['seminal']['evidence'][k] for k in ('proof', 'numerical test', 'assumption')), (1, 2, 2)),
    'word v3': (wc['v3.0'], 7761), 'word v2': (wc['v2.0'], 7862), 'word v1.3': (wc['v1.3'], 7641),
}
(RUN / 'stage4.5-artifacts/phase-c-checks.json').write_text(json.dumps(out, indent=1, ensure_ascii=False) + '\n', encoding='utf-8')
print(json.dumps(out['stated_vs_recomputed'], indent=1))
print('formula', json.dumps(out['formula'], indent=1))
print('word_counts', wc, 'abstract', out['abstract'])
print('retrieval', {k: v for k, v in retr.items() if k != 'screening_counts'})
print('seminal', out['seminal'])
print('families', json.dumps(fam))
print('reliability', {k: v for k, v in out['reliability'].items() if k != 'dispute_rows'})
print('ledger', json.dumps({k: v for k, v in tally.items() if k != 'audit_evidence'}, indent=1))
