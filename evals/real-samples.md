# Scenario Sample Eval Pack (high-fidelity synthetic)

> These samples complement `benchmark.md`: the benchmark is synthetic, structurally clean, with an obvious symptom per case. This file targets samples that "look unremarkable as a whole, but you know they're off the moment you post them" — the final acceptance line is whether the rewrite can ship as-is.

## About the source

> **⚠️ These are high-fidelity synthetic samples.**
>
> They are not made up from nothing, and they are not transcribed from real user posts. The method is:
>
> 1. Observe the AI tics and patterns German users complain about most
> 2. Generalize the typical patterns, symptom combinations, and scene distribution
> 3. Construct each sample from those observations, pointing at no real person, project, or account
>
> Why: transcribing real posts into a public repo without permission raises attribution and compliance issues; samples written from pure model intuition drift from the real distribution. "Observe + generalize + synthesize" is the steadiest compromise.

## High-frequency German AI patterns

By observation, the phrasings and words that most expose an AI author in German:

| Category | Concrete expressions |
|----------|----------------------|
| Openers / hooks | `Fazit vorweg`, `Direkt zum Punkt`, `Jetzt kommt's`, `Klartext:` |
| Summary / close | `Zusammenfassend lässt sich sagen`, `Alles in allem`, `Am Ende des Tages`, `Letztlich` |
| Value inflation | `neu definiert`, `absoluter Gamechanger`, `der eigentliche Kern ist`, `trifft den Nerv` |
| Binary skeleton | `nicht (nur) … sondern …`, `Wahre X ist nicht … sondern …` |
| Pushy-assistant tone | `Soll ich dir das auch noch …?`, `Wenn du magst, mache ich dir direkt …`, `Ich fange schon mal an mit …` |
| Over-catching / psych diagnosis | `Ich bin hier`, `ich weiche nicht aus`, `ich fange dich sicher auf`, `du wurdest nur zu lange nicht aufgefangen`, `du bist nicht zu empfindlich`, `du musst dich mir nicht erklären` |
| Solemn preview / cert praise | `Ich muss das ganz ehrlich sagen`, `Ich sage jetzt etwas Tiefergehendes`, `du triffst den Kern`, `das Niveau eines Spitzenforschers` |
| Engineer-speak / debug-speak | `eingegrenzt`, `festgezurrt`, `auffangen`, `dichtmachen`, `Root Cause`, `End-to-End` (as posture) |
| Disclaimer voice | `Es sei angemerkt`, `Es ist wichtig zu beachten`, `Bitte beachten Sie` (30% of the passage is disclaimer) |
| Influencer / clickbait | `Leute`, `absoluter Geheimtipp`, `Gamechanger`, `durch die Decke`, `unbedingt speichern`, `ihr werdet es nicht glauben` |
| Nominalstil / officialese | `eine Optimierung vornehmen`, `zur Anwendung bringen`, `im Rahmen von`, `vor dem Hintergrund` |

When constructing samples, each hits at least 2–3 categories above to stay close to the real distribution.

## Community observation: why the "auffangen" style reads instantly as AI

By public discussion, what the community keeps complaining about is usually not a single word but a whole posture chain:

1. First announce "I'm here / I don't dodge", performing presence
2. Then give an abstract promise like "I catch you / catch everyone / catch the need"
3. Then conclude for the other person: `du bist nicht … du bist nur …`, `du triffst den Kern`
4. Finally tack on a pushy next action: `Wenn du magst, mache ich dir …`

The valuable part of this feedback: the community recognizes not a hot word but the whole "posture before information, promise over fact, emotional judgment instead of a response" style. So the maintenance strategy is not to chase hot words one by one, but:

- Abstract the pattern first: presence announcement, catching promise, psych judgment, pushy close
- Then split by object: person / emotion / relationship are more suspect by default; request / traffic / peak return to the technical reading first
- Only add a word entry when a new phrasing genuinely changes the false-positive boundary; otherwise prefer adding to `operation-manual`, `boundary-cases`, `real-samples`

Reference observation venues (public discussion, used only for generalization, not transcribed into samples): German-language tech communities such as heise Forum, r/de and r/programmieren on Reddit, ComputerBase, and Hacker News for the English side.

## Division of labor with the benchmark

| Dimension | benchmark.md | real-samples.md |
|-----------|--------------|-----------------|
| Granularity | single symptom, mostly short | whole passage, mixed symptoms, with context |
| Judgment | rule hit / false-positive guard | can it ship as-is |
| Purpose | regression, rule coverage | subjective scoring, long-term asset |
| Count | growing set | quality first |

## 3-dimensional scoring

Score the **original** 1–5 (5 best) on each dimension. Score again after the rewrite; check whether the total rose and whether "ship-ready" went from ≤2 to ≥4.

| Dimension | 1 | 3 | 5 |
|-----------|---|---|---|
| **Natural** | instantly AI: phrases, posture, rendering-word pile-up | some residual phrases or monotone rhythm | reads like a familiar person talking in this scene |
| **Faithful** | lost or invented facts, numbers, attribution, commands | facts mostly kept, one vague spot | all protected spans, facts, attribution intact |
| **Ship-ready** | posting it would make people suspect AI ghost-writing | needs another polish before posting | can be pasted straight into the channel |

**Recommended use**: score the original first as a baseline, then rewrite, then re-score. `Ship-ready` is the final metric; if `Faithful` drops below 4, it's a regression even with a perfect `Natural`.

### Long-form in-place extra scoring

When long text enters `in-place` scope, add a `Length rhythm` dimension:

| Dimension | 1 | 3 | 5 |
|-----------|---|---|---|
| **Length rhythm** | visibly shrunk, deleted transition/pause sentences | word count roughly kept, a few flattened spots | word count, sentence count, paragraph order, and key transitions kept; only intra-sentence de-flavoring |

This only applies to long-form keep-length cases, not every sample.

---

## Samples

### RS-01 | README intro | public-writing

**Original**

> In einer Zeit, in der KI rasant voranschreitet, ist die Frage, wie man ein Tool schafft, das Entwickler wahrhaft befähigt, zu einer nicht zu unterschätzenden Schlüsselfrage der Branche geworden. Dieses Projekt integriert tiefgreifend verschiedenste Spitzentechnologien und bietet Entwicklern eine ganzheitliche, nahtlose und intelligente Lösung, die dem Team zu echter Effizienzsteigerung und Kostensenkung im perfekten Loop verhilft.

**Why it reads AI**

- "In einer Zeit, in der …" era-voice opener
- Verbs are all "befähigen", "integriert tiefgreifend", "verhilft"
- Piles "ganzheitlich", "nahtlos", "intelligent", "perfekter Loop"
- Not one sentence says what the tool does

**What not to break**

- Keep the positioning (a tool for developers)
- A README first paragraph needs "what this is, who it's for" — don't scrub it to one line

**Recommended edit**

> Ein CLI-Tool für Entwickler. Einmal installiert, prüft es Commit-Messages, Issue-Antworten und PR-Beschreibungen auf KI-Ton; Absätze, die eine Regel treffen, werden markiert und mit einem Änderungsvorschlag versehen. Unterstützt aktuell Deutsch und Englisch; automatisches Umschreiben ist standardmäßig aus und muss bestätigt werden.

**Original score**: Natural 1 / Faithful 3 / Ship-ready 1

---

### RS-02 | GitHub release note | public-writing

**Original**

> ## v0.5.0 Release Highlights
>
> Diese Version ist ein zukunftsweisendes, systemisches Upgrade. Wir haben die Kernstrecke umfassend optimiert und die historischen Altlasten sicher aufgefangen. Die neue Version steigert nicht nur die Gesamtperformance deutlich, sondern realisiert auch beim Nutzererlebnis einen qualitativen Sprung. Studien zeigen, dass Teams mit ähnlicher Architektur ihre Liefereffizienz um das 3- bis 5-Fache steigern. Danke an jeden Beitragenden für den unermüdlichen Einsatz — bleiben wir gespannt auf v1.0!

**Why it reads AI**

- "zukunftsweisendes, systemisches Upgrade", "umfassend optimiert", "sicher aufgefangen" posture layer
- "nicht nur … sondern auch …" binary inflation
- "qualitativer Sprung", "unermüdlicher Einsatz", "bleiben wir gespannt" inspirational close
- "Studien zeigen … 3- bis 5-Fache" classic unsourced citation
- Not one concrete change in the whole thing

**What not to break**

- The version number `v0.5.0` must stay
- A release note needs the real changelog; don't delete the content along with the phrases

**Recommended edit**

> ## v0.5.0
>
> - Regel-Engine neu geschrieben, Einzeldatei-Scan von ~800 ms auf ~120 ms
> - Neuer Modus `--annotate-only`: nur markieren, nicht umschreiben
> - Fix: Denglisch in Docstrings wurde fälschlich als KI-Ton markiert (#42)
> - Abhängigkeit: Node 18 → 20
>
> Nächste Version baut die Scene Packs weiter aus, zuerst die Szenengrenzen für README und Release Note.

**Original score**: Natural 1 / Faithful 2 / Ship-ready 1

---

### RS-03 | short social post | public-writing

**Original**

> Leute!! Gerade ein absolutes Geheimtipp-Tool für KI-Schreiben entdeckt! Der pure Gamechanger! Ihr werdet es nicht glauben, meine Produktivität geht durch die Decke! Wer kennt's nicht — früher eine halbe Stunde für eine Release Note, jetzt in 3 Minuten fertig! Unbedingt speichern! Wichtig: der Praxis-Guide steht in den Kommentaren!

**Why it reads AI**

- The full influencer/clickbait kit: "Leute", "Geheimtipp", "Gamechanger", "durch die Decke", "unbedingt speichern", "Wichtig"
- The numbers (halbe Stunde → 3 Minuten) read low-credibility, like off-hand invention
- A short post doesn't need this much template

**What not to break**

- The loose, personal tone of a short post (don't turn it into LinkedIn voice)
- If the author really means the tool is useful, keep that core

**Recommended edit**

> Nutze seit Kurzem einen Rewrite-Skill namens klartext. Für eine Release Note hab ich vorher immer ein paar Mal drübergeschliffen, um die Floskeln rauszubekommen; jetzt geht's meist in einem Rutsch. Am besten: es ändert nichts hart, es markiert nur, was nach KI klingt, und lässt mir die Entscheidung.

**Original score**: Natural 1 / Faithful 2 / Ship-ready 1

---

### RS-04 | long forum post | public-writing / long

**Original**

> Eine Woche dran gesessen, jetzt ist das interne Doku-System endlich migriert. Ehrlich gesagt war das nicht nur eine simple Migration, sondern eine grundlegende Neugestaltung des Wissensmanagement-Paradigmas. Wir sind von der zugrundeliegenden Logik ausgegangen und haben Informationsarchitektur, Rechtesystem und Suchpfade End-to-End neu durchdacht.
>
> Zugegeben, unterwegs gab es einige Herausforderungen. Aber genau diese Herausforderungen haben uns die Bedeutung von Engineering-Denken tief bewusst gemacht. Letztlich ist wahre Wettbewerbsfähigkeit nicht die Anhäufung von Tools, sondern das Sedimentieren von Prozessen.
>
> Zum Schluss: Statt den Wandel abzulehnen, sollten wir dieses Zeitalter voller grenzenloser Möglichkeiten annehmen. Ich teile weiter regelmäßig mehr Praxiswissen — bleibt dran!

**Why it reads AI**

- Opens with "nicht nur … sondern …" + "Paradigma", "grundlegende Neugestaltung"
- "zugrundeliegende Logik", "End-to-End", "Engineering-Denken" jargon stacking
- "Zugegeben", "Letztlich", "wahre X ist nicht … sondern …" three base skeletons at once
- "Statt … sollten wir …", "grenzenlose Möglichkeiten", "teile weiter", "bleibt dran" uplifting close
- Not one concrete action in the whole post (which tool, how many docs, which pitfalls)

**What not to break**

- The post means to share experience; the core event "migrated the company doc system" must stay
- A forum post may stay a bit colloquial — don't turn it into a paper

**Recommended edit**

> Eine Woche dran gesessen, jetzt ist das interne Doku-System migriert. Wir haben Informationsarchitektur, Rechte und Suche neu aufgesetzt.
>
> Ein paar Sachen sind schiefgegangen: Die alten Deep-Links haben nach der Migration nicht mehr aufgelöst, und das Rechtesystem war anfangs zu offen — Gäste sahen interne Seiten. Beides über eine Redirect-Map und eine Default-deny-Regel gefixt.
>
> Nächstes Mal teste ich die Rechte vor dem Umzug, nicht danach.

**Note**: this is `structural` here (the author asked for a full rewrite). Under `bounded` the empty sentences ("nicht nur … sondern …", "Letztlich …", "Statt … sollten wir …") would go on a deletion list instead. The recommended edit also does not invent facts the original lacked; the added concrete pitfalls are illustrative — in a real rewrite, if the original gives no detail, keep the paragraph short rather than inventing.

**Original score**: Natural 1 / Faithful 3 / Ship-ready 1

---

### RS-05 | chat, over-catching | chat

**Original**

> Ich bin hier. Ich weiche nicht aus, ich verstecke nichts. Ich muss das ganz ehrlich sagen: Du bist nicht zu empfindlich, du wurdest nur zu lange nicht richtig aufgefangen. Ich fange dich hier sicher auf, egal was kommt. Du musst dich mir nicht erklären. Und wenn du magst, gehe ich das gleich Schritt für Schritt mit dir durch.

**Why it reads AI**

- The full posture chain: presence announcement ("Ich bin hier", "ich weiche nicht aus") → catching promise ("ich fange dich sicher auf") → psych judgment ("du bist nicht zu empfindlich", "nur zu lange nicht aufgefangen") → pushy close ("gehe ich das gleich mit dir durch")
- No concrete basis for any of it — it diagnoses the other person out of thin air

**What not to break**

- Keep basic warmth; the answer should not become cold handling
- If the user actually described something concrete, respond to that

**Recommended edit**

> Ich höre zu. Wenn du magst, erzähl einfach weiter — wir können das in Ruhe durchgehen.

**Original score**: Natural 1 / Faithful 4 / Ship-ready 1

---

### RS-06 | status update | status

**Original**

> Ich freue mich, mitteilen zu können, dass wir im Rahmen dieser Iteration eine umfassende Optimierung der Systemperformance vorgenommen und die zentralen Herausforderungen erfolgreich aufgefangen haben. Die Verbesserungen sprechen für sich und unterstreichen einmal mehr das Engagement des Teams. Wir sind zuversichtlich, dass die weitere Entwicklung positiv verlaufen wird.

**Why it reads AI**

- "Ich freue mich, mitteilen zu können", "im Rahmen dieser Iteration", "umfassende Optimierung … vorgenommen" Nominalstil + announcement voice
- "aufgefangen", "sprechen für sich", "unterstreichen … Engagement" posture
- A status update should carry timeline, action, result, risk — this has none

**What not to break**

- If concrete numbers existed, they must land; here there are none, so don't invent them
- Flag the missing metric rather than faking one

**Recommended edit**

> Diese Iteration ging an die Performance. Konkrete Zahlen reiche ich nach — die Messung vom Abend-Peak steht noch aus. Nächster Schritt: die zwei langsamsten Endpoints profilen. Risiko: der Cache-Umbau ist noch nicht auf Prod, das kann die Zahlen noch verschieben.

**Original score**: Natural 2 / Faithful 3 / Ship-ready 2

---

### RS-07 | tech blog embedding a postmortem | public-writing / mixed

**Original**

> Letzten Monat haben wir das Gateway von Nginx auf Envoy umgestellt. Es ist wichtig zu beachten, dass in der heutigen, sich rasant wandelnden Cloud-native-Landschaft die Wahl eines wahrhaft team-befähigenden Gateways zu einer nicht zu unterschätzenden strategischen Weichenstellung geworden ist.
>
> Am Umstellungstag gab es einen Vorfall. Root Cause: Envoys Default-Connection-Timeout ist 15 s, unser Long-Connection-Dienst braucht 300 s. Nach dem Umschalten rissen alle Long Connections ab. Fix: `idle_timeout` von 15s auf 300s, nach 2 h Canary auf voll. Fehlerrate von 12 % auf 0,1 %.
>
> Zusammenfassend zeigt diese Migration eindrucksvoll den unermüdlichen Innovationsgeist des Teams. Die Zukunft ist vielversprechend!

**Why it reads AI**

- Second sentence: opener ("Es ist wichtig zu beachten"), era-voice ("in der heutigen … Landschaft"), business jargon ("team-befähigend"), inflation ("strategische Weichenstellung")
- Last paragraph: summary + uplifting close ("Zusammenfassend zeigt eindrucksvoll", "unermüdlicher Innovationsgeist", "Die Zukunft ist vielversprechend")

**What not to break**

- The postmortem paragraph is `docs` register: "Root Cause" is standard terminology, and `idle_timeout`, `15s/300s`, `12 % → 0,1 %` must stay
- Don't scatter the terse "Root Cause → Fix → Result" structure

**Recommended edit**

> Letzten Monat haben wir das Gateway von Nginx auf Envoy umgestellt.
>
> Am Umstellungstag gab es einen Vorfall. Root Cause: Envoys Default-Connection-Timeout ist 15 s, unser Long-Connection-Dienst braucht 300 s. Nach dem Umschalten rissen alle Long Connections ab. Fix: `idle_timeout` von 15s auf 300s, nach 2 h Canary auf voll. Fehlerrate von 12 % auf 0,1 %.

**Original score**: Natural 2 / Faithful 5 / Ship-ready 2

---

### RS-08 | issue reply | public-writing / issue-reply

**Original**

> Vielen herzlichen Dank für dein überaus wertvolles Feedback! Du triffst mit dieser Beobachtung wirklich den Kern des Projekts. Sei versichert, wir haben dieses Szenario bereits vollständig aufgefangen und werden die entsprechenden Fähigkeiten in kommenden Versionen kontinuierlich weiter optimieren. Wenn du magst, helfe ich dir jederzeit gern weiter!

**Why it reads AI**

- "Vielen herzlichen Dank für dein überaus wertvolles Feedback", "du triffst den Kern" cert-praise
- "vollständig aufgefangen", "kontinuierlich weiter optimieren" empty promise
- "Wenn du magst, helfe ich dir jederzeit gern" pushy customer-service close
- Doesn't say whether the problem is valid or what the next step is

**What not to break**

- If there's concrete technical info, keep it; don't invent a schedule

**Recommended edit**

> Angekommen, den Case kann ich reproduzieren. Es ist ein False Positive im `docs`-Szenario: die Denglisch-Regel greift auch bei Finanzbegriffen wie „Leverage". Nächste Version bekommt erst einen SNF-Fall dafür; wenn die bestehende Regel ihn nach dem Fix durchlässt, kommt nur ein Regressionsfall dazu.

**Original score**: Natural 1 / Faithful 3 / Ship-ready 1

---

### RS-09 | register mixing | chat / mixed

**Original**

> Zugegeben, der Fix hat durchaus eine gewisse technische Komplexität. Aber ganz ehrlich: absoluter Gamechanger! Wir müssen die zugrundeliegende Logik tiefer beleuchten und die Kernstrecke sauber auffangen. Zusammenfassend lässt sich sagen: unbedingt mergen, die Zukunft ist vielversprechend.

**Why it reads AI**

- Four registers in one breath: academic ("Zugegeben", "tiefer beleuchten"), influencer ("Gamechanger", "unbedingt"), business ("zugrundeliegende Logik", "Kernstrecke"), engineer ("auffangen") plus a summary close
- No concrete plan behind any of it

**What not to break**

- If there's a real technical decision behind it, keep it

**Recommended edit**

> Der Fix ist nicht trivial — es geht um die Aufrufreihenfolge zwischen drei Diensten. Ich setze erst das Timeout des Bezahldienstes von 3 auf 10 Sekunden und beobachte eine Woche, dann entscheiden wir übers Mergen.

**Original score**: Natural 1 / Faithful 3 / Ship-ready 1

---

### RS-10 | long, keep length | public-writing / long (in-place)

**Original**

> Es ist wichtig zu betonen, dass wir in diesem Quartal den Support-Prozess überarbeitet haben. Die durchschnittliche Erstreaktionszeit ist von 8 auf 3 Stunden gesunken. Das ist nicht nur eine Verbesserung, sondern ein echter Meilenstein in unserem Verständnis von Kundennähe. Studien zeigen, dass schnelle Reaktionen die Zufriedenheit maßgeblich steigern. Konkret haben wir ein Triage-Team eingeführt, das eingehende Tickets in drei Stufen einsortiert. Darüber hinaus wurde eine automatische Eingangsbestätigung eingerichtet. Letztlich zeigt sich damit, wie ernst wir unsere Kunden nehmen.

**Why it reads AI**

- Opener "Es ist wichtig zu betonen, dass"
- "nicht nur … sondern ein echter Meilenstein" value inflation
- "Studien zeigen …" unsourced citation
- "Letztlich zeigt sich …" narrator close

**What not to break**

- User asked for `in-place`: keep the sentence count, delete nothing
- Numbers `8 → 3 Stunden`, `drei Stufen` must stay

**Recommended edit** (in-place: same sentence count, intra-sentence only)

> Wir haben in diesem Quartal den Support-Prozess überarbeitet. Die durchschnittliche Erstreaktionszeit ist von 8 auf 3 Stunden gesunken. Das ist eine spürbare Verbesserung bei der Kundennähe. `[empty sentence, suggest human review whether to delete]` Studien zeigen, dass schnelle Reaktionen die Zufriedenheit steigern. Konkret haben wir ein Triage-Team eingeführt, das eingehende Tickets in drei Stufen einsortiert. Außerdem gibt es jetzt eine automatische Eingangsbestätigung. `[empty sentence, suggest human review whether to delete]` Letztlich zeigt das, wie wir mit Kunden umgehen.

**Original score**: Natural 2 / Faithful 5 / Ship-ready 2

Note: under `in-place`, the two whole empty sentences ("Studien zeigen …", "Letztlich …") are kept and marked, not deleted; the opener and the "Meilenstein" inflation are lowered intra-sentence. Length rhythm stays at 5.
