import json, urllib.request, time, sys
recs = json.load(open('search/selected_sources.json'))
out = []
for r in recs:
    doi = r['doi']; url = 'https://api.openalex.org/works/doi:' + doi
    row = {'id': r['id'], 'doi': doi, 'expected_title': r['title'], 'expected_year': r['year'], 'expected_first_author': r['authors'].split(',')[0].strip()}
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'ARS-integrity-check/1.0 (mailto:integrity@example.org)'})
        with urllib.request.urlopen(req, timeout=30) as f:
            row['http'] = f.status
            if f.status == 200:
                w = json.load(f)
                row['oa_id'] = w.get('id'); row['title'] = w.get('title'); row['year'] = w.get('publication_year')
                row['doi_echo'] = w.get('doi'); row['is_retracted'] = w.get('is_retracted')
                au = w.get('authorships') or []
                row['first_author'] = (au[0]['author']['display_name'] if au else None)
    except Exception as e:
        row['error'] = repr(e)[:200]
    out.append(row); time.sleep(0.15)
json.dump(out, open('stage4.5-artifacts/round2/phase-a-doi-checks.json','w'), indent=1)
print('done', len(out))
