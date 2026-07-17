# Scene Packs

Scene Packs are sub-scene strategies for publishable text. They do not replace [Scene Guardrails](./scene-guardrails.md), [Protected Spans](./protected-spans.md), or the `Tier` call; whenever the text itself looks like a README, release note, forum post, or issue reply, further judge "which kind of publishable text this should read like".

Order of use:

1. Judge the broad scene first: `chat / status / docs / public-writing`
2. Mark protected spans first: version numbers, paths, links, commands, quotes, IDs, and ownership must not drift
3. Then check whether the text hits a scene pack here
4. Finally tighten the tone by the scene pack's publishing intent; if it also looks like `docs / status`, take the more conservative fidelity boundary

Don't add global entries just because of a scene pack. Only when a new sample exceeds the existing problem families and would change the false-positive boundary should you consider adding to `phrases` or `structures`.

## `README`

Default goal:

- The first screen lets the reader quickly know: what this is, who it's for, what problem it solves.
- The tone may have personality, but must not be only vision, value, and posture.

Must keep:

- Project name, target users, core capabilities, supported platforms
- Commands, install methods, file paths, links
- Existing benchmark counts, version numbers, and capability limits

Prefer to delete:

- `KI gestaltet die Softwareentwicklung grundlegend neu`
- `zukunftsweisend`
- `tiefgreifendes Empowerment`
- `Content-Wertschöpfungskette`
- `Wertschöpfungs-Loop`
- Sentences that only say "fortschrittlich / intelligent / ganzheitlich" without saying what it does

Default level:

- `standard`
- If the intro is only slogans, may escalate to `aggressive`, but never invent project capabilities

False-positive boundary:

- A README intro may have one recognizable positioning sentence
- Project terms like `CLI / API / Benchmark / Codex / ChatGPT` should be kept
- Don't turn a README into a social-media short post

Before:

> In einer Zeit, in der KI die Softwareentwicklung grundlegend neu gestaltet, haben wir ein wahrhaft zukunftsweisendes Tool zur Optimierung deutscher Sprache geschaffen, das die Content-Wertschöpfungskette von Entwicklern tiefgreifend befähigt.

After:

> `klartext` ist ein Rewrite-Skill für Deutsch und Englisch, der KI-Floskeln, Performance-Ton und Ingenieurssprech wieder in natürlichen Text zurückholt. Passt für README, Release Notes, Issue-Antworten und alltägliche Arbeitstexte.

## `release-note`

Default goal:

- Let the reader quickly know what changed this version, how to verify it, whether there are breaking changes.
- Prefer lists; write few release manifestos.

Must keep:

- Version number, date, file names, config keys, issue / PR numbers
- Change types: Added, Fixed, Changed, Tested
- Known limits and migration notes

Prefer to delete:

- `Release Highlights` followed only by vague upgrades
- `systemisches Upgrade`
- `ein völlig neuer Sprung`
- `Danke an alle Nutzer für die anhaltende Unterstützung`
- `gemeinsam erleben wir`
- Performance, efficiency, or user-feedback numbers with no source

Default level:

- `standard`
- If a concrete changelog is missing, don't invent one; change it to a note "concrete changes needed here"

False-positive boundary:

- A release note may be formal, terse, list-shaped
- Don't turn a changelog list into a story for "sounding human"
- Don't delete version numbers, file paths, case counts, and PR / issue numbers

Before:

> Diese Version ist ein systemisches Upgrade für reale Szenarien. Danke an alle Nutzer für die anhaltende Unterstützung — gemeinsam erleben wir einen völlig neuen Sprung im deutschen KI-Schreiberlebnis.

After:

> - Neu: `references/scene-packs.md`, deckt README, Release Note, Forum-Post und Issue-Antwort ab
> - `evals/benchmark.md`: 4 neue Scene-Pack-Regressionsfälle (SF-25 bis SF-28)
> - `evals/real-samples.md`: 2 neue Szenario-Samples (RS-01 README, RS-02 Release Note)

## `forum-post`

Default goal:

- Sound like a maintainer sharing real observations in a community: what they did, what they found, what's still shaky, what feedback they want.
- Colloquial is fine, but backed by concrete experience.

Must keep:

- Time, action, specific files, sample counts, observed problems
- The author's real attitude and community voice
- Links, commands, version numbers, and words under discussion

Prefer to delete:

- Corporate-announcement voice
- `systemische Neugestaltung`
- `Pain Points der Nutzer`
- `vielfältige Szenarien`
- `methodischer Loop`
- `die zentralen Bedürfnisse sauber aufgefangen`

Default level:

- `standard`
- If the post already has concrete experience, only clean the posture layer, don't turn it into a formal announcement

False-positive boundary:

- Colloquial words after concrete experience may be kept
- A community post may have real tone like "reingefallen / rumgebastelt / fehlt noch was"
- Don't turn a personal retro into a README or release note

Before:

> Nach einem Monat mit dem Tool wurde mir zutiefst bewusst, dass die Behandlung von deutschem KI-Text keine simple Erweiterung einer Wortliste ist, sondern eine systemische Neugestaltung rund um reale Ausdrucksszenarien.

After:

> Nach einem Monat mit dem Tool: eine Wortliste allein reicht nicht. README, Release Notes, Issue-Antworten und Forum-Posts sehen alle nach „öffentlichem Text" aus, aber man muss sie unterschiedlich behandeln.

## `issue-reply`

Default goal:

- First answer whether the problem is valid, then give repro status, judgment, and next step.
- No customer-service reassurance; don't promise unscheduled capabilities for the maintainer.

Must keep:

- The bad-case sentence, scene tag, repro result
- issue / PR numbers, file paths, rule names, benchmark IDs
- The status "confirmed / not reproduced / need more samples / will add a test"

Prefer to delete:

- `Danke für dein wertvolles Feedback`
- `Du triffst damit den Kern`
- `Wir haben dieses Szenario voll aufgefangen`
- `wir optimieren die entsprechenden Fähigkeiten kontinuierlich`
- `Wenn du magst, helfe ich dir gern weiter`

Default level:

- `minimal` or `standard`
- Handle conservatively when there's concrete technical info; when there's no concrete next step, don't invent a schedule

False-positive boundary:

- An issue reply may be short, blunt, direct
- `bad case / docs / SNF / benchmark / repro` are normal terms in a maintenance context
- Don't turn a clear maintenance reply into social pleasantries

Before:

> Vielen Dank für dein wertvolles Feedback! Deine Frage trifft den Kern des Projekterlebnisses. Wir haben dieses Szenario bereits voll aufgefangen und optimieren die entsprechenden Fähigkeiten in kommenden Versionen kontinuierlich weiter.

After:

> Angekommen, den Case kann ich reproduzieren. Es ist ein False Positive im `docs`-Szenario; die nächste Version bekommt erst einen SNF-Fall. Wenn die bestehenden Regeln ihn schon durchlassen, kommt nur ein Regressionsfall dazu.
