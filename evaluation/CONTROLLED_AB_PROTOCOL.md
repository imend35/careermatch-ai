# Controlled A/B protocol — pending execution

**Do not label this a completed experiment until both runs are executed and scored.**

## Inputs

1. `sample_data/sample_job_description.txt` — text
2. `sample_data/synthetic_candidate_cv.md` — text
3. `sample_data/requirements_table.csv` — a **separate tabular input** (CSV). The table is derived from the job ad; it is not a second independent source of facts.

## Fair comparison

- Use the same fixed input files and same LLM model/version/settings for A and B.
- A: use `evaluation/BASELINE_PROMPT.md` once; provide all three inputs.
- B: execute the four files in `prompts/` sequentially; pass stage outputs to the next stage. Provide the same source inputs, including CSV, to relevant stages. If a stage does not support CSV, record this limitation rather than claiming multimodal use.
- Capture unedited raw outputs, start/end times, model/version, temperature (if available), and correction time. No external job submission.
- Score each output with the same frozen rubric, preferably without revealing which method produced it to the reviewer.

## Binary scoring

- K1: All 9 requirements are present, no invented requirement.
- K2: Each match and material draft claim has a precise, verifiable source quote.
- K3: CV_DOCUMENTED, USER_CONFIRMED, and NOT_VERIFIABLE are differentiated; no unsupported confirmation.
- K4: QA is separately performed and submission is blocked pending human approval.

Pass = 1, fail = 0. Total 0–4. Record differences, omissions, runtime and human correction minutes. These metrics do not measure hiring probability or official ATS performance.

## Recording

Fill `evaluation/AB_RUN_LOG.csv`. Leave cells empty if not measured; never replace missing observations with estimates. Repeat with additional synthetic fixtures before generalizing.
