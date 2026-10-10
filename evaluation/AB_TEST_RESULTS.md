# CareerMatch AI — Baseline A: Single-Shot Evaluation

Baseline A · Version 1.0

Run date: October 10, 2026 Evaluation type: Single-shot, evidence-based analysis Model: OpenAI GPT-6 Candidate: Alex Morgan (synthetic) Position: Senior Business Analyst — Example Enterprise Solutions (fictional)

This evaluation uses only the three supplied inputs: the fictional job description, synthetic candidate CV, and nine-row requirements CSV. It is a controlled demonstration, not a real ATS assessment, employment recommendation, or job application.

## 1. Requirement extraction and evidence matching

The job description contains nine explicit requirements (REQ-001–REQ-009) and seven responsibilities. The CSV contains the same nine requirements.

### Requirement-by-requirement assessment

| ID      | Requirement and source evidence                                                 | CV evidence                                                                                      | Classification    | Score |
| ------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ----------------- | ----- |
| REQ-001 | “University degree in a relevant field.”                                        | “BSc, Computer Science”                                                                          | MATCHED           | 1     |
| REQ-002 | “Experience in business analysis, process analysis, and process modeling.”      | “Modeled as-is and to-be processes using BPMN” and requirements workshops                        | MATCHED           | 1     |
| REQ-003 | “Knowledge and hands-on experience in SQL and data analysis.”                   | “Used SQL queries to validate data flows and prepare operational reports.”                       | MATCHED           | 1     |
| REQ-004 | “Proficiency in functional analysis, requirements analysis, and documentation.” | “documented functional and non-functional requirements” and “Produced functional specifications” | MATCHED           | 1     |
| REQ-005 | “Ability to prepare user stories, use cases, and flow diagrams.”                | “wrote user stories, use cases” and “process diagrams”                                           | MATCHED           | 1     |
| REQ-006 | “Knowledge of software development lifecycle and Agile methodologies.”          | “Agile/Scrum, SDLC” and two Scrum teams                                                          | MATCHED           | 1     |
| REQ-007 | “Experience in system integrations and integration scenarios.”                  | “Analyzed REST API and web-service integration scenarios”                                        | MATCHED           | 1     |
| REQ-008 | “Interest in artificial intelligence and current technology trends.”            | “evaluated potential AI-assisted workflow improvements” and AI workflow prototype                | PARTIALLY_MATCHED | 0.5   |
| REQ-009 | “Strong analytical thinking, problem-solving, and communication skills.”        | “analytical problem-solving, cross-functional communication” and stakeholder meetings            | MATCHED           | 1     |

For REQ-008, the CV documents interest and practical exploration of AI, but does not independently establish ongoing monitoring of current technology trends. The conservative classification is therefore PARTIALLY_MATCHED.

Evidence provenance: All nine assessments are based on `CV_DOCUMENTED` material from the synthetic CV. No `USER_CONFIRMED` evidence was supplied. External verification of the fictional claims is not available.

## 2. Rubric alignment calculation

Requirement alignment

# 94.44%

8.5 / 9 points

&#x20;8 matched

&#x20;1 partially matched

0 unmatched

Calculation:

\\[ \frac{8(1)+1(0.5)}{9}\times100=94.44\\% \\]

This is a custom evidence-alignment rubric, not an ATS score or an estimate of interview or hiring probability.

## 3. Responsibility coverage

The seven responsibilities are assessed separately and do not alter the nine-requirement score.

| Responsibility (job description quote)                                                            | CV evidence                                                                    | Assessment        |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ----------------- |
| “Analyze current and target business processes and define functional and technical requirements.” | As-is/to-be BPMN modeling; functional and non-functional requirements          | PARTIALLY_MATCHED |
| “Recommend product and process improvements, including responsible use of AI tools.”              | AI-assisted workflow improvements evaluated; prototype includes human review   | PARTIALLY_MATCHED |
| “Prepare clear analysis and design documentation for development teams.”                          | Functional specifications, process diagrams, user stories                      | MATCHED           |
| “Support functional testing, coordinate UAT, and report results.”                                 | Coordinated SIT/UAT and defect tracking; UAT plans                             | PARTIALLY_MATCHED |
| “Perform SQL and data analysis to support business reporting.”                                    | SQL validation, operational reports, data-quality analysis                     | MATCHED           |
| “Follow applicable privacy, information-security, workplace-safety, and quality requirements.”    | No explicit evidence of compliance with all four areas                         | NOT_VERIFIABLE    |
| “Monitor relevant AI tools and identify potential efficiency improvements.”                       | Evaluated potential AI-assisted improvements; no documented ongoing monitoring | PARTIALLY_MATCHED |

The partial classifications distinguish directly documented experience from aspects that the CV does not establish, such as formal technical-requirements ownership, AI governance practices, testing-results reporting, or ongoing tool monitoring.

## 4. Application content drafts

All drafts below are based on synthetic CV evidence. They are intended for human review, not automatic submission.

### Professional summary

Senior Business Analyst with 10 years of experience across financial services, telecommunications, and cloud software environments. Skilled in business process analysis, BPMN, requirements elicitation, functional documentation, SQL, Agile/Scrum delivery, system integrations, and UAT. Experienced in collaborating with cross-functional teams, translating business needs into actionable specifications, and supporting data-driven operational improvements. Interested in responsible AI-assisted workflow optimization and practical applications of emerging technologies.

### Relevant skills

Business Analysis: Requirements Elicitation, Functional Analysis, BRD/FRD, BPMN, Process Mapping, Gap Analysis, User Stories, Use Cases, Acceptance Criteria.

Technical & Data: SQL, PostgreSQL, REST APIs, Web Services, Data Validation, System Integration Testing, Power BI.

Delivery & Collaboration: Agile/Scrum, SDLC, UAT, Stakeholder Workshops, Backlog Refinement, Jira, Confluence.

AI: AI-Assisted Workflow Evaluation, Human-in-the-Loop Workflow Prototyping.

### Short cover letter

Dear Hiring Manager,

I am interested in the Senior Business Analyst position at Example Enterprise Solutions.

My background includes 10 years of experience in business analysis across financial services, telecommunications, and cloud software. I have worked on requirements elicitation, BPMN process modeling, functional documentation, SQL-based data analysis, system integrations, and Agile delivery.

In my previous roles, I collaborated with cross-functional teams, prepared user stories and use cases, and coordinated system integration and user acceptance testing. I have also explored AI-assisted workflow improvements, including a demonstration prototype designed to support human review.

I would welcome the opportunity to discuss how my experience aligns with your team's requirements.

Kind regards,

Alex Morgan

## 5. Independent claim audit

This is a separate claim-level review of the drafted content against the supplied CV, not independent verification of the fictional employment history.

| Material claim                                         | Provenance     | Audit result |
| ------------------------------------------------------ | -------------- | ------------ |
| 10 years of business analysis experience               | CV_DOCUMENTED  | Supported    |
| Financial services, telecommunications, cloud software | CV_DOCUMENTED  | Supported    |
| BPMN, requirements, Agile/Scrum, SQL                   | CV_DOCUMENTED  | Supported    |
| REST API integration and UAT coordination              | CV_DOCUMENTED  | Supported    |
| AI-assisted workflow evaluation                        | CV_DOCUMENTED  | Supported    |
| Human-review AI prototype                              | CV_DOCUMENTED  | Supported    |
| Current AI tools monitored continuously                | NOT_VERIFIABLE | Not claimed  |
| Regulatory compliance expertise                        | NOT_VERIFIABLE | Not claimed  |
| User approval of application materials                 | NOT_VERIFIABLE | Not granted  |

Audit conclusion: No unsupported material achievement, certification, quantified improvement, or employer was introduced in the drafts. The fictional CV is the sole source of the candidate's experience claims.

## 6. Binary evaluation checks K1–K4

The supplied Baseline A prompt requests K1–K4 but does not define their precise acceptance criteria. The following are operational definitions for this run; they must be reconciled with the Chain B rubric before the A/B comparison.

| Check | Operational definition                                                                      | Result |
| ----- | ------------------------------------------------------------------------------------------- | ------ |
| K1    | All nine requirements and seven responsibilities extracted                                  | PASS   |
| K2    | All nine requirements matched to CV evidence, classified, and scored                        | PASS   |
| K3    | Professional summary, skills, and cover letter produced without unsupported material claims | PASS   |
| K4    | Claim audit, provenance separation, missing information, and human approval gate included   | PASS   |

These are output-level checks, not proof that the candidate's fictional credentials are independently verified.

## 7. Missing information and human approval gate

The following remain unverified or incomplete:

- No explicit user confirmation of any CV claim.
- No documented evidence of all privacy, information-security, workplace-safety, and quality compliance requirements.
- No documented ongoing monitoring of current AI tools.
- No complete evidence of formal AI governance, UAT results reporting, or technical-requirements ownership.
- No human approval for application submission.
- No actual start/end timestamps or manual correction duration captured for the evaluation.

Submission status: NOT AUTHORIZED

Human approval is required before any external application action. No application has been submitted.

## 8. A/B run measurement log

The CSV log has been prepared with the model identification, run date, K1–K4 decisions, and explicit placeholders for unavailable measurement fields.

AB_RUN_LOG.csv

Baseline A · One recorded run

&#x20;Copy values

Download AB_RUN_LOG.csv

Measurement limitation: Exact generation start/end times and manual correction minutes were not captured. The model's configurable settings were not exposed. These fields have not been fabricated.

## 9. Baseline A conclusion

Rubric alignment

# 94.44%

Output checks

# 4 / 4

Requirements assessed

## 9 / 9

Responsibilities assessed

## 7 / 7

The single-shot baseline produced a structured, evidence-grounded analysis, application drafts, and an explicit human approval gate.

A/B comparison caution: This output should be preserved unedited as the Baseline A artifact. Any later human corrections, timing measurements, or rubric changes should be recorded separately so that Chain B can be compared fairly against the same inputs and evaluation criteria.
