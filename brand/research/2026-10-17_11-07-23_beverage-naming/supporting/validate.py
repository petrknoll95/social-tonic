"""Validate this research package without network, writes, or external actions."""
from pathlib import Path
import csv,json,re,collections
ROOT=Path(__file__).resolve().parents[1]
errors=[]
def check(ok,msg):
 if not ok:errors.append(msg)
def read_csv(rel):
 with (ROOT/rel).open(encoding='utf-8',newline='') as f:
  rd=csv.DictReader(f);rows=list(rd)
  check(len(rd.fieldnames)==len(set(rd.fieldnames)),f'duplicate header {rel}')
  check(all(None not in r and all(v is not None for v in r.values()) for r in rows),f'ragged CSV {rel}')
 return rows
brands=read_csv('data/brand-name-analysis.csv');evidence=read_csv('data/commercial-evidence.csv');sources=read_csv('sources.csv')
check(len(brands)==48,'brand count');check(collections.Counter(x['sample_group'] for x in brands)=={'beverage':36,'non_beverage':12},'group count')
check(len(evidence)==69,'evidence count');check(len(sources)==144,'source count')
lookup={s['source_id']:s for s in sources};bids={b['brand_id'] for b in brands}
for rows,key in [(brands,'brand_id'),(evidence,'evidence_id'),(sources,'source_id')]:check(len({r[key] for r in rows})==len(rows),f'duplicate {key}')
for b in brands:
 check(int(b['character_count'])==len(b['brand_name']),f'character count {b["brand_id"]}')
 check(int(b['word_count'])==len(b['brand_name'].split()),f'word count {b["brand_id"]}')
 check(b['syllable_count']=='' or (b['syllable_count'].isdigit() and int(b['syllable_count'])>0),f'syllables {b["brand_id"]}')
 for s in b['source_ids'].split(';'):check(s in lookup,f'unknown source {s}')
 check(any(e['brand_id']==b['brand_id'] for e in evidence),f'no commercial evidence {b["brand_id"]}')
for e in evidence:
 check(e['brand_id'] in bids,f'evidence brand {e["evidence_id"]}')
 check(e['source_id'] in lookup,f'evidence source {e["evidence_id"]}')
 if e['source_id'] in lookup:check(e['source_url']==lookup[e['source_id']]['url'],f'evidence URL {e["evidence_id"]}')
 check(bool(e['geography'] and e['period'] and e['provenance'] and e['limitations']),f'evidence scope {e["evidence_id"]}')
for s in sources:
 check(s['url'].startswith(('https://','http://')),f'URL scheme {s["source_id"]}')
 check(s['accessed_date']=='2026-10-17',f'access date {s["source_id"]}')
 check(bool(s['supported_claims'] and s['limitations']),f'claim scope {s["source_id"]}')
 if re.match(r'^\d{4}-\d{2}-\d{2}$',s['publication_date']):check(s['publication_date']<='2026-10-17',f'future source {s["source_id"]}')
# Ensure integrated CSVs match reviewed ledger contents, preserving text types.
for key,rows in [('brands',brands),('evidence',evidence),('sources',sources)]:
 merged=[]
 for name in ['lead','empirical','beverage','language-legal']:
  merged+=json.loads((ROOT/f'supporting/workstreams/{name}.json').read_text()).get(key,[])
 normal=[{k:str(v) for k,v in r.items()} for r in merged]
 check(rows==normal,f'JSON/CSV mismatch {key}')
links=0
for f in list(ROOT.rglob('*.md'))+[ROOT.parent/'README.md']:
 t=f.read_text()
 check(not re.search(r'<!-- (?:SAMPLE_COUNTS|SOURCE_LINKS|EMPIRICAL_TABLE) -->',t),f'placeholder {f.name}')
 defs=dict(re.findall(r'^\[([^\]]+)\]:\s+(\S+)',t,re.M))
 for lab in re.findall(r'\]\[([^\]]+)\]',t):check(lab in defs,f'undefined reference {lab} in {f.name}')
 for target in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)',t)+list(defs.values()):
  target=target.strip('<>')
  if target.startswith(('https://','http://','mailto:','#')):continue
  filepart=target.split('#')[0]
  check((f.parent/filepart).exists(),f'broken local link {f.relative_to(ROOT.parent)} -> {target}');links+=1
 # Check explicit research IDs, excluding longer brand/evidence IDs.
 for sid in re.findall(r'(?<!\w)(?:LEAD|EMP|CON|BEV|LEG)\d{3}(?!\w)',t):check(sid in lookup,f'unknown cited ID {sid} in {f.name}')
report=(ROOT/'report.md').read_text()
for required in ['48 names','69 separate commercial/status observations','144 source records','25/36, 10/36 and 1/36','12/47','10/35','18/43','15/36, 7/36, 12/36 and 2/36']:
 check(required in report,f'missing report-count assertion {required}')
check(collections.Counter(b['commercial_status'] for b in brands)=={'established':24,'emerging_traction':7,'active_scale_unknown':15,'discontinued':2},'status totals')
check(collections.Counter(b['descriptor_independence'] for b in brands)=={'category_opaque':34,'category_partial':12,'category_clear':2},'descriptor totals')
check(sum(b['syllable_count']!='' for b in brands)==43,'syllable denominator')
check(sum(b['syllable_count']=='2' for b in brands)==18,'two-syllable numerator')
print(json.dumps({'brands':len(brands),'evidence_rows':len(evidence),'source_records':len(sources),'unique_source_urls':len({s['url'] for s in sources}),'local_links_checked':links,'errors':errors},ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
