# Claude Code install

## Option 1: plugin, one command (recommended)

```text
/plugin marketplace add michi-onl/shuorenhua
/plugin install klartext@klartext
```

Run these two commands in a Claude Code conversation; the skill is discovered and triggered automatically. Upgrade via the `/plugin` panel or `claude plugin update klartext`.

The plugin ships all files (`SKILL.md` + `references/`), so the lite / full split is no longer needed. If you already installed manually via options 2–4 below, remove the old install first to avoid the same skill triggering twice.

## lite / full (for manual installs)

- `lite`: load only `SKILL.md`. Good for quick rewrites and light review.
- `full`: load `SKILL.md` + `references/`. Good for project-level installs, public text, technical docs, and cases that need false-positive protection.

Claude Code discovers and triggers skills in the skills directory based on the `description` at the top of `SKILL.md` — ready to use once installed.

## Option 2: project-level

```bash
mkdir -p .claude/skills/klartext
cp SKILL.md .claude/skills/klartext/
cp -r references .claude/skills/klartext/
```

This is the full usage and the default recommendation for project-level installs. The rules go into version control with the project; teammates get it on clone.

## Option 3: global

```bash
git clone https://github.com/michi-onl/shuorenhua.git
mkdir -p ~/.claude/skills
cp -r shuorenhua ~/.claude/skills/klartext
```

Copy the whole repo in; the extra evals and install files don't affect triggering. For a minimal install, copy only `SKILL.md` (lite) or `SKILL.md` + `references/` (full).

## Option 4: follow updates

```bash
git clone https://github.com/michi-onl/shuorenhua.git
ln -s "$PWD/shuorenhua" ~/.claude/skills/klartext
```

The symlink points at your local repo, so `git pull` upgrades it — no re-copying.

## Trigger note (optional)

Claude Code triggers this skill automatically from the description at the top of `SKILL.md`. To improve hit stability in a long-lived project, or to restrict it to external text, add a trigger note to the project's `CLAUDE.md` (optional, not required):

```markdown
## Writing style
When a task involves "de-AI", "auf Deutsch natürlicher", "sound human", "not like a template", follow `.claude/skills/klartext/SKILL.md`.
Apply it to external text first; don't apply it to code, logs, config, or command output.
```

## Usage

Just say, in the conversation:

```text
Rewrite this text with the klartext rules.
```

Or more specifically:

```text
Lightly edit this status update with the klartext rules; keep the terms and system subjects, don't turn it into casual chat.
```

To first judge "where it sounds AI" without rewriting:

```text
Don't rewrite yet, just flag the problems in this text in annotation mode: ...
```

Good for:

- You want to see first whether this text should change
- You're doing review, not rewriting for the author
- You suspect unsourced citations, register mixing, or engineer-speak, but don't want to touch the body yet

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
In einer Zeit, in der KI die Softwareentwicklung grundlegend neu gestaltet, ist die Frage, wie man ein wahrhaft entwickler-befähigendes Tool schafft, zu einer nicht zu unterschätzenden Schlüsselfrage geworden.
```

If the output drops `grundlegend neu gestaltet / entwickler-befähigend / nicht zu unterschätzen / Schlüsselfrage` and doesn't scatter the information, it's wired up.
