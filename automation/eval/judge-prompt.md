# Benchmark Judge Prompt

Use the prompt below directly for cross-scoring. It only judges the model-under-test output by `evals/run-eval.md`; it does not rewrite.

```text
You are cross-scoring the klartext benchmark. Read the benchmark cases and the model-under-test output, and judge each result by the existing standard in ./evals/run-eval.md.

Path boundary:
- Use only `./evals/`, `./SKILL.md`, `./references/`, and the model-under-test output file in the current working directory.
- Do not read or reference a globally installed copy such as `~/.codex/skills/klartext`, `~/.claude/skills/klartext`, or any path outside the repo.
- If a global skill is auto-triggered, treat it as environment noise; this run's standard is the current working-directory files.

Read first:
- ./evals/run-eval.md
- ./evals/benchmark.md
- ./evals/benchmark-map.md

The model-under-test titles are blind IDs (B-xx). Before scoring, map each blind ID back to the benchmark.md case ID (SF-xx / SNF-xx) via ./evals/benchmark-map.md, then score by that case's `**Expected**` / `**Reason**`; use the mapped case ID in the output table.

Read as needed:
- ./SKILL.md
- ./references/scene-packs.md
- ./references/protected-spans.md
- ./references/operation-manual.md
- ./references/boundary-cases.md

The input provides:
- A blind range (e.g. B-01 to B-15)
- The model-under-test output
- If Long-form / in-place cases are included, the runner provides original char count, output char count, and retention percentage

Scoring standard:
- Cite the standard in ./evals/run-eval.md; don't invent a new one.
- SF: main problem removed, meaning and protected spans kept, no over-rewriting → ✅.
- SF: problem identified but action incomplete, flagged risk when it should have rewritten directly, bounded directly deleted or softened a whole empty sentence → ⚠️.
- SF: main problem untouched, invented facts, changed protected spans, wrong scene, long-form wrongly deleted/merged/reordered → ❌.
- SNF: kept the original or made only a minimal harmless adjustment → ✅.
- SNF: wrongly changed terms, system subjects, technical reports, quoted text, discussed words, a reasonable transition, real sentences, or protected spans → ❌.
- Scene Packs, Long-form / in-place, Bounded, Residual Audit, fact-preservation, and unsourced-citation cases are judged by the matching section of ./evals/run-eval.md.
- Use only the retention percentage the runner provides; don't count or estimate it yourself.

Output format must be exactly:

| Case | Verdict ✅/⚠️/❌ | One-line basis |
|------|------------------|----------------|
| SF-01 (B-xx) | ✅ | <one-line basis> |

Then output:

## Summary

- SF pass: X/Y
- SNF false positive: X/Y
- ⚠️ list: <case IDs; "none" if empty>
- ❌ list: <case IDs; "none" if empty>

Forbidden:
- Don't rewrite the model-under-test output.
- Don't output a grade outside the scoring scale.
- Don't replace the ./evals/run-eval.md standard with subjective reasons like "style is okay / not natural enough".
- Don't skip cases; if the output is missing one, mark ❌ and note the missing output.
```
