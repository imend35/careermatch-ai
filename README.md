# CareerMatch AI

### Evidence-Based Job Application Assistant

CareerMatch AI is a prompt-engineering project that explores how structured prompt chaining can support job requirement extraction, CV matching, application content generation, and quality validation.

The project emphasizes evidence-based reasoning, transparent evaluation, and human-in-the-loop approval.

## Project Overview

Job applicants often need to analyze job descriptions, compare requirements against their qualifications, tailor application documents, and verify the accuracy of AI-generated content.

CareerMatch AI addresses these tasks through a four-stage prompt workflow designed to reduce unsupported claims and improve the traceability of application recommendations.

## Four-Stage Prompt Chain

| Stage | Component                     | Purpose                                                                           |
| ----- | ----------------------------- | --------------------------------------------------------------------------------- |
| 1     | Job Requirement Extractor     | Extracts and classifies job requirements and responsibilities                     |
| 2     | CV & Skills Matcher           | Compares candidate qualifications with job requirements using documented evidence |
| 3     | Application Content Generator | Drafts tailored professional summaries, CV improvements, and cover letters        |
| 4     | Quality Validator             | Audits generated claims, checks consistency, and requires human approval          |

## Key Features

- Structured job requirement extraction
- Evidence-based CV and skills matching
- Explainable requirement alignment scoring
- ATS-oriented content recommendations
- Tailored cover letter drafting
- Evidence traceability and gap identification
- Independent quality validation
- Human-in-the-loop approval workflow
- Baseline versus prompt-chain evaluation

## Workflow

```text
Job Description
      |
      v
[1] Requirement Extraction
      |
      v
Structured Requirements
      |
      +---- Candidate CV
      |
      v
[2] CV & Skills Matching
      |
      v
Evidence-Based Matching Matrix
      |
      v
[3] Application Content Generation
      |
      v
Application Drafts
      |
      v
[4] Quality Validation
      |
      v
Human Review & Approval
```

## Project Structure

```text
careermatch-ai/
├── prompts/
├── sample_data/
├── outputs/
├── evaluation/
├── src/
├── README.md
├── requirements.txt
└── .gitignore
```

The folders will contain reusable prompt templates, synthetic candidate data, example outputs, evaluation reports, and validation scripts.

## Evaluation Approach

The project compares a single-prompt baseline with a four-stage prompt chain.

The evaluation focuses on four criteria:

1. Correct extraction of job requirements
2. Traceability of claims to supporting evidence
3. Separation of CV-documented and user-confirmed information
4. Quality validation and human approval safeguards

Initial artifact reviews have identified strengths and remaining limitations. A fully controlled, timed comparison between both methods has not yet been completed.

Any reported alignment score is an internal evidence-based metric, not an official ATS score or a prediction of hiring success.

## Privacy and Responsible AI

This public repository is intended to use synthetic candidate data.

The workflow is designed to:

- Avoid fabricating qualifications, achievements, and experience
- Distinguish documented evidence from user-confirmed information
- Identify unsupported or uncertain claims
- Prevent automatic job application submission
- Require explicit human approval before external use

No real candidate's private CV or personal contact information should be committed to this repository.

## Technology Stack

- Prompt Engineering
- Generative AI / Large Language Models
- Python
- JSON
- CSV
- Markdown
- Git and GitHub

## Current Status

**In development**

The four prompt stages have been designed and evaluated using a real job application scenario. Repository packaging, synthetic-data demonstrations, automated validation, and controlled A/B testing are being finalized.

## Future Improvements

- Automated prompt-chain orchestration
- Expanded test datasets
- Reproducible end-to-end evaluation
- Additional job description formats
- Enhanced evidence traceability
- Optional user interface

## Author

**Esila Nur Demirci**

GitHub: [imend35](https://github.com/imend35)

## Disclaimer

CareerMatch AI is an educational prompt-engineering project. Generated content requires human verification and must not be treated as an official hiring assessment or ATS result.
