# Operations and release readiness

Status: future operational requirements. No production deployment, backup service, or monitoring is configured.

## Environments

| Environment | Data | Purpose |
| --- | --- | --- |
| Local / test | Fictional fixtures | Development and automated checks |
| Preview / staging | Fictional fixtures initially | Review and integration verification |
| Production | School-approved records only after readiness review | School operations |

Separate secrets and storage by environment. Development authentication must fail closed outside local/test operation. Preview URLs must not expose real records. Do not copy production data into developer machines to reproduce a bug.

## Release process

Reviewed pull request → documented checks → preview verification → authorized release. Include migrations and compatibility effects. Record the deployed revision and a rollback or forward-recovery plan. Data migrations can make code-only rollback unsafe; rehearse recovery for consequential changes.

## Backup and restore

Back up database records and file assets consistently, protect backup access, and test restoration into an isolated environment. Verify relationships and file checksums after restoration. School owners must choose recovery time and data-loss objectives before production; no objectives are asserted here.

## Monitoring

Track health, import completion/failure, unresolved identities, missing files, authorization failures, and job backlog without logging private content. Alerts need an actual responsible owner and response path. A dashboard without ownership is not operational coverage.

## Vendor retirement

For each function, document authoritative source, retained history, reconciliation results, user workflow coverage, cutover date, and recovery procedure. Obtain the relevant school owner’s authorization before switching official writes or ending service. Verify exports and accessible files independently before losing source access.
