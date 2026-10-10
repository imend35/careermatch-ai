# CareerMatch AI — Weekly Recurring Use Case

**Project:** CareerMatch AI  
**Course:** Prompt Engineering 2.0 (Multimodal)  
**Version:** 1.0  
**Date:** 2026-10-10

## 1. Real-World Problem

Job seekers frequently need to review new job advertisements, compare requirements with their qualifications, and prepare tailored application materials.

Repeating this work manually every week can be time-consuming and may introduce unsupported claims or inconsistencies.

CareerMatch AI is designed to support this recurring workflow through structured, evidence-based analysis.

## 2. Weekly Task

**Task name:** Weekly Job Opportunity and CV Alignment Review

**Frequency:** At least once per week

**Trigger:** A user selects a new job opportunity for evaluation during their weekly job-search review.

**Expected outcome:** An evidence-based requirement matching report, draft application materials, and an independent claim audit awaiting human approval.

The weekly frequency describes the intended usage scenario. Automated scheduling and repeated real-world execution have not been demonstrated.

## 3. Input Types

The workflow can use:

| Input              | Format           | Purpose                                  |
| ------------------ | ---------------- | ---------------------------------------- |
| Job advertisement  | Text             | Original job requirements                |
| Candidate CV       | Text or Markdown | Candidate qualifications                 |
| Requirements table | CSV              | Structured requirement records           |
| User confirmations | Structured text  | Explicitly confirmed additional evidence |

A supplementary Stage 2 execution demonstrated text-and-CSV processing.

## 4. Four-Stage Workflow

### Stage 1 — Requirement Extraction

Extract qualifications and responsibilities from the job advertisement.

**Output:** Structured requirements with exact source evidence.

**Control:** Verify that extracted requirements are present in the original advertisement.

### Stage 2 — CV Matching

Compare the candidate CV against the extracted requirements.

**Output:** Evidence-based matching matrix and internal alignment calculation.

**Control:** Verify exact CV quotations, matching classifications, and score arithmetic.

### Stage 3 — Application Drafting

Prepare a professional summary, relevant skills section, and cover letter using documented evidence.

**Output:** Draft application materials.

**Control:** Reject invented qualifications, achievements, or employment details.

### Stage 4 — Independent Audit

Audit generated claims against the original source materials.

**Output:** Audit findings and human approval status.

**Control:** Preserve `PENDING_HUMAN_APPROVAL` until explicit authorization.

## 5. Weekly Execution Procedure

1. Select a relevant job advertisement.
2. Prepare the current candidate CV.
3. Extract and verify the job requirements.
4. Review the structured requirements table.
5. Run evidence-based CV matching.
6. Generate application drafts.
7. Audit all material claims.
8. Present the results to the candidate for review.
9. Record the outcome without automatically submitting an application.

## 6. Error Handling

| Condition                     | Expected Behavior                        |
| ----------------------------- | ---------------------------------------- |
| Missing job description       | Stop extraction and report missing input |
| Invalid CSV structure         | Report validation failure                |
| Missing CV evidence           | Mark the requirement as NOT_VERIFIABLE   |
| Unsupported application claim | Flag for review or correction            |
| Inconsistent requirement IDs  | Stop or request reconciliation           |
| Missing human approval        | Block external submission                |

## 7. Human Approval Checkpoint

The candidate must review and explicitly approve any external application action.

A passing audit does not automatically authorize submission.

The demonstration does not implement automatic job applications.

## 8. Evaluation Criteria

The weekly workflow should be assessed using:

- Completeness of requirement extraction
- Accuracy of source quotations
- Coverage of requirement IDs
- Consistency of matching classifications
- Reproducibility of alignment calculations
- Absence of unsupported application claims
- Preservation of the human approval gate

## 9. Current Implementation Evidence

The repository includes:

- Four reusable workflow prompts
- Synthetic job and candidate fixtures
- Recorded Baseline A and Chain B results
- Deterministic validation tests
- Supplementary text-and-CSV validation
- Supplementary Stage 2 LLM execution
- Three reusable prompt library cards
- Final project self-evaluation

## 10. Limitations

This document describes an intended weekly recurring workflow.

It does not establish that:

- The application has been deployed as an automated weekly service.
- Weekly runs have occurred over multiple weeks.
- Real job applications have been submitted.
- The system has been evaluated against real recruitment outcomes.

## 11. Conclusion

CareerMatch AI addresses a realistic, repeatable weekly job-search task.

The project demonstrates how a four-stage prompt workflow can support structured requirement extraction, CV alignment, application drafting, and independent evidence auditing while preserving human control.

**External application actions always require explicit human approval.**
