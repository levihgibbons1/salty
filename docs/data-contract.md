# Academic data contract

Status: proposed implementation contract for Milestone 1. These names are domain concepts, not existing database tables or live endpoints. M1-03 must supply executable schemas and migrations and reconcile any changes here.

## Identity and relationships

| Entity | Required relationship and invariant |
| --- | --- |
| Person | Stable internal ID; independent of email and current school status |
| ExternalIdentity | Provider instance + external subject uniquely identify a verified link to a person |
| AcademicTerm | Stable term identity with explicit dates and source references |
| Course / Section | Course describes a subject; section identifies a specific offering and term |
| Enrollment | Links person to section with contextual role and effective dates |
| Assignment | Belongs to a section; preserves instructions, source identity, and due-date semantics |
| Submission | Belongs to assignment and student; distinguishes attempts and source revisions |
| Feedback | Links to submission or appropriate enrollment record; preserves author/source and visibility |
| FileAsset | Metadata, checksum, storage reference, and authorized parent relationship |
| ImportRun | Scope, actor/service, counts, timestamps, failures, and completeness status |
| AuditEvent | Actor, operation, target reference, outcome, and timestamp; no unnecessary record content |

Do not match people solely by display name. Ambiguous external identities are unresolved import items, not guesses. Provider instance distinguishes separate Canvas installations; entity type distinguishes overlapping provider IDs.

## Provenance and time

Imported records preserve source provider/instance, external identifier, source update time when supplied, import time, and import-run reference. Source timestamps may be absent; do not substitute an import timestamp while labeling it as a source timestamp.

Use timezone-aware instants for events and deadlines, and preserve the applicable source timezone. Represent date-only values as dates. Keep original source identifiers as strings. Preserve null/unknown separately from zero, empty, or false: an ungraded submission is not a zero grade.

## Import lifecycle

1. Establish authorized scope and create a run record.
2. Read pages/batches from the adapter; validate each payload.
3. Resolve source identities and relationships.
4. Upsert using stable source keys; retain meaningful changes under the chosen revision policy.
5. Copy authorized files, verify checksums, and associate their access boundary.
6. Reconcile expected and observed items where the source provides an inventory.
7. Finish as complete, partial, or failed with actionable error references.

A successful request is not proof of complete history. Missing pages, inaccessible files, unsupported record types, and unresolved identities must be visible. A source omission or failed request is not proof of deletion.

Retry transient failures with bounded attempts and provider-aware backoff when live adapters arrive. Invalid data needs correction, not infinite retries. Recoverable checkpoints must not skip unfinished records.

## Files and revisions

A file is archived only when its bytes are preserved and verified. File storage references are internal; clients obtain content through authorized access. Define allowed types, size limits, and safe download behavior during implementation. Never execute imported content.

Repeat imports with identical source content must not create duplicate records or revisions. Changed content must follow an explicit revision policy. An approved deletion process must address stored files, derived indexes, and caches as well as rows.

## Fictional fixture requirements

Include two students with distinct access, a teacher with one allowed and one unrelated section, two terms, graded and ungraded submissions, multiple attempts, changed feedback, preserved files, duplicate inputs, malformed records, and an inaccessible-file scenario. Label all fixture people and content as fictional. Do not lightly anonymize real student records and call them fictional.
