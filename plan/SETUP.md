# Setup and environment blueprint

## This planning package

Requires Python 3.10+ and Make only. Run `make plan-check`, `make plan-test`, and `make plan-render`. No database, Docker, npm packages, credentials or internet are needed to validate the plan. Do not expect `make up` to exist until the foundation tasks implement it.

## Future application setup

Foundation tasks verify/pin Node/TypeScript/Express/React/PostgreSQL/Flutter and supporting packages, create lockfiles and record licenses. Implement Make targets for up, down, migrate, seed-reference, seed-demo, test, test-integration and verify. Seed references separately from synthetic demonstration data. API docs use generated OpenAPI; user interfaces use generated clients.

Required configuration categories: app environment/base URLs, admin migration database URL, non-owner application database URL, separate worker role, auth/session/token keys, private object-storage endpoint/bucket/credentials, email destination/provider, telemetry endpoint, webhook signing/rotation keys and encryption/key-management references. Never commit actual values or return them in logs. Application and migration secrets must not be interchangeable.

Development uses isolated Docker PostgreSQL and local email/object-storage emulators where feasible; staging and production have separate accounts and data. Production infrastructure region and processors require localization review. Infrastructure-as-code, secret rotation, health endpoints and backup jobs are delivery tasks, not resources provisioned by this planning package.
