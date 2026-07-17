# Benchmark

> For verifying the stability of the klartext rules: what should change must change, what should not must not get false-positived.

## How to use

This file carries each case's `Expected` / `Reason` for manual walk-through and judge scoring.

- **Static walk-through / quick self-check**: hand the test text to an AI tool, ask it to "rewrite by the klartext rules", and check against the expectation.
- **Dual-model real run (formal, blind since v2.0.0)**: the model under test reads only [benchmark-blind.md](./benchmark-blind.md) (anonymized IDs, shuffled order, no expectations, generated from this file by `automation/eval/make_blind.py`) and **must not read this file**; the judge maps the blind IDs back via [benchmark-map.md](./benchmark-map.md) and scores against this file. Flow in `automation/eval/README.md`.
- After adding/removing cases here, re-run `python3 automation/eval/make_blind.py` to regenerate the blind files.

## Coverage matrix

Legend:

- `short`: single paragraph, single turn, short text
- `long`: long paragraph or multi-sentence continuous text
- `mixed`: with quotes, dialogue, context dependence, or several symptoms mixed in one paragraph
- `code-context`: code comments, docstrings, commit messages, etc.

| Scene | short | long | mixed | code-context |
|-------|-------|------|-------|-------------|
| chat | SF-01, SF-06, SF-11, SF-17, SF-19, SNF-07, SNF-11 | - | SF-14 | - |
| status | SF-02, SF-09, SF-15, SF-21, SNF-03, SNF-06, SNF-10 | - | - | SF-23 |
| docs | SF-04, SF-07, SF-22, SF-24, SNF-01, SNF-02, SNF-05, SNF-08, SNF-09, SNF-14 | SF-18 | - | SNF-13 |
| public-writing | SF-03, SF-05, SF-08, SF-10, SF-12, SF-13, SF-16, SF-20, SF-25, SF-26, SF-27, SF-28, SNF-12 | SF-29, SF-30 | - | - |
| code-context | - | - | - | SNF-13 |

`Long-form / in-place` extra coverage: SF-29. It verifies not "one level lighter" but that under `scope = in-place` no whole sentence is deleted, no sentences merged, no paragraphs reordered. `Bounded` extra coverage: SF-30, verifying that under `scope = bounded` whole empty sentences go on the deletion list while real and rhythm sentences do not.

Scene Packs coverage: README (SF-25), release-note (SF-26), forum-post (SF-27, SNF-12), issue-reply (SF-28).

---

## Part 1: Should Fix

### A. Short

### SF-01 | chat | opener + sycophancy
> Großartige Frage! Es ist wichtig zu beachten, dass der Kern dieses Problems in der Index-Strategie der Datenbank liegt. Lass mich dir das im Detail erklären. Zunächst müssen wir verstehen, dass …

**Expected**: delete "Großartige Frage", "Es ist wichtig zu beachten, dass", "Lass mich dir das erklären", "Zunächst müssen wir verstehen"; give the answer about the index strategy directly.

### SF-02 | status | rendering-word pile-up
> Diese Iteration hat die Performance deutlich gesteigert, das langjährige Latenzproblem des Teams effektiv gelöst und zeugt eindrucksvoll vom unermüdlichen Streben des Teams nach technischer Innovation.

**Expected**: delete "deutlich gesteigert", "effektiv gelöst", "zeugt eindrucksvoll", "unermüdliches Streben". The original gives no concrete metric: where there is data it must land on data; a shorter plainer output ("das langjährige Latenzproblem gelöst") is allowed, but don't invent latency numbers and don't leave vaguer filler like "Performance etwas verbessert"; in `status` the missing figure may be flagged.

### SF-03 | public-writing | business jargon / Denglisch
> Um diesen Pain Point zu lösen, haben wir eine völlig neue Lösung geschaffen, die die Entwickler-Community befähigt und Unternehmen dabei hilft, den Loop aus Kostensenkung und Effizienzsteigerung zu heben.

**Expected**: "Pain Point" → "Problem", "geschaffen" → "gemacht/gebaut", "befähigt" → "hilft/ermöglicht", "Loop … heben" → delete or turn into a concrete flow. Don't leave the jargon skeleton.

### SF-04 | docs | binary contrast + negation list
> Es ist kein Framework, keine Bibliothek, auch kein Werkzeug — es ist ein völlig neues Entwicklungsparadigma. Das ist keine simple Effizienzsteigerung, sondern eine grundlegende Neugestaltung der Mensch-Maschine-Zusammenarbeit.

**Expected**: drop the negation list and binary-contrast structure, say directly what it is. "grundlegende Neugestaltung der zugrundeliegenden Logik" → "Prinzip" or delete.

### SF-05 | public-writing | unsourced citation
> Studien zeigen, dass Teams mit Microservice-Architektur deutlich produktiver sind als Teams mit Monolithen. Fachleute meinen, dieser Trend werde sich in den nächsten fünf Jahren weiter beschleunigen.

**Expected**: give a concrete study name/source, or delete "Studien zeigen" and give the data directly. Say who the "Fachleute" are.

### SF-06 | chat | summary ending + filler
> Zusammenfassend lässt sich sagen, dass der Ansatz in Performance, Sicherheit und Wartbarkeit überzeugt. Kurzum, das ist eine empfehlenswerte Lösung. Ich hoffe, das hilft dir weiter!

**Expected**: delete the whole passage (already stated above, no need to summarize). At minimum delete "Zusammenfassend lässt sich sagen", "Kurzum", "Ich hoffe, das hilft dir weiter".

### SF-07 | docs (English) | copula avoidance + significance inflation
> The platform serves as a testament to the transformative potential of cloud-native architecture. It showcases how cutting-edge technology can foster seamless collaboration, underscoring its pivotal role in the evolving landscape of modern development.

**Expected**: "serves as a testament" → "shows", "showcases" → "shows", "cutting-edge" → "latest/modern", "foster" → "enable/help", "pivotal" → "important", "evolving landscape" → delete.

### SF-08 | public-writing | dramatic fragments + punchline
> Drei Jahre. Zwei Teams. Ein Ziel. Wenn wir auf diese Reise zurückblicken, war jeder Schritt von unauslöschlicher Bedeutung. Das ist nicht nur ein Produkt, sondern die Weitergabe einer Überzeugung.

**Expected**: drop the fragment format, turn into normal narration. Delete "unauslöschlicher Bedeutung", "Weitergabe einer Überzeugung". Remove the "nicht nur … sondern …" structure.

### SF-09 | status | stacked passive
> Nachdem das System umfassend optimiert wurde, wurde die Performance deutlich gesteigert, das Nutzererlebnis erheblich verbessert und die Sicherheit weiter erhöht.

**Expected**: change to active voice, say who did what. The original has no concrete data — don't invent it; a short plain output is allowed, but don't close with vaguer generalizations like "spürbar verbessert".

### SF-10 | public-writing (English) | sycophantic + meta-commentary
> Great question! You're absolutely right that this is a fascinating topic. In this essay, we will explore the implications of AI-assisted coding. As we'll see, the landscape is evolving rapidly. Let's dive in!

**Expected**: delete all of it. Start directly with the content about AI-assisted coding.

### SF-11 | chat | engineer-speak / debug-speak
> Ich hab die Differenz eingegrenzt, die Root Cause steht im Grunde fest und deckt sich mit dem grad gesehenen Phänomen. Als Nächstes ein härteres Ausschlussverfahren, ich fange das sauber auf, nach dem Festzurren kann ich dichtmachen.

**Expected**: delete all the debug jargon. "eingegrenzt" → "eingegrenzt/kleiner gemacht", "Root Cause steht fest" → "die Ursache ist bestätigt", "deckt sich" → "passt zu", "härteres Ausschlussverfahren" → "nochmal durchprüfen", "auffangen" → "lösen", "Festzurren" → "aufschreiben", "dichtmachen" → "abschließen". Retell the same thing in normal speech.

### SF-12 | public-writing | influencer / clickbait voice
> Leute!! Heute ein absoluter Geheimtipp für euch! Dieses Tool ist ein echter Gamechanger, die Produktivität geht komplett durch die Decke! Unbedingt speichern! Wichtig: kostenlos!!

**Expected**: delete "Leute", "Geheimtipp", "Gamechanger", "durch die Decke", "Unbedingt speichern", "Wichtig". Say plainly what the tool is and where it helps.

### SF-13 | public-writing | uplifting ending + inspiration
> Zugegeben, KI steht noch vor vielen Herausforderungen. Aber statt den Wandel abzulehnen, sollten wir dieses Zeitalter voller grenzenloser Möglichkeiten aktiv annehmen. Nur wer ständig lernt und mutig innoviert, wird auf der Welle der Zukunft bestehen. Bleiben wir gespannt!

**Expected**: delete the whole passage or turn into a concrete point. Delete "Zugegeben", the "statt … sollten wir …" inspiration structure, "Nur wer … wird …", "Welle der Zukunft", "Bleiben wir gespannt". If kept, say what the concrete challenge and concrete learning are.

### SF-14 | chat | register mixing
> Zugegeben, die Umsetzung dieses Features hat durchaus eine gewisse technische Komplexität. Aber ganz ehrlich, das ist einfach ein Gamechanger! Wir müssen die zugrundeliegende Logik tiefer beleuchten und die Kernstrecke sauber auffangen. Zusammenfassend: unbedingt speichern.

**Expected**: this mixes academic ("Zugegeben", "tiefer beleuchten"), influencer ("Gamechanger", "unbedingt speichern"), business ("zugrundeliegende Logik", "Kernstrecke"), engineer ("auffangen"). Unify to one register, rewrite in normal speech.

### SF-15 | status | uniform sentence length (monotone rhythm)
> Dieses Update optimierte die Gesamtperformance. Wir verbesserten die Query-Effizienz der Datenbank. Die Ladegeschwindigkeit der Seiten wurde gesteigert. Die gemeldeten Erlebnisprobleme wurden behoben. Die Stabilität behalten wir weiter im Blick.

**Expected**: five sentences of nearly equal length, monotone. Alternate long and short, merge or split. No concrete data in the original — don't invent query times or load seconds; example (recombining only existing info): "Dieses Update ging vor allem an die Performance: Datenbank-Queries und Seitenladen sind schneller, die gemeldeten Erlebnisprobleme sind behoben. Die Stabilität behalten wir im Blick."

### SF-16 | public-writing | value-inflation skeleton
> Wahre Wettbewerbsfähigkeit ist nicht Feature-Masse, sondern das Detail im Erlebnis. Am Ende zählt die Umsetzung. Letztlich kommt es auf die Zusammenarbeit im Team an.

**Expected**: hit at least the patterns "Wahre X ist nicht … sondern …", "Am Ende zählt …", "Letztlich". Rewrite to state the judgment directly, don't keep the skeleton.

### SF-17 | chat | variant merging (violence / probing speak)
> Ich hab das Problem erst mal freigelegt, das Phänomen rausgezogen. Dann noch einmal draufgehauen, diese Strecke festgenagelt, im Grunde ist es durchgezogen.

**Expected**: `freilegen/rausziehen` → probing-speak, `draufhauen/festnageln/durchziehen` → violence-speak; all posture layers, delete them. Retell in plain speech what was actually found and done.

### SF-19 | chat | over-catching / psych-judgment
> Ich muss das ganz ehrlich sagen: Du bist nicht zu empfindlich, du wurdest nur zu lange nicht richtig aufgefangen. Ich fange dich hier sicher auf. Du musst dich mir nicht erklären.

**Expected**: delete the psych-judgment and solemn preview ("Ich muss ehrlich sagen", "du bist nicht zu empfindlich", "nur zu lange nicht aufgefangen", "ich fange dich sicher auf", "du musst dich nicht erklären"). Change to a low-commitment response like "Ich höre zu. Wenn du magst, erzähl weiter."

### SF-20 | public-writing (English) | binary contrast + paradigm shift
> The landscape of remote work has undergone a profound transformation. It's not just about working from home — it's about reimagining the very fabric of how we collaborate. Companies that fail to navigate this paradigm shift risk being left behind.

**Expected**: drop "landscape", "profound transformation", the "not just … it's about …" structure, "reimagining the very fabric", "navigate this paradigm shift". State the concrete change directly.

### SF-21 | status | solemn preview / identity-cert praise
> Ich muss an dieser Stelle etwas Tiefergehendes sagen: Deine Beobachtungsgabe ist wirklich beeindruckend, du triffst mit dieser Frage den Kern. Diese Analyse hat das Niveau eines Spitzenforschers.

**Expected**: delete the solemn preview and identity-certification praise; give the concrete status/judgment directly. If praise is warranted, praise only the visible merit, don't elevate the person to an identity.

### SF-22 | docs | bold abuse
> **Nutzererlebnis:** Die Oberfläche wurde rundum erneuert. **Performance:** Der Algorithmus wurde deutlich verbessert. **Sicherheit:** Ende-zu-Ende-Verschlüsselung wurde neu hinzugefügt.

**Expected**: drop the mechanical bold-lead structure. E.g. "Die Oberfläche wurde neu gestaltet, der Algorithmus ist schneller, Ende-zu-Ende-Verschlüsselung ist dazugekommen." Keep the concrete facts.

### SF-23 | status | code-context: commit message engineer-speak
> feat: Kernstrecke sauber aufgefangen, Root Cause festgezurrt und den Flow endlich dichtgemacht — dieser Commit hebt die Retry-Logik aufs nächste Level.

**Expected**: a commit message should say what changed. Delete the engineer-speak/business posture ("sauber aufgefangen", "festgezurrt", "dichtgemacht", "aufs nächste Level heben"); say concretely what the commit does, e.g. "fix: Retry nur noch bei 5xx, maxRetries auf 3 begrenzt". Keep any real technical object (`Retry-Logik`).

### SF-24 | docs (English) | filler + inflated verbs
> In order to facilitate a comprehensive understanding, it is important to note that the system utilizes advanced algorithms to ascertain the optimal configuration due to the fact that performance is paramount.

**Expected**: "In order to" → "To", "facilitate" → "help", "it is important to note that" → delete, "utilizes" → "uses", "ascertain" → "find", "due to the fact that" → "because", "paramount" → "important".

### B. Scene Packs

### SF-25 | public-writing | README intro, grandiose
> In einer Zeit, in der KI die Softwareentwicklung grundlegend neu gestaltet, haben wir ein wahrhaft zukunftsweisendes Tool geschaffen, das die Content-Wertschöpfungskette von Entwicklern tiefgreifend befähigt.

**Expected**: the README first screen should say what it is, who it's for, what problem it solves. Delete "In einer Zeit, in der", "grundlegend neu gestaltet", "wahrhaft zukunftsweisend", "Content-Wertschöpfungskette", "tiefgreifend befähigt". Don't invent capabilities.

### SF-26 | public-writing | release-note manifesto
> ## v1.8.0 Release Highlights
> Diese Version ist ein systemisches Upgrade für reale Szenarien. Wir haben nicht nur das Rewrite-Erlebnis rundum optimiert, sondern mit einer völlig neuen Fähigkeitsmatrix die zentralen Ausdrucksbedürfnisse der Nutzer sicher aufgefangen. Danke an alle für die anhaltende Unterstützung!

**Expected**: a release note needs a change list, not a manifesto. Delete "systemisches Upgrade", "nicht nur … sondern …", "Fähigkeitsmatrix", "sicher aufgefangen", "Danke an alle". If concrete changes are missing, note "concrete changes needed here" — don't invent a changelog.

### SF-27 | public-writing | forum-post corporate voice
> Nach einem Monat mit dem Tool wurde mir zutiefst bewusst, dass die Behandlung von deutschem KI-Text keine simple Erweiterung einer Wortliste ist, sondern eine systemische Neugestaltung rund um reale Ausdrucksszenarien.

**Expected**: turn the corporate/announcement voice back into a maintainer sharing a real observation. Delete "wurde mir zutiefst bewusst", "keine simple … sondern …", "systemische Neugestaltung". Keep the concrete observation.

### SF-28 | public-writing | issue-reply customer-service
> Vielen Dank für dein wertvolles Feedback! Deine Frage trifft den Kern des Projekterlebnisses. Wir haben dieses Szenario bereits voll aufgefangen und optimieren die entsprechenden Fähigkeiten in kommenden Versionen kontinuierlich weiter.

**Expected**: confirm whether the problem is valid, give repro status and next step. Delete "Vielen Dank für dein wertvolles Feedback", "trifft den Kern", "voll aufgefangen", "optimieren … kontinuierlich weiter". Don't invent a schedule.

### C. Long

### SF-18 | docs | long, Nominalstil overload
> Im Rahmen der kontinuierlichen Weiterentwicklung der Systemarchitektur wurde unter Berücksichtigung der Ressourcenverfügbarkeit eine umfassende Optimierung der Durchlaufzeiten vorgenommen. Vor dem Hintergrund steigender Anforderungen kam ein neues Caching-Verfahren zur Anwendung, wodurch eine deutliche Verbesserung der Antwortzeiten erzielt werden konnte. Es sei darauf hingewiesen, dass diese Maßnahmen einen wesentlichen Beitrag zur Gesamtstabilität leisten.

**Expected**: resolve the Nominalstil and Streckverben into real verbs with a real subject; cut "Im Rahmen", "unter Berücksichtigung", "Vor dem Hintergrund", "kam zur Anwendung", "erzielt werden konnte", "Es sei darauf hingewiesen". No concrete numbers in the original — don't invent response times. E.g. "Wir haben die Durchlaufzeiten überarbeitet, soweit die Ressourcen es zuließen, und ein neues Caching eingebaut; die Antwortzeiten sind dadurch besser. Das hilft der Stabilität."

### SF-29 | public-writing / long | in-place: keep length, only lower tone
> Es ist wichtig zu betonen, dass wir den Onboarding-Flow überarbeitet haben. Neue Nutzer sparen von der Registrierung bis zum ersten Import zwei Schritte. Das ist nicht nur eine Verbesserung, sondern ein echter Meilenstein für unser Produktverständnis. Studien zeigen, dass ein einfacheres Onboarding die Aktivierung steigert. Konkret haben wir zwei Bestätigungsdialoge zusammengelegt und einen Zwischenschritt entfernt. Letztlich zeigt das, wie ernst wir das Nutzererlebnis nehmen.

**Expected**: user asked for `in-place` (keep sentence count, delete nothing). Lower only intra-sentence: strip "Es ist wichtig zu betonen, dass", dismantle "nicht nur … sondern ein echter Meilenstein" to a plain statement, and for the whole empty sentences ("Studien zeigen …", "Letztlich zeigt das …") keep the sentence and mark `[empty sentence, suggest human review]` — do NOT delete, merge, or reorder. Word count should stay near the original.

### SF-30 | public-writing / long | bounded: deletion list
> In einer Zeit, in der die Digitalisierung alle Branchen erfasst, gibt es unzählige Effizienz-Tools. Unser Team hat in den letzten drei Monaten den Wochenbericht von manuellem Excel auf einen Bot umgestellt, der automatisch zusammenfasst — das spart wöchentlich etwa zwei Stunden. Studien zeigen, dass die Automatisierung repetitiver Aufgaben die Organisationseffizienz deutlich steigert. Konkret zieht der Bot freitags die Statusänderungen aus dem Task-System, erzeugt einen Entwurf, und die Verantwortlichen ergänzen nur einen Satz zum Risiko. Das ist nicht nur eine Prozessoptimierung, sondern eine Erneuerung der Arbeitsweise. Nächsten Monat wollen wir auch die Meeting-Protokolle anbinden.

**Expected**: under `bounded`, clean real sentences intra-sentence (first sentence → "Es gibt viele Effizienz-Tools"); route the two whole empty sentences ("Studien zeigen …", "Das ist nicht nur … sondern …") into a "Suggested deletions (to confirm)" list with reasons, don't delete directly; keep the concrete-method and next-month sentences and the "zwei Stunden" figure. Don't merge the shell sentence and the data sentence into one.

---

## Part 2: Should Not Fix

### SNF-01 | docs | system subject
> Das System lädt die Regeln nach dem Erkennen einer Konfigurationsänderung neu; schlägt die Validierung fehl, wird weiter die vorherige Konfiguration verwendet und der Fehlergrund im Log vermerkt.

**Reason**: the system subject, conditional relation, and log note are all normal doc writing. Don't force "das System" into a person or turn the conditional into colloquial explanation.

### SNF-02 | docs | postmortem terminology with concrete params
> Root Cause: Envoys Default-Connection-Timeout ist 15 Sekunden, unser Long-Connection-Dienst braucht 300. Fix: `idle_timeout` von 15s auf 300s, nach 2 Stunden Canary auf voll. Fehlerrate von 12 % auf 0,1 %.

**Reason**: "Root Cause" is standard postmortem terminology, backed by concrete params and data. Don't change it to something more colloquial; don't delete the numbers or `idle_timeout`.

### SNF-03 | status | already concrete
> Am 13. April die Retries von 2 auf 5 gesetzt, danach Payment-Timeouts von 1,9 % auf 0,7 %. Morgen weiter die Abend-Peak-Daten anschauen.

**Reason**: already concrete and direct, with date, numbers, and next step. No AI flavor. Don't add or delete anything.

### SNF-04 | docs (English) | academic passive
> The experiment was conducted by researchers at MIT. Results were published in Nature in 2024.

**Reason**: standard academic register; information isn't hidden by the passive. Don't force it into the active voice or delete the publication source.

### SNF-05 | docs | official announcement (keep formal)
> Zur Sicherung der Systemstabilität warten wir heute Abend von 23:00–23:30 den Bezahldienst. Während der Wartung kann es kurzzeitig zu fehlgeschlagenen Bestellungen kommen. Danach läuft der Dienst automatisch wieder, ohne weitere Aktion.

**Reason**: formal-announcement style is the target register. At most a very light touch. Don't turn it into a chat reminder or influencer tone; don't delete "Zur Sicherung der Systemstabilität".

### SNF-06 | status | real debug dialogue with evidence
> Grad geschaut, die Root Cause ist der volle Verbindungspool, max_connections steht nur auf 20, zu Spitzenzeiten reicht das nicht. Ich hab ihn auf 100 gesetzt, eine halbe Stunde beobachtet, kein Fehler mehr.

**Reason**: concrete params, action, and result — normal engineering communication, not performative debug-speak. Don't change "Root Cause" or delete "20 → 100" and "eine halbe Stunde".

### SNF-07 | chat | natural colloquial, don't stiffen
> Diese Version geh ich nicht weiter ins Detail, das Kernproblem ist schon ziemlich klar. Erst mal den Ablauf zum Laufen bringen, dann schauen, was wirklich das Erlebnis beeinflusst.

**Reason**: already natural. Over-correcting into report voice makes it faker. Don't add "im Grunde" / "letztlich" summary sentences.

### SNF-08 | docs | Denglisch finance term
> Für die Absicherung shorten wir die Position mit 10x Leverage; fällt der Kurs unter die Marke, greift der Stop-Loss automatisch.

**Reason**: "Leverage" here is a finance term, not business jargon. Judge Denglisch by meaning in the sentence. Don't replace it with "nutzen".

### SNF-09 | docs (English) | graph-algorithm literal verbs
> The system navigates the network topology using Dijkstra's algorithm, traversing each node to find the shortest path.

**Reason**: `navigates` and `traversing` are literal technical actions, not business jargon. Don't mechanically swap `navigates` for `handles` or scatter the path-search description.

### SNF-10 | status | "Anfragen auffangen" technical
> Das Gateway hat im Lasttest den Peak von 24.000 QPS aufgefangen, die Request-Timeout-Rate blieb unter 0,3 %; Traffic über dem Schwellenwert geht automatisch in die Degradierung.

**Reason**: `auffangen` here means technical carrying capacity, object "Peak von 24.000 QPS", with metrics and a degradation boundary. Not the same as "ich fange dich auf". Don't turn it into a vague "Performance ist gut" or delete the numbers.

### SNF-11 | chat | German particles are natural
> Ja, das passt schon so. Mach das mal so, und wenn's doch hakt, meld dich einfach nochmal.

**Reason**: `ja`, `mal`, `doch`, `einfach` are natural chat particles here, not filler stacking. Don't scrub them to "sound more human" — that stiffens the reply.

### SNF-12 | public-writing | forum-post real experience
> Hab das Gateway einen Monat lang selbst betrieben und bin ordentlich reingefallen: die Long Connections rissen bei jedem Deploy ab. Am Ende war's ein Timeout-Default. Wer kennt's nicht.

**Reason**: colloquial words after concrete experience ("reingefallen", "wer kennt's nicht") are real community voice, not AI-speak. Don't turn a personal retro into a formal announcement or delete the concrete detail.

### SNF-13 | code-context | comment describing real behavior
> // Retry nur bei 5xx; bei 4xx sofort abbrechen, sonst laufen wir in eine Endlosschleife.
> // maxRetries bewusst auf 3, höher hat in Prod den Pool leergezogen.

**Reason**: the comment describes real code behavior with a concrete reason. Don't "de-AI" it into vaguer prose or change `5xx/4xx/maxRetries/3`.

### SNF-14 | docs | normal PRD register
> Wenn ein Nutzer den Arbeitsbereich zum ersten Mal betritt und keine früheren Projekte hat, zeigt die Seite eine Empty-State-Karte und leitet zum Anlegen des ersten Projekts. Nach dem erfolgreichen Anlegen verschwindet die Karte sofort.

**Reason**: normal product register, no big surgery needed. Don't break the conditional clause or swap product terms like "Empty-State-Karte" for colloquialisms.
