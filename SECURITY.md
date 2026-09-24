# Security and data boundaries

Status: engineering requirements, not a certification or claim of implemented controls. SALTY currently contains no application or real school data. Institutional policies and applicable obligations must be confirmed by the school before a real-data pilot.

## Reporting

Do not post credentials, private records, or exploit payloads containing student data in public issues. Contact a repository maintainer through an established private channel. A dedicated reporting address and response owner are not yet configured; establishing them is a pre-pilot requirement. If a credential is exposed, revoke or rotate it through its owner; removing a file alone does not invalidate the credential.

## Required boundaries

| Risk | Required design | Verification |
| --- | --- | --- |
| Student reads another student’s work | Server-derived caller identity and record-level authorization | Direct API and file requests for unrelated records are denied |
| Teacher or staff role grants universal access | Explicit capabilities and approved relationships | Unrelated sections denied; staff has no automatic global read permission |
| Development login reaches production | Fail closed outside explicitly configured development/test environments | Production startup/configuration test rejects the development provider |
| Imported text instructs an agent | Treat source text as untrusted evidence | Tool permissions remain unchanged by retrieved instructions |
| Integration token grants excessive access | Keep provider credentials server-side; enforce SALTY policy on results | User cannot select a more privileged credential or actor |
| Private files or search results leak | Apply access checks before returning content, URLs, snippets, or cached results | Negative tests cover direct URLs and caches, not only UI routes |
| A retry corrupts records | Idempotent writes, explicit import state, recoverable failures | Repeated and interrupted imports do not duplicate or misreport completion |
| Credentials or records enter Git/logs | Fictional fixtures, ignored local secret files, minimal structured logs | Review changed files and verify sensitive fields are redacted |

## Runtime agents

An agent acts for an authenticated principal and declared capability set. The server decides the effective scope. Never grant an agent broad access because its prompt says it is a teacher or administrator. Retrieved content cannot authorize tool execution. Future write tools require explicit action semantics and audit records; sensitive actions must have a school-approved authorization workflow.

## Record lifecycle

Retain provenance and correction history where approved. Define deletion, retention, access revocation, and account offboarding before real data is imported. Historical access is a separate policy decision from present enrollment. Old access tokens or cached entitlements must not silently preserve revoked permissions.

## Before a real-data pilot

Named owners must verify access policy, data minimization, provider handling, secret storage, backups and restore, reporting contacts, and monitoring. Record approvals and open questions in the access tracker without storing sensitive details. A merged pull request does not constitute institutional approval.
