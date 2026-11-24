import unittest,json,sys,pathlib,re,collections,subprocess
import yaml
ROOT=pathlib.Path(__file__).resolve().parents[1]
S=ROOT/'skills/detectionhammer-ad'
sys.path.insert(0,str(S/'scripts'))
from evidence_verdict import evaluate
from dh_review import matches

def read(p):return json.loads(p.read_text())
class ReleaseTests(unittest.TestCase):
 def test_real_yaml_matches_fixture_semantics(self):
  rules=read(S/'assets/rules/watch-rules.json'); fixtures=read(S/'assets/fixtures/watch-fixtures.json')
  self.assertEqual(len({r['id'] for r in rules}),len(rules))
  self.assertEqual(len(list((S/'assets/rules').glob('*.yml'))),len(rules))
  by={}
  for r in rules:
   d=yaml.safe_load((S/'assets/rules'/f"{r['name']}.yml").read_text())
   self.assertEqual(d['id'],r['id']);self.assertEqual(d['status'],'experimental')
   self.assertEqual(d['logsource'],{'product':'windows','service':'security'})
   self.assertEqual(d['detection'],{'selection':{'EventID':r['event_id']},'condition':'selection'})
   by[r['name']]={'channel':'Security','event_id':d['detection']['selection']['EventID']}
  for c in fixtures:
   with self.subTest(rule=c['rule'],event=c['event']):self.assertEqual(matches(by[c['rule']],c['event']),c['expected'])
 def test_catalog_csv_agreement(self):
  import csv
  a=read(S/'references/catalog.json')['scenarios']; b=list(csv.DictReader((S/'references/catalog.csv').read_text(encoding='utf-8').splitlines()))
  self.assertEqual(len(a),len(b));self.assertEqual(len(a),150)
  for r,c in zip(a,b):
   self.assertEqual((r['id'],r['title'],r['mode'],r['detection_hypothesis']),(c['id'],c['title'],c['mode'],c['detection_hypothesis']))
   self.assertEqual(r['attack_candidate'] or '',c['candidate_attack']);self.assertEqual(','.join(map(str,r['event_ids'])),c['event_ids'])
 def test_markdown_scenario_ids(self):
  a=read(S/'references/catalog.json')['scenarios']
  for r in a:
   self.assertIn('## '+r['id']+' · '+r['title'],(S/'references'/f"{r['module'].lower()}.md").read_text())
 def test_manifest_consistency(self):
  a=read(ROOT/'plugin.json'); front=yaml.safe_load((S/'SKILL.md').read_text().split('---',2)[1]);self.assertEqual(a['name'],front['name']);self.assertEqual(a['version'],front['metadata']['version'])
  for f in ['.claude-plugin/plugin.json','.codex-plugin/plugin.json']:
   b=read(ROOT/f);self.assertEqual((a['name'],a['version']),(b['name'],b['version']))
  self.assertLess(len(front['description']),1024);self.assertLess(len((S/'SKILL.md').read_text().splitlines()),500)
  self.assertEqual(read(ROOT/'.claude-plugin/marketplace.json')['plugins'][0]['name'],a['name'])
  self.assertEqual(read(ROOT/'.agents/plugins/marketplace.json')['plugins'][0]['name'],a['name'])
 def test_cli(self):
  for cmd in ['validate','fixtures']:
   self.assertEqual(subprocess.run([sys.executable,str(S/'scripts/dh_review.py'),cmd],capture_output=True).returncode,0)
 def test_verdict_matrix(self):
  b={k:True for k in ('authorized','execution_confirmed','expected_alert','sources_complete','ingestion_window_elapsed','correlation_verified','telemetry_observed')};b.update(mode='synthetic',evidence_refs=['synthetic:001'],alert_observed=False,prevention_confirmed=False)
  for override,expected in [({},'NO_ALERT_REPORTED_IN_COMPLETE_QUERY'),({'authorized':False},'INCONCLUSIVE'),({'sources_complete':False},'INCONCLUSIVE'),({'ingestion_window_elapsed':False},'INCONCLUSIVE'),({'correlation_verified':False},'INCONCLUSIVE'),({'execution_confirmed':False},'INCONCLUSIVE'),({'evidence_refs':[]},'INCONCLUSIVE'),({'expected_alert':False},'NO_ALERT_EXPECTED'),({'alert_observed':True},'ALERT_REPORTED'),({'prevention_confirmed':True,'execution_confirmed':False},'PREVENTION_REPORTED'),({'mode':'posture_review'},'NOT_RUNTIME_VALIDATION')]:
   with self.subTest(override=override):
    out=evaluate(b|override);self.assertEqual(out['verdict'],expected);self.assertFalse(out['coverage_eligible'])
  with self.assertRaises(ValueError):evaluate(b|{'sources_complete':'true'})
 def test_no_execution_hooks(self):
  self.assertFalse((ROOT/'hooks').exists()); self.assertFalse((ROOT/'.mcp.json').exists());self.assertFalse((ROOT/'mcp.json').exists())
if __name__=='__main__':unittest.main()
