# CareerMatch AI — Multimodal Input Validation Report

**Version:** 1.0  
**Date:** 2026-10-10  
**Project:** CareerMatch AI  
**Test Status:** PASS

## 1. Objective

Validate that the CareerMatch AI demonstration can process two distinct input representations: unstructured job description text and a structured CSV requirements table.

## 2. Test Inputs

| Input                | Format | Source                                            |
| -------------------- | ------ | ------------------------------------------------- |
| Job description      | TXT    | `sample_data/sample_job_description.txt`          |
| Requirements table   | CSV    | `tests/multimodal/requirements_input.csv`         |
| Reference extraction | JSON   | `tests/chain_b/stage1/chain_b_stage1_output.json` |

All inputs contain fictional demonstration data.

## 3. Validation Method

The Python script `tests/multimodal/validate_multimodal.py`:

1. Reads the original job description as text.
2. Parses the CSV as structured tabular data.
3. Loads the previously recorded Stage 1 requirement extraction.
4. Checks for duplicate requirement identifiers.
5. Verifies that each CSV requirement appears in the original job description.
6. Compares CSV requirement text against Stage 1 extraction.
7. Confirms that both requirement ID sets match.

## 4. Recorded Execution

**Command:**

```powershell
python tests/multimodal/validate_multimodal.py
```

**Observed output:**

```json
{
  "status": "PASS",
  "input_types": ["text", "csv_table"],
  "csv_rows": 9,
  "stage1_requirements": 9,
  "issues": [],
  "scope": "Deterministic text/CSV consistency check"
}
```

## 5. Results

| Validation Criterion                       | Result |
| ------------------------------------------ | ------ |
| Job description text read                  | PASS   |
| Structured CSV parsed                      | PASS   |
| Nine CSV requirements checked              | PASS   |
| CSV and Stage 1 requirement IDs consistent | PASS   |
| No validation issues reported              | PASS   |

## 6. Limitations

This test demonstrates deterministic processing and consistency checking across text and CSV inputs.

It does not demonstrate that a new four-stage LLM execution consumed the CSV directly.

It does not measure model accuracy, inference latency, token consumption, or external ATS performance.

The existing Baseline A versus Chain B evaluation remains unchanged.

## 7. Conclusion

The deterministic multimodal-input consistency check passed with nine requirements and zero reported issues.

A separate Chain B execution with the structured CSV explicitly included as an input is required to establish end-to-end text-and-table processing within the prompt chain.

**Human approval remains mandatory before any external application action.**
