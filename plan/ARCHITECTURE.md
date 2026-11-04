# Architecture

## Runtime topology

Use a modular monolith: TypeScript Node/Express API, PostgreSQL, durable background worker, React office application, React platform-admin application, and Flutter Android warehouse client. Share domain contracts, permission codes and generated clients, not database access from frontends. Choose exact supported dependency versions and licenses in the foundation task; do not copy stale lockfiles.

Planned code layout: `api/src/modules/<domain>`, `api/src/db`, `apps/web`, `apps/admin`, `packages/contracts`, `packages/ui`, `mobile`, `infra`, `scripts`, `plan`. This planning delivery deliberately does not scaffold runtime applications.

PostgreSQL is authoritative for operations, quantities and valuations. Use pg-boss-style PostgreSQL-backed jobs plus a transactional outbox. SSE supplies online invalidation; clients always refetch authorized state. Private S3-compatible object storage holds attachments and exports with scoped download authorization. SMTP/email, telemetry and object-store providers are infrastructure configuration; no vendor account is assumed.

## Tenant and scope model

Use shared database/shared schema with mandatory tenant keys on scoped records and FORCE RLS. Normal app and worker roles are neither table owners nor BYPASSRLS. Migrations use a separate owner role. Scope is established by authenticated membership and applied with transaction-local database settings. Never accept a client tenant/company identifier as authorization.

A platform control-plane service accesses only tenant lifecycle, entitlements and approved support-session metadata. Domain access requires explicit customer-approved support scope. Tenant isolation also partitions object keys, cache keys, idempotency keys, job payloads, event channels and exports.

Company-local records carry tenant_id and company_id. Cross-company operations are explicit paired commands requiring both grants; no shared stock bucket or accidental cross-company foreign key is allowed. Catalog templates may be copied but remain independent.

## Module boundaries

Only the stock posting service updates physical projections. Purchasing, sales, returns, counts, ownership and Android invoke this service through typed commands. Only the valuation service creates valuation entries. Accounting export consumes valuation evidence, never raw UI totals. Approval, audit, notifications and privacy are shared primitives.

Module dependencies are in registry.json and form a DAG. Lot/serial and owner identity exist in phase 4 before movements. Every early receipt records original cost facts in phase 5; phase 11 replays these into final valuation. No financial production launch is allowed before replay and reconciliation succeed.

## Transactions and integration

A stock command uses a scoped transaction, canonical lock order, optimistic document version, persistent idempotency key, immutable move, balance projection, cost fact, audit and outbox. Domain side effects commit together. HTTP responses occur only after commit. Workers recheck scope and deduplicate before side effects.

External effects occur after commit via outbox. Retry with bounded backoff; dead-letter after eight attempts. Customer-owned integrations use signed webhook events and API scopes. External accounting receives versioned batches and returns acknowledgements. Never wrap a remote network call inside a stock database transaction.

## Reliability and migration

Use expand-contract migrations, versioned event/API payloads and feature flags. Support current and immediately preceding mobile schema during a rollout, with a published upgrade window. Unknown command versions fail visibly; old offline commands are not silently reinterpreted. Retain immutable history and replayable projections to support repair and audit.
