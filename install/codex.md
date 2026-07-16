# Codex install / usage

## lite / full

- `lite`: load only `SKILL.md`. Good for one-off rewrites, tight context, or just cutting the obvious template feel.
- `full`: load `SKILL.md` + `references/`. Good for long-lived projects, README / release note / issue replies, technical docs, and cases that need false-positive protection.

## Option 1: long-term project use (recommended)

Put the skill files into the project:

```bash
mkdir -p klartext
cp SKILL.md klartext/
cp -r references klartext/
```

This is the full usage and the default recommendation for long-term project use.

Write the trigger condition and boundary into `AGENTS.md`:

```markdown
## Writing style
When a task involves "de-AI", "auf Deutsch natürlicher", "sound human", "not like a template", follow `klartext/SKILL.md`.
Apply it to external text first; don't apply it to code, logs, config, or command output.
```

This way the rules are versioned with the project and reusable across the team.

## Option 2: one-off rewrite

Run in the repo root and have Codex read `SKILL.md` before rewriting:

```bash
codex exec -C . "Read ./SKILL.md and rewrite the following text by its rules: ..."
```

No project changes needed; good for occasional use. This is the lite usage; for public text, technical boundaries, or Scene Packs, also have Codex read the relevant files under `references/`.

To first judge "where it sounds AI" without rewriting:

```bash
codex exec -C . "Read ./SKILL.md and, in annotation mode only, flag the problems in the following text: ..."
```

## Option 3: global AGENTS

First put the full rules into a local skill directory:

```bash
mkdir -p ~/.codex/skills/klartext
cp SKILL.md ~/.codex/skills/klartext/
cp -r references ~/.codex/skills/klartext/
```

This is the full usage. Copying only `SKILL.md` also works, but false-positive protection and scene detail are weaker.

Then write a trigger entry into the global `AGENTS.md`:

```bash
mkdir -p ~/.codex
cat >> ~/.codex/AGENTS.md <<'EOF'
When a task involves "de-AI", "auf Deutsch natürlicher", "sound human", "not like a template", use the local skill `klartext`.
Apply it to external text first; don't apply it to code, logs, config, or command output.
EOF
```

The global entry should carry only the trigger condition; don't paste the whole `SKILL.md` into global rules. Keep the full rules in the project or a local skill dir and read them on demand.

## Note

"Installed a skill" does not mean Codex will unconditionally apply all rules. You need to give it a clear trigger entry (`AGENTS.md`, a project prompt, or an explicit "read `SKILL.md`" in a single task) before it handles text by the rules.

## Three scopes for long-form rewrites

For long text (roughly 1000+ words of `public-writing`), you can specify one of three scopes, orthogonal to the strength level:

- `structural`: freely delete/merge/reorder, most thorough de-flavoring, but length is unpredictable (measured: the same piece may be -18% to -39%)
- `bounded` (long-form default): real sentences get only intra-sentence cleanup; whole empty sentences aren't deleted directly but listed as "Suggested deletions (to confirm)" for you to decide
- `in-place`: delete nothing, only lower tone intra-sentence, for "exactly as-is" requests

Just say it in the instruction, e.g. "Rewrite in bounded scope; list the whole empty sentences for me to confirm, don't delete them directly."

## Verification

```text
Rewrite with klartext rules: In einer Zeit, in der KI die Softwareentwicklung grundlegend neu gestaltet, ist die Frage, wie man ein wahrhaft entwickler-befähigendes Tool schafft, zu einer nicht zu unterschätzenden Schlüsselfrage geworden.
```

If the output drops `grundlegend neu gestaltet / entwickler-befähigend / nicht zu unterschätzen / Schlüsselfrage` without emptying the information, it's wired up.
