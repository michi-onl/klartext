# Positive Style Contract

> The goal is not just to scrub AI phrases clean, but to pull text back to "a specific person saying this thing" in the current scene.

This document defines positive targets. It is not a new house style, and it is not a voice-fitting protocol.

It solves:

- After scrubbing phrases, the text is still too flat, too even, too much like "cleaned-up AI"
- Adding emotion or detail to "sound more natural" makes the text fake
- Every scene gets flattened into one "smart, smooth, summarizing" voice

Order of use:

1. Detect the scene per `SKILL.md`, confirm the main register and no-touch boundary
2. Read [Protected Spans](./protected-spans.md), circle the no-drift content
3. Judge Tier and level
4. Then use this positive contract to judge "what counts as more human"

## 1. Anti-goals

This contract does not pursue:

- Don't force colloquialism
- Don't manufacture a personal voice
- Don't polish every sentence smooth
- Don't manufacture "humanness" with punchlines, rhetorical questions, choppy fragments, or lyricism
- Don't add facts not in the original for the sake of concreteness

## 2. Positive targets

Rewritten text should lean toward these 5:

### 2.1 Concrete action over abstract inflation

Prefer who did what, what changed, what was seen — not empty shells like "Leistungssteigerung", "Wertfreisetzung", "grundlegende Neugestaltung".

Better:

> Den Cache von lokalem LRU auf Redis umgestellt, damit der App-Speicher zu Spitzenzeiten nicht mehr volläuft.

Not good enough:

> Cache-Layer erfolgreich modernisiert, was die Systemstabilität und Gesamtresilienz deutlich steigert.

### 2.2 Real subject and action over posture layer

Prefer to keep the subject and action carrying the fact; write less "wir müssen tiefer nachdenken", "wir fangen das sauber auf".

Better:

> Ich habe zuerst die zwei Fehlerpfade abgeglichen, beide sind derselbe Timeout.

Not good enough:

> Wir haben die zentralen Phänomene abgeglichen und werden als Nächstes die Kernstrecke sauber auffangen.

### 2.3 Rhythm may be natural, don't make the whole paragraph even

Natural expression allows slight asymmetry: some sentences shorter, some a bit expanded. Don't make every sentence the same length, same lift, same landing.

In long text, moderate repetition is not always filler. It may carry a transition, a pause, emphasis, or an emotional buffer. To judge whether a repetition should be cut, first check whether deleting it makes the paragraph jump; if it jumps, keep the rhythm and only handle intra-sentence template and inflation words.

Under `bounded` scope, this boundary lands on the deletion list: rhythm-bearing repetition and transitions do not go on the list; only whole empty sentences — where stripping the marker leaves nothing — go on it.

Better:

> Die Datenbank ist diese Runde schneller. Der Hauptquery fiel von 800 ms auf 120 ms, und der First Paint vorn ging von 2 s auf 0,4 s mit runter.

Not good enough:

> Dieses Update optimierte die Datenbank-Performance. Wir verbesserten die Ladegeschwindigkeit. Auch die gemeldeten Probleme wurden behoben.

The numbers in "Better" may only be written if you actually have that data. If the original has no data, adjust sentence length and order for rhythm — don't invent numbers.

### 2.4 Let plain sentences exist

Not every sentence must "sound like a conclusion". If a plain factual sentence is enough, don't add "was das zeigt" or "im Grunde bedeutet das".

Plain connecting sentences may exist in long text too. `Außerdem`, `gleichzeitig`, `das heißt`, `anders betrachtet` — if what follows is a concrete fact, experience, or judgment, don't lump them into summary endings or narrator voice. Keep the connecting role first, then check whether the sentence has empty modifiers to lower.

Better:

> Diesmal zuerst die Rechtegrenze nachgezogen, damit Gäste keine internen Seiten mehr sehen.

Not good enough:

> Das ist nicht nur ein Rechte-Fix, sondern zeigt unser tiefes Verständnis für Produktgrenzen und Sicherheit.

### 2.5 One register, don't fake another person

`chat` may be natural, but don't put on airs; `docs` may be professional, but don't perform insight; `public-writing` may have a stance, but don't sound like an announcement or a hype thread.

### 2.6 Having boundaries is more natural than performing understanding

You may be warm, but don't do the other person's psychological judgment, and don't perform "I fully get you now" as the content itself.

Better:

> Ich höre zu. Wenn du magst, erzähl weiter.

Not good enough:

> Du bist nicht zu empfindlich, du wurdest nur zu lange nicht richtig aufgefangen. Ich muss das ehrlich sagen: du bist klarer als die meisten.

## 3. Scene calibration

### `chat`

Goal:

- Sound like you're responding to the person, not delivering a statement
- Colloquial is fine, but no sycophancy, no lecture voice, no summary voice, and no psychological conclusions about the other person

Signs of better:

- Direct answer
- A responsive relationship
- A natural pause, but no dragging

### `status`

Goal:

- After reading, you know progress, problems, and next step
- Focus is timeline and result, not "completed an important upgrade"

Signs of better:

- Action and result are distinguishable
- Risk isn't lightened
- If there's a number, conclusion, or owner, you can find it at a glance

### `docs`

Goal:

- Reads like a spec, not a promo
- Domain terms stay; sentences only get necessary tightening

Signs of better:

- Search terms are still there
- Sentences are more direct, but terminology isn't scattered
- Formal specs aren't turned into chatter for "sounding human"

### `public-writing`

Goal:

- Has a stance, but the stance comes from facts and experience, not empty lift
- May have rhythm, but no hawking, no slogans, no faked depth

Signs of better:

- You can tell what the author actually wants to say
- Fewer broad words like "Zeitalter", "Wandel", "das wahre X"
- Necessary rhetoric kept, but paragraphs aren't written as poster copy

## 4. Cleaner vs more human

These pairs aren't "the one right answer"; they show where the difference is.

### A. `status`

Original:

> Diese Optimierung steigerte die Gesamtleistung des Systems erheblich und verbesserte das Nutzererlebnis effektiv.

Cleaned but still AI-ish:

> Diese Optimierung steigerte die Systemleistung und verbesserte das Nutzererlebnis.

More human:

> Diesmal vor allem die Query-Strecke geändert. Die Startseiten-API fiel von 800 ms auf 120 ms, und die Ruckler-Meldungen von vorher sind deutlich weniger geworden.

Difference:

- The first version only weakened the exaggeration
- The second says concretely "what was improved"

### B. `docs`

Original:

> Diese Fähigkeit ist keine simple Konfigurationsoption, sondern ein zukunftsweisender, systemischer Mechanismus.

Cleaned but still AI-ish:

> Diese Fähigkeit ist keine simple Konfigurationsoption, sondern ein systemischer Mechanismus.

More human:

> Das ist keine einzelne Config-Option. Sie ändert Cache-Strategie, Retry-Logik und Timeout zusammen.

Difference:

- The first version keeps the inflation skeleton
- The second explains directly what it actually touches

### C. `public-writing`

Original:

> Wahre Wettbewerbsfähigkeit ist nicht Feature-Masse, sondern das Detail im Erlebnis.

Cleaned but still AI-ish:

> Wettbewerbsfähigkeit liegt nicht in der Feature-Masse, sondern im Detail.

More human:

> Egal wie schnell du Features nachschiebst — wenn die Latenz hoch ist, die Führung chaotisch und die Fehlermeldungen unverständlich, bleiben die Nutzer trotzdem nicht.

Difference:

- The first version only shortened the sentence
- The second lands the judgment on concrete experience

## 5. Final check

Before submitting, ask yourself these 5:

1. Is this passage stating the thing, or still performing "I'm great at summarizing"
2. Do the key judgments land on an action, result, example, or condition
3. Are the sentences smooth but not flattened into one voice
4. In this scene, was the formality broken
5. If "sounding more human" requires adding a new fact, this step should stop

If scrubbing leaves only an empty frame, don't add a slogan — prefer to add a factual sentence.
