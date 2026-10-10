# CareerMatch AI — Stage 2 Text + CSV Test Report

**Version:** 1.0  
**Date:** 2026-10-10  
**Model:** GPT-6  
**Test:** Supplementary Stage 2 LLM execution  
**Reported Status:** PASS  
**Review Status:** PASS WITH REVIEW NOTES

## 1. Objective

Evaluate nine structured CSV requirements against an unstructured synthetic candidate CV using an evidence-based language model.

The original job description was provided as a reference for requirement verification.

This test supplements the original Chain B evaluation without modifying its historical results.

## 2. Inputs

| File                                      | Format        | Role                      |
| ----------------------------------------- | ------------- | ------------------------- |
| `sample_data/synthetic_candidate_cv.md`   | Markdown text | Candidate evidence        |
| `tests/multimodal/requirements_input.csv` | CSV table     | Requirement IDs and texts |
| `sample_data/sample_job_description.txt`  | Plain text    | Source verification       |

## 3. Recorded Results

| Metric                 | Result                 |
| ---------------------- | ---------------------- |
| Requirements evaluated | 9                      |
| Fully matched          | 7                      |
| Partially matched      | 2                      |
| Not verifiable         | 0                      |
| Not matched            | 0                      |
| Weighted points        | 8.0 / 9.0              |
| CV-only alignment      | 88.89%                 |
| Confirmed alignment    | 88.89%                 |
| Official ATS score     | Not applicable         |
| Human approval         | PENDING_HUMAN_APPROVAL |
| External submission    | Not performed          |

**Calculation:**

(7 × 1.0 + 2 × 0.5) / 9 × 100 = 88.89%

## 4. Evidence and Validation

The model reported that:

- All nine CSV requirements were evaluated once.
- Both text and CSV inputs were used.
- CSV requirements matched the job description.
- Candidate claims were supported by quoted CV evidence.
- No additional user confirmations were assumed.
- Human approval remained pending.

These are recorded model-reported checks, not an independent verification of every claim.

## 5. Review Notes

### REQ-005 — User Stories, Use Cases, and Flow Diagrams

**Model classification:** PARTIALLY_MATCHED

The synthetic CV explicitly documents user stories, use cases, BPMN process modeling, and process diagrams.

The model considered the absence of the exact phrase "flow diagrams" a limitation.

**Review disposition:** The partial-match decision is conservative but may warrant reconsideration. The documented process diagrams provide relevant evidence. No historical output has been changed.

### REQ-008 — AI and Technology Trends

**Model classification:** PARTIALLY_MATCHED

The CV documents an AI workflow prototype and participation in AI-assisted workflow improvement.

The model did not consider broader awareness of current technology trends independently established.

**Review disposition:** Retain as a conservative partial match unless additional evidence is supplied.

## 6. Comparison with Original Chain B

| Metric             | Original Chain B | Supplementary Stage 2 |
| ------------------ | ---------------: | --------------------: |
| Fully matched      |                8 |                     7 |
| Partially matched  |                1 |                     2 |
| Evidence alignment |           94.44% |                88.89% |

The supplementary result is 5.55 percentage points lower.

The tests were not a controlled comparison of input formats. Differences cannot be attributed solely to CSV input or prompt quality.

## 7. Limitations

- One supplementary LLM execution was recorded.
- The candidate and employer are fictional.
- No independent employment or education verification occurred.
- Execution time and token consumption were not measured.
- Model-reported validation does not replace external audit.
- This test demonstrates Stage 2 text-and-table processing, not a complete new four-stage execution using both input formats.
- The alignment score is an internal evidence measure, not an ATS or hiring score.

## 8. Conclusion

The supplementary Stage 2 execution produced a complete nine-requirement matching result using text and CSV inputs.

The recorded output satisfied the main structural and arithmetic checks, with two conservative partial matches requiring review.

**Final human approval remains mandatory. No application was submitted.**
