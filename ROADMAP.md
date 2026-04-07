# AI-Server-Ready roadmap

## Phase 0 — Stabilize the base
- Keep the repository simple and runnable locally.
- Use local files first; avoid fragile remote dependencies.
- Build repeatable reporting and repo-audit steps.

## Phase 1 — Ingestion
- Add loaders for local folders and selected repositories.
- Extract README, requirements, and top-level structure.
- Produce one summary report per source.

## Phase 2 — Orchestration
- Add task definitions for audit, indexing, and reporting.
- Keep execution explicit and reversible.
- Log every run in `state/`.

## Phase 3 — Delivery
- Export reports in Markdown.
- Optionally add a small web dashboard only after the CLI is stable.

## Success criteria
- A new source can be ingested with one command.
- Reports are reproducible.
- The stack remains lightweight and maintainable.
