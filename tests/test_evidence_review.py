import itertools
import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "skills/detectionhammer-ad/scripts"))
from evidence_review import GATES, evaluate

class EvidenceTests(unittest.TestCase):
    def test_all_boolean_combinations(self):
        for mode in ("synthetic", "imported_lab_evidence", "posture_review"):
            for bits in itertools.product((False, True), repeat=len(GATES)):
                r = dict(zip(GATES, bits), mode=mode, evidence_refs=["synthetic:1"])
                out = evaluate(r)
                self.assertFalse(out["coverage_eligible"])
                self.assertFalse(out["evidence_verified_by_tool"])
                if not r["authorized"]:
                    self.assertEqual(out["verdict"], "INCONCLUSIVE")
                    self.assertEqual(out["evidence_refs"], [])
                if out["verdict"] == "NO_ALERT_REPORTED_IN_COMPLETE_QUERY":
                    for gate in ("authorized", "execution_confirmed", "expected_alert",
                                 "sources_complete", "ingestion_window_elapsed", "correlation_verified"):
                        self.assertTrue(r[gate])
                    self.assertFalse(r["alert_observed"])
                    self.assertNotEqual(mode, "posture_review")
                if mode == "posture_review":
                    self.assertEqual(out["alert"], "UNKNOWN")
                    self.assertEqual(out["prevention"], "UNVERIFIED")

    def test_validation(self):
        r = dict.fromkeys(GATES, True)
        r.update(mode="synthetic", evidence_refs=["fixture:1"])
        for change in ({"authorized": 1}, {"mode": "unknown"}, {"mode": []}, {"mode": {}}, {"evidence_refs": [""]},
                       {"evidence_refs": ["x", "x"]}, {"evidence_refs": "x"}):
            with self.assertRaises(ValueError):
                evaluate(dict(r, **change))

    def test_independent_axes(self):
        r = dict.fromkeys(GATES, True)
        r.update(mode="synthetic", evidence_refs=["fixture:1"])
        out = evaluate(r)
        self.assertEqual(out["alert"], "REPORTED")
        self.assertEqual(out["prevention"], "REPORTED")
        self.assertEqual(out["verdict"], "PREVENTION_REPORTED")

if __name__ == "__main__":
    unittest.main()
