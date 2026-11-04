# Acceptance scenarios

> Registry baseline 1.0 · 2026-11-04 · 51 modules · 790 tasks · 156 capabilities · 13 phases. Generated; edit registry.json and run `make plan-render`.

These are required application tests, not tests claimed to have run. The planning checker validates ownership and coverage; software implementation must produce the actual evidence.

## T-F001 — Research baseline

Feature F001 · module M01 · QA task INV-007.

- Given: Authorized Product owner and valid Product baseline and localization prerequisites.
- When: Research baseline.
- Then: Each agreed feature has an official source or an explicit product decision and a disposition.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F002 — Ethiopia localization review

Feature F002 · module M01 · QA task INV-007.

- Given: Authorized Product owner and valid Product baseline and localization prerequisites.
- When: Ethiopia localization review.
- Then: Record reviewed legal sources, applicability, reviewer, date and approval for data hosting, retention and document wording before pilot; tax invoices are excluded.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F003 — Dependency and version decisions

Feature F003 · module M01 · QA task INV-007.

- Given: Authorized Product owner and valid Product baseline and localization prerequisites.
- When: Dependency and version decisions.
- Then: Verify supported versions and licenses of Node, Express, React, PostgreSQL, Flutter and chosen libraries before lockfile creation; record exact versions in an ADR.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F004 — Reproducible development stack

Feature F004 · module M02 · QA task INV-014.

- Given: Authorized Engineer and valid Repository and delivery tooling prerequisites.
- When: Reproducible development stack.
- Then: A clean checkout boots API, worker, web, admin and PostgreSQL through documented Make targets without production credentials.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F005 — CI and contract generation

Feature F005 · module M02 · QA task INV-014.

- Given: Authorized Engineer and valid Repository and delivery tooling prerequisites.
- When: CI and contract generation.
- Then: Typechecks, lint, unit tests, API drift checks, integration tests and plan validation are separate visible CI jobs.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F006 — Environment separation

Feature F006 · module M02 · QA task INV-014.

- Given: Authorized Engineer and valid Repository and delivery tooling prerequisites.
- When: Environment separation.
- Then: Development, staging and production use separate credentials, databases, storage and notification destinations.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F007 — Tenant onboarding

Feature F007 · module M03 · QA task INV-030.

- Given: Authorized Platform operator and valid Tenants and SaaS entitlements prerequisites.
- When: Tenant onboarding.
- Then: A new customer gets isolated settings and an initial administrator; duplicate slug retry returns the original tenant.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F008 — Operator-managed plans

Feature F008 · module M03 · QA task INV-030.

- Given: Authorized Platform operator and valid Tenants and SaaS entitlements prerequisites.
- When: Operator-managed plans.
- Then: Versioned feature and storage limits are enforced in API and worker paths; no card processing is implemented.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F009 — Suspension and reactivation

Feature F009 · module M03 · QA task INV-030.

- Given: Authorized Platform operator and valid Tenants and SaaS entitlements prerequisites.
- When: Suspension and reactivation.
- Then: Suspended customers cannot post new stock but retain authorized export access; reactivation does not replay old commands automatically.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F010 — Invite and recovery

Feature F010 · module M04 · QA task INV-046.

- Given: Authorized Tenant admin and valid Identity, invitations and devices prerequisites.
- When: Invite and recovery.
- Then: Invitation and password-reset tokens are single-use, expire and cannot change tenant scope.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F011 — MFA and sessions

Feature F011 · module M04 · QA task INV-046.

- Given: Authorized Tenant admin and valid Identity, invitations and devices prerequisites.
- When: MFA and sessions.
- Then: MFA is mandatory for platform and tenant administrators; recovery codes are hashed, single-use and audited.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F012 — Device revocation

Feature F012 · module M04 · QA task INV-046.

- Given: Authorized Tenant admin and valid Identity, invitations and devices prerequisites.
- When: Device revocation.
- Then: A revoked Android device loses sync access immediately online; local unlock expires within 24 hours offline and queued work requires renewed authorization.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F013 — Permission catalog

Feature F013 · module M05 · QA task INV-062.

- Given: Authorized Tenant admin and valid Scoped roles and permissions prerequisites.
- When: Permission catalog.
- Then: Each action has a declared permission; default roles and custom roles use the same authorization path.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F014 — Tenant company warehouse boundaries

Feature F014 · module M05 · QA task INV-062.

- Given: Authorized Tenant admin and valid Scoped roles and permissions prerequisites.
- When: Tenant company warehouse boundaries.
- Then: Grants union only within their authorized scopes; foreign tenant IDs and warehouse IDs are denied even when object UUIDs are known.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F015 — Support access

Feature F015 · module M05 · QA task INV-062.

- Given: Authorized Tenant admin and valid Scoped roles and permissions prerequisites.
- When: Support access.
- Then: Time-limited customer-approved support sessions are read-only by default and separately audited; platform staff never inherit unrestricted warehouse access.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F016 — Policy routing

Feature F016 · module M06 · QA task INV-078.

- Given: Authorized Tenant admin and valid Approval policies and decisions prerequisites.
- When: Policy routing.
- Then: Company and warehouse policies resolve deterministically using most-specific scope then amount threshold; missing approver configuration blocks submission.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F017 — Separation of duties

Feature F017 · module M06 · QA task INV-078.

- Given: Authorized Tenant admin and valid Approval policies and decisions prerequisites.
- When: Separation of duties.
- Then: Requesters cannot approve their own adjustment, PO, scrap, period close or intercompany transaction.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F018 — Approval versioning

Feature F018 · module M06 · QA task INV-078.

- Given: Authorized Tenant admin and valid Approval policies and decisions prerequisites.
- When: Approval versioning.
- Then: Submission snapshots policy and document version; editing an approved document requires a new revision and approval.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F019 — Transactional audit

Feature F019 · module M07 · QA task INV-094.

- Given: Authorized Auditor and valid Audit and business events prerequisites.
- When: Transactional audit.
- Then: Every sensitive mutation writes its audit and outbox record in the same database transaction or fully rolls back.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F020 — Append-only evidence

Feature F020 · module M07 · QA task INV-094.

- Given: Authorized Auditor and valid Audit and business events prerequisites.
- When: Append-only evidence.
- Then: Application roles cannot edit or delete audit records; corrections reference the original action.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F021 — Event privacy

Feature F021 · module M07 · QA task INV-094.

- Given: Authorized Auditor and valid Audit and business events prerequisites.
- When: Event privacy.
- Then: Event payloads contain scoped identifiers and necessary facts only; secrets and contact data are excluded from analytics.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F022 — Idempotent commands

Feature F022 · module M08 · QA task INV-110.

- Given: Authorized Platform operator and valid Jobs, idempotency and delivery prerequisites.
- When: Idempotent commands.
- Then: Same key and same payload return the original committed result; same key with different payload returns 409.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F023 — Outbox processing

Feature F023 · module M08 · QA task INV-110.

- Given: Authorized Platform operator and valid Jobs, idempotency and delivery prerequisites.
- When: Outbox processing.
- Then: Worker crash before or after delivery never duplicates downstream postings; consumers deduplicate by event ID.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F024 — Retries and dead letters

Feature F024 · module M08 · QA task INV-110.

- Given: Authorized Platform operator and valid Jobs, idempotency and delivery prerequisites.
- When: Retries and dead letters.
- Then: Exponential retry with jitter stops after eight attempts and raises an actionable dead-letter alert; manual replay retains the original correlation ID.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F025 — Private attachments

Feature F025 · module M09 · QA task INV-125.

- Given: Authorized Buyer and valid Attachments and collaboration prerequisites.
- When: Private attachments.
- Then: Upload size and MIME limits, malware quarantine and entity authorization apply before a file becomes downloadable.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F026 — Comments and evidence

Feature F026 · module M09 · QA task INV-125.

- Given: Authorized Buyer and valid Attachments and collaboration prerequisites.
- When: Comments and evidence.
- Then: Scoped comments and attachments remain linked to business documents after archival; personal data export and retention rules apply.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F027 — Notification routing

Feature F027 · module M10 · QA task INV-140.

- Given: Authorized Tenant admin and valid Notifications and preferences prerequisites.
- When: Notification routing.
- Then: Approval, shortage, expiry, recall and sync-conflict events target authorized recipients only.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F028 — Delivery and preferences

Feature F028 · module M10 · QA task INV-140.

- Given: Authorized Tenant admin and valid Notifications and preferences prerequisites.
- When: Delivery and preferences.
- Then: In-app and email notifications deduplicate by recipient and event; transactional security notices cannot be disabled.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F029 — Accessible visual system

Feature F029 · module M11 · QA task INV-146.

- Given: Authorized Designer and valid Design system and accessibility prerequisites.
- When: Accessible visual system.
- Then: Shared typography, spacing, color, forms and tables cover light/dark themes, keyboard navigation and WCAG 2.2 AA acceptance checks.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F030 — Screen state contracts

Feature F030 · module M11 · QA task INV-146.

- Given: Authorized Designer and valid Design system and accessibility prerequisites.
- When: Screen state contracts.
- Then: Every screen defines loading, empty, permission-denied, error, offline and lifecycle states across 375/768/1280/1920/2560 widths.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F031 — Office context switching

Feature F031 · module M12 · QA task INV-162.

- Given: Authorized All staff and valid Office and admin application shells prerequisites.
- When: Office context switching.
- Then: Company and warehouse context is visible on every operational screen; switching clears stale query caches and unsaved work is confirmed.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F032 — Platform admin separation

Feature F032 · module M12 · QA task INV-162.

- Given: Authorized All staff and valid Office and admin application shells prerequisites.
- When: Platform admin separation.
- Then: Tenant administration and platform support use separate navigation and permissions; bundles are not the security boundary.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F033 — Search and navigation

Feature F033 · module M12 · QA task INV-162.

- Given: Authorized All staff and valid Office and admin application shells prerequisites.
- When: Search and navigation.
- Then: Keyboard search uses authorized results and preserves tenant/company context in deep links.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F034 — Durable local repository

Feature F034 · module M13 · QA task INV-179.

- Given: Authorized Warehouse operator and valid Android foundation and sync protocol prerequisites.
- When: Durable local repository.
- Then: Encrypted SQLite cache and command queue survive process death; tenant switching wipes cached data before a new bootstrap.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F035 — Sync protocol foundation

Feature F035 · module M13 · QA task INV-179.

- Given: Authorized Warehouse operator and valid Android foundation and sync protocol prerequisites.
- When: Sync protocol foundation.
- Then: Cursor-based pulls, tombstones, command IDs and ordered dependencies have executable protocol fixtures before business mobile screens.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F036 — Pending versus posted

Feature F036 · module M13 · QA task INV-179.

- Given: Authorized Warehouse operator and valid Android foundation and sync protocol prerequisites.
- When: Pending versus posted.
- Then: Offline captures display pending status and never claim stock is committed until server acknowledgement.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F037 — Company and branch setup

Feature F037 · module M14 · QA task INV-195.

- Given: Authorized Tenant admin and valid Companies, branches and regional settings prerequisites.
- When: Company and branch setup.
- Then: Codes are unique within tenant/company; active warehouses prevent hard deletion of their parent.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F038 — Regional defaults

Feature F038 · module M14 · QA task INV-195.

- Given: Authorized Tenant admin and valid Companies, branches and regional settings prerequisites.
- When: Regional defaults.
- Then: New companies default to ETB, English and Africa/Addis_Ababa; UTC instants and company-local business dates remain distinct.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F039 — Currency governance

Feature F039 · module M14 · QA task INV-195.

- Given: Authorized Tenant admin and valid Companies, branches and regional settings prerequisites.
- When: Currency governance.
- Then: Company base currency is immutable after the first valued movement; foreign-currency orders snapshot exchange rates with source and effective date.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F040 — Partner directory

Feature F040 · module M15 · QA task INV-211.

- Given: Authorized Buyer and valid Suppliers and customers prerequisites.
- When: Partner directory.
- Then: A partner may be both supplier and customer; archive blocks new orders while retaining history.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F041 — Partner commercial references

Feature F041 · module M15 · QA task INV-211.

- Given: Authorized Buyer and valid Suppliers and customers prerequisites.
- When: Partner commercial references.
- Then: Supplier SKU, purchase unit, minimum order and lead time are effective-dated; customer item codes do not overwrite internal SKUs.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F042 — Contact privacy

Feature F042 · module M15 · QA task INV-211.

- Given: Authorized Buyer and valid Suppliers and customers prerequisites.
- When: Contact privacy.
- Then: Contact exports and deletion/anonymization follow retention rules without deleting stock evidence.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F043 — Product and variant catalog

Feature F043 · module M16 · QA task INV-228.

- Given: Authorized Catalog manager and valid Products, variants and packaging prerequisites.
- When: Product and variant catalog.
- Then: SKU and barcode uniqueness are enforced per company; variant attribute combinations cannot duplicate.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F044 — Tracking configuration

Feature F044 · module M16 · QA task INV-228.

- Given: Authorized Catalog manager and valid Products, variants and packaging prerequisites.
- When: Tracking configuration.
- Then: None, lot or serial tracking is chosen before stock exists; changing it requires a controlled migration and reconciliation.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F045 — Packaging and barcode aliases

Feature F045 · module M16 · QA task INV-228.

- Given: Authorized Catalog manager and valid Products, variants and packaging prerequisites.
- When: Packaging and barcode aliases.
- Then: Multiple packaging barcodes resolve to explicit unit quantities; a carton scan cannot silently count as one base unit.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F046 — Catalog import

Feature F046 · module M16 · QA task INV-228.

- Given: Authorized Catalog manager and valid Products, variants and packaging prerequisites.
- When: Catalog import.
- Then: CSV dry-run reports row-level duplicate codes and invalid references; accepted batches are idempotent.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F047 — Unit conversions

Feature F047 · module M17 · QA task INV-244.

- Given: Authorized Catalog manager and valid Units and exact arithmetic prerequisites.
- When: Unit conversions.
- Then: Convert only within a unit category using exact rational factors; snapshot conversions on document lines.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F048 — Quantity precision

Feature F048 · module M17 · QA task INV-244.

- Given: Authorized Catalog manager and valid Units and exact arithmetic prerequisites.
- When: Quantity precision.
- Then: Quantities use decimal strings with at most six fractional digits; serial quantities are whole units and conversion remainder must be explicitly resolved.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F049 — Monetary precision

Feature F049 · module M17 · QA task INV-244.

- Given: Authorized Catalog manager and valid Units and exact arithmetic prerequisites.
- When: Monetary precision.
- Then: Unit costs and rates use fixed precision; extended amounts round half-up to currency minor units once at document boundaries with deterministic remainder allocation.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F050 — Location hierarchy

Feature F050 · module M18 · QA task INV-260.

- Given: Authorized Warehouse supervisor and valid Warehouses and location hierarchy prerequisites.
- When: Location hierarchy.
- Then: Warehouse, zone and bin form an acyclic tree; supplier, customer, inventory-loss and transit locations have explicit types.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F051 — Operational areas

Feature F051 · module M18 · QA task INV-260.

- Given: Authorized Warehouse supervisor and valid Warehouses and location hierarchy prerequisites.
- When: Operational areas.
- Then: Receiving, quarantine, stock, packing and dispatch locations have reservation eligibility rules.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F052 — Archival and capacity

Feature F052 · module M18 · QA task INV-260.

- Given: Authorized Warehouse supervisor and valid Warehouses and location hierarchy prerequisites.
- When: Archival and capacity.
- Then: Occupied or reserved locations cannot be archived; putaway cannot exceed configured capacity without a supervisor-approved exception.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F053 — Lot and serial identity

Feature F053 · module M19 · QA task INV-276.

- Given: Authorized Catalog manager and valid Lot, serial and ownership identities prerequisites.
- When: Lot and serial identity.
- Then: Tracking identifiers are company/product scoped; a serial cannot simultaneously exist in two physical locations.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F054 — Ownership dimensions

Feature F054 · module M19 · QA task INV-276.

- Given: Authorized Catalog manager and valid Lot, serial and ownership identities prerequisites.
- When: Ownership dimensions.
- Then: Every stock bucket distinguishes company-owned and partner-owned goods; supplier custody is not company valuation.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F055 — Receipt tracking requirements

Feature F055 · module M19 · QA task INV-276.

- Given: Authorized Catalog manager and valid Lot, serial and ownership identities prerequisites.
- When: Receipt tracking requirements.
- Then: Tracked products cannot be posted without lot/serial allocation; early phases may create identities but advanced recall controls arrive in phase 8.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F056 — Posting transaction

Feature F056 · module M20 · QA task INV-293.

- Given: Authorized Warehouse supervisor and valid Immutable stock ledger and projections prerequisites.
- When: Posting transaction.
- Then: Lock affected buckets in canonical order; move, balance, cost fact, command receipt, audit and outbox commit atomically.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F057 — No negative physical stock

Feature F057 · module M20 · QA task INV-293.

- Given: Authorized Warehouse supervisor and valid Immutable stock ledger and projections prerequisites.
- When: No negative physical stock.
- Then: Concurrent outgoing moves cannot reduce a controlled physical bucket below zero; shortages return a typed conflict without partial effects.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F058 — Reversal and rebuild

Feature F058 · module M20 · QA task INV-293.

- Given: Authorized Warehouse supervisor and valid Immutable stock ledger and projections prerequisites.
- When: Reversal and rebuild.
- Then: Posted rows are immutable; eligible reversals reference originals and a rebuild from movements reproduces projections exactly.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F059 — Cost fact capture

Feature F059 · module M20 · QA task INV-293.

- Given: Authorized Warehouse supervisor and valid Immutable stock ledger and projections prerequisites.
- When: Cost fact capture.
- Then: Receipt/issue source costs, conversion factors and ownership are preserved from day one for phase 11 valuation replay; financial go-live is gated until valuation is complete.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F060 — Atomic allocation

Feature F060 · module M21 · QA task INV-309.

- Given: Authorized Sales clerk and valid Reservations and availability prerequisites.
- When: Atomic allocation.
- Then: Two concurrent orders requesting the same ten units can reserve at most ten in total.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F061 — Partial allocation and release

Feature F061 · module M21 · QA task INV-309.

- Given: Authorized Sales clerk and valid Reservations and availability prerequisites.
- When: Partial allocation and release.
- Then: Partial fills identify remaining demand; cancel, expiry and short-pick release only unconsumed reservations.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F062 — Availability and forecast

Feature F062 · module M21 · QA task INV-309.

- Given: Authorized Sales clerk and valid Reservations and availability prerequisites.
- When: Availability and forecast.
- Then: Available equals eligible on-hand minus active reservations; forecast adds dated confirmed receipts and subtracts outstanding demand without double-counting reservations.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F063 — Opening stock

Feature F063 · module M22 · QA task INV-325.

- Given: Authorized Warehouse operator and valid Core receipts, issues and opening stock prerequisites.
- When: Opening stock.
- Then: Approved opening batches load quantities, tracking and cost basis once with reconciliation totals and a migration reference.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F064 — Receipt and internal issue

Feature F064 · module M22 · QA task INV-325.

- Given: Authorized Warehouse operator and valid Core receipts, issues and opening stock prerequisites.
- When: Receipt and internal issue.
- Then: Done quantities are validated against unit/tracking rules; controlled over-receipts require explicit approval.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F065 — Partial operations and backorders

Feature F065 · module M22 · QA task INV-325.

- Given: Authorized Warehouse operator and valid Core receipts, issues and opening stock prerequisites.
- When: Partial operations and backorders.
- Then: Posting part of a document creates a linked remainder or cancels it explicitly; replay never creates a second backorder.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F066 — Immediate and staged transfers

Feature F066 · module M23 · QA task INV-341.

- Given: Authorized Warehouse operator and valid Transfers and in-transit custody prerequisites.
- When: Immediate and staged transfers.
- Then: In-warehouse moves commit once; inter-warehouse shipment moves stock into transit until destination receipt.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F067 — Partial receipt and discrepancy

Feature F067 · module M23 · QA task INV-341.

- Given: Authorized Warehouse operator and valid Transfers and in-transit custody prerequisites.
- When: Partial receipt and discrepancy.
- Then: Received quantity cannot exceed shipped balance; missing or damaged quantities stay in transit until approved return/scrap resolution.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F068 — Transfer conservation

Feature F068 · module M23 · QA task INV-341.

- Given: Authorized Warehouse operator and valid Transfers and in-transit custody prerequisites.
- When: Transfer conservation.
- Then: Company-owned quantities sum equally across source, transit and destination before and after transfer; retries preserve totals.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F069 — Requisition and quotation comparison

Feature F069 · module M24 · QA task INV-358.

- Given: Authorized Requester and valid Requisitions, RFQs and purchase orders prerequisites.
- When: Requisition and quotation comparison.
- Then: Approved need produces RFQs; offers compare converted units, currency, lead time and landed-cost estimates without hiding original prices.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F070 — Approved PO revisions

Feature F070 · module M24 · QA task INV-358.

- Given: Authorized Requester and valid Requisitions, RFQs and purchase orders prerequisites.
- When: Approved PO revisions.
- Then: Approved orders snapshot commercial terms; amendment preserves prior revision and reapproves changed commitments.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F071 — Blanket order releases

Feature F071 · module M24 · QA task INV-358.

- Given: Authorized Requester and valid Requisitions, RFQs and purchase orders prerequisites.
- When: Blanket order releases.
- Then: Call-offs cannot exceed approved quantity/value ceiling or validity dates without a new agreement revision.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F072 — Purchase cancellation

Feature F072 · module M24 · QA task INV-358.

- Given: Authorized Requester and valid Requisitions, RFQs and purchase orders prerequisites.
- When: Purchase cancellation.
- Then: Cancel only unreceived quantities; received quantities require vendor-return workflow rather than destructive edits.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F073 — PO receipt matching

Feature F073 · module M25 · QA task INV-374.

- Given: Authorized Warehouse operator and valid Supplier receiving and inspection handoff prerequisites.
- When: PO receipt matching.
- Then: Partial deliveries track ordered, received and outstanding quantities independently; receipt references deduplicate within supplier/company.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F074 — Receive to quarantine

Feature F074 · module M25 · QA task INV-374.

- Given: Authorized Warehouse operator and valid Supplier receiving and inspection handoff prerequisites.
- When: Receive to quarantine.
- Then: Inspection-required stock posts into quarantine; accepted goods become available only after quality release.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F075 — Receipt cost snapshot

Feature F075 · module M25 · QA task INV-374.

- Given: Authorized Warehouse operator and valid Supplier receiving and inspection handoff prerequisites.
- When: Receipt cost snapshot.
- Then: Purchase price, exchange rate and unit conversion are copied onto cost facts without creating a vendor bill.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F076 — Inspection execution

Feature F076 · module M26 · QA task INV-390.

- Given: Authorized Quality inspector and valid Quality inspections and disposition prerequisites.
- When: Inspection execution.
- Then: Required checklist results and evidence must be complete before disposition; inspector authority is warehouse scoped.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F077 — Split disposition

Feature F077 · module M26 · QA task INV-390.

- Given: Authorized Quality inspector and valid Quality inspections and disposition prerequisites.
- When: Split disposition.
- Then: Accepted plus rejected quantities equal inspected quantity; release moves accepted stock only and leaves rejected stock blocked.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F078 — Reinspection and evidence

Feature F078 · module M26 · QA task INV-390.

- Given: Authorized Quality inspector and valid Quality inspections and disposition prerequisites.
- When: Reinspection and evidence.
- Then: Failed items require a new linked inspection; prior results remain immutable.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F079 — Quotation and pricing

Feature F079 · module M27 · QA task INV-406.

- Given: Authorized Sales clerk and valid Sales quotations and orders prerequisites.
- When: Quotation and pricing.
- Then: Server resolves effective price tier and currency; discounts beyond configured authority require approval.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F080 — Sales confirmation

Feature F080 · module M27 · QA task INV-406.

- Given: Authorized Sales clerk and valid Sales quotations and orders prerequisites.
- When: Sales confirmation.
- Then: Confirmation snapshots terms and creates fulfillment demand; insufficient stock produces partial allocation/backorder rather than a fictitious sale of available stock.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F081 — Order changes

Feature F081 · module M27 · QA task INV-406.

- Given: Authorized Sales clerk and valid Sales quotations and orders prerequisites.
- When: Order changes.
- Then: Shipped quantities cannot be cancelled; edits to unfulfilled demand release/recompute reservations and version checks prevent lost updates.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F082 — Pick verification

Feature F082 · module M28 · QA task INV-422.

- Given: Authorized Picker and valid Pick, pack and dispatch prerequisites.
- When: Pick verification.
- Then: Location, SKU, lot/serial and actual quantity match the assigned task; short-picks release missing reservation and record reason.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F083 — Packing control

Feature F083 · module M28 · QA task INV-422.

- Given: Authorized Picker and valid Pick, pack and dispatch prerequisites.
- When: Packing control.
- Then: Package contents cannot exceed picked stock; repacking preserves traceability and labels identify packages uniquely.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F084 — Dispatch and delivery records

Feature F084 · module M28 · QA task INV-422.

- Given: Authorized Picker and valid Pick, pack and dispatch prerequisites.
- When: Dispatch and delivery records.
- Then: Dispatch consumes reservations and posts outgoing stock exactly once; packing slip is explicitly not a tax invoice.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F085 — Linked return entitlement

Feature F085 · module M29 · QA task INV-438.

- Given: Authorized Sales clerk and valid Customer and vendor returns prerequisites.
- When: Linked return entitlement.
- Then: Cumulative returned quantities cannot exceed original delivered/received quantities; serial returns must match originals.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F086 — Customer return inspection

Feature F086 · module M29 · QA task INV-438.

- Given: Authorized Sales clerk and valid Customer and vendor returns prerequisites.
- When: Customer return inspection.
- Then: Returned stock enters quarantine, then restock or scrap; original movement cost basis is retained for valuation.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F087 — Vendor returns

Feature F087 · module M29 · QA task INV-438.

- Given: Authorized Sales clerk and valid Customer and vendor returns prerequisites.
- When: Vendor returns.
- Then: Rejected or authorized stock ships to supplier and adjusts PO receiving status according to explicit replace-or-close choice; no credit note is issued here.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F088 — Expiry and FEFO

Feature F088 · module M30 · QA task INV-454.

- Given: Authorized Quality inspector and valid Expiry, recalls and scrap prerequisites.
- When: Expiry and FEFO.
- Then: Removal date drives FEFO with deterministic lot tie-breaks; expired, recalled or quarantined stock is not reservable.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F089 — Recall genealogy

Feature F089 · module M30 · QA task INV-454.

- Given: Authorized Quality inspector and valid Expiry, recalls and scrap prerequisites.
- When: Recall genealogy.
- Then: Lot/serial trace traverses receipts, internal moves, shipments and returns; affected customer contacts are access-controlled.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F090 — Approved scrap

Feature F090 · module M30 · QA task INV-454.

- Given: Authorized Quality inspector and valid Expiry, recalls and scrap prerequisites.
- When: Approved scrap.
- Then: Scrap posts to a loss location only after approval and evidence; quantities and value remain traceable through reversal rules.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F091 — Blind and cycle counting

Feature F091 · module M31 · QA task INV-470.

- Given: Authorized Counter and valid Blind counts and reconciliation prerequisites.
- When: Blind and cycle counting.
- Then: Counter sees required identities but not system quantity; location schedules generate count assignments without duplicates.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F092 — Moving-stock reconciliation

Feature F092 · module M31 · QA task INV-470.

- Given: Authorized Counter and valid Blind counts and reconciliation prerequisites.
- When: Moving-stock reconciliation.
- Then: Snapshot plus timestamped movements is reconciled to each count observation; ambiguous late/offline observations require recount before posting.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F093 — Variance approval

Feature F093 · module M31 · QA task INV-470.

- Given: Authorized Counter and valid Blind counts and reconciliation prerequisites.
- When: Variance approval.
- Then: Independent approval posts signed adjustments once; zero variance produces no movement and original observations remain immutable.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F094 — Multi-step routes

Feature F094 · module M32 · QA task INV-486.

- Given: Authorized Warehouse supervisor and valid Routes, putaway and cross-docking prerequisites.
- When: Multi-step routes.
- Then: One/two/three-step inbound and outbound templates create dependent operations exactly once; activated route versions are snapshotted per operation.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F095 — Putaway and capacity

Feature F095 · module M32 · QA task INV-486.

- Given: Authorized Warehouse supervisor and valid Routes, putaway and cross-docking prerequisites.
- When: Putaway and capacity.
- Then: Rules choose eligible destinations deterministically by priority and free capacity; no eligible destination creates an exception task.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F096 — Cross-docking

Feature F096 · module M32 · QA task INV-486.

- Given: Authorized Warehouse supervisor and valid Routes, putaway and cross-docking prerequisites.
- When: Cross-docking.
- Then: Incoming accepted stock can satisfy outbound demand without visiting storage while retaining reservation, ownership and inspection requirements.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F097 — Batch and wave formation

Feature F097 · module M33 · QA task INV-502.

- Given: Authorized Warehouse supervisor and valid Batch and wave picking prerequisites.
- When: Batch and wave formation.
- Then: Group compatible pick tasks within one warehouse and ownership boundary; a task belongs to only one active released batch.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F098 — Picking strategies

Feature F098 · module M33 · QA task INV-502.

- Given: Authorized Warehouse supervisor and valid Batch and wave picking prerequisites.
- When: Picking strategies.
- Then: Support piece, batch and wave execution using configured FIFO/FEFO/nearest-location selection; costing method remains independent from physical selection.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F099 — Replanning exceptions

Feature F099 · module M33 · QA task INV-502.

- Given: Authorized Warehouse supervisor and valid Batch and wave picking prerequisites.
- When: Replanning exceptions.
- Then: Short-picks and cancellations replan only uncompleted work without losing completed scan evidence.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F100 — Min-max and safety stock

Feature F100 · module M34 · QA task INV-518.

- Given: Authorized Buyer and valid Replenishment and demand planning prerequisites.
- When: Min-max and safety stock.
- Then: Dated forecast below minimum suggests replenishment to maximum with purchase multiples, lead time and explicit safety buffer.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F101 — Buyer approval

Feature F101 · module M34 · QA task INV-518.

- Given: Authorized Buyer and valid Replenishment and demand planning prerequisites.
- When: Buyer approval.
- Then: Accepted suggestion creates a draft requisition or PO for normal approval; rerunning planning does not duplicate existing supply.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F102 — Pick-face replenishment

Feature F102 · module M34 · QA task INV-518.

- Given: Authorized Buyer and valid Replenishment and demand planning prerequisites.
- When: Pick-face replenishment.
- Then: Bin replenishment moves eligible reserve stock to pick locations and reports shortages without generating impossible transfers.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F103 — Consignment custody

Feature F103 · module M35 · QA task INV-534.

- Given: Authorized Buyer and valid Consignment and owner-separated stock prerequisites.
- When: Consignment custody.
- Then: Partner-owned stock appears in custody quantities but is excluded from company-owned value and unavailable to unrelated owner demand.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F104 — Ownership acquisition

Feature F104 · module M35 · QA task INV-534.

- Given: Authorized Buyer and valid Consignment and owner-separated stock prerequisites.
- When: Ownership acquisition.
- Then: Approved acquisition changes ownership through paired ledger movements and a documented cost basis; custody location need not change.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F105 — Owner returns

Feature F105 · module M35 · QA task INV-534.

- Given: Authorized Buyer and valid Consignment and owner-separated stock prerequisites.
- When: Owner returns.
- Then: Unsold consignment returns to its owner without treating it as a company-owned inventory sale.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F106 — Linked supplier fulfillment

Feature F106 · module M36 · QA task INV-550.

- Given: Authorized Buyer and valid Dropship fulfillment prerequisites.
- When: Linked supplier fulfillment.
- Then: Eligible sales demand creates linked purchase demand without reserving warehouse stock.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F107 — Supplier delivery evidence

Feature F107 · module M36 · QA task INV-550.

- Given: Authorized Buyer and valid Dropship fulfillment prerequisites.
- When: Supplier delivery evidence.
- Then: Confirmation updates fulfillment and external-location movement history exactly once; internal on-hand remains unchanged.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F108 — Dropship returns

Feature F108 · module M36 · QA task INV-550.

- Given: Authorized Buyer and valid Dropship fulfillment prerequisites.
- When: Dropship returns.
- Then: Return authorization records supplier/customer routing and ownership without manufacturing a warehouse receipt.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F109 — Paired commercial documents

Feature F109 · module M37 · QA task INV-566.

- Given: Authorized Company admin and valid Intercompany trade and transfers prerequisites.
- When: Paired commercial documents.
- Then: Within one tenant, approved intercompany requests create linked sale/purchase documents with explicit currencies and prices.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F110 — Company-local ledgers

Feature F110 · module M37 · QA task INV-566.

- Given: Authorized Company admin and valid Intercompany trade and transfers prerequisites.
- When: Company-local ledgers.
- Then: Shipment and receipt use each company ledger and base currency; buyer receipt is not posted before physical receipt.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F111 — Independent permissions

Feature F111 · module M37 · QA task INV-566.

- Given: Authorized Company admin and valid Intercompany trade and transfers prerequisites.
- When: Independent permissions.
- Then: Users require explicit rights in each company for paired actions; no cross-tenant automatic trading is permitted in baseline.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F112 — Phantom kit definitions

Feature F112 · module M38 · QA task INV-582.

- Given: Authorized Catalog manager and valid Kits without manufacturing prerequisites.
- When: Phantom kit definitions.
- Then: Versioned kits explode into stock components; cyclic/nested definitions are validated and no manufactured finished-stock balance is created.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F113 — Kit allocation and fulfillment

Feature F113 · module M38 · QA task INV-582.

- Given: Authorized Catalog manager and valid Kits without manufacturing prerequisites.
- When: Kit allocation and fulfillment.
- Then: Available kits equal the limiting component quantity; partial-kit dispatch is blocked unless order is explicitly revised to components.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F114 — Kit returns

Feature F114 · module M38 · QA task INV-582.

- Given: Authorized Catalog manager and valid Kits without manufacturing prerequisites.
- When: Kit returns.
- Then: Return evidence identifies actual components and original allocation costs rather than inventing a kit valuation layer.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F115 — Offline operational capture

Feature F115 · module M39 · QA task INV-599.

- Given: Authorized Warehouse operator and valid Offline Android warehouse workflows prerequisites.
- When: Offline operational capture.
- Then: Receipt, transfer, pick, pack and count observations queue durably with source document version and command dependencies.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F116 — Conflict review

Feature F116 · module M39 · QA task INV-599.

- Given: Authorized Warehouse operator and valid Offline Android warehouse workflows prerequisites.
- When: Conflict review.
- Then: Insufficient stock, revoked permissions, changed documents and expired task leases create explicit actionable conflicts; stock quantities never use last-write-wins.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F117 — Reconnect recovery

Feature F117 · module M39 · QA task INV-599.

- Given: Authorized Warehouse operator and valid Offline Android warehouse workflows prerequisites.
- When: Reconnect recovery.
- Then: Airplane mode, process death, duplicated batches and intermittent acknowledgements produce one committed operation or one visible unresolved conflict.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F118 — Camera and handheld scanning

Feature F118 · module M40 · QA task INV-616.

- Given: Authorized Warehouse operator and valid Scanners, labels and printer interfaces prerequisites.
- When: Camera and handheld scanning.
- Then: Camera, keyboard-wedge and Android intent scanner adapters normalize input without dropping GS1 separators or leading zeroes.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F119 — GS1 parsing

Feature F119 · module M40 · QA task INV-616.

- Given: Authorized Warehouse operator and valid Scanners, labels and printer interfaces prerequisites.
- When: GS1 parsing.
- Then: Parse GTIN, lot, serial and expiry application identifiers with length/check-digit validation; internal labels never impersonate assigned GS1 company prefixes.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F120 — Label generation and reprints

Feature F120 · module M40 · QA task INV-616.

- Given: Authorized Warehouse operator and valid Scanners, labels and printer interfaces prerequisites.
- When: Label generation and reprints.
- Then: PDF and ZPL interfaces support product, bin, lot and package labels; retries/reprints preserve entity IDs and are logged.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F121 — FIFO costing

Feature F121 · module M41 · QA task INV-633.

- Given: Authorized Valuation analyst and valid Valuation methods and subledger prerequisites.
- When: FIFO costing.
- Then: Outgoing owned stock consumes oldest eligible company/product cost layers; physical picking strategy does not change costing order.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F122 — Weighted-average costing

Feature F122 · module M41 · QA task INV-633.

- Given: Authorized Valuation analyst and valid Valuation methods and subledger prerequisites.
- When: Weighted-average costing.
- Then: Incoming cost updates the exact moving average; issues use the current average and rounding residual stays reconciled to remaining value.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F123 — Standard costing

Feature F123 · module M41 · QA task INV-633.

- Given: Authorized Valuation analyst and valid Valuation methods and subledger prerequisites.
- When: Standard costing.
- Then: Approved standard cost versions apply prospectively and price differences are recorded as valuation variance, not silently dropped.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F124 — Returns and replay

Feature F124 · module M41 · QA task INV-633.

- Given: Authorized Valuation analyst and valid Valuation methods and subledger prerequisites.
- When: Returns and replay.
- Then: Returns reverse original issue/receipt basis; replay of immutable cost facts yields the same quantity/value totals and identifies any missing historical basis.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F125 — Charge allocation

Feature F125 · module M42 · QA task INV-649.

- Given: Authorized Valuation analyst and valid Landed costs and revaluation prerequisites.
- When: Charge allocation.
- Then: Freight, duty and handling charges from external evidence allocate by quantity, value, weight or volume; missing bases block allocation.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F126 — Remainder and consumed stock

Feature F126 · module M42 · QA task INV-649.

- Given: Authorized Valuation analyst and valid Landed costs and revaluation prerequisites.
- When: Remainder and consumed stock.
- Then: Allocation sums exactly to total charges; already-consumed shares create linked valuation adjustments rather than rewriting posted issue rows.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F127 — Approved revaluation

Feature F127 · module M42 · QA task INV-649.

- Given: Authorized Valuation analyst and valid Landed costs and revaluation prerequisites.
- When: Approved revaluation.
- Then: Revaluation records reason, authorization and effective open period; standard-cost changes produce explicit remaining-stock delta.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F128 — Period reconciliation

Feature F128 · module M43 · QA task INV-665.

- Given: Authorized Valuation analyst and valid Valuation periods and reconciliation prerequisites.
- When: Period reconciliation.
- Then: Owned stock quantities and value reconcile by product/company; transit, consignment and external locations are separately explained.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F129 — Close prerequisites

Feature F129 · module M43 · QA task INV-665.

- Given: Authorized Valuation analyst and valid Valuation periods and reconciliation prerequisites.
- When: Close prerequisites.
- Then: Missing costs, unresolved valuation errors and unreviewed export differences block close; late physical activity posts in the current open period with original occurrence date retained.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F130 — Controlled reopen

Feature F130 · module M43 · QA task INV-665.

- Given: Authorized Valuation analyst and valid Valuation periods and reconciliation prerequisites.
- When: Controlled reopen.
- Then: Reopen requires independent approval and reason; a new close/export revision supersedes the old one without deleting evidence.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F131 — Balanced export format

Feature F131 · module M44 · QA task INV-681.

- Given: Authorized Valuation analyst and valid Accounting export batches prerequisites.
- When: Balanced export format.
- Then: Versioned CSV/JSON inventory journal proposals balance by currency and map every line to valuation evidence; missing external account mappings block release.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F132 — Delivery acknowledgement

Feature F132 · module M44 · QA task INV-681.

- Given: Authorized Valuation analyst and valid Accounting export batches prerequisites.
- When: Delivery acknowledgement.
- Then: Same batch ID and checksum replay safely; conflicting acknowledgement is rejected and partial rejection stays visible for reconciliation.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F133 — Accounting boundary

Feature F133 · module M44 · QA task INV-681.

- Given: Authorized Valuation analyst and valid Accounting export batches prerequisites.
- When: Accounting boundary.
- Then: External ledger owns posting and financial statements; the product emits inventory proposals only and never claims to create invoices, bills or bank transactions.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F134 — As-of stock and value

Feature F134 · module M45 · QA task INV-697.

- Given: Authorized Warehouse supervisor and valid Operational reports and analytics prerequisites.
- When: As-of stock and value.
- Then: Stock card, on-hand, reserved, transit, owner, aging and value reports reconcile to the ledger at the same as-of instant.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F135 — Service metrics

Feature F135 · module M45 · QA task INV-697.

- Given: Authorized Warehouse supervisor and valid Operational reports and analytics prerequisites.
- When: Service metrics.
- Then: Fulfillment rate, backorder age, purchase lead-time variance and supplier acceptance rate have published numerator/denominator definitions.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F136 — Secure exports

Feature F136 · module M45 · QA task INV-697.

- Given: Authorized Warehouse supervisor and valid Operational reports and analytics prerequisites.
- When: Secure exports.
- Then: Large reports run as scoped jobs; permissions are rechecked on download and expired export URLs cannot be reused.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F137 — Public API contracts

Feature F137 · module M46 · QA task INV-714.

- Given: Authorized Integration operator and valid External APIs, imports and webhooks prerequisites.
- When: Public API contracts.
- Then: API keys are hashed, scoped, expiring and revocable; cursor pagination, rate limits and documented error shapes apply consistently.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F138 — Signed webhooks

Feature F138 · module M46 · QA task INV-714.

- Given: Authorized Integration operator and valid External APIs, imports and webhooks prerequisites.
- When: Signed webhooks.
- Then: HMAC signatures cover timestamp and raw body; replay window, secret rotation, destination validation and SSRF protection are tested.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F139 — Versioned imports

Feature F139 · module M46 · QA task INV-714.

- Given: Authorized Integration operator and valid External APIs, imports and webhooks prerequisites.
- When: Versioned imports.
- Then: Dry-run validates references and duplicates before commit; error CSV names exact rows and no partial stock posting is hidden.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F140 — Connector boundary

Feature F140 · module M46 · QA task INV-714.

- Given: Authorized Integration operator and valid External APIs, imports and webhooks prerequisites.
- When: Connector boundary.
- Then: Generic CSV/API/webhook adapters ship; named accounting, courier and payment connectors remain explicit later-scope entries.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F141 — Mapping and rehearsal

Feature F141 · module M47 · QA task INV-730.

- Given: Authorized Implementation operator and valid Customer migration and onboarding prerequisites.
- When: Mapping and rehearsal.
- Then: Map master data, opening quantities, tracking, ownership, reservations and opening cost layers with source checksums and reconciliation reports.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F142 — Cutover controls

Feature F142 · module M47 · QA task INV-730.

- Given: Authorized Implementation operator and valid Customer migration and onboarding prerequisites.
- When: Cutover controls.
- Then: Freeze source writes, apply the final delta, reconcile totals and obtain named customer approval before enabling production posting.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F143 — Rollback boundary

Feature F143 · module M47 · QA task INV-730.

- Given: Authorized Implementation operator and valid Customer migration and onboarding prerequisites.
- When: Rollback boundary.
- Then: Before first new live movement restore the rehearsed snapshot; afterward use forward corrections and replay accepted commands rather than deleting live history.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F144 — Support runbooks

Feature F144 · module M48 · QA task INV-746.

- Given: Authorized Platform operator and valid SaaS support and customer lifecycle prerequisites.
- When: Support runbooks.
- Then: Customer-approved support access is time-bounded and logged; cross-tenant searching requires a platform purpose and exposes minimum metadata.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F145 — Tenant portability

Feature F145 · module M48 · QA task INV-746.

- Given: Authorized Platform operator and valid SaaS support and customer lifecycle prerequisites.
- When: Tenant portability.
- Then: Export includes master data, documents, stock and valuation ledgers, attachments manifest and schema version; completeness is reconciled before delivery.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F146 — Offboarding and holds

Feature F146 · module M48 · QA task INV-746.

- Given: Authorized Platform operator and valid SaaS support and customer lifecycle prerequisites.
- When: Offboarding and holds.
- Then: Offboarding revokes access, schedules configured deletion and respects documented legal holds; backup expiry and data-destruction evidence are tracked.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F147 — Isolation assessment

Feature F147 · module M49 · QA task INV-762.

- Given: Authorized Security reviewer and valid Security, privacy and localization release prerequisites.
- When: Isolation assessment.
- Then: Negative tests cover API, raw application-role SQL, jobs, files, reports, mobile and integrations across two tenants and two companies.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F148 — Privacy rights and retention

Feature F148 · module M49 · QA task INV-762.

- Given: Authorized Security reviewer and valid Security, privacy and localization release prerequisites.
- When: Privacy rights and retention.
- Then: Export/anonymize contact data while retaining permitted transaction evidence; retention and hosting decisions require reviewed Ethiopian legal applicability, not assumed durations.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F149 — Launch security

Feature F149 · module M49 · QA task INV-762.

- Given: Authorized Security reviewer and valid Security, privacy and localization release prerequisites.
- When: Launch security.
- Then: Threat model, dependency/license scans, penetration-test findings and critical/high vulnerability closure are signed off before pilot.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F150 — Observability

Feature F150 · module M50 · QA task INV-779.

- Given: Authorized Platform operator and valid Reliability, recovery and performance prerequisites.
- When: Observability.
- Then: Metrics expose posting latency, lock conflicts, sync lag, dead letters, export failures, backup age and per-tenant resource saturation without PII.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F151 — Backup and recovery

Feature F151 · module M50 · QA task INV-779.

- Given: Authorized Platform operator and valid Reliability, recovery and performance prerequisites.
- When: Backup and recovery.
- Then: Encrypted backups and point-in-time recovery are rehearsed to a separate environment; target RPO is 15 minutes and RTO is four hours.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F152 — Performance budgets

Feature F152 · module M50 · QA task INV-779.

- Given: Authorized Platform operator and valid Reliability, recovery and performance prerequisites.
- When: Performance budgets.
- Then: At the documented launch dataset, online reads meet p95 500ms and stock posting p95 one second; Android critical flows work on a mid-range device with intermittent connectivity.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F153 — Safe deployment

Feature F153 · module M50 · QA task INV-779.

- Given: Authorized Platform operator and valid Reliability, recovery and performance prerequisites.
- When: Safe deployment.
- Then: Expand-contract migrations and tested rollback/forward-fix procedures preserve committed stock and valuation history.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F154 — Pilot scenario coverage

Feature F154 · module M51 · QA task INV-790.

- Given: Authorized Product owner and valid Pilot, training and production release prerequisites.
- When: Pilot scenario coverage.
- Then: Distributor, retailer warehouse and lot/expiry business pilots each sign off purchase-to-stock, order-to-dispatch, returns, counts and exports.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F155 — Training and support

Feature F155 · module M51 · QA task INV-790.

- Given: Authorized Product owner and valid Pilot, training and production release prerequisites.
- When: Training and support.
- Then: Role-based quick starts, barcode-device setup, offline conflict guidance and escalation contacts are delivered and exercised.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## T-F156 — Production go-live

Feature F156 · module M51 · QA task INV-790.

- Given: Authorized Product owner and valid Pilot, training and production release prerequisites.
- When: Production go-live.
- Then: All phase gates pass, critical defects are closed, restore evidence is current and customer acceptance is recorded; failed gates block release.
- Negative: Denied scope, invalid lifecycle or duplicate command causes no unauthorized/duplicate side effect.

## Cross-module critical scenarios

### C01 — Concurrent reservation

Owner: INV-309; modules: M20, M21.

Create ten available units. Submit two concurrent reservations of seven with different keys.

Expected: Total active reservations never exceed ten; losing request returns shortage or a documented partial allocation; no negative bucket.

### C02 — Atomic posting failure

Owner: INV-293; modules: M07, M08, M20.

Inject failure between movement, projection, audit and outbox writes. Retry the same command.

Expected: All writes roll back together; retry commits once and every projection matches the ledger.

### C03 — Duplicate and conflicting command

Owner: INV-325; modules: M08, M22.

Post a receipt twice with the same command ID, then reuse the ID with a changed quantity.

Expected: First two responses identify one receipt; changed payload returns 409 and creates no movement.

### C04 — Partial receipt and backorder

Owner: INV-390; modules: M24, M25, M26.

Order 100, receive 60, accept 55 and reject five, then receive the remaining 40.

Expected: Stock totals reflect 55 accepted, five quarantined/rejected and 40 newly inspected; order quantities and backorders do not duplicate.

### C05 — Transfer discrepancy

Owner: INV-470; modules: M23, M31.

Ship 20 to transit, receive 18, report two damaged, obtain scrap approval.

Expected: Source decreases 20, destination increases 18, transit decreases only when receipt and scrap are posted; loss is two and conservation holds.

### C06 — Unauthorized scope everywhere

Owner: INV-762; modules: M05, M46, M49.

Use tenant A credentials with tenant B IDs in API, raw app-role SQL, jobs, signed downloads, reports, sync and API keys.

Expected: No foreign row, attachment, event or balance leaks; all mutation attempts are rejected and logged without leaking private data.

### C07 — Serial uniqueness and returns

Owner: INV-438; modules: M19, M29.

Receive serial S once, attempt duplicate receipt, ship it, return twice.

Expected: A serial has one physical position; duplicate receipt and excessive return are rejected; first return goes to quarantine.

### C08 — Recall and expiry race

Owner: INV-454; modules: M21, M30.

Reserve a lot, activate recall or reach removal date, then attempt dispatch.

Expected: Dispatch rechecks eligibility and blocks; released reservations and affected customer trace remain auditable.

### C09 — Blind count with moving stock

Owner: INV-470; modules: M20, M31.

Snapshot 100, ship ten, observe 88, receive five, submit a late offline observation.

Expected: System reconciles observation-time movements; variance is not computed from a stale end balance; ambiguity requests recount; approved adjustment posts once.

### C10 — Costing and rounding

Owner: INV-633; modules: M17, M41.

Receive 10 at ETB 2 and 10 at ETB 4; issue 12. Repeat with fractional units and return two original issued units.

Expected: FIFO issue value is ETB 28 and remaining value ETB 32; moving average issue value is ETB 36 and remaining value ETB 24; returns restore original allocated basis and all minor-unit residuals reconcile.

### C11 — Landed costs after consumption

Owner: INV-649; modules: M41, M42.

Allocate ETB 10.01 over three equal receipt shares after one share has been consumed.

Expected: Allocated minor units sum to 1001; deterministic remainder assignment and consumed-stock adjustment preserve original rows and explain the full delta.

### C12 — Period lock and late receipt

Owner: INV-665; modules: M22, M43.

Close a period, submit a late-dated receipt and attempt a direct valuation edit.

Expected: Original occurrence date is retained; accounting effect goes to the current open period; locked entries cannot be silently changed.

### C13 — Accounting acknowledgement replay

Owner: INV-681; modules: M43, M44.

Deliver batch B, lose response, retry, receive a partial rejection, then a corrected acknowledgement.

Expected: External references and checksum prevent duplicate proposals; rejected lines stay visible; reconciliation cannot falsely show fully accepted.

### C14 — Offline lifecycle

Owner: INV-599; modules: M13, M39.

Capture a pick and count offline, kill/restart app, change document online, revoke device and reconnect with duplicate commands.

Expected: Queue survives encrypted; unacknowledged work stays pending; stale version and revoked authorization conflict; no last-write-wins or duplicate stock.

### C15 — Ownership and kits

Owner: INV-633; modules: M35, M38, M41.

Store ten vendor-owned and five owned units; sell a two-component kit with one unavailable owned component.

Expected: Vendor stock does not inflate company value or satisfy unrelated ownership demand; incomplete kit dispatch is blocked.

### C16 — Webhook security

Owner: INV-714; modules: M08, M46.

Replay signed payload, alter body, use expired timestamp, rotate secret and target private network address.

Expected: Receiver deduplicates event IDs; tamper/expired signatures and SSRF destinations fail; retries do not duplicate side effects.

### C17 — Restore and cutover

Owner: INV-790; modules: M47, M50, M51.

Rehearse migration, capture customer reconciliation, restore isolated backup and replay the approved post-backup command set.

Expected: Stock, reservations, valuations and export references reconcile; measured RPO <=15 minutes and RTO <=4 hours; no blind restoration over new live movements.

### C18 — Forecast without double counting

Owner: INV-518; modules: M21, M34.

Have 100 on hand, 30 reserved against 40 open demand and 20 confirmed future receipts.

Expected: Available is 70; forecast at receipt horizon is 80, not 50; unconfirmed suggestions do not count as supply.

### C19 — Intercompany and dropship

Owner: INV-633; modules: M36, M37, M41.

Fulfill a dropship and a linked intercompany shipment/partial receipt in distinct base currencies.

Expected: Dropship never increases warehouse on-hand; intercompany ledgers reconcile independently with snapshotted FX and buyer stock only on receipt.
