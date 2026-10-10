# Baseline A — Single-shot prompt

Version: 1.0 | Date: 2026-10-10

Use the _same_ job description and synthetic candidate CV used in Chain B. Also provide the requirement table CSV as a separate tabular input. Do not invent evidence or imply a real ATS assessment.

## Prompt (copy and paste)

You are an evidence-based job application analyst. Using ONLY the following three inputs, complete the entire task in ONE response:

[JOB_DESCRIPTION_TEXT]

[CANDIDATE_CV_TEXT]

[REQUIREMENTS_CSV_TABLE]

Tasks: (1) extract all requirements and responsibilities with source quotes, (2) match each requirement to specific CV quotes and label it MATCHED, PARTIALLY_MATCHED, NOT_MATCHED, or NOT_VERIFIABLE, (3) draft a professional summary, relevant skills and a short cover letter, (4) independently audit all material claims and require human approval before any submission. Separate CV_DOCUMENTED from USER_CONFIRMED and NOT_VERIFIABLE. Never assume user confirmation when none is provided. Score each requirement as 1, 0.5, 0, or 0 respectively; report alignment as a rubric percentage, not an ATS score. Provide the four binary evaluation checks K1–K4 with supporting evidence. Return a clear structured answer and identify missing information. Do not submit any application.

## Measurement

Record the model/version/settings, run date, start/end times, manual correction minutes, and K1–K4 decisions in `AB_RUN_LOG.csv`. Save the full unedited output privately or publish only synthetic content.
