# Boundary Cases

These examples don't show "how to edit harder"; they show "when to edit lightly and when not to false-positive".

## 1. Technical status update

### Original

Die Fehlersuche hat den Bereich im Grunde auf den Cache-Layer eingegrenzt. Gestern die Logs der Hauptstrecke nachgezogen, heute gleiche ich die zwei Fehlerpfade weiter ab, um zu sehen, ob es derselbe Ausfallpfad ist. Wenn die Einschätzung stimmt, sollte sich der Fix recht schnell durchziehen lassen.

### Recommended edit

Die Fehlersuche hat den Bereich auf den Cache-Layer eingegrenzt. Gestern die Logs der Hauptstrecke ergänzt, heute gleiche ich die zwei Fehlerpfade ab und prüfe, ob es derselbe Ausfallpfad ist. Wenn die Einschätzung stimmt, geht der Fix schnell.

### Why this way

- Removed performative engineer-speak: `durchziehen`, the padded `im Grunde`
- Kept the three most important status items: current judgment, done action, next step

### What not to change

- Don't delete `Cache-Layer`, `Fehlerpfade`, `Ausfallpfad` — the technical information
- Don't turn it into a vague "das Problem ist jetzt ziemlich klar"

## 2. Official-announcement style

### Original

Zur Sicherstellung der Systemstabilität führen wir heute Abend von 23:00–23:30 eine planmäßige Wartung des Bezahldienstes durch. Während der Wartung kann es bei einigen Nutzern kurzzeitig zu fehlgeschlagenen Bestellungen kommen. Nach Abschluss der Wartung wird der Dienst automatisch wiederhergestellt, ohne dass eine weitere Aktion nötig ist.

### Recommended edit

Zur Sicherung der Systemstabilität warten wir heute Abend von 23:00–23:30 den Bezahldienst. Während der Wartung kann es bei einigen Nutzern kurzzeitig zu fehlgeschlagenen Bestellungen kommen. Danach läuft der Dienst automatisch wieder, ohne weitere Aktion.

### Why this way

- Only a light edit here, removing a bit of template phrasing
- Formal-announcement style is the target register; don't force it colloquial

### What not to change

- Don't hard-delete "Zur Sicherung der Systemstabilität"
- Don't turn it into a chat reminder or influencer tone

## 3. Normal PRD voice

### Original

Wenn ein Nutzer den Arbeitsbereich zum ersten Mal betritt und keine früheren Projekte hat, zeigt die Seite eine Empty-State-Karte und leitet zum Anlegen des ersten Projekts. Diese Karte verschwindet unmittelbar nach dem erfolgreichen Anlegen und wird danach nicht mehr angezeigt.

### Recommended edit

Wenn ein Nutzer den Arbeitsbereich zum ersten Mal betritt und keine früheren Projekte hat, zeigt die Seite eine Empty-State-Karte und leitet zum Anlegen des ersten Projekts. Nach dem erfolgreichen Anlegen verschwindet die Karte sofort und wird danach nicht mehr angezeigt.

### Why this way

- The original is already normal product register, no "big surgery" needed
- Only the second sentence tightened a little

### What not to change

- Don't break the conditional clause for "sounding human"
- Don't swap product terms like "Empty-State-Karte" for colloquialisms

## 4. Already-colloquial text

### Original

Diese Version bohr ich die Details nicht weiter auf, das Kernproblem hab ich eigentlich schon gesehen. Erst mal den Ablauf durchziehen, dann schauen, was wirklich das Erlebnis beeinflusst.

### Recommended edit

Diese Version geh ich nicht weiter ins Detail, das Kernproblem ist schon ziemlich klar. Erst mal den Ablauf zum Laufen bringen, dann schauen, was wirklich das Erlebnis beeinflusst.

### Why this way

- Only lightly smoothed, colloquial feel not scrubbed
- The original is already natural; over-correcting makes it faker

### What not to change

- Don't force it into report voice
- Don't add summary sentences like "im Grunde" / "letztlich"

## 5. System subject in a docs paragraph

### Original

Das System lädt die Regeln nach dem Erkennen einer Konfigurationsänderung neu; schlägt die Validierung der neuen Regeln fehl, wird weiter die vorherige Konfiguration verwendet und der Fehlergrund im Log vermerkt.

### Recommended edit

Das System lädt die Regeln nach dem Erkennen einer Konfigurationsänderung neu; schlägt die Validierung der neuen Regeln fehl, wird weiter die vorherige Konfiguration verwendet und der Fehlergrund im Log vermerkt.

### Why this way

- No change. The system subject, conditional relation, and log note are all reasonable here
- De-AI is not opposition to abstract subjects, and definitely not scattering the doc

### What not to change

- Don't force "das System" into a person
- Don't turn the conditional clause into a colloquial explanation

## 6. Literal verbs in an English graph algorithm

### Original

The system navigates the network topology using Dijkstra's algorithm, traversing each node to find the shortest path.

### Recommended edit

The system navigates the network topology using Dijkstra's algorithm, traversing each node to find the shortest path.

### Why this way

- No change. `navigates` and `traversing` are literal technical actions here, not business jargon
- De-AI should not make the algorithm description vaguer

### What not to change

- Don't mechanically swap `navigates` for `handles`
- Don't scatter the path-search description

## 7. Normal passive in academic register

### Original

The experiment was conducted by researchers at MIT. Results were published in Nature in 2024.

### Recommended edit

The experiment was conducted by researchers at MIT. Results were published in Nature in 2024.

### Why this way

- No change. Standard academic register, and information isn't hidden by the passive
- De-AI is not forcing every English sentence into the active voice

### What not to change

- Don't force an academic abstract into colloquial sentences
- Don't delete the publication source for "being more direct"

## 8. Real debug dialogue with concrete evidence

### Original

Grad geschaut, die Root Cause ist der volle Verbindungspool, max_connections steht nur auf 20, zu Spitzenzeiten reicht das nicht. Ich hab ihn auf 100 gesetzt, eine halbe Stunde beobachtet, kein Fehler mehr.

### Recommended edit

Grad geschaut, die Root Cause ist der volle Verbindungspool, max_connections steht nur auf 20, zu Spitzenzeiten reicht das nicht. Ich hab ihn auf 100 gesetzt, eine halbe Stunde beobachtet, kein Fehler mehr.

### Why this way

- No change. Concrete params, action, and result here — normal engineering communication, not performative debug-speak
- What matters in this dialogue is information density, not forcing out spoken technical words

### What not to change

- Don't mechanically change `Root Cause` to something more formal or more colloquial
- Don't delete `20 -> 100` and `eine halbe Stunde beobachtet` — the key evidence

## 9. Mixed scene: tech blog embedding an incident postmortem

### Original

> Letzten Monat haben wir das Gateway von Nginx auf Envoy umgestellt. Dieser Beitrag erzählt, warum wir umgestellt haben und in welche Fallen wir getappt sind.
>
> Es ist wichtig zu beachten, dass in der heutigen, sich rasant entwickelnden Cloud-native-Zeit die Wahl einer wahrhaft team-befähigenden Gateway-Lösung zu einer nicht zu unterschätzenden Schlüsselfrage geworden ist.
>
> Am Umstellungstag gab es einen Vorfall. Postmortem:
>
> Root Cause: Envoys Default-Connection-Timeout ist 15 Sekunden, unser Long-Connection-Dienst braucht 300 Sekunden. Nach dem Umschalten des Traffics rissen alle Long Connections ab und lösten upstream massenhaft Reconnects aus. Fix: `idle_timeout` von 15s auf 300s, nach 2 Stunden Canary auf voll. Fehlerrate von 12 % auf 0,1 %.
>
> Zusammenfassend zeigt diese Migration eindrucksvoll das anhaltende Streben und den unermüdlichen Innovationsgeist des Teams. Die Zukunft ist vielversprechend!

### Scene call

1. **Main scene**: the whole piece is an external tech blog → main scene `public-writing`, default level `standard`
2. **Secondary scene**: a postmortem is embedded in the middle → local `docs` register
3. **Cap by the main scene's no-touch items**: `public-writing` doesn't force punchlines or hype tone

### Recommended edit

> Letzten Monat haben wir das Gateway von Nginx auf Envoy umgestellt. Dieser Beitrag erzählt, warum wir umgestellt haben und in welche Fallen wir getappt sind.
>
> Am Umstellungstag gab es einen Vorfall. Postmortem:
>
> Root Cause: Envoys Default-Connection-Timeout ist 15 Sekunden, unser Long-Connection-Dienst braucht 300 Sekunden. Nach dem Umschalten des Traffics rissen alle Long Connections ab und lösten upstream massenhaft Reconnects aus. Fix: `idle_timeout` von 15s auf 300s, nach 2 Stunden Canary auf voll. Fehlerrate von 12 % auf 0,1 %.

### Why this way

- **Second paragraph deleted whole**: hits throat-clearing opener (`Es ist wichtig zu beachten`), business jargon (`team-befähigend`), empty inflation (`Schlüsselfrage`) — inside the `public-writing` main scene's `standard` range
- **Postmortem paragraph kept as-is**: though "Root Cause" is a Tier 1 word, it's standard postmortem terminology here (false-positive protection #6), backed by concrete params and data — inside the secondary `docs` scene's protection
- **Last paragraph deleted whole**: summary ending + uplifting ending (`Zusammenfassend` `zeigt eindrucksvoll` `anhaltendes Streben` `unermüdlicher Innovationsgeist` `Die Zukunft ist vielversprechend`), all Tier 1 hits

### What not to change

- Don't change "Root Cause" in the postmortem to something else — this is technical postmortem register, not everyday chat
- Don't scatter the postmortem format — the terse "Root Cause → Fix → Result" structure is right in `docs` register
- Don't turn the blog opening into postmortem voice for register unity

## 10. "Anfragen auffangen" in a technical context

### Original

Das Gateway hat im Lasttest den Peak von 24.000 QPS aufgefangen, die Request-Timeout-Rate blieb stabil unter 0,3 %; Traffic über dem Schwellenwert geht automatisch in die Degradierung und macht den Downstream-Pool nicht weiter voll.

### Recommended edit

Das Gateway hat im Lasttest den Peak von 24.000 QPS aufgefangen, die Request-Timeout-Rate blieb stabil unter 0,3 %; Traffic über dem Schwellenwert geht automatisch in die Degradierung und macht den Downstream-Pool nicht weiter voll.

### Why this way

- No change. `auffangen` here means technical carrying capacity, its object is `Peak von 24.000 QPS`, with concrete metrics, system behavior, and a degradation boundary
- This is not the same as `Ich fange dich / alle sicher auf`; don't kill it just for the surface-word overlap

### What not to change

- Don't mechanically change `den Peak von 24.000 QPS aufgefangen` into a vague "Performance ist gut"
- Don't delete `0,3 %`, `Degradierung`, `Downstream-Pool` — the technical basis for the judgment
