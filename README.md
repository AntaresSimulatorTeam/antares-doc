# Antares documentation website

Welcome to the Antares website for user documentation!

This documentation is written in `markdown` then built using the static site generator
[`MkDocs`](https://www.mkdocs.org/) and the 
[`Material for MkDocs theme`](https://squidfunk.github.io/mkdocs-material/).

## How to build and edit the documentation

Before making changes, please review the 
[guidelines](https://antares-doc.readthedocs.io/en/latest/contributing/guidelines-docs/)
to ensure consistency.

If you're unfamiliar with Git or pull requests, you can submit your modified file as an issue, 
and someone from the team can assist you.

Moreover, you can follow the guides:

- To [edit the documentation on GitHub](https://antares-doc.readthedocs.io/en/latest/contributing/online-editing/)
- To [edit the documentation locally](https://antares-doc.readthedocs.io/en/latest/contributing/local-editing/)

## Run checks

Pull requests check the merged result with a strict MkDocs build and local Markdown link checks.
The same checks run on pushes to `master`. Run them locally with
[uv](https://docs.astral.sh/uv/) and [Lychee 0.24.2](https://github.com/lycheeverse/lychee/releases/tag/lychee-v0.24.2):

```bash
uv sync --locked
uv run --locked mkdocs build --strict
lychee --config lychee.toml --offline README.md AGENTS.md 'docs/**/*.md'
```

Lychee checks file targets in Markdown; MkDocs validates page anchors with its own heading rules.
The shared request settings are in `lychee.toml`.

External Markdown links are checked every Monday at 06:00 UTC. To run that check on demand, select
**Actions → Check links → Run workflow** on GitHub, or run:

```bash
lychee --config lychee.toml --scheme http --scheme https README.md AGENTS.md 'docs/**/*.md'
```

External failures appear in the workflow logs and job summary and fail that run. This includes
`theses.fr`, HTTP errors, and timeouts after bounded retries. External dead links remain monitored,
while third-party outages do not fail unrelated documentation PR checks. Review failed scheduled
runs and fix broken URLs; do not hide a transient outage with a permanent domain exclusion.

## Useful links

- Antares website: [https://antares-doc.readthedocs.io/](https://antares-doc.readthedocs.io/)
- Source files: [https://github.com/AntaresSimulatorTeam/antares-doc](https://github.com/AntaresSimulatorTeam/antares-doc)
