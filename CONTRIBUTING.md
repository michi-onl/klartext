# Contributing

Thanks for considering a contribution to klartext.

## Submitting a new phrase

New phrases are the most common contribution. Before submitting one, make a judgment:

- If it's only a synonym variant of an existing pattern, prefer adding a `benchmark`, an example, or an `operation-manual` note — don't keep growing the word table
- Suggest a new entry only if at least one holds:
  - The phrasing recurs across multiple sources
  - It changes the false-positive boundary
  - No existing pattern absorbs it stably

### 1. Determine the Tier

| Tier | Standard | Example |
|------|----------|---------|
| Tier 1 | deleting the word/phrase doesn't reduce the sentence's information | "es ist wichtig zu beachten", "delve" |
| Tier 2 | fine alone, an AI signal when clustered | "zudem", "darüber hinaus", "nuanced" |
| Tier 3 | common word, a problem only at whole-text saturation | "wichtig", "significant" |

**If you can't decide, default to Tier 2.**

### 2. Provide an example

Attach at least one before/after per new phrase:

```
❌ Erwähnenswert ist, dass die Lösung in mehreren Dimensionen überzeugt.
✅ Die Lösung schlägt die Baseline bei Latenz und Durchsatz.
```

### 3. State the false-positive risk

In what scene is this word/phrase legitimate? For example:

- "Hebel"/"Leverage" is a standard finance term, don't flag it
- "navigate" is correct in nautical/map contexts

If there's a false-positive risk, also suggest adding it to the protection list in `references/severity.md`.

### 4. Explain why "variant merging" isn't enough

Answer at least one:

- Compared to an existing representative item, what new posture or risk does this add?
- Why isn't adding a benchmark or operation-manual note enough?
- Could it make existing rules misjudge a real-person context?

## Submitting a structural anti-pattern

When adding a `references/structures.md` entry, include:

1. The pattern name
2. The problem description (why this is AI flavor)
3. German + English ❌/✅ pairs (if it's a cross-language pattern)
4. Scope note (all scenes or only the aggressive level)

## Submitting a benchmark case

`evals/benchmark.md` welcomes new cases. Format is described in the file. Both kinds are needed:

- **Should Fix**: text with AI flavor + the expected rewrite direction
- **Should Not Fix**: text that looks AI but is actually reasonable + the reason not to change it

Before adding a benchmark, decide the action type:

- If you found "a new scene boundary existing rules don't cover", prefer adding a `benchmark`
- If you found "an existing pattern absorbs it, but the maintainer judges it inconsistently", prefer adding to `references/operation-manual.md`
- If it's just a synonym variant already in the table, you usually don't need to change both `phrases` and `benchmark`
- For boundaries prone to false positives (unsourced citations, mixed scenes, discussed words, system subjects), prefer adding a benchmark

## Submitting a bad case

If you hit a real "still sounds AI after the rewrite" case, prefer the GitHub [bad-case template](.github/ISSUE_TEMPLATE/bad-case.md). It asks for:

- The original or a redacted snippet
- The tool and load mode: `lite` (only `SKILL.md`) or `full` (`SKILL.md` + `references/`)
- The scene: `chat / status / docs / public-writing / code-context / mixed`
- Where you feel it's still unnatural
- Which facts, terms, commands, quotes, or responsible subjects must not be broken

Don't submit unauthorized full private chats, sensitive info, accounts, secrets, internal links, or real personal identity data. Bad cases in a public repo should be redacted snippets, public-source observations, or authorized samples.

## PR conventions

1. One PR does one thing (add a phrase, add a structure, add a benchmark case, edit docs)
2. Update `CHANGELOG.md`
3. If you changed rule logic, update `SKILL.md` and the matching `references/` file
4. If you changed the benchmark's count, standard, or scoring logic, update `evals/run-eval.md` and the result-doc references

## Maintainer: Community Observation Intake

When a batch of new AI posture chains recurs in public discussion (heise, Reddit, Hacker News, ComputerBase, X, etc.), run this intake once rather than adding a single word entry. This is a maintainer flow, not something to run during a rewrite.

### Triggers

- **Multiple independent complaints** about the same class of expression in public discussion, not a single point
- The pattern isn't in the `phrases-de.md` table, but the variants repeat each other
- A class of expression suddenly spikes after a new SOTA model ships (e.g. the "auffangen" style)
- An existing pattern's boundary is broken by a counterexample: a word is false-positived in a technical context, or a new phrasing slips through in a counseling/reassurance context

### Intake, five steps

1. **Trace the source**: record 2–3 public-discussion links in `evals/real-samples.md` or `CHANGELOG.md` as observation sources. No unauthorized full transcription
2. **Abstract the posture chain**: generalize the recurring **string of expressions** into 1–2 identify-signals. A posture chain is steadier than a word: `Ich bin hier / ich weiche nicht aus / ich fange dich sicher auf / du bist nicht … du bist nur …` together is "over-catching + psych judgment"
3. **Judge object / scene**: list the pass boundary — which objects and scenes are the false-positive zone. Avoid "flatten everything on seeing `auffangen`"
4. **Add samples both ways**:
   - Add an `SF` covering the posture-layer hit (expected rewrite)
   - Add an `SNF` covering the pass boundary (expected no-change)
   - If possible, add one `real-samples.md` whole-passage sample (with 3-dim scoring)
5. **Upgrade the rule**: change the related `phrases-de.md` entry to "judge by object / scene", and sync the `operation-manual.md` `Identify signal` and `Keep when` with the pass boundary

### When not to run intake

- A single complaint with no recurring pattern → note it in a `tasks/` observation memo, start on the next hit
- Just a literal variant of an existing category → run the variant-merge judgment at the top of "Submitting a new phrase", no full intake
- The source is a private chat / unauthorized transcript → redact or synthesize first, don't put it straight into `real-samples.md`

### Reread check

- Do the new SF / SNF come in a pair (should-change + should-pass)
- Does the upgraded rule state the pass boundary explicitly
- Does the CHANGELOG record the observation source, not just "added a rule"
- Did this intake accidentally flatten a technical-context expression (especially `docs / code-context`)

### Automation

The top-level `automation/` directory has an intake automation tool: drop a batch of samples into `tasks/current/intake/inbox/<date>.md` (local working dir), run one `codex exec` command, and get a `tasks/current/intake/reports/<date>-intake.md` classified into "covered / variant merge / candidate new pattern", with up to four suggested actions (`no action / add benchmark / add operation-manual / consider adding a word or structure`).

Commands, file conventions, and hard constraints in `automation/README.md`; the prompt in `automation/intake-prompt.md`; the protocol in `automation/intake.md`.

Boundary: automation only covers steps 2–3 above (abstract the posture chain, judge object/scene) and outputs suggestions only; step 1 (trace), step 4 (add samples both ways), and step 5 (upgrade the rule) still need human assessment. **The intake report does not, and should not, auto-edit `benchmark.md` / `phrases-de.md` / `structures.md` / `operation-manual.md`.**

## Contributions not accepted

- Pure personal-preference word additions/removals (need an AI-text-frequency basis or multi-person consensus)
- Changes tightly bound to a specific platform (this project stays platform-agnostic)
- Content not MIT-compatible
