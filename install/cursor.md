# Cursor / Windsurf install

## lite / full

- `lite`: load only `SKILL.md`. Good for quick rewrites and tight-context editing tasks.
- `full`: load `SKILL.md` + `references/`. Good for long-lived rules, public text, technical docs, and cases that need false-positive protection.

## Option 1: project rules

```bash
# Cursor
mkdir -p .cursor/rules
cp SKILL.md .cursor/rules/klartext.md

# Windsurf
mkdir -p .windsurf/rules
cp SKILL.md .windsurf/rules/klartext.md
```

The above is the lite usage. For the reference files (phrase tables, structural anti-patterns, etc.), create a `references/` folder in the same directory and copy them in, upgrading to full:

```bash
# Cursor
cp -r references .cursor/rules/

# Windsurf
cp -r references .windsurf/rules/
```

## Option 2: global rules

Paste the contents of `SKILL.md` into Cursor Settings > Rules.

## Note

A rules file is loaded into context, but that doesn't mean it auto-applies to all output. When you want it, say so explicitly:

```text
Rewrite this text with the klartext rules.
```

To first judge "where it sounds AI" without rewriting:

```text
Don't rewrite yet, just flag the problems in this text in annotation mode: ...
```

For unsourced citations, you can specify a mode:

```text
Rewrite this text with the klartext rules; handle unsourced citations as audit-only.
```

Three modes: `rewrite-safe` (default for chat/public-writing, delete unsupported authority framing), `audit-only` (default for docs/status, only flag the missing source), `rewrite-with-placeholder` (keep the structure but expose the missing source). Without one, the scene default applies.

Use lite when tokens are tight; use full when you need fine rewriting, Scene Packs, or false-positive protection.

## Three scopes for long-form rewrites

For long text (roughly 1000+ words of `public-writing`), you can specify one of three scopes, orthogonal to the strength level:

- `structural`: freely delete/merge/reorder, most thorough de-flavoring, but length is unpredictable (measured: the same piece may be -18% to -39%)
- `bounded` (long-form default): real sentences get only intra-sentence cleanup; whole empty sentences aren't deleted directly but listed as "Suggested deletions (to confirm)" for you to decide
- `in-place`: delete nothing, only lower tone intra-sentence, for "exactly as-is" requests

Just say it in the instruction, e.g. "Rewrite in bounded scope; list the whole empty sentences for me to confirm, don't delete them directly."

## Verification

```text
Rewrite this text with the klartext rules: In einer Zeit, in der KI die Softwareentwicklung grundlegend neu gestaltet, ist die Frage, wie man ein wahrhaft entwickler-befähigendes Tool schafft, zu einer nicht zu unterschätzenden Schlüsselfrage geworden.
```

If the output drops `grundlegend neu gestaltet / entwickler-befähigend / nicht zu unterschätzen / Schlüsselfrage` without scattering the information, it's wired up.
