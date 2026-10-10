# CareerMatch AI — Project Presentation

**Subtitle:** Evidence-Based Job Application Assistant

## 1. Problem

Tailoring a job application requires interpreting requirements, comparing them with verifiable CV evidence, drafting relevant material, and checking that no unsupported achievements are introduced. A single unstructured prompt can make this workflow difficult to audit.

## 2. Objective

Design a transparent four-stage prompt chain with explicit evidence traceability and a human-approval gate. Demonstrate the structure through fictional candidate/job inputs and repeatable static checks.

## 3. Solution Architecture

1. **Requirement Extraction:** Identify requirements and responsibilities with literal references to the job posting.
2. **CV Matching:** Classify evidence as CV-documented, user-confirmed, or unverifiable; produce a requirement-level matrix.
3. **Content Generation:** Draft a tailored professional summary, skills list, CV bullet recommendations, and cover letter with claim IDs.
4. **Quality Validation:** Check claim coverage and approval status; prohibit automatic external submission.

## 4. Example Data

The public demonstration uses a fully fictional Senior Business Analyst posting and a fictional candidate, Alex Morgan. The sample has nine requirements and seven responsibilities. Outputs are deliberately constructed JSON examples, not captured LLM responses.

## 5. Testing

The Python validator checks structural and literal-evidence consistency, score arithmetic, and the human-approval gate. The unittest suite includes a valid-case test and negative tests for fabricated evidence, incorrect scores, missing job references, and unauthorized submission.

**Run:**

```bash
python -m src.validate
python -m unittest discover -s tests -v
```

## 6. Evaluation and Findings

The prior private retrospective audit met **3/4** evaluation criteria, with claim-level evidence traceability identified as the gap. This is not a controlled A/B result.

The synthetic example shows **9/9 rubric matches (100%)** and an **illustrative QA score of 91/100**. These are example values, not external ATS scores or empirical LLM accuracy measurements.

A controlled comparison of a one-shot baseline and the four-stage chain, including execution time and manual correction effort, is **pending**.

## 7. Responsible AI

Synthetic public inputs protect candidate privacy. Source citations, explicit uncertainty, and human approval reduce the risk of fabricated qualifications or premature submission. Literal checks cannot substitute for human semantic review.

## 8. Next Steps

- Run controlled, logged LLM experiments with identical input pairs.
- Record model versions, timing, K1–K4 pass/fail judgments, and reviewer correction time.
- Expand synthetic fixtures and adversarial tests.
- Add optional orchestration and a user interface after validation.

## 9. Portfolio Links

**Repository:** https://github.com/imend35/careermatch-ai

**Author:** Esila Nur Demirci
