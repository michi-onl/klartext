# Repository guide

This is **klartext**, a German-English fork of [shuorenhua (说人话)](https://github.com/MrGeDiao/shuorenhua). Same method (scenes, Tiers, scopes, reread contract); the target languages are German and English, and the phrase tables and examples are re-derived for German.

## Language

- The skill's instructional prose (`SKILL.md`, `references/`, `install/`) is **English-first**. This is the meta language; keep it consistent.
- The **target** languages the skill cleans are German and English. Phrase tables, examples, and eval samples are German (+English).
- Keep code, file paths, command names, API names, and settled technical terms in their original form; don't translate where translation reduces clarity.

## Style

- Follow the repo's existing tone: direct, concrete, low-ceremony, no translationese.
- German example text is German-framed; keep only the necessary English/technical terms.

## Layout

- `SKILL.md` is the skill entry point; `references/` holds the behavioral rules and phrase tables; `evals/` holds test cases; `automation/` holds eval and automation scripts.
- `tasks/` is a gitignored workspace (`current/` in progress, `archive/` done, `external-inputs/` collected material). Planning and process docs go only there, never into commit history.

## Collaboration

- Commit under the repository owner's name, with no AI signature line (no `Co-Authored-By`). This is an established convention.
- Do documentation work directly; for feature work, the usual flow is to write a self-contained spec into `tasks/current/` and hand it to a cheaper model to execute.
- If the installed Claude Code skill is a symlink into this repo, editing `SKILL.md` here changes the live skill immediately; upgrades happen via `git pull` — never copy files into the skills directory.
