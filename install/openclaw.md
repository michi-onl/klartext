# OpenClaw install

## lite / full

- `lite`: ship only `SKILL.md`. Good for tight tokens or basic rewrites.
- `full`: ship `SKILL.md` + `references/`. Good for long-lived workspaces, external text, technical docs, and cases that need false-positive protection.

## 1. Put the skill into the workspace

```bash
mkdir -p workspace/skills/klartext
cp SKILL.md workspace/skills/klartext/
cp -r references workspace/skills/klartext/
```

The above is the full usage. When tokens are tight, shipping only `SKILL.md` still does basic rewrites; `references/` makes scene detection and false-positive protection steadier.

## 2. Pick one trigger method

**Method A: on-demand trigger (default)**

Once the files are in `workspace/skills/`, OpenClaw decides when to enable the skill from its `name` and `description`. Say "rewrite this with the klartext rules" in the conversation and it triggers, no extra config.

**Method B: set as the default writing style**

To auto-apply to all external text, add to `workspace/SOUL.md`:

```markdown
## klartext
All external text (messages, docs, summaries, public writing) follows the rules in `skills/klartext/SKILL.md`.
Internal technical output (code, logs, config) is exempt.
```

## 3. Sync to the VM

```bash
git add workspace/skills/klartext
git commit -m "feat: add klartext skill"
git push
```

`git pull` on the VM makes it live. If the VM auto-pulls, it works right after push.

## Usage tips

To first judge "where it sounds AI" without rewriting:

```text
Don't rewrite yet, just flag the problems in this text in annotation mode: ...
```

For unsourced citations, you can specify a mode:

```text
Rewrite this text with the klartext rules; handle unsourced citations as audit-only.
```

Three modes: `rewrite-safe` (default for chat/public-writing, delete unsupported authority framing), `audit-only` (default for docs/status, only flag the missing source), `rewrite-with-placeholder` (keep the structure but expose the missing source). Without one, the scene default applies.

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

If the output drops `grundlegend neu gestaltet / entwickler-befähigend / nicht zu unterschätzen / Schlüsselfrage` without scattering the information, the skill is active.
