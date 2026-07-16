# Severity

> Not every AI-flavored word should be cut wholesale. Tiered handling reduces false positives and keeps natural expression.

## Tier definitions

### Tier 1: Replace by default

**Definition**: appears 5–20x more often in AI-generated text than in human text.

**Handling**: replace with something concrete or delete by default. But keep it under false-positive protection (below).

**Typical German words**: von entscheidender Bedeutung, es ist wichtig zu beachten, zusammenfassend lässt sich sagen, bahnbrechend, wegweisend, leveragen, aufs nächste Level heben, ganzheitlich, Mehrwert generieren, zielführend, Deep Dive, Gamechanger, eine Optimierung vornehmen, stellt … dar, ebnet den Weg für

**Typical English words**: delve, landscape, tapestry, leverage, pivotal, testament, showcases, underscores, nestled, vibrant, groundbreaking, game-changer, serves as

---

### Tier 2: Flag when clustered in one paragraph

**Definition**: perfectly fine alone, but a signal of AI flavor when clustered in one paragraph (threshold below).

**Handling**: keep the single best-fitting one, replace or rephrase the rest.

**Length reference**:
- Short paragraph (< 100 words): flag at 2+ in one paragraph
- Long paragraph (≥ 100 words): flag at 3+; two scattered across different spots of a long paragraph may pass

**Typical German words**: zudem, darüber hinaus, des Weiteren, gleichzeitig, folglich, maßgeblich, essenziell, facettenreich, nahtlos, dynamisch, transformativ, Eckpfeiler

**Typical English words**: harness, navigate, foster, elevate, unleash, nuanced, crucial, multifaceted, transformative, cornerstone, paramount

---

### Tier 3: Flag at high whole-text density

**Definition**: normal common words, only a problem when their whole-text frequency is clearly above normal writing.

**Method**: normalize by text length —
- Short text (< 200 words): the same Tier 3 word appears 3+ times
- Medium text (200–1000 words): the same Tier 3 word appears 5+ times
- Long text (> 1000 words): the same Tier 3 word is > 0.5% of words

**Handling**: replace some occurrences with synonyms, or rephrase to reduce repetition.

**Typical German words**: wichtig, entscheidend, zentral, innovativ, optimieren, verbessern, ermöglichen, gewährleisten, sicherstellen, fördern

**Typical English words**: significant, innovative, effective, dynamic, compelling, unprecedented, exceptional, comprehensive, robust, seamless

---

## Decision flow

```
suspicious word
  ├─ hits false-positive protection? → yes → pass
  ├─ in the Tier 1 list? → replace by default
  ├─ in the Tier 2 list?
  │    ├─ short paragraph and 2+ in it? → flag, keep one
  │    ├─ long paragraph and 3+ in it? → flag, keep one
  │    └─ below threshold? → pass
  └─ in the Tier 3 list?
       ├─ over density threshold? → replace some
       └─ under? → pass
```

## False-positive protection

Even on a table hit, do not change in these cases:

1. **Quoted text**: keep others' words or source-document text as-is
2. **Term definitions**: when the word itself is the object under discussion (e.g. "what does 'ganzheitlich' mean")
3. **Code / config**: technical names, variable names, API names are not changed
4. **Industry-specific context**: some words are standard terms in a field (e.g. "Hebel"/leverage in finance)
5. **System subjects in technical description**: when describing a system, service, or component's behavior, a non-human subject is fine (e.g. "das Gateway gibt 504 zurück")
6. **Engineering terms in technical reports**: in postmortems, incident reports, and changelogs, terms like "Root Cause", "Konvergenz", "Regression" are standard, not to be replaced
7. **Real colloquial web language**: when a blogger naturally uses "reingefallen", "wer kennt's nicht" after concrete experience with real detail, that is not AI-speak
8. **Literal English technical verbs**: `navigate`, `traverse`, `route` in graph algorithms, network topology, path search may be kept
9. **Normal passive in academic or experimental register**: `wurde durchgeführt`, `wurde veröffentlicht` in papers and lab reports should not be mechanically rewritten
10. **Real debug dialogue with concrete evidence**: if the dialogue has concrete parameters, actions, durations, and observed results, technical colloquialisms like `Root Cause`, `dichtgemacht` may be kept
11. **English words inside German sentences (Denglisch)**: judge by the word's actual meaning in the current sentence, don't mechanically apply the `phrases-en` table. `Der Leverage-Punkt liegt im Cache` — `Leverage` is business jargon, handle it; `mit 10x Leverage shorten` — `Leverage` is a finance term, keep it
12. **German register / address form**: do not flip Sie ↔ du to "sound more human"; the address form is part of fidelity, not flavor
