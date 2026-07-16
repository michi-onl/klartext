# ChatGPT / generic LLM install

## lite / full

- `lite`: load only `SKILL.md`. Good for pasting into a chat, an API system prompt, tight context, or occasional rewrites.
- `full`: load `SKILL.md` + `references/`. Good for a Custom GPT, a Project, public text, technical docs, and cases that need false-positive protection.

For ChatGPT / generic LLMs, start from lite; upgrade to full for long-term use, README / release note / issue replies, or when you worry about terms and facts getting false-positived.

## ChatGPT

### Approach 1: Custom GPT (recommended)

`SKILL.md` is long — well over the 1,500-character limit of Custom Instructions. A Custom GPT gets around that and loads the full rules without trimming.

To build one:

1. Open the [ChatGPT GPT Editor](https://chatgpt.com/gpts/editor) and create a new GPT
2. Name it "klartext", description "German-English de-AI rewrite assistant"
3. Paste the content below the divider in [`install/chatgpt-gpt-instructions.md`](chatgpt-gpt-instructions.md) into Instructions
4. Upload Knowledge Files: `SKILL.md` + every `.md` file under `references/` (full usage)
5. Save and publish as "Only me" or "Anyone with a link"

Then just open that GPT and chat.

### Approach 2: Projects

If you have ChatGPT Plus / Pro, you can also use Projects:

1. Create a Project
2. Upload `SKILL.md` and the `references/` files you need to Project Files; full is recommended for long-term use, lite (only `SKILL.md`) for temporary projects
3. In Project Instructions write: `Rewrite the user's text by the rules in the project file SKILL.md.`

Project files have no strict character limit; the effect is similar to a Custom GPT.

### Approach 3: paste into the chat (lightweight)

Don't want to build a GPT or Project? Paste the `SKILL.md` content at the start of the conversation. Good for one-off use. This is the lite usage.

> **Note:** Custom Instructions (Settings > Personalization) have a 1,500-character cap and can't hold the full `SKILL.md`. Not recommended.

## Claude (Web / Project)

1. Create a Project
2. Add the `SKILL.md` content to Project Instructions
3. For steadier false-positive protection, add the relevant `references/` files to Project Knowledge

## API / System Prompt

```python
messages = [
    {"role": "system", "content": open("SKILL.md").read()},
    {"role": "user", "content": "Rewrite the following text: ..."}
]
```

If you already have a main system prompt, splice `SKILL.md` in as a style module — don't overwrite the whole thing.

## Usage tips

To first judge "where it sounds AI" without rewriting, say in the chat:

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

## When to add `references/`

- Heavy AI flavor where a plain word-table rewrite isn't enough
- German-English mixing that needs fine scene detection
- Technical copy where you worry about false-positiving terms
- Structural problems, not just word deletion

Add first: `structures.md` / `severity.md` / `operation-manual.md` / `boundary-cases.md`
