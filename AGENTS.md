# Agent Guidance

This repository contains the Python API client published on PyPI. See the README for usage and `docs/development.md` for generation and packaging.

## Language

English is the default language for work in this public repository. Write documentation, code comments, issue text, pull request titles and descriptions, and commit messages in English unless a user explicitly requests another language or the content is intended to be localized for end users.

- `rium_api_client/api/` and `rium_api_client/models/` are generated. Do not edit them directly; check the source schema and generation instructions first. Do not guess at generation inputs if the schema is unavailable.
- Check Git status before and after work, preserve existing changes, and avoid changing files outside this repository or the parent's recorded submodule commit.
- Publishing to PyPI changes an external package. Do so only when explicitly requested; never store credentials in files or logs.
- No test suite is configured. Do not claim test coverage; report only checks that exist and were run.
- When AI generates or materially authors a commit, add an `Assisted-by` Git trailer naming the agent, for example `Assisted-by: Codex`. Apply this rule when this client is developed independently as well as when invoked through the parent repository.
- Create pull requests as drafts by default. Keep them in draft until a human explicitly approves making them ready for review; do not mark a draft ready on the agent's own initiative. Apply exactly one label: `ai-assisted` when a human led the work and AI assisted, or `ai-generated` when an AI agent led implementation. Fill in AI usage, agent, model, and work mode in the PR template.

With Python dependencies and Ruff available, run from the repository root:

```sh
ruff check .
poetry build
```

`poetry build` creates local artifacts; publishing is a separate action.
