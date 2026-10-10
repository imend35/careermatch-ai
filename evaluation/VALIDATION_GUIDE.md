# Validation Guide

Run from repository root using Python 3.10+:

```powershell
python -m src.validate
python -m unittest discover -s tests -v
```

The first command prints a JSON report and exits with code 0 when checks pass.
The second runs one valid-fixture test and four negative tests that intentionally inject defects into temporary copies.

No third-party packages or API keys are required. These are **static fixture checks**, not LLM runs. The public demo must keep `submission_authorized=false` and human approval `PENDING`.

## Scope

- 9 requirement IDs, 7 responsibility IDs, and their literal evidence in the sample posting
- CV evidence quotes appearing in the synthetic Markdown CV
- Requirement coverage, claim traceability references, and QA claim coverage
- Recomputed rubric score and official ATS score remaining null
- Human approval pending and external submission blocked

Literal substring checks are not semantic entailment checks. A human reviewer is still required.
