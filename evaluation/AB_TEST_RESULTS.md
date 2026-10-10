# Evaluation and A/B Test Status

## Evaluation design

**Baseline A:** one-shot prompt receiving the same job description and candidate CV.
**Chain B:** four prompts (requirements → CV matching → application drafting → QA).

Predefined binary checks:

| ID  | Pass condition                                                                               |
| --- | -------------------------------------------------------------------------------------------- |
| K1  | All nine job requirements extracted without fabricated requirements                          |
| K2  | Each requirement match and material draft claim has a specific verifiable evidence reference |
| K3  | CV-documented, user-confirmed, and unverifiable evidence clearly separated                   |
| K4  | Independent QA stage and no external submission before human approval                        |

## Historical retrospective review (real-candidate experiment)

A previous artifact review reported **3/4 checks passed**; K2 failed because some generated claims lacked precise source references. This result relates to earlier private artifacts **not included in this public repository**. It is **not** a controlled A/B outcome and should not be conflated with the synthetic fixture.

## Synthetic demo

The public JSON files in `outputs/` are **illustrative, programmatically assembled fixtures**, not independently sampled model outputs. The synthetic example reports 100% rubric alignment (9/9), which is **not an ATS score** and does not establish model accuracy. QA's 91/100 is an illustrative manual rubric value, not an independent audit.

Run `python -m src.validate` and `python -m unittest discover -s tests -v` to validate fixture consistency and rejection of intentionally corrupted fixtures.

## Controlled A/B test: NOT YET RUN

| Measure                    | Baseline A   | Chain B      |
| -------------------------- | ------------ | ------------ |
| Same fixed inputs          | Pending      | Pending      |
| K1–K4 pass count           | Not measured | Not measured |
| Wall-clock time            | Not measured | Not measured |
| Human correction time      | Not measured | Not measured |
| Model / version / settings | Not recorded | Not recorded |

**Protocol:** Freeze one identical input pair, use the same model/version/settings, execute A and B independently, timestamp start/end, have a reviewer score K1–K4 blind where practical, log manual edits, and publish raw redacted outputs. Repeat across multiple fixtures before making comparative claims.

## Limits

Static tests verify JSON structure, evidence substring references, scoring arithmetic, and approval gating. They **cannot** determine semantic truth, hiring suitability, real ATS compatibility, or LLM reliability.
