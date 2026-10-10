# Three reusable prompt library cards

## Card 1 — Requirement Extractor

**Purpose:** Extract requirements and responsibilities without fabrication.
**Version/date:** 1.0 / 2026-10-10
**Variables:** `[JOB_DESCRIPTION_TEXT]`, `[REQUIREMENTS_CSV_TABLE]`

**Prompt:**

> From [JOB_DESCRIPTION_TEXT] extract each requirement and responsibility as separate numbered records. Compare each requirement with [REQUIREMENTS_CSV_TABLE]. Include the exact source quote and source section for every record. Do not invent priorities, requirements, or employer details. Flag disagreements between text and table as unresolved. Output structured JSON.

**Evaluation:** 9 distinct requirements, 7 responsibilities, each backed by a verbatim job-text quote; no invented conditions.

## Card 2 — Evidence-Based CV Matcher

**Purpose:** Match requirements only to verifiable candidate evidence.
**Version/date:** 1.0 / 2026-10-10
**Variables:** `[REQUIREMENTS_JSON]`, `[CANDIDATE_CV_TEXT]`, `[USER_CONFIRMATIONS]`

**Prompt:**

> Compare [REQUIREMENTS_JSON] with [CANDIDATE_CV_TEXT]. For each requirement assign MATCHED, PARTIALLY_MATCHED, NOT_MATCHED, or NOT_VERIFIABLE and include an exact CV quote or a dated item from [USER_CONFIRMATIONS]. Mark the source CV_DOCUMENTED, USER_CONFIRMED, or NOT_VERIFIABLE. Never convert an assumption into a confirmed fact. Compute a transparent 1/0.5/0 scoring percentage, explicitly not an ATS score. Output structured JSON.

**Evaluation:** Every requirement covered once, all CV quotes searchable in the supplied CV, no invented confirmation, correct arithmetic.

## Card 3 — Human Approval Quality Gate

**Purpose:** Validate drafted claims and block unauthorized external submission.
**Version/date:** 1.0 / 2026-10-10
**Variables:** `[APPLICATION_DRAFT_JSON]`, `[MATCHING_JSON]`, `[CANDIDATE_CV_TEXT]`, `[HUMAN_APPROVAL]`

**Prompt:**

> Independently audit each material claim in [APPLICATION_DRAFT_JSON] against [MATCHING_JSON] and [CANDIDATE_CV_TEXT]. List claim IDs, exact evidence, contradictions, missing citations, and required edits. If [HUMAN_APPROVAL] is absent or pending, set submission_authorized=false regardless of quality score. Do not send an application. Return a structured QA report.

**Evaluation:** All material claims checked, missing support flagged, approval state explicit, no automatic submission.
