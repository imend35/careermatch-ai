# CareerMatch AI — Final Project Self-Evaluation

**Course:** Prompt Engineering 2.0 (Multimodal)  
**Project:** CareerMatch AI  
**Version:** 1.1  
**Evaluation Date:** October 10, 2026

## 1. Is the task divided into clear steps?

**Status: PASS**

The workflow contains four specialized stages:

1. Job Requirement Extraction
2. Evidence-Based CV Matching
3. Application Drafting
4. Independent Claim Audit and Human Approval

Each stage has a defined purpose, inputs, outputs, and validation criteria.

## 2. Are at least two input types used?

**Status: PASS FOR SUPPLEMENTARY STAGE 2 DEMONSTRATION**

The project uses unstructured text and a structured CSV table.

The supplementary Stage 2 execution processed:

- Synthetic candidate CV (Markdown text)
- Requirements table (CSV)
- Original job description (plain text)

The recorded execution evaluated nine CSV requirements and produced evidence-based matching results.

A separate deterministic validation also confirmed consistency between the CSV, original job description, and existing Stage 1 extraction.

**Limitation:** The supplementary test establishes text-and-table processing at Stage 2. A complete new four-stage LLM run using both formats has not been recorded.

**Evidence:**

- `tests/multimodal/MULTIMODAL_TEST_REPORT.md`
- `tests/multimodal/STAGE2_TEXT_CSV_OUTPUT.json`
- `tests/multimodal/STAGE2_TEXT_CSV_TEST_REPORT.md`

## 3. Is every output supported by evidence?

**Status: PASS — WITHIN RECORDED VALIDATION SCOPE**

Job requirements retain source quotations from the original fictional advertisement.

Candidate matches reference exact quotations from the synthetic CV.

The workflow distinguishes `CV_DOCUMENTED`, `USER_CONFIRMED`, and `NOT_VERIFIABLE` information.

The recorded audit and validation support internal traceability, but do not constitute independent verification of candidate credentials.

## 4. Were results measured against predefined criteria?

**Status: PARTIAL**

The project documents K1–K4 evaluation criteria and records results for Baseline A and Chain B.

Both original approaches achieved:

- 4/4 recorded output-level checks
- 94.44% custom evidence alignment

The supplementary text-and-CSV Stage 2 execution reported:

- 9 evaluated requirements
- 7 full matches
- 2 partial matches
- 88.89% custom evidence alignment

The supplementary result was not a controlled comparison with the original Chain B run.

The original A/B comparison also has limitations: some criteria were mapped retrospectively, input conditions were not perfectly equivalent, and execution time was not recorded.

No accuracy, speed, or cost superiority is claimed.

## 5. Is there a human approval checkpoint?

**Status: PASS**

The independent auditor requires explicit human review before any external application action.

The recorded approval status remains:

`PENDING_HUMAN_APPROVAL`

No external application was submitted.

## 6. Were three reusable prompt library cards created?

**Status: PASS**

Three reusable cards are documented in:

`docs/PROMPT_LIBRARY_CARDS.md`

The cards cover:

1. Evidence-Based Job Requirement Extractor
2. Evidence-Based CV and Skills Matcher
3. Independent Claim Auditor and Human Approval Gate

Each card includes its name, purpose, bracketed variables, reusable prompt, validation criteria, version, and source reference.

## Summary

| Criterion | Status |
|---|---|
| Task decomposition | PASS |
| Two input types | PASS — Supplementary Stage 2 |
| Evidence traceability | PASS — Recorded scope |
| Criteria-based evaluation | PARTIAL |
| Human approval | PASS |
| Three prompt library cards | PASS |

## Remaining Limitations

- The original A/B comparison is only partially controlled.
- Only one supplementary text-and-CSV LLM execution is documented.
- Model-reported checks do not replace independent verification.
- A complete new four-stage text-and-table execution has not been recorded.
- Execution latency and token costs were not measured.
- The project uses synthetic public demonstration data.
- The recurring weekly use case should be explicitly documented and evidenced.

## Conclusion

CareerMatch AI demonstrates a four-stage prompt-chain design, source-based matching, structured output validation, reusable prompt cards, and human approval safeguards.

The supplementary Stage 2 execution adds recorded evidence of text-and-table processing.

The project meets five self-evaluation criteria within their stated scopes. The criteria-based comparison remains partial because the original A/B evaluation was not fully controlled.

All alignment percentages are internal demonstration metrics, not official ATS scores or hiring probabilities.