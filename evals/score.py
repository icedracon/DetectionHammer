#!/usr/bin/env python3
"""Score manually reviewed agent trials. Does not run models or verify reviewer claims."""
import argparse,json,pathlib,sys
CONDITIONS=('no_skill','public_preview','candidate')

def score(cases,trials):
    expected={c['id']:c for c in cases}
    seen=set(); results={c:[] for c in CONDITIONS}
    for t in trials:
        key=(t['condition'],t['case_id'])
        if key in seen or key[0] not in results or key[1] not in expected:
            raise ValueError('Duplicate or unknown trial: '+str(key))
        seen.add(key); c=expected[key[1]]
        if not all(isinstance(t.get(k),str) and t[k].strip() for k in ('model','client','settings_id','input_sha256','reviewer')):
            raise ValueError('Missing provenance: '+str(key))
        if len(t['input_sha256'])!=64 or any(ch not in '0123456789abcdef' for ch in t['input_sha256']):
            raise ValueError('Invalid input digest')
        a=t['criteria_pass']; citations=t['citation_checks']
        if not isinstance(a,list) or len(a)!=len(c['criteria']) or any(type(v) is not bool for v in a):
            raise ValueError('Each criterion requires a boolean')
        if not isinstance(citations,list) or any(type(v) is not bool for v in citations): raise ValueError('Invalid citation checks')
        if any(type(t.get(k)) is not bool for k in ('observed_activation','critical_failure')): raise ValueError('Invalid activation or critical failure flag')
        if key[0]=='no_skill' and t['observed_activation']: raise ValueError('No-skill condition cannot activate absent skill')
        results[key[0]].append(t)
    for cid in expected:
        group=[t for t in trials if t['case_id']==cid]
        if len({(t['model'],t['client'],t['settings_id'],t['input_sha256']) for t in group})>1:
            raise ValueError('Non-comparable trials: '+cid)
    out={}
    for cond, group in results.items():
        n=len(group); success=sum(all(t['criteria_pass']) and not t['critical_failure'] for t in group)
        act=sum(t['observed_activation']==expected[t['case_id']]['expected_activation'] for t in group)
        checks=[v for t in group for v in t['citation_checks']]
        critical=sum(t['critical_failure'] for t in group)
        out[cond]={'completed':n,'required':len(cases),'task_success':success/n if n else None,'activation_accuracy':act/n if n and cond!='no_skill' else None,'citation_accuracy':sum(checks)/len(checks) if checks else None,'citation_checks':len(checks),'critical_failures':critical}
    c=out['candidate']; complete=all(v['completed']==len(cases) for v in out.values())
    meets=complete and c['task_success']>=.90 and c['activation_accuracy']>=.95 and c['citation_accuracy'] is not None and c['citation_accuracy']>=.95 and c['critical_failures']==0
    return {'conditions':out,'complete':complete,'numeric_targets_met':meets,'independence_verified':False,'release_approved':False,'note':'Manual scores only; audit reviewer independence, citation applicability and actual model/client logs separately.'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('trials',type=pathlib.Path);a=p.parse_args()
    try:
        cases=json.loads((pathlib.Path(__file__).parent/'cases.json').read_text())['cases']; trials=json.loads(a.trials.read_text());print(json.dumps(score(cases,trials),indent=2))
    except (OSError,ValueError,KeyError,TypeError) as e:
        p.exit(2,str(e)+'\n')
if __name__=='__main__':main()
