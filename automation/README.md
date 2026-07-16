# Community Sample Intake — run guide

> Entry point for the maintainer's local tool.
> The protocol spec (what intake is, why) is in `./intake.md`; the prompt itself is in `./intake-prompt.md`.
> This README only covers "how to run one round".

## When to run

- Public discussion (heise, Reddit, Hacker News, ComputerBase, X, etc.) surfaces a batch of new AI posture chains
- You suspect existing tables might not catch it, but aren't sure if it's a variant or a new pattern
- The full trigger set is in `CONTRIBUTING.md`, section "Maintainer: Community Observation Intake"

## File convention

Tool itself (committed):

| Role | Path |
|------|------|
| Protocol spec | `automation/intake.md` |
| The prompt | `automation/intake-prompt.md` |
| Run guide | `automation/README.md` (this file) |

Run instances (local-only, `tasks/` is in `.gitignore`):

| Role | Path |
|------|------|
| Input (this round's batch) | `tasks/current/intake/inbox/<YYYY-MM-DD>.md` |
| Output (this round's report) | `tasks/current/intake/reports/<YYYY-MM-DD>-intake.md` |

Each input sample carries three columns "source / original text / submitter note"; the closer to the raw observation, the better.

## One command

Run in the repo root (replace the date):

```bash
codex exec -C . -s read-only --ephemeral \
  -o tasks/current/intake/reports/2026-05-01-intake.md \
  'You are running the klartext repo intake automation.

Read ./automation/intake-prompt.md in full and act on the prompt in its text code block. That prompt is fixed: which references to read first, how to classify into "covered / variant merge / candidate new pattern", the hard constraints (don''t suggest adding a word by default; don''t misjudge a discussed word, a quoted word, or a real person''s concrete narrative as AI-speak), and the final output format.

This round''s batch is in ./tasks/current/intake/inbox/2026-05-01.md.

Output the final intake report directly, in the prompt''s recommended format (sample count / covered / variant merge / candidate new pattern / suggested action / one-line verdict), with no process narration or meta commentary.'
```

Key flags:

- `-C .` — makes codex use the repo root as the working directory so the relative paths resolve
- `-s read-only` — locks the sandbox read-only, a second backstop for "don't auto-edit the repo"
- `--ephemeral` — no persistent session, run-and-discard
- `-o <report path>` — writes the model's final output straight to the reports dir, no stdout copy-paste

> `tasks/current/intake/inbox/` and `reports/` are in `.gitignore`; `mkdir -p` them once before first use.

## After the run

The report contains only four kinds of suggested action: `no action / add benchmark / add operation-manual / consider adding a word or structure`.

- Default assumption: this round does **not** need a direct repo change
- If the suggestion is `add benchmark`: assess manually, then edit `evals/benchmark.md`
- If the suggestion is `add operation-manual`: assess manually, then edit `references/operation-manual.md`
- If the suggestion is `consider adding a word or structure`: watch 2–3 rounds first, confirm it recurs, then consider adding it
- No action should be done **automatically** by intake; this layer is a suggestion, not a landing

## If the prompt breaks

If a change to `intake-prompt.md` makes the report drift from the spec format (missing sections, messy family classification, a discussed word misjudged as AI-speak), the prompt is broken — roll back or recalibrate. For calibration, prepare a synthetic batch covering the three-tier conclusions + two trap types (discussed word, technical-context pass) as an expected baseline, then run and compare.
