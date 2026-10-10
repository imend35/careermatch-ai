# CareerMatch AI — Controlled A/B Comparison (Provisional)

**Date:** 2026-10-10  
**Fixture:** Fictional Senior Business Analyst job posting and Alex Morgan synthetic CV  
**Models:** Baseline A explicitly records GPT-6. Chain B was conducted in this GPT-6 conversation, but per-stage model configuration was not separately captured.  
**Scope:** One recorded Baseline A run and one recorded Chain B sequence; no repetitions or timing measurements.

## Common evaluation criteria

- **K1:** Nine job requirements and seven responsibilities extracted.
- **K2:** Nine requirements classified and linked to CV evidence.
- **K3:** Professional summary, relevant skills, and cover letter generated without unsupported material claims.
- **K4:** Claim audit, provenance, missing information, and human-approval gate included.

Baseline A defines these operationally in its submitted report. For Chain B, the same criteria are **mapped retrospectively** to its stage artifacts, not claimed to have been independently pre-registered.

| Metric                     | Baseline A                       | Chain B                                         | Interpretation                                            |
| -------------------------- | -------------------------------- | ----------------------------------------------- | --------------------------------------------------------- |
| Requirements extracted     | 9/9                              | 9/9                                             | Tie                                                       |
| Responsibilities extracted | 7/7                              | 7/7                                             | Tie                                                       |
| Requirement matches        | 8 full, 1 partial                | 8 full, 1 partial                               | Tie                                                       |
| Evidence-alignment score   | 94.44%                           | 94.44%\*                                        | Tie                                                       |
| K1–K4                      | 4/4 PASS (reported)              | 4/4 PASS (mapped from artifacts)                | Tie on output checks                                      |
| CV provenance              | CV_DOCUMENTED; no USER_CONFIRMED | CV_DOCUMENTED; no USER_CONFIRMED                | Tie                                                       |
| Claim audit                | Within one response              | Separate Stage 4 output (10/10 internal checks) | Architectural difference, not proven accuracy improvement |
| Human approval             | NOT AUTHORIZED                   | PENDING; no submission                          | Tie on gate                                               |
| Start/end time             | Not captured                     | Not captured                                    | Cannot compare speed                                      |
| Manual correction time     | Not measured                     | Not measured                                    | Cannot compare effort                                     |

\*Chain B alignment = (8 × 1 + 1 × 0.5) / 9 × 100 = 94.44%, using the same scoring rule as Baseline A. This is a **custom evidence-alignment metric**, not an ATS or hiring score.

## Findings

Both approaches achieve the same observed coverage and matching results on this single synthetic fixture. The multi-stage Chain B process produces distinct extraction, matching, drafting, and audit artifacts, making the workflow easier to inspect and troubleshoot stage by stage. However, the available evidence does **not** establish that Chain B is more accurate, faster, or less labor-intensive. Baseline A also performed a claim-level audit and explicitly withheld submission authorization; it must not be characterized as lacking these safeguards.

Chain B Stage 4 reports **PASS_WITH_NOTES**, with ten internal consistency checks passed. This is not external validation of fictional employment claims, nor proof of independent evaluation by a different model or reviewer.

## Validity limitations

1. One test case and one run per approach: insufficient for statistical inference or generalization.
2. No captured latency, token cost, manual-correction duration, or repeated-run variability.
3. Baseline A used the supplied requirements CSV, while the Stage 1 Chain B extractor used the job description; thus the information supplied at each step is not perfectly identical. The overall task fixture is the same, but this is a **partially controlled** comparison, not a rigorously input-equivalent experiment.
4. Baseline A checks were reported in its output; Chain B checks were inferred from saved stage artifacts. These are not independently blinded ratings.
5. Some output labels such as PASS are internal assertions. The recorded checks and artifacts support a descriptive comparison, not a universal reliability claim.
6. All candidate and employer data are fictional; human approval remains absent and no application was sent.

## Self-evaluation

**What worked:** Clear source evidence, conservative partial-match handling for REQ-008, explicit CV_DOCUMENTED provenance, separate audit records, and an enforced human-approval boundary.

**What should improve:** Predefine a common scoring rubric before running both conditions; use strictly identical informational inputs; log start/end times, token use, and manual corrections; run multiple synthetic job/CV cases with blinded scoring; add negative tests for unsupported skills, missing data, and prompt injection.

**Conclusion:** Chain B offers stronger _process modularity and inspectability_, while measured output quality is tied with Baseline A on this fixture. No demonstrated accuracy or speed advantage can be claimed.

## Source artifacts

- `AB_RUN_LOG(2).csv` and supplied Baseline A full report (`Yapıştırılan markdown(8).md`)
- `chain_b_stage1_output.json` through `chain_b_stage4_audit.json`
- Stage 1–4 validation notes
