# Final Submission Checklist

## Repository

- [ ] `README.md` describes the project and includes reproducible commands.
- [ ] `prompts/` contains four stage prompts.
- [ ] `sample_data/` contains only fictional public demo inputs.
- [ ] `outputs/` contains four illustrative JSON outputs.
- [ ] `src/` and `tests/` are present.
- [ ] `evaluation/AB_TEST_RESULTS.md` clearly marks controlled A/B tests as pending.
- [ ] `docs/PROJECT_PRESENTATION.md` is included.

## Local verification

Run from repository root:

```powershell
python -m src.validate
python -m unittest discover -s tests -v
git status --short
```

- [ ] Validator reports `passed: true`.
- [ ] Five tests pass (`OK`).
- [ ] No private CV, email, telephone, secrets, or `.env` files are staged.
- [ ] `git diff --cached --name-only` shows only intended files.

## Claim accuracy

- [ ] Do not call the synthetic 100% alignment an official ATS score.
- [ ] Do not call the illustrative 91/100 QA value an independent audit.
- [ ] Do not describe the earlier retrospective 3/4 as controlled A/B results.
- [ ] Do not claim automated LLM orchestration or submission exists.
- [ ] Explicitly note controlled A/B measurement is pending.

## Course-specific completion (verify against assignment rubric)

- [ ] Four prompt stages and validation workflow demonstrated.
- [ ] Input modalities required by the course demonstrated, not merely stored as files.
- [ ] Required self-evaluation questions answered.
- [ ] Three reusable prompt library cards included if required.
- [ ] Timed baseline-versus-chain runs completed **if the course requires empirical A/B comparison**.
- [ ] Final submission format and deadline confirmed.

**Note:** A GitHub-ready portfolio package does not automatically mean all course grading criteria are complete.
