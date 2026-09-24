# SALTY

Pacifica Christian’s unified school operating system—shared student records, modular apps, and permission-aware AI agents.

## Vision

SALTY will become the school’s operating system and authoritative record platform. Existing systems are temporary integration and migration sources. Functions move into SALTY gradually, with verified records and explicit ownership changes before a platform is retired.

Google is the intended school sign-in provider. Permanent SALTY person IDs remain independent of Google accounts. Edge apps share identities, permissions, and records through documented interfaces.

## Current status

This repository contains the project foundation and contributor documentation. **There is no runnable application, database, authentication service, or live integration yet.** No school administrator access is needed to contribute to this stage.

## Documentation

Use the [SALTY handbook](docs/README.md) for role-specific reading routes, contracts, testing, and operations. [Security requirements](SECURITY.md) apply to every future app and integration.

## Start here

1. Clone `https://github.com/levihgibbons1/salty.git` and open the repository in your editor or coding tool.
2. Read [agent instructions](AGENTS.md), [architecture](docs/architecture.md), and [Milestone 1](docs/milestone-1.md).
3. Follow [CONTRIBUTING.md](CONTRIBUTING.md) to choose a task and submit a pull request.
4. With Python 3.10 or newer installed, run `python3 scripts/check_docs.py` to validate local Markdown links and required foundation files. It uses only the standard library.

Claude Code, Gemini, Codex, Grok Build, Muse, and other tools can contribute through the same files and Git workflow. Tool support varies; explicitly point your tool to `AGENTS.md` if it does not discover project instructions automatically.

## First milestone: SALTY Foundation

Build a development-only sign-in and persistent academic archive using entirely fictional identities and two semesters of sample coursework. Demonstrate repeatable imports, retained files, permission boundaries, and setup by a second contributor. Live Google and Canvas connections follow when access is available.

- [Milestone and acceptance criteria](docs/milestone-1.md)
- [Architecture and data ownership](docs/architecture.md)
- [Access dependencies](docs/access-tracker.md)
- [Architecture decisions](docs/decisions.md)

## Project stewardship

Institutional sponsorship, production infrastructure ownership, and data access must be established with Pacifica before a real-data pilot. This repository is currently hosted under `levihgibbons1`; school ownership is a future coordination item, not an existing approval.
