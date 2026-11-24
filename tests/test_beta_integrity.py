import json, pathlib, unittest, re
ROOT=pathlib.Path(__file__).resolve().parents[1]
S=ROOT/'skills/detectionhammer-ad'; R=S/'references'
class BetaIntegrity(unittest.TestCase):
    def test_association_review(self):
        rows=json.loads((R/'catalog.json').read_text())['scenarios']
        mapped=[x for x in rows if x['attack_candidate']]
        self.assertEqual(len(mapped),34)
        for x in mapped:
            self.assertIn(x['attack_mapping_status'], {'concept_association_reviewed','related_context_reviewed'})
            self.assertIn('https://attack.mitre.org/techniques/'+x['attack_candidate'].replace('.','/')+'/',x['references'])
        by={x['id']:x for x in rows}
        for k,v in {'DH-IDN-007':'T1098.007','DH-PER-003':'T1098.007','DH-PER-005':'T1685.001','DH-PER-006':'T1685.005'}.items():
            self.assertEqual(by[k]['attack_candidate'],v)
        self.assertEqual(sum(x.get('review_depth')=='expanded_reference' for x in rows),150)
    def test_full_methodology_and_csv(self):
        import csv
        rows=json.loads((R/'catalog.json').read_text())['scenarios']
        csvrows=list(csv.DictReader((R/'catalog.csv').read_text(encoding='utf-8').splitlines()))
        for field in ('positive_evidence','negative_control','limitations'):
            self.assertEqual(len({x[field] for x in rows}),150,field)
            self.assertTrue(all(len(x[field])>24 for x in rows),field)
        for a,b in zip(rows,csvrows):
            for field in ('id','module','positive_evidence','negative_control','limitations','review_depth'):
                self.assertEqual(a[field],b[field],(a['id'],field))
    def test_markdown_exact_sections(self):
        for x in json.loads((R/'catalog.json').read_text())['scenarios']:
            md=(R/(x['module'].lower()+'.md')).read_text()
            block=md.split('## '+x['id']+' · '+x['title'],1)[1].split('\n## ',1)[0]
            for k in ('positive_evidence','negative_control','limitations','attack_mapping_status'):
                self.assertIn(x[k],block)
    def test_eval_pack(self):
        data=json.loads((ROOT/'evals/cases.json').read_text());cases=data['cases']
        self.assertEqual(len(cases),20);self.assertEqual(len({x['id'] for x in cases}),20)
        self.assertEqual(data['status'],'unexecuted');self.assertTrue(any(not x['expected_activation'] for x in cases))
        self.assertTrue(all(x['criteria'] for x in cases))
    def test_skill_local_links(self):
        for link in re.findall(r'\[[^\]]+\]\(([^)]+)\)',(S/'SKILL.md').read_text()):
            if '://' not in link:self.assertTrue((S/link).is_file(),link)
        self.assertTrue((ROOT/'assets/detectionhammer-cinematic.webp').is_file())
if __name__=='__main__':unittest.main()
