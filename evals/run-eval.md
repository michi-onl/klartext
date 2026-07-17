# klartext eval instructions

> This file is the standard for the static walk-through / pre-release quick self-check (evaluator sees the expectations), and the single source for the judge's scoring criteria.
> The formal dual-model real-run standard is blind: the model under test reads only `benchmark-blind.md`, not this file or `benchmark.md`. See `automation/eval/README.md`.

## Generic eval prompt

Paste the following to any long-context model to run the eval:

---

You are an evaluator for a "de-AI" rule set that works on German and English text.

**Rule file locations:**
- Core entry: `./SKILL.md`
- Positive Style Contract: `./references/positive-style.md`
- Protected Spans: `./references/protected-spans.md`
- German banned phrases: `./references/phrases-de.md`
- English banned phrases: `./references/phrases-en.md`
- Structural anti-patterns: `./references/structures.md`
- Severity: `./references/severity.md`
- Rewrite examples: `./references/examples.md`
- Operation manual: `./references/operation-manual.md`
- Scene guardrails: `./references/scene-guardrails.md`
- Scene Packs: `./references/scene-packs.md`
- Boundary cases: `./references/boundary-cases.md`

**Benchmark location:**
`./evals/benchmark.md`

**Your task:**

1. Read `SKILL.md` first, understand the main flow: scene detection → protected spans → Tier → rewrite level → scope → fidelity reread → residual reread → output contract
2. Read files under `references/` as needed for phrases, structures, boundaries, and false-positive protection
3. Read `./evals/benchmark.md` and evaluate each case in it

### For Should Fix (SF-01 to SF-30):
- Judge the main scene (chat / status / docs / public-writing) and the problem type
- Judge the rewrite level (minimal / standard / aggressive)
- Judge the scope (structural / bounded / in-place); long `public-writing` defaults to `bounded` (whole empty sentences to the deletion list, real sentences cleaned intra-sentence, no merging, no reordering); when the user asks for exactly-as-is or the sample is marked `Long-form / in-place`, use the `in-place` intra-sentence boundary
- Do the fidelity reread first; only when pass 1 preserved the facts but obvious residue remains, do the `Residual Audit`
- Pass 2 checks only 5 things: opener residue, summary residue, narrator residue, empty-judgment residue, uniform sentence length
- Process the original by the rules: output the rewrite by default; if the sample passes as `audit-only`, output only the missing-source / missing-attribution risk note, without forcing a full rewrite
- List the hits (problem type + the specific word/structure hit)
- Judge pass/fail (✅ pass / ⚠️ partial / ❌ fail) with a short reason
- For unsourced-citation SF cases, judge by scene: `public-writing / chat` pass by deleting the unsupported authority framing; `docs / status` pass by flagging the missing source without faking proof
- For `Residual Audit` SF cases, check pass 2 did only light fixes; if it rewrote everything, added facts, or made `status / docs` more colloquial, mark `❌`
- For `Scene Packs` SF cases, check it hit the `README / release-note / forum-post / issue-reply` sub-scene and tightened tone by publishing intent
- For `Long-form / in-place` SF cases, check it kept the sentence count, paragraph order, and key transitions; if it deleted whole sentences, merged adjacent sentences, or reordered paragraphs, mark `❌`

### For Should NOT Fix (SNF-01 to SNF-14):
- Judge why this text should not change
- If it kept the original or made only minimal harmless adjustments → ✅ pass
- If it wrongly changed terms, system subjects, technical reports, quoted text, or reasonable expressions in boundary cases → ❌ false positive, name the spot
- For `Scene Packs` SNF cases, confirm it didn't turn an already-direct README/release note/forum post/issue reply into another scene
- For `Long-form / in-place` SNF cases, confirm it didn't delete rhythm-bearing repetition, connectors, or transitions

### Final summary:
Output a summary table:

```text
| Case | Type | Result | Note |
|------|------|--------|------|
| SF-01 | Should Fix | ✅/⚠️/❌ | ... |
| ... | ... | ... | ... |
| SNF-01 | Should NOT Fix | ✅/❌ | ... |
| ... | ... | ... | ... |
```

And give:
- SF pass rate: X/30
- SNF false-positive rate: X/14
- Targets met: SF > 90%, SNF false-positive rate < 10%

**Notes:**
- Don't false-positive system subjects, technical terms, academic passive, real debug dialogue, and other known boundaries
- `code-context` samples: only touch text in comments / docstrings / commit messages, never the code
- `Scene Packs` samples: keep the main scene and protected spans first, then handle by sub-scene publishing intent; don't turn a release note into marketing, a forum post into an announcement, or an issue reply into customer-service talk
- `Long-form / in-place` samples: don't delete whole sentences, merge adjacent sentences, or reorder paragraphs; word-count retention target ≥ 0.90, hard floor 0.85
- `Bounded` samples: don't directly delete whole empty sentences, don't put real sentences on the deletion list, and don't merge a business-jargon shell sentence with the data sentence that follows it

---

## Codex quick run

```bash
codex exec -C . --sandbox read-only \
  "Read ./SKILL.md first, then the relevant files under ./references/, and evaluate all cases in ./evals/benchmark.md. For SF cases, judge scene, Tier, rewrite level, and scope, then process by the rules and judge pass/fail; for README, release note, forum post, issue reply, also read ./references/scene-packs.md and handle by the sub-scene; for Long-form / in-place samples, honor the no-delete-whole-sentence, no-merge, no-reorder boundary and check word-count retention, sentence-count alignment, and key transitions. Do the fidelity reread first; only when pass 1 preserved the facts but obvious residue remains, do a Residual Audit. The Residual Audit checks only opener residue, summary residue, narrator residue, empty-judgment residue, uniform sentence length, and allows only light fixes. Output the rewrite by default, but for unsourced-citation samples passing as audit-only, output only the missing-source risk note. Unsourced-citation SF cases are judged by scene: public-writing/chat pass by deleting the unsupported framing, docs/status pass by flagging the missing source without faking proof. For SNF cases, judge false positives. Note: mixed samples only touch the truly problematic body, not user instructions, quotes, or discussed words. code-context samples only touch comments/docstrings/commit messages, not code. Scene Packs samples must not delete version numbers, paths, links, IDs, or attribution. Finally output a summary table, SF pass rate, and SNF false-positive rate."
```

## Claude Code quick run

Start Claude Code in the project directory and say:

```text
Read ./SKILL.md and all files under ./references/, then evaluate all cases in ./evals/benchmark.md. For SF cases, judge scene, Tier, rewrite level, and scope, then process by the rules and judge pass/fail; for README, release note, forum post, issue reply, also read ./references/scene-packs.md and handle by the sub-scene; for Long-form / in-place samples, honor the no-delete-whole-sentence, no-merge, no-reorder boundary and check word-count retention, sentence-count alignment, and key transitions. Do the fidelity reread first; only when pass 1 preserved the facts but obvious residue remains, do a Residual Audit. The Residual Audit checks only opener residue, summary residue, narrator residue, empty-judgment residue, uniform sentence length, and allows only light fixes. Output the rewrite by default, but for unsourced-citation samples passing as audit-only, output only the missing-source risk note. Unsourced-citation SF cases are judged by scene: public-writing/chat pass by deleting the unsupported framing, docs/status pass by flagging the missing source. For SNF cases, judge false positives. Note: mixed samples only touch the truly problematic body, not user instructions, quotes, or discussed words. code-context samples only touch comments/docstrings/commit messages, not code. Scene Packs samples must not delete version numbers, paths, links, IDs, or attribution. Finally output a summary table, SF pass rate, and SNF false-positive rate.
```

## Generic LLM / API

If you use ChatGPT, Claude Web, or another API:

1. Use the "Generic eval prompt" section above (between the two horizontal rules) as the system prompt or first message
2. Paste `SKILL.md`, the `references/` files, and `evals/benchmark.md` together
3. When tokens are tight, prioritize `SKILL.md` + `benchmark.md` + `scene-packs.md` + `severity.md` + `boundary-cases.md`

Note: models with a short context window may not run all cases at once; batch them (SF first, then SNF).
