# 🚀 CareerMatch AI

**Evidence-Based Job Application Assistant | Prompt Engineering & Responsible AI Portfolio Project**

CareerMatch AI is an evidence-based, multi-stage AI workflow designed to analyze job descriptions, match candidate qualifications against documented CV evidence, generate tailored application materials, and audit claims before human approval.

The project demonstrates **prompt chaining, structured outputs, evidence traceability, hallucination prevention, evaluation design, and human-in-the-loop AI governance**.

It also includes a comparison between a single-shot prompting approach (**Baseline A**) and a four-stage prompt chain (**Chain B**).

> **Privacy & Ethics:** All publicly shared candidate profiles, organizations, and job advertisements are fictional. The project does not perform real ATS assessments, predict hiring outcomes, or automatically submit job applications.

---

## 1. Project Overview

Traditional AI-assisted job application workflows may introduce unsupported qualifications, overlook job requirements, or produce application documents without sufficient evidence verification.

CareerMatch AI addresses these risks through an evidence-first approach.

### Project Objectives

- Extract qualifications and responsibilities from job advertisements.
- Match requirements against verifiable CV statements.
- Distinguish documented qualifications from unverified information.
- Generate tailored professional summaries, relevant skills, and cover letters.
- Detect unsupported claims and potential hallucinations.
- Require explicit human approval before any external application action.
- Compare single-shot prompting with a structured prompt-chain architecture.

**Core Principle:**

> Every material claim must be traceable to documented evidence. The model may assist with analysis and drafting, but it must not invent qualifications or authorize application submission.

---

## 2. System Architecture

CareerMatch AI uses a four-stage prompt chain.

```text
                  JOB DESCRIPTION
                         |
                         v
          +-----------------------------+
          | Stage 1                     |
          | Requirement Extraction      |
          +-----------------------------+
                         |
                         v
                Requirements JSON
                         |
                         |       SYNTHETIC CV
                         |             |
                         v             v
          +-----------------------------+
          | Stage 2                     |
          | Evidence-Based CV Matching  |
          +-----------------------------+
                         |
                         v
                 Evidence Matrix
                         |
                         v
          +-----------------------------+
          | Stage 3                     |
          | Application Drafting        |
          +-----------------------------+
                         |
                         v
                Application Drafts
                         |
                         v
          +-----------------------------+
          | Stage 4                     |
          | Independent Claim Audit     |
          +-----------------------------+
                         |
                         v
                  Audit Results
                         |
                         v
              HUMAN APPROVAL GATE
                         |
                  Approval Pending
```

The workflow separates extraction, evidence matching, drafting, and auditing into independently inspectable stages.

### Stage 1 — Requirement Extraction

**Prompt:** `prompts/01_requirement_extractor.md`

Extracts job requirements and responsibilities from the original advertisement.

Key features:

- Job metadata identification
- Requirement classification
- Required/preferred/unspecified priority handling
- Source evidence quotations
- Stable requirement and responsibility IDs
- Structured JSON output
- Protection against instructions embedded in job advertisements

**Test results:**

- 9 requirements extracted
- 7 responsibilities extracted
- 16 source evidence quotations checked
- JSON structure validated

### Stage 2 — Evidence-Based CV Matching

**Prompt:** `prompts/02_cv_matcher.md`

Matches each job requirement against documented candidate qualifications.

Matching classifications:

| Classification    | Description                                               |
| ----------------- | --------------------------------------------------------- |
| MATCHED           | Requirement supported by CV evidence                      |
| PARTIALLY_MATCHED | Some elements supported; others remain unverified         |
| NOT_MATCHED       | Requirement not demonstrated by the available CV evidence |
| NOT_VERIFIABLE    | Insufficient information to determine the match           |

Evidence provenance classifications:

- `CV_DOCUMENTED`
- `USER_CONFIRMED`
- `NOT_VERIFIABLE`

**Test results:**

- 8 matched requirements
- 1 partially matched requirement
- 0 unmatched requirements
- 16 CV evidence quotations checked

No user-confirmed evidence was supplied during the synthetic evaluation.

### Stage 3 — Evidence-Based Application Drafting

**Prompt:** `prompts/03_application_drafter.md`

Generates application materials using documented candidate evidence.

Outputs:

- Tailored professional summary
- Relevant skills
- Short cover letter
- Supporting evidence references

The drafting stage must not invent professional experience, achievements, certifications, tools, employment eligibility, or quantified business outcomes.

All generated content remains subject to human review.

### Stage 4 — Independent Audit & Human Approval

**Prompt:** `prompts/04_independent_auditor.md`

Reviews the application drafts against the original job advertisement, synthetic CV, and preceding stage outputs.

Audit checks include:

- Claim-to-evidence verification
- Requirement consistency
- Unsupported claim detection
- Evidence provenance
- Privacy and synthetic-data safeguards
- Human approval requirements

**Recorded test results:**

- 10/10 internal validation checks passed
- Audit status: `PASS_WITH_NOTES`
- Human approval: `PENDING_HUMAN_APPROVAL`
- External submission: Not authorized

The separate audit stage improves process inspectability. It does not establish independent verification by a different model or external reviewer.

---

## 3. Baseline A vs. Chain B — A/B Evaluation

The project compares two prompt engineering approaches using the same fictional job advertisement and synthetic candidate profile.

### Baseline A — Single-Shot Prompting

A single prompt performs requirement extraction, evidence matching, application drafting, and claim auditing in one response.

### Chain B — Multi-Stage Prompt Chaining

Four specialized prompts perform the same overall workflow through separate, structured stages.

### Evaluation Results

**Evaluation date:** October 10, 2026

**Model:** GPT-6 recorded for Baseline A. Chain B was conducted in a GPT-6 conversation; separate per-stage model configurations were not recorded.

| Evaluation Metric              | Baseline A             | Chain B          |
| ------------------------------ | ---------------------- | ---------------- |
| Requirements extracted         | 9/9                    | 9/9              |
| Responsibilities extracted     | 7/7                    | 7/7              |
| Fully matched requirements     | 8                      | 8                |
| Partially matched requirements | 1                      | 1                |
| Evidence alignment             | 94.44%                 | 94.44%           |
| K1–K4 checks                   | 4/4 PASS               | 4/4 PASS         |
| Claim audit                    | Within single response | Separate Stage 4 |
| Evidence provenance            | Documented             | Documented       |
| Human approval                 | Not authorized         | Pending          |
| Execution time                 | Not recorded           | Not recorded     |
| Manual correction time         | Not recorded           | Not recorded     |

### Evidence Alignment Calculation

The evaluation uses a custom requirement-matching rubric:

- MATCHED = 1 point
- PARTIALLY_MATCHED = 0.5 points
- NOT_MATCHED = 0 points

For the nine requirements:

```text
Alignment = ((8 × 1) + (1 × 0.5)) / 9 × 100

Alignment = 94.44%
```

**Important:** This percentage is an internal evidence-alignment measure, not an ATS score, hiring probability, or prediction of interview success.

### Evaluation Criteria

| Criterion | Description                                                                                     |
| --------- | ----------------------------------------------------------------------------------------------- |
| K1        | Extract all nine requirements and seven responsibilities                                        |
| K2        | Classify and match all nine requirements against CV evidence                                    |
| K3        | Produce application drafts without unsupported material claims                                  |
| K4        | Include claim auditing, provenance separation, missing information, and human approval controls |

The criteria were defined operationally in the Baseline A report and retrospectively mapped to Chain B artifacts.

### Key Findings

Both approaches achieved the same observed requirement coverage and evidence-alignment results.

Chain B provides additional architectural benefits:

- Separation of responsibilities between stages
- More inspectable intermediate JSON artifacts
- Easier identification of stage-specific errors
- A distinct auditing step
- Explicit evidence tracking throughout the workflow

However, the available evaluation does **not** demonstrate that Chain B is more accurate, faster, or less labor-intensive than Baseline A.

### Evaluation Limitations

This is a provisional, partially controlled comparison.

- Only one synthetic job/CV scenario was evaluated.
- One recorded run was available for each approach.
- Exact execution times and token costs were not captured.
- Manual correction duration was not measured.
- Baseline A received a requirements CSV directly, while Chain B initially extracted requirements from the job description.
- The evaluations were not independently blinded.
- No statistical significance or generalization can be established.

The results therefore support a descriptive architectural comparison rather than a universal performance claim.

**Detailed report:** `tests/ab_comparison/AB_COMPARISON_REPORT.md`

---

## Supplementary Text + CSV Input Demonstration

CareerMatch AI includes a supplementary GPT-6 Stage 2 evaluation demonstrating evidence-based CV matching with two input representations:

- **Unstructured text:** Synthetic candidate CV in Markdown.
- **Structured table:** Nine job requirements in CSV format.

The original job description is also used to verify requirement consistency.

### Recorded Results

| Metric                 |                 Result |
| ---------------------- | ---------------------: |
| Requirements evaluated |                      9 |
| Fully matched          |                      7 |
| Partially matched      |                      2 |
| Evidence alignment     |                 88.89% |
| Human approval         | PENDING_HUMAN_APPROVAL |

The supplementary result is separate from the original Baseline A versus Chain B comparison, in which both approaches achieved 94.44% evidence alignment.

The difference does not establish an advantage or disadvantage for either input format.

### Validation

The supplementary deterministic text/CSV consistency test passed:

```bash
python tests/multimodal/validate_multimodal.py
```

The latest recorded local verification also passed all five Python unit tests and the static fixture validator.

### Supporting Files

- `tests/multimodal/requirements_input.csv`
- `tests/multimodal/validate_multimodal.py`
- `tests/multimodal/MULTIMODAL_TEST_REPORT.md`
- `tests/multimodal/STAGE2_TEXT_CSV_PROMPT.md`
- `tests/multimodal/STAGE2_TEXT_CSV_OUTPUT.json`
- `tests/multimodal/STAGE2_TEXT_CSV_TEST_REPORT.md`

**Scope:** One supplementary Stage 2 LLM execution. This is not a new end-to-end four-stage multimodal evaluation or an official ATS assessment.

### Weekly Use Case and Prompt Library

The intended recurring task is a weekly job advertisement and CV alignment review.

See:

- `docs/WEEKLY_USE_CASE.md`
- `docs/PROMPT_LIBRARY_CARDS.md`
- `docs/SELF_EVALUATION.md`

The weekly use case is documented but has not been deployed as an automated recurring service.

---

## 4. Repository Structure

The repository separates reusable prompts, synthetic demonstration data, static validation utilities, and recorded evaluation artifacts.

careermatch-ai/
├── README.md
├── prompts/
│ ├── 01_requirement_extractor.md
│ ├── 02_cv_matcher.md
│ ├── 03_application_drafter.md
│ └── 04_independent_auditor.md
├── sample_data/
│ └── [synthetic job and candidate fixtures]
├── outputs/
│ └── [illustrative JSON fixtures]
├── src/
│ └── validate.py
├── tests/
│ ├── test_validation.py
│ ├── chain_b/
│ │ ├── stage1/
│ │ ├── stage2/
│ │ ├── stage3/
│ │ └── stage4/
│ ├── ab_comparison/
│ │ ├── AB_COMPARISON_REPORT.md
│ │ └── AB_COMPARISON_RUN_LOG.csv
│ └── multimodal/
│ ├── requirements_input.csv
│ ├── validate_multimodal.py
│ ├── MULTIMODAL_TEST_REPORT.md
│ ├── STAGE2_TEXT_CSV_PROMPT.md
│ ├── STAGE2_TEXT_CSV_OUTPUT.json
│ └── STAGE2_TEXT_CSV_TEST_REPORT.md
├── docs/
│ ├── PROJECT_PRESENTATION.md
│ ├── FINAL_SUBMISSION_CHECKLIST.md
│ ├── SELF_EVALUATION.md
│ ├── PROMPT_LIBRARY_CARDS.md
│ └── WEEKLY_USE_CASE.md
└── make_demo_outputs.py

````

The `outputs/` directory contains illustrative static demo fixtures. These are distinct from the recorded conversational A/B evaluation artifacts under `tests/`.

---

## 5. Quick Start

### Prerequisites

- Python 3.10 or later
- Git
- A terminal or VS Code

No API key or third-party Python package is required for the existing static validation workflow.

### Clone the Repository

```bash
git clone https://github.com/imend35/careermatch-ai.git
cd careermatch-ai
````

### Run Static Validation

```bash
python -m src.validate
```

### Run Unit Tests

```bash
python -m unittest discover -s tests -v
```

### Regenerate Illustrative Demo Outputs

```bash
python make_demo_outputs.py
python -m src.validate
```

These commands operate on the repository's deterministic demonstration fixtures.

They do not automatically execute the four LLM prompts or reproduce the recorded GPT-6 A/B conversation.

### Reproducing the Prompt Evaluation

To reproduce the conversational experiment:

1. Use the same fictional job description and synthetic candidate CV.
2. Execute the Baseline A single-shot prompt using the specified inputs.
3. Execute Chain B prompts sequentially, passing the required structured outputs between stages.
4. Preserve original model outputs without silently correcting them.
5. Evaluate both approaches using the same K1–K4 criteria.
6. Record model configuration, timestamps, manual corrections, and any deviations from the original inputs.
7. Compare the results and document limitations.

For a stronger future experiment, both approaches should receive informationally equivalent inputs and be evaluated across multiple synthetic scenarios.

---

## 6. Validation and Quality Assurance

The project combines static consistency checks with evidence-based prompt evaluation.

### Static Python Validation

The existing validator checks aspects of the illustrative fixtures, including:

- Requirement and responsibility identifiers
- Literal source evidence presence
- Evidence-reference consistency
- Matching coverage
- Rubric-score arithmetic
- Claim audit coverage
- Submission restrictions while approval is pending

Negative tests intentionally introduce invalid conditions to verify that selected consistency errors are detected.

### LLM Output Evaluation

The recorded prompt evaluation considers:

- Requirement completeness
- Source evidence accuracy
- CV claim support
- Matching classification
- Hallucination prevention
- Structured output validity
- Human approval status

Static validation and LLM evaluation serve different purposes.

Passing deterministic tests does not independently establish that the model's semantic interpretation is correct.

---

## 7. Responsible AI, Privacy & Safety

CareerMatch AI follows an evidence-first and human-controlled approach.

### Evidence Integrity

The workflow must not:

- Invent qualifications or employment history
- Fabricate achievements or certifications
- Treat undocumented assumptions as confirmed facts
- Present unsupported claims as verified evidence
- Misrepresent internal alignment metrics as official ATS scores

### Prompt Injection Resistance

Job advertisements and CV content are treated as untrusted input data.

The prompt chain instructs the model not to follow embedded instructions that attempt to override the workflow's operational rules.

This is a design safeguard, not a guarantee of resistance to every prompt-injection attack.

### Privacy Protection

The public demonstration uses fictional candidate and employer information.

Real applicant CVs, personal contact details, and private application materials should not be committed to public repositories.

### Human-in-the-Loop Approval

Application drafting and application submission are separate actions.

No external application submission is implemented in the current project.

Any future submission functionality must require explicit human authorization.

---

## 8. Technology Stack

| Category           | Technologies / Concepts                                        |
| ------------------ | -------------------------------------------------------------- |
| AI Model           | OpenAI GPT-6 (recorded evaluation)                             |
| Prompt Engineering | Single-Shot Prompting, Prompt Chaining, Role-Based Prompting   |
| Structured Outputs | JSON, Markdown                                                 |
| Evaluation         | K1–K4 Checks, Evidence Alignment, A/B Comparison               |
| Programming        | Python                                                         |
| Validation         | Python unittest, Deterministic Consistency Checks              |
| Version Control    | Git, GitHub                                                    |
| Responsible AI     | Evidence Provenance, Hallucination Auditing, Human-in-the-Loop |

---

## 9. Project Outcomes

The recorded evaluation demonstrates:

- Extraction of 9 job requirements and 7 responsibilities
- Evidence matching across all 9 requirements
- 94.44% internal evidence alignment for both approaches
- Generation of evidence-based application materials
- Separate claim auditing in Chain B
- Explicit human approval controls
- Documentation of experimental limitations

The principal observed advantage of Chain B is **workflow modularity and inspectability**, not a demonstrated improvement in matching accuracy.

---

## 10. Future Improvements

Planned areas for further development:

- Automated orchestration of the four prompt stages
- JSON Schema validation for structured LLM outputs
- Additional synthetic test scenarios
- Automated negative testing for hallucinations and prompt injection
- Repeated-run evaluations
- Latency and token-cost measurement
- Human correction effort tracking
- Blinded evaluation of generated drafts
- More rigorous input-equivalent A/B testing
- Optional application review interface with explicit human authorization

These items represent future work and are not claimed as implemented features.

---

## 11. Author

**Esila Nur Demirci**

Senior Business Analyst | Scrum Master | Data Analytics | AI & Data Engineering

GitHub: https://github.com/imend35

---

## 12. Disclaimer

CareerMatch AI is an educational and portfolio demonstration of evidence-based prompt engineering.

All public candidate and job data are synthetic.

The project does not provide official ATS scores, employment eligibility determinations, hiring predictions, or automatic job application submissions.

**Every generated application document requires human review before real-world use.**

---

_CareerMatch AI — Building more transparent, traceable, and human-controlled AI-assisted career workflows._

**Last Updated:** October 10, 2026
