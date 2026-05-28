# Contributing to the documentation

Thank you for helping improve this documentation. This guide covers everything you need to know
before opening a pull request — from setting up your environment to the conventions we follow.

This documentation is written in [`markdown`](https://www.markdownguide.org/cheat-sheet/) 
then built using the static site generator [`MkDocs`](https://www.mkdocs.org/) and the 
[`Material for MkDocs theme`](https://squidfunk.github.io/mkdocs-material/).

MkDocs uses a single configuration file `mkdocs.yaml` at the root of the project.
It defines the page navigation, which plugin is used... All the actual 
documentation pages are actually in the `docs/` folder with the markdown `.md`
extension.

## Before you start

- **For small fixes** (typos, broken links, outdated commands): open a PR directly.
- **For new pages or significant restructuring**: open an issue first to align on scope and placement
  in the nav before writing.
- **For questions**: use the project's discussion forum rather than issues.

## Workflow

1. Fork the repository and create a branch from `main`.
2. Make your changes and preview them locally with `mkdocs serve`.
3. Verify the site builds cleanly with `mkdocs build` (fix any warnings).
4. Open a pull request with a clear title and a short description of what changed and why.

!!! warning "Don't commit the `/site` directory"
    The build output is gitignored. Never force-add it to your commit.

## File and formatting conventions

Following these conventions keeps the source consistent and makes reviews faster.

### Files

- **Encoding:** UTF-8, Unix line endings (`\n`), trailing newline at end of file.
- **New pages:** always add a corresponding entry to the `nav` in `mkdocs.yml`. Pages missing from
  `nav` won't appear in the sidebar.
- **Images:** store them in `docs/assets/` or a local `images/` subfolder next to the page. Use
  SVG for diagrams, PNG for screenshots.

### Headings

- One H1 per page (`#`) — this becomes the page title in the sidebar.
- Use `##` and `###` for sections and subsections. Don't go deeper than `####`.
- Use **sentence case**: `## Getting started`, not `## Getting Started`.
- Don't skip heading levels.
- Name eloquently pages and headings so that the feature you're documenting 
  would be the first result in the search bar. 

### Line length

Soft limit of **100 characters** for prose. Exceptions: code blocks, links, tables, and math
equations can be longer when wrapping would hurt readability.

### Code blocks

Always specify the language:

````markdown
```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```
````

Use `bash` for shell commands. Use `text` or `console` for output-only blocks.

### Links

- Between pages, use **relative links**: `[see this page](../other/page.md)`.
- For external sites, use absolute URLs.
- Never use bare URLs in prose — always write `[label](url)`.

### Math

Use MathJax syntax for equations:

- Inline: `$E = mc^2$` gives $E = mc^2$
- Centered: `$$ \int_0^\infty f(x)\,dx $$` (on a distinct line separated by blank lines) gives
    
    $$ \int_0^\infty f(x)\,dx $$

Math is exempt from the 100-character line limit.

## Material theme features

The site uses the following Material features. 
Check their [website](https://squidfunk.github.io/mkdocs-material/) for reference and tips.

### Admonitions

Use admonitions to surface important content without interrupting the main flow:

```markdown
!!! note
    Supplementary information that is helpful but not critical.

!!! warning
    Something that could cause errors or data loss.

!!! tip
    A shortcut or best practice worth highlighting.

??? example
    Collapsible blocks for longer examples or optional detail.
```

!!! warning
    Don't invent custom admonition types that aren't configured in `mkdocs.yml`.

### Content tabs

Use tabs to show alternatives — OS-specific commands, language variants, and so on:

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

Keep tab labels short and consistent across pages. If you introduce a tab set on one page, use the
same labels elsewhere for the same alternatives.

### Code annotations

Use annotations to explain code inline, without cluttering the block itself:

````markdown
```python
import os  # (1)!
```

1. Imports the standard `os` module for interacting with the operating system.
````

Only use annotations when the explanation doesn't fit naturally in the surrounding prose.


## Writing style

Our documentation is developer-facing and technical. Write with precision, not formality.

| Principle | Do | Don't |
|---|---|---|
| **Voice** | "Run the command" | "The command should be run" |
| **Tense** | Present tense | "This will create…" |
| **Person** | "you" | "the user", "one" |
| **Openings** | Start with what the page covers and why | "In this document, we will…" |
| **Emphasis** | **Bold** for key terms, `code` for literals | Italics for emphasis, quotes for code |

**Also avoid:**

- Filler words: "simply", "just", "easy", "obviously"
- Undefined acronyms — spell them out on first use
- Vague pronouns — "it" and "this" should always have a clear referent
- Passive voice — restructure to name the actor

**Lists:**

- Use **numbered lists** for sequential steps.
- Use **bullet lists** for unordered options or properties.


## What NOT to do

- Do not use raw HTML unless there is no markdown equivalent.
- Do not hardcode the site URL in links.
- Do not commit the `/site` build directory.
- Do not modify `mkdocs.yml` plugin or theme settings without understanding the build impact —
  coordinate in an issue first.
- Do not add a page to `docs/` without a `nav` entry in `mkdocs.yml`.
- Do not go deeper than `####` for headings — restructure the content instead.

## Diagrams

Diagrams are made using [`drawio`](https://www.drawio.com/) an open source 
diagramming tool. For vscode users, there is a an 
[extension](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio)
for editing diagrams inside your editor. Otherwise, you can download the 
drawio app. 
