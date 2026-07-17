<h1 align="center">klartext — German-English de-AI rewrite skill</h1>

<p align="center">
  <strong>Don't let the model put on airs for you.</strong>
</p>

<p align="center">
  For Codex, Claude Code, Cursor, ChatGPT, and custom agents.
  <br>
  Cleans chat, technical sync, README, forum posts, and long-form German text: keep the facts first, then take that "instantly AI" tone down.
</p>

<p align="center">
  <a href="https://github.com/michi-onl/klartext/stargazers"><img src="https://img.shields.io/github/stars/michi-onl/klartext?style=for-the-badge&amp;label=stars" alt="GitHub stars"></a>
  <a href="https://github.com/michi-onl/klartext/releases"><img src="https://img.shields.io/github/v/release/michi-onl/klartext?style=for-the-badge&amp;label=release" alt="GitHub release"></a>
  <a href="evals/benchmark.md"><img src="https://img.shields.io/badge/benchmark-44%20cases-2563eb?style=for-the-badge" alt="Benchmark: 44 cases"></a>
  <a href="evals/real-samples.md"><img src="https://img.shields.io/badge/scenario%20samples-10-16a34a?style=for-the-badge" alt="Scenario samples: 10"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/michi-onl/klartext?style=for-the-badge" alt="License"></a>
</p>

<p align="center">
  <a href="#what-it-becomes">What it becomes</a> ·
  <a href="#30-second-start">30-second start</a> ·
  <a href="#how-it-decides">How it decides</a> ·
  <a href="#evaluation">Evaluation</a> ·
  <a href="#install">Install</a> ·
  <a href="#faq">FAQ</a>
</p>

> **Auf Deutsch:** `klartext` reinigt genau das Deutsch, bei dem jedes Wort stimmt, aber sofort klar ist, dass es nicht von dir kommt. Es macht Floskeln nicht hübscher und erfindet keine Fakten; es sichert erst Versionen, Befehle, Verantwortung und Belege, dann räumt es Übermaß-Empathie, Ingenieurssprech, Influencer-Ton, Nominalstil und quellenlose Autoritätsfloskeln weg. Ziel: Nach dem Umschreiben kannst du es direkt abschicken.

`klartext` is a German-English fork of [shuorenhua (说人话)](https://github.com/MrGeDiao/shuorenhua), which does the same job for Chinese and English. Same method — scenes, Tiers, scopes, reread contract — but the phrase tables and examples are re-derived for German. It targets the text where every word is correct but you can tell at a glance it wasn't written by you. It doesn't dress empty phrases up prettier and it doesn't invent facts; it locks down versions, commands, ownership, and evidence first, then strips over-catching, engineer-speak, influencer tone, Nominalstil, and unsourced authority framing.

It fits these scenes:

| Scene | What it does |
|-------|--------------|
| Everyday chat | remove over-catching, salesy endings, and report voice; keep the colloquial feel |
| Technical status sync | keep facts, versions, commands, errors, and ownership; lower the phrases |
| README / release note | say the project, changes, verification, and limits clearly; no release manifesto |
| Forum post / issue reply | sound like a maintainer talking, not a customer-service announcement |
| Long-form German | clean intra-sentence to keep the rhythm; whole empty sentences go on a "Suggested deletions" list you confirm, so long text doesn't shrink out of control |

English de-AI already has [stop-slop](https://github.com/hardikpandya/stop-slop) and [humanizer](https://github.com/blader/humanizer). `klartext` adds the German layer: what these tones look like in German, tiered by publishing scene, with facts locked before the rewrite.

## What it becomes

### Chat answer, award first then upsell

**Before**

> Großartige Frage, du triffst damit voll den Kern! Kurz gesagt: Erst den Flow zum Laufen bringen, dann optimieren. Ich kann dir direkt eine absolut sichere finale Lösung geben, schon getestet, läuft rund. Soll ich dir die Doku gleich mit aufräumen? Nur ein Wort von dir.

**After**

> Genau da liegt's: erst den Flow zum Laufen bringen, dann optimieren. Die Lösung schick ich dir. Doku auch mit dazu?

An award up front, an upsell chasing at the end, "kurz gesagt" and "der Kern" rotating in the middle — a posture chain that reads instantly as AI. The text is a synthetic example that packs the most-flagged tics into one paragraph.

### Release note, no changes in sight

**Before**

> ## v1.8.0 Release Highlights
>
> Diese Version ist ein zukunftsweisendes, systemisches Upgrade. Wir haben nicht nur das Rewrite-Erlebnis rundum optimiert, sondern mit einer völlig neuen Fähigkeitsmatrix die zentralen Ausdrucksbedürfnisse der Nutzer in README, Release Note, Forum-Post und Issue-Antwort sicher aufgefangen. Danke an alle für die anhaltende Unterstützung!

**After**

> ## v1.8.0
>
> - Neu: `references/scene-packs.md`, deckt README, Release Note, Forum-Post und Issue-Antwort ab
> - `evals/benchmark.md`: 4 neue Scene-Pack-Regressionsfälle
> - `evals/real-samples.md`: 2 neue Szenario-Samples
>
> Diese Version macht keine Voice Calibration; das Thema wird auf später verschoben.

A release-note reader wants the change list, not a manifesto. Keep the version number, strip the posture layer, and write down what wasn't done too. Full sample in [evals/real-samples.md](evals/real-samples.md) RS-02.

### The grand opening of a public intro

**Before**

> In einer Zeit, in der KI die Softwareentwicklung grundlegend neu gestaltet, ist die Frage, wie man ein wahrhaft entwickler-befähigendes Tool schafft, zu einer nicht zu unterschätzenden Schlüsselfrage der Branche geworden.

**After**

> Es gibt viele KI-Tools, aber das umgeschriebene Deutsch trägt oft noch Floskeln. Dieses Projekt räumt genau die weg: Übermaß-Empathie, Ingenieurssprech, Nominalstil, quellenlose Autorität und Selbstaufwertung.

More examples in [references/examples.md](references/examples.md) and [evals/real-samples.md](evals/real-samples.md).

## 30-second start

**Claude Code** — two commands in the conversation, then it triggers automatically:

```text
/plugin marketplace add michi-onl/klartext
/plugin install klartext@klartext
```

Once installed, say "de-AI this / mach das auf Deutsch natürlicher" in the conversation and it triggers. Manual install (cp / symlink to follow updates) in [install/claude-code.md](install/claude-code.md).

**Codex** — one-off use after clone:

```bash
git clone https://github.com/michi-onl/klartext.git && cd klartext
codex exec -C . "Read ./SKILL.md and rewrite the following text by its rules: …"
```

For long-term project use, copy the skill files into the project and note the trigger in `AGENTS.md`; see [install/codex.md](install/codex.md).

**Just want to see the problems, not a rewrite**: add "in annotation mode, only flag problems, don't rewrite" to the instruction.

Cursor, OpenClaw, ChatGPT, and custom agents in [Install](#install).

## How it decides

`klartext` doesn't replace on sight. One principle:

> **Information first, then style.**

The full flow is six fixed steps:

1. Detect the scene: `chat / status / docs / public-writing`; on README, release note, forum post, issue reply, enter the matching Scene Pack
2. Mark protected spans: numbers, versions, commands, paths, errors, quotes, names, and ownership are locked first (full list in [references/protected-spans.md](references/protected-spans.md))
3. Judge hit strength (`Tier 1 / 2 / 3`), then set rewrite level (`minimal / standard / aggressive`) and scope (`structural / bounded / in-place`); Tier only describes how strongly a problem is hit, not the strength
4. Change by pattern first, the word table is only a fallback
5. Fidelity reread: facts, terms, register, protected spans, one by one
6. Only if residue remains, do a second Residual Audit, light fixes only

### Scene and strength

The four scenes' default strength:

| Scene | Default | Strategy |
|-------|---------|----------|
| `chat` | light | cut only obvious phrases, don't turn chat into an official memo |
| `status` | medium | keep action, state, blockers, and next step |
| `docs` | medium | technical expression first, second pass more conservative |
| `public-writing` | heavy | full-rule scan, and trigger Scene Packs as needed |

### By publishing intent (Scene Packs)

Publishable text is further split by "where it's going" — not a tone change, but a change of edit by publishing purpose: a README first screen says what this is and who it's for; a release note lists the changes, verification, and limits; a forum post reads like a maintainer sharing observations, not a corporate announcement; an issue reply confirms the problem and next step, no customer-service reassurance. Each sub-scene's goal and common symptoms in [references/scene-packs.md](references/scene-packs.md).

### Long-form without shrinking: three scopes

Long text under the default actions accumulates sentence deletions and merges, so 1800 words might get compressed to 1000; conversely, deleting nothing leaves whole empty sentences in place. So long-form splits "how much to delete" into three scopes, orthogonal to strength:

| scope | Delete whole sentences? | For |
|-------|-------------------------|-----|
| `structural` | freely delete/merge/reorder | short text, explicit rewrite |
| `bounded` (long-form default) | whole empty sentences become a "Suggested deletions (to confirm)" list, you decide | `public-writing` long text |
| `in-place` | delete nothing, only lower tone intra-sentence | explicit "exactly as-is" |

### Which way the rewrite leans

Cleaning isn't only deletion. It also pulls the text toward:

- Concrete action over abstract inflation
- A real subject and action over posture
- Slight asymmetry allowed, not every sentence polished into one voice
- Calibrated by scene: chat doesn't become an announcement, docs don't become a bit

## Evaluation

The rule layer covers a native German phrase table, the English phrase table ([phrases-en.md](references/phrases-en.md)), and 21 structural anti-patterns.

The current benchmark has 44 cases:

| Type | Count | Goal |
|------|-------|------|
| SF | 30 | text that should change must hit and fix the main problem |
| SNF | 14 | text that shouldn't be touched must pass or get a light note |
| Scenario samples | 10 | whole-passage samples scored on natural, faithful, ship-ready; long-form adds `length rhythm` |
| Scene Packs | 4 | README / release-note / forum-post / issue-reply cases |
| Long-form (in-place / bounded) | 2 | keep length / deletion list, checking retention, sentence alignment, and key transitions |

The benchmark uses a blind real-run standard: the model under test reads only the anonymized, shuffled [benchmark-blind.md](evals/benchmark-blind.md) (no expectations), and the judge scores via the map table. The static walk-through is a pre-release quick self-check. Full case set in [evals/benchmark.md](evals/benchmark.md); whole-passage scenario samples (high-fidelity synthetic) in [evals/real-samples.md](evals/real-samples.md). Each real run's eval-set version, model, and standard are registered in [evals/run-manifest.md](evals/run-manifest.md). No German real run is recorded yet — see the manifest.

## Install

| Platform | Doc |
|----------|-----|
| Codex | [install/codex.md](install/codex.md) |
| Claude Code | [install/claude-code.md](install/claude-code.md) |
| Cursor / Windsurf | [install/cursor.md](install/cursor.md) |
| OpenClaw | [install/openclaw.md](install/openclaw.md) |
| ChatGPT / Custom GPT | [install/chatgpt.md](install/chatgpt.md) |

The core needs only `SKILL.md` (lite); for long-term projects, public text, and cases needing false-positive protection, bring the full `references/` package (full).

For long-term project use, add a trigger note to `AGENTS.md`:

```markdown
## Writing style
When a task involves "de-AI", "auf Deutsch natürlicher", "sound human", "not like a template", follow `klartext/SKILL.md`.
Apply it to external text first; don't apply it to code, logs, config, or command output.
```

## FAQ

### Is this for fooling AI detectors?

No. The goal is to reduce template feel, performance, and register drift so text is more natural and shippable — not to evade detection.

### Can I use it for English?

Yes. This is a German-English project; the English side (carried over from the upstream) cleans common English phrases and the template feel in Denglisch (German-English mixing).

### Why does it sometimes still sound AI after the rewrite?

"Removing obvious tics" is not "having a specific author's personal voice". The current version is better at clearing template feel and performance; it doesn't fit a specific person's long-term writing habits.

### Will it break technical docs?

Normally it won't edit technical docs in chat voice. `docs`, `status`, and `code-context` have more conservative protection; commands, paths, versions, errors, and metrics are kept faithful first.

### German-specific: does it flip Sie/du?

No. The address form (Sie vs du) and grammatical attribution are treated as protected spans; it won't silently flip them to "sound more human".

## Contributing: a bad case beats a star

New eval samples, boundary cases, real problem cases, before/after samples, and false-positive guards are welcome. If you hit a "still sounds AI after the rewrite" text, submit it via the [bad-case template](.github/ISSUE_TEMPLATE/bad-case.md). Redact first — don't paste unauthorized full private chats, secrets, internal links, or real personal identity data.

Before submitting a new word, ask one thing:

> Is this a "new pattern", or just "a variant of an existing pattern"?

Full rules in [CONTRIBUTING.md](CONTRIBUTING.md).

## Related projects

- [shuorenhua (说人话)](https://github.com/MrGeDiao/shuorenhua): the Chinese-English upstream this fork is based on
- [stop-slop](https://github.com/hardikpandya/stop-slop): English AI-slop rules and scoring framework
- [humanizer](https://github.com/blader/humanizer): English AI-pattern taxonomy
- [avoid-ai-writing](https://github.com/conorbronsdon/avoid-ai-writing): AI-writing problem taxonomy and severity reference

## License

[MIT](LICENSE)
