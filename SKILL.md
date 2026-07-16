---
name: klartext
description: Checks and cleans AI slop out of German and English text. Use for "de-AI", "sound human", "not like a template", "not so much like ChatGPT", "auf Deutsch natürlicher", "keine Textbausteine", "kein KI-Deutsch" style rewrites and reviews. Controls edit strength by scene while preserving facts, terminology, register, and attribution.
---

# Klartext

Pull text back from "a model performing writing" to "a specific person expressing this in the current situation".

This skill is not a banned-word replacer, and it is not anti-technical, anti-abstract, or anti-professional. Its goal is to reduce template feel, performance, and register drift while keeping facts, terminology, and the responsible subject intact.

> Origin: this is a German-English fork of [shuorenhua (说人话)](https://github.com/MrGeDiao/shuorenhua), which does the same job for Chinese and English. The method, tiers, scopes, and reread contract are shared; the phrase tables and examples are re-derived for German (English side is carried over unchanged).

## When to use

Use it for:

- The user explicitly says "de-AI this", "sound human", "auf Deutsch natürlicher", "nicht wie ein Textbaustein", "not so much like ChatGPT"
- Rewriting German or English `chat`, `status`, `docs`, `public-writing`
- Deciding first whether a text needs a light, medium, or heavy edit

Do not force it onto:

- Literal translation, preserving original style, imitating an official template or a specific brand voice
- Text that is mostly code, logs, commands, config, API names, or error messages
- Fact-checking requests, where the user wants correctness review, not a style rewrite

## Core stance

- De-AI-ing mainly targets template feel, wrap-up cadence, false agency, register mixing, and performative engineer-speak.
- Keep it technical. Domain terms, system subjects, postmortem language, and PRD/release-note terminology may be kept by default.
- Information first, style second. No rewrite may add facts, drop core facts, or change the responsible subject.
- No mechanical synonym-swap table. By default you may delete sentences, merge sentences, lower the register, change the subject, and cut summary endings; only in `in-place` scope do you restrict yourself to intra-sentence edits.
- Phrase tables list representative items only; they do not chase every variant. For a new tic, first classify it under an existing pattern, then decide whether a new entry is warranted.
- German-specific: never silently flip register (Sie ↔ du) or grammatical gender/attribution. Register is treated like any other protected span.

## Execution order

Do this in fixed order, no skipping:

1. Detect scene: `chat / status / docs / public-writing`
2. Mark no-touch spans: draw the `protected spans` first — terms, system subjects, quoted text, commands, or formal register that must survive
3. Judge Tier: `Tier 1 / Tier 2 / Tier 3`, by how strongly the problem is hit — Tier is not the same axis as edit strength
4. Then set level: `minimal / standard / aggressive`
5. Then set scope: `structural / bounded / in-place` — how far you may delete: free deletion and reordering, only whole empty sentences into a deletion list, or nothing deleted at all
6. Run the minimal rules in this file first; whenever `references/` is readable, keep reading by problem type: [Protected Spans](./references/protected-spans.md), [Positive Style Contract](./references/positive-style.md), [Operation Manual](./references/operation-manual.md), [Structural Anti-patterns](./references/structures.md), and the relevant phrase tables. If the goal is "ready to ship", or the text is clearly a README, release note, forum post, or issue reply, also read [Scene Packs](./references/scene-packs.md), [Scenario Samples](./evals/real-samples.md), and [Rewrite Examples](./references/examples.md)
7. Reread in two passes: fidelity reread first, then a residual-flavor reread if needed
8. Output: a single recommended version by default; switch to `annotation mode` only when the user explicitly asks to "flag problems, don't rewrite"

When running step 6, handle by "pattern" first, then fall back to "entry":

- The same class of debug-speak, violence-speak, proactive-pushiness, or summary-cue speak is handled by one pattern; you do not need a per-word hit
- Only when a new phrasing changes the false-positive boundary, or clearly does not belong to an existing pattern, treat it as a new entry

## 1. Scene detection

Judge the main scene first, then handle local problems. Mixed text keeps one main register; other registers survive only at the information level.

### `chat`

Signals:

- Short replies, everyday conversation, collaboration, comments, quick feedback
- Colloquial is fine, but do not put on airs

Default level: `minimal`

### `status`

Signals:

- Standup updates, progress sync, retro summaries, report-style status
- Focus is timeline, action, result, risk

Default level: `minimal` or `standard`

### `docs`

Signals:

- How-tos, technical notes, API docs, FAQ, incident postmortems
- Focus is searchability, reproducibility, stable terminology

Default level: `minimal`

### `public-writing`

Signals:

- Newsletters, LinkedIn/blog posts, public threads, opinion pieces
- Focus is register consistency; don't fake "having insight"

Default level: `standard`

See [Scene Guardrails](./references/scene-guardrails.md) for tighter per-scene floors.

### Scene Packs

If the text itself hits any sub-scene below — regardless of whether the user says so, and regardless of the main-scene call — also read Scene Packs:

- `README`: on project intro, quick start, install, feature list, README intro signals, the first screen must say "what this is, who it's for, what problem it solves"
- `release-note`: on version headers, `Release Highlights`, `Added / Changed / Fixed / Tested`, changelog lists, list the changes, verification, and limits — no release manifesto
- `forum-post`: on heise/Reddit/Hacker News/community-thread/retro signals, keep the maintainer's real observations and community voice — don't turn it into an announcement
- `issue-reply`: on issue/PR reply, bad case, repro, "benchmark in next version" signals, confirm the problem and the next step first — no customer-service reassurance

Sub-scenes only govern publishing intent and register tightening; they do not override protected spans, Tier, level, or reread rules. Full strategy in [Scene Packs](./references/scene-packs.md).

## 2. Single-file fallback rules

Even with only `SKILL.md` loaded, basic rewriting must work. These rules apply directly by default:

- Delete throat-clearing openers, sycophancy, and meta-commentary: e.g. `Es ist wichtig zu beachten, dass`, `Lass mich dir das erklären`, `Ich hoffe, das hilft dir weiter`, `Großartige Frage!`
- Delete empty summaries and wrap-up cadence: e.g. `Zusammenfassend lässt sich sagen`, `Letztendlich`, `Im Grunde genommen`, `Am Ende des Tages`
- Handle binary-contrast skeletons: `nicht X, sondern Y`, `statt X lieber Y` — usually drop the first half and just say `Y`
- Handle unsourced citations: `Studien zeigen`, `Untersuchungen belegen`, `Experten sagen`, `studies show`, `experts say` — pick `rewrite-safe` or `audit-only` by scene; use `rewrite-with-placeholder` only when the user explicitly wants the argument skeleton kept; never invent sources
- Turn business jargon and performative engineer-speak back into plain actions: e.g. `leveragen`, `Synergien heben`, `aufs nächste Level heben`, `Deep Dive`, `abholen`, `zielführend`, `leverage`
- On over-catching, doing the reader's emotional labor, or identity-certification praise: e.g. `Du bist nicht zu empfindlich`, `Du wurdest nur zu lange nicht richtig aufgefangen`, `Du triffst damit den Kern`, `das Niveau eines Spitzenforschers` — delete the posture layer and return to a low-commitment reply or a concrete judgment; don't perform "I get you"
- On translationese, prefer to shorten the subject and action; avoid long attributive chains, stacked passives, `im Rahmen von …`, `vor dem Hintergrund …`
- False-positive protection first: quoted text, commands, API names, field names, logs, error messages, system subjects, and technical-report terminology are kept by default
- For English words inside German sentences (Denglisch), judge each word by its actual meaning in the sentence — don't mechanically apply the English word table

Single-file mode is only a fallback, not the full mode. Whenever `references/` is readable, keep reading the matching files; only when the system prompt truly ships `SKILL.md` alone do you degrade to this file's basic cleanup.

### Unsourced citation modes

When handling unsourced citations, always pick exactly one of these 3 modes:

- `rewrite-safe`
  - Delete authority framing like `Studien zeigen / studies show / Fachleute meinen`
  - Keep only judgments that already hold without the invented source
  - Default for `chat` and `public-writing`
- `audit-only`
  - Don't write a source for the author, and don't turn an unsupported claim into something that reads as proven
  - Point out "missing source / missing attribution" explicitly; keep the sentence unrewritten if needed
  - Default for `docs` and `status`
- `rewrite-with-placeholder`
  - Only when the user explicitly wants the original structure, tone, or editorial frame kept
  - You may write a placeholder like "some research suggests …, but no source is given here"
  - Never fill in an institution, data, year, or study name

If the user picks no mode, use the scene default; for cross-scene text, prefer the more conservative `audit-only`.

## 3. Rewrite level

### `minimal`

For: text that is basically natural and only needs local template feel, wrap-up cadence, and excess rhetoric removed.

Default actions:

- Delete empty summaries
- Push over-inflated tone back to normal
- Push "sentences that sound like they're explaining that they can write" back to plain statements

### `standard`

For: clear AI flavor or register mixing, but the information skeleton is good.

Default actions:

- Unify register
- Fix engineer-performance-speak, business jargon, narrator voice
- Merge sentences or change the subject where needed

### `aggressive`

For: dense `Tier 1` hits, or `Tier 1 + Tier 2` stacking into strong template or performance feel across a passage.

Limits:

- Allowed only when `Tier 1` is clearly dense, or several structural problems stack
- Protect facts and terms first, then rewrite
- `docs` does not escalate to `aggressive` by default

## 3.5 Edit scope

Scope is whether you may change sentence and paragraph structure this time; it is a separate axis from `minimal / standard / aggressive`. The three scopes differ by "can you delete whole sentences, and how": `structural` deletes/merges/reorders freely; `bounded` deletes only whole empty sentences that lose no information, and routes them through a deletion list for the user to confirm; `in-place` deletes nothing.

### `structural`

Default scope. For short text, text explicitly asked to be rewritten, and text with very high AI-flavor density where original cadence need not be kept.

Allowed actions:

- Delete whole empty summary sentences
- Merge adjacent factual sentences
- Lightly adjust sentence order or paragraph landing
- Rewrite local structure by scene

### `bounded`

Default scope for long German `public-writing` (roughly 1000+ words). The goal is to clean whole-sentence AI flavor thoroughly without `structural` compressing it unpredictably — long text under `structural` shrinks by an amount that depends on the model (the same piece might be -18% or -39%), which the user cannot predict. `bounded` hands "how much to cut" back to the user.

Relationship to the other two:

- More restrained than `structural`: no merging adjacent sentences, no reordering paragraphs, no deleting real sentences or intentional rhythm repetition
- More de-flavoring than `in-place`: may delete sentences that are "entirely empty", but not directly — they go into a deletion list for the user to decide

A sentence may enter the deletion list only if all three hold:

1. Deleting it leaves the paragraph's information unchanged (it carries no unique fact, number, judgment, action, or instruction)
2. It is not the only transition between two adjacent real sentences
3. It hits a pure empty pattern: empty summary / value-inflation ending / unsourced authority framing / sycophantic opener / whole-sentence narration

Two kinds of action run separately (evidence-based: in long text, a leading discourse marker at the start of a sentence can be cleaned intra-sentence, but a whole empty sentence cannot be deleted under `in-place` — it only gets softened into another phrasing):

- A strippable leading marker at the sentence start (`Erwähnenswert ist / Letztlich / Das zeigt`) still followed by real content → clean it intra-sentence, drop the marker, keep the skeleton, no list
- A whole sentence that is empty, where stripping the marker leaves nothing (unsourced claim, `nicht nur … sondern auch …` value inflation) → goes into the deletion list; do not softening it into another phrasing on your own

Output: the body is the intra-sentence-cleaned draft, followed by a "Suggested deletions (to confirm)" list, each item `original + why deleting loses no information`. Delete only on the user's nod; the user decides the length.

### `in-place`

For when the user explicitly asks "exactly as-is / delete nothing / strictly keep the sentence count". Stricter than `bounded`: even whole empty sentences are not deleted, only lowered intra-sentence.

Default triggers:

- The user prompt explicitly asks to keep the sentence count, exact as-is, delete nothing, or reports that `bounded` still cut too much

Forbidden actions:

- Don't delete whole sentences (even if the whole sentence is empty)
- Don't merge adjacent sentences
- Don't reorder paragraphs
- Don't compress multiple paragraphs into one

Allowed actions:

- Intra-sentence word or phrase replacement
- Delete intra-sentence cue layers, empty modifiers, and tone padding
- Push intra-sentence inflated tone back to a plain judgment
- Break an overloaded structure inside a single sentence, without changing paragraph order

Before deleting a phrase, run a semantic-independence check: after deletion, the remainder must still be a complete, readable statement with no dangling reference. Otherwise use intra-sentence replacement, don't force the deletion. For a whole empty sentence, keep the original and mark `[empty sentence, suggest human review whether to delete]`; don't soften it into a new phrasing.

`aggressive + in-place` can coexist, but warn the user first: long text under `aggressive` shrinks visibly; if the user really wants to keep length, prefer `standard + bounded`. Only when the user insists, run `aggressive + in-place`, still honoring the no-delete, no-merge, no-reorder boundaries.

## 4. Tier severity

Tier is how strongly a problem is hit, consistent with [Severity](./references/severity.md); it does not indicate edit strength.

### Tier 1

Replace by default. On hitting these words or patterns, usually delete or swap for something concrete. Common types:

- Throat-clearing openers, summary endings, sycophantic sentences
- Obvious business jargon, content-mill phrasing, performative engineer-speak
- Over-catching empathy, doing the reader's emotional labor, solemn previews and identity-certification praise
- In English: sycophantic openers, significance inflation, business jargon

Default handling: local hits use `minimal` or `standard`; dense hits may escalate to `aggressive`

### Tier 2

Fine alone, but an AI-flavor signal when clustered in one paragraph. Common types:

- Stacked high-frequency connectives
- Stacked decorative modifiers
- One class of posture word repeated in one paragraph

Length reference: short paragraph (< 100 words) flags at 2+ in one paragraph; long paragraph (≥ 100 words) flags at 3+.

Default handling: keep the single best-fitting one, rewrite the rest; usually `minimal` or `standard`

### Tier 3

Common words that are not a problem by themselves, handled only when whole-text density is clearly too high. Common types:

- `wichtig / entscheidend / zentral / verbessern`
- `significant / innovative / effective`

Default handling: replace only some of the repeated hits, usually `minimal`, sometimes leave unchanged

## 5. No-touch and keep rules

The following are kept by default unless the user explicitly wants the style changed and the change does not harm information:

- Quoted text, commands, API names, parameter names, field names, config keys, logs, error messages
- System-behavior subjects in technical docs
- Domain terminology in postmortem / incident / PRD / release note
- Abstract sentences carrying key facts, even if they "sound a bit AI"
- German register and address form (Sie/du) — do not flip it silently

Don't make text faker in the name of "sounding human". Professional text may be professional; the point is to avoid template feel and performance, not formality.

Full protection list in [Protected Spans](./references/protected-spans.md).

## 6. Positive style targets

Rewritten text should aim to satisfy:

- Concrete information, not empty summaries propping up momentum
- A real subject and action, not a false agent as backstop
- One consistent register, not jumping between engineer-speak, business-speak, and influencer-speak
- "Ready to ship" as the endpoint, not polishing further into distortion to seem human
- Rhythm, but rhythm from cutting redundancy and keeping the point, not from forced punchlines
- A stance, but a stance from judgment or fact, not from "faking insight"
- Boundaries: if unsure, say so; don't do the other person's psychological judgment, and don't perform "I understand"

Fuller positive targets, per-scene calibration, and "cleaner vs more human" comparisons in [Positive Style Contract](./references/positive-style.md).

## 7. Output contract

Output one recommended version by default; do not default to showing the review process, multiple versions, or item-by-item commentary.

### Annotation mode

Enable only when the user explicitly asks for something like:

- `Don't rewrite yet, just flag the problems`
- `Where does this sound AI?`
- `Only diagnose / review / annotate`
- `Tell me first whether it needs changing`

`annotation mode` does not hand over a full rewrite; it outputs only the 1–5 most important problem points by default. Each point always contains these 4 fields:

- `Problem family`: e.g. `throat-clearing opener / unsourced citation / engineer-speak / register mixing`
- `Trigger`: name the hit word, structure, or local sentence
- `Suggested action`: delete, swap for something concrete, add a source, leave unchanged
- `Rewrite recommended`: `yes / no`

Extra constraints:

- If the main problem is "missing source", you may only suggest adding a source without forcing a rewrite
- If the text falls inside the false-positive boundary, write `Rewrite recommended: no`
- Don't say "only flag problems" while sneaking in a full rewrite
- When the user did not ask for `annotation mode`, still output a single recommended version per the default contract

For unsourced citations, output must match the chosen mode:

- Under `annotation mode`, output only the handling suggestion, not a full rewrite
- Under the default rewrite mode, deliver the rewrite per the chosen mode
- `rewrite-safe`: suggest deleting the unsupported authority framing; if not `annotation mode`, deliver the rewrite without inventing sources
- `audit-only`: point out the missing source/attribution rather than pretending it's confirmed
- `rewrite-with-placeholder`: keep the argument slot but expose "source to be added here"; if not `annotation mode`, deliver a rewrite with the placeholder cue

Only for high-risk false positives, add one very short note, e.g.:

- `Kept the system subject and terms to avoid distortion.`
- `Only a light edit here, to avoid turning a formal notice into a chat post.`

## 8. Required reread checks

Before submitting a rewrite, always split the reread into two passes, don't mix them:

### Pass 1 | Fidelity reread

Check these 5 first:

1. Whether protected spans drifted
2. Whether information was lost
3. Whether register is consistent
4. Whether terminology got distorted
5. Whether the edits produced an abrupt break

If deleting a sentence leaves a paragraph with no landing, rebuild one factual sentence from information already in the original; don't add a slogan sentence. If the original has no usable information, add nothing — better a shorter paragraph.

Extra checks under `bounded / in-place` scope:

- Information retention first: every information point in the original (fact, number, judgment, action) must be traceable in the output — this is a hard metric
- `in-place`: if output word count drops below 85% of the original, roll back and check for accidentally deleted, merged, or compressed sentences (in-place should delete no whole sentence)
- `bounded`: word count drops because whole empty sentences are removed, no hard floor; but confirm each deletion-list item is a pure empty sentence that "loses no information", with no real sentence or rhythm-bearing repetition mixed in
- If sentence count changes by more than ~10%, roll back and check for sneaked-in unconfirmed structural edits
- Key factual sentences, transition sentences, and rhythm-bearing repetition must not be deleted just for "looking like a template"

### Pass 2 | Residual Audit

Only when pass 1 already preserved the facts but it still reads slightly AI. Pass 2 always checks only these 5 things:

1. Opener residue: still using cue layers like `Vorweg / Kurz gesagt / Es ist wichtig zu beachten`
2. Summary residue: still using empty endings like `Alles in allem / Letztendlich / Zusammenfassend`
3. Narrator residue: still explaining "what this shows" instead of stating the fact or judgment directly
4. Empty-judgment residue: still writing `die Richtung stimmt / von großer Bedeutung / hat den Nutzer wirklich verstanden`
5. Uniform sentence length: every sentence about the same length, evenly polished

Pass 2 allows only light fixes:

- Delete one residual opener or ending
- Merge two over-uniform factual sentences, or break one overloaded sentence
- Push one narrator / empty-judgment sentence back to direct expression

Don't do these in pass 2:

- Don't rewrite the whole thing
- Don't add facts not in the original
- Don't change terms, params, commands, errors, or attribution for "sounding more human"

Conservative scene strategy:

- `public-writing` and AI-heavy `chat` more often need pass 2
- `docs / status / code-context` are more conservative by default; if pass 2 would make the tone colloquial, advertise-y, or hurt fidelity, stop at pass 1

## Reference navigation

- This file can stand alone as a fallback; the full mode is `SKILL.md` + `references/` working together
- To see "what counts as more human": read [Positive Style Contract](./references/positive-style.md)
- To see which numbers, quotes, commands, params must not drift: read [Protected Spans](./references/protected-spans.md)
- For high-frequency German phrases: read [German Banned Phrases](./references/phrases-de.md)
- For high-frequency English phrases: read [English Banned Phrases](./references/phrases-en.md)
- For sentence- and paragraph-level structural problems: read [Structural Anti-patterns](./references/structures.md)
- To calibrate hit rules by `Tier 1 / 2 / 3`: read [Severity](./references/severity.md)
- For how to act on a specific symptom: read [Operation Manual](./references/operation-manual.md)
- To confirm what must not be touched in a scene: read [Scene Guardrails](./references/scene-guardrails.md)
- To calibrate the false-positive boundary or run a static regression: read [Boundary Cases](./references/boundary-cases.md)
- For scenario samples (high-fidelity synthetic, acceptance is "can it ship as-is"): read [Scenario Samples](./evals/real-samples.md)
- For default rewrite vs `annotation mode` side by side: read [Rewrite Examples](./references/examples.md)
- For a variant not in the phrase tables: read the "variant merging" rule in [Operation Manual](./references/operation-manual.md) first, then decide whether to add an entry

Default practice: use this file for the main calls (scene, Tier, level, output contract), then read `references/` by problem type; only in single-file installs do you stay on this file's fallback rules.
