# Six-question self-evaluation (course rubric)

Date: 2026-10-10. Status describes artifacts, not yet a completed controlled experiment.

| Question                                   | Current evidence                                                                                      | Status            |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------- | ----------------- |
| Is the task divided?                       | Four prompt files each cover one stage.                                                               | YES — designed    |
| Are two input types used?                  | Job/CV text and a CSV requirements table are prepared; CSV must still be supplied to actual LLM runs. | PENDING EXECUTION |
| Is supporting evidence requested?          | Source quotes and claim traceability fields exist in synthetic example outputs.                       | YES — in fixture  |
| Was it scored against predefined criteria? | K1–K4 frozen; historical retrospective review 3/4; controlled A/B scores not measured.                | PARTIAL           |
| Is there a human approval checkpoint?      | Demo QA keeps approval PENDING and submission_authorized=false.                                       | YES — in fixture  |
| Are three prompt library cards written?    | See `evaluation/PROMPT_LIBRARY_CARDS.md`.                                                             | YES — documented  |

## Remaining work

Execute both LLM variants with identical inputs, capture times and unedited results, score K1–K4, and update this report using observed outcomes. Static JSON validation is not equivalent to an LLM run.
