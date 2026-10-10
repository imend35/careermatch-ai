# CareerMatch AI

**Evidence-Based Job Application Assistant | Prompt Engineering Portfolio Project**

CareerMatch AI demonstrates a four-stage prompt-chain design for analyzing job postings, matching candidate evidence, drafting application materials, and validating claims before human approval.

> **Demo scope:** The public repository uses fully synthetic candidate and job data. Its JSON outputs are illustrative fixtures, **not recorded LLM inference runs**. Static Python checks validate internal consistency, not semantic correctness or real ATS performance.

## Quick Start

Requires Python 3.10+; no API keys or third-party Python packages required for static validation.

```bash
git clone https://github.com/imend35/careermatch-ai.git
cd careermatch-ai
python -m src.validate
python -m unittest discover -s tests -v
```

To regenerate the illustrative demo fixtures:

```bash
python make_demo_outputs.py
python -m src.validate
```

## Four-Stage Prompt Chain

| Stage | Prompt                                | Output                                                          |
| ----- | ------------------------------------- | --------------------------------------------------------------- |
| 1     | `prompts/01_requirement_extractor.md` | Requirements and responsibilities with source evidence          |
| 2     | `prompts/02_cv_matcher.md`            | CV-to-requirement evidence matrix and rubric alignment          |
| 3     | `prompts/03_content_generator.md`     | Tailored summary, CV bullet suggestions, and cover letter draft |
| 4     | `prompts/04_quality_validator.md`     | Claim audit, quality review, and human-approval gate            |

```text
Job description ──> [1] Requirements ──┐
                                       ├──> [2] Evidence matching ──> [3] Drafts ──> [4] QA
Synthetic CV ──────────────────────────┘                                      │
                                                                     Human approval required
```

## Repository Guide

| Location                             | Contents                                                   |
| ------------------------------------ | ---------------------------------------------------------- |
| `prompts/`                           | Four reusable prompt templates                             |
| `sample_data/`                       | Synthetic CV (Markdown/JSON) and fictional job posting     |
| `outputs/`                           | Four illustrative JSON artifacts                           |
| `src/validate.py`                    | Deterministic fixture and evidence-reference checks        |
| `tests/`                             | Positive and negative validation tests                     |
| `evaluation/`                        | Evaluation criteria, A/B test status, and validation guide |
| `docs/PROJECT_PRESENTATION.md`       | English project presentation                               |
| `docs/FINAL_SUBMISSION_CHECKLIST.md` | Release and submission checklist                           |

## Validation

The static validator checks nine requirement IDs and seven responsibility IDs, literal evidence presence in the synthetic sources, match-matrix coverage, rubric-score arithmetic, claim-audit coverage, and blocked submission while approval is pending. Negative tests intentionally introduce errors to ensure they are detected.

These checks **do not** demonstrate that an LLM has correctly interpreted evidence, that the drafts are suitable for a real application, or that an external ATS would assign the displayed score.

## Evaluation Status

- A retrospective review of an earlier **private** job-application exercise reported **3 of 4** predefined criteria met; evidence traceability was incomplete for some claims. That review was **not a controlled A/B test**.
- The public synthetic fixture displays **100% internal rubric alignment** and an **illustrative 91/100 QA score**. Neither number is an official ATS score or an independently measured model result.
- A controlled baseline-vs-chain experiment using identical inputs and timed LLM executions **has not yet been run**. See [`evaluation/AB_TEST_RESULTS.md`](evaluation/AB_TEST_RESULTS.md).

## Responsible AI and Privacy

- No real applicant's CV or contact information is required for the public demo.
- Do not invent qualifications or present user-confirmed details as documented CV evidence.
- Keep source references auditable and flag unsupported claims.
- External application submission is **not implemented** and requires explicit human approval in any future implementation.

## Technology

Prompt Engineering · Generative AI workflow design · Python · JSON · Markdown · Git/GitHub

## Author

**Esila Nur Demirci** · [GitHub: imend35](https://github.com/imend35)

## Disclaimer

Educational demonstration only. No hiring predictions, official ATS scoring, or automatic application submissions.
