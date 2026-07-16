# Protected Spans

> Before chasing "more human", lock down the spans that must not drift.

This document expands the no-touch principles in `SKILL.md` into an executable pre-check list. It uses an in-prompt checklist; it does not require a separate `facts ledger` format.

Order of use:

1. Detect the scene
2. Scan protected spans first
3. Then delete/merge sentences, change subjects, lower register
4. On reread, check each protected-span class is still there

## 1. Protect first

Protect first, rewrite second. Spans to mark out by default:

### 1.1 Numbers, dates, ranges, units

- Numbers
- Percentages
- Times
- Dates
- Version numbers
- Ranges
- Units

Default rules:

- Don't change values
- Don't round casually
- Don't turn a precise statement into a vague one
- Don't add a comparison the original didn't have

### 1.2 Names and attribution

- People's names
- Organization names
- Product names
- Module names
- Service names
- issue / PR / RFC numbers
- The responsible subject and attribution of opinions

Default rules:

- Don't change the subject
- Don't blur "who did it / who said it / who owns it"
- Don't turn the author's own judgment into something others supposedly proved

### 1.3 Quoted text and titles

- Text inside quotation marks
- Citation format
- Article titles
- Report names
- Key words from the original quote

Default rules:

- Keep quoted content as-is by default
- Edit inside quotation marks only when the user explicitly asks
- Don't paraphrase a quote and stuff it back inside quotation marks

### 1.4 Commands, code, params, fields, paths

- Commands
- Code blocks
- API names
- Parameter names
- Field names
- Config keys
- File paths
- Environment variables

Default rules:

- Keep spelling, case, symbols, underscores, hyphens
- Don't translate code semantics
- Don't turn technical spans outside comments into plain language

### 1.5 Errors, logs, statuses, metrics

- Error messages
- Raw log text
- HTTP status codes
- Metric names
- Experiment results
- Monitoring values
- Metric relationships in conclusions

Default rules:

- Don't change the error type
- Don't drop time range, sample range, or comparison baseline
- Don't turn "observed" into "proven"

### 1.6 German register and address form

- Sie vs du (formal vs informal address)
- Grammatical gender when it carries attribution
- Regionally/legally fixed formulations (e.g. official notices, Impressum text)

Default rules:

- Don't silently flip Sie ↔ du; if the register is inconsistent in the original, ask or keep the dominant one
- Don't "gender-neutralize" or "de-neutralize" beyond what the user asked

## 2. What may change around them

Outside protected spans, these can usually change:

- Throat-clearing openers
- Summary endings
- Business jargon
- Narrator voice
- Posture layer
- Empty-judgment wrapping

Actions you can take:

- Delete filler before/after a span
- Adjust sentence order without changing factual relationships
- Push an abstract conclusion back to a concrete action
- Merge repeated sentences without swallowing a protected item

If a sentence can only become natural by changing a protected span, prefer fidelity — accept a little stiffness.

## 3. Scene notes

### `status`

Protect especially:

- Timeline
- Current judgment
- Next step
- Risk ownership
- Metrics and ranges

Don't lighten "risk", "blocked", "unconfirmed" for smoothness.

### `docs`

Protect especially:

- Terminology
- Conditions
- Order
- Commands
- Config
- System subjects

Don't sacrifice searchability for colloquialism.

### `code-context`

Protect especially:

- The code itself
- Real behavior described in comments
- Parameters
- Return values
- Constraints

You may fix AI flavor in comments, but must not change the function's behavior.

### `mixed`

Protect especially:

- Quote boundaries
- Local scene-switch points
- The original formatting of quotes, code blocks, retro blocks, notice blocks

Decide where the body is and where the quote or embedded block is before deciding which regions may move.

## 4. Worked examples

### A. `status`

Original:

> Gestern das Verbindungspool-Limit von 20 auf 100 gesetzt, die 504er sind erstmal weg. Noch 24 Stunden beobachten, wenn die Fehlerrate unter 0,1 % bleibt, gehen wir auf voll.

Protected:

- `20`
- `100`
- `504`
- `24 Stunden`
- `0,1 %`

Changeable:

- `sind erstmal weg`
- `Noch … beobachten`

### B. `docs`

Original:

> Nach `bin/migrate --tenant=prod`: erscheint im Log `schema mismatch`, zuerst prüfen, ob `DB_SCHEMA_VERSION` mit der Produktion übereinstimmt.

Protected:

- `bin/migrate --tenant=prod`
- `schema mismatch`
- `DB_SCHEMA_VERSION`

Changeable:

- `zuerst prüfen`
- the explanation layer around it

### C. `mixed`

Original:

> Der Nutzer sagt „Diesen Satz nicht ändern, so lassen". Im Fließtext nur Floskeln wie „Es ist wichtig zu beachten" rausnehmen.

Protected:

- `„Diesen Satz nicht ändern, so lassen"`

Changeable:

- the body text outside the quotation marks

## 5. Final check

On reread, verify at least these 5:

1. Did numbers, dates, units, version numbers drift
2. Was the subject, attribution, or ownership swapped
3. Were quotes, code, commands, paths, params broken
4. Were errors, status codes, metrics, comparisons loosened
5. Were facts, sources, or judgments not in the original added for "sounding human"

When unsure, keep the protected span — don't gamble.
