import importlib.util,json,pathlib,unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('score',ROOT/'evals/score.py'); mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
CASES=json.loads((ROOT/'evals/cases.json').read_text())['cases']
def sample():
    return [dict(condition=cond,case_id=c['id'],model='mock',client='mock',settings_id='1',input_sha256='a'*64,reviewer='synthetic',criteria_pass=[True]*len(c['criteria']),observed_activation=c['expected_activation'] if cond!='no_skill' else False,citation_checks=[True],critical_failure=False) for cond in mod.CONDITIONS for c in CASES]
class BenchTests(unittest.TestCase):
    def test_empty(self):
        o=mod.score(CASES,[]);self.assertFalse(o['complete']);self.assertFalse(o['numeric_targets_met']);self.assertIsNone(o['conditions']['candidate']['task_success'])
    def test_complete_synthetic(self):
        o=mod.score(CASES,sample());self.assertTrue(o['numeric_targets_met']);self.assertFalse(o['release_approved'])
    def test_critical_failure(self):
        t=sample();t[-1]['critical_failure']=True;self.assertFalse(mod.score(CASES,t)['numeric_targets_met'])
    def test_duplicate(self):
        t=sample();self.assertRaises(ValueError,mod.score,CASES,t+[t[0]])
    def test_noncomparable(self):
        t=sample();t[-1]['input_sha256']='b'*64;self.assertRaises(ValueError,mod.score,CASES,t)
    def test_partial(self):
        self.assertFalse(mod.score(CASES,sample()[:-1])['numeric_targets_met'])
