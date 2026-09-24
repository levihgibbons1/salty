# Verification strategy

## Available now

Run `python3 scripts/check_docs.py` and `git diff --check`. The documentation checker verifies required files and simple relative Markdown file links. It does not validate anchors, external URLs, Markdown semantics, security, or application behavior.

## Required as implementation arrives

| Boundary | Meaningful checks |
| --- | --- |
| Identity | Stable person mapping; development provider rejected in production configuration |
| Authorization | Own student records allowed; other student records denied; teacher section scope; direct file access denied outside scope |
| Imports | Duplicate/reordered input, source ID collisions across providers, changed records, partial pages, malformed data, interruption and retry |
| Persistence | Real test database migrations, restart persistence, preserved file bytes and checksums |
| Archive UI | Two-term navigation, feedback/source visibility, keyboard access, partial and failed import states |
| Setup | Fresh-clone instructions succeed without private credentials or a paid coding tool |

Use unit tests for validation and transformations, integration tests for real storage/authorization boundaries, and a small end-to-end suite for the critical archive flow. A mocked database test cannot establish durability. Tests should assert behavior rather than copy implementation logic.

## Evidence in a pull request

List exact commands and their outcomes, explain skipped checks, and identify fixture scenarios. Do not mark milestone items complete solely because CI is green. CI’s scope must be explicit. Screenshots use fictional data and supplement, not replace, behavior checks.

## CI growth

The current workflow checks documentation only. The scaffold task must add application checks appropriate to the selected stack. Before a shared pilot, configure maintainer review and required checks in repository settings; a YAML file does not enable branch protection.
