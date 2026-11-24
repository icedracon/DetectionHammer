#!/usr/bin/env python3
"""Offline catalog and fixture checker. No network, subprocess or host modification."""
import argparse, collections, json, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
def read(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))
def catalog():
    return read('references/catalog.json')['scenarios']
def matches(rule, event):
    return event.get('channel') == rule['channel'] and type(event.get('event_id')) is int and event['event_id'] == rule['event_id']
def fixtures():
    rules = {r['name']:r for r in read('assets/rules/watch-rules.json')}
    cases = read('assets/fixtures/watch-fixtures.json')
    errors = [c for c in cases if matches(rules[c['rule']], c['event']) != c['expected']]
    print(json.dumps({'fixtures':len(cases),'passed':len(cases)-len(errors),'errors':errors,'mode':'synthetic_visibility_only'},indent=2))
    return int(bool(errors))
def validate():
    rows=catalog(); errors=[]; ids=set(); titles=set(); counts=collections.Counter()
    required={'id','module','title','mode','event_ids','attack_candidate','attack_mapping_status','sources','prerequisites','detection_hypothesis','positive_evidence','negative_control','limitations','references'}
    expected={'KRB':20,'NTL':12,'LDAP':10,'PKI':20,'DEL':12,'ACL':15,'DC':10,'GPO':10,'LAT':12,'IDN':10,'TRU':9,'PER':10}
    for r in rows:
        if not required <= r.keys(): errors.append('missing fields'); continue
        i=r['id']; counts[r['module']]+=1
        if i in ids or r['title'] in titles: errors.append('duplicate: '+i)
        ids.add(i); titles.add(r['title'])
        if not re.fullmatch(r'DH-[A-Z]+-\d{3}',i) or not i.startswith('DH-'+r['module']+'-'): errors.append('ID: '+i)
        if r['mode'] not in ('configuration_review','evidence_review'): errors.append('mode: '+i)
        if (r['mode']=='configuration_review') != (not r['event_ids']): errors.append('event mode: '+i)
        if any(type(e) is not int or e<=0 for e in r['event_ids']): errors.append('event IDs: '+i)
        if r['attack_candidate'] and not re.fullmatch(r'T\d{4}(?:\.\d{3})?',r['attack_candidate']): errors.append('ATT&CK ID: '+i)
        if not all(r[k] for k in required-{'attack_candidate','event_ids'}): errors.append('empty field: '+i)
        if not (ROOT/'references'/f"{r['module'].lower()}.md").is_file(): errors.append('reference: '+i)
    if counts!=expected: errors.append('module counts')
    print(json.dumps({'catalog_entries':len(rows),'module_counts':dict(counts),'candidate_attack_mappings':sum(bool(r['attack_candidate']) for r in rows),'modes':dict(collections.Counter(r['mode'] for r in rows)),'errors':errors,'scope':'structural checks only'},indent=2))
    return int(bool(errors))
def main():
    p=argparse.ArgumentParser(); sub=p.add_subparsers(dest='cmd',required=True)
    sub.add_parser('validate'); sub.add_parser('fixtures'); lp=sub.add_parser('list'); lp.add_argument('--module',choices=['KRB','NTL','LDAP','PKI','DEL','ACL','DC','GPO','LAT','IDN','TRU','PER']); sp=sub.add_parser('show'); sp.add_argument('id')
    a=p.parse_args()
    if a.cmd=='validate': return validate()
    if a.cmd=='fixtures': return fixtures()
    if a.cmd=='list':
        for r in catalog():
            if not a.module or r['module']==a.module: print(r['id'],r['title'],sep='\t')
        return 0
    for r in catalog():
        if r['id']==a.id: print(json.dumps(r,indent=2)); return 0
    print('Unknown scenario',file=sys.stderr); return 2
if __name__=='__main__': sys.exit(main())
