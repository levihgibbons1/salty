# SALTY handbook

Status: implementation guidance for a documentation-only repository. Requirements in these documents describe what must be built; they do not claim controls or features already exist.

## Reading routes

| Your task | Read in order |
| --- | --- |
| First contribution | [Project overview](../README.md), [shared instructions](../AGENTS.md), [contribution guide](../CONTRIBUTING.md), [current milestone](milestone-1.md) |
| Plan product behavior | [Product brief](product.md), [architecture](architecture.md), [decisions](decisions.md) |
| Implement persistence or imports | [Data contract](data-contract.md), [security](../SECURITY.md), [testing](testing.md) |
| Build an edge app or runtime agent | [App contract](app-contract.md), [data contract](data-contract.md), [security](../SECURITY.md) |
| Select the first stack | [M1-01 task brief](tasks/m1-01.md), [architecture](architecture.md), [decisions](decisions.md) |
| Prepare a school pilot | [Access tracker](access-tracker.md), [operations](operations.md), [security](../SECURITY.md) |
| Resume work with another tool | [Handoff template](templates/handoff.md), relevant issue, current code and test output |

## Sources of truth

- Product scope: product.md and milestone-1.md.
- Contributor behavior: ../AGENTS.md. Tool-specific entry files link to it.
- Architecture choices: accepted entries in decisions.md.
- Interface requirements: data-contract.md and app-contract.md; executable schemas will accompany implementation.
- Current behavior: code and reproducible checks. Documentation must be corrected when it overstates implementation.
- Work ownership and progress: GitHub issues and pull requests. Milestone checkboxes reflect verified completion.

When documents conflict, identify the conflict and fix its canonical source. Do not silently invent an institutional policy or report a proposal as an accepted decision.

## Maintaining this handbook

Update affected documents in the same pull request as a behavior change. Link to canonical definitions instead of copying them into multiple tool instruction files. Use explicit labels: proposed, accepted, implemented, or verified. Record consequential choices using the [decision template](templates/decision.md).
