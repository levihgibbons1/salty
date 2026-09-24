# Architecture decisions

## ADR-001: Tool-independent contributor foundation

Status: accepted for repository setup.

Contributors use Git, shared documentation, and reproducible checks. No specific coding agent is required. AGENTS.md is canonical; tool-specific entry files link to it. Runtime agent access is separate from code contribution access.

## ADR-002: Build against fictional development adapters first

Status: accepted for Milestone 1.

Institutional integrations are unavailable or unverified. Build real persistence, authorization, import behavior, and interfaces using fictional data. Live integrations must fit those boundaries. Development sign-in cannot be enabled in production.

## Pending decisions

M1-01 must select and justify the language/framework, relational database, file storage strategy, migrations, tests, and local startup process. Hosting and AI providers remain separate decisions. Review existing project code when supplied before choosing compatibility constraints.
