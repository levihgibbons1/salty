# Milestone 1 — SALTY Foundation

## Outcome

A second contributor can run SALTY with fictional identities, import two semesters of coursework, browse preserved work, and submit a tested change using their preferred editor or coding agent. School administrator access is not a prerequisite.

## Work items

- [x] **M1-01: Development scaffold.** Inspect any available existing project code, select the stack in an architecture decision, and document install/start/test/reset commands. Provide a health check and reproducible dependencies.
- [ ] **M1-02: Identity and permissions.** Add fictional student, teacher, and staff accounts with permanent person IDs. Enforce contextual server-side access. Verify production startup rejects development sign-in.
- [ ] **M1-03: Records and fixtures.** Add database migrations and entirely fictional data for at least two students, two terms, course sections, assignments, submissions, feedback, and example files.
- [ ] **M1-04: Import pipeline.** Validate source data, map identities, preserve files and provenance, report errors, and prevent duplicates on retries.
- [ ] **M1-05: Academic archive.** Browse term → course → assignment → submission and feedback. Display source and last-import information, empty states, and import failures.
- [ ] **M1-06: Persistence and isolation.** Verify restart persistence, two-term retention, repeated imports, rejected malformed imports, unauthorized record/file access, and source-independent retrieval of archived files.
- [ ] **M1-07: Contributor handoff.** Have another person follow setup from a fresh clone, make a bounded change with their preferred tool, run checks, and open a pull request. Record gaps and fix the guide.

Suggested sequence: M1-01 → M1-02 and M1-03 → M1-04 → M1-05 → M1-06 → M1-07. Coordinate shared files before concurrent work.

## Demo script

1. Start from a documented clean local environment and seed fictional identities.
2. Sign in as sample student A and import semester one through the authorized import flow.
3. Import semester two; confirm both terms and their files are accessible.
4. Import the same source again; verify no duplicate records.
5. Restart the app and database; confirm preserved records and files remain.
6. Sign in as student B; verify student A’s private data and file URLs are denied.
7. Demonstrate a teacher’s allowed section and a denied unrelated section.
8. Confirm archived content remains available without the source adapter running.

## Outside this milestone

Live school account authorization, real student data, production launch, full LMS replacement, sending external messages, and live AI-provider integration. Define extension points now; implement those features in later milestones. No fake live-agent responses should be presented as working integrations.

## Definition of done

All work items pass their acceptance checks, application setup is reproducible, CI runs meaningful application checks, and the second-contributor handoff succeeds. Documentation scaffolding alone does not complete this milestone.
