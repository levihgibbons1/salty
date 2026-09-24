# Architecture decisions

## ADR-001: Tool-independent contributor foundation

Status: accepted for repository setup.

Contributors use Git, shared documentation, and reproducible checks. No specific coding agent is required. AGENTS.md is canonical; tool-specific entry files link to it. Runtime agent access is separate from code contribution access.

## ADR-002: Build against fictional development adapters first

Status: accepted for Milestone 1.

Institutional integrations are unavailable or unverified. Build real persistence, authorization, import behavior, and interfaces using fictional data. Live integrations must fit those boundaries. Development sign-in cannot be enabled in production.

## Pending decisions

ADR-003 selects the local scaffold stack. Production database and hosting decisions remain open. Hosting and AI providers remain separate decisions. Review existing project code when supplied before choosing compatibility constraints.

## ADR-003: Django and SQLite for the local scaffold

Status: implemented for M1-01; production architecture remains undecided.

Considered Django + SQLite, Flask + SQLite, and a TypeScript web stack + PostgreSQL. Django supplies migrations, request handling, and a test runner with fewer initial choices than Flask. SQLite removes the contributor dependency on Docker or an external database. A TypeScript/PostgreSQL stack is also viable but adds setup services before the first local flow needs them.

Select Python 3.12–3.14, Django 5.2, Django ORM/migrations, local SQLite, and local file storage under ignored `.local/`. Use Django’s test runner and Ruff formatting/linting. Pin dependencies in requirements.txt and test the supported runtime endpoints in CI. [Django’s compatibility documentation](https://docs.djangoproject.com/en/5.2/releases/5.2/) supports these Python versions.

Do not assume SQLite is the final school database. Before a multi-user pilot, evaluate PostgreSQL, migration behavior, concurrency, production storage, and deployment in a separate ADR. Use Django migrations for versioned schema changes; a custom SQL migration runner is unnecessary. File storage is local-only and not publicly served. No default auth user tables are installed yet, preserving the custom identity decision for M1-02.

Existing Formation Pathways, StudyHub, and PlayForge source has not been supplied locally or inspected. Compatibility with their implementation languages is unverified; shared APIs remain the planned boundary. This decision establishes a working base, not a promise of direct code reuse.
