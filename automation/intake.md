# Community sample intake automation

## Goal

Turn "what new tic is the community complaining about" from ad-hoc manual word-collecting into a stable intake process:

- First judge whether it's already covered by existing rules
- Then distinguish "variant of an existing pattern" from "genuinely new pattern"
- Finally output suggestions only, don't auto-edit the repo

The goal of this automation is not to expand the word table directly, but to cut the maintainer's screening cost.

## Recommended input

Each run takes a batch of community samples; sources may be mixed:

- Meme screenshots
- Chat screenshots
- Text excerpts
- Examples pasted in issues / comments

Input should carry minimal context:

- Source platform
- Original or OCR text
- One line: why it looks AI-flavored

## Automation flow

### 1. Extract samples

- OCR from screenshots, keeping the original sentence where possible
- Drop irrelevant UI text, keep only candidate sentences
- Deduplicate words repeated within one image

### 2. Merge into existing problem families

For each sample, prefer an existing pattern (with `references/operation-manual.md` and `references/phrases-de.md` categories as authority, listing the main families by frequency):

- engineer-speak / debug-speak
- business jargon
- quack-doctor probing
- violence-speak
- proactive pushiness
- summary-cue speak
- summary ending
- over-catching / psych-judgment speak
- solemn preview / identity-certification praise
- narrator voice
- influencer / clickbait voice
- transition filler
- binary-contrast sentence
- value-inflation skeleton
- register mixing
- unsourced citation
- Nominalstil overload (German-specific)
- other structural anti-patterns (see `references/structures.md`, 21 classes)

If it classifies cleanly, don't rush to suggest a new word. **Missing a covered family wrongly pushes a covered sample into "candidate new pattern" and breaks the "covered → no action" boundary** — when unsure, go back and compare against the family numbers in `operation-manual.md` rather than dumping it in "other".

### 3. Output a three-tier conclusion

Each sample lands exactly one conclusion:

- `covered`
  - The word table or structure table already has a representative item
  - No action needed
- `variant merge`
  - Not listed verbatim, but an existing pattern already absorbs it
  - Suggest a benchmark or operation-manual note, not a new word
- `candidate new pattern`
  - No existing pattern explains it
  - Or it clearly changes the false-positive boundary
  - Only then suggest a human review for whether to add it

### 4. Generate suggestions, don't write the repo directly

Each run outputs an intake report, always containing:

- `Sample count this round`
- `Covered`
- `Variant merge`
- `Candidate new pattern`
- `Suggested action`

`Suggested action` allows only these 4:

- `no action`
- `add benchmark`
- `add operation-manual`
- `consider adding a word or structure`

### 5. Land in the repo only after human confirmation

Only after human confirmation do you take follow-up actions:

- Update `evals/benchmark.md`
- Update `references/operation-manual.md`
- For a new structural pattern, update `references/structures.md`
- Update `references/phrases-de.md` only when necessary

By default, don't let the automation edit these files directly.

## Recommended output format

The report must contain 6 sections: `Sample count this round` / `Covered` / `Variant merge` / `Candidate new pattern` / `Suggested action` / `One-line verdict`. This format is pinned by the hard constraints in `intake-prompt.md`; the run entry and changelog are validated against it.

```md
# Weekly community-tic intake

Sample count this round: 3

## Covered
- "festnageln" → violence-speak, already in the table; action: no action

## Variant merge
- "freilegen" → quack-doctor-probing variant, suggest add benchmark
- "rausziehen" → quack-doctor-probing variant, suggest add operation-manual example

## Candidate new pattern
- none

## Suggested action
- no action: 1
- add 1 SF benchmark
- update the operation-manual variant-merge note

Verdict: no new word needed this round, existing patterns absorb it.
```

## Scheduling

- Frequency: once a week is enough
- Trigger: run at a fixed time, or after the maintainer feeds in a batch
- Output location: open an inbox item rather than editing files directly

## Don't do

- Don't auto-append every new word to the table
- Don't derive "must add a rule" from a single meme
- Don't skip the false-positive check
- Don't let the automation auto-open a PR

## If you later wire it into Codex automation

The automation prompt should do intake only, no repo writes. Core requirements:

- First read `SKILL.md`, `references/phrases-de.md`, `references/structures.md`, `references/operation-manual.md`
- Classify input samples into "covered / variant merge / candidate new pattern"
- Output the suggested action and reasoning
- Don't modify repo files unless the user explicitly asks

A reusable prompt template is in `./intake-prompt.md`; the run entry is in `./README.md`.
