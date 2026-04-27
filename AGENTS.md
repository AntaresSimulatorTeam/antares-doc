# AGENTS.md

This file gives LLMs and also contributors context about this project. 
Read it before making any changes.

## Project overview

This is a developer-facing documentation site built with [MkDocs](https://www.mkdocs.org/) and the
[Material theme](https://squidfunk.github.io/mkdocs-material/). Dependencies are managed with
[uv](https://docs.astral.sh/uv/).

---

## Setup

```bash
uv sync
```

## Commands

```bash
mkdocs serve       # Start local dev server at http://localhost:8000
mkdocs build       # Build static site into /site (gitignored)
```

---

## Project structure

```
.
├── docs/                  # All markdown source files
│   ├── index.md           # Home page
│   └── ...                # Sections mirror mkdocs.yml nav
├── mkdocs.yml             # Site config, nav, plugins, theme options
├── pyproject.toml         # Project dependencies (managed by uv)
└── uv.lock                # Lockfile — commit this
```

- **Never add a page without updating the `nav` in `mkdocs.yml`.**
- Pages not listed in `nav` will not appear in the sidebar.

---

## File formatting rules

### General

- **Encoding:** UTF-8, Unix line endings (`\n`), trailing newline at end of file.
- **Line length:** Soft limit of 100 characters for prose. Hard-wrap code blocks and tables only
  when necessary for readability. Math can be longer.
- **Indentation:** 4 spaces for nested lists and admonition content. Do not use tabs.

### Headings

- Every page has exactly **one H1** (`#`), which becomes the page title.
- Use `##` and `###` for sections and subsections. Avoid going deeper than `####`.
- Headings use **sentence case**, not Title Case (e.g. `## Getting started`, not `## Getting Started`).
- Do not skip heading levels.

### Code blocks

Always specify the language for syntax highlighting:

````markdown
```python
def hello():
    print("hello")
```
````

For shell commands, use `bash`. For output-only blocks (no prompt), use `text` or `console`.

### Links

- Use **relative links** between docs pages: `[see this page](../other/page.md)`.
- Use absolute URLs only for external sites.
- Do not use bare URLs in prose — always use `[label](url)` syntax.

### Images

- Store images in `docs/assets/` or a local `images/` subfolder near the page.
- Always include alt text: `![Alt description](path/to/image.png)`.
- Prefer SVG for diagrams, PNG for screenshots.

### Math

- Use MathJax to render equations (inline: $ $, centered: $$ $$).
- Math is also an exception for the line width of 100 characters.

---

## Material theme features in use

### Admonitions

Use admonitions to call out important content. Standard types:

```markdown
!!! note
    Use for supplementary information that is helpful but not critical.

!!! warning
    Use for things that could cause errors or data loss.

!!! tip
    Use for shortcuts or best practices.

??? example
    Use collapsible blocks (`???`) for longer examples or optional detail.
```

Do not invent custom admonition types that are not configured in `mkdocs.yml`.

### Content tabs

Use for showing alternatives (e.g. OS-specific instructions, language variants):

```markdown
=== "Linux / macOS"
    ```bash
    export MY_VAR=value
    ```

=== "Windows"
    ```powershell
    $env:MY_VAR = "value"
    ```
```

Keep tab labels short and consistent across pages.

### Code annotations

Use annotations to explain code inline without cluttering the block:

```markdown
```python
import os  # (1)!
```

1. This imports the standard `os` module.
```

Only use annotations when the explanation cannot fit naturally in surrounding prose.

---

## Writing style

- **Voice:** Second person ("you"), active voice. Write procedures in the imperative ("Run the
  command", not "The command should be run").
- **Tense:** Present tense. Avoid "will" unless describing future behaviour explicitly.
- **Contractions:** Acceptable (e.g. "don't", "it's") — this is developer docs, not legal writing.
- **Introductions:** Every page should open with 1–2 sentences explaining what the page covers and
  why it matters. Skip generic filler like "In this document, we will...".
- **Procedures:** Use numbered lists for sequential steps. Use bullet lists for unordered options.
- **Emphasis:** Use **bold** for UI labels, key terms on first use, and critical warnings. Use
  `code` for all commands, file paths, env vars, function names, and literal values.
- **Avoid:** Jargon without definition, acronym without explanation, passive voice, vague pronouns 
  ("it", "this" with no referent), and filler phrases ("simply", "just", "easy", "obviously").

---

## What NOT to do

- Do not use raw HTML unless there is no markdown equivalent and it is absolutely necessary.
- Do not hardcode the site URL in links — use relative paths.
- Do not commit the `/site` build directory.
- Do not change `mkdocs.yml` plugins or theme settings without understanding the impact on the
  build.
- Do not add pages to `docs/` without a corresponding `nav` entry.