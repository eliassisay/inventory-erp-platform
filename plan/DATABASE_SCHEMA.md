# Conceptual database schema and constraints

[ENTITIES.md](ENTITIES.md) is the complete table/field ownership register. The migration task in each row owns its SQL schema, indexes and regression tests. This document defines mandatory cross-cutting semantics; runtime migrations do not exist yet.

## Common fields and types

- Domain entities use UUID primary keys; scoped entities include tenant_id and company_id where company-local, created_at, updated_at, created_by and optimistic version. Actor identifiers reference the identity provider's textual subject, not an assumed UUID.
- Instants are timestamptz in UTC; business dates are DATE interpreted in company time zone. Quantity and unit conversion facts are immutable snapshots on posted lines.
- Quantity NUMERIC(24,6), unit cost/FX NUMERIC(30,12); finite values only. Validate precision before SQL so database rounding cannot hide invalid input. API decimals are strings. Currency amount is BIGINT minor units with explicit currency code and exponent snapshot.
- Audit/outbox/movement/valuation rows are append-only; mutable projections and drafts carry versions. JSON payloads require versioned schemas; never use unrestricted JSON for quantities or permission rules.
- Contact/email/address/body fields are classified personal data. Blob columns contain private object keys and hashes, never public download URLs.

## Scope and keys

Composite unique keys `(tenant_id,id)` and `(tenant_id,company_id,id)` support scoped foreign keys. Company-local child references include both scope columns. Global unit/currency definitions are read-only reference data; tenant custom units remain scoped. Users belong to the identity control plane and gain tenant access only through memberships. Tenant memberships and support metadata are not a bypass into business tables.

Codes are trimmed and case-normalized for uniqueness per owner scope. Product variant attribute sets are canonicalized before uniqueness checks. Warehouse/location trees reject cycles; archive is blocked when current stock, reservations or open operations still reference a location.

Default FK deletion is RESTRICT for business history. Actor deletion/anonymization never cascades into posted evidence. Any SET NULL actor reference retains an audit-safe pseudonymous identifier according to the approved privacy policy.

## Stock relationships

Bucket key: tenant + company + location + product variant + owner + lot/serial + condition. Nullable dimensions must compare as equal for uniqueness. Projected on_hand and reserved quantities are exact; eligible reserved <= on_hand. Quarantine/expired/recalled conditions are excluded from eligible supply.

Each move has source and destination location, positive base quantity, unit snapshot, tracking/owner dimensions, business source line, occurrence time, posting time, posted sequence, command ID and optional reversal link. Signed projection effects derive from direction; clients never submit a balance_after value as authority. For a physical bucket, balance is incoming minus outgoing posted moves.

External supplier/customer/loss virtual locations balance movement history but do not create owned warehouse stock. In-transit custody is a real controlled location for quantity tracking. Cross-company moves are separate linked company postings, not one bucket with two company owners.

Reservations reference exact eligible buckets and demand lines. Allocation/consumption/release records sum to reservation quantity. A serial has at most one physical position and at most one active reservation; all serial operations use whole units.

## Valuation relationships

Cost facts link receipt/issue move to source unit cost, currency, FX, ownership and conversion snapshot. FIFO layers track remaining quantities; moving-average state and standard-cost versions are explicit. Valuation entries link original move/layer, reason and open period, with signed minor-unit amounts. Revaluation/landed-cost entries append corrections; original entry amounts never change.

Accounting batch lines reference valuation entries and external account mapping versions. Uniqueness prevents exporting the same entry twice within an active batch revision. Acknowledgements use batch ID + checksum + external reference; rejected/superseded lines remain explainable.

## Index and migration requirements

Index all scoped FKs and common `(tenant_id,company_id,warehouse_id,status,created_at,id)` access paths. Ledger indexes include scope/product/time/id and source-document references. Idempotency uniqueness includes tenant/company/action/key. Scoped contact/barcode searches require normalized indexed keys. Validate query plans using the launch-volume fixture; partitioning is a measured optimization, not a substitute for authorization.

Every DATA task tests fresh migration, down/up on an isolated database, scope mismatch, uniqueness, deletion policy and precision boundaries. Production destructive rollback is not assumed safe; use expand-contract migration and documented forward repair when posted data exists.
