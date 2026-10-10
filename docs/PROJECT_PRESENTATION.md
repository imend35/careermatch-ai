# CareerMatch AI — Final Project Presentation

**Project:** Evidence-Based Job Application Assistant  
**Category:** Prompt Engineering · Generative AI · Responsible AI  
**Author:** Esila Nur Demirci  
**Date:** October 10, 2026  
**GitHub:** https://github.com/imend35/careermatch-ai

---

## 1. Problem Statement

AI-assisted job application tools can help candidates analyze job advertisements and prepare tailored application materials. However, they may introduce unsupported qualifications, overlook requirements, or produce content without adequate evidence verification.

These issues create risks involving hallucinations, inaccurate candidate representation, and limited transparency.

**The challenge:** How can we design a structured AI workflow that produces evidence-based job application materials while preserving traceability and human control?

## 2. Project Objectives

CareerMatch AI was developed to:

- Extract qualifications and responsibilities from job advertisements.
- Match requirements against documented CV evidence.
- Distinguish supported, partially supported, and unverifiable qualifications.
- Generate professional summaries, relevant skills, and cover letters.
- Audit material claims before human review.
- Prevent unauthorized application submission.
- Compare single-shot prompting with a multi-stage prompt chain.

The project uses fully synthetic candidate and job data.

## 3. Solution Architecture

CareerMatch AI implements a four-stage prompt chain.

### Stage 1 — Requirement Extraction

**Prompt:** `prompts/01_requirement_extractor.md`

Extracts job requirements and responsibilities with exact source quotations and stable identifiers.

**Recorded output:**

- 9 requirements
- 7 responsibilities
- Structured JSON with source references

### Stage 2 — Evidence-Based CV Matching

**Prompt:** `prompts/02_cv_matcher.md`

Matches extracted requirements against the synthetic candidate CV.

**Recorded output:**

- 8 fully matched requirements
- 1 partially matched requirement
- Evidence provenance classification
- Requirement-level matching matrix

The matching process distinguishes `CV_DOCUMENTED`, `USER_CONFIRMED`, and `NOT_VERIFIABLE` information.

No user-confirmed evidence was supplied in the recorded synthetic evaluation.

### Stage 3 — Application Drafting

**Prompt:** `prompts/03_application_drafter.md`

Produces:

- Tailored professional summary
- Relevant skills
- Short cover letter
- Supporting evidence references

The drafting process is restricted to supported candidate information.

### Stage 4 — Claim Audit and Human Approval

**Prompt:** `prompts/04_independent_auditor.md`

Reviews generated claims against the original synthetic sources and previous stage outputs.

**Recorded audit result:**

- Status: `PASS_WITH_NOTES`
- Internal checks: 10/10 passed
- Human approval: `PENDING_HUMAN_APPROVAL`
- Submission: Not authorized

This is a separate audit stage within the workflow, not verification by an external independent reviewer.

## 4. Prompt Engineering Techniques

The project demonstrates:

**Prompt Chaining:** Dividing a complex task into four specialized stages.

**Role-Based Prompting:** Assigning a defined analytical responsibility to each stage.

**Structured Output Design:** Using JSON contracts and stable identifiers.

**Evidence-Grounded Generation:** Linking extracted requirements and generated claims to source quotations.

**Hallucination Mitigation:** Preventing unsupported qualifications from being presented as documented facts.

**Prompt Injection Safeguards:** Treating job descriptions and CVs as untrusted input data.

**Human-in-the-Loop Governance:** Requiring explicit human approval before external application actions.

These techniques reduce selected workflow risks but do not guarantee error-free LLM behavior.

## 5. Experimental Design

Two approaches were evaluated using the same fictional Senior Business Analyst job scenario and synthetic candidate, Alex Morgan.

### Baseline A — Single-Shot Prompt

One prompt performs extraction, matching, drafting, and auditing in a single response.

### Chain B — Four-Stage Prompt Chain

Four specialized prompts produce separate intermediate artifacts.

**Evaluation date:** October 10, 2026

**Model information:** Baseline A explicitly recorded GPT-6. Chain B was conducted in a GPT-6 conversation, although per-stage model configuration was not separately captured.

The comparison is partially controlled because Baseline A received a requirements CSV directly, whereas Chain B initially extracted requirements from the job advertisement.

## 6. A/B Evaluation Results

| Evaluation Metric              | Baseline A      | Chain B        |
| ------------------------------ | --------------- | -------------- |
| Requirements extracted         | 9/9             | 9/9            |
| Responsibilities extracted     | 7/7             | 7/7            |
| Fully matched requirements     | 8               | 8              |
| Partially matched requirements | 1               | 1              |
| Evidence alignment             | 94.44%          | 94.44%         |
| K1–K4 evaluation checks        | 4/4 PASS        | 4/4 PASS       |
| Claim audit                    | Single response | Separate stage |
| Human approval                 | Not authorized  | Pending        |
| Execution time                 | Not captured    | Not captured   |
| Manual correction time         | Not measured    | Not measured   |

### Evidence Alignment Formula

```text
Alignment = ((8 × 1) + (1 × 0.5)) / 9 × 100
Alignment = 94.44%
```

This percentage is a custom evidence-alignment measure. It is not an official ATS score or a hiring probability.

### Evaluation Criteria

- **K1:** Extract all nine requirements and seven responsibilities.
- **K2:** Classify and match all nine requirements to CV evidence.
- **K3:** Produce application drafts without unsupported material claims.
- **K4:** Include claim auditing, provenance separation, missing information, and human approval controls.

Both approaches satisfied all four recorded output-level checks.

## 7. Key Findings

The evaluation produced three principal findings.

**Finding 1 — Equivalent Observed Matching Results**

Both approaches achieved 94.44% evidence alignment on the synthetic test scenario.

**Finding 2 — Improved Process Inspectability**

Chain B separates requirement extraction, CV matching, drafting, and auditing into distinct artifacts. This makes intermediate outputs easier to inspect and troubleshoot.

**Finding 3 — No Demonstrated Accuracy or Speed Advantage**

The available data does not establish that Chain B is more accurate, faster, or less labor-intensive than Baseline A.

Additional controlled experiments would be necessary to assess those claims.

## 8. Python Validation and Unit Testing

The repository includes a deterministic Python validator and a unit-test suite.

### Commands

```bash
python -m src.validate
python -m unittest discover -s tests -v
```

### Recorded Local Test Results

**Validation status:** PASS

| Validation Metric | Result |
| ----------------- | ------ |
| Requirements      | 9      |
| Responsibilities  | 7      |
| Matching rows     | 9      |
| Traceable claims  | 13     |
| Validation issues | 0      |

**Unit tests:** 5/5 passed

| Test                              | Result |
| --------------------------------- | ------ |
| Valid synthetic fixture           | PASS   |
| Fake CV evidence rejection        | PASS   |
| Missing job evidence rejection    | PASS   |
| Score mismatch rejection          | PASS   |
| Unauthorized submission rejection | PASS   |

Recorded unit-test runtime: **0.055 seconds**.

This is the runtime of the Python unit tests, not the LLM evaluation.

The static tests validate fixture consistency and selected safeguards. They do not independently measure semantic LLM accuracy.

## 9. Responsible AI and Privacy

CareerMatch AI applies several responsible AI principles.

**Evidence Integrity:** Candidate qualifications must be supported by documented evidence.

**Transparency:** Requirements, matches, and claims use traceable references.

**Uncertainty Management:** Missing or unverifiable information is explicitly identified.

**Privacy:** Public demonstrations use fictional candidate and employer information.

**Human Oversight:** Generated application materials require human review. No external application submission is implemented.

**Metric Integrity:** Internal alignment percentages are not presented as official ATS results.

## 10. Experimental Limitations

The current evaluation has important limitations:

1. One synthetic job/CV scenario.
2. One recorded run per approach.
3. No captured LLM execution timestamps or token costs.
4. No measured manual correction time.
5. Partially different informational inputs between approaches.
6. No independent blinded evaluation.
7. No statistical evidence supporting generalization.

The findings therefore support a descriptive comparison of workflow architectures.

## 11. Lessons Learned

This project reinforced the importance of:

- Designing clear input and output contracts.
- Separating complex LLM tasks into inspectable stages.
- Preserving source evidence throughout a workflow.
- Distinguishing static tests from empirical LLM evaluation.
- Using conservative matching classifications.
- Documenting experimental limitations.
- Keeping humans responsible for final application decisions.

## 12. Future Improvements

Potential next steps include:

- Automated execution of the four-stage prompt chain.
- JSON Schema validation for model-generated outputs.
- Additional synthetic evaluation scenarios.
- Repeated experiments with equivalent inputs.
- Token, latency, and manual-correction measurements.
- Blinded assessment of generated drafts.
- More comprehensive prompt-injection testing.
- A human-review interface for application materials.

These are planned improvements, not existing implemented features.

## 13. Conclusion

CareerMatch AI demonstrates an evidence-based approach to AI-assisted job application preparation.

The project successfully documents a four-stage prompt chain, structured evidence matching, application drafting, claim auditing, and human approval safeguards.

The recorded A/B evaluation found equivalent requirement alignment between single-shot and multi-stage prompting on one synthetic fixture.

The primary demonstrated benefit of Chain B is **modularity and inspectability**, rather than a measured improvement in accuracy or execution speed.

The project highlights how transparent evidence tracking, structured evaluation, and human oversight can support more responsible generative AI workflows.

---

**Repository:** https://github.com/imend35/careermatch-ai

**Author:** Esila Nur Demirci

_Educational portfolio project. Synthetic data only. No official ATS assessment or automatic application submission._
