"""Deterministic checks for the synthetic CareerMatch AI demo.

Usage: python -m src.validate
No LLM calls, no external dependencies, no submission actions.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCORES = {"MATCHED": 1.0, "PARTIALLY_MATCHED": 0.5,
          "NOT_VERIFIABLE": 0.0, "NOT_MATCHED": 0.0}


def check(root: Path = ROOT) -> dict:
    issues = []
    def load(relative):
        path = root / relative
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            issues.append(f"{relative}: unreadable JSON ({exc})")
            return {}

    cv_path = root / "sample_data/synthetic_candidate_cv.md"
    try:
        cv_text = cv_path.read_text(encoding="utf-8")
    except OSError as exc:
        issues.append(f"Missing synthetic Markdown CV: {exc}")
        cv_text = ""

    cv = load("sample_data/synthetic_candidate_cv.json")
    extraction = load("outputs/01_requirements.json")
    matching = load("outputs/02_cv_matching.json")
    draft = load("outputs/03_application_draft.json")
    qa = load("outputs/04_quality_validation.json")

    if cv.get("synthetic") is not True:
        issues.append("Candidate JSON must explicitly mark synthetic=true.")
    requirements = extraction.get("requirements", [])
    responsibilities = extraction.get("responsibilities", [])
    req_ids = [r.get("id") for r in requirements]
    resp_ids = [r.get("id") for r in responsibilities]
    if len(req_ids) != 9 or len(set(req_ids)) != 9:
        issues.append("Expected nine distinct requirement IDs.")
    if len(resp_ids) != 7 or len(set(resp_ids)) != 7:
        issues.append("Expected seven distinct responsibility IDs.")

    job_path = root / "sample_data/sample_job_description.txt"
    try:
        job_text = job_path.read_text(encoding="utf-8")
    except OSError as exc:
        issues.append(f"Missing job description: {exc}")
        job_text = ""
    for record in requirements + responsibilities:
        quote = record.get("source_evidence")
        if not isinstance(quote, str) or not quote.strip() or quote not in job_text:
            issues.append(f"{record.get('id')}: source evidence not found in job posting.")

    matrix = matching.get("matching_matrix", [])
    if {r.get("requirement_id") for r in matrix} != set(req_ids) or len(matrix) != len(req_ids):
        issues.append("Matching matrix does not cover each requirement exactly once.")
    for row in matrix:
        for evidence in row.get("evidence", []):
            kind = evidence.get("source_type")
            quote = evidence.get("exact_quote")
            if kind == "CV_DOCUMENTED" and (not isinstance(quote, str) or quote not in cv_text):
                issues.append(f"{row.get('requirement_id')}: CV quote not found.")
            if kind == "USER_CONFIRMED" and not evidence.get("user_confirmation_date"):
                issues.append(f"{row.get('requirement_id')}: missing confirmation date.")
            if kind not in {"CV_DOCUMENTED", "USER_CONFIRMED", "NOT_VERIFIABLE"}:
                issues.append(f"{row.get('requirement_id')}: invalid evidence source.")

    scoring = matching.get("scoring", {})
    for key, status_key in (("cv_only_alignment_percent", "cv_only_status"),
                            ("confirmed_alignment_percent", "confirmed_status")):
        try:
            expected = round(100 * sum(SCORES[r[status_key]] for r in matrix) / len(matrix), 2)
            if abs(expected - float(scoring[key])) > 0.01:
                issues.append(f"Score mismatch for {key}: expected {expected}.")
        except (KeyError, ZeroDivisionError, TypeError, ValueError) as exc:
            issues.append(f"Cannot calculate {key}: {exc}")
    if scoring.get("official_ats_score") is not None:
        issues.append("Official ATS score must remain null.")

    claims = draft.get("claim_traceability", [])
    claim_ids = [c.get("claim_id") for c in claims]
    if not claims or len(set(claim_ids)) != len(claim_ids):
        issues.append("Missing or duplicate claim IDs.")
    for claim in claims:
        if not set(claim.get("requirement_ids", [])).issubset(set(req_ids)):
            issues.append(f"{claim.get('claim_id')}: unknown requirement ID.")
        if claim.get("evidence_source") == "CV_DOCUMENTED":
            quote = claim.get("exact_quote_or_confirmation")
            if not isinstance(quote, str) or quote not in cv_text:
                issues.append(f"{claim.get('claim_id')}: claim quote not in CV.")
        elif claim.get("evidence_source") == "USER_CONFIRMED":
            if not claim.get("confirmation_date"):
                issues.append(f"{claim.get('claim_id')}: missing confirmation date.")
        else:
            issues.append(f"{claim.get('claim_id')}: unsupported claim source.")

    qa_claim_ids = {c.get("claim_id") for c in qa.get("claim_audit", [])}
    if set(claim_ids) != qa_claim_ids:
        issues.append("QA claim audit does not cover exactly the generated claims.")
    if qa.get("human_approval", {}).get("status") != "PENDING":
        issues.append("Public demo must keep approval PENDING.")
    if qa.get("submission_authorized") is not False:
        issues.append("Public demo must block submission.")
    return {"passed": not issues, "checks": {
        "requirements": len(req_ids), "responsibilities": len(resp_ids),
        "matching_rows": len(matrix), "claims": len(claims)},
        "issues": issues, "scope": "Static synthetic fixture validation; not an LLM evaluation"}


def main():
    result = check()
    print(json.dumps(result, indent=2, ensure_ascii=False))
    raise SystemExit(0 if result["passed"] else 1)


if __name__ == "__main__":
    main()
