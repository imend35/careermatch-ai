
import csv
import json
from pathlib import Path

# I locate the project root relative to this test file.
ROOT = Path(__file__).resolve().parents[2]

# I define the text, tabular, and reference inputs.
JOB_PATH = ROOT / "sample_data/sample_job_description.txt"
CSV_PATH = ROOT / "tests/multimodal/requirements_input.csv"
STAGE1_PATH = ROOT / "tests/chain_b/stage1/chain_b_stage1_output.json"


def validate_inputs():
    # I read the original job advertisement as text.
    job_text = JOB_PATH.read_text(encoding="utf-8")

    # I parse the CSV as structured tabular data.
    with CSV_PATH.open(encoding="utf-8-sig", newline="") as file:
        csv_rows = list(csv.DictReader(file))

    # I load the existing Stage 1 extraction for comparison.
    stage1 = json.loads(STAGE1_PATH.read_text(encoding="utf-8"))

    extracted = {
        item["id"]: item
        for item in stage1["requirements"]
    }

    issues = []
    seen_ids = set()

    for row in csv_rows:
        requirement_id = row["requirement_id"]
        requirement_text = row["requirement_text"]

        # I detect duplicate requirement identifiers.
        if requirement_id in seen_ids:
            issues.append(f"Duplicate requirement ID: {requirement_id}")
        seen_ids.add(requirement_id)

        # I verify that the CSV text exists in the original posting.
        if requirement_text not in job_text:
            issues.append(f"{requirement_id}: text not found in job posting")

        # I verify that the requirement exists in Stage 1.
        if requirement_id not in extracted:
            issues.append(f"{requirement_id}: missing from Stage 1")
            continue

        # I compare the CSV text with the extracted requirement.
        if requirement_text != extracted[requirement_id]["text"]:
            issues.append(f"{requirement_id}: Stage 1 text mismatch")

    # I check that the CSV and Stage 1 cover the same requirement IDs.
    if seen_ids != set(extracted):
        issues.append("CSV and Stage 1 requirement ID sets differ")

    result = {
        "status": "PASS" if not issues else "FAIL",
        "input_types": ["text", "csv_table"],
        "csv_rows": len(csv_rows),
        "stage1_requirements": len(extracted),
        "issues": issues,
        "scope": "Deterministic text/CSV consistency check"
    }

    print(json.dumps(result, indent=2, ensure_ascii=False))
    return not issues


if __name__ == "__main__":
    raise SystemExit(0 if validate_inputs() else 1)
