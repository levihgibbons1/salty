# Edge-app and agent contract

Status: proposed contract. No registration service, SDK, or API exists yet. M1-01 selects the implementation stack; later changes provide executable API schemas.

## Shared integration boundary

Apps use SALTY identity and authorized application APIs. They do not issue their own school person IDs, infer authority from email domains, or receive general database credentials. Apps may own specialized domain records linked to shared people and sections.

An app registration must eventually declare an ID, name, owner, route, purpose, requested capabilities, and the records it creates or consumes. Installation and permission grants are separate operations. A registered app has no implicit right to every student record.

## Initial capability vocabulary

Proposed capabilities: `academic.read_self`, `academic.read_assigned_sections`, and `imports.run_fixture`. These are design names, not implemented permissions. Each grant also needs contextual scope. A teacher role alone is insufficient for unrelated sections; an import fixture capability is development-only.

## Request behavior

- Derive the actor from a verified session; never accept an arbitrary client-supplied actor as authority.
- Validate identifiers and input schemas. Authorize target records and nested/file resources.
- Define pagination, stable ordering, error semantics, and idempotency for retryable writes when endpoints are implemented.
- Return provenance and freshness where users need to assess evidence.
- Distinguish not found, forbidden, and failed operations according to a documented information-disclosure policy.
- Keep failures actionable without exposing private payloads or credentials.

## UI expectations

Support keyboard navigation, labeled controls, visible focus, and readable states. Include loading, empty, stale/partial import, denied, and failed states. A hidden button is not an access control. Do not describe sample data as live school information.

## Future runtime tools

Tools such as “list my assignments” and “retrieve authorized feedback” wrap the same application operations. A model does not choose the caller’s identity. Results preserve record references so answers can cite their evidence. Tool inputs and outputs have schemas; untrusted retrieved text cannot change the schemas or permission checks.

## Compatibility

Document breaking API or event changes and update consumers together, or provide a transition period. Keep a single canonical schema when code exists instead of separately maintained language-specific definitions. Events, if introduced, carry minimal references and are not a bypass around record authorization.
