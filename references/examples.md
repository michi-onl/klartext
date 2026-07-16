# Rewrite Examples

> Each example shows the AI version and the human version of the same content.

## German examples

### Example 1: Project intro

**AI version:**
> Dieses Projekt ist eine innovative Lösung, die durch die tiefe Integration verschiedenster Spitzentechnologien ein ganzheitliches, nahtloses und intelligentes Nutzererlebnis bietet. Es steigert nicht nur die Effizienz erheblich, sondern senkt zugleich effektiv die Betriebskosten und realisiert echte Kosteneinsparung bei gleichzeitiger Wertsteigerung.

**Human version:**
> Das Projekt verbindet Spracherkennung mit automatischer Übersetzung: Man spricht Deutsch, raus kommen englische Untertitel. Zwei Wochen nach Launch 1200 tägliche Nutzer, Übersetzungsgenauigkeit 94 %.

**What changed:**
- Deleted "innovativ", "Spitzentechnologien", "ganzheitlich", "nahtlos", "intelligent" — all empty words
- Deleted the "nicht nur … sondern auch …" binary structure
- Added concrete functionality and data

---

### Example 2: Technical summary

**AI version:**
> Zusammenfassend haben wir durch die umfassende Optimierung und kontinuierliche Weiterentwicklung der Systemarchitektur in Performance, Sicherheit und Wartbarkeit deutliche Fortschritte erzielt. Dieses Ergebnis zeugt eindrucksvoll vom unermüdlichen Streben und der herausragenden Kompetenz des Teams im Bereich technischer Innovation.

**Human version:**
> Nach dieser Runde: API-Antwortzeit von 800 ms auf 120 ms, 3 SQL-Injection-Lücken gefixt, die God-Class mit 6000 Zeilen in 12 Module zerlegt.

**What changed:**
- Deleted "Zusammenfassend" and the whole summary opener
- "deutliche Fortschritte" → concrete data
- Deleted "zeugt eindrucksvoll", "unermüdliches Streben", "herausragende Kompetenz" — self-praise
- Replaced abstract description with concrete changes

---

### Example 3: Message reply

**AI version:**
> Großartige Frage! Das ist in der Tat ein Thema, das eine tiefere Betrachtung verdient. Lass mich dir das im Detail erklären. Zunächst müssen wir verstehen, dass der Kern dieses Problems darin liegt …

**Human version:**
> Der Kern ist, dass der Cache nicht invalidiert wird. Der Nutzer ändert das Avatar, aber das CDN liefert das alte — die TTL steht auf 7 Tage, das ist zu lang. Auf 1 Stunde stellen, dann passt es.

**What changed:**
- Deleted all sycophancy and buildup
- Gave the cause and the fix directly

---

### Example 4: News summary

**AI version:**
> Im heutigen, sich rasant entwickelnden Bereich der künstlichen Intelligenz hat OpenAI kürzlich sein neuestes großes Sprachmodell veröffentlicht, was in der Branche breite Aufmerksamkeit und rege Diskussionen auslöste. Das Modell erzielte bei mehreren Schlüsselmetriken einen deutlichen Durchbruch und markiert den Eintritt der KI-Technologie in eine völlig neue Entwicklungsphase.

**Human version:**
> OpenAI hat GPT-5 veröffentlicht. MMLU-Score 92,3 %, 7 Punkte über der Vorgängerversion. Das Kontextfenster verdoppelt sich auf 256K. Der API-Preis bleibt gleich.

**What changed:**
- Deleted "Im heutigen", "rasant entwickelnd", "breite Aufmerksamkeit", "rege Diskussionen" — all filler
- "deutlicher Durchbruch" → concrete score
- Deleted "völlig neue Entwicklungsphase" — the reader can judge that

---

### Example 5: Engineer-speak / debug-speak

**AI version:**
> Ich hab es erst mal aufgebohrt, die Root Cause sitzt tief, lässt sich nicht direkt plattmachen. Aktuell die Differenz eingegrenzt, deckt sich mit dem grad gesehenen Phänomen. Als Nächstes sauber auffangen, nach dem Festzurren kann ich es dichtmachen.

**Human version:**
> Geschaut: die Ursache ist ein hartcodierter Wert, den man nicht direkt ändern kann. Ich hab die Suche auf zwei mögliche Stellen eingegrenzt, das passt zur früheren Fehlermeldung. Ich schreib das Ergebnis auf, in einer Runde bau ich es um.

**What changed:**
- "aufgebohrt" → "geschaut", "Root Cause sitzt tief" → "die Ursache ist ein hartcodierter Wert"
- "plattmachen" → "ändern", "eingegrenzt" kept once as plain, "grad gesehenes Phänomen" → "Fehlermeldung"
- "auffangen" → deleted, "Festzurren" → "aufschreiben", "dichtmachen" → "umbauen"
- The whole passage moved from postmortem voice to normal colleague talk

---

### Example 6: Influencer / clickbait AI voice

**AI version:**
> Leute!! Heute ein absoluter Geheimtipp für euch! Dieses Tool ist ein echter Gamechanger, die Produktivität geht komplett durch die Decke! Unbedingt speichern! Wichtig: kostenlos!!

**Human version:**
> Empfehlung: Raycast. Die Gratis-Version reicht, vor allem schneller Start und viele Plugins. Ich hatte vorher Alfred; nach dem Wechsel spare ich täglich vielleicht zehn, fünfzehn Minuten, hauptsächlich beim Fensterwechsel und beim Nachschlagen.

**What changed:**
- Deleted all forced-persona influencer language
- "Geheimtipp", "Gamechanger", "durch die Decke", "unbedingt speichern" all cut
- Replaced with the concrete tool name, concrete usage, concrete time saved

---

### Example 7: Register mixing

**AI version:**
> Zugegeben, der Fix dieses Bugs hat durchaus eine gewisse technische Komplexität. Aber ganz ehrlich, das Erlebnis ist einfach ein Gamechanger! Wir müssen die zugrundeliegende Logik tiefer beleuchten und die Kernstrecke sauber auffangen. Zusammenfassend: Die Zukunft ist vielversprechend.

**Human version:**
> Der Bug ist schwer zu fixen, es geht um die Aufrufreihenfolge zwischen drei Diensten. Ich setze erst mal das Timeout des Bezahldienstes von 3 auf 10 Sekunden und beobachte eine Woche.

**What changed:**
- The original mixed 4 registers (academic / influencer / business / engineer / inspirational), unified to technical colloquial
- Replaced vague description with a concrete plan

---

## English Examples

### Example 1: Product description

**AI version:**
> Our groundbreaking platform serves as a testament to the transformative potential of AI, empowering teams to navigate complex challenges and unlock unprecedented levels of productivity. Nestled at the intersection of innovation and practicality, it showcases how cutting-edge technology can foster meaningful collaboration.

**Human version:**
> The platform auto-assigns tickets based on who fixed similar bugs before. Teams using it close issues 2 days faster on average.

**What changed:**
- Removed "groundbreaking", "testament", "empowering", "navigate", "unprecedented", "nestled", "showcases", "cutting-edge", "foster"
- Replaced vague claims with specific functionality and data

---

### Example 2: Technical update

**AI version:**
> We're excited to announce a comprehensive update that significantly enhances performance, bolsters security, and streamlines the developer experience. This pivotal release underscores our commitment to delivering robust, scalable solutions.

**Human version:**
> This release cuts cold start time by 60%, patches CVE-2024-3891, and drops the config from 200 lines to 40. Upgrade guide is in the changelog.

**What changed:**
- "Comprehensive update" → specific changes
- "Significantly enhances" → "cuts by 60%"
- "Bolsters security" → specific CVE
- "Streamlines developer experience" → specific config reduction
- Deleted "pivotal", "underscores", "commitment", "robust", "scalable"

---

### Example 3: Analysis (two-pass demo)

**AI version:**
> The landscape of remote work has undergone a profound transformation. It's not just about working from home — it's about reimagining the very fabric of how we collaborate. Companies that fail to navigate this paradigm shift risk being left behind in an increasingly competitive ecosystem.

**First pass:**
> Remote work changed how teams collaborate. The teams that leaned into async communication and cut meetings adapted faster.

**Audit — what still feels AI?**
- "changed how teams collaborate" is still broad
- "adapted faster" is vague and a bit polished

**Final:**
> Remote work changed how teams collaborated, but not every company adjusted in the same way. Some changed how they communicated and worked together. Others just kept the same habits in a different setting.

**What changed in second pass:**
- Replaced the broad opener with a clearer contrast that stays inside the original claim
- Removed the vague "adapted faster"
- Broke the rhythm a bit without inventing new facts

---

## Two-pass examples | Residual Audit

### Example A: one pass vs two passes in public writing

**Original:**
> Wir haben den Onboarding-Flow überarbeitet, neue Nutzer sparen von der Registrierung bis zum ersten Import zwei Schritte. Noch wichtiger: das zeigt, dass wir langsam wirklich verstehen, wo Nutzer am ersten Tag am ehesten hängen bleiben.

**First pass:**
> Wir haben den Onboarding-Flow überarbeitet, neue Nutzer sparen von der Registrierung bis zum ersten Import zwei Schritte. Wir wissen jetzt auch besser, wo Nutzer am ersten Tag am ehesten hängen bleiben.

**Second pass:**
> Wir haben den Onboarding-Flow überarbeitet, neue Nutzer sparen von der Registrierung bis zum ersten Import zwei Schritte. Wo Nutzer am ersten Tag am ehesten hängen bleiben, ist genau der erste Import.

**What the second pass changed:**
- Removed the narrator layer `Noch wichtiger / das zeigt, dass wir wirklich verstehen`
- Kept the original judgment, only pushed it into a more direct sentence
- Added no new facts, and did not rewrite the whole paragraph

### Example B: a restrained second pass in a status scene

**Original:**
> Am 13. April die Retries von 2 auf 5 gesetzt. Payment-Timeouts von 1,9 % auf 0,7 %. Diese Änderung bestätigt zudem, dass unsere Optimierungsrichtung stimmt. Morgen weiter die Abend-Peak-Daten anschauen.

**First pass:**
> Am 13. April die Retries von 2 auf 5 gesetzt, danach Payment-Timeouts von 1,9 % auf 0,7 %. Die Änderung zeigt, dass die Richtung stimmt. Morgen weiter die Abend-Peak-Daten anschauen.

**Second pass:**
> Am 13. April die Retries von 2 auf 5 gesetzt, danach Payment-Timeouts von 1,9 % auf 0,7 %. Morgen weiter die Abend-Peak-Daten anschauen.

**What the second pass changed:**
- Only deleted the empty judgment `die Richtung stimmt`
- Kept date, numbers, and next step; didn't polish toward colloquial
- In a `status` scene, if pass 1 is already direct enough, pass 2 stops here

---

## Bounded dual-contract example

> A bounded output has two parts: the intra-sentence-cleaned body, and a deletion list for the user to confirm. Example (synthetic text):

**Original**

> In einer Zeit, in der die Digitalisierung alle Branchen erfasst, gibt es unzählige Effizienz-Tools. Unser Team hat in den letzten drei Monaten den Wochenbericht von manuellem Excel auf einen Bot umgestellt, der automatisch zusammenfasst — das spart wöchentlich etwa zwei Stunden. Studien zeigen, dass die Automatisierung repetitiver Aufgaben die Organisationseffizienz deutlich steigert. Konkret: Der Bot zieht freitags die Statusänderungen aus dem Task-System, erzeugt einen Entwurf, und die Verantwortlichen ergänzen nur einen Satz zum Risiko. Das ist nicht nur eine Prozessoptimierung, sondern eine Erneuerung der Arbeitsweise. Nächsten Monat wollen wir auch die Meeting-Protokolle anbinden.

**Body (intra-sentence cleaned)**

> Es gibt viele Effizienz-Tools. Unser Team hat in den letzten drei Monaten den Wochenbericht von manuellem Excel auf einen Bot umgestellt, der automatisch zusammenfasst — das spart wöchentlich etwa zwei Stunden. Konkret: Der Bot zieht freitags die Statusänderungen aus dem Task-System, erzeugt einen Entwurf, und die Verantwortlichen ergänzen nur einen Satz zum Risiko. Nächsten Monat wollen wir auch die Meeting-Protokolle anbinden.

**Suggested deletions (to confirm)**

1. „Studien zeigen, dass die Automatisierung repetitiver Aufgaben die Organisationseffizienz deutlich steigert." — unsourced authority framing; deleting it leaves the paragraph's information unchanged (the surrounding sentences already give the method and the benefit), and it carries no transition. Don't rewrite it into "angeblich / man hört", which only reshells the unsourced claim.
2. „Das ist nicht nur eine Prozessoptimierung, sondern eine Erneuerung der Arbeitsweise." — value-inflation ending; stripping the pattern leaves no information, and the previous sentence (concrete method) connects directly to the next (next month's plan) without a break.

The first sentence "In einer Zeit … unzählige Tools" did not go on the list: stripping the buildup still leaves the real judgment "es gibt viele Effizienz-Tools", so it's cleaned intra-sentence, not deleted whole.

---

## Annotation mode examples

> These pairs show the same text under `annotation mode` vs the default rewrite mode.

### Example A: unsourced citation in public copy

**Original:**
> Studien zeigen, dass Teams mit KI-gestützter Entwicklung ihre Liefergeschwindigkeit deutlich steigern. Fachleute meinen, dieser Trend werde sich im kommenden Jahrzehnt weiter beschleunigen.

**Annotation mode:**
- `Problem family`: unsourced citation
- `Trigger`: `Studien zeigen`, `Fachleute meinen`
- `Suggested action`: add a concrete source; if none, delete the authority framing
- `Rewrite recommended`: yes

**Default rewrite:**
> Teams mit KI-gestützter Entwicklung liefern womöglich schneller, aber der Satz gibt keine konkrete Quelle. Entweder eine Studienquelle ergänzen, oder die Aussage direkt zurückhaltender formulieren.

### Example B: conservative handling in a status scene

**Original:**
> Die Daten zeigen, dass dieses Redesign die Retention deutlich gesteigert hat. Fachleute meinen, diese Richtung sei bereits als tragfähig bestätigt.

**Annotation mode:**
- `Problem family`: unsourced citation
- `Trigger`: `Die Daten zeigen`, `Fachleute meinen`
- `Suggested action`: in a `status` scene, prefer adding the data source and attribution; don't rewrite it as an established fact
- `Rewrite recommended`: yes

**Default rewrite:**
> Diesem Absatz fehlen Datenquelle und Zuordnung. Als Status sollte der Sync konkrete Reports, Zeitraum oder Verantwortliche ergänzen; bis dahin nicht als bestätigtes Ergebnis schreiben.

### Example C: no-change case in technical docs

**Original:**
> Das Gateway gibt nach einem Request-Timeout 504 zurück. Der Cache-Dienst aktualisiert die Hot Keys alle 5 Minuten. Der Load Balancer verteilt den Traffic gewichtet auf drei Backend-Knoten.

**Annotation mode:**
- `Problem family`: no obvious problem
- `Trigger`: system subjects and technical terms are normal doc writing
- `Suggested action`: leave unchanged
- `Rewrite recommended`: no

**Default rewrite:**
> Das Gateway gibt nach einem Request-Timeout 504 zurück. Der Cache-Dienst aktualisiert die Hot Keys alle 5 Minuten. Der Load Balancer verteilt den Traffic gewichtet auf drei Backend-Knoten.
