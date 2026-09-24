# Product brief

## Destination

SALTY is Pacifica Christian’s intended school operating system and authoritative data platform. A person’s record can continue from inquiry through enrollment, school life, graduation, and approved alumni participation. Edge apps use shared identities and records. Authorized runtime agents retrieve relevant evidence through the same permission boundaries.

Existing vendors remain authoritative for their assigned functions until a validated cutover. Integration is a migration mechanism, not the final product goal. Google remains the intended sign-in provider under the current plan; replacing every external infrastructure dependency is not a Milestone 1 requirement.

## First users and jobs

| User | Initial job | Evidence of success |
| --- | --- | --- |
| Student | Revisit prior coursework and feedback | Preserved content loads across two terms without contacting the source |
| Teacher | Review work for authorized sections | Relevant student work is accessible; unrelated work is denied |
| Contributor | Make a change with a preferred coding tool | Fresh setup, checks, and a reviewed pull request succeed |
| Future school data owner | Reconcile an import | Counts, failures, provenance, and missing items are inspectable |

## Product principles

1. Preserve useful records with provenance and governed retention.
2. One person identity across apps; provider accounts are links to that identity.
3. Give users clear sources, dates, and failure states instead of silent guesses.
4. Restrict access by relationship and purpose, not merely by possessing a login.
5. Label AI interpretations separately from official facts and human observations.
6. Make integrations replaceable without rebuilding the archive or apps.
7. Keep contributor workflows usable without a particular editor or model vendor.

## Milestone 1 boundary

A local development product with fictional identities and coursework, persistent records and files, repeatable imports, and an academic archive. See [the acceptance criteria](milestone-1.md).

No real-data pilot, live institution-wide access, official grading writes, production rollout, or vendor retirement is included. Live AI is a later feature; archive correctness must not depend on model behavior.

## Questions that remain open

- Who are the school sponsor, technical owner, and departmental data owners?
- Which existing repositories should share code or contracts with SALTY?
- Which information is approved for retention, and for how long?
- What historical access should teachers retain after a section ends?
- Which function should transfer into SALTY after the archive pilot?

These are planning inputs. Fictional development can proceed while institutional questions are resolved.
