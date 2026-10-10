import json
import tempfile
import unittest
from pathlib import Path
from shutil import copytree
from src.validate import ROOT, check


class DemoValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        copytree(ROOT / "sample_data", self.root / "sample_data")
        copytree(ROOT / "outputs", self.root / "outputs")

    def tearDown(self):
        self.temp.cleanup()

    def test_valid_synthetic_fixture(self):
        result = check(self.root)
        self.assertTrue(result["passed"], result["issues"])

    def test_submission_must_be_blocked(self):
        path = self.root / "outputs/04_quality_validation.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["submission_authorized"] = True
        path.write_text(json.dumps(data), encoding="utf-8")
        self.assertFalse(check(self.root)["passed"])

    def test_fake_cv_evidence_is_rejected(self):
        path = self.root / "outputs/02_cv_matching.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["matching_matrix"][0]["evidence"][0]["exact_quote"] = "Unverifiable invented CV statement"
        path.write_text(json.dumps(data), encoding="utf-8")
        self.assertFalse(check(self.root)["passed"])

    def test_score_mismatch_is_rejected(self):
        path = self.root / "outputs/02_cv_matching.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["scoring"]["cv_only_alignment_percent"] = 23.0
        path.write_text(json.dumps(data), encoding="utf-8")
        self.assertFalse(check(self.root)["passed"])

    def test_missing_job_evidence_is_rejected(self):
        path = self.root / "outputs/01_requirements.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["requirements"][0]["source_evidence"] = "A requirement absent from the posting"
        path.write_text(json.dumps(data), encoding="utf-8")
        self.assertFalse(check(self.root)["passed"])


if __name__ == "__main__":
    unittest.main()
