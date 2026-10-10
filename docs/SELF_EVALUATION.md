# CareerMatch AI — Final Project Self-Evaluation

**Course:** Prompt Engineering 2.0 (Multimodal)  
**Project:** CareerMatch AI  
**Evaluation Date:** October 10, 2026

## 1. Is the task divided into clear steps?

**Status: PASS**

The workflow consists of four specialized stages:

1. Job Requirement Extraction
2. Evidence-Based CV Matching
3. Application Drafting
4. Independent Claim Audit and Human Approval

Each stage has a defined responsibility, input, output, and validation objective.

## 2. Are at least two input types used?

**Status: PARTIALLY DEMONSTRATED**

The project uses textual job descriptions and candidate CVs, together with a structured CSV requirements table in the Baseline A evaluation.

However, the current Chain B demonstration does not yet establish that the CSV was independently processed as a second input modality within the four-stage workflow.

An additional demonstration should explicitly combine textual and tabular inputs and preserve their separate evidence references.

## 3. Is every output supported by evidence?

**Status: PASS — Within Recorded Validation Scope**

Requirements are linked to original job advertisement quotations.

Candidate matches and application claims are linked to synthetic CV evidence.

The project distinguishes documented evidence, user-confirmed evidence, and unverifiable information.

Static validation and the recorded Stage 4 audit support internal traceability, without establishing external verification of fictional credentials.

## 4. Were results measured against predefined criteria?

**Status: PARTIAL**

The project compares Baseline A and Chain B using four evaluation criteria (K1–K4).

Both approaches achieved 4/4 recorded output-level checks and 94.44% evidence alignment.

However, Chain B criteria were mapped retrospectively to its artifacts, and the informational inputs were not perfectly equivalent.

A future experiment should apply the same predefined criteria and equivalent inputs before execution.

## 5. Is there a human approval checkpoint?

**Status: PASS**

All generated application materials require human review.

The Stage 4 audit records `PENDING_HUMAN_APPROVAL`.

No external application submission is implemented or authorized.

## 6. Were the three best prompts converted into reusable library cards?

**Status: PENDING**

Three reusable prompt library cards will be prepared with the required fields:

- Name
- Purpose
- Bracketed variables
- Prompt
- Control criteria

Each card will include a version and revision date.

## Summary

| Criterion                  | Result                 |
| -------------------------- | ---------------------- |
| Task decomposition         | PASS                   |
| Two input types            | PARTIALLY DEMONSTRATED |
| Evidence traceability      | PASS                   |
| Criteria-based evaluation  | PARTIAL                |
| Human approval             | PASS                   |
| Three prompt library cards | PENDING                |

## Conclusion

CareerMatch AI demonstrates a functional four-stage prompt-chain design, evidence-based application drafting, internal validation, and human oversight.

Before final course submission, the project should strengthen the explicit two-input-type demonstration, complete the three reusable prompt cards, and document the limitations of the partially controlled A/B comparison.

The recorded results do not establish an accuracy or speed advantage for Chain B.
