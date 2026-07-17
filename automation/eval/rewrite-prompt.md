# Benchmark Rewrite Prompt

Use the prompt below directly in a model run. It only makes the model under test process a given blind range by the rules; it does not score.

> Blind standard: the model under test reads only `evals/benchmark-blind.md` (anonymized IDs, shuffled, no expectations), not `benchmark.md` or `run-eval.md` — those carry expectations and scoring criteria, and reading them voids the run.

```text
You are running the klartext benchmark blind rewrite. As the model under test, process the given range of blind cases by the current repo rules, and output a stable, judge-comparable result. You work on German and English text.

Path boundary:
- Use only `./SKILL.md`, `./references/`, `./evals/benchmark-blind.md`, and `./automation/eval/rewrite-prompt.md` in the current working directory.
- Do not read any file under `./evals/` other than `benchmark-blind.md`: the rest carry expectations and scoring standards, and reading them voids this run.
- The "Scenario Sample Eval Pack" referenced by SKILL.md step 6 is skipped in this run; do not read it.
- Do not read or reference a globally installed copy such as `~/.codex/skills/klartext`, `~/.claude/skills/klartext`, or any path outside the repo.
- If a global skill is auto-triggered, treat it as environment noise; this run's standard is the current working-directory files.

Read first:
- ./SKILL.md
- ./evals/benchmark-blind.md

Then read as needed:
- ./references/positive-style.md
- ./references/protected-spans.md
- ./references/phrases-de.md
- ./references/phrases-en.md
- ./references/structures.md
- ./references/severity.md
- ./references/examples.md
- ./references/operation-manual.md
- ./references/scene-guardrails.md
- ./references/scene-packs.md
- ./references/boundary-cases.md

The input specifies a blind range, e.g.:
- B-01 to B-15
- B-16 to B-30
- B-31 to B-44

Each case's fields come from ./evals/benchmark-blind.md:
- Title line: blind ID / scene
- Test text: the quote or code block after the title

Requirements:

1. Process every case in the given range one by one; don't skip, merge, or add/remove IDs.
2. For each case, output the decision chain first, then the result.
3. The decision chain always has four items, each a short phrase:
   - Scene: chat / status / docs / public-writing / code-context, with README / release-note / forum-post / issue-reply / long where needed
   - Tier: Tier 1 / Tier 2 / Tier 3 / protected / not-fix
   - Level: minimal / standard / aggressive / audit-only / no-op
   - scope: structural / bounded / in-place / not-applicable
4. Change what should change: output the rewrite by default; if the rule says audit-only (e.g. unsourced citation in status/docs), output the risk note, don't fake proof.
5. Keep what the rules say to keep, and state which rule passed it; if you made a minimal harmless adjustment, state why it didn't false-positive protected spans, terms, quotes, or a reasonable context.
6. code-context: only comments, docstrings, or commit messages, never the code.
7. Scene Packs: keep the main scene and protected spans first, then handle by README / release-note / forum-post / issue-reply publishing intent.
8. When scope is in-place: don't delete whole sentences, merge adjacent sentences, or reorder paragraphs.
9. When scope is bounded: clean real sentences intra-sentence, route whole empty sentences into a "Suggested deletions (to confirm)" list; don't put real, information-bearing, or rhythm-bearing sentences on the list; don't merge adjacent sentences.

Output format must be exactly:

## <blind ID>

Decision chain: scene=<...>; Tier=<...>; level=<...>; scope=<...>

Hits:
- <the problem type hit, the protected point, or the pass reason>

Result:
<the rewrite, the audit-only risk note, or the keep-original note>

Forbidden:
- Don't guess or label whether a case is "should fix" or "should not fix"; just process by the rules.
- Don't self-score pass / partial / fail; scoring is the judge's job.
- Don't skip cases.
- Don't merge several cases under one title.
- Don't change the two format lines `## <blind ID>` and `Decision chain: scene=...; Tier=...; level=...; scope=...`.
- Don't invent sources, data, responsible subjects, commands, version numbers, or metrics the original lacks, to make the result look better.
```
