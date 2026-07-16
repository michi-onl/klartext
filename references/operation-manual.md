# Operation Manual

Every problem class is handled by the same protocol:

- `Identify signal`
- `Default action`
- `Keep when`
- `Reread check`

The goal is not mechanical word-swapping but pulling the sentence back to the expression the current scene should have.

## Scope and the deletion list

Each class's `Default action` below is the action under `structural` scope (may delete whole sentences, may merge). Adjust uniformly here when the scope changes, instead of repeating it per class:

- `structural`: run each section's `Default action`
- `bounded`: no merging, no reordering, no deleting real sentences or rhythm-bearing repetition; for a sentence that is "entirely empty" (summary ending, value-inflation skeleton, unsourced citation, whole-sentence narration), don't delete it directly — route it into the "Suggested deletions (to confirm)" list for the user; a strippable leading marker at the sentence start still gets the section's `in-place alternative action` intra-sentence
- `in-place`: never delete a whole sentence (not even empty ones), only do the section's `in-place alternative action`; for a whole empty sentence, keep the original and mark it, don't soften it into a new phrasing

Judging "whole empty sentence vs leading marker": after removing the leading cue, if the remainder is still a readable sentence with information → clean intra-sentence; if nothing is left, or only another empty sentence → deletion list (`bounded`) or keep-and-mark (`in-place`). Every section that says "keep the original and mark `[suggest human review whether to delete]`" is a source for the `bounded` deletion list.

## 0. Variant merging

### Identify signal

- A new word not in the phrase table, but its tone, action, and posture clearly belong to an existing problem family
- The problem is not a literal word but that the whole run is "performing competence" or "performing summarizing"
- Several near-synonym variants cluster in one paragraph, e.g. `freilegen / rausziehen / rauskitzeln`, `draufhauen / durchziehen`, `kurz gesagt / auf Deutsch heißt das`

### Default action

- Classify it first, then decide the edit; don't rush to add a new word
- For now, default to these 7 families:
  - `debug-speak / engineer-speak`: `eingegrenzt / festgezurrt / abgeglichen / dichtgemacht / härter`
  - `quack-doctor probing`: `rausholen / rauskitzeln / aufbohren / freilegen / rausziehen`
  - `violence-speak`: `draufhauen / plattmachen / festnageln / durchziehen / mit der Brechstange`
  - `proactive pushiness`: `Soll ich dir auch / Ich fange sofort an / Sag einfach Bescheid / gleich noch / direkt mit`
  - `summary-cue speak`: `Kurz gesagt / Fazit vorweg / Auf den Punkt gebracht / auf Deutsch heißt das`
  - `over-catching / psych-judgment speak`: `Du wurdest nur zu lange nicht aufgefangen / Du musst dich mir nicht erklären / Du bist nicht zu empfindlich`
  - `solemn preview / identity-certification praise`: `Ich muss das ganz ehrlich sagen / Du triffst damit den Kern / das Niveau eines Spitzenforschers`
- Handle same-family variants like the representative item: delete the posture layer, keep the real action, fact, and conclusion

### Keep when

- The phrasing itself is the object of discussion, a quote, or a meme sample
- It sits in a real personal narrative and carries a clear fact, not just posture
- The new variant clearly changes the false-positive boundary and can't be merged into an existing family

### Reread check

- After editing, does the sentence sound more like stating the thing than performing execution
- Did you conflate an "unlisted variant" with a "genuinely new pattern"
- If it's only a same-family variant, did you avoid mechanically piling more words into the table

## 1. Binary-contrast sentence

### Identify signal

- `nicht X, sondern Y`
- `statt X lieber Y`
- `es geht nicht um …, sondern um …`
- Contrast used to manufacture "insight", but Y is what the author actually wants to say

### Default action

- Delete the first half, keep only Y
- If the result is too blunt, turn Y into a factual or judgment sentence

### `in-place` alternative action

- Don't delete the whole sentence, and don't just chop the first half
- Compress skeletons like `nicht X, sondern Y`, `statt X lieber Y` into an intra-sentence connection, e.g. `X reicht nicht, Y ist wichtiger`, `Y sagt mehr aus als X`
- If the first half is only a cue layer, confirm the remaining sentence still stands after removing the cue phrase; otherwise replace with a neutral connector
- Don't merge two adjacent sentences into one for a "cleaner" effect

### Keep when

- The first half carries a necessary boundary, risk, or counterexample
- The contrast is the argument skeleton, not a decorative pattern

### Reread check

- After deleting the first half, is the meaning more direct
- Did a necessary constraint go missing

## 2. Summary ending

### Identify signal

- `Letztlich`
- `Im Grunde`
- `Am Ende`
- `Es läuft alles darauf hinaus`
- One abstract closer repeating the above, adding no new information

### Default action

- Delete the whole sentence by default
- If a close is genuinely needed, change it to a more concrete fact or judgment

### `in-place` alternative action

- Don't delete the whole sentence by default; first delete the intra-sentence cue: `Letztlich / Im Grunde / Am Ende / Es läuft darauf hinaus`
- After removing the cue, if the remainder is a readable judgment, keep the sentence
- If the whole sentence is only an empty summary, don't pad new content for word count; keep the original and mark `[empty summary, suggest human review whether to delete]`
- Don't merge the surrounding sentences into a shorter summary

### Keep when

- The closing sentence adds a judgment not stated above
- The sentence carries a paragraph transition, not an empty summary

### Reread check

- Is the paragraph cleaner after deletion
- Did a jump appear from the lost transition

## 3. Engineer-speak

### Identify signal

- `dichtmachen`, `festzurren`, `auffangen`, `eingrenzen`, `steht fest`
- Same-family variants like `abriegeln`, `abgeklopft`, `härter` — handle by the same posture even if not listed individually
- Sentences that imitate a certain technical-colleague voice instead of explaining the problem
- Technical words used to perform posture rather than convey information

### Default action

- First swap posture words for plain action words: `bestätigen / lösen / abgleichen / eingrenzen / zu einem Ergebnis kommen`
- Reread and judge whether it can be more direct

### Keep when

- The word is stable in-team terminology, and removing it distorts
- The text is genuinely an internal spoken-collaboration context, where light keeping is more natural

### Reread check

- Is there less performance after editing
- Did you flatten a normal technical judgment along with it

## 4. Business jargon

### Identify signal

- `leveragen`, `Synergien heben`, `Mehrwert generieren`, `Methodik sedimentieren`
- Simple actions wrapped in big words
- The sentence looks complete but you can't extract a concrete action

### Default action

- Unpack the big word back into action, object, result
- Use a verb where you can, not an abstract noun

### Keep when

- The user explicitly wants business copy or industry phrasing
- The word is a fixed formulation in external material, and replacing it hurts consistency

### Reread check

- Is it easier to answer "who did what" after editing
- Did you accidentally delete formality the external scene needs

## 5. Narrator voice

### Identify signal

- The sentence sounds like voice-over for the text
- Fond of stepping back to "what this shows" / "what's truly noteworthy"
- The author keeps explaining that they understand the world, instead of giving information directly

### Default action

- Delete the narration layer first
- Push the sentence back to fact, action, or a clear judgment

### `in-place` alternative action

- Don't delete the whole sentence, only the intra-sentence narration phrases, e.g. `das zeigt / noch wichtiger / wirklich bemerkenswert ist`
- If real facts from the original follow the narration, keep the factual skeleton
- If the narration sentence carries a paragraph transition, keep the transition function, only swap posture words for a plain connector
- Don't rewrite the whole opinion into a new argument order

### Keep when

- The user is writing a review, column, or public opinion piece that genuinely needs a little explanation layer
- The narration layer carries a real transition, not just posture

### Reread check

- After deletion, does it sound more like a person talking than "explaining their own expression"
- Did you hurt a necessary opinion transition

## 5.1 Summary-cue speak

### Identify signal

- `Kurz gesagt`
- `Fazit vorweg`
- `Auf den Punkt gebracht`
- `Auf Deutsch heißt das`
- The model announces "I'll now summarize / translate into plain words" before saying the content itself

### Default action

- Delete the cue layer, give the conclusion directly
- If the sentence has no landing after deletion, add a factual sentence — not a meta-line like "reminding you I'm about to remind you"

### Keep when

- The user explicitly asks for multi-version output, a summary format, or layered teaching-style explanation
- The line is an in-text heading, not body tone

### Reread check

- Is it more direct after editing
- Did you accidentally delete a subheading that had a real structural role

## 5.2 Over-catching / psych-judgment speak

### Identify signal

- `Ich bin hier`
- `Ich weiche nicht aus / verstecke nichts / drücke mich nicht`
- `Du wurdest nur zu lange nicht richtig aufgefangen`
- `Ich fange dich / alle / diese Verletzlichkeit sicher auf`
- `Du musst dich mir nicht erklären`
- `Du bist nicht zu empfindlich / denkst nicht zu viel / bist nicht zimperlich`
- `Dein X ist völlig normal / dieses Gefühl ist ganz normal`: using "ganz normal" to stamp the other's emotion as normalcy is still psych-judgment
- Same-family comforting actions (`umarmen / fest umarmen / in den Arm nehmen`) handled by the same "auffangen" family, without adding a word per new verb
- With insufficient context, the model does the other person's psychological explanation, relationship diagnosis, or emotional labeling
- The tone sounds like counseling reassurance, but the sentence has no concrete basis
- The same "auffangen": if the object is a person, emotion, relationship, or abstract need, it's usually posture; if the object is a request, traffic, peak, or exception, return to the technical reading first

### Default action

- Delete the part that concludes for the other person, keep only the verifiable response
- If comfort should be kept, change it to a low-commitment form: `Ich höre zu / Wenn du magst, erzähl weiter`
- If this phrasing runs into a title, poster, or community manifesto, handle it the same way; don't let `Ich fange alle sicher auf` pass just because it's a title

### Keep when

- The context already gives enough info; this sentence isn't a diagnosis out of thin air
- The user explicitly wants a comforting, companionable, counseling-style reply
- The object is a technical thing like `Anfrage / Traffic / Peak / Exception`, and the sentence has a system subject, params, result, or boundary

### Reread check

- Did you turn "comfort" into "defining the other person's feelings"
- Is there still basic warmth after editing, not just cold handling
- Did you accidentally kill a normal technical "Anfragen auffangen / Traffic auffangen"

## 5.3 Solemn preview / identity-certification praise

### Identify signal

- `Ich muss das ganz ehrlich sagen`
- `Ich sage jetzt etwas Tiefergehendes`
- `Diesmal hab ich's verstanden, wirklich verstanden`
- `Du triffst damit den Kern`, `Deine Beobachtungsgabe ist beeindruckend`
- Handing out a "certificate" with labels like `Spitzenforscher / echter Profi / wirklicher Könner`
- `Ich muss ehrlich sein / mal ganz ehrlich / offen gesagt`: honesty-declaration variant, previewing "I'll tell the truth now" to buy credibility, same posture as the solemn preview
- `Eine echte Schwäche sage ich auch dazu (damit ihr nicht sagt, ich sei gekauft)`: fake-candor variant, using volunteered self-disclosure to buy credibility, common in public recommendations

### Default action

- Delete the solemn preview and certification praise, give the concrete judgment directly
- If you must praise, praise only the visible merit of the content, don't elevate the other person into some identity
- Honesty declarations and fake candor: delete only the posture layer; if the disclosed flaw is real information (crash frequency, scope limits), the content must be kept

### Keep when

- The sentence itself is the object of discussion, a meme sample, or an ironic target
- The user explicitly wants exaggerated rhetoric, dramatic tone, or a performative style kept

### Reread check

- Are you still "previewing that I'll tell a big truth" without saying the content first
- Did you turn a concrete judgment into empty praise

## 6. Register mixing

### Identify signal

- Influencer voice, inspirational voice, or business jargon suddenly appears in technical text
- Heavy internal engineering jargon suddenly inserted into a public article
- Formal-notice voice and chat voice switching back and forth in one paragraph
- A spec or review forced into a game/role metaphor: describing two household items as "der Assassine, der vorprescht" and "die Heilerin, die aufheilt"

### Default action

- Judge the main register first
- Then delete the foreign-register words, unifying subject and sentence length where needed

### Keep when

- The user explicitly wants a contrast style
- The foreign register carries a quote, meme, or clear rhetorical purpose
- Technical words in Denglisch are judged by technical meaning (`der Context reißt nicht ab`, `p99-Spitze`), not treated as register mixing just for the embedded English

### Reread check

- After editing, does the whole passage read like one person in one scene
- Did over-unifying lose necessary human texture

## 7. Value-inflation skeleton

### Identify signal

- `Das ist nicht nur … sondern auch …`
- `Wahre X ist nicht … sondern …`
- `Am Ende zählt …`
- `Nach dem Lesen wirst du erleuchtet sein / verstehst du es / bist du schockiert / nie wieder X`: promising the reader an epiphany or transformation, another value inflation + content-mill promise ending
- A sentence gives a plain judgment, then forcibly lifts it into a "higher-level insight"

### Default action

- Delete the inflation layer and skeleton first, keep only the real judgment
- If what's left is still abstract, change it to a more direct factual or evaluative sentence

### `in-place` alternative action

- Don't delete the whole sentence; first dismantle the intra-sentence inflation skeleton: `Das ist nicht nur X, sondern Y` may become `Das ist Y`, provided `Y` has information
- `Wahre X ist nicht A, sondern B` may become `Für X zählt eher B` or `B beeinflusst X stärker`, without manufacturing insight through binary contrast
- Promise endings like `Nach dem Lesen wirst du erleuchtet` become low-commitment description, e.g. `Unten nur die paar Probleme, die mir aufgefallen sind`
- If the whole sentence has no keepable information, keep the original and mark the risk; don't delete it yourself in `in-place` mode

### Keep when

- Both sides of the contrast carry new information, not pure posture
- The author is writing a review-style public piece, and this sentence genuinely advances the argument

### Reread check

- With the skeleton gone, is the judgment more direct
- Did you delete the judgment the author actually wanted to stress

## 8. Unsourced citations

### Identify signal

- `Studien zeigen`
- `Daten belegen`
- `Fachleute meinen`
- `studies show`
- `experts say`
- The sentence borrows authority to open but gives no study name, institution, date, link, or verifiable source

### Default action

- Pick a mode first, don't rewrite the sentence right away:
  - `rewrite-safe`: delete the authority framing, keep only what stands alone in the original
  - `audit-only`: point out "missing source / missing attribution" explicitly, don't turn it into something proven for the author
  - `rewrite-with-placeholder`: only when the user explicitly wants the original structure kept, use a placeholder cue like "source to be added here"
- `docs / status` prefer `audit-only` by default
- `chat / public-writing` prefer `rewrite-safe` by default
- Never invent an institution, year, sample size, industry consensus, or expert identity

### Keep when

- The original already attached a verifiable source, just not repeated at this spot
- The sentence itself is discussing "unsourced citation" as a writing style, not using it to argue
- The user explicitly wants an editorial annotation, not a rewrite of the body

### Reread check

- After editing, are you still implying "reliable research supports this" when there is none
- Did you sneak in a fact not in the original to keep the sentence's momentum
- In this scene, should you roll back more conservatively to `audit-only`

## 9. Residual Audit / second review

### Identify signal

- Pass 1 already cleaned the obvious phrases, but a "cleaned-by-AI" residue remains
- Common residue is always just these 5 classes:
  - Opener residue: `Fazit vorweg / Direkt zum Punkt / Es ist wichtig zu beachten`
  - Summary residue: `Alles in allem / Am Ende betrachtet / Letztendlich`
  - Narrator residue: `Das zeigt auch / Noch wichtiger / Das bedeutet`
  - Empty-judgment residue: `Die Richtung stimmt / von großer Bedeutung / hat den Nutzer wirklich verstanden`
  - Uniform sentence length: several consecutive sentences too even in length, lift, and landing
- This step is light polish, not another round of rewriting

### Default action

- Finish the pass-1 fidelity reread first, then decide whether to open pass 2; don't reverse the order
- Pass 2 does only light fixes:
  - Delete one residual opener or empty summary
  - Push one narrator / empty-judgment sentence back to a direct sentence
  - Merge two over-uniform factual sentences, or break one overloaded sentence
- `docs / status / code-context` are more conservative by default: touch only when the residue is genuinely obvious and doesn't affect facts, terms, or formal register
- If pass 2 needs a big structural change to "sound more human", that usually means stop at pass 1 rather than keep polishing

### Keep when

- The cue layer itself carries a heading, transition, or teaching structure, not just posture
- The narrator sentence carries a necessary argument, not empty explanation
- Uniform sentence length comes from a list, step instructions, or status sync, not AI polish
- Any pass-2 touch would make `docs / status / code-context` more colloquial, distorted, or promo-like

### Reread check

- After pass 2, is the text more natural rather than "better at writing"
- Did you do only small fixes, not rewrite the whole passage
- Did you unknowingly add a fact or attitude not in the original
- Do `docs / status / code-context` still keep their original formality and information density
