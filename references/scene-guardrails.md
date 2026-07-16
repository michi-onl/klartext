# Scene Guardrails

Detect the scene first, then decide what must not be touched. Removing template feel does not mean flattening every text into one voice.

Whenever `references/` is readable, use [Protected Spans](./protected-spans.md) to mark the no-drift spans first, then narrow the rewrite scope by the per-scene no-touch items here.

This file defines only the broad scene boundaries. For finer publishing scenes — README, release note, forum post, issue reply — even when the first call looks like `docs` or `status`, also read [Scene Packs](./scene-packs.md) while keeping the more conservative fact and terminology boundaries here.

## `chat`

Goal:

- Natural, direct, responsive

Default level:

- `minimal`

Unsourced-citation default:

- `rewrite-safe`

Don't touch:

- Don't make the reply harder just to "de-AI" it
- Don't inflate tone or add value judgments out of nowhere
- Don't turn a simple response into a summing-up
- Don't do the other person's psychological analysis, relationship diagnosis, or empty reassurance

Prefer to keep:

- Conversational rhythm
- Concrete responsiveness
- Reasonable colloquial pauses
- Original quotes the user explicitly asked to keep

## `status`

Goal:

- High fact density; after reading you know progress, problems, next step

Default level:

- `minimal` or `standard`

Unsourced-citation default:

- `audit-only`

Don't touch:

- Don't delete the timeline
- Don't delete ownership/attribution
- Don't lighten the risk
- Don't sacrifice reporting efficiency to "sound human"

Prefer to keep:

- Time, action, result, risk, blockers
- Numbers, dates, ranges, and ownership

## `docs`

Goal:

- Searchable, reproducible, citable

Default level:

- `minimal`

Unsourced-citation default:

- `audit-only`

Don't touch:

- Don't break terminology stability
- Don't change search terms, commands, API names, field names
- Don't sacrifice system subjects and imperative instructions for colloquialism
- Don't turn a formal spec into chatter

Prefer to keep:

- Terminology
- System-behavior subjects
- Step order
- Constraints
- Commands, paths, params, fields, errors, and status codes

## `public-writing`

Goal:

- Consistent register, has a stance without posturing

Default level:

- `standard`

Unsourced-citation default:

- `rewrite-safe`

Don't touch:

- Don't manufacture exaggerated judgments for rhythm
- Don't turn restrained writing into influencer hype
- Don't force punchlines
- Don't turn a formal announcement into a social-media comment

Prefer to keep:

- The author's original stance
- Normal formality
- Necessary rhetorical rhythm
- Existing facts, attribution, and verifiable citations

Long-form note:

- Long German text (roughly 1000+ words) defaults to `bounded` scope, especially opinion pieces, retros, reviews, and public text with paragraph rhythm: clean real sentences intra-sentence, route whole empty sentences into a "Suggested deletions (to confirm)" list for the user, no merging, no reordering
- When the user explicitly asks "exactly as-is / delete nothing / strictly keep sentence count", or reports that `bounded` still cut too much, switch to the stricter `in-place` (even whole empty sentences are not deleted, only lowered intra-sentence)
- When the prompt contains signals like `keep the length / don't shrink / word count / rhythm / don't delete / as-is as possible`, treat as long-form even if under 1000 words
- Under `bounded / in-place`, never compress a paragraph into a short summary; keep paragraph rhythm and transition-bearing repetition first — the only difference is whether whole empty sentences "go to the deletion list" or "stay and get lowered intra-sentence"

## Mixed scenes

If a passage hits several scenes at once:

1. Judge the main purpose first
2. Mark protected spans first, then cap the rewrite by the main scene's no-touch items
3. Clean only clearly jarring words in the secondary scene; don't chase absolute purity
