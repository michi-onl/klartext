# Structural Anti-patterns (cross-language)

> These are not word-level problems but sentence- and paragraph-level AI traces. Common to German and English.

## 1. Fake-dramatic binary contrast

**Pattern**: negate X, then affirm Y, to manufacture a false epiphany.

```
❌ Es ist kein technisches Problem, sondern ein Management-Problem.
❌ It's not about the code. It's about the culture.
```

```
✅ Der Management-Prozess geht leichter kaputt als der Code selbst.
✅ The culture around code review matters more than the code itself.
```

## 2. Negation-list buildup

**Pattern**: say what it isn't, then what it is. The long way around.

```
❌ Es ist kein Framework, keine Bibliothek, kein Werkzeug — es ist eine Denkweise.
❌ It's not a framework. It's not a library. It's a way of thinking.
```

```
✅ Sieh es als Denkmodell, nicht als konkretes Werkzeug.
✅ Think of it as a mental model, not a tool.
```

## 3. Dramatic sentence fragments

**Pattern**: sentence fragments manufacturing false force.

```
❌ Drei Jahre. Zwei Leute. Eine Idee.
❌ Three years. Two people. One idea.
```

```
✅ Zwei Leute haben drei Jahre gebraucht, um aus der Idee ein Produkt zu machen.
✅ Two people spent three years turning the idea into a product.
```

## 4. Rhetorical-question setup

**Pattern**: open with a rhetorical question or "what if" to bait.

```
❌ Was, wenn ich dir sage, dass 90 % der Start-ups denselben Fehler machen?
❌ What if I told you 90% of startups make the same mistake?
```

```
✅ 90 % der Start-ups bepreisen falsch: nach Kosten statt nach Wert.
✅ 90% of startups misprice their product, using cost-based pricing instead of value-based.
```

## 5. False agency

**Pattern**: give lifeless things human actions ("befähigt", "treibt an", "ermöglicht"). Rewrite when the sentence is abstract and empty. A non-human subject describing system behavior in technical docs ("das Gateway gibt 504 zurück", "der Cache läuft ab") is fine and needs no change.

```
❌ Das Framework befähigt die Entwickler-Community.
❌ The framework empowers the developer community.
```

```
✅ Mit diesem Framework schreiben Entwickler 30 % weniger Boilerplate.
✅ Developers write 30% less boilerplate with this framework.
✅ Das Gateway gibt nach dem Timeout 504 zurück. (technical description, unchanged)
```

## 6. Stacked passive voice

**Pattern**: consecutive passives hiding the actor. Normal passive in papers, lab reports, or formal academic abstracts need not change.

```
❌ Nachdem das System optimiert wurde, wurde die Leistung deutlich gesteigert und das Nutzererlebnis erheblich verbessert.
❌ The system was optimized, performance was improved, and user experience was enhanced.
```

```
✅ Wir haben die Datenbank-Queries optimiert, die Ladezeit fiel von 3 s auf 0,8 s.
✅ We optimized database queries and cut page load time from 3s to 0.8s.
```

```
✅ Das Experiment wurde von Forschenden am MIT durchgeführt. (academic register, keep)
```

## 7. Rule-of-three lists

**Pattern**: AI loves groups of three. Two or one is often more natural.

```
❌ Innovation, Zusammenarbeit, Exzellenz.
❌ Innovation, collaboration, and excellence.
```

```
✅ Bau die Sachen, und bau sie gut.
✅ Build things. Build them well.
```

## 8. Mechanical "Erstens … zweitens … abschließend …"

**Pattern**: mechanical enumeration that manufactures false logic.

```
❌ Zunächst müssen wir das Ziel definieren; anschließend einen Plan erstellen; abschließend die Umsetzung angehen.
```

```
✅ Erst das Ziel klar machen, dann Prioritäten setzen, und beim Machen nachjustieren.
```

## 9. Wh- opening sentences (English-specific)

**Pattern**: sentences opening with What/When/Where/Which/Who/Why/How over-cluster in AI text.

```
❌ What makes this approach unique is its simplicity.
```

```
✅ This approach works because it's simple.
```

## 10. Summary endings

**Pattern**: end each paragraph or the whole text with "zusammenfassend"/"alles in allem", repeating what was said.

```
❌ Zusammenfassend lässt sich sagen, dass der Ansatz in Leistung, Sicherheit und Wartbarkeit überzeugt.
❌ In conclusion, this approach excels in performance, security, and maintainability.
```

```
✅ Löschen. Wenn du es oben klar gesagt hast, sag es nicht nochmal.
✅ Delete it. If you said it clearly above, don't repeat it.
```

## 11. Symmetry padding

**Pattern**: forced parallelism for "balance", with no information gain.

```
❌ Wir wollen sowohl Geschwindigkeit als auch Qualität; sowohl Innovation als auch Zuverlässigkeit.
```

```
✅ Zwischen Geschwindigkeit und Qualität priorisieren wir Qualität.
```

## 12. Unsourced citations

**Pattern**: "Studien zeigen"/"Daten belegen"/"Experten sagen" without a concrete source, manufacturing false authority.

```
❌ Studien zeigen, dass Homeoffice die Produktivität um 30 % steigert.
❌ Studies show that remote work increases productivity by 30%.
```

```
✅ Ein Stanford-Experiment von 2023 fand, dass voll remote arbeitende Mitarbeitende 13 % mehr Code committen als Hybrid-Arbeitende.
✅ A 2023 Stanford experiment found fully remote employees committed 13% more code than hybrid workers.
```

## 13. Bold abuse

**Pattern**: mechanically bold every bullet lead to fake hierarchy.

```
❌ **Nutzererlebnis:** Oberfläche rundum erneuert. **Performance:** Algorithmus deutlich verbessert. **Sicherheit:** Ende-zu-Ende-Verschlüsselung neu.
```

```
✅ Die Oberfläche wurde neu gestaltet, der Algorithmus ist 2x schneller, Ende-zu-Ende-Verschlüsselung ist dazugekommen.
```

## 14. Compulsive bullet-pointing

**Pattern**: everything must be 1. 2. 3., even a simple reply, faking orderliness.

```
❌ Zu deiner Frage mein Vorschlag:
   1. Zuerst die Konfigurationsdatei prüfen
   2. Umgebungsvariablen bestätigen
   3. Dienst neu starten
```

```
✅ Vielleicht steht in der Config das DB_HOST falsch, schau da mal. Wenn nicht, starte den Dienst neu.
```

## 15. Compulsive uplifting ending

**Pattern**: whatever came before, the last paragraph must add value, sprinkle inspiration, look to the future.

```
❌ … Kurzum, lasst uns den Wandel annehmen und die grenzenlosen Möglichkeiten des KI-Zeitalters aktiv gestalten! Die Zukunft ist vielversprechend!
```

```
✅ Löschen. Wenn oben alles gesagt ist, hör auf.
```

## 16. Fake colloquialism / forced influencer voice

**Pattern**: when AI tries to be "relatable", it stuffs in influencer/clickbait phrasing ("absoluter Gamechanger", "ihr werdet es nicht glauben", "Zeit für Klartext"), which reads faker. Real people use these randomly; AI does it in bulk.

```
❌ Leute, dieses Tool ist ein absoluter Gamechanger! Ihr werdet es nicht glauben, die Produktivität geht durch die Decke! Unbedingt speichern!
```

```
✅ Das Tool ist wirklich brauchbar, vor allem weil die Stapelverarbeitung schnell ist — spart mir einiges an Zeit.
```

## 17. Debug-speak narrative

**Pattern**: AI narrates everyday matters in postmortem/SRE voice — "eingegrenzt", "dichtgemacht", "Root Cause", "abgeräumt" — generalizing debug jargon to all conversation.

```
❌ Ich habe die Differenz eingegrenzt, die Root Cause steht im Grunde fest, als Nächstes räume ich das mit einem härteren Ausschlussverfahren ab.
```

```
✅ Die Ursache ist gefunden: ein abgelaufener Cache. Ich hab die Möglichkeiten durchgegangen, jetzt bleibt nur die eine.
```

## 18. Uniform sentence length (statistical signal)

**Pattern**: AI text has nearly identical sentence lengths (length stdev ~1.2 vs ~4.7+ for humans). It reads "flat, no breathing room".

**Detection**: don't look at a single word — look at whether the whole paragraph's rhythm is monotone. Long and short sentences should alternate.

## 19. Value-inflation skeleton

**Pattern**: give a fact, then lift it into "insight" with `nicht nur … sondern auch …`, `wahre X ist nicht … sondern …`, `am Ende zählt …`.

```
❌ Das ist nicht nur ein Produkt, sondern die Weitergabe einer Überzeugung.
❌ Wahre Wettbewerbsfähigkeit ist nicht Feature-Masse, sondern das Detail im Erlebnis. Am Ende zählt die Umsetzung.
```

```
✅ Das ist eine Produktentscheidung: das Detail im Erlebnis entscheidet, ob es langfristig benutzt wird.
✅ Egal wie viele Features — am Ende zählen Erlebnisdetails und Umsetzung.
```

## 20. Punctuation tic (em-dash overload)

**Pattern**: overusing the Gedankenstrich (—) — opening with one, several `—` per paragraph, insertions, turns, and additions all carried by dashes; often paired with semicolon runs. A cross-model phenomenon that prompts often can't suppress.

**Detection**: look at density and position, not a single occurrence. Signals: dash at the very start, 2+ `—` in one paragraph, several consecutive paragraphs leaning on dashes. A single dash is not a problem — don't kill on sight.

```
❌ Was mich am Tool am meisten überzeugt, ist die Geschwindigkeit — es öffnet direkt mit Ergebnis. Suche, Start, Zwischenablage — alles in einem Eingabefeld — du musst dir nicht mal Shortcuts merken.
```

```
✅ Was mich am Tool am meisten überzeugt, ist die Geschwindigkeit: es öffnet direkt mit Ergebnis. Suche, Start, Zwischenablage, alles in einem Eingabefeld, du musst dir nicht mal Shortcuts merken.
```

**Default action**: turn excess dashes back into colons, commas, parentheses, or full stops by meaning; keep at most one real insertion/build-up dash per paragraph.

**Keep when**: connectors in titles and names (`todo — Terminal-Aufgaben`); quoted text; the dash itself is the topic; the only dash in a paragraph that genuinely carries an insertion.

## 21. Nominalstil overload (German-specific)

**Pattern**: German AI text piles on nominalizations and Streckverben ("eine Optimierung vornehmen", "zur Anwendung bringen", "unter Berücksichtigung von"), turning verbs into noun+light-verb constructions. It reads bureaucratic and agent-less.

```
❌ Im Rahmen der Prozessoptimierung wurde eine Verbesserung der Durchlaufzeiten unter Berücksichtigung der Ressourcenverfügbarkeit erzielt.
```

```
✅ Wir haben den Prozess umgestellt, dadurch laufen die Aufträge schneller durch — soweit die Leute frei sind.
```

**Default action**: resolve Streckverben back to a full verb, give the sentence a real subject, and cut `im Rahmen von / vor dem Hintergrund / unter Berücksichtigung` where they only pad.
