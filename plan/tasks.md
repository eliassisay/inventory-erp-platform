# Inventory ERP — Implementation tasks

> Registry baseline 1.0 · 2026-11-04 · 51 modules · 790 tasks · 156 capabilities · 13 phases. Generated; edit registry.json and run `make plan-render`.

Statuses: `[ ]` planned, `[~]` active, `[?]` verified awaiting review, `[x]` accepted/merged. At most one active task. Use `make task-status ID=INV-001 STATUS=~`; status is stored in registry.json, never copied from generated Markdown. No software task is claimed complete by this planning delivery.

## Phase 1 — Research baseline and architecture

### M01 · Product baseline and localization

- [ ] INV-001 · `ops` · `M01·AUTHZ` · Product baseline and localization: enforce access boundaries
  - Depends on: none.
  - Deliverable: Enforce roles Product owner, Compliance reviewer and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Product baseline and localization identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-002 · `ops` · `M01·LIFE` · Research baseline
  - Depends on: INV-001.
  - Deliverable: Each agreed feature has an official source or an explicit product decision and a disposition.
  - Acceptance: Each agreed feature has an official source or an explicit product decision and a disposition. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Each agreed feature has an official source or an explicit product decision and a disposition. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-003 · `ops` · `M01·LIFE` · Ethiopia localization review
  - Depends on: INV-001.
  - Deliverable: Record reviewed legal sources, applicability, reviewer, date and approval for data hosting, retention and document wording before pilot; tax invoices are excluded.
  - Acceptance: Record reviewed legal sources, applicability, reviewer, date and approval for data hosting, retention and document wording before pilot; tax invoices are excluded. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Record reviewed legal sources, applicability, reviewer, date and approval for data hosting, retention and document wording before pilot; tax invoices are excluded. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-004 · `ops` · `M01·LIFE` · Dependency and version decisions
  - Depends on: INV-001.
  - Deliverable: Verify supported versions and licenses of Node, Express, React, PostgreSQL, Flutter and chosen libraries before lockfile creation; record exact versions in an ADR.
  - Acceptance: Verify supported versions and licenses of Node, Express, React, PostgreSQL, Flutter and chosen libraries before lockfile creation; record exact versions in an ADR. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Verify supported versions and licenses of Node, Express, React, PostgreSQL, Flutter and chosen libraries before lockfile creation; record exact versions in an ADR. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-005 · `ops` · `M01·INTEGRATION` · Product baseline and localization: dependency integration
  - Depends on: INV-002, INV-003, INV-004.
  - Deliverable: Exercise Product baseline and localization with prerequisite modules none; reviewed product baseline and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-006 · `ops` · `M01·OPERABILITY` · Product baseline and localization: runbook and failure signals
  - Depends on: INV-005.
  - Deliverable: Document deployment/configuration, metrics and recovery for Product baseline and localization; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-007 · `qa` · `M01·QA` · Product baseline and localization: acceptance and invariants
  - Depends on: INV-001, INV-002, INV-003, INV-004, INV-005, INV-006.
  - Deliverable: Execute the feature acceptance suite for Product baseline and localization, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Each agreed feature has an official source or an explicit product decision and a disposition. Record reviewed legal sources, applicability, reviewer, date and approval for data hosting, retention and document wording before pilot; tax invoices are excluded. Verify supported versions and licenses of Node, Express, React, PostgreSQL, Flutter and chosen libraries before lockfile creation; record exact versions in an ADR.

## Phase 2 — SaaS foundations

### M02 · Repository and delivery tooling

- [ ] INV-008 · `backend` · `M02·AUTHZ` · Repository and delivery tooling: enforce access boundaries
  - Depends on: INV-007.
  - Deliverable: Enforce roles Engineer and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Repository and delivery tooling identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-009 · `devops` · `M02·LIFE` · Reproducible development stack
  - Depends on: INV-008, INV-007.
  - Deliverable: A clean checkout boots API, worker, web, admin and PostgreSQL through documented Make targets without production credentials.
  - Acceptance: A clean checkout boots API, worker, web, admin and PostgreSQL through documented Make targets without production credentials. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: A clean checkout boots API, worker, web, admin and PostgreSQL through documented Make targets without production credentials. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-010 · `devops` · `M02·LIFE` · CI and contract generation
  - Depends on: INV-008, INV-007.
  - Deliverable: Typechecks, lint, unit tests, API drift checks, integration tests and plan validation are separate visible CI jobs.
  - Acceptance: Typechecks, lint, unit tests, API drift checks, integration tests and plan validation are separate visible CI jobs. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Typechecks, lint, unit tests, API drift checks, integration tests and plan validation are separate visible CI jobs. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-011 · `devops` · `M02·LIFE` · Environment separation
  - Depends on: INV-008, INV-007.
  - Deliverable: Development, staging and production use separate credentials, databases, storage and notification destinations.
  - Acceptance: Development, staging and production use separate credentials, databases, storage and notification destinations. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Development, staging and production use separate credentials, databases, storage and notification destinations. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-012 · `backend` · `M02·INTEGRATION` · Repository and delivery tooling: dependency integration
  - Depends on: INV-009, INV-010, INV-011.
  - Deliverable: Exercise Repository and delivery tooling with prerequisite modules M01 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-013 · `devops` · `M02·OPERABILITY` · Repository and delivery tooling: runbook and failure signals
  - Depends on: INV-012.
  - Deliverable: Document deployment/configuration, metrics and recovery for Repository and delivery tooling; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-014 · `qa` · `M02·QA` · Repository and delivery tooling: acceptance and invariants
  - Depends on: INV-008, INV-009, INV-010, INV-011, INV-012, INV-013.
  - Deliverable: Execute the feature acceptance suite for Repository and delivery tooling, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: A clean checkout boots API, worker, web, admin and PostgreSQL through documented Make targets without production credentials. Typechecks, lint, unit tests, API drift checks, integration tests and plan validation are separate visible CI jobs. Development, staging and production use separate credentials, databases, storage and notification destinations.

### M03 · Tenants and SaaS entitlements

- [ ] INV-015 · `backend` · `M03·DATA` · Tenants and SaaS entitlements: schema and migrations
  - Depends on: INV-014.
  - Deliverable: Create scoped tables tenants, tenant_memberships, subscriptions, entitlements, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Tenants and SaaS entitlements. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-016 · `backend` · `M03·API` · Tenants and SaaS entitlements: request and response contracts
  - Depends on: INV-015.
  - Deliverable: Implement and document 8 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /tenants, POST /tenants/{id}/activate, PUT /tenants/{id}/entitlements, POST /tenants/{id}/suspend, GET /tenants, GET /tenants/{id}, GET /subscriptions, GET /subscriptions/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-017 · `backend` · `M03·AUTHZ` · Tenants and SaaS entitlements: enforce access boundaries
  - Depends on: INV-015.
  - Deliverable: Enforce roles Platform operator, Tenant admin and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Tenants and SaaS entitlements identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-018 · `backend` · `M03·LIFE` · Tenant onboarding
  - Depends on: INV-016, INV-017, INV-015.
  - Deliverable: A new customer gets isolated settings and an initial administrator; duplicate slug retry returns the original tenant.
  - Acceptance: A new customer gets isolated settings and an initial administrator; duplicate slug retry returns the original tenant. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: A new customer gets isolated settings and an initial administrator; duplicate slug retry returns the original tenant. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-019 · `backend` · `M03·LIFE` · Operator-managed plans
  - Depends on: INV-016, INV-017, INV-015.
  - Deliverable: Versioned feature and storage limits are enforced in API and worker paths; no card processing is implemented.
  - Acceptance: Versioned feature and storage limits are enforced in API and worker paths; no card processing is implemented. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Versioned feature and storage limits are enforced in API and worker paths; no card processing is implemented. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-020 · `backend` · `M03·LIFE` · Suspension and reactivation
  - Depends on: INV-016, INV-017, INV-015.
  - Deliverable: Suspended customers cannot post new stock but retain authorized export access; reactivation does not replay old commands automatically.
  - Acceptance: Suspended customers cannot post new stock but retain authorized export access; reactivation does not replay old commands automatically. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Suspended customers cannot post new stock but retain authorized export access; reactivation does not replay old commands automatically. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-021 · `design` · `M03·DESIGN` · Tenants and SaaS entitlements: screen design
  - Depends on: INV-017.
  - Deliverable: Approve S-M03-01: list/work queue, detail/history and permitted action forms for Tenants and SaaS entitlements.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M03-01.

- [ ] INV-022 · `frontend` · `M03·BUILD` · Tenants and SaaS entitlements: accessible user workflows
  - Depends on: INV-016, INV-018, INV-019, INV-020, INV-021.
  - Deliverable: Build S-M03-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Tenants and SaaS entitlements feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M03-01.

- [ ] INV-023 · `backend` · `M03·NOTIFY` · Tenants and SaaS entitlements: actionable notifications
  - Depends on: INV-018, INV-019, INV-020.
  - Deliverable: Register m03.attention and m03.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-024 · `backend` · `M03·ADMIN` · Tenants and SaaS entitlements: administrative review controls
  - Depends on: INV-022.
  - Deliverable: Provide authorized history, exception review and safe recovery for Tenants and SaaS entitlements using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-025 · `backend` · `M03·AUDIT` · Tenants and SaaS entitlements: mutation evidence
  - Depends on: INV-018, INV-019, INV-020.
  - Deliverable: Declare audit actions for Tenant onboarding, Operator-managed plans, Suspension and reactivation; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-026 · `backend` · `M03·EVENTS` · Tenants and SaaS entitlements: versioned domain events
  - Depends on: INV-018, INV-019, INV-020.
  - Deliverable: Publish m03.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-027 · `backend` · `M03·PRIVACY` · Tenants and SaaS entitlements: data classification and retention
  - Depends on: INV-018, INV-019, INV-020.
  - Deliverable: Classify all fields in tenants, tenant_memberships, subscriptions, entitlements; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-028 · `backend` · `M03·INTEGRATION` · Tenants and SaaS entitlements: dependency integration
  - Depends on: INV-018, INV-019, INV-020, INV-016.
  - Deliverable: Exercise Tenants and SaaS entitlements with prerequisite modules M02 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-029 · `devops` · `M03·OPERABILITY` · Tenants and SaaS entitlements: runbook and failure signals
  - Depends on: INV-028.
  - Deliverable: Document deployment/configuration, metrics and recovery for Tenants and SaaS entitlements; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-030 · `qa` · `M03·QA` · Tenants and SaaS entitlements: acceptance and invariants
  - Depends on: INV-015, INV-016, INV-017, INV-018, INV-019, INV-020, INV-021, INV-022, INV-023, INV-024, INV-025, INV-026, INV-027, INV-028, INV-029.
  - Deliverable: Execute the feature acceptance suite for Tenants and SaaS entitlements, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: A new customer gets isolated settings and an initial administrator; duplicate slug retry returns the original tenant. Versioned feature and storage limits are enforced in API and worker paths; no card processing is implemented. Suspended customers cannot post new stock but retain authorized export access; reactivation does not replay old commands automatically.

### M04 · Identity, invitations and devices

- [ ] INV-031 · `backend` · `M04·DATA` · Identity, invitations and devices: schema and migrations
  - Depends on: INV-030.
  - Deliverable: Create scoped tables users, invitations, device_sessions, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Identity, invitations and devices. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-032 · `backend` · `M04·API` · Identity, invitations and devices: request and response contracts
  - Depends on: INV-031.
  - Deliverable: Implement and document 14 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /invitations, POST /invitations/accept, POST /auth/mfa/enroll, POST /auth/mfa/verify, DELETE /devices/{id}/session, GET /invitations, GET /invitations/{id}, GET /devices, GET /devices/{id}, POST /auth/sign-in, POST /auth/sign-out, GET /auth/session, POST /auth/password-reset/request, POST /auth/password-reset/confirm. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-033 · `backend` · `M04·AUTHZ` · Identity, invitations and devices: enforce access boundaries
  - Depends on: INV-031.
  - Deliverable: Enforce roles Tenant admin, Warehouse operator and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Identity, invitations and devices identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-034 · `backend` · `M04·LIFE` · Invite and recovery
  - Depends on: INV-032, INV-033, INV-031.
  - Deliverable: Invitation and password-reset tokens are single-use, expire and cannot change tenant scope.
  - Acceptance: Invitation and password-reset tokens are single-use, expire and cannot change tenant scope. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Invitation and password-reset tokens are single-use, expire and cannot change tenant scope. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-035 · `backend` · `M04·LIFE` · MFA and sessions
  - Depends on: INV-032, INV-033, INV-031.
  - Deliverable: MFA is mandatory for platform and tenant administrators; recovery codes are hashed, single-use and audited.
  - Acceptance: MFA is mandatory for platform and tenant administrators; recovery codes are hashed, single-use and audited. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: MFA is mandatory for platform and tenant administrators; recovery codes are hashed, single-use and audited. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-036 · `backend` · `M04·LIFE` · Device revocation
  - Depends on: INV-032, INV-033, INV-031.
  - Deliverable: A revoked Android device loses sync access immediately online; local unlock expires within 24 hours offline and queued work requires renewed authorization.
  - Acceptance: A revoked Android device loses sync access immediately online; local unlock expires within 24 hours offline and queued work requires renewed authorization. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: A revoked Android device loses sync access immediately online; local unlock expires within 24 hours offline and queued work requires renewed authorization. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-037 · `design` · `M04·DESIGN` · Identity, invitations and devices: screen design
  - Depends on: INV-033.
  - Deliverable: Approve S-M04-01: list/work queue, detail/history and permitted action forms for Identity, invitations and devices.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M04-01.

- [ ] INV-038 · `frontend` · `M04·BUILD` · Identity, invitations and devices: accessible user workflows
  - Depends on: INV-032, INV-034, INV-035, INV-036, INV-037.
  - Deliverable: Build S-M04-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Identity, invitations and devices feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M04-01.

- [ ] INV-039 · `backend` · `M04·NOTIFY` · Identity, invitations and devices: actionable notifications
  - Depends on: INV-034, INV-035, INV-036.
  - Deliverable: Register m04.attention and m04.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-040 · `backend` · `M04·ADMIN` · Identity, invitations and devices: administrative review controls
  - Depends on: INV-038.
  - Deliverable: Provide authorized history, exception review and safe recovery for Identity, invitations and devices using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-041 · `backend` · `M04·AUDIT` · Identity, invitations and devices: mutation evidence
  - Depends on: INV-034, INV-035, INV-036.
  - Deliverable: Declare audit actions for Invite and recovery, MFA and sessions, Device revocation; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-042 · `backend` · `M04·EVENTS` · Identity, invitations and devices: versioned domain events
  - Depends on: INV-034, INV-035, INV-036.
  - Deliverable: Publish m04.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-043 · `backend` · `M04·PRIVACY` · Identity, invitations and devices: data classification and retention
  - Depends on: INV-034, INV-035, INV-036.
  - Deliverable: Classify all fields in users, invitations, device_sessions; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-044 · `backend` · `M04·INTEGRATION` · Identity, invitations and devices: dependency integration
  - Depends on: INV-034, INV-035, INV-036, INV-032.
  - Deliverable: Exercise Identity, invitations and devices with prerequisite modules M03 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-045 · `devops` · `M04·OPERABILITY` · Identity, invitations and devices: runbook and failure signals
  - Depends on: INV-044.
  - Deliverable: Document deployment/configuration, metrics and recovery for Identity, invitations and devices; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-046 · `qa` · `M04·QA` · Identity, invitations and devices: acceptance and invariants
  - Depends on: INV-031, INV-032, INV-033, INV-034, INV-035, INV-036, INV-037, INV-038, INV-039, INV-040, INV-041, INV-042, INV-043, INV-044, INV-045.
  - Deliverable: Execute the feature acceptance suite for Identity, invitations and devices, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Invitation and password-reset tokens are single-use, expire and cannot change tenant scope. MFA is mandatory for platform and tenant administrators; recovery codes are hashed, single-use and audited. A revoked Android device loses sync access immediately online; local unlock expires within 24 hours offline and queued work requires renewed authorization.

### M05 · Scoped roles and permissions

- [ ] INV-047 · `backend` · `M05·DATA` · Scoped roles and permissions: schema and migrations
  - Depends on: INV-046.
  - Deliverable: Create scoped tables roles, permissions, role_permissions, role_bindings, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Scoped roles and permissions. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-048 · `backend` · `M05·API` · Scoped roles and permissions: request and response contracts
  - Depends on: INV-047.
  - Deliverable: Implement and document 8 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: GET /permissions, POST /roles, PUT /roles/{id}/permissions, POST /role-bindings, GET /roles, GET /roles/{id}, GET /role-bindings, GET /role-bindings/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-049 · `backend` · `M05·AUTHZ` · Scoped roles and permissions: enforce access boundaries
  - Depends on: INV-047.
  - Deliverable: Enforce roles Tenant admin and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Scoped roles and permissions identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-050 · `backend` · `M05·LIFE` · Permission catalog
  - Depends on: INV-048, INV-049, INV-047.
  - Deliverable: Each action has a declared permission; default roles and custom roles use the same authorization path.
  - Acceptance: Each action has a declared permission; default roles and custom roles use the same authorization path. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Each action has a declared permission; default roles and custom roles use the same authorization path. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-051 · `backend` · `M05·LIFE` · Tenant company warehouse boundaries
  - Depends on: INV-048, INV-049, INV-047.
  - Deliverable: Grants union only within their authorized scopes; foreign tenant IDs and warehouse IDs are denied even when object UUIDs are known.
  - Acceptance: Grants union only within their authorized scopes; foreign tenant IDs and warehouse IDs are denied even when object UUIDs are known. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Grants union only within their authorized scopes; foreign tenant IDs and warehouse IDs are denied even when object UUIDs are known. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-052 · `backend` · `M05·LIFE` · Support access
  - Depends on: INV-048, INV-049, INV-047.
  - Deliverable: Time-limited customer-approved support sessions are read-only by default and separately audited; platform staff never inherit unrestricted warehouse access.
  - Acceptance: Time-limited customer-approved support sessions are read-only by default and separately audited; platform staff never inherit unrestricted warehouse access. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Time-limited customer-approved support sessions are read-only by default and separately audited; platform staff never inherit unrestricted warehouse access. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-053 · `design` · `M05·DESIGN` · Scoped roles and permissions: screen design
  - Depends on: INV-049.
  - Deliverable: Approve S-M05-01: list/work queue, detail/history and permitted action forms for Scoped roles and permissions.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M05-01.

- [ ] INV-054 · `frontend` · `M05·BUILD` · Scoped roles and permissions: accessible user workflows
  - Depends on: INV-048, INV-050, INV-051, INV-052, INV-053.
  - Deliverable: Build S-M05-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Scoped roles and permissions feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M05-01.

- [ ] INV-055 · `backend` · `M05·NOTIFY` · Scoped roles and permissions: actionable notifications
  - Depends on: INV-050, INV-051, INV-052.
  - Deliverable: Register m05.attention and m05.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-056 · `backend` · `M05·ADMIN` · Scoped roles and permissions: administrative review controls
  - Depends on: INV-054.
  - Deliverable: Provide authorized history, exception review and safe recovery for Scoped roles and permissions using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-057 · `backend` · `M05·AUDIT` · Scoped roles and permissions: mutation evidence
  - Depends on: INV-050, INV-051, INV-052.
  - Deliverable: Declare audit actions for Permission catalog, Tenant company warehouse boundaries, Support access; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-058 · `backend` · `M05·EVENTS` · Scoped roles and permissions: versioned domain events
  - Depends on: INV-050, INV-051, INV-052.
  - Deliverable: Publish m05.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-059 · `backend` · `M05·PRIVACY` · Scoped roles and permissions: data classification and retention
  - Depends on: INV-050, INV-051, INV-052.
  - Deliverable: Classify all fields in roles, permissions, role_permissions, role_bindings; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-060 · `backend` · `M05·INTEGRATION` · Scoped roles and permissions: dependency integration
  - Depends on: INV-050, INV-051, INV-052, INV-048.
  - Deliverable: Exercise Scoped roles and permissions with prerequisite modules M04 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-061 · `devops` · `M05·OPERABILITY` · Scoped roles and permissions: runbook and failure signals
  - Depends on: INV-060.
  - Deliverable: Document deployment/configuration, metrics and recovery for Scoped roles and permissions; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-062 · `qa` · `M05·QA` · Scoped roles and permissions: acceptance and invariants
  - Depends on: INV-047, INV-048, INV-049, INV-050, INV-051, INV-052, INV-053, INV-054, INV-055, INV-056, INV-057, INV-058, INV-059, INV-060, INV-061.
  - Deliverable: Execute the feature acceptance suite for Scoped roles and permissions, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Each action has a declared permission; default roles and custom roles use the same authorization path. Grants union only within their authorized scopes; foreign tenant IDs and warehouse IDs are denied even when object UUIDs are known. Time-limited customer-approved support sessions are read-only by default and separately audited; platform staff never inherit unrestricted warehouse access.

### M06 · Approval policies and decisions

- [ ] INV-063 · `backend` · `M06·DATA` · Approval policies and decisions: schema and migrations
  - Depends on: INV-062.
  - Deliverable: Create scoped tables approval_policies, approval_instances, approval_decisions, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Approval policies and decisions. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-064 · `backend` · `M06·API` · Approval policies and decisions: request and response contracts
  - Depends on: INV-063.
  - Deliverable: Implement and document 6 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /approval-policies, POST /approvals/{id}/decisions, GET /approvals, GET /approval-policies, GET /approval-policies/{id}, GET /approvals/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-065 · `backend` · `M06·AUTHZ` · Approval policies and decisions: enforce access boundaries
  - Depends on: INV-063.
  - Deliverable: Enforce roles Tenant admin, Approver and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Approval policies and decisions identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-066 · `backend` · `M06·LIFE` · Policy routing
  - Depends on: INV-064, INV-065, INV-063.
  - Deliverable: Company and warehouse policies resolve deterministically using most-specific scope then amount threshold; missing approver configuration blocks submission.
  - Acceptance: Company and warehouse policies resolve deterministically using most-specific scope then amount threshold; missing approver configuration blocks submission. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Company and warehouse policies resolve deterministically using most-specific scope then amount threshold; missing approver configuration blocks submission. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-067 · `backend` · `M06·LIFE` · Separation of duties
  - Depends on: INV-064, INV-065, INV-063.
  - Deliverable: Requesters cannot approve their own adjustment, PO, scrap, period close or intercompany transaction.
  - Acceptance: Requesters cannot approve their own adjustment, PO, scrap, period close or intercompany transaction. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Requesters cannot approve their own adjustment, PO, scrap, period close or intercompany transaction. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-068 · `backend` · `M06·LIFE` · Approval versioning
  - Depends on: INV-064, INV-065, INV-063.
  - Deliverable: Submission snapshots policy and document version; editing an approved document requires a new revision and approval.
  - Acceptance: Submission snapshots policy and document version; editing an approved document requires a new revision and approval. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Submission snapshots policy and document version; editing an approved document requires a new revision and approval. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-069 · `design` · `M06·DESIGN` · Approval policies and decisions: screen design
  - Depends on: INV-065.
  - Deliverable: Approve S-M06-01: list/work queue, detail/history and permitted action forms for Approval policies and decisions.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M06-01.

- [ ] INV-070 · `frontend` · `M06·BUILD` · Approval policies and decisions: accessible user workflows
  - Depends on: INV-064, INV-066, INV-067, INV-068, INV-069.
  - Deliverable: Build S-M06-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Approval policies and decisions feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M06-01.

- [ ] INV-071 · `backend` · `M06·NOTIFY` · Approval policies and decisions: actionable notifications
  - Depends on: INV-066, INV-067, INV-068.
  - Deliverable: Register m06.attention and m06.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-072 · `backend` · `M06·ADMIN` · Approval policies and decisions: administrative review controls
  - Depends on: INV-070.
  - Deliverable: Provide authorized history, exception review and safe recovery for Approval policies and decisions using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-073 · `backend` · `M06·AUDIT` · Approval policies and decisions: mutation evidence
  - Depends on: INV-066, INV-067, INV-068.
  - Deliverable: Declare audit actions for Policy routing, Separation of duties, Approval versioning; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-074 · `backend` · `M06·EVENTS` · Approval policies and decisions: versioned domain events
  - Depends on: INV-066, INV-067, INV-068.
  - Deliverable: Publish m06.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-075 · `backend` · `M06·PRIVACY` · Approval policies and decisions: data classification and retention
  - Depends on: INV-066, INV-067, INV-068.
  - Deliverable: Classify all fields in approval_policies, approval_instances, approval_decisions; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-076 · `backend` · `M06·INTEGRATION` · Approval policies and decisions: dependency integration
  - Depends on: INV-066, INV-067, INV-068, INV-064.
  - Deliverable: Exercise Approval policies and decisions with prerequisite modules M05 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-077 · `devops` · `M06·OPERABILITY` · Approval policies and decisions: runbook and failure signals
  - Depends on: INV-076.
  - Deliverable: Document deployment/configuration, metrics and recovery for Approval policies and decisions; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-078 · `qa` · `M06·QA` · Approval policies and decisions: acceptance and invariants
  - Depends on: INV-063, INV-064, INV-065, INV-066, INV-067, INV-068, INV-069, INV-070, INV-071, INV-072, INV-073, INV-074, INV-075, INV-076, INV-077.
  - Deliverable: Execute the feature acceptance suite for Approval policies and decisions, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Company and warehouse policies resolve deterministically using most-specific scope then amount threshold; missing approver configuration blocks submission. Requesters cannot approve their own adjustment, PO, scrap, period close or intercompany transaction. Submission snapshots policy and document version; editing an approved document requires a new revision and approval.

### M07 · Audit and business events

- [ ] INV-079 · `backend` · `M07·DATA` · Audit and business events: schema and migrations
  - Depends on: INV-062.
  - Deliverable: Create scoped tables audit_records, outbox_events, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Audit and business events. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-080 · `backend` · `M07·API` · Audit and business events: request and response contracts
  - Depends on: INV-079.
  - Deliverable: Implement and document 3 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: GET /audit-records, GET /events/{id}, GET /audit-records/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-081 · `backend` · `M07·AUTHZ` · Audit and business events: enforce access boundaries
  - Depends on: INV-079.
  - Deliverable: Enforce roles Auditor, Platform operator and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Audit and business events identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-082 · `backend` · `M07·LIFE` · Transactional audit
  - Depends on: INV-080, INV-081, INV-079.
  - Deliverable: Every sensitive mutation writes its audit and outbox record in the same database transaction or fully rolls back.
  - Acceptance: Every sensitive mutation writes its audit and outbox record in the same database transaction or fully rolls back. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Every sensitive mutation writes its audit and outbox record in the same database transaction or fully rolls back. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-083 · `backend` · `M07·LIFE` · Append-only evidence
  - Depends on: INV-080, INV-081, INV-079.
  - Deliverable: Application roles cannot edit or delete audit records; corrections reference the original action.
  - Acceptance: Application roles cannot edit or delete audit records; corrections reference the original action. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Application roles cannot edit or delete audit records; corrections reference the original action. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-084 · `backend` · `M07·LIFE` · Event privacy
  - Depends on: INV-080, INV-081, INV-079.
  - Deliverable: Event payloads contain scoped identifiers and necessary facts only; secrets and contact data are excluded from analytics.
  - Acceptance: Event payloads contain scoped identifiers and necessary facts only; secrets and contact data are excluded from analytics. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Event payloads contain scoped identifiers and necessary facts only; secrets and contact data are excluded from analytics. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-085 · `design` · `M07·DESIGN` · Audit and business events: screen design
  - Depends on: INV-081.
  - Deliverable: Approve S-M07-01: list/work queue, detail/history and permitted action forms for Audit and business events.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M07-01.

- [ ] INV-086 · `frontend` · `M07·BUILD` · Audit and business events: accessible user workflows
  - Depends on: INV-080, INV-082, INV-083, INV-084, INV-085.
  - Deliverable: Build S-M07-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Audit and business events feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M07-01.

- [ ] INV-087 · `backend` · `M07·NOTIFY` · Audit and business events: actionable notifications
  - Depends on: INV-082, INV-083, INV-084.
  - Deliverable: Register m07.attention and m07.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-088 · `backend` · `M07·ADMIN` · Audit and business events: administrative review controls
  - Depends on: INV-086.
  - Deliverable: Provide authorized history, exception review and safe recovery for Audit and business events using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-089 · `backend` · `M07·AUDIT` · Audit and business events: mutation evidence
  - Depends on: INV-082, INV-083, INV-084.
  - Deliverable: Declare audit actions for Transactional audit, Append-only evidence, Event privacy; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-090 · `backend` · `M07·EVENTS` · Audit and business events: versioned domain events
  - Depends on: INV-082, INV-083, INV-084.
  - Deliverable: Publish m07.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-091 · `backend` · `M07·PRIVACY` · Audit and business events: data classification and retention
  - Depends on: INV-082, INV-083, INV-084.
  - Deliverable: Classify all fields in audit_records, outbox_events; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-092 · `backend` · `M07·INTEGRATION` · Audit and business events: dependency integration
  - Depends on: INV-082, INV-083, INV-084, INV-080.
  - Deliverable: Exercise Audit and business events with prerequisite modules M05 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-093 · `devops` · `M07·OPERABILITY` · Audit and business events: runbook and failure signals
  - Depends on: INV-092.
  - Deliverable: Document deployment/configuration, metrics and recovery for Audit and business events; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-094 · `qa` · `M07·QA` · Audit and business events: acceptance and invariants
  - Depends on: INV-079, INV-080, INV-081, INV-082, INV-083, INV-084, INV-085, INV-086, INV-087, INV-088, INV-089, INV-090, INV-091, INV-092, INV-093.
  - Deliverable: Execute the feature acceptance suite for Audit and business events, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Every sensitive mutation writes its audit and outbox record in the same database transaction or fully rolls back. Application roles cannot edit or delete audit records; corrections reference the original action. Event payloads contain scoped identifiers and necessary facts only; secrets and contact data are excluded from analytics.

### M08 · Jobs, idempotency and delivery

- [ ] INV-095 · `backend` · `M08·DATA` · Jobs, idempotency and delivery: schema and migrations
  - Depends on: INV-094.
  - Deliverable: Create scoped tables command_receipts, job_attempts, dead_letters, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Jobs, idempotency and delivery. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-096 · `backend` · `M08·API` · Jobs, idempotency and delivery: request and response contracts
  - Depends on: INV-095.
  - Deliverable: Implement and document 3 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: GET /jobs, POST /jobs/{id}/retry, GET /jobs/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-097 · `backend` · `M08·AUTHZ` · Jobs, idempotency and delivery: enforce access boundaries
  - Depends on: INV-095.
  - Deliverable: Enforce roles Platform operator and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Jobs, idempotency and delivery identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-098 · `backend` · `M08·LIFE` · Idempotent commands
  - Depends on: INV-096, INV-097, INV-095.
  - Deliverable: Same key and same payload return the original committed result; same key with different payload returns 409.
  - Acceptance: Same key and same payload return the original committed result; same key with different payload returns 409. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Same key and same payload return the original committed result; same key with different payload returns 409. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-099 · `backend` · `M08·LIFE` · Outbox processing
  - Depends on: INV-096, INV-097, INV-095.
  - Deliverable: Worker crash before or after delivery never duplicates downstream postings; consumers deduplicate by event ID.
  - Acceptance: Worker crash before or after delivery never duplicates downstream postings; consumers deduplicate by event ID. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Worker crash before or after delivery never duplicates downstream postings; consumers deduplicate by event ID. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-100 · `backend` · `M08·LIFE` · Retries and dead letters
  - Depends on: INV-096, INV-097, INV-095.
  - Deliverable: Exponential retry with jitter stops after eight attempts and raises an actionable dead-letter alert; manual replay retains the original correlation ID.
  - Acceptance: Exponential retry with jitter stops after eight attempts and raises an actionable dead-letter alert; manual replay retains the original correlation ID. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Exponential retry with jitter stops after eight attempts and raises an actionable dead-letter alert; manual replay retains the original correlation ID. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-101 · `design` · `M08·DESIGN` · Jobs, idempotency and delivery: screen design
  - Depends on: INV-097.
  - Deliverable: Approve S-M08-01: list/work queue, detail/history and permitted action forms for Jobs, idempotency and delivery.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M08-01.

- [ ] INV-102 · `frontend` · `M08·BUILD` · Jobs, idempotency and delivery: accessible user workflows
  - Depends on: INV-096, INV-098, INV-099, INV-100, INV-101.
  - Deliverable: Build S-M08-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Jobs, idempotency and delivery feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M08-01.

- [ ] INV-103 · `backend` · `M08·NOTIFY` · Jobs, idempotency and delivery: actionable notifications
  - Depends on: INV-098, INV-099, INV-100.
  - Deliverable: Register m08.attention and m08.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-104 · `backend` · `M08·ADMIN` · Jobs, idempotency and delivery: administrative review controls
  - Depends on: INV-102.
  - Deliverable: Provide authorized history, exception review and safe recovery for Jobs, idempotency and delivery using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-105 · `backend` · `M08·AUDIT` · Jobs, idempotency and delivery: mutation evidence
  - Depends on: INV-098, INV-099, INV-100.
  - Deliverable: Declare audit actions for Idempotent commands, Outbox processing, Retries and dead letters; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-106 · `backend` · `M08·EVENTS` · Jobs, idempotency and delivery: versioned domain events
  - Depends on: INV-098, INV-099, INV-100.
  - Deliverable: Publish m08.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-107 · `backend` · `M08·PRIVACY` · Jobs, idempotency and delivery: data classification and retention
  - Depends on: INV-098, INV-099, INV-100.
  - Deliverable: Classify all fields in command_receipts, job_attempts, dead_letters; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-108 · `backend` · `M08·INTEGRATION` · Jobs, idempotency and delivery: dependency integration
  - Depends on: INV-098, INV-099, INV-100, INV-096.
  - Deliverable: Exercise Jobs, idempotency and delivery with prerequisite modules M07 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-109 · `devops` · `M08·OPERABILITY` · Jobs, idempotency and delivery: runbook and failure signals
  - Depends on: INV-108.
  - Deliverable: Document deployment/configuration, metrics and recovery for Jobs, idempotency and delivery; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-110 · `qa` · `M08·QA` · Jobs, idempotency and delivery: acceptance and invariants
  - Depends on: INV-095, INV-096, INV-097, INV-098, INV-099, INV-100, INV-101, INV-102, INV-103, INV-104, INV-105, INV-106, INV-107, INV-108, INV-109.
  - Deliverable: Execute the feature acceptance suite for Jobs, idempotency and delivery, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Same key and same payload return the original committed result; same key with different payload returns 409. Worker crash before or after delivery never duplicates downstream postings; consumers deduplicate by event ID. Exponential retry with jitter stops after eight attempts and raises an actionable dead-letter alert; manual replay retains the original correlation ID.

### M09 · Attachments and collaboration

- [ ] INV-111 · `backend` · `M09·DATA` · Attachments and collaboration: schema and migrations
  - Depends on: INV-062, INV-094.
  - Deliverable: Create scoped tables attachments, comments, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Attachments and collaboration. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-112 · `backend` · `M09·API` · Attachments and collaboration: request and response contracts
  - Depends on: INV-111.
  - Deliverable: Implement and document 8 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /attachments/upload-tickets, POST /attachments/{id}/finalize, GET /attachments/{id}/download, POST /comments, GET /attachments, GET /attachments/{id}, GET /comments, GET /comments/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-113 · `backend` · `M09·AUTHZ` · Attachments and collaboration: enforce access boundaries
  - Depends on: INV-111.
  - Deliverable: Enforce roles Buyer, Sales clerk, Warehouse supervisor and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Attachments and collaboration identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-114 · `backend` · `M09·LIFE` · Private attachments
  - Depends on: INV-112, INV-113, INV-111.
  - Deliverable: Upload size and MIME limits, malware quarantine and entity authorization apply before a file becomes downloadable.
  - Acceptance: Upload size and MIME limits, malware quarantine and entity authorization apply before a file becomes downloadable. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Upload size and MIME limits, malware quarantine and entity authorization apply before a file becomes downloadable. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-115 · `backend` · `M09·LIFE` · Comments and evidence
  - Depends on: INV-112, INV-113, INV-111.
  - Deliverable: Scoped comments and attachments remain linked to business documents after archival; personal data export and retention rules apply.
  - Acceptance: Scoped comments and attachments remain linked to business documents after archival; personal data export and retention rules apply. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Scoped comments and attachments remain linked to business documents after archival; personal data export and retention rules apply. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-116 · `design` · `M09·DESIGN` · Attachments and collaboration: screen design
  - Depends on: INV-113.
  - Deliverable: Approve S-M09-01: list/work queue, detail/history and permitted action forms for Attachments and collaboration.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M09-01.

- [ ] INV-117 · `frontend` · `M09·BUILD` · Attachments and collaboration: accessible user workflows
  - Depends on: INV-112, INV-114, INV-115, INV-116.
  - Deliverable: Build S-M09-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Attachments and collaboration feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M09-01.

- [ ] INV-118 · `backend` · `M09·NOTIFY` · Attachments and collaboration: actionable notifications
  - Depends on: INV-114, INV-115.
  - Deliverable: Register m09.attention and m09.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-119 · `backend` · `M09·ADMIN` · Attachments and collaboration: administrative review controls
  - Depends on: INV-117.
  - Deliverable: Provide authorized history, exception review and safe recovery for Attachments and collaboration using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-120 · `backend` · `M09·AUDIT` · Attachments and collaboration: mutation evidence
  - Depends on: INV-114, INV-115.
  - Deliverable: Declare audit actions for Private attachments, Comments and evidence; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-121 · `backend` · `M09·EVENTS` · Attachments and collaboration: versioned domain events
  - Depends on: INV-114, INV-115.
  - Deliverable: Publish m09.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-122 · `backend` · `M09·PRIVACY` · Attachments and collaboration: data classification and retention
  - Depends on: INV-114, INV-115.
  - Deliverable: Classify all fields in attachments, comments; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-123 · `backend` · `M09·INTEGRATION` · Attachments and collaboration: dependency integration
  - Depends on: INV-114, INV-115, INV-112.
  - Deliverable: Exercise Attachments and collaboration with prerequisite modules M05, M07 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-124 · `devops` · `M09·OPERABILITY` · Attachments and collaboration: runbook and failure signals
  - Depends on: INV-123.
  - Deliverable: Document deployment/configuration, metrics and recovery for Attachments and collaboration; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-125 · `qa` · `M09·QA` · Attachments and collaboration: acceptance and invariants
  - Depends on: INV-111, INV-112, INV-113, INV-114, INV-115, INV-116, INV-117, INV-118, INV-119, INV-120, INV-121, INV-122, INV-123, INV-124.
  - Deliverable: Execute the feature acceptance suite for Attachments and collaboration, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 2 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Upload size and MIME limits, malware quarantine and entity authorization apply before a file becomes downloadable. Scoped comments and attachments remain linked to business documents after archival; personal data export and retention rules apply.

### M10 · Notifications and preferences

- [ ] INV-126 · `backend` · `M10·DATA` · Notifications and preferences: schema and migrations
  - Depends on: INV-110.
  - Deliverable: Create scoped tables notification_preferences, notifications, notification_deliveries, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Notifications and preferences. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-127 · `backend` · `M10·API` · Notifications and preferences: request and response contracts
  - Depends on: INV-126.
  - Deliverable: Implement and document 4 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: GET /notifications, PATCH /notification-preferences, POST /notifications/{id}/read, GET /notifications/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-128 · `backend` · `M10·AUTHZ` · Notifications and preferences: enforce access boundaries
  - Depends on: INV-126.
  - Deliverable: Enforce roles Tenant admin, All staff and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Notifications and preferences identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-129 · `backend` · `M10·LIFE` · Notification routing
  - Depends on: INV-127, INV-128, INV-126.
  - Deliverable: Approval, shortage, expiry, recall and sync-conflict events target authorized recipients only.
  - Acceptance: Approval, shortage, expiry, recall and sync-conflict events target authorized recipients only. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Approval, shortage, expiry, recall and sync-conflict events target authorized recipients only. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-130 · `backend` · `M10·LIFE` · Delivery and preferences
  - Depends on: INV-127, INV-128, INV-126.
  - Deliverable: In-app and email notifications deduplicate by recipient and event; transactional security notices cannot be disabled.
  - Acceptance: In-app and email notifications deduplicate by recipient and event; transactional security notices cannot be disabled. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: In-app and email notifications deduplicate by recipient and event; transactional security notices cannot be disabled. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-131 · `design` · `M10·DESIGN` · Notifications and preferences: screen design
  - Depends on: INV-128.
  - Deliverable: Approve S-M10-01: list/work queue, detail/history and permitted action forms for Notifications and preferences.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M10-01.

- [ ] INV-132 · `frontend` · `M10·BUILD` · Notifications and preferences: accessible user workflows
  - Depends on: INV-127, INV-129, INV-130, INV-131.
  - Deliverable: Build S-M10-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Notifications and preferences feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M10-01.

- [ ] INV-133 · `backend` · `M10·NOTIFY` · Notifications and preferences: actionable notifications
  - Depends on: INV-129, INV-130.
  - Deliverable: Register m10.attention and m10.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-134 · `backend` · `M10·ADMIN` · Notifications and preferences: administrative review controls
  - Depends on: INV-132.
  - Deliverable: Provide authorized history, exception review and safe recovery for Notifications and preferences using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-135 · `backend` · `M10·AUDIT` · Notifications and preferences: mutation evidence
  - Depends on: INV-129, INV-130.
  - Deliverable: Declare audit actions for Notification routing, Delivery and preferences; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-136 · `backend` · `M10·EVENTS` · Notifications and preferences: versioned domain events
  - Depends on: INV-129, INV-130.
  - Deliverable: Publish m10.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-137 · `backend` · `M10·PRIVACY` · Notifications and preferences: data classification and retention
  - Depends on: INV-129, INV-130.
  - Deliverable: Classify all fields in notification_preferences, notifications, notification_deliveries; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-138 · `backend` · `M10·INTEGRATION` · Notifications and preferences: dependency integration
  - Depends on: INV-129, INV-130, INV-127.
  - Deliverable: Exercise Notifications and preferences with prerequisite modules M08 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-139 · `devops` · `M10·OPERABILITY` · Notifications and preferences: runbook and failure signals
  - Depends on: INV-138.
  - Deliverable: Document deployment/configuration, metrics and recovery for Notifications and preferences; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-140 · `qa` · `M10·QA` · Notifications and preferences: acceptance and invariants
  - Depends on: INV-126, INV-127, INV-128, INV-129, INV-130, INV-131, INV-132, INV-133, INV-134, INV-135, INV-136, INV-137, INV-138, INV-139.
  - Deliverable: Execute the feature acceptance suite for Notifications and preferences, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 2 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Approval, shortage, expiry, recall and sync-conflict events target authorized recipients only. In-app and email notifications deduplicate by recipient and event; transactional security notices cannot be disabled.

## Phase 3 — Design system and application shells

### M11 · Design system and accessibility

- [ ] INV-141 · `backend` · `M11·AUTHZ` · Design system and accessibility: enforce access boundaries
  - Depends on: INV-014.
  - Deliverable: Enforce roles Designer and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Design system and accessibility identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-142 · `frontend` · `M11·LIFE` · Accessible visual system
  - Depends on: INV-141, INV-014.
  - Deliverable: Shared typography, spacing, color, forms and tables cover light/dark themes, keyboard navigation and WCAG 2.2 AA acceptance checks.
  - Acceptance: Shared typography, spacing, color, forms and tables cover light/dark themes, keyboard navigation and WCAG 2.2 AA acceptance checks. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Shared typography, spacing, color, forms and tables cover light/dark themes, keyboard navigation and WCAG 2.2 AA acceptance checks. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-143 · `frontend` · `M11·LIFE` · Screen state contracts
  - Depends on: INV-141, INV-014.
  - Deliverable: Every screen defines loading, empty, permission-denied, error, offline and lifecycle states across 375/768/1280/1920/2560 widths.
  - Acceptance: Every screen defines loading, empty, permission-denied, error, offline and lifecycle states across 375/768/1280/1920/2560 widths. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Every screen defines loading, empty, permission-denied, error, offline and lifecycle states across 375/768/1280/1920/2560 widths. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-144 · `backend` · `M11·INTEGRATION` · Design system and accessibility: dependency integration
  - Depends on: INV-142, INV-143.
  - Deliverable: Exercise Design system and accessibility with prerequisite modules M02 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-145 · `devops` · `M11·OPERABILITY` · Design system and accessibility: runbook and failure signals
  - Depends on: INV-144.
  - Deliverable: Document deployment/configuration, metrics and recovery for Design system and accessibility; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-146 · `qa` · `M11·QA` · Design system and accessibility: acceptance and invariants
  - Depends on: INV-141, INV-142, INV-143, INV-144, INV-145.
  - Deliverable: Execute the feature acceptance suite for Design system and accessibility, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 2 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Shared typography, spacing, color, forms and tables cover light/dark themes, keyboard navigation and WCAG 2.2 AA acceptance checks. Every screen defines loading, empty, permission-denied, error, offline and lifecycle states across 375/768/1280/1920/2560 widths.

### M12 · Office and admin application shells

- [ ] INV-147 · `backend` · `M12·DATA` · Office and admin application shells: schema and migrations
  - Depends on: INV-030, INV-046, INV-062, INV-140, INV-146.
  - Deliverable: Create scoped tables saved_views, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Office and admin application shells. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-148 · `backend` · `M12·API` · Office and admin application shells: request and response contracts
  - Depends on: INV-147.
  - Deliverable: Implement and document 6 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: GET /me/context, PATCH /me/preferences, GET /saved-views, GET /saved-views/{id}, POST /saved-views, DELETE /saved-views/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-149 · `backend` · `M12·AUTHZ` · Office and admin application shells: enforce access boundaries
  - Depends on: INV-147.
  - Deliverable: Enforce roles All staff, Platform operator and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Office and admin application shells identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-150 · `backend` · `M12·LIFE` · Office context switching
  - Depends on: INV-148, INV-149, INV-147.
  - Deliverable: Company and warehouse context is visible on every operational screen; switching clears stale query caches and unsaved work is confirmed.
  - Acceptance: Company and warehouse context is visible on every operational screen; switching clears stale query caches and unsaved work is confirmed. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Company and warehouse context is visible on every operational screen; switching clears stale query caches and unsaved work is confirmed. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-151 · `backend` · `M12·LIFE` · Platform admin separation
  - Depends on: INV-148, INV-149, INV-147.
  - Deliverable: Tenant administration and platform support use separate navigation and permissions; bundles are not the security boundary.
  - Acceptance: Tenant administration and platform support use separate navigation and permissions; bundles are not the security boundary. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Tenant administration and platform support use separate navigation and permissions; bundles are not the security boundary. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-152 · `backend` · `M12·LIFE` · Search and navigation
  - Depends on: INV-148, INV-149, INV-147.
  - Deliverable: Keyboard search uses authorized results and preserves tenant/company context in deep links.
  - Acceptance: Keyboard search uses authorized results and preserves tenant/company context in deep links. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Keyboard search uses authorized results and preserves tenant/company context in deep links. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-153 · `design` · `M12·DESIGN` · Office and admin application shells: screen design
  - Depends on: INV-149, INV-146.
  - Deliverable: Approve S-M12-01: list/work queue, detail/history and permitted action forms for Office and admin application shells.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M12-01.

- [ ] INV-154 · `frontend` · `M12·BUILD` · Office and admin application shells: accessible user workflows
  - Depends on: INV-148, INV-150, INV-151, INV-152, INV-153.
  - Deliverable: Build S-M12-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Office and admin application shells feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M12-01.

- [ ] INV-155 · `backend` · `M12·NOTIFY` · Office and admin application shells: actionable notifications
  - Depends on: INV-150, INV-151, INV-152.
  - Deliverable: Register m12.attention and m12.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-156 · `backend` · `M12·ADMIN` · Office and admin application shells: administrative review controls
  - Depends on: INV-154.
  - Deliverable: Provide authorized history, exception review and safe recovery for Office and admin application shells using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-157 · `backend` · `M12·AUDIT` · Office and admin application shells: mutation evidence
  - Depends on: INV-150, INV-151, INV-152.
  - Deliverable: Declare audit actions for Office context switching, Platform admin separation, Search and navigation; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-158 · `backend` · `M12·EVENTS` · Office and admin application shells: versioned domain events
  - Depends on: INV-150, INV-151, INV-152.
  - Deliverable: Publish m12.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-159 · `backend` · `M12·PRIVACY` · Office and admin application shells: data classification and retention
  - Depends on: INV-150, INV-151, INV-152.
  - Deliverable: Classify all fields in saved_views; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-160 · `backend` · `M12·INTEGRATION` · Office and admin application shells: dependency integration
  - Depends on: INV-150, INV-151, INV-152, INV-148.
  - Deliverable: Exercise Office and admin application shells with prerequisite modules M03, M04, M05, M10, M11 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-161 · `devops` · `M12·OPERABILITY` · Office and admin application shells: runbook and failure signals
  - Depends on: INV-160.
  - Deliverable: Document deployment/configuration, metrics and recovery for Office and admin application shells; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-162 · `qa` · `M12·QA` · Office and admin application shells: acceptance and invariants
  - Depends on: INV-147, INV-148, INV-149, INV-150, INV-151, INV-152, INV-153, INV-154, INV-155, INV-156, INV-157, INV-158, INV-159, INV-160, INV-161.
  - Deliverable: Execute the feature acceptance suite for Office and admin application shells, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Company and warehouse context is visible on every operational screen; switching clears stale query caches and unsaved work is confirmed. Tenant administration and platform support use separate navigation and permissions; bundles are not the security boundary. Keyboard search uses authorized results and preserves tenant/company context in deep links.

### M13 · Android foundation and sync protocol

- [ ] INV-163 · `backend` · `M13·DATA` · Android foundation and sync protocol: schema and migrations
  - Depends on: INV-046, INV-062, INV-110, INV-146.
  - Deliverable: Create scoped tables sync_devices, sync_cursors, sync_commands, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Android foundation and sync protocol. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-164 · `backend` · `M13·API` · Android foundation and sync protocol: request and response contracts
  - Depends on: INV-163.
  - Deliverable: Implement and document 4 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /sync/register, GET /sync/bootstrap, GET /sync/changes, POST /sync/commands. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-165 · `backend` · `M13·AUTHZ` · Android foundation and sync protocol: enforce access boundaries
  - Depends on: INV-163.
  - Deliverable: Enforce roles Warehouse operator and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Android foundation and sync protocol identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-166 · `backend` · `M13·LIFE` · Durable local repository
  - Depends on: INV-164, INV-165, INV-163.
  - Deliverable: Encrypted SQLite cache and command queue survive process death; tenant switching wipes cached data before a new bootstrap.
  - Acceptance: Encrypted SQLite cache and command queue survive process death; tenant switching wipes cached data before a new bootstrap. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Encrypted SQLite cache and command queue survive process death; tenant switching wipes cached data before a new bootstrap. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-167 · `backend` · `M13·LIFE` · Sync protocol foundation
  - Depends on: INV-164, INV-165, INV-163.
  - Deliverable: Cursor-based pulls, tombstones, command IDs and ordered dependencies have executable protocol fixtures before business mobile screens.
  - Acceptance: Cursor-based pulls, tombstones, command IDs and ordered dependencies have executable protocol fixtures before business mobile screens. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Cursor-based pulls, tombstones, command IDs and ordered dependencies have executable protocol fixtures before business mobile screens. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-168 · `backend` · `M13·LIFE` · Pending versus posted
  - Depends on: INV-164, INV-165, INV-163.
  - Deliverable: Offline captures display pending status and never claim stock is committed until server acknowledgement.
  - Acceptance: Offline captures display pending status and never claim stock is committed until server acknowledgement. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Offline captures display pending status and never claim stock is committed until server acknowledgement. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-169 · `design` · `M13·DESIGN` · Android foundation and sync protocol: screen design
  - Depends on: INV-165, INV-146.
  - Deliverable: Approve S-M13-01: list/work queue, detail/history and permitted action forms for Android foundation and sync protocol.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M13-01.

- [ ] INV-170 · `mobile` · `M13·BUILD` · Android foundation and sync protocol: accessible user workflows
  - Depends on: INV-164, INV-166, INV-167, INV-168, INV-169.
  - Deliverable: Build S-M13-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Android foundation and sync protocol feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M13-01.

- [ ] INV-171 · `backend` · `M13·NOTIFY` · Android foundation and sync protocol: actionable notifications
  - Depends on: INV-166, INV-167, INV-168.
  - Deliverable: Register m13.attention and m13.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-172 · `backend` · `M13·ADMIN` · Android foundation and sync protocol: administrative review controls
  - Depends on: INV-170.
  - Deliverable: Provide authorized history, exception review and safe recovery for Android foundation and sync protocol using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-173 · `backend` · `M13·AUDIT` · Android foundation and sync protocol: mutation evidence
  - Depends on: INV-166, INV-167, INV-168.
  - Deliverable: Declare audit actions for Durable local repository, Sync protocol foundation, Pending versus posted; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-174 · `backend` · `M13·EVENTS` · Android foundation and sync protocol: versioned domain events
  - Depends on: INV-166, INV-167, INV-168.
  - Deliverable: Publish m13.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-175 · `backend` · `M13·PRIVACY` · Android foundation and sync protocol: data classification and retention
  - Depends on: INV-166, INV-167, INV-168.
  - Deliverable: Classify all fields in sync_devices, sync_cursors, sync_commands; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-176 · `backend` · `M13·INTEGRATION` · Android foundation and sync protocol: dependency integration
  - Depends on: INV-166, INV-167, INV-168, INV-164.
  - Deliverable: Exercise Android foundation and sync protocol with prerequisite modules M04, M05, M08, M11 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-177 · `backend` · `M13·OFFLINE` · Android foundation and sync protocol: interrupted-device recovery
  - Depends on: INV-170, INV-176.
  - Deliverable: Validate durable queue and cached state for Android foundation and sync protocol against OFFLINE_SYNC.md.
  - Acceptance: Process death and acknowledgement loss never duplicate a command. Conflicts remain visible; stale authorization cannot commit offline-captured changes.
  - Tests: Airplane mode; reboot; duplicate batch; stale version; revoked device; cursor reset.

- [ ] INV-178 · `devops` · `M13·OPERABILITY` · Android foundation and sync protocol: runbook and failure signals
  - Depends on: INV-176.
  - Deliverable: Document deployment/configuration, metrics and recovery for Android foundation and sync protocol; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-179 · `qa` · `M13·QA` · Android foundation and sync protocol: acceptance and invariants
  - Depends on: INV-163, INV-164, INV-165, INV-166, INV-167, INV-168, INV-169, INV-170, INV-171, INV-172, INV-173, INV-174, INV-175, INV-176, INV-177, INV-178.
  - Deliverable: Execute the feature acceptance suite for Android foundation and sync protocol, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Encrypted SQLite cache and command queue survive process death; tenant switching wipes cached data before a new bootstrap. Cursor-based pulls, tombstones, command IDs and ordered dependencies have executable protocol fixtures before business mobile screens. Offline captures display pending status and never claim stock is committed until server acknowledgement.

## Phase 4 — Companies and inventory master data

### M14 · Companies, branches and regional settings

- [ ] INV-180 · `backend` · `M14·DATA` · Companies, branches and regional settings: schema and migrations
  - Depends on: INV-030, INV-062, INV-078.
  - Deliverable: Create scoped tables companies, branches, regional_settings, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Companies, branches and regional settings. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-181 · `backend` · `M14·API` · Companies, branches and regional settings: request and response contracts
  - Depends on: INV-180.
  - Deliverable: Implement and document 7 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /companies, POST /branches, PATCH /companies/{id}/settings, GET /companies, GET /companies/{id}, GET /branches, GET /branches/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-182 · `backend` · `M14·AUTHZ` · Companies, branches and regional settings: enforce access boundaries
  - Depends on: INV-180.
  - Deliverable: Enforce roles Tenant admin and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Companies, branches and regional settings identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-183 · `backend` · `M14·LIFE` · Company and branch setup
  - Depends on: INV-181, INV-182, INV-180.
  - Deliverable: Codes are unique within tenant/company; active warehouses prevent hard deletion of their parent.
  - Acceptance: Codes are unique within tenant/company; active warehouses prevent hard deletion of their parent. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Codes are unique within tenant/company; active warehouses prevent hard deletion of their parent. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-184 · `backend` · `M14·LIFE` · Regional defaults
  - Depends on: INV-181, INV-182, INV-180.
  - Deliverable: New companies default to ETB, English and Africa/Addis_Ababa; UTC instants and company-local business dates remain distinct.
  - Acceptance: New companies default to ETB, English and Africa/Addis_Ababa; UTC instants and company-local business dates remain distinct. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: New companies default to ETB, English and Africa/Addis_Ababa; UTC instants and company-local business dates remain distinct. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-185 · `backend` · `M14·LIFE` · Currency governance
  - Depends on: INV-181, INV-182, INV-180.
  - Deliverable: Company base currency is immutable after the first valued movement; foreign-currency orders snapshot exchange rates with source and effective date.
  - Acceptance: Company base currency is immutable after the first valued movement; foreign-currency orders snapshot exchange rates with source and effective date. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Company base currency is immutable after the first valued movement; foreign-currency orders snapshot exchange rates with source and effective date. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-186 · `design` · `M14·DESIGN` · Companies, branches and regional settings: screen design
  - Depends on: INV-182, INV-146.
  - Deliverable: Approve S-M14-01: list/work queue, detail/history and permitted action forms for Companies, branches and regional settings.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M14-01.

- [ ] INV-187 · `frontend` · `M14·BUILD` · Companies, branches and regional settings: accessible user workflows
  - Depends on: INV-181, INV-183, INV-184, INV-185, INV-186.
  - Deliverable: Build S-M14-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Companies, branches and regional settings feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M14-01.

- [ ] INV-188 · `backend` · `M14·NOTIFY` · Companies, branches and regional settings: actionable notifications
  - Depends on: INV-183, INV-184, INV-185.
  - Deliverable: Register m14.attention and m14.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-189 · `backend` · `M14·ADMIN` · Companies, branches and regional settings: administrative review controls
  - Depends on: INV-187.
  - Deliverable: Provide authorized history, exception review and safe recovery for Companies, branches and regional settings using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-190 · `backend` · `M14·AUDIT` · Companies, branches and regional settings: mutation evidence
  - Depends on: INV-183, INV-184, INV-185.
  - Deliverable: Declare audit actions for Company and branch setup, Regional defaults, Currency governance; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-191 · `backend` · `M14·EVENTS` · Companies, branches and regional settings: versioned domain events
  - Depends on: INV-183, INV-184, INV-185.
  - Deliverable: Publish m14.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-192 · `backend` · `M14·PRIVACY` · Companies, branches and regional settings: data classification and retention
  - Depends on: INV-183, INV-184, INV-185.
  - Deliverable: Classify all fields in companies, branches, regional_settings; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-193 · `backend` · `M14·INTEGRATION` · Companies, branches and regional settings: dependency integration
  - Depends on: INV-183, INV-184, INV-185, INV-181.
  - Deliverable: Exercise Companies, branches and regional settings with prerequisite modules M03, M05, M06 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-194 · `devops` · `M14·OPERABILITY` · Companies, branches and regional settings: runbook and failure signals
  - Depends on: INV-193.
  - Deliverable: Document deployment/configuration, metrics and recovery for Companies, branches and regional settings; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-195 · `qa` · `M14·QA` · Companies, branches and regional settings: acceptance and invariants
  - Depends on: INV-180, INV-181, INV-182, INV-183, INV-184, INV-185, INV-186, INV-187, INV-188, INV-189, INV-190, INV-191, INV-192, INV-193, INV-194.
  - Deliverable: Execute the feature acceptance suite for Companies, branches and regional settings, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Codes are unique within tenant/company; active warehouses prevent hard deletion of their parent. New companies default to ETB, English and Africa/Addis_Ababa; UTC instants and company-local business dates remain distinct. Company base currency is immutable after the first valued movement; foreign-currency orders snapshot exchange rates with source and effective date.

### M15 · Suppliers and customers

- [ ] INV-196 · `backend` · `M15·DATA` · Suppliers and customers: schema and migrations
  - Depends on: INV-195.
  - Deliverable: Create scoped tables partners, partner_contacts, partner_references, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Suppliers and customers. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-197 · `backend` · `M15·API` · Suppliers and customers: request and response contracts
  - Depends on: INV-196.
  - Deliverable: Implement and document 5 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /partners, PATCH /partners/{id}, POST /partners/{id}/references, GET /partners, GET /partners/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-198 · `backend` · `M15·AUTHZ` · Suppliers and customers: enforce access boundaries
  - Depends on: INV-196.
  - Deliverable: Enforce roles Buyer, Sales clerk, Tenant admin and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Suppliers and customers identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-199 · `backend` · `M15·LIFE` · Partner directory
  - Depends on: INV-197, INV-198, INV-196.
  - Deliverable: A partner may be both supplier and customer; archive blocks new orders while retaining history.
  - Acceptance: A partner may be both supplier and customer; archive blocks new orders while retaining history. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: A partner may be both supplier and customer; archive blocks new orders while retaining history. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-200 · `backend` · `M15·LIFE` · Partner commercial references
  - Depends on: INV-197, INV-198, INV-196.
  - Deliverable: Supplier SKU, purchase unit, minimum order and lead time are effective-dated; customer item codes do not overwrite internal SKUs.
  - Acceptance: Supplier SKU, purchase unit, minimum order and lead time are effective-dated; customer item codes do not overwrite internal SKUs. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Supplier SKU, purchase unit, minimum order and lead time are effective-dated; customer item codes do not overwrite internal SKUs. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-201 · `backend` · `M15·LIFE` · Contact privacy
  - Depends on: INV-197, INV-198, INV-196.
  - Deliverable: Contact exports and deletion/anonymization follow retention rules without deleting stock evidence.
  - Acceptance: Contact exports and deletion/anonymization follow retention rules without deleting stock evidence. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Contact exports and deletion/anonymization follow retention rules without deleting stock evidence. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-202 · `design` · `M15·DESIGN` · Suppliers and customers: screen design
  - Depends on: INV-198, INV-146.
  - Deliverable: Approve S-M15-01: list/work queue, detail/history and permitted action forms for Suppliers and customers.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M15-01.

- [ ] INV-203 · `frontend` · `M15·BUILD` · Suppliers and customers: accessible user workflows
  - Depends on: INV-197, INV-199, INV-200, INV-201, INV-202.
  - Deliverable: Build S-M15-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Suppliers and customers feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M15-01.

- [ ] INV-204 · `backend` · `M15·NOTIFY` · Suppliers and customers: actionable notifications
  - Depends on: INV-199, INV-200, INV-201.
  - Deliverable: Register m15.attention and m15.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-205 · `backend` · `M15·ADMIN` · Suppliers and customers: administrative review controls
  - Depends on: INV-203.
  - Deliverable: Provide authorized history, exception review and safe recovery for Suppliers and customers using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-206 · `backend` · `M15·AUDIT` · Suppliers and customers: mutation evidence
  - Depends on: INV-199, INV-200, INV-201.
  - Deliverable: Declare audit actions for Partner directory, Partner commercial references, Contact privacy; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-207 · `backend` · `M15·EVENTS` · Suppliers and customers: versioned domain events
  - Depends on: INV-199, INV-200, INV-201.
  - Deliverable: Publish m15.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-208 · `backend` · `M15·PRIVACY` · Suppliers and customers: data classification and retention
  - Depends on: INV-199, INV-200, INV-201.
  - Deliverable: Classify all fields in partners, partner_contacts, partner_references; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-209 · `backend` · `M15·INTEGRATION` · Suppliers and customers: dependency integration
  - Depends on: INV-199, INV-200, INV-201, INV-197.
  - Deliverable: Exercise Suppliers and customers with prerequisite modules M14 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-210 · `devops` · `M15·OPERABILITY` · Suppliers and customers: runbook and failure signals
  - Depends on: INV-209.
  - Deliverable: Document deployment/configuration, metrics and recovery for Suppliers and customers; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-211 · `qa` · `M15·QA` · Suppliers and customers: acceptance and invariants
  - Depends on: INV-196, INV-197, INV-198, INV-199, INV-200, INV-201, INV-202, INV-203, INV-204, INV-205, INV-206, INV-207, INV-208, INV-209, INV-210.
  - Deliverable: Execute the feature acceptance suite for Suppliers and customers, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: A partner may be both supplier and customer; archive blocks new orders while retaining history. Supplier SKU, purchase unit, minimum order and lead time are effective-dated; customer item codes do not overwrite internal SKUs. Contact exports and deletion/anonymization follow retention rules without deleting stock evidence.

### M16 · Products, variants and packaging

- [ ] INV-212 · `backend` · `M16·DATA` · Products, variants and packaging: schema and migrations
  - Depends on: INV-195, INV-244.
  - Deliverable: Create scoped tables product_templates, product_variants, product_categories, product_barcodes, packaging, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Products, variants and packaging. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-213 · `backend` · `M16·API` · Products, variants and packaging: request and response contracts
  - Depends on: INV-212.
  - Deliverable: Implement and document 11 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /products, POST /products/{id}/variants, POST /products/{id}/barcodes, POST /products/{id}/archive, GET /products, GET /products/{id}, GET /product-categories, GET /product-categories/{id}, POST /product-categories, PATCH /products/{id}, PATCH /product-categories/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-214 · `backend` · `M16·AUTHZ` · Products, variants and packaging: enforce access boundaries
  - Depends on: INV-212.
  - Deliverable: Enforce roles Catalog manager and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Products, variants and packaging identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-215 · `backend` · `M16·LIFE` · Product and variant catalog
  - Depends on: INV-213, INV-214, INV-212.
  - Deliverable: SKU and barcode uniqueness are enforced per company; variant attribute combinations cannot duplicate.
  - Acceptance: SKU and barcode uniqueness are enforced per company; variant attribute combinations cannot duplicate. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: SKU and barcode uniqueness are enforced per company; variant attribute combinations cannot duplicate. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-216 · `backend` · `M16·LIFE` · Tracking configuration
  - Depends on: INV-213, INV-214, INV-212.
  - Deliverable: None, lot or serial tracking is chosen before stock exists; changing it requires a controlled migration and reconciliation.
  - Acceptance: None, lot or serial tracking is chosen before stock exists; changing it requires a controlled migration and reconciliation. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: None, lot or serial tracking is chosen before stock exists; changing it requires a controlled migration and reconciliation. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-217 · `backend` · `M16·LIFE` · Packaging and barcode aliases
  - Depends on: INV-213, INV-214, INV-212.
  - Deliverable: Multiple packaging barcodes resolve to explicit unit quantities; a carton scan cannot silently count as one base unit.
  - Acceptance: Multiple packaging barcodes resolve to explicit unit quantities; a carton scan cannot silently count as one base unit. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Multiple packaging barcodes resolve to explicit unit quantities; a carton scan cannot silently count as one base unit. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-218 · `backend` · `M16·LIFE` · Catalog import
  - Depends on: INV-213, INV-214, INV-212.
  - Deliverable: CSV dry-run reports row-level duplicate codes and invalid references; accepted batches are idempotent.
  - Acceptance: CSV dry-run reports row-level duplicate codes and invalid references; accepted batches are idempotent. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: CSV dry-run reports row-level duplicate codes and invalid references; accepted batches are idempotent. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-219 · `design` · `M16·DESIGN` · Products, variants and packaging: screen design
  - Depends on: INV-214, INV-146.
  - Deliverable: Approve S-M16-01: list/work queue, detail/history and permitted action forms for Products, variants and packaging.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M16-01.

- [ ] INV-220 · `frontend` · `M16·BUILD` · Products, variants and packaging: accessible user workflows
  - Depends on: INV-213, INV-215, INV-216, INV-217, INV-218, INV-219.
  - Deliverable: Build S-M16-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Products, variants and packaging feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M16-01.

- [ ] INV-221 · `backend` · `M16·NOTIFY` · Products, variants and packaging: actionable notifications
  - Depends on: INV-215, INV-216, INV-217, INV-218.
  - Deliverable: Register m16.attention and m16.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-222 · `backend` · `M16·ADMIN` · Products, variants and packaging: administrative review controls
  - Depends on: INV-220.
  - Deliverable: Provide authorized history, exception review and safe recovery for Products, variants and packaging using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-223 · `backend` · `M16·AUDIT` · Products, variants and packaging: mutation evidence
  - Depends on: INV-215, INV-216, INV-217, INV-218.
  - Deliverable: Declare audit actions for Product and variant catalog, Tracking configuration, Packaging and barcode aliases, Catalog import; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-224 · `backend` · `M16·EVENTS` · Products, variants and packaging: versioned domain events
  - Depends on: INV-215, INV-216, INV-217, INV-218.
  - Deliverable: Publish m16.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-225 · `backend` · `M16·PRIVACY` · Products, variants and packaging: data classification and retention
  - Depends on: INV-215, INV-216, INV-217, INV-218.
  - Deliverable: Classify all fields in product_templates, product_variants, product_categories, product_barcodes, packaging; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-226 · `backend` · `M16·INTEGRATION` · Products, variants and packaging: dependency integration
  - Depends on: INV-215, INV-216, INV-217, INV-218, INV-213.
  - Deliverable: Exercise Products, variants and packaging with prerequisite modules M14 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-227 · `devops` · `M16·OPERABILITY` · Products, variants and packaging: runbook and failure signals
  - Depends on: INV-226.
  - Deliverable: Document deployment/configuration, metrics and recovery for Products, variants and packaging; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-228 · `qa` · `M16·QA` · Products, variants and packaging: acceptance and invariants
  - Depends on: INV-212, INV-213, INV-214, INV-215, INV-216, INV-217, INV-218, INV-219, INV-220, INV-221, INV-222, INV-223, INV-224, INV-225, INV-226, INV-227.
  - Deliverable: Execute the feature acceptance suite for Products, variants and packaging, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 4 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: SKU and barcode uniqueness are enforced per company; variant attribute combinations cannot duplicate. None, lot or serial tracking is chosen before stock exists; changing it requires a controlled migration and reconciliation. Multiple packaging barcodes resolve to explicit unit quantities; a carton scan cannot silently count as one base unit. CSV dry-run reports row-level duplicate codes and invalid references; accepted batches are idempotent.

### M17 · Units and exact arithmetic

- [ ] INV-229 · `backend` · `M17·DATA` · Units and exact arithmetic: schema and migrations
  - Depends on: INV-195.
  - Deliverable: Create scoped tables uom_categories, units, currency_definitions, exchange_rates, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Units and exact arithmetic. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-230 · `backend` · `M17·API` · Units and exact arithmetic: request and response contracts
  - Depends on: INV-229.
  - Deliverable: Implement and document 6 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: GET /units, POST /units, POST /exchange-rates, GET /units/{id}, GET /exchange-rates, GET /exchange-rates/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-231 · `backend` · `M17·AUTHZ` · Units and exact arithmetic: enforce access boundaries
  - Depends on: INV-229.
  - Deliverable: Enforce roles Catalog manager and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Units and exact arithmetic identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-232 · `backend` · `M17·LIFE` · Unit conversions
  - Depends on: INV-230, INV-231, INV-229.
  - Deliverable: Convert only within a unit category using exact rational factors; snapshot conversions on document lines.
  - Acceptance: Convert only within a unit category using exact rational factors; snapshot conversions on document lines. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Convert only within a unit category using exact rational factors; snapshot conversions on document lines. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-233 · `backend` · `M17·LIFE` · Quantity precision
  - Depends on: INV-230, INV-231, INV-229.
  - Deliverable: Quantities use decimal strings with at most six fractional digits; serial quantities are whole units and conversion remainder must be explicitly resolved.
  - Acceptance: Quantities use decimal strings with at most six fractional digits; serial quantities are whole units and conversion remainder must be explicitly resolved. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Quantities use decimal strings with at most six fractional digits; serial quantities are whole units and conversion remainder must be explicitly resolved. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-234 · `backend` · `M17·LIFE` · Monetary precision
  - Depends on: INV-230, INV-231, INV-229.
  - Deliverable: Unit costs and rates use fixed precision; extended amounts round half-up to currency minor units once at document boundaries with deterministic remainder allocation.
  - Acceptance: Unit costs and rates use fixed precision; extended amounts round half-up to currency minor units once at document boundaries with deterministic remainder allocation. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Unit costs and rates use fixed precision; extended amounts round half-up to currency minor units once at document boundaries with deterministic remainder allocation. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-235 · `design` · `M17·DESIGN` · Units and exact arithmetic: screen design
  - Depends on: INV-231, INV-146.
  - Deliverable: Approve S-M17-01: list/work queue, detail/history and permitted action forms for Units and exact arithmetic.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M17-01.

- [ ] INV-236 · `frontend` · `M17·BUILD` · Units and exact arithmetic: accessible user workflows
  - Depends on: INV-230, INV-232, INV-233, INV-234, INV-235.
  - Deliverable: Build S-M17-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Units and exact arithmetic feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M17-01.

- [ ] INV-237 · `backend` · `M17·NOTIFY` · Units and exact arithmetic: actionable notifications
  - Depends on: INV-232, INV-233, INV-234.
  - Deliverable: Register m17.attention and m17.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-238 · `backend` · `M17·ADMIN` · Units and exact arithmetic: administrative review controls
  - Depends on: INV-236.
  - Deliverable: Provide authorized history, exception review and safe recovery for Units and exact arithmetic using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-239 · `backend` · `M17·AUDIT` · Units and exact arithmetic: mutation evidence
  - Depends on: INV-232, INV-233, INV-234.
  - Deliverable: Declare audit actions for Unit conversions, Quantity precision, Monetary precision; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-240 · `backend` · `M17·EVENTS` · Units and exact arithmetic: versioned domain events
  - Depends on: INV-232, INV-233, INV-234.
  - Deliverable: Publish m17.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-241 · `backend` · `M17·PRIVACY` · Units and exact arithmetic: data classification and retention
  - Depends on: INV-232, INV-233, INV-234.
  - Deliverable: Classify all fields in uom_categories, units, currency_definitions, exchange_rates; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-242 · `backend` · `M17·INTEGRATION` · Units and exact arithmetic: dependency integration
  - Depends on: INV-232, INV-233, INV-234, INV-230.
  - Deliverable: Exercise Units and exact arithmetic with prerequisite modules M14 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-243 · `devops` · `M17·OPERABILITY` · Units and exact arithmetic: runbook and failure signals
  - Depends on: INV-242.
  - Deliverable: Document deployment/configuration, metrics and recovery for Units and exact arithmetic; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-244 · `qa` · `M17·QA` · Units and exact arithmetic: acceptance and invariants
  - Depends on: INV-229, INV-230, INV-231, INV-232, INV-233, INV-234, INV-235, INV-236, INV-237, INV-238, INV-239, INV-240, INV-241, INV-242, INV-243.
  - Deliverable: Execute the feature acceptance suite for Units and exact arithmetic, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Convert only within a unit category using exact rational factors; snapshot conversions on document lines. Quantities use decimal strings with at most six fractional digits; serial quantities are whole units and conversion remainder must be explicitly resolved. Unit costs and rates use fixed precision; extended amounts round half-up to currency minor units once at document boundaries with deterministic remainder allocation.

### M18 · Warehouses and location hierarchy

- [ ] INV-245 · `backend` · `M18·DATA` · Warehouses and location hierarchy: schema and migrations
  - Depends on: INV-195.
  - Deliverable: Create scoped tables warehouses, locations, location_capacities, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Warehouses and location hierarchy. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-246 · `backend` · `M18·API` · Warehouses and location hierarchy: request and response contracts
  - Depends on: INV-245.
  - Deliverable: Implement and document 9 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /warehouses, POST /locations, POST /locations/{id}/archive, GET /warehouses, GET /warehouses/{id}, GET /locations, GET /locations/{id}, PATCH /warehouses/{id}, PATCH /locations/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-247 · `backend` · `M18·AUTHZ` · Warehouses and location hierarchy: enforce access boundaries
  - Depends on: INV-245.
  - Deliverable: Enforce roles Warehouse supervisor and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Warehouses and location hierarchy identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-248 · `backend` · `M18·LIFE` · Location hierarchy
  - Depends on: INV-246, INV-247, INV-245.
  - Deliverable: Warehouse, zone and bin form an acyclic tree; supplier, customer, inventory-loss and transit locations have explicit types.
  - Acceptance: Warehouse, zone and bin form an acyclic tree; supplier, customer, inventory-loss and transit locations have explicit types. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Warehouse, zone and bin form an acyclic tree; supplier, customer, inventory-loss and transit locations have explicit types. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-249 · `backend` · `M18·LIFE` · Operational areas
  - Depends on: INV-246, INV-247, INV-245.
  - Deliverable: Receiving, quarantine, stock, packing and dispatch locations have reservation eligibility rules.
  - Acceptance: Receiving, quarantine, stock, packing and dispatch locations have reservation eligibility rules. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Receiving, quarantine, stock, packing and dispatch locations have reservation eligibility rules. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-250 · `backend` · `M18·LIFE` · Archival and capacity
  - Depends on: INV-246, INV-247, INV-245.
  - Deliverable: Occupied or reserved locations cannot be archived; putaway cannot exceed configured capacity without a supervisor-approved exception.
  - Acceptance: Occupied or reserved locations cannot be archived; putaway cannot exceed configured capacity without a supervisor-approved exception. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Occupied or reserved locations cannot be archived; putaway cannot exceed configured capacity without a supervisor-approved exception. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-251 · `design` · `M18·DESIGN` · Warehouses and location hierarchy: screen design
  - Depends on: INV-247, INV-146.
  - Deliverable: Approve S-M18-01: list/work queue, detail/history and permitted action forms for Warehouses and location hierarchy.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M18-01.

- [ ] INV-252 · `frontend` · `M18·BUILD` · Warehouses and location hierarchy: accessible user workflows
  - Depends on: INV-246, INV-248, INV-249, INV-250, INV-251.
  - Deliverable: Build S-M18-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Warehouses and location hierarchy feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M18-01.

- [ ] INV-253 · `backend` · `M18·NOTIFY` · Warehouses and location hierarchy: actionable notifications
  - Depends on: INV-248, INV-249, INV-250.
  - Deliverable: Register m18.attention and m18.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-254 · `backend` · `M18·ADMIN` · Warehouses and location hierarchy: administrative review controls
  - Depends on: INV-252.
  - Deliverable: Provide authorized history, exception review and safe recovery for Warehouses and location hierarchy using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-255 · `backend` · `M18·AUDIT` · Warehouses and location hierarchy: mutation evidence
  - Depends on: INV-248, INV-249, INV-250.
  - Deliverable: Declare audit actions for Location hierarchy, Operational areas, Archival and capacity; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-256 · `backend` · `M18·EVENTS` · Warehouses and location hierarchy: versioned domain events
  - Depends on: INV-248, INV-249, INV-250.
  - Deliverable: Publish m18.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-257 · `backend` · `M18·PRIVACY` · Warehouses and location hierarchy: data classification and retention
  - Depends on: INV-248, INV-249, INV-250.
  - Deliverable: Classify all fields in warehouses, locations, location_capacities; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-258 · `backend` · `M18·INTEGRATION` · Warehouses and location hierarchy: dependency integration
  - Depends on: INV-248, INV-249, INV-250, INV-246.
  - Deliverable: Exercise Warehouses and location hierarchy with prerequisite modules M14 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-259 · `devops` · `M18·OPERABILITY` · Warehouses and location hierarchy: runbook and failure signals
  - Depends on: INV-258.
  - Deliverable: Document deployment/configuration, metrics and recovery for Warehouses and location hierarchy; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-260 · `qa` · `M18·QA` · Warehouses and location hierarchy: acceptance and invariants
  - Depends on: INV-245, INV-246, INV-247, INV-248, INV-249, INV-250, INV-251, INV-252, INV-253, INV-254, INV-255, INV-256, INV-257, INV-258, INV-259.
  - Deliverable: Execute the feature acceptance suite for Warehouses and location hierarchy, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Warehouse, zone and bin form an acyclic tree; supplier, customer, inventory-loss and transit locations have explicit types. Receiving, quarantine, stock, packing and dispatch locations have reservation eligibility rules. Occupied or reserved locations cannot be archived; putaway cannot exceed configured capacity without a supervisor-approved exception.

### M19 · Lot, serial and ownership identities

- [ ] INV-261 · `backend` · `M19·DATA` · Lot, serial and ownership identities: schema and migrations
  - Depends on: INV-211, INV-228, INV-244, INV-260.
  - Deliverable: Create scoped tables lots, serials, stock_owners, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Lot, serial and ownership identities. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-262 · `backend` · `M19·API` · Lot, serial and ownership identities: request and response contracts
  - Depends on: INV-261.
  - Deliverable: Implement and document 7 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /lots, POST /serials, GET /tracking-identities, GET /lots, GET /lots/{id}, GET /serials, GET /serials/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-263 · `backend` · `M19·AUTHZ` · Lot, serial and ownership identities: enforce access boundaries
  - Depends on: INV-261.
  - Deliverable: Enforce roles Catalog manager, Warehouse supervisor and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Lot, serial and ownership identities identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-264 · `backend` · `M19·LIFE` · Lot and serial identity
  - Depends on: INV-262, INV-263, INV-261.
  - Deliverable: Tracking identifiers are company/product scoped; a serial cannot simultaneously exist in two physical locations.
  - Acceptance: Tracking identifiers are company/product scoped; a serial cannot simultaneously exist in two physical locations. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Tracking identifiers are company/product scoped; a serial cannot simultaneously exist in two physical locations. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-265 · `backend` · `M19·LIFE` · Ownership dimensions
  - Depends on: INV-262, INV-263, INV-261.
  - Deliverable: Every stock bucket distinguishes company-owned and partner-owned goods; supplier custody is not company valuation.
  - Acceptance: Every stock bucket distinguishes company-owned and partner-owned goods; supplier custody is not company valuation. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Every stock bucket distinguishes company-owned and partner-owned goods; supplier custody is not company valuation. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-266 · `backend` · `M19·LIFE` · Receipt tracking requirements
  - Depends on: INV-262, INV-263, INV-261.
  - Deliverable: Tracked products cannot be posted without lot/serial allocation; early phases may create identities but advanced recall controls arrive in phase 8.
  - Acceptance: Tracked products cannot be posted without lot/serial allocation; early phases may create identities but advanced recall controls arrive in phase 8. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Tracked products cannot be posted without lot/serial allocation; early phases may create identities but advanced recall controls arrive in phase 8. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-267 · `design` · `M19·DESIGN` · Lot, serial and ownership identities: screen design
  - Depends on: INV-263, INV-146.
  - Deliverable: Approve S-M19-01: list/work queue, detail/history and permitted action forms for Lot, serial and ownership identities.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M19-01.

- [ ] INV-268 · `frontend` · `M19·BUILD` · Lot, serial and ownership identities: accessible user workflows
  - Depends on: INV-262, INV-264, INV-265, INV-266, INV-267.
  - Deliverable: Build S-M19-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Lot, serial and ownership identities feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M19-01.

- [ ] INV-269 · `backend` · `M19·NOTIFY` · Lot, serial and ownership identities: actionable notifications
  - Depends on: INV-264, INV-265, INV-266.
  - Deliverable: Register m19.attention and m19.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-270 · `backend` · `M19·ADMIN` · Lot, serial and ownership identities: administrative review controls
  - Depends on: INV-268.
  - Deliverable: Provide authorized history, exception review and safe recovery for Lot, serial and ownership identities using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-271 · `backend` · `M19·AUDIT` · Lot, serial and ownership identities: mutation evidence
  - Depends on: INV-264, INV-265, INV-266.
  - Deliverable: Declare audit actions for Lot and serial identity, Ownership dimensions, Receipt tracking requirements; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-272 · `backend` · `M19·EVENTS` · Lot, serial and ownership identities: versioned domain events
  - Depends on: INV-264, INV-265, INV-266.
  - Deliverable: Publish m19.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-273 · `backend` · `M19·PRIVACY` · Lot, serial and ownership identities: data classification and retention
  - Depends on: INV-264, INV-265, INV-266.
  - Deliverable: Classify all fields in lots, serials, stock_owners; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-274 · `backend` · `M19·INTEGRATION` · Lot, serial and ownership identities: dependency integration
  - Depends on: INV-264, INV-265, INV-266, INV-262.
  - Deliverable: Exercise Lot, serial and ownership identities with prerequisite modules M15, M16, M17, M18 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-275 · `devops` · `M19·OPERABILITY` · Lot, serial and ownership identities: runbook and failure signals
  - Depends on: INV-274.
  - Deliverable: Document deployment/configuration, metrics and recovery for Lot, serial and ownership identities; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-276 · `qa` · `M19·QA` · Lot, serial and ownership identities: acceptance and invariants
  - Depends on: INV-261, INV-262, INV-263, INV-264, INV-265, INV-266, INV-267, INV-268, INV-269, INV-270, INV-271, INV-272, INV-273, INV-274, INV-275.
  - Deliverable: Execute the feature acceptance suite for Lot, serial and ownership identities, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Tracking identifiers are company/product scoped; a serial cannot simultaneously exist in two physical locations. Every stock bucket distinguishes company-owned and partner-owned goods; supplier custody is not company valuation. Tracked products cannot be posted without lot/serial allocation; early phases may create identities but advanced recall controls arrive in phase 8.

## Phase 5 — Stock integrity and core operations

### M20 · Immutable stock ledger and projections

- [ ] INV-277 · `backend` · `M20·DATA` · Immutable stock ledger and projections: schema and migrations
  - Depends on: INV-094, INV-110, INV-244, INV-260, INV-276.
  - Deliverable: Create scoped tables stock_moves, stock_buckets, cost_facts, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Immutable stock ledger and projections. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-278 · `backend` · `M20·API` · Immutable stock ledger and projections: request and response contracts
  - Depends on: INV-277.
  - Deliverable: Implement and document 4 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: GET /stock/moves, GET /stock/balances, POST /stock/moves/{id}/reverse, GET /stock/moves/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-279 · `backend` · `M20·AUTHZ` · Immutable stock ledger and projections: enforce access boundaries
  - Depends on: INV-277.
  - Deliverable: Enforce roles Warehouse supervisor, Auditor and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Immutable stock ledger and projections identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-280 · `backend` · `M20·LIFE` · Posting transaction
  - Depends on: INV-278, INV-279, INV-277.
  - Deliverable: Lock affected buckets in canonical order; move, balance, cost fact, command receipt, audit and outbox commit atomically.
  - Acceptance: Lock affected buckets in canonical order; move, balance, cost fact, command receipt, audit and outbox commit atomically. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Lock affected buckets in canonical order; move, balance, cost fact, command receipt, audit and outbox commit atomically. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-281 · `backend` · `M20·LIFE` · No negative physical stock
  - Depends on: INV-278, INV-279, INV-277.
  - Deliverable: Concurrent outgoing moves cannot reduce a controlled physical bucket below zero; shortages return a typed conflict without partial effects.
  - Acceptance: Concurrent outgoing moves cannot reduce a controlled physical bucket below zero; shortages return a typed conflict without partial effects. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Concurrent outgoing moves cannot reduce a controlled physical bucket below zero; shortages return a typed conflict without partial effects. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-282 · `backend` · `M20·LIFE` · Reversal and rebuild
  - Depends on: INV-278, INV-279, INV-277.
  - Deliverable: Posted rows are immutable; eligible reversals reference originals and a rebuild from movements reproduces projections exactly.
  - Acceptance: Posted rows are immutable; eligible reversals reference originals and a rebuild from movements reproduces projections exactly. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Posted rows are immutable; eligible reversals reference originals and a rebuild from movements reproduces projections exactly. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-283 · `backend` · `M20·LIFE` · Cost fact capture
  - Depends on: INV-278, INV-279, INV-277.
  - Deliverable: Receipt/issue source costs, conversion factors and ownership are preserved from day one for phase 11 valuation replay; financial go-live is gated until valuation is complete.
  - Acceptance: Receipt/issue source costs, conversion factors and ownership are preserved from day one for phase 11 valuation replay; financial go-live is gated until valuation is complete. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Receipt/issue source costs, conversion factors and ownership are preserved from day one for phase 11 valuation replay; financial go-live is gated until valuation is complete. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-284 · `design` · `M20·DESIGN` · Immutable stock ledger and projections: screen design
  - Depends on: INV-279, INV-146.
  - Deliverable: Approve S-M20-01: list/work queue, detail/history and permitted action forms for Immutable stock ledger and projections.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M20-01.

- [ ] INV-285 · `frontend` · `M20·BUILD` · Immutable stock ledger and projections: accessible user workflows
  - Depends on: INV-278, INV-280, INV-281, INV-282, INV-283, INV-284.
  - Deliverable: Build S-M20-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Immutable stock ledger and projections feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M20-01.

- [ ] INV-286 · `backend` · `M20·NOTIFY` · Immutable stock ledger and projections: actionable notifications
  - Depends on: INV-280, INV-281, INV-282, INV-283.
  - Deliverable: Register m20.attention and m20.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-287 · `backend` · `M20·ADMIN` · Immutable stock ledger and projections: administrative review controls
  - Depends on: INV-285.
  - Deliverable: Provide authorized history, exception review and safe recovery for Immutable stock ledger and projections using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-288 · `backend` · `M20·AUDIT` · Immutable stock ledger and projections: mutation evidence
  - Depends on: INV-280, INV-281, INV-282, INV-283.
  - Deliverable: Declare audit actions for Posting transaction, No negative physical stock, Reversal and rebuild, Cost fact capture; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-289 · `backend` · `M20·EVENTS` · Immutable stock ledger and projections: versioned domain events
  - Depends on: INV-280, INV-281, INV-282, INV-283.
  - Deliverable: Publish m20.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-290 · `backend` · `M20·PRIVACY` · Immutable stock ledger and projections: data classification and retention
  - Depends on: INV-280, INV-281, INV-282, INV-283.
  - Deliverable: Classify all fields in stock_moves, stock_buckets, cost_facts; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-291 · `backend` · `M20·INTEGRATION` · Immutable stock ledger and projections: dependency integration
  - Depends on: INV-280, INV-281, INV-282, INV-283, INV-278.
  - Deliverable: Exercise Immutable stock ledger and projections with prerequisite modules M07, M08, M17, M18, M19 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-292 · `devops` · `M20·OPERABILITY` · Immutable stock ledger and projections: runbook and failure signals
  - Depends on: INV-291.
  - Deliverable: Document deployment/configuration, metrics and recovery for Immutable stock ledger and projections; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-293 · `qa` · `M20·QA` · Immutable stock ledger and projections: acceptance and invariants
  - Depends on: INV-277, INV-278, INV-279, INV-280, INV-281, INV-282, INV-283, INV-284, INV-285, INV-286, INV-287, INV-288, INV-289, INV-290, INV-291, INV-292.
  - Deliverable: Execute the feature acceptance suite for Immutable stock ledger and projections, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 4 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Lock affected buckets in canonical order; move, balance, cost fact, command receipt, audit and outbox commit atomically. Concurrent outgoing moves cannot reduce a controlled physical bucket below zero; shortages return a typed conflict without partial effects. Posted rows are immutable; eligible reversals reference originals and a rebuild from movements reproduces projections exactly. Receipt/issue source costs, conversion factors and ownership are preserved from day one for phase 11 valuation replay; financial go-live is gated until valuation is complete. C02: Atomic posting failure. All writes roll back together; retry commits once and every projection matches the ledger.

### M21 · Reservations and availability

- [ ] INV-294 · `backend` · `M21·DATA` · Reservations and availability: schema and migrations
  - Depends on: INV-293.
  - Deliverable: Create scoped tables reservations, reservation_allocations, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Reservations and availability. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-295 · `backend` · `M21·API` · Reservations and availability: request and response contracts
  - Depends on: INV-294.
  - Deliverable: Implement and document 6 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /reservations, POST /reservations/{id}/release, GET /stock/availability, GET /stock/forecast, GET /reservations, GET /reservations/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-296 · `backend` · `M21·AUTHZ` · Reservations and availability: enforce access boundaries
  - Depends on: INV-294.
  - Deliverable: Enforce roles Sales clerk, Warehouse supervisor and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Reservations and availability identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-297 · `backend` · `M21·LIFE` · Atomic allocation
  - Depends on: INV-295, INV-296, INV-294.
  - Deliverable: Two concurrent orders requesting the same ten units can reserve at most ten in total.
  - Acceptance: Two concurrent orders requesting the same ten units can reserve at most ten in total. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Two concurrent orders requesting the same ten units can reserve at most ten in total. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-298 · `backend` · `M21·LIFE` · Partial allocation and release
  - Depends on: INV-295, INV-296, INV-294.
  - Deliverable: Partial fills identify remaining demand; cancel, expiry and short-pick release only unconsumed reservations.
  - Acceptance: Partial fills identify remaining demand; cancel, expiry and short-pick release only unconsumed reservations. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Partial fills identify remaining demand; cancel, expiry and short-pick release only unconsumed reservations. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-299 · `backend` · `M21·LIFE` · Availability and forecast
  - Depends on: INV-295, INV-296, INV-294.
  - Deliverable: Available equals eligible on-hand minus active reservations; forecast adds dated confirmed receipts and subtracts outstanding demand without double-counting reservations.
  - Acceptance: Available equals eligible on-hand minus active reservations; forecast adds dated confirmed receipts and subtracts outstanding demand without double-counting reservations. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Available equals eligible on-hand minus active reservations; forecast adds dated confirmed receipts and subtracts outstanding demand without double-counting reservations. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-300 · `design` · `M21·DESIGN` · Reservations and availability: screen design
  - Depends on: INV-296, INV-146.
  - Deliverable: Approve S-M21-01: list/work queue, detail/history and permitted action forms for Reservations and availability.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M21-01.

- [ ] INV-301 · `frontend` · `M21·BUILD` · Reservations and availability: accessible user workflows
  - Depends on: INV-295, INV-297, INV-298, INV-299, INV-300.
  - Deliverable: Build S-M21-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Reservations and availability feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M21-01.

- [ ] INV-302 · `backend` · `M21·NOTIFY` · Reservations and availability: actionable notifications
  - Depends on: INV-297, INV-298, INV-299.
  - Deliverable: Register m21.attention and m21.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-303 · `backend` · `M21·ADMIN` · Reservations and availability: administrative review controls
  - Depends on: INV-301.
  - Deliverable: Provide authorized history, exception review and safe recovery for Reservations and availability using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-304 · `backend` · `M21·AUDIT` · Reservations and availability: mutation evidence
  - Depends on: INV-297, INV-298, INV-299.
  - Deliverable: Declare audit actions for Atomic allocation, Partial allocation and release, Availability and forecast; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-305 · `backend` · `M21·EVENTS` · Reservations and availability: versioned domain events
  - Depends on: INV-297, INV-298, INV-299.
  - Deliverable: Publish m21.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-306 · `backend` · `M21·PRIVACY` · Reservations and availability: data classification and retention
  - Depends on: INV-297, INV-298, INV-299.
  - Deliverable: Classify all fields in reservations, reservation_allocations; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-307 · `backend` · `M21·INTEGRATION` · Reservations and availability: dependency integration
  - Depends on: INV-297, INV-298, INV-299, INV-295.
  - Deliverable: Exercise Reservations and availability with prerequisite modules M20 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-308 · `devops` · `M21·OPERABILITY` · Reservations and availability: runbook and failure signals
  - Depends on: INV-307.
  - Deliverable: Document deployment/configuration, metrics and recovery for Reservations and availability; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-309 · `qa` · `M21·QA` · Reservations and availability: acceptance and invariants
  - Depends on: INV-294, INV-295, INV-296, INV-297, INV-298, INV-299, INV-300, INV-301, INV-302, INV-303, INV-304, INV-305, INV-306, INV-307, INV-308.
  - Deliverable: Execute the feature acceptance suite for Reservations and availability, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Two concurrent orders requesting the same ten units can reserve at most ten in total. Partial fills identify remaining demand; cancel, expiry and short-pick release only unconsumed reservations. Available equals eligible on-hand minus active reservations; forecast adds dated confirmed receipts and subtracts outstanding demand without double-counting reservations. C01: Concurrent reservation. Total active reservations never exceed ten; losing request returns shortage or a documented partial allocation; no negative bucket.

### M22 · Core receipts, issues and opening stock

- [ ] INV-310 · `backend` · `M22·DATA` · Core receipts, issues and opening stock: schema and migrations
  - Depends on: INV-078, INV-293, INV-309.
  - Deliverable: Create scoped tables stock_operations, stock_operation_lines, opening_batches, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Core receipts, issues and opening stock. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-311 · `backend` · `M22·API` · Core receipts, issues and opening stock: request and response contracts
  - Depends on: INV-310.
  - Deliverable: Implement and document 8 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /stock/operations, POST /stock/operations/{id}/validate, POST /stock/opening-batches, POST /stock/operations/{id}/cancel, GET /stock/operations, GET /stock/operations/{id}, GET /stock/opening-batches, GET /stock/opening-batches/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-312 · `backend` · `M22·AUTHZ` · Core receipts, issues and opening stock: enforce access boundaries
  - Depends on: INV-310.
  - Deliverable: Enforce roles Warehouse operator, Warehouse supervisor and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Core receipts, issues and opening stock identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-313 · `backend` · `M22·LIFE` · Opening stock
  - Depends on: INV-311, INV-312, INV-310.
  - Deliverable: Approved opening batches load quantities, tracking and cost basis once with reconciliation totals and a migration reference.
  - Acceptance: Approved opening batches load quantities, tracking and cost basis once with reconciliation totals and a migration reference. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Approved opening batches load quantities, tracking and cost basis once with reconciliation totals and a migration reference. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-314 · `backend` · `M22·LIFE` · Receipt and internal issue
  - Depends on: INV-311, INV-312, INV-310.
  - Deliverable: Done quantities are validated against unit/tracking rules; controlled over-receipts require explicit approval.
  - Acceptance: Done quantities are validated against unit/tracking rules; controlled over-receipts require explicit approval. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Done quantities are validated against unit/tracking rules; controlled over-receipts require explicit approval. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-315 · `backend` · `M22·LIFE` · Partial operations and backorders
  - Depends on: INV-311, INV-312, INV-310.
  - Deliverable: Posting part of a document creates a linked remainder or cancels it explicitly; replay never creates a second backorder.
  - Acceptance: Posting part of a document creates a linked remainder or cancels it explicitly; replay never creates a second backorder. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Posting part of a document creates a linked remainder or cancels it explicitly; replay never creates a second backorder. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-316 · `design` · `M22·DESIGN` · Core receipts, issues and opening stock: screen design
  - Depends on: INV-312, INV-146.
  - Deliverable: Approve S-M22-01: list/work queue, detail/history and permitted action forms for Core receipts, issues and opening stock.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M22-01.

- [ ] INV-317 · `frontend` · `M22·BUILD` · Core receipts, issues and opening stock: accessible user workflows
  - Depends on: INV-311, INV-313, INV-314, INV-315, INV-316.
  - Deliverable: Build S-M22-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Core receipts, issues and opening stock feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M22-01.

- [ ] INV-318 · `backend` · `M22·NOTIFY` · Core receipts, issues and opening stock: actionable notifications
  - Depends on: INV-313, INV-314, INV-315.
  - Deliverable: Register m22.attention and m22.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-319 · `backend` · `M22·ADMIN` · Core receipts, issues and opening stock: administrative review controls
  - Depends on: INV-317.
  - Deliverable: Provide authorized history, exception review and safe recovery for Core receipts, issues and opening stock using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-320 · `backend` · `M22·AUDIT` · Core receipts, issues and opening stock: mutation evidence
  - Depends on: INV-313, INV-314, INV-315.
  - Deliverable: Declare audit actions for Opening stock, Receipt and internal issue, Partial operations and backorders; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-321 · `backend` · `M22·EVENTS` · Core receipts, issues and opening stock: versioned domain events
  - Depends on: INV-313, INV-314, INV-315.
  - Deliverable: Publish m22.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-322 · `backend` · `M22·PRIVACY` · Core receipts, issues and opening stock: data classification and retention
  - Depends on: INV-313, INV-314, INV-315.
  - Deliverable: Classify all fields in stock_operations, stock_operation_lines, opening_batches; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-323 · `backend` · `M22·INTEGRATION` · Core receipts, issues and opening stock: dependency integration
  - Depends on: INV-313, INV-314, INV-315, INV-311.
  - Deliverable: Exercise Core receipts, issues and opening stock with prerequisite modules M06, M20, M21 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-324 · `devops` · `M22·OPERABILITY` · Core receipts, issues and opening stock: runbook and failure signals
  - Depends on: INV-323.
  - Deliverable: Document deployment/configuration, metrics and recovery for Core receipts, issues and opening stock; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-325 · `qa` · `M22·QA` · Core receipts, issues and opening stock: acceptance and invariants
  - Depends on: INV-310, INV-311, INV-312, INV-313, INV-314, INV-315, INV-316, INV-317, INV-318, INV-319, INV-320, INV-321, INV-322, INV-323, INV-324.
  - Deliverable: Execute the feature acceptance suite for Core receipts, issues and opening stock, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Approved opening batches load quantities, tracking and cost basis once with reconciliation totals and a migration reference. Done quantities are validated against unit/tracking rules; controlled over-receipts require explicit approval. Posting part of a document creates a linked remainder or cancels it explicitly; replay never creates a second backorder. C03: Duplicate and conflicting command. First two responses identify one receipt; changed payload returns 409 and creates no movement.

### M23 · Transfers and in-transit custody

- [ ] INV-326 · `backend` · `M23·DATA` · Transfers and in-transit custody: schema and migrations
  - Depends on: INV-325.
  - Deliverable: Create scoped tables transfers, transfer_lines, transfer_discrepancies, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Transfers and in-transit custody. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-327 · `backend` · `M23·API` · Transfers and in-transit custody: request and response contracts
  - Depends on: INV-326.
  - Deliverable: Implement and document 6 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /transfers, POST /transfers/{id}/ship, POST /transfers/{id}/receive, POST /transfers/{id}/resolve-discrepancy, GET /transfers, GET /transfers/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-328 · `backend` · `M23·AUTHZ` · Transfers and in-transit custody: enforce access boundaries
  - Depends on: INV-326.
  - Deliverable: Enforce roles Warehouse operator, Warehouse supervisor and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Transfers and in-transit custody identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-329 · `backend` · `M23·LIFE` · Immediate and staged transfers
  - Depends on: INV-327, INV-328, INV-326.
  - Deliverable: In-warehouse moves commit once; inter-warehouse shipment moves stock into transit until destination receipt.
  - Acceptance: In-warehouse moves commit once; inter-warehouse shipment moves stock into transit until destination receipt. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: In-warehouse moves commit once; inter-warehouse shipment moves stock into transit until destination receipt. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-330 · `backend` · `M23·LIFE` · Partial receipt and discrepancy
  - Depends on: INV-327, INV-328, INV-326.
  - Deliverable: Received quantity cannot exceed shipped balance; missing or damaged quantities stay in transit until approved return/scrap resolution.
  - Acceptance: Received quantity cannot exceed shipped balance; missing or damaged quantities stay in transit until approved return/scrap resolution. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Received quantity cannot exceed shipped balance; missing or damaged quantities stay in transit until approved return/scrap resolution. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-331 · `backend` · `M23·LIFE` · Transfer conservation
  - Depends on: INV-327, INV-328, INV-326.
  - Deliverable: Company-owned quantities sum equally across source, transit and destination before and after transfer; retries preserve totals.
  - Acceptance: Company-owned quantities sum equally across source, transit and destination before and after transfer; retries preserve totals. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Company-owned quantities sum equally across source, transit and destination before and after transfer; retries preserve totals. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-332 · `design` · `M23·DESIGN` · Transfers and in-transit custody: screen design
  - Depends on: INV-328, INV-146.
  - Deliverable: Approve S-M23-01: list/work queue, detail/history and permitted action forms for Transfers and in-transit custody.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M23-01.

- [ ] INV-333 · `frontend` · `M23·BUILD` · Transfers and in-transit custody: accessible user workflows
  - Depends on: INV-327, INV-329, INV-330, INV-331, INV-332.
  - Deliverable: Build S-M23-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Transfers and in-transit custody feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M23-01.

- [ ] INV-334 · `backend` · `M23·NOTIFY` · Transfers and in-transit custody: actionable notifications
  - Depends on: INV-329, INV-330, INV-331.
  - Deliverable: Register m23.attention and m23.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-335 · `backend` · `M23·ADMIN` · Transfers and in-transit custody: administrative review controls
  - Depends on: INV-333.
  - Deliverable: Provide authorized history, exception review and safe recovery for Transfers and in-transit custody using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-336 · `backend` · `M23·AUDIT` · Transfers and in-transit custody: mutation evidence
  - Depends on: INV-329, INV-330, INV-331.
  - Deliverable: Declare audit actions for Immediate and staged transfers, Partial receipt and discrepancy, Transfer conservation; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-337 · `backend` · `M23·EVENTS` · Transfers and in-transit custody: versioned domain events
  - Depends on: INV-329, INV-330, INV-331.
  - Deliverable: Publish m23.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-338 · `backend` · `M23·PRIVACY` · Transfers and in-transit custody: data classification and retention
  - Depends on: INV-329, INV-330, INV-331.
  - Deliverable: Classify all fields in transfers, transfer_lines, transfer_discrepancies; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-339 · `backend` · `M23·INTEGRATION` · Transfers and in-transit custody: dependency integration
  - Depends on: INV-329, INV-330, INV-331, INV-327.
  - Deliverable: Exercise Transfers and in-transit custody with prerequisite modules M22 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-340 · `devops` · `M23·OPERABILITY` · Transfers and in-transit custody: runbook and failure signals
  - Depends on: INV-339.
  - Deliverable: Document deployment/configuration, metrics and recovery for Transfers and in-transit custody; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-341 · `qa` · `M23·QA` · Transfers and in-transit custody: acceptance and invariants
  - Depends on: INV-326, INV-327, INV-328, INV-329, INV-330, INV-331, INV-332, INV-333, INV-334, INV-335, INV-336, INV-337, INV-338, INV-339, INV-340.
  - Deliverable: Execute the feature acceptance suite for Transfers and in-transit custody, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: In-warehouse moves commit once; inter-warehouse shipment moves stock into transit until destination receipt. Received quantity cannot exceed shipped balance; missing or damaged quantities stay in transit until approved return/scrap resolution. Company-owned quantities sum equally across source, transit and destination before and after transfer; retries preserve totals.

## Phase 6 — Purchasing and inbound quality

### M24 · Requisitions, RFQs and purchase orders

- [ ] INV-342 · `backend` · `M24·DATA` · Requisitions, RFQs and purchase orders: schema and migrations
  - Depends on: INV-078, INV-211, INV-228, INV-244, INV-325.
  - Deliverable: Create scoped tables purchase_requisitions, rfqs, rfq_lines, purchase_orders, purchase_order_lines, purchase_agreements, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Requisitions, RFQs and purchase orders. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-343 · `backend` · `M24·API` · Requisitions, RFQs and purchase orders: request and response contracts
  - Depends on: INV-342.
  - Deliverable: Implement and document 16 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /purchase/requisitions, POST /purchase/rfqs, POST /purchase/rfqs/{id}/compare, POST /purchase/orders, POST /purchase/orders/{id}/submit, POST /purchase/agreements, GET /purchase/requisitions, GET /purchase/requisitions/{id}, GET /purchase/rfqs, GET /purchase/rfqs/{id}, GET /purchase/orders, GET /purchase/orders/{id}, GET /purchase/agreements, GET /purchase/agreements/{id}, PATCH /purchase/orders/{id}, POST /purchase/orders/{id}/cancel. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-344 · `backend` · `M24·AUTHZ` · Requisitions, RFQs and purchase orders: enforce access boundaries
  - Depends on: INV-342.
  - Deliverable: Enforce roles Requester, Buyer, Approver and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Requisitions, RFQs and purchase orders identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-345 · `backend` · `M24·LIFE` · Requisition and quotation comparison
  - Depends on: INV-343, INV-344, INV-342.
  - Deliverable: Approved need produces RFQs; offers compare converted units, currency, lead time and landed-cost estimates without hiding original prices.
  - Acceptance: Approved need produces RFQs; offers compare converted units, currency, lead time and landed-cost estimates without hiding original prices. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Approved need produces RFQs; offers compare converted units, currency, lead time and landed-cost estimates without hiding original prices. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-346 · `backend` · `M24·LIFE` · Approved PO revisions
  - Depends on: INV-343, INV-344, INV-342.
  - Deliverable: Approved orders snapshot commercial terms; amendment preserves prior revision and reapproves changed commitments.
  - Acceptance: Approved orders snapshot commercial terms; amendment preserves prior revision and reapproves changed commitments. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Approved orders snapshot commercial terms; amendment preserves prior revision and reapproves changed commitments. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-347 · `backend` · `M24·LIFE` · Blanket order releases
  - Depends on: INV-343, INV-344, INV-342.
  - Deliverable: Call-offs cannot exceed approved quantity/value ceiling or validity dates without a new agreement revision.
  - Acceptance: Call-offs cannot exceed approved quantity/value ceiling or validity dates without a new agreement revision. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Call-offs cannot exceed approved quantity/value ceiling or validity dates without a new agreement revision. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-348 · `backend` · `M24·LIFE` · Purchase cancellation
  - Depends on: INV-343, INV-344, INV-342.
  - Deliverable: Cancel only unreceived quantities; received quantities require vendor-return workflow rather than destructive edits.
  - Acceptance: Cancel only unreceived quantities; received quantities require vendor-return workflow rather than destructive edits. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Cancel only unreceived quantities; received quantities require vendor-return workflow rather than destructive edits. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-349 · `design` · `M24·DESIGN` · Requisitions, RFQs and purchase orders: screen design
  - Depends on: INV-344, INV-146.
  - Deliverable: Approve S-M24-01: list/work queue, detail/history and permitted action forms for Requisitions, RFQs and purchase orders.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M24-01.

- [ ] INV-350 · `frontend` · `M24·BUILD` · Requisitions, RFQs and purchase orders: accessible user workflows
  - Depends on: INV-343, INV-345, INV-346, INV-347, INV-348, INV-349.
  - Deliverable: Build S-M24-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Requisitions, RFQs and purchase orders feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M24-01.

- [ ] INV-351 · `backend` · `M24·NOTIFY` · Requisitions, RFQs and purchase orders: actionable notifications
  - Depends on: INV-345, INV-346, INV-347, INV-348.
  - Deliverable: Register m24.attention and m24.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-352 · `backend` · `M24·ADMIN` · Requisitions, RFQs and purchase orders: administrative review controls
  - Depends on: INV-350.
  - Deliverable: Provide authorized history, exception review and safe recovery for Requisitions, RFQs and purchase orders using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-353 · `backend` · `M24·AUDIT` · Requisitions, RFQs and purchase orders: mutation evidence
  - Depends on: INV-345, INV-346, INV-347, INV-348.
  - Deliverable: Declare audit actions for Requisition and quotation comparison, Approved PO revisions, Blanket order releases, Purchase cancellation; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-354 · `backend` · `M24·EVENTS` · Requisitions, RFQs and purchase orders: versioned domain events
  - Depends on: INV-345, INV-346, INV-347, INV-348.
  - Deliverable: Publish m24.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-355 · `backend` · `M24·PRIVACY` · Requisitions, RFQs and purchase orders: data classification and retention
  - Depends on: INV-345, INV-346, INV-347, INV-348.
  - Deliverable: Classify all fields in purchase_requisitions, rfqs, rfq_lines, purchase_orders, purchase_order_lines, purchase_agreements; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-356 · `backend` · `M24·INTEGRATION` · Requisitions, RFQs and purchase orders: dependency integration
  - Depends on: INV-345, INV-346, INV-347, INV-348, INV-343.
  - Deliverable: Exercise Requisitions, RFQs and purchase orders with prerequisite modules M06, M15, M16, M17, M22 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-357 · `devops` · `M24·OPERABILITY` · Requisitions, RFQs and purchase orders: runbook and failure signals
  - Depends on: INV-356.
  - Deliverable: Document deployment/configuration, metrics and recovery for Requisitions, RFQs and purchase orders; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-358 · `qa` · `M24·QA` · Requisitions, RFQs and purchase orders: acceptance and invariants
  - Depends on: INV-342, INV-343, INV-344, INV-345, INV-346, INV-347, INV-348, INV-349, INV-350, INV-351, INV-352, INV-353, INV-354, INV-355, INV-356, INV-357.
  - Deliverable: Execute the feature acceptance suite for Requisitions, RFQs and purchase orders, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 4 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Approved need produces RFQs; offers compare converted units, currency, lead time and landed-cost estimates without hiding original prices. Approved orders snapshot commercial terms; amendment preserves prior revision and reapproves changed commitments. Call-offs cannot exceed approved quantity/value ceiling or validity dates without a new agreement revision. Cancel only unreceived quantities; received quantities require vendor-return workflow rather than destructive edits.

### M25 · Supplier receiving and inspection handoff

- [ ] INV-359 · `backend` · `M25·DATA` · Supplier receiving and inspection handoff: schema and migrations
  - Depends on: INV-358, INV-276, INV-325.
  - Deliverable: Create scoped tables receipts, receipt_lines, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Supplier receiving and inspection handoff. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-360 · `backend` · `M25·API` · Supplier receiving and inspection handoff: request and response contracts
  - Depends on: INV-359.
  - Deliverable: Implement and document 5 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /purchase/orders/{id}/receipts, POST /receipts/{id}/validate, GET /purchase/orders/{id}/receiving-status, GET /receipts, GET /receipts/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-361 · `backend` · `M25·AUTHZ` · Supplier receiving and inspection handoff: enforce access boundaries
  - Depends on: INV-359.
  - Deliverable: Enforce roles Warehouse operator, Warehouse supervisor and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Supplier receiving and inspection handoff identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-362 · `backend` · `M25·LIFE` · PO receipt matching
  - Depends on: INV-360, INV-361, INV-359.
  - Deliverable: Partial deliveries track ordered, received and outstanding quantities independently; receipt references deduplicate within supplier/company.
  - Acceptance: Partial deliveries track ordered, received and outstanding quantities independently; receipt references deduplicate within supplier/company. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Partial deliveries track ordered, received and outstanding quantities independently; receipt references deduplicate within supplier/company. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-363 · `backend` · `M25·LIFE` · Receive to quarantine
  - Depends on: INV-360, INV-361, INV-359.
  - Deliverable: Inspection-required stock posts into quarantine; accepted goods become available only after quality release.
  - Acceptance: Inspection-required stock posts into quarantine; accepted goods become available only after quality release. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Inspection-required stock posts into quarantine; accepted goods become available only after quality release. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-364 · `backend` · `M25·LIFE` · Receipt cost snapshot
  - Depends on: INV-360, INV-361, INV-359.
  - Deliverable: Purchase price, exchange rate and unit conversion are copied onto cost facts without creating a vendor bill.
  - Acceptance: Purchase price, exchange rate and unit conversion are copied onto cost facts without creating a vendor bill. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Purchase price, exchange rate and unit conversion are copied onto cost facts without creating a vendor bill. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-365 · `design` · `M25·DESIGN` · Supplier receiving and inspection handoff: screen design
  - Depends on: INV-361, INV-146.
  - Deliverable: Approve S-M25-01: list/work queue, detail/history and permitted action forms for Supplier receiving and inspection handoff.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M25-01.

- [ ] INV-366 · `frontend` · `M25·BUILD` · Supplier receiving and inspection handoff: accessible user workflows
  - Depends on: INV-360, INV-362, INV-363, INV-364, INV-365.
  - Deliverable: Build S-M25-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Supplier receiving and inspection handoff feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M25-01.

- [ ] INV-367 · `backend` · `M25·NOTIFY` · Supplier receiving and inspection handoff: actionable notifications
  - Depends on: INV-362, INV-363, INV-364.
  - Deliverable: Register m25.attention and m25.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-368 · `backend` · `M25·ADMIN` · Supplier receiving and inspection handoff: administrative review controls
  - Depends on: INV-366.
  - Deliverable: Provide authorized history, exception review and safe recovery for Supplier receiving and inspection handoff using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-369 · `backend` · `M25·AUDIT` · Supplier receiving and inspection handoff: mutation evidence
  - Depends on: INV-362, INV-363, INV-364.
  - Deliverable: Declare audit actions for PO receipt matching, Receive to quarantine, Receipt cost snapshot; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-370 · `backend` · `M25·EVENTS` · Supplier receiving and inspection handoff: versioned domain events
  - Depends on: INV-362, INV-363, INV-364.
  - Deliverable: Publish m25.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-371 · `backend` · `M25·PRIVACY` · Supplier receiving and inspection handoff: data classification and retention
  - Depends on: INV-362, INV-363, INV-364.
  - Deliverable: Classify all fields in receipts, receipt_lines; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-372 · `backend` · `M25·INTEGRATION` · Supplier receiving and inspection handoff: dependency integration
  - Depends on: INV-362, INV-363, INV-364, INV-360.
  - Deliverable: Exercise Supplier receiving and inspection handoff with prerequisite modules M24, M19, M22 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-373 · `devops` · `M25·OPERABILITY` · Supplier receiving and inspection handoff: runbook and failure signals
  - Depends on: INV-372.
  - Deliverable: Document deployment/configuration, metrics and recovery for Supplier receiving and inspection handoff; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-374 · `qa` · `M25·QA` · Supplier receiving and inspection handoff: acceptance and invariants
  - Depends on: INV-359, INV-360, INV-361, INV-362, INV-363, INV-364, INV-365, INV-366, INV-367, INV-368, INV-369, INV-370, INV-371, INV-372, INV-373.
  - Deliverable: Execute the feature acceptance suite for Supplier receiving and inspection handoff, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Partial deliveries track ordered, received and outstanding quantities independently; receipt references deduplicate within supplier/company. Inspection-required stock posts into quarantine; accepted goods become available only after quality release. Purchase price, exchange rate and unit conversion are copied onto cost facts without creating a vendor bill.

### M26 · Quality inspections and disposition

- [ ] INV-375 · `backend` · `M26·DATA` · Quality inspections and disposition: schema and migrations
  - Depends on: INV-078, INV-374.
  - Deliverable: Create scoped tables quality_plans, inspections, inspection_results, quality_dispositions, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Quality inspections and disposition. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-376 · `backend` · `M26·API` · Quality inspections and disposition: request and response contracts
  - Depends on: INV-375.
  - Deliverable: Implement and document 8 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /quality/plans, POST /inspections/{id}/results, POST /inspections/{id}/release, POST /inspections/{id}/reject, GET /quality/plans, GET /quality/plans/{id}, GET /inspections, GET /inspections/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-377 · `backend` · `M26·AUTHZ` · Quality inspections and disposition: enforce access boundaries
  - Depends on: INV-375.
  - Deliverable: Enforce roles Quality inspector, Warehouse supervisor and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Quality inspections and disposition identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-378 · `backend` · `M26·LIFE` · Inspection execution
  - Depends on: INV-376, INV-377, INV-375.
  - Deliverable: Required checklist results and evidence must be complete before disposition; inspector authority is warehouse scoped.
  - Acceptance: Required checklist results and evidence must be complete before disposition; inspector authority is warehouse scoped. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Required checklist results and evidence must be complete before disposition; inspector authority is warehouse scoped. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-379 · `backend` · `M26·LIFE` · Split disposition
  - Depends on: INV-376, INV-377, INV-375.
  - Deliverable: Accepted plus rejected quantities equal inspected quantity; release moves accepted stock only and leaves rejected stock blocked.
  - Acceptance: Accepted plus rejected quantities equal inspected quantity; release moves accepted stock only and leaves rejected stock blocked. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Accepted plus rejected quantities equal inspected quantity; release moves accepted stock only and leaves rejected stock blocked. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-380 · `backend` · `M26·LIFE` · Reinspection and evidence
  - Depends on: INV-376, INV-377, INV-375.
  - Deliverable: Failed items require a new linked inspection; prior results remain immutable.
  - Acceptance: Failed items require a new linked inspection; prior results remain immutable. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Failed items require a new linked inspection; prior results remain immutable. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-381 · `design` · `M26·DESIGN` · Quality inspections and disposition: screen design
  - Depends on: INV-377, INV-146.
  - Deliverable: Approve S-M26-01: list/work queue, detail/history and permitted action forms for Quality inspections and disposition.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M26-01.

- [ ] INV-382 · `frontend` · `M26·BUILD` · Quality inspections and disposition: accessible user workflows
  - Depends on: INV-376, INV-378, INV-379, INV-380, INV-381.
  - Deliverable: Build S-M26-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Quality inspections and disposition feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M26-01.

- [ ] INV-383 · `backend` · `M26·NOTIFY` · Quality inspections and disposition: actionable notifications
  - Depends on: INV-378, INV-379, INV-380.
  - Deliverable: Register m26.attention and m26.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-384 · `backend` · `M26·ADMIN` · Quality inspections and disposition: administrative review controls
  - Depends on: INV-382.
  - Deliverable: Provide authorized history, exception review and safe recovery for Quality inspections and disposition using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-385 · `backend` · `M26·AUDIT` · Quality inspections and disposition: mutation evidence
  - Depends on: INV-378, INV-379, INV-380.
  - Deliverable: Declare audit actions for Inspection execution, Split disposition, Reinspection and evidence; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-386 · `backend` · `M26·EVENTS` · Quality inspections and disposition: versioned domain events
  - Depends on: INV-378, INV-379, INV-380.
  - Deliverable: Publish m26.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-387 · `backend` · `M26·PRIVACY` · Quality inspections and disposition: data classification and retention
  - Depends on: INV-378, INV-379, INV-380.
  - Deliverable: Classify all fields in quality_plans, inspections, inspection_results, quality_dispositions; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-388 · `backend` · `M26·INTEGRATION` · Quality inspections and disposition: dependency integration
  - Depends on: INV-378, INV-379, INV-380, INV-376.
  - Deliverable: Exercise Quality inspections and disposition with prerequisite modules M06, M25 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-389 · `devops` · `M26·OPERABILITY` · Quality inspections and disposition: runbook and failure signals
  - Depends on: INV-388.
  - Deliverable: Document deployment/configuration, metrics and recovery for Quality inspections and disposition; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-390 · `qa` · `M26·QA` · Quality inspections and disposition: acceptance and invariants
  - Depends on: INV-375, INV-376, INV-377, INV-378, INV-379, INV-380, INV-381, INV-382, INV-383, INV-384, INV-385, INV-386, INV-387, INV-388, INV-389.
  - Deliverable: Execute the feature acceptance suite for Quality inspections and disposition, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Required checklist results and evidence must be complete before disposition; inspector authority is warehouse scoped. Accepted plus rejected quantities equal inspected quantity; release moves accepted stock only and leaves rejected stock blocked. Failed items require a new linked inspection; prior results remain immutable. C04: Partial receipt and backorder. Stock totals reflect 55 accepted, five quarantined/rejected and 40 newly inspected; order quantities and backorders do not duplicate.

## Phase 7 — Sales orders and fulfillment

### M27 · Sales quotations and orders

- [ ] INV-391 · `backend` · `M27·DATA` · Sales quotations and orders: schema and migrations
  - Depends on: INV-078, INV-211, INV-228, INV-244, INV-309.
  - Deliverable: Create scoped tables price_lists, price_rules, quotations, sales_orders, sales_order_lines, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Sales quotations and orders. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-392 · `backend` · `M27·API` · Sales quotations and orders: request and response contracts
  - Depends on: INV-391.
  - Deliverable: Implement and document 12 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /sales/quotations, POST /sales/quotations/{id}/confirm, POST /sales/orders/{id}/allocate, POST /sales/orders/{id}/cancel, POST /sales/price-lists, GET /sales/quotations, GET /sales/quotations/{id}, GET /sales/orders, GET /sales/orders/{id}, GET /sales/price-lists, GET /sales/price-lists/{id}, PATCH /sales/orders/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-393 · `backend` · `M27·AUTHZ` · Sales quotations and orders: enforce access boundaries
  - Depends on: INV-391.
  - Deliverable: Enforce roles Sales clerk, Sales manager and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Sales quotations and orders identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-394 · `backend` · `M27·LIFE` · Quotation and pricing
  - Depends on: INV-392, INV-393, INV-391.
  - Deliverable: Server resolves effective price tier and currency; discounts beyond configured authority require approval.
  - Acceptance: Server resolves effective price tier and currency; discounts beyond configured authority require approval. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Server resolves effective price tier and currency; discounts beyond configured authority require approval. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-395 · `backend` · `M27·LIFE` · Sales confirmation
  - Depends on: INV-392, INV-393, INV-391.
  - Deliverable: Confirmation snapshots terms and creates fulfillment demand; insufficient stock produces partial allocation/backorder rather than a fictitious sale of available stock.
  - Acceptance: Confirmation snapshots terms and creates fulfillment demand; insufficient stock produces partial allocation/backorder rather than a fictitious sale of available stock. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Confirmation snapshots terms and creates fulfillment demand; insufficient stock produces partial allocation/backorder rather than a fictitious sale of available stock. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-396 · `backend` · `M27·LIFE` · Order changes
  - Depends on: INV-392, INV-393, INV-391.
  - Deliverable: Shipped quantities cannot be cancelled; edits to unfulfilled demand release/recompute reservations and version checks prevent lost updates.
  - Acceptance: Shipped quantities cannot be cancelled; edits to unfulfilled demand release/recompute reservations and version checks prevent lost updates. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Shipped quantities cannot be cancelled; edits to unfulfilled demand release/recompute reservations and version checks prevent lost updates. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-397 · `design` · `M27·DESIGN` · Sales quotations and orders: screen design
  - Depends on: INV-393, INV-146.
  - Deliverable: Approve S-M27-01: list/work queue, detail/history and permitted action forms for Sales quotations and orders.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M27-01.

- [ ] INV-398 · `frontend` · `M27·BUILD` · Sales quotations and orders: accessible user workflows
  - Depends on: INV-392, INV-394, INV-395, INV-396, INV-397.
  - Deliverable: Build S-M27-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Sales quotations and orders feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M27-01.

- [ ] INV-399 · `backend` · `M27·NOTIFY` · Sales quotations and orders: actionable notifications
  - Depends on: INV-394, INV-395, INV-396.
  - Deliverable: Register m27.attention and m27.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-400 · `backend` · `M27·ADMIN` · Sales quotations and orders: administrative review controls
  - Depends on: INV-398.
  - Deliverable: Provide authorized history, exception review and safe recovery for Sales quotations and orders using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-401 · `backend` · `M27·AUDIT` · Sales quotations and orders: mutation evidence
  - Depends on: INV-394, INV-395, INV-396.
  - Deliverable: Declare audit actions for Quotation and pricing, Sales confirmation, Order changes; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-402 · `backend` · `M27·EVENTS` · Sales quotations and orders: versioned domain events
  - Depends on: INV-394, INV-395, INV-396.
  - Deliverable: Publish m27.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-403 · `backend` · `M27·PRIVACY` · Sales quotations and orders: data classification and retention
  - Depends on: INV-394, INV-395, INV-396.
  - Deliverable: Classify all fields in price_lists, price_rules, quotations, sales_orders, sales_order_lines; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-404 · `backend` · `M27·INTEGRATION` · Sales quotations and orders: dependency integration
  - Depends on: INV-394, INV-395, INV-396, INV-392.
  - Deliverable: Exercise Sales quotations and orders with prerequisite modules M06, M15, M16, M17, M21 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-405 · `devops` · `M27·OPERABILITY` · Sales quotations and orders: runbook and failure signals
  - Depends on: INV-404.
  - Deliverable: Document deployment/configuration, metrics and recovery for Sales quotations and orders; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-406 · `qa` · `M27·QA` · Sales quotations and orders: acceptance and invariants
  - Depends on: INV-391, INV-392, INV-393, INV-394, INV-395, INV-396, INV-397, INV-398, INV-399, INV-400, INV-401, INV-402, INV-403, INV-404, INV-405.
  - Deliverable: Execute the feature acceptance suite for Sales quotations and orders, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Server resolves effective price tier and currency; discounts beyond configured authority require approval. Confirmation snapshots terms and creates fulfillment demand; insufficient stock produces partial allocation/backorder rather than a fictitious sale of available stock. Shipped quantities cannot be cancelled; edits to unfulfilled demand release/recompute reservations and version checks prevent lost updates.

### M28 · Pick, pack and dispatch

- [ ] INV-407 · `backend` · `M28·DATA` · Pick, pack and dispatch: schema and migrations
  - Depends on: INV-406, INV-325, INV-341.
  - Deliverable: Create scoped tables pick_tasks, pick_lines, packages, package_contents, dispatches, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Pick, pack and dispatch. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-408 · `backend` · `M28·API` · Pick, pack and dispatch: request and response contracts
  - Depends on: INV-407.
  - Deliverable: Implement and document 9 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: GET /pick-tasks, POST /pick-tasks/{id}/confirm, POST /packages, POST /dispatches/{id}/validate, GET /pick-tasks/{id}, GET /packages, GET /packages/{id}, GET /dispatches, GET /dispatches/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-409 · `backend` · `M28·AUTHZ` · Pick, pack and dispatch: enforce access boundaries
  - Depends on: INV-407.
  - Deliverable: Enforce roles Picker, Packer, Dispatcher and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Pick, pack and dispatch identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-410 · `backend` · `M28·LIFE` · Pick verification
  - Depends on: INV-408, INV-409, INV-407.
  - Deliverable: Location, SKU, lot/serial and actual quantity match the assigned task; short-picks release missing reservation and record reason.
  - Acceptance: Location, SKU, lot/serial and actual quantity match the assigned task; short-picks release missing reservation and record reason. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Location, SKU, lot/serial and actual quantity match the assigned task; short-picks release missing reservation and record reason. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-411 · `backend` · `M28·LIFE` · Packing control
  - Depends on: INV-408, INV-409, INV-407.
  - Deliverable: Package contents cannot exceed picked stock; repacking preserves traceability and labels identify packages uniquely.
  - Acceptance: Package contents cannot exceed picked stock; repacking preserves traceability and labels identify packages uniquely. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Package contents cannot exceed picked stock; repacking preserves traceability and labels identify packages uniquely. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-412 · `backend` · `M28·LIFE` · Dispatch and delivery records
  - Depends on: INV-408, INV-409, INV-407.
  - Deliverable: Dispatch consumes reservations and posts outgoing stock exactly once; packing slip is explicitly not a tax invoice.
  - Acceptance: Dispatch consumes reservations and posts outgoing stock exactly once; packing slip is explicitly not a tax invoice. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Dispatch consumes reservations and posts outgoing stock exactly once; packing slip is explicitly not a tax invoice. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-413 · `design` · `M28·DESIGN` · Pick, pack and dispatch: screen design
  - Depends on: INV-409, INV-146.
  - Deliverable: Approve S-M28-01: list/work queue, detail/history and permitted action forms for Pick, pack and dispatch.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M28-01.

- [ ] INV-414 · `frontend` · `M28·BUILD` · Pick, pack and dispatch: accessible user workflows
  - Depends on: INV-408, INV-410, INV-411, INV-412, INV-413.
  - Deliverable: Build S-M28-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Pick, pack and dispatch feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M28-01.

- [ ] INV-415 · `backend` · `M28·NOTIFY` · Pick, pack and dispatch: actionable notifications
  - Depends on: INV-410, INV-411, INV-412.
  - Deliverable: Register m28.attention and m28.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-416 · `backend` · `M28·ADMIN` · Pick, pack and dispatch: administrative review controls
  - Depends on: INV-414.
  - Deliverable: Provide authorized history, exception review and safe recovery for Pick, pack and dispatch using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-417 · `backend` · `M28·AUDIT` · Pick, pack and dispatch: mutation evidence
  - Depends on: INV-410, INV-411, INV-412.
  - Deliverable: Declare audit actions for Pick verification, Packing control, Dispatch and delivery records; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-418 · `backend` · `M28·EVENTS` · Pick, pack and dispatch: versioned domain events
  - Depends on: INV-410, INV-411, INV-412.
  - Deliverable: Publish m28.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-419 · `backend` · `M28·PRIVACY` · Pick, pack and dispatch: data classification and retention
  - Depends on: INV-410, INV-411, INV-412.
  - Deliverable: Classify all fields in pick_tasks, pick_lines, packages, package_contents, dispatches; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-420 · `backend` · `M28·INTEGRATION` · Pick, pack and dispatch: dependency integration
  - Depends on: INV-410, INV-411, INV-412, INV-408.
  - Deliverable: Exercise Pick, pack and dispatch with prerequisite modules M27, M22, M23 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-421 · `devops` · `M28·OPERABILITY` · Pick, pack and dispatch: runbook and failure signals
  - Depends on: INV-420.
  - Deliverable: Document deployment/configuration, metrics and recovery for Pick, pack and dispatch; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-422 · `qa` · `M28·QA` · Pick, pack and dispatch: acceptance and invariants
  - Depends on: INV-407, INV-408, INV-409, INV-410, INV-411, INV-412, INV-413, INV-414, INV-415, INV-416, INV-417, INV-418, INV-419, INV-420, INV-421.
  - Deliverable: Execute the feature acceptance suite for Pick, pack and dispatch, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Location, SKU, lot/serial and actual quantity match the assigned task; short-picks release missing reservation and record reason. Package contents cannot exceed picked stock; repacking preserves traceability and labels identify packages uniquely. Dispatch consumes reservations and posts outgoing stock exactly once; packing slip is explicitly not a tax invoice.

## Phase 8 — Traceability, returns and inventory control

### M29 · Customer and vendor returns

- [ ] INV-423 · `backend` · `M29·DATA` · Customer and vendor returns: schema and migrations
  - Depends on: INV-374, INV-422, INV-390.
  - Deliverable: Create scoped tables return_authorizations, return_lines, return_receipts, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Customer and vendor returns. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-424 · `backend` · `M29·API` · Customer and vendor returns: request and response contracts
  - Depends on: INV-423.
  - Deliverable: Implement and document 6 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /returns, POST /returns/{id}/authorize, POST /returns/{id}/receive, POST /returns/{id}/ship, GET /returns, GET /returns/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-425 · `backend` · `M29·AUTHZ` · Customer and vendor returns: enforce access boundaries
  - Depends on: INV-423.
  - Deliverable: Enforce roles Sales clerk, Buyer, Warehouse supervisor and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Customer and vendor returns identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-426 · `backend` · `M29·LIFE` · Linked return entitlement
  - Depends on: INV-424, INV-425, INV-423.
  - Deliverable: Cumulative returned quantities cannot exceed original delivered/received quantities; serial returns must match originals.
  - Acceptance: Cumulative returned quantities cannot exceed original delivered/received quantities; serial returns must match originals. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Cumulative returned quantities cannot exceed original delivered/received quantities; serial returns must match originals. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-427 · `backend` · `M29·LIFE` · Customer return inspection
  - Depends on: INV-424, INV-425, INV-423.
  - Deliverable: Returned stock enters quarantine, then restock or scrap; original movement cost basis is retained for valuation.
  - Acceptance: Returned stock enters quarantine, then restock or scrap; original movement cost basis is retained for valuation. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Returned stock enters quarantine, then restock or scrap; original movement cost basis is retained for valuation. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-428 · `backend` · `M29·LIFE` · Vendor returns
  - Depends on: INV-424, INV-425, INV-423.
  - Deliverable: Rejected or authorized stock ships to supplier and adjusts PO receiving status according to explicit replace-or-close choice; no credit note is issued here.
  - Acceptance: Rejected or authorized stock ships to supplier and adjusts PO receiving status according to explicit replace-or-close choice; no credit note is issued here. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Rejected or authorized stock ships to supplier and adjusts PO receiving status according to explicit replace-or-close choice; no credit note is issued here. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-429 · `design` · `M29·DESIGN` · Customer and vendor returns: screen design
  - Depends on: INV-425, INV-146.
  - Deliverable: Approve S-M29-01: list/work queue, detail/history and permitted action forms for Customer and vendor returns.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M29-01.

- [ ] INV-430 · `frontend` · `M29·BUILD` · Customer and vendor returns: accessible user workflows
  - Depends on: INV-424, INV-426, INV-427, INV-428, INV-429.
  - Deliverable: Build S-M29-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Customer and vendor returns feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M29-01.

- [ ] INV-431 · `backend` · `M29·NOTIFY` · Customer and vendor returns: actionable notifications
  - Depends on: INV-426, INV-427, INV-428.
  - Deliverable: Register m29.attention and m29.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-432 · `backend` · `M29·ADMIN` · Customer and vendor returns: administrative review controls
  - Depends on: INV-430.
  - Deliverable: Provide authorized history, exception review and safe recovery for Customer and vendor returns using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-433 · `backend` · `M29·AUDIT` · Customer and vendor returns: mutation evidence
  - Depends on: INV-426, INV-427, INV-428.
  - Deliverable: Declare audit actions for Linked return entitlement, Customer return inspection, Vendor returns; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-434 · `backend` · `M29·EVENTS` · Customer and vendor returns: versioned domain events
  - Depends on: INV-426, INV-427, INV-428.
  - Deliverable: Publish m29.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-435 · `backend` · `M29·PRIVACY` · Customer and vendor returns: data classification and retention
  - Depends on: INV-426, INV-427, INV-428.
  - Deliverable: Classify all fields in return_authorizations, return_lines, return_receipts; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-436 · `backend` · `M29·INTEGRATION` · Customer and vendor returns: dependency integration
  - Depends on: INV-426, INV-427, INV-428, INV-424.
  - Deliverable: Exercise Customer and vendor returns with prerequisite modules M25, M28, M26 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-437 · `devops` · `M29·OPERABILITY` · Customer and vendor returns: runbook and failure signals
  - Depends on: INV-436.
  - Deliverable: Document deployment/configuration, metrics and recovery for Customer and vendor returns; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-438 · `qa` · `M29·QA` · Customer and vendor returns: acceptance and invariants
  - Depends on: INV-423, INV-424, INV-425, INV-426, INV-427, INV-428, INV-429, INV-430, INV-431, INV-432, INV-433, INV-434, INV-435, INV-436, INV-437.
  - Deliverable: Execute the feature acceptance suite for Customer and vendor returns, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Cumulative returned quantities cannot exceed original delivered/received quantities; serial returns must match originals. Returned stock enters quarantine, then restock or scrap; original movement cost basis is retained for valuation. Rejected or authorized stock ships to supplier and adjusts PO receiving status according to explicit replace-or-close choice; no credit note is issued here. C07: Serial uniqueness and returns. A serial has one physical position; duplicate receipt and excessive return are rejected; first return goes to quarantine.

### M30 · Expiry, recalls and scrap

- [ ] INV-439 · `backend` · `M30·DATA` · Expiry, recalls and scrap: schema and migrations
  - Depends on: INV-276, INV-293, INV-390, INV-422.
  - Deliverable: Create scoped tables recalls, recall_targets, scrap_requests, expiry_policies, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Expiry, recalls and scrap. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-440 · `backend` · `M30·API` · Expiry, recalls and scrap: request and response contracts
  - Depends on: INV-439.
  - Deliverable: Implement and document 9 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: GET /traceability, POST /recalls, POST /recalls/{id}/close, POST /scrap, POST /scrap/{id}/post, GET /recalls, GET /recalls/{id}, GET /scrap, GET /scrap/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-441 · `backend` · `M30·AUTHZ` · Expiry, recalls and scrap: enforce access boundaries
  - Depends on: INV-439.
  - Deliverable: Enforce roles Quality inspector, Warehouse supervisor, Approver and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Expiry, recalls and scrap identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-442 · `backend` · `M30·LIFE` · Expiry and FEFO
  - Depends on: INV-440, INV-441, INV-439.
  - Deliverable: Removal date drives FEFO with deterministic lot tie-breaks; expired, recalled or quarantined stock is not reservable.
  - Acceptance: Removal date drives FEFO with deterministic lot tie-breaks; expired, recalled or quarantined stock is not reservable. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Removal date drives FEFO with deterministic lot tie-breaks; expired, recalled or quarantined stock is not reservable. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-443 · `backend` · `M30·LIFE` · Recall genealogy
  - Depends on: INV-440, INV-441, INV-439.
  - Deliverable: Lot/serial trace traverses receipts, internal moves, shipments and returns; affected customer contacts are access-controlled.
  - Acceptance: Lot/serial trace traverses receipts, internal moves, shipments and returns; affected customer contacts are access-controlled. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Lot/serial trace traverses receipts, internal moves, shipments and returns; affected customer contacts are access-controlled. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-444 · `backend` · `M30·LIFE` · Approved scrap
  - Depends on: INV-440, INV-441, INV-439.
  - Deliverable: Scrap posts to a loss location only after approval and evidence; quantities and value remain traceable through reversal rules.
  - Acceptance: Scrap posts to a loss location only after approval and evidence; quantities and value remain traceable through reversal rules. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Scrap posts to a loss location only after approval and evidence; quantities and value remain traceable through reversal rules. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-445 · `design` · `M30·DESIGN` · Expiry, recalls and scrap: screen design
  - Depends on: INV-441, INV-146.
  - Deliverable: Approve S-M30-01: list/work queue, detail/history and permitted action forms for Expiry, recalls and scrap.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M30-01.

- [ ] INV-446 · `frontend` · `M30·BUILD` · Expiry, recalls and scrap: accessible user workflows
  - Depends on: INV-440, INV-442, INV-443, INV-444, INV-445.
  - Deliverable: Build S-M30-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Expiry, recalls and scrap feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M30-01.

- [ ] INV-447 · `backend` · `M30·NOTIFY` · Expiry, recalls and scrap: actionable notifications
  - Depends on: INV-442, INV-443, INV-444.
  - Deliverable: Register m30.attention and m30.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-448 · `backend` · `M30·ADMIN` · Expiry, recalls and scrap: administrative review controls
  - Depends on: INV-446.
  - Deliverable: Provide authorized history, exception review and safe recovery for Expiry, recalls and scrap using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-449 · `backend` · `M30·AUDIT` · Expiry, recalls and scrap: mutation evidence
  - Depends on: INV-442, INV-443, INV-444.
  - Deliverable: Declare audit actions for Expiry and FEFO, Recall genealogy, Approved scrap; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-450 · `backend` · `M30·EVENTS` · Expiry, recalls and scrap: versioned domain events
  - Depends on: INV-442, INV-443, INV-444.
  - Deliverable: Publish m30.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-451 · `backend` · `M30·PRIVACY` · Expiry, recalls and scrap: data classification and retention
  - Depends on: INV-442, INV-443, INV-444.
  - Deliverable: Classify all fields in recalls, recall_targets, scrap_requests, expiry_policies; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-452 · `backend` · `M30·INTEGRATION` · Expiry, recalls and scrap: dependency integration
  - Depends on: INV-442, INV-443, INV-444, INV-440.
  - Deliverable: Exercise Expiry, recalls and scrap with prerequisite modules M19, M20, M26, M28 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-453 · `devops` · `M30·OPERABILITY` · Expiry, recalls and scrap: runbook and failure signals
  - Depends on: INV-452.
  - Deliverable: Document deployment/configuration, metrics and recovery for Expiry, recalls and scrap; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-454 · `qa` · `M30·QA` · Expiry, recalls and scrap: acceptance and invariants
  - Depends on: INV-439, INV-440, INV-441, INV-442, INV-443, INV-444, INV-445, INV-446, INV-447, INV-448, INV-449, INV-450, INV-451, INV-452, INV-453.
  - Deliverable: Execute the feature acceptance suite for Expiry, recalls and scrap, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Removal date drives FEFO with deterministic lot tie-breaks; expired, recalled or quarantined stock is not reservable. Lot/serial trace traverses receipts, internal moves, shipments and returns; affected customer contacts are access-controlled. Scrap posts to a loss location only after approval and evidence; quantities and value remain traceable through reversal rules. C08: Recall and expiry race. Dispatch rechecks eligibility and blocks; released reservations and affected customer trace remain auditable.

### M31 · Blind counts and reconciliation

- [ ] INV-455 · `backend` · `M31·DATA` · Blind counts and reconciliation: schema and migrations
  - Depends on: INV-078, INV-293, INV-325.
  - Deliverable: Create scoped tables count_sessions, count_lines, count_movements, count_adjustments, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Blind counts and reconciliation. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-456 · `backend` · `M31·API` · Blind counts and reconciliation: request and response contracts
  - Depends on: INV-455.
  - Deliverable: Implement and document 8 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /counts, POST /counts/{id}/start, POST /counts/{id}/lines, POST /counts/{id}/recount, POST /counts/{id}/approve, POST /counts/{id}/post, GET /counts, GET /counts/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-457 · `backend` · `M31·AUTHZ` · Blind counts and reconciliation: enforce access boundaries
  - Depends on: INV-455.
  - Deliverable: Enforce roles Counter, Warehouse supervisor, Approver and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Blind counts and reconciliation identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-458 · `backend` · `M31·LIFE` · Blind and cycle counting
  - Depends on: INV-456, INV-457, INV-455.
  - Deliverable: Counter sees required identities but not system quantity; location schedules generate count assignments without duplicates.
  - Acceptance: Counter sees required identities but not system quantity; location schedules generate count assignments without duplicates. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Counter sees required identities but not system quantity; location schedules generate count assignments without duplicates. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-459 · `backend` · `M31·LIFE` · Moving-stock reconciliation
  - Depends on: INV-456, INV-457, INV-455.
  - Deliverable: Snapshot plus timestamped movements is reconciled to each count observation; ambiguous late/offline observations require recount before posting.
  - Acceptance: Snapshot plus timestamped movements is reconciled to each count observation; ambiguous late/offline observations require recount before posting. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Snapshot plus timestamped movements is reconciled to each count observation; ambiguous late/offline observations require recount before posting. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-460 · `backend` · `M31·LIFE` · Variance approval
  - Depends on: INV-456, INV-457, INV-455.
  - Deliverable: Independent approval posts signed adjustments once; zero variance produces no movement and original observations remain immutable.
  - Acceptance: Independent approval posts signed adjustments once; zero variance produces no movement and original observations remain immutable. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Independent approval posts signed adjustments once; zero variance produces no movement and original observations remain immutable. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-461 · `design` · `M31·DESIGN` · Blind counts and reconciliation: screen design
  - Depends on: INV-457, INV-146.
  - Deliverable: Approve S-M31-01: list/work queue, detail/history and permitted action forms for Blind counts and reconciliation.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M31-01.

- [ ] INV-462 · `frontend` · `M31·BUILD` · Blind counts and reconciliation: accessible user workflows
  - Depends on: INV-456, INV-458, INV-459, INV-460, INV-461.
  - Deliverable: Build S-M31-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Blind counts and reconciliation feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M31-01.

- [ ] INV-463 · `backend` · `M31·NOTIFY` · Blind counts and reconciliation: actionable notifications
  - Depends on: INV-458, INV-459, INV-460.
  - Deliverable: Register m31.attention and m31.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-464 · `backend` · `M31·ADMIN` · Blind counts and reconciliation: administrative review controls
  - Depends on: INV-462.
  - Deliverable: Provide authorized history, exception review and safe recovery for Blind counts and reconciliation using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-465 · `backend` · `M31·AUDIT` · Blind counts and reconciliation: mutation evidence
  - Depends on: INV-458, INV-459, INV-460.
  - Deliverable: Declare audit actions for Blind and cycle counting, Moving-stock reconciliation, Variance approval; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-466 · `backend` · `M31·EVENTS` · Blind counts and reconciliation: versioned domain events
  - Depends on: INV-458, INV-459, INV-460.
  - Deliverable: Publish m31.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-467 · `backend` · `M31·PRIVACY` · Blind counts and reconciliation: data classification and retention
  - Depends on: INV-458, INV-459, INV-460.
  - Deliverable: Classify all fields in count_sessions, count_lines, count_movements, count_adjustments; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-468 · `backend` · `M31·INTEGRATION` · Blind counts and reconciliation: dependency integration
  - Depends on: INV-458, INV-459, INV-460, INV-456.
  - Deliverable: Exercise Blind counts and reconciliation with prerequisite modules M06, M20, M22 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-469 · `devops` · `M31·OPERABILITY` · Blind counts and reconciliation: runbook and failure signals
  - Depends on: INV-468.
  - Deliverable: Document deployment/configuration, metrics and recovery for Blind counts and reconciliation; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-470 · `qa` · `M31·QA` · Blind counts and reconciliation: acceptance and invariants
  - Depends on: INV-455, INV-456, INV-457, INV-458, INV-459, INV-460, INV-461, INV-462, INV-463, INV-464, INV-465, INV-466, INV-467, INV-468, INV-469.
  - Deliverable: Execute the feature acceptance suite for Blind counts and reconciliation, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Counter sees required identities but not system quantity; location schedules generate count assignments without duplicates. Snapshot plus timestamped movements is reconciled to each count observation; ambiguous late/offline observations require recount before posting. Independent approval posts signed adjustments once; zero variance produces no movement and original observations remain immutable. C05: Transfer discrepancy. Source decreases 20, destination increases 18, transit decreases only when receipt and scrap are posted; loss is two and conservation holds. C09: Blind count with moving stock. System reconciles observation-time movements; variance is not computed from a stale end balance; ambiguity requests recount; approved adjustment posts once.

## Phase 9 — Advanced warehouse and supply workflows

### M32 · Routes, putaway and cross-docking

- [ ] INV-471 · `backend` · `M32·DATA` · Routes, putaway and cross-docking: schema and migrations
  - Depends on: INV-260, INV-341, INV-374, INV-422, INV-390.
  - Deliverable: Create scoped tables warehouse_routes, route_steps, putaway_rules, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Routes, putaway and cross-docking. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-472 · `backend` · `M32·API` · Routes, putaway and cross-docking: request and response contracts
  - Depends on: INV-471.
  - Deliverable: Implement and document 7 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /warehouse-routes, POST /putaway-rules, POST /cross-dock-allocations, GET /warehouse-routes, GET /warehouse-routes/{id}, GET /putaway-rules, GET /putaway-rules/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-473 · `backend` · `M32·AUTHZ` · Routes, putaway and cross-docking: enforce access boundaries
  - Depends on: INV-471.
  - Deliverable: Enforce roles Warehouse supervisor and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Routes, putaway and cross-docking identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-474 · `backend` · `M32·LIFE` · Multi-step routes
  - Depends on: INV-472, INV-473, INV-471.
  - Deliverable: One/two/three-step inbound and outbound templates create dependent operations exactly once; activated route versions are snapshotted per operation.
  - Acceptance: One/two/three-step inbound and outbound templates create dependent operations exactly once; activated route versions are snapshotted per operation. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: One/two/three-step inbound and outbound templates create dependent operations exactly once; activated route versions are snapshotted per operation. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-475 · `backend` · `M32·LIFE` · Putaway and capacity
  - Depends on: INV-472, INV-473, INV-471.
  - Deliverable: Rules choose eligible destinations deterministically by priority and free capacity; no eligible destination creates an exception task.
  - Acceptance: Rules choose eligible destinations deterministically by priority and free capacity; no eligible destination creates an exception task. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Rules choose eligible destinations deterministically by priority and free capacity; no eligible destination creates an exception task. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-476 · `backend` · `M32·LIFE` · Cross-docking
  - Depends on: INV-472, INV-473, INV-471.
  - Deliverable: Incoming accepted stock can satisfy outbound demand without visiting storage while retaining reservation, ownership and inspection requirements.
  - Acceptance: Incoming accepted stock can satisfy outbound demand without visiting storage while retaining reservation, ownership and inspection requirements. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Incoming accepted stock can satisfy outbound demand without visiting storage while retaining reservation, ownership and inspection requirements. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-477 · `design` · `M32·DESIGN` · Routes, putaway and cross-docking: screen design
  - Depends on: INV-473, INV-146.
  - Deliverable: Approve S-M32-01: list/work queue, detail/history and permitted action forms for Routes, putaway and cross-docking.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M32-01.

- [ ] INV-478 · `frontend` · `M32·BUILD` · Routes, putaway and cross-docking: accessible user workflows
  - Depends on: INV-472, INV-474, INV-475, INV-476, INV-477.
  - Deliverable: Build S-M32-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Routes, putaway and cross-docking feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M32-01.

- [ ] INV-479 · `backend` · `M32·NOTIFY` · Routes, putaway and cross-docking: actionable notifications
  - Depends on: INV-474, INV-475, INV-476.
  - Deliverable: Register m32.attention and m32.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-480 · `backend` · `M32·ADMIN` · Routes, putaway and cross-docking: administrative review controls
  - Depends on: INV-478.
  - Deliverable: Provide authorized history, exception review and safe recovery for Routes, putaway and cross-docking using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-481 · `backend` · `M32·AUDIT` · Routes, putaway and cross-docking: mutation evidence
  - Depends on: INV-474, INV-475, INV-476.
  - Deliverable: Declare audit actions for Multi-step routes, Putaway and capacity, Cross-docking; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-482 · `backend` · `M32·EVENTS` · Routes, putaway and cross-docking: versioned domain events
  - Depends on: INV-474, INV-475, INV-476.
  - Deliverable: Publish m32.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-483 · `backend` · `M32·PRIVACY` · Routes, putaway and cross-docking: data classification and retention
  - Depends on: INV-474, INV-475, INV-476.
  - Deliverable: Classify all fields in warehouse_routes, route_steps, putaway_rules; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-484 · `backend` · `M32·INTEGRATION` · Routes, putaway and cross-docking: dependency integration
  - Depends on: INV-474, INV-475, INV-476, INV-472.
  - Deliverable: Exercise Routes, putaway and cross-docking with prerequisite modules M18, M23, M25, M28, M26 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-485 · `devops` · `M32·OPERABILITY` · Routes, putaway and cross-docking: runbook and failure signals
  - Depends on: INV-484.
  - Deliverable: Document deployment/configuration, metrics and recovery for Routes, putaway and cross-docking; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-486 · `qa` · `M32·QA` · Routes, putaway and cross-docking: acceptance and invariants
  - Depends on: INV-471, INV-472, INV-473, INV-474, INV-475, INV-476, INV-477, INV-478, INV-479, INV-480, INV-481, INV-482, INV-483, INV-484, INV-485.
  - Deliverable: Execute the feature acceptance suite for Routes, putaway and cross-docking, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: One/two/three-step inbound and outbound templates create dependent operations exactly once; activated route versions are snapshotted per operation. Rules choose eligible destinations deterministically by priority and free capacity; no eligible destination creates an exception task. Incoming accepted stock can satisfy outbound demand without visiting storage while retaining reservation, ownership and inspection requirements.

### M33 · Batch and wave picking

- [ ] INV-487 · `backend` · `M33·DATA` · Batch and wave picking: schema and migrations
  - Depends on: INV-422, INV-486.
  - Deliverable: Create scoped tables picking_waves, wave_tasks, pick_batches, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Batch and wave picking. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-488 · `backend` · `M33·API` · Batch and wave picking: request and response contracts
  - Depends on: INV-487.
  - Deliverable: Implement and document 7 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /picking-waves, POST /picking-waves/{id}/release, POST /pick-batches/{id}/assign, GET /picking-waves, GET /picking-waves/{id}, GET /pick-batches, GET /pick-batches/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-489 · `backend` · `M33·AUTHZ` · Batch and wave picking: enforce access boundaries
  - Depends on: INV-487.
  - Deliverable: Enforce roles Warehouse supervisor, Picker and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Batch and wave picking identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-490 · `backend` · `M33·LIFE` · Batch and wave formation
  - Depends on: INV-488, INV-489, INV-487.
  - Deliverable: Group compatible pick tasks within one warehouse and ownership boundary; a task belongs to only one active released batch.
  - Acceptance: Group compatible pick tasks within one warehouse and ownership boundary; a task belongs to only one active released batch. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Group compatible pick tasks within one warehouse and ownership boundary; a task belongs to only one active released batch. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-491 · `backend` · `M33·LIFE` · Picking strategies
  - Depends on: INV-488, INV-489, INV-487.
  - Deliverable: Support piece, batch and wave execution using configured FIFO/FEFO/nearest-location selection; costing method remains independent from physical selection.
  - Acceptance: Support piece, batch and wave execution using configured FIFO/FEFO/nearest-location selection; costing method remains independent from physical selection. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Support piece, batch and wave execution using configured FIFO/FEFO/nearest-location selection; costing method remains independent from physical selection. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-492 · `backend` · `M33·LIFE` · Replanning exceptions
  - Depends on: INV-488, INV-489, INV-487.
  - Deliverable: Short-picks and cancellations replan only uncompleted work without losing completed scan evidence.
  - Acceptance: Short-picks and cancellations replan only uncompleted work without losing completed scan evidence. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Short-picks and cancellations replan only uncompleted work without losing completed scan evidence. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-493 · `design` · `M33·DESIGN` · Batch and wave picking: screen design
  - Depends on: INV-489, INV-146.
  - Deliverable: Approve S-M33-01: list/work queue, detail/history and permitted action forms for Batch and wave picking.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M33-01.

- [ ] INV-494 · `frontend` · `M33·BUILD` · Batch and wave picking: accessible user workflows
  - Depends on: INV-488, INV-490, INV-491, INV-492, INV-493.
  - Deliverable: Build S-M33-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Batch and wave picking feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M33-01.

- [ ] INV-495 · `backend` · `M33·NOTIFY` · Batch and wave picking: actionable notifications
  - Depends on: INV-490, INV-491, INV-492.
  - Deliverable: Register m33.attention and m33.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-496 · `backend` · `M33·ADMIN` · Batch and wave picking: administrative review controls
  - Depends on: INV-494.
  - Deliverable: Provide authorized history, exception review and safe recovery for Batch and wave picking using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-497 · `backend` · `M33·AUDIT` · Batch and wave picking: mutation evidence
  - Depends on: INV-490, INV-491, INV-492.
  - Deliverable: Declare audit actions for Batch and wave formation, Picking strategies, Replanning exceptions; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-498 · `backend` · `M33·EVENTS` · Batch and wave picking: versioned domain events
  - Depends on: INV-490, INV-491, INV-492.
  - Deliverable: Publish m33.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-499 · `backend` · `M33·PRIVACY` · Batch and wave picking: data classification and retention
  - Depends on: INV-490, INV-491, INV-492.
  - Deliverable: Classify all fields in picking_waves, wave_tasks, pick_batches; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-500 · `backend` · `M33·INTEGRATION` · Batch and wave picking: dependency integration
  - Depends on: INV-490, INV-491, INV-492, INV-488.
  - Deliverable: Exercise Batch and wave picking with prerequisite modules M28, M32 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-501 · `devops` · `M33·OPERABILITY` · Batch and wave picking: runbook and failure signals
  - Depends on: INV-500.
  - Deliverable: Document deployment/configuration, metrics and recovery for Batch and wave picking; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-502 · `qa` · `M33·QA` · Batch and wave picking: acceptance and invariants
  - Depends on: INV-487, INV-488, INV-489, INV-490, INV-491, INV-492, INV-493, INV-494, INV-495, INV-496, INV-497, INV-498, INV-499, INV-500, INV-501.
  - Deliverable: Execute the feature acceptance suite for Batch and wave picking, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Group compatible pick tasks within one warehouse and ownership boundary; a task belongs to only one active released batch. Support piece, batch and wave execution using configured FIFO/FEFO/nearest-location selection; costing method remains independent from physical selection. Short-picks and cancellations replan only uncompleted work without losing completed scan evidence.

### M34 · Replenishment and demand planning

- [ ] INV-503 · `backend` · `M34·DATA` · Replenishment and demand planning: schema and migrations
  - Depends on: INV-309, INV-358, INV-486.
  - Deliverable: Create scoped tables reorder_rules, replenishment_suggestions, internal_replenishments, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Replenishment and demand planning. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-504 · `backend` · `M34·API` · Replenishment and demand planning: request and response contracts
  - Depends on: INV-503.
  - Deliverable: Implement and document 8 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /reorder-rules, POST /replenishment/run, POST /replenishment/{id}/accept, GET /stock/shortages, GET /reorder-rules, GET /reorder-rules/{id}, GET /replenishment, GET /replenishment/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-505 · `backend` · `M34·AUTHZ` · Replenishment and demand planning: enforce access boundaries
  - Depends on: INV-503.
  - Deliverable: Enforce roles Buyer, Warehouse supervisor and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Replenishment and demand planning identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-506 · `backend` · `M34·LIFE` · Min-max and safety stock
  - Depends on: INV-504, INV-505, INV-503.
  - Deliverable: Dated forecast below minimum suggests replenishment to maximum with purchase multiples, lead time and explicit safety buffer.
  - Acceptance: Dated forecast below minimum suggests replenishment to maximum with purchase multiples, lead time and explicit safety buffer. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Dated forecast below minimum suggests replenishment to maximum with purchase multiples, lead time and explicit safety buffer. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-507 · `backend` · `M34·LIFE` · Buyer approval
  - Depends on: INV-504, INV-505, INV-503.
  - Deliverable: Accepted suggestion creates a draft requisition or PO for normal approval; rerunning planning does not duplicate existing supply.
  - Acceptance: Accepted suggestion creates a draft requisition or PO for normal approval; rerunning planning does not duplicate existing supply. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Accepted suggestion creates a draft requisition or PO for normal approval; rerunning planning does not duplicate existing supply. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-508 · `backend` · `M34·LIFE` · Pick-face replenishment
  - Depends on: INV-504, INV-505, INV-503.
  - Deliverable: Bin replenishment moves eligible reserve stock to pick locations and reports shortages without generating impossible transfers.
  - Acceptance: Bin replenishment moves eligible reserve stock to pick locations and reports shortages without generating impossible transfers. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Bin replenishment moves eligible reserve stock to pick locations and reports shortages without generating impossible transfers. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-509 · `design` · `M34·DESIGN` · Replenishment and demand planning: screen design
  - Depends on: INV-505, INV-146.
  - Deliverable: Approve S-M34-01: list/work queue, detail/history and permitted action forms for Replenishment and demand planning.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M34-01.

- [ ] INV-510 · `frontend` · `M34·BUILD` · Replenishment and demand planning: accessible user workflows
  - Depends on: INV-504, INV-506, INV-507, INV-508, INV-509.
  - Deliverable: Build S-M34-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Replenishment and demand planning feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M34-01.

- [ ] INV-511 · `backend` · `M34·NOTIFY` · Replenishment and demand planning: actionable notifications
  - Depends on: INV-506, INV-507, INV-508.
  - Deliverable: Register m34.attention and m34.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-512 · `backend` · `M34·ADMIN` · Replenishment and demand planning: administrative review controls
  - Depends on: INV-510.
  - Deliverable: Provide authorized history, exception review and safe recovery for Replenishment and demand planning using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-513 · `backend` · `M34·AUDIT` · Replenishment and demand planning: mutation evidence
  - Depends on: INV-506, INV-507, INV-508.
  - Deliverable: Declare audit actions for Min-max and safety stock, Buyer approval, Pick-face replenishment; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-514 · `backend` · `M34·EVENTS` · Replenishment and demand planning: versioned domain events
  - Depends on: INV-506, INV-507, INV-508.
  - Deliverable: Publish m34.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-515 · `backend` · `M34·PRIVACY` · Replenishment and demand planning: data classification and retention
  - Depends on: INV-506, INV-507, INV-508.
  - Deliverable: Classify all fields in reorder_rules, replenishment_suggestions, internal_replenishments; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-516 · `backend` · `M34·INTEGRATION` · Replenishment and demand planning: dependency integration
  - Depends on: INV-506, INV-507, INV-508, INV-504.
  - Deliverable: Exercise Replenishment and demand planning with prerequisite modules M21, M24, M32 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-517 · `devops` · `M34·OPERABILITY` · Replenishment and demand planning: runbook and failure signals
  - Depends on: INV-516.
  - Deliverable: Document deployment/configuration, metrics and recovery for Replenishment and demand planning; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-518 · `qa` · `M34·QA` · Replenishment and demand planning: acceptance and invariants
  - Depends on: INV-503, INV-504, INV-505, INV-506, INV-507, INV-508, INV-509, INV-510, INV-511, INV-512, INV-513, INV-514, INV-515, INV-516, INV-517.
  - Deliverable: Execute the feature acceptance suite for Replenishment and demand planning, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Dated forecast below minimum suggests replenishment to maximum with purchase multiples, lead time and explicit safety buffer. Accepted suggestion creates a draft requisition or PO for normal approval; rerunning planning does not duplicate existing supply. Bin replenishment moves eligible reserve stock to pick locations and reports shortages without generating impossible transfers. C18: Forecast without double counting. Available is 70; forecast at receipt horizon is 80, not 50; unconfirmed suggestions do not count as supply.

### M35 · Consignment and owner-separated stock

- [ ] INV-519 · `backend` · `M35·DATA` · Consignment and owner-separated stock: schema and migrations
  - Depends on: INV-211, INV-276, INV-293, INV-422.
  - Deliverable: Create scoped tables consignment_agreements, ownership_changes, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Consignment and owner-separated stock. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-520 · `backend` · `M35·API` · Consignment and owner-separated stock: request and response contracts
  - Depends on: INV-519.
  - Deliverable: Implement and document 7 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /consignment-agreements, POST /stock/ownership-changes, GET /stock/by-owner, GET /consignment-agreements, GET /consignment-agreements/{id}, GET /stock/ownership-changes, GET /stock/ownership-changes/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-521 · `backend` · `M35·AUTHZ` · Consignment and owner-separated stock: enforce access boundaries
  - Depends on: INV-519.
  - Deliverable: Enforce roles Buyer, Warehouse supervisor and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Consignment and owner-separated stock identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-522 · `backend` · `M35·LIFE` · Consignment custody
  - Depends on: INV-520, INV-521, INV-519.
  - Deliverable: Partner-owned stock appears in custody quantities but is excluded from company-owned value and unavailable to unrelated owner demand.
  - Acceptance: Partner-owned stock appears in custody quantities but is excluded from company-owned value and unavailable to unrelated owner demand. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Partner-owned stock appears in custody quantities but is excluded from company-owned value and unavailable to unrelated owner demand. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-523 · `backend` · `M35·LIFE` · Ownership acquisition
  - Depends on: INV-520, INV-521, INV-519.
  - Deliverable: Approved acquisition changes ownership through paired ledger movements and a documented cost basis; custody location need not change.
  - Acceptance: Approved acquisition changes ownership through paired ledger movements and a documented cost basis; custody location need not change. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Approved acquisition changes ownership through paired ledger movements and a documented cost basis; custody location need not change. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-524 · `backend` · `M35·LIFE` · Owner returns
  - Depends on: INV-520, INV-521, INV-519.
  - Deliverable: Unsold consignment returns to its owner without treating it as a company-owned inventory sale.
  - Acceptance: Unsold consignment returns to its owner without treating it as a company-owned inventory sale. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Unsold consignment returns to its owner without treating it as a company-owned inventory sale. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-525 · `design` · `M35·DESIGN` · Consignment and owner-separated stock: screen design
  - Depends on: INV-521, INV-146.
  - Deliverable: Approve S-M35-01: list/work queue, detail/history and permitted action forms for Consignment and owner-separated stock.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M35-01.

- [ ] INV-526 · `frontend` · `M35·BUILD` · Consignment and owner-separated stock: accessible user workflows
  - Depends on: INV-520, INV-522, INV-523, INV-524, INV-525.
  - Deliverable: Build S-M35-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Consignment and owner-separated stock feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M35-01.

- [ ] INV-527 · `backend` · `M35·NOTIFY` · Consignment and owner-separated stock: actionable notifications
  - Depends on: INV-522, INV-523, INV-524.
  - Deliverable: Register m35.attention and m35.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-528 · `backend` · `M35·ADMIN` · Consignment and owner-separated stock: administrative review controls
  - Depends on: INV-526.
  - Deliverable: Provide authorized history, exception review and safe recovery for Consignment and owner-separated stock using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-529 · `backend` · `M35·AUDIT` · Consignment and owner-separated stock: mutation evidence
  - Depends on: INV-522, INV-523, INV-524.
  - Deliverable: Declare audit actions for Consignment custody, Ownership acquisition, Owner returns; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-530 · `backend` · `M35·EVENTS` · Consignment and owner-separated stock: versioned domain events
  - Depends on: INV-522, INV-523, INV-524.
  - Deliverable: Publish m35.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-531 · `backend` · `M35·PRIVACY` · Consignment and owner-separated stock: data classification and retention
  - Depends on: INV-522, INV-523, INV-524.
  - Deliverable: Classify all fields in consignment_agreements, ownership_changes; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-532 · `backend` · `M35·INTEGRATION` · Consignment and owner-separated stock: dependency integration
  - Depends on: INV-522, INV-523, INV-524, INV-520.
  - Deliverable: Exercise Consignment and owner-separated stock with prerequisite modules M15, M19, M20, M28 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-533 · `devops` · `M35·OPERABILITY` · Consignment and owner-separated stock: runbook and failure signals
  - Depends on: INV-532.
  - Deliverable: Document deployment/configuration, metrics and recovery for Consignment and owner-separated stock; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-534 · `qa` · `M35·QA` · Consignment and owner-separated stock: acceptance and invariants
  - Depends on: INV-519, INV-520, INV-521, INV-522, INV-523, INV-524, INV-525, INV-526, INV-527, INV-528, INV-529, INV-530, INV-531, INV-532, INV-533.
  - Deliverable: Execute the feature acceptance suite for Consignment and owner-separated stock, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Partner-owned stock appears in custody quantities but is excluded from company-owned value and unavailable to unrelated owner demand. Approved acquisition changes ownership through paired ledger movements and a documented cost basis; custody location need not change. Unsold consignment returns to its owner without treating it as a company-owned inventory sale.

### M36 · Dropship fulfillment

- [ ] INV-535 · `backend` · `M36·DATA` · Dropship fulfillment: schema and migrations
  - Depends on: INV-358, INV-406.
  - Deliverable: Create scoped tables dropship_links, dropship_confirmations, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Dropship fulfillment. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-536 · `backend` · `M36·API` · Dropship fulfillment: request and response contracts
  - Depends on: INV-535.
  - Deliverable: Implement and document 4 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /sales/orders/{id}/dropship, POST /dropships/{id}/confirm, GET /dropships, GET /dropships/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-537 · `backend` · `M36·AUTHZ` · Dropship fulfillment: enforce access boundaries
  - Depends on: INV-535.
  - Deliverable: Enforce roles Buyer, Sales clerk and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Dropship fulfillment identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-538 · `backend` · `M36·LIFE` · Linked supplier fulfillment
  - Depends on: INV-536, INV-537, INV-535.
  - Deliverable: Eligible sales demand creates linked purchase demand without reserving warehouse stock.
  - Acceptance: Eligible sales demand creates linked purchase demand without reserving warehouse stock. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Eligible sales demand creates linked purchase demand without reserving warehouse stock. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-539 · `backend` · `M36·LIFE` · Supplier delivery evidence
  - Depends on: INV-536, INV-537, INV-535.
  - Deliverable: Confirmation updates fulfillment and external-location movement history exactly once; internal on-hand remains unchanged.
  - Acceptance: Confirmation updates fulfillment and external-location movement history exactly once; internal on-hand remains unchanged. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Confirmation updates fulfillment and external-location movement history exactly once; internal on-hand remains unchanged. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-540 · `backend` · `M36·LIFE` · Dropship returns
  - Depends on: INV-536, INV-537, INV-535.
  - Deliverable: Return authorization records supplier/customer routing and ownership without manufacturing a warehouse receipt.
  - Acceptance: Return authorization records supplier/customer routing and ownership without manufacturing a warehouse receipt. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Return authorization records supplier/customer routing and ownership without manufacturing a warehouse receipt. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-541 · `design` · `M36·DESIGN` · Dropship fulfillment: screen design
  - Depends on: INV-537, INV-146.
  - Deliverable: Approve S-M36-01: list/work queue, detail/history and permitted action forms for Dropship fulfillment.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M36-01.

- [ ] INV-542 · `frontend` · `M36·BUILD` · Dropship fulfillment: accessible user workflows
  - Depends on: INV-536, INV-538, INV-539, INV-540, INV-541.
  - Deliverable: Build S-M36-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Dropship fulfillment feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M36-01.

- [ ] INV-543 · `backend` · `M36·NOTIFY` · Dropship fulfillment: actionable notifications
  - Depends on: INV-538, INV-539, INV-540.
  - Deliverable: Register m36.attention and m36.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-544 · `backend` · `M36·ADMIN` · Dropship fulfillment: administrative review controls
  - Depends on: INV-542.
  - Deliverable: Provide authorized history, exception review and safe recovery for Dropship fulfillment using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-545 · `backend` · `M36·AUDIT` · Dropship fulfillment: mutation evidence
  - Depends on: INV-538, INV-539, INV-540.
  - Deliverable: Declare audit actions for Linked supplier fulfillment, Supplier delivery evidence, Dropship returns; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-546 · `backend` · `M36·EVENTS` · Dropship fulfillment: versioned domain events
  - Depends on: INV-538, INV-539, INV-540.
  - Deliverable: Publish m36.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-547 · `backend` · `M36·PRIVACY` · Dropship fulfillment: data classification and retention
  - Depends on: INV-538, INV-539, INV-540.
  - Deliverable: Classify all fields in dropship_links, dropship_confirmations; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-548 · `backend` · `M36·INTEGRATION` · Dropship fulfillment: dependency integration
  - Depends on: INV-538, INV-539, INV-540, INV-536.
  - Deliverable: Exercise Dropship fulfillment with prerequisite modules M24, M27 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-549 · `devops` · `M36·OPERABILITY` · Dropship fulfillment: runbook and failure signals
  - Depends on: INV-548.
  - Deliverable: Document deployment/configuration, metrics and recovery for Dropship fulfillment; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-550 · `qa` · `M36·QA` · Dropship fulfillment: acceptance and invariants
  - Depends on: INV-535, INV-536, INV-537, INV-538, INV-539, INV-540, INV-541, INV-542, INV-543, INV-544, INV-545, INV-546, INV-547, INV-548, INV-549.
  - Deliverable: Execute the feature acceptance suite for Dropship fulfillment, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Eligible sales demand creates linked purchase demand without reserving warehouse stock. Confirmation updates fulfillment and external-location movement history exactly once; internal on-hand remains unchanged. Return authorization records supplier/customer routing and ownership without manufacturing a warehouse receipt.

### M37 · Intercompany trade and transfers

- [ ] INV-551 · `backend` · `M37·DATA` · Intercompany trade and transfers: schema and migrations
  - Depends on: INV-195, INV-341, INV-358, INV-406.
  - Deliverable: Create scoped tables intercompany_links, intercompany_shipments, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Intercompany trade and transfers. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-552 · `backend` · `M37·API` · Intercompany trade and transfers: request and response contracts
  - Depends on: INV-551.
  - Deliverable: Implement and document 5 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /intercompany/orders, POST /intercompany/{id}/approve, GET /intercompany/{id}/reconciliation, GET /intercompany, GET /intercompany/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-553 · `backend` · `M37·AUTHZ` · Intercompany trade and transfers: enforce access boundaries
  - Depends on: INV-551.
  - Deliverable: Enforce roles Company admin, Buyer, Sales manager and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Intercompany trade and transfers identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-554 · `backend` · `M37·LIFE` · Paired commercial documents
  - Depends on: INV-552, INV-553, INV-551.
  - Deliverable: Within one tenant, approved intercompany requests create linked sale/purchase documents with explicit currencies and prices.
  - Acceptance: Within one tenant, approved intercompany requests create linked sale/purchase documents with explicit currencies and prices. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Within one tenant, approved intercompany requests create linked sale/purchase documents with explicit currencies and prices. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-555 · `backend` · `M37·LIFE` · Company-local ledgers
  - Depends on: INV-552, INV-553, INV-551.
  - Deliverable: Shipment and receipt use each company ledger and base currency; buyer receipt is not posted before physical receipt.
  - Acceptance: Shipment and receipt use each company ledger and base currency; buyer receipt is not posted before physical receipt. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Shipment and receipt use each company ledger and base currency; buyer receipt is not posted before physical receipt. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-556 · `backend` · `M37·LIFE` · Independent permissions
  - Depends on: INV-552, INV-553, INV-551.
  - Deliverable: Users require explicit rights in each company for paired actions; no cross-tenant automatic trading is permitted in baseline.
  - Acceptance: Users require explicit rights in each company for paired actions; no cross-tenant automatic trading is permitted in baseline. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Users require explicit rights in each company for paired actions; no cross-tenant automatic trading is permitted in baseline. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-557 · `design` · `M37·DESIGN` · Intercompany trade and transfers: screen design
  - Depends on: INV-553, INV-146.
  - Deliverable: Approve S-M37-01: list/work queue, detail/history and permitted action forms for Intercompany trade and transfers.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M37-01.

- [ ] INV-558 · `frontend` · `M37·BUILD` · Intercompany trade and transfers: accessible user workflows
  - Depends on: INV-552, INV-554, INV-555, INV-556, INV-557.
  - Deliverable: Build S-M37-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Intercompany trade and transfers feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M37-01.

- [ ] INV-559 · `backend` · `M37·NOTIFY` · Intercompany trade and transfers: actionable notifications
  - Depends on: INV-554, INV-555, INV-556.
  - Deliverable: Register m37.attention and m37.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-560 · `backend` · `M37·ADMIN` · Intercompany trade and transfers: administrative review controls
  - Depends on: INV-558.
  - Deliverable: Provide authorized history, exception review and safe recovery for Intercompany trade and transfers using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-561 · `backend` · `M37·AUDIT` · Intercompany trade and transfers: mutation evidence
  - Depends on: INV-554, INV-555, INV-556.
  - Deliverable: Declare audit actions for Paired commercial documents, Company-local ledgers, Independent permissions; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-562 · `backend` · `M37·EVENTS` · Intercompany trade and transfers: versioned domain events
  - Depends on: INV-554, INV-555, INV-556.
  - Deliverable: Publish m37.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-563 · `backend` · `M37·PRIVACY` · Intercompany trade and transfers: data classification and retention
  - Depends on: INV-554, INV-555, INV-556.
  - Deliverable: Classify all fields in intercompany_links, intercompany_shipments; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-564 · `backend` · `M37·INTEGRATION` · Intercompany trade and transfers: dependency integration
  - Depends on: INV-554, INV-555, INV-556, INV-552.
  - Deliverable: Exercise Intercompany trade and transfers with prerequisite modules M14, M23, M24, M27 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-565 · `devops` · `M37·OPERABILITY` · Intercompany trade and transfers: runbook and failure signals
  - Depends on: INV-564.
  - Deliverable: Document deployment/configuration, metrics and recovery for Intercompany trade and transfers; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-566 · `qa` · `M37·QA` · Intercompany trade and transfers: acceptance and invariants
  - Depends on: INV-551, INV-552, INV-553, INV-554, INV-555, INV-556, INV-557, INV-558, INV-559, INV-560, INV-561, INV-562, INV-563, INV-564, INV-565.
  - Deliverable: Execute the feature acceptance suite for Intercompany trade and transfers, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Within one tenant, approved intercompany requests create linked sale/purchase documents with explicit currencies and prices. Shipment and receipt use each company ledger and base currency; buyer receipt is not posted before physical receipt. Users require explicit rights in each company for paired actions; no cross-tenant automatic trading is permitted in baseline.

### M38 · Kits without manufacturing

- [ ] INV-567 · `backend` · `M38·DATA` · Kits without manufacturing: schema and migrations
  - Depends on: INV-228, INV-309, INV-422.
  - Deliverable: Create scoped tables kit_definitions, kit_components, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Kits without manufacturing. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-568 · `backend` · `M38·API` · Kits without manufacturing: request and response contracts
  - Depends on: INV-567.
  - Deliverable: Implement and document 6 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /kits, POST /kits/{id}/activate, GET /kits/{id}/availability, GET /kits, GET /kits/{id}, PATCH /kits/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-569 · `backend` · `M38·AUTHZ` · Kits without manufacturing: enforce access boundaries
  - Depends on: INV-567.
  - Deliverable: Enforce roles Catalog manager, Sales clerk and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Kits without manufacturing identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-570 · `backend` · `M38·LIFE` · Phantom kit definitions
  - Depends on: INV-568, INV-569, INV-567.
  - Deliverable: Versioned kits explode into stock components; cyclic/nested definitions are validated and no manufactured finished-stock balance is created.
  - Acceptance: Versioned kits explode into stock components; cyclic/nested definitions are validated and no manufactured finished-stock balance is created. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Versioned kits explode into stock components; cyclic/nested definitions are validated and no manufactured finished-stock balance is created. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-571 · `backend` · `M38·LIFE` · Kit allocation and fulfillment
  - Depends on: INV-568, INV-569, INV-567.
  - Deliverable: Available kits equal the limiting component quantity; partial-kit dispatch is blocked unless order is explicitly revised to components.
  - Acceptance: Available kits equal the limiting component quantity; partial-kit dispatch is blocked unless order is explicitly revised to components. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Available kits equal the limiting component quantity; partial-kit dispatch is blocked unless order is explicitly revised to components. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-572 · `backend` · `M38·LIFE` · Kit returns
  - Depends on: INV-568, INV-569, INV-567.
  - Deliverable: Return evidence identifies actual components and original allocation costs rather than inventing a kit valuation layer.
  - Acceptance: Return evidence identifies actual components and original allocation costs rather than inventing a kit valuation layer. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Return evidence identifies actual components and original allocation costs rather than inventing a kit valuation layer. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-573 · `design` · `M38·DESIGN` · Kits without manufacturing: screen design
  - Depends on: INV-569, INV-146.
  - Deliverable: Approve S-M38-01: list/work queue, detail/history and permitted action forms for Kits without manufacturing.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M38-01.

- [ ] INV-574 · `frontend` · `M38·BUILD` · Kits without manufacturing: accessible user workflows
  - Depends on: INV-568, INV-570, INV-571, INV-572, INV-573.
  - Deliverable: Build S-M38-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Kits without manufacturing feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M38-01.

- [ ] INV-575 · `backend` · `M38·NOTIFY` · Kits without manufacturing: actionable notifications
  - Depends on: INV-570, INV-571, INV-572.
  - Deliverable: Register m38.attention and m38.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-576 · `backend` · `M38·ADMIN` · Kits without manufacturing: administrative review controls
  - Depends on: INV-574.
  - Deliverable: Provide authorized history, exception review and safe recovery for Kits without manufacturing using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-577 · `backend` · `M38·AUDIT` · Kits without manufacturing: mutation evidence
  - Depends on: INV-570, INV-571, INV-572.
  - Deliverable: Declare audit actions for Phantom kit definitions, Kit allocation and fulfillment, Kit returns; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-578 · `backend` · `M38·EVENTS` · Kits without manufacturing: versioned domain events
  - Depends on: INV-570, INV-571, INV-572.
  - Deliverable: Publish m38.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-579 · `backend` · `M38·PRIVACY` · Kits without manufacturing: data classification and retention
  - Depends on: INV-570, INV-571, INV-572.
  - Deliverable: Classify all fields in kit_definitions, kit_components; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-580 · `backend` · `M38·INTEGRATION` · Kits without manufacturing: dependency integration
  - Depends on: INV-570, INV-571, INV-572, INV-568.
  - Deliverable: Exercise Kits without manufacturing with prerequisite modules M16, M21, M28 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-581 · `devops` · `M38·OPERABILITY` · Kits without manufacturing: runbook and failure signals
  - Depends on: INV-580.
  - Deliverable: Document deployment/configuration, metrics and recovery for Kits without manufacturing; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-582 · `qa` · `M38·QA` · Kits without manufacturing: acceptance and invariants
  - Depends on: INV-567, INV-568, INV-569, INV-570, INV-571, INV-572, INV-573, INV-574, INV-575, INV-576, INV-577, INV-578, INV-579, INV-580, INV-581.
  - Deliverable: Execute the feature acceptance suite for Kits without manufacturing, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Versioned kits explode into stock components; cyclic/nested definitions are validated and no manufactured finished-stock balance is created. Available kits equal the limiting component quantity; partial-kit dispatch is blocked unless order is explicitly revised to components. Return evidence identifies actual components and original allocation costs rather than inventing a kit valuation layer.

## Phase 10 — Warehouse Android and hardware

### M39 · Offline Android warehouse workflows

- [ ] INV-583 · `backend` · `M39·DATA` · Offline Android warehouse workflows: schema and migrations
  - Depends on: INV-179, INV-374, INV-422, INV-454, INV-470, INV-502.
  - Deliverable: Create scoped tables mobile_assignments, sync_conflicts, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Offline Android warehouse workflows. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-584 · `backend` · `M39·API` · Offline Android warehouse workflows: request and response contracts
  - Depends on: INV-583.
  - Deliverable: Implement and document 6 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: GET /mobile/assignments, POST /mobile/conflicts/{id}/resolve, POST /mobile/assignments/{id}/acknowledge, GET /mobile/assignments/{id}, GET /mobile/conflicts, GET /mobile/conflicts/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-585 · `backend` · `M39·AUTHZ` · Offline Android warehouse workflows: enforce access boundaries
  - Depends on: INV-583.
  - Deliverable: Enforce roles Warehouse operator, Counter and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Offline Android warehouse workflows identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-586 · `backend` · `M39·LIFE` · Offline operational capture
  - Depends on: INV-584, INV-585, INV-583.
  - Deliverable: Receipt, transfer, pick, pack and count observations queue durably with source document version and command dependencies.
  - Acceptance: Receipt, transfer, pick, pack and count observations queue durably with source document version and command dependencies. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Receipt, transfer, pick, pack and count observations queue durably with source document version and command dependencies. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-587 · `backend` · `M39·LIFE` · Conflict review
  - Depends on: INV-584, INV-585, INV-583.
  - Deliverable: Insufficient stock, revoked permissions, changed documents and expired task leases create explicit actionable conflicts; stock quantities never use last-write-wins.
  - Acceptance: Insufficient stock, revoked permissions, changed documents and expired task leases create explicit actionable conflicts; stock quantities never use last-write-wins. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Insufficient stock, revoked permissions, changed documents and expired task leases create explicit actionable conflicts; stock quantities never use last-write-wins. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-588 · `backend` · `M39·LIFE` · Reconnect recovery
  - Depends on: INV-584, INV-585, INV-583.
  - Deliverable: Airplane mode, process death, duplicated batches and intermittent acknowledgements produce one committed operation or one visible unresolved conflict.
  - Acceptance: Airplane mode, process death, duplicated batches and intermittent acknowledgements produce one committed operation or one visible unresolved conflict. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Airplane mode, process death, duplicated batches and intermittent acknowledgements produce one committed operation or one visible unresolved conflict. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-589 · `design` · `M39·DESIGN` · Offline Android warehouse workflows: screen design
  - Depends on: INV-585, INV-146.
  - Deliverable: Approve S-M39-01: list/work queue, detail/history and permitted action forms for Offline Android warehouse workflows.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M39-01.

- [ ] INV-590 · `mobile` · `M39·BUILD` · Offline Android warehouse workflows: accessible user workflows
  - Depends on: INV-584, INV-586, INV-587, INV-588, INV-589.
  - Deliverable: Build S-M39-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Offline Android warehouse workflows feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M39-01.

- [ ] INV-591 · `backend` · `M39·NOTIFY` · Offline Android warehouse workflows: actionable notifications
  - Depends on: INV-586, INV-587, INV-588.
  - Deliverable: Register m39.attention and m39.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-592 · `backend` · `M39·ADMIN` · Offline Android warehouse workflows: administrative review controls
  - Depends on: INV-590.
  - Deliverable: Provide authorized history, exception review and safe recovery for Offline Android warehouse workflows using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-593 · `backend` · `M39·AUDIT` · Offline Android warehouse workflows: mutation evidence
  - Depends on: INV-586, INV-587, INV-588.
  - Deliverable: Declare audit actions for Offline operational capture, Conflict review, Reconnect recovery; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-594 · `backend` · `M39·EVENTS` · Offline Android warehouse workflows: versioned domain events
  - Depends on: INV-586, INV-587, INV-588.
  - Deliverable: Publish m39.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-595 · `backend` · `M39·PRIVACY` · Offline Android warehouse workflows: data classification and retention
  - Depends on: INV-586, INV-587, INV-588.
  - Deliverable: Classify all fields in mobile_assignments, sync_conflicts; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-596 · `backend` · `M39·INTEGRATION` · Offline Android warehouse workflows: dependency integration
  - Depends on: INV-586, INV-587, INV-588, INV-584.
  - Deliverable: Exercise Offline Android warehouse workflows with prerequisite modules M13, M25, M28, M30, M31, M33 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-597 · `backend` · `M39·OFFLINE` · Offline Android warehouse workflows: interrupted-device recovery
  - Depends on: INV-590, INV-596.
  - Deliverable: Validate durable queue and cached state for Offline Android warehouse workflows against OFFLINE_SYNC.md.
  - Acceptance: Process death and acknowledgement loss never duplicate a command. Conflicts remain visible; stale authorization cannot commit offline-captured changes.
  - Tests: Airplane mode; reboot; duplicate batch; stale version; revoked device; cursor reset.

- [ ] INV-598 · `devops` · `M39·OPERABILITY` · Offline Android warehouse workflows: runbook and failure signals
  - Depends on: INV-596.
  - Deliverable: Document deployment/configuration, metrics and recovery for Offline Android warehouse workflows; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-599 · `qa` · `M39·QA` · Offline Android warehouse workflows: acceptance and invariants
  - Depends on: INV-583, INV-584, INV-585, INV-586, INV-587, INV-588, INV-589, INV-590, INV-591, INV-592, INV-593, INV-594, INV-595, INV-596, INV-597, INV-598.
  - Deliverable: Execute the feature acceptance suite for Offline Android warehouse workflows, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Receipt, transfer, pick, pack and count observations queue durably with source document version and command dependencies. Insufficient stock, revoked permissions, changed documents and expired task leases create explicit actionable conflicts; stock quantities never use last-write-wins. Airplane mode, process death, duplicated batches and intermittent acknowledgements produce one committed operation or one visible unresolved conflict. C14: Offline lifecycle. Queue survives encrypted; unacknowledged work stays pending; stale version and revoked authorization conflict; no last-write-wins or duplicate stock.

### M40 · Scanners, labels and printer interfaces

- [ ] INV-600 · `backend` · `M40·DATA` · Scanners, labels and printer interfaces: schema and migrations
  - Depends on: INV-228, INV-276, INV-422, INV-599.
  - Deliverable: Create scoped tables label_templates, print_jobs, scanner_profiles, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Scanners, labels and printer interfaces. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-601 · `backend` · `M40·API` · Scanners, labels and printer interfaces: request and response contracts
  - Depends on: INV-600.
  - Deliverable: Implement and document 8 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /labels/preview, POST /print-jobs, POST /print-jobs/{id}/reprint, GET /print-jobs, GET /print-jobs/{id}, GET /label-templates, GET /label-templates/{id}, POST /label-templates. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-602 · `backend` · `M40·AUTHZ` · Scanners, labels and printer interfaces: enforce access boundaries
  - Depends on: INV-600.
  - Deliverable: Enforce roles Warehouse operator, Warehouse supervisor and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Scanners, labels and printer interfaces identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-603 · `backend` · `M40·LIFE` · Camera and handheld scanning
  - Depends on: INV-601, INV-602, INV-600.
  - Deliverable: Camera, keyboard-wedge and Android intent scanner adapters normalize input without dropping GS1 separators or leading zeroes.
  - Acceptance: Camera, keyboard-wedge and Android intent scanner adapters normalize input without dropping GS1 separators or leading zeroes. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Camera, keyboard-wedge and Android intent scanner adapters normalize input without dropping GS1 separators or leading zeroes. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-604 · `backend` · `M40·LIFE` · GS1 parsing
  - Depends on: INV-601, INV-602, INV-600.
  - Deliverable: Parse GTIN, lot, serial and expiry application identifiers with length/check-digit validation; internal labels never impersonate assigned GS1 company prefixes.
  - Acceptance: Parse GTIN, lot, serial and expiry application identifiers with length/check-digit validation; internal labels never impersonate assigned GS1 company prefixes. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Parse GTIN, lot, serial and expiry application identifiers with length/check-digit validation; internal labels never impersonate assigned GS1 company prefixes. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-605 · `backend` · `M40·LIFE` · Label generation and reprints
  - Depends on: INV-601, INV-602, INV-600.
  - Deliverable: PDF and ZPL interfaces support product, bin, lot and package labels; retries/reprints preserve entity IDs and are logged.
  - Acceptance: PDF and ZPL interfaces support product, bin, lot and package labels; retries/reprints preserve entity IDs and are logged. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: PDF and ZPL interfaces support product, bin, lot and package labels; retries/reprints preserve entity IDs and are logged. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-606 · `design` · `M40·DESIGN` · Scanners, labels and printer interfaces: screen design
  - Depends on: INV-602, INV-146.
  - Deliverable: Approve S-M40-01: list/work queue, detail/history and permitted action forms for Scanners, labels and printer interfaces.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M40-01.

- [ ] INV-607 · `mobile` · `M40·BUILD` · Scanners, labels and printer interfaces: accessible user workflows
  - Depends on: INV-601, INV-603, INV-604, INV-605, INV-606.
  - Deliverable: Build S-M40-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Scanners, labels and printer interfaces feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M40-01.

- [ ] INV-608 · `backend` · `M40·NOTIFY` · Scanners, labels and printer interfaces: actionable notifications
  - Depends on: INV-603, INV-604, INV-605.
  - Deliverable: Register m40.attention and m40.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-609 · `backend` · `M40·ADMIN` · Scanners, labels and printer interfaces: administrative review controls
  - Depends on: INV-607.
  - Deliverable: Provide authorized history, exception review and safe recovery for Scanners, labels and printer interfaces using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-610 · `backend` · `M40·AUDIT` · Scanners, labels and printer interfaces: mutation evidence
  - Depends on: INV-603, INV-604, INV-605.
  - Deliverable: Declare audit actions for Camera and handheld scanning, GS1 parsing, Label generation and reprints; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-611 · `backend` · `M40·EVENTS` · Scanners, labels and printer interfaces: versioned domain events
  - Depends on: INV-603, INV-604, INV-605.
  - Deliverable: Publish m40.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-612 · `backend` · `M40·PRIVACY` · Scanners, labels and printer interfaces: data classification and retention
  - Depends on: INV-603, INV-604, INV-605.
  - Deliverable: Classify all fields in label_templates, print_jobs, scanner_profiles; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-613 · `backend` · `M40·INTEGRATION` · Scanners, labels and printer interfaces: dependency integration
  - Depends on: INV-603, INV-604, INV-605, INV-601.
  - Deliverable: Exercise Scanners, labels and printer interfaces with prerequisite modules M16, M19, M28, M39 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-614 · `backend` · `M40·OFFLINE` · Scanners, labels and printer interfaces: interrupted-device recovery
  - Depends on: INV-607, INV-613.
  - Deliverable: Validate durable queue and cached state for Scanners, labels and printer interfaces against OFFLINE_SYNC.md.
  - Acceptance: Process death and acknowledgement loss never duplicate a command. Conflicts remain visible; stale authorization cannot commit offline-captured changes.
  - Tests: Airplane mode; reboot; duplicate batch; stale version; revoked device; cursor reset.

- [ ] INV-615 · `devops` · `M40·OPERABILITY` · Scanners, labels and printer interfaces: runbook and failure signals
  - Depends on: INV-613.
  - Deliverable: Document deployment/configuration, metrics and recovery for Scanners, labels and printer interfaces; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-616 · `qa` · `M40·QA` · Scanners, labels and printer interfaces: acceptance and invariants
  - Depends on: INV-600, INV-601, INV-602, INV-603, INV-604, INV-605, INV-606, INV-607, INV-608, INV-609, INV-610, INV-611, INV-612, INV-613, INV-614, INV-615.
  - Deliverable: Execute the feature acceptance suite for Scanners, labels and printer interfaces, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Camera, keyboard-wedge and Android intent scanner adapters normalize input without dropping GS1 separators or leading zeroes. Parse GTIN, lot, serial and expiry application identifiers with length/check-digit validation; internal labels never impersonate assigned GS1 company prefixes. PDF and ZPL interfaces support product, bin, lot and package labels; retries/reprints preserve entity IDs and are logged.

## Phase 11 — Valuation and accounting boundary

### M41 · Valuation methods and subledger

- [ ] INV-617 · `backend` · `M41·DATA` · Valuation methods and subledger: schema and migrations
  - Depends on: INV-293, INV-438, INV-454, INV-534, INV-550, INV-566, INV-582.
  - Deliverable: Create scoped tables valuation_policies, valuation_layers, valuation_entries, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Valuation methods and subledger. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-618 · `backend` · `M41·API` · Valuation methods and subledger: request and response contracts
  - Depends on: INV-617.
  - Deliverable: Implement and document 8 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: GET /valuation/layers, GET /valuation/entries, POST /valuation/rebuild, POST /valuation/policies, GET /valuation/policies, GET /valuation/policies/{id}, GET /valuation/layers/{id}, POST /valuation/policies/{id}/approve. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-619 · `backend` · `M41·AUTHZ` · Valuation methods and subledger: enforce access boundaries
  - Depends on: INV-617.
  - Deliverable: Enforce roles Valuation analyst, Auditor and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Valuation methods and subledger identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-620 · `backend` · `M41·LIFE` · FIFO costing
  - Depends on: INV-618, INV-619, INV-617.
  - Deliverable: Outgoing owned stock consumes oldest eligible company/product cost layers; physical picking strategy does not change costing order.
  - Acceptance: Outgoing owned stock consumes oldest eligible company/product cost layers; physical picking strategy does not change costing order. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Outgoing owned stock consumes oldest eligible company/product cost layers; physical picking strategy does not change costing order. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-621 · `backend` · `M41·LIFE` · Weighted-average costing
  - Depends on: INV-618, INV-619, INV-617.
  - Deliverable: Incoming cost updates the exact moving average; issues use the current average and rounding residual stays reconciled to remaining value.
  - Acceptance: Incoming cost updates the exact moving average; issues use the current average and rounding residual stays reconciled to remaining value. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Incoming cost updates the exact moving average; issues use the current average and rounding residual stays reconciled to remaining value. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-622 · `backend` · `M41·LIFE` · Standard costing
  - Depends on: INV-618, INV-619, INV-617.
  - Deliverable: Approved standard cost versions apply prospectively and price differences are recorded as valuation variance, not silently dropped.
  - Acceptance: Approved standard cost versions apply prospectively and price differences are recorded as valuation variance, not silently dropped. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Approved standard cost versions apply prospectively and price differences are recorded as valuation variance, not silently dropped. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-623 · `backend` · `M41·LIFE` · Returns and replay
  - Depends on: INV-618, INV-619, INV-617.
  - Deliverable: Returns reverse original issue/receipt basis; replay of immutable cost facts yields the same quantity/value totals and identifies any missing historical basis.
  - Acceptance: Returns reverse original issue/receipt basis; replay of immutable cost facts yields the same quantity/value totals and identifies any missing historical basis. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Returns reverse original issue/receipt basis; replay of immutable cost facts yields the same quantity/value totals and identifies any missing historical basis. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-624 · `design` · `M41·DESIGN` · Valuation methods and subledger: screen design
  - Depends on: INV-619, INV-146.
  - Deliverable: Approve S-M41-01: list/work queue, detail/history and permitted action forms for Valuation methods and subledger.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M41-01.

- [ ] INV-625 · `frontend` · `M41·BUILD` · Valuation methods and subledger: accessible user workflows
  - Depends on: INV-618, INV-620, INV-621, INV-622, INV-623, INV-624.
  - Deliverable: Build S-M41-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Valuation methods and subledger feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M41-01.

- [ ] INV-626 · `backend` · `M41·NOTIFY` · Valuation methods and subledger: actionable notifications
  - Depends on: INV-620, INV-621, INV-622, INV-623.
  - Deliverable: Register m41.attention and m41.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-627 · `backend` · `M41·ADMIN` · Valuation methods and subledger: administrative review controls
  - Depends on: INV-625.
  - Deliverable: Provide authorized history, exception review and safe recovery for Valuation methods and subledger using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-628 · `backend` · `M41·AUDIT` · Valuation methods and subledger: mutation evidence
  - Depends on: INV-620, INV-621, INV-622, INV-623.
  - Deliverable: Declare audit actions for FIFO costing, Weighted-average costing, Standard costing, Returns and replay; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-629 · `backend` · `M41·EVENTS` · Valuation methods and subledger: versioned domain events
  - Depends on: INV-620, INV-621, INV-622, INV-623.
  - Deliverable: Publish m41.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-630 · `backend` · `M41·PRIVACY` · Valuation methods and subledger: data classification and retention
  - Depends on: INV-620, INV-621, INV-622, INV-623.
  - Deliverable: Classify all fields in valuation_policies, valuation_layers, valuation_entries; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-631 · `backend` · `M41·INTEGRATION` · Valuation methods and subledger: dependency integration
  - Depends on: INV-620, INV-621, INV-622, INV-623, INV-618.
  - Deliverable: Exercise Valuation methods and subledger with prerequisite modules M20, M29, M30, M35, M36, M37, M38 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-632 · `devops` · `M41·OPERABILITY` · Valuation methods and subledger: runbook and failure signals
  - Depends on: INV-631.
  - Deliverable: Document deployment/configuration, metrics and recovery for Valuation methods and subledger; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-633 · `qa` · `M41·QA` · Valuation methods and subledger: acceptance and invariants
  - Depends on: INV-617, INV-618, INV-619, INV-620, INV-621, INV-622, INV-623, INV-624, INV-625, INV-626, INV-627, INV-628, INV-629, INV-630, INV-631, INV-632.
  - Deliverable: Execute the feature acceptance suite for Valuation methods and subledger, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 4 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Outgoing owned stock consumes oldest eligible company/product cost layers; physical picking strategy does not change costing order. Incoming cost updates the exact moving average; issues use the current average and rounding residual stays reconciled to remaining value. Approved standard cost versions apply prospectively and price differences are recorded as valuation variance, not silently dropped. Returns reverse original issue/receipt basis; replay of immutable cost facts yields the same quantity/value totals and identifies any missing historical basis. C10: Costing and rounding. FIFO issue value is ETB 28 and remaining value ETB 32; moving average issue value is ETB 36 and remaining value ETB 24; returns restore original allocated basis and all minor-unit residuals reconcile. C15: Ownership and kits. Vendor stock does not inflate company value or satisfy unrelated ownership demand; incomplete kit dispatch is blocked. C19: Intercompany and dropship. Dropship never increases warehouse on-hand; intercompany ledgers reconcile independently with snapshotted FX and buyer stock only on receipt.

### M42 · Landed costs and revaluation

- [ ] INV-634 · `backend` · `M42·DATA` · Landed costs and revaluation: schema and migrations
  - Depends on: INV-078, INV-633.
  - Deliverable: Create scoped tables landed_cost_batches, landed_cost_lines, landed_cost_allocations, revaluations, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Landed costs and revaluation. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-635 · `backend` · `M42·API` · Landed costs and revaluation: request and response contracts
  - Depends on: INV-634.
  - Deliverable: Implement and document 8 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /landed-costs, POST /landed-costs/{id}/allocate, POST /landed-costs/{id}/post, POST /valuation/revaluations, GET /landed-costs, GET /landed-costs/{id}, GET /valuation/revaluations, GET /valuation/revaluations/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-636 · `backend` · `M42·AUTHZ` · Landed costs and revaluation: enforce access boundaries
  - Depends on: INV-634.
  - Deliverable: Enforce roles Valuation analyst, Approver and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Landed costs and revaluation identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-637 · `backend` · `M42·LIFE` · Charge allocation
  - Depends on: INV-635, INV-636, INV-634.
  - Deliverable: Freight, duty and handling charges from external evidence allocate by quantity, value, weight or volume; missing bases block allocation.
  - Acceptance: Freight, duty and handling charges from external evidence allocate by quantity, value, weight or volume; missing bases block allocation. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Freight, duty and handling charges from external evidence allocate by quantity, value, weight or volume; missing bases block allocation. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-638 · `backend` · `M42·LIFE` · Remainder and consumed stock
  - Depends on: INV-635, INV-636, INV-634.
  - Deliverable: Allocation sums exactly to total charges; already-consumed shares create linked valuation adjustments rather than rewriting posted issue rows.
  - Acceptance: Allocation sums exactly to total charges; already-consumed shares create linked valuation adjustments rather than rewriting posted issue rows. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Allocation sums exactly to total charges; already-consumed shares create linked valuation adjustments rather than rewriting posted issue rows. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-639 · `backend` · `M42·LIFE` · Approved revaluation
  - Depends on: INV-635, INV-636, INV-634.
  - Deliverable: Revaluation records reason, authorization and effective open period; standard-cost changes produce explicit remaining-stock delta.
  - Acceptance: Revaluation records reason, authorization and effective open period; standard-cost changes produce explicit remaining-stock delta. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Revaluation records reason, authorization and effective open period; standard-cost changes produce explicit remaining-stock delta. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-640 · `design` · `M42·DESIGN` · Landed costs and revaluation: screen design
  - Depends on: INV-636, INV-146.
  - Deliverable: Approve S-M42-01: list/work queue, detail/history and permitted action forms for Landed costs and revaluation.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M42-01.

- [ ] INV-641 · `frontend` · `M42·BUILD` · Landed costs and revaluation: accessible user workflows
  - Depends on: INV-635, INV-637, INV-638, INV-639, INV-640.
  - Deliverable: Build S-M42-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Landed costs and revaluation feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M42-01.

- [ ] INV-642 · `backend` · `M42·NOTIFY` · Landed costs and revaluation: actionable notifications
  - Depends on: INV-637, INV-638, INV-639.
  - Deliverable: Register m42.attention and m42.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-643 · `backend` · `M42·ADMIN` · Landed costs and revaluation: administrative review controls
  - Depends on: INV-641.
  - Deliverable: Provide authorized history, exception review and safe recovery for Landed costs and revaluation using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-644 · `backend` · `M42·AUDIT` · Landed costs and revaluation: mutation evidence
  - Depends on: INV-637, INV-638, INV-639.
  - Deliverable: Declare audit actions for Charge allocation, Remainder and consumed stock, Approved revaluation; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-645 · `backend` · `M42·EVENTS` · Landed costs and revaluation: versioned domain events
  - Depends on: INV-637, INV-638, INV-639.
  - Deliverable: Publish m42.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-646 · `backend` · `M42·PRIVACY` · Landed costs and revaluation: data classification and retention
  - Depends on: INV-637, INV-638, INV-639.
  - Deliverable: Classify all fields in landed_cost_batches, landed_cost_lines, landed_cost_allocations, revaluations; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-647 · `backend` · `M42·INTEGRATION` · Landed costs and revaluation: dependency integration
  - Depends on: INV-637, INV-638, INV-639, INV-635.
  - Deliverable: Exercise Landed costs and revaluation with prerequisite modules M06, M41 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-648 · `devops` · `M42·OPERABILITY` · Landed costs and revaluation: runbook and failure signals
  - Depends on: INV-647.
  - Deliverable: Document deployment/configuration, metrics and recovery for Landed costs and revaluation; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-649 · `qa` · `M42·QA` · Landed costs and revaluation: acceptance and invariants
  - Depends on: INV-634, INV-635, INV-636, INV-637, INV-638, INV-639, INV-640, INV-641, INV-642, INV-643, INV-644, INV-645, INV-646, INV-647, INV-648.
  - Deliverable: Execute the feature acceptance suite for Landed costs and revaluation, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Freight, duty and handling charges from external evidence allocate by quantity, value, weight or volume; missing bases block allocation. Allocation sums exactly to total charges; already-consumed shares create linked valuation adjustments rather than rewriting posted issue rows. Revaluation records reason, authorization and effective open period; standard-cost changes produce explicit remaining-stock delta. C11: Landed costs after consumption. Allocated minor units sum to 1001; deterministic remainder assignment and consumed-stock adjustment preserve original rows and explain the full delta.

### M43 · Valuation periods and reconciliation

- [ ] INV-650 · `backend` · `M43·DATA` · Valuation periods and reconciliation: schema and migrations
  - Depends on: INV-633, INV-649.
  - Deliverable: Create scoped tables valuation_periods, valuation_reconciliations, period_close_checks, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Valuation periods and reconciliation. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-651 · `backend` · `M43·API` · Valuation periods and reconciliation: request and response contracts
  - Depends on: INV-650.
  - Deliverable: Implement and document 5 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /valuation/periods/{id}/reconcile, POST /valuation/periods/{id}/close, POST /valuation/periods/{id}/reopen, GET /valuation/periods, GET /valuation/periods/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-652 · `backend` · `M43·AUTHZ` · Valuation periods and reconciliation: enforce access boundaries
  - Depends on: INV-650.
  - Deliverable: Enforce roles Valuation analyst, Approver, Auditor and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Valuation periods and reconciliation identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-653 · `backend` · `M43·LIFE` · Period reconciliation
  - Depends on: INV-651, INV-652, INV-650.
  - Deliverable: Owned stock quantities and value reconcile by product/company; transit, consignment and external locations are separately explained.
  - Acceptance: Owned stock quantities and value reconcile by product/company; transit, consignment and external locations are separately explained. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Owned stock quantities and value reconcile by product/company; transit, consignment and external locations are separately explained. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-654 · `backend` · `M43·LIFE` · Close prerequisites
  - Depends on: INV-651, INV-652, INV-650.
  - Deliverable: Missing costs, unresolved valuation errors and unreviewed export differences block close; late physical activity posts in the current open period with original occurrence date retained.
  - Acceptance: Missing costs, unresolved valuation errors and unreviewed export differences block close; late physical activity posts in the current open period with original occurrence date retained. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Missing costs, unresolved valuation errors and unreviewed export differences block close; late physical activity posts in the current open period with original occurrence date retained. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-655 · `backend` · `M43·LIFE` · Controlled reopen
  - Depends on: INV-651, INV-652, INV-650.
  - Deliverable: Reopen requires independent approval and reason; a new close/export revision supersedes the old one without deleting evidence.
  - Acceptance: Reopen requires independent approval and reason; a new close/export revision supersedes the old one without deleting evidence. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Reopen requires independent approval and reason; a new close/export revision supersedes the old one without deleting evidence. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-656 · `design` · `M43·DESIGN` · Valuation periods and reconciliation: screen design
  - Depends on: INV-652, INV-146.
  - Deliverable: Approve S-M43-01: list/work queue, detail/history and permitted action forms for Valuation periods and reconciliation.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M43-01.

- [ ] INV-657 · `frontend` · `M43·BUILD` · Valuation periods and reconciliation: accessible user workflows
  - Depends on: INV-651, INV-653, INV-654, INV-655, INV-656.
  - Deliverable: Build S-M43-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Valuation periods and reconciliation feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M43-01.

- [ ] INV-658 · `backend` · `M43·NOTIFY` · Valuation periods and reconciliation: actionable notifications
  - Depends on: INV-653, INV-654, INV-655.
  - Deliverable: Register m43.attention and m43.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-659 · `backend` · `M43·ADMIN` · Valuation periods and reconciliation: administrative review controls
  - Depends on: INV-657.
  - Deliverable: Provide authorized history, exception review and safe recovery for Valuation periods and reconciliation using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-660 · `backend` · `M43·AUDIT` · Valuation periods and reconciliation: mutation evidence
  - Depends on: INV-653, INV-654, INV-655.
  - Deliverable: Declare audit actions for Period reconciliation, Close prerequisites, Controlled reopen; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-661 · `backend` · `M43·EVENTS` · Valuation periods and reconciliation: versioned domain events
  - Depends on: INV-653, INV-654, INV-655.
  - Deliverable: Publish m43.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-662 · `backend` · `M43·PRIVACY` · Valuation periods and reconciliation: data classification and retention
  - Depends on: INV-653, INV-654, INV-655.
  - Deliverable: Classify all fields in valuation_periods, valuation_reconciliations, period_close_checks; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-663 · `backend` · `M43·INTEGRATION` · Valuation periods and reconciliation: dependency integration
  - Depends on: INV-653, INV-654, INV-655, INV-651.
  - Deliverable: Exercise Valuation periods and reconciliation with prerequisite modules M41, M42 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-664 · `devops` · `M43·OPERABILITY` · Valuation periods and reconciliation: runbook and failure signals
  - Depends on: INV-663.
  - Deliverable: Document deployment/configuration, metrics and recovery for Valuation periods and reconciliation; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-665 · `qa` · `M43·QA` · Valuation periods and reconciliation: acceptance and invariants
  - Depends on: INV-650, INV-651, INV-652, INV-653, INV-654, INV-655, INV-656, INV-657, INV-658, INV-659, INV-660, INV-661, INV-662, INV-663, INV-664.
  - Deliverable: Execute the feature acceptance suite for Valuation periods and reconciliation, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Owned stock quantities and value reconcile by product/company; transit, consignment and external locations are separately explained. Missing costs, unresolved valuation errors and unreviewed export differences block close; late physical activity posts in the current open period with original occurrence date retained. Reopen requires independent approval and reason; a new close/export revision supersedes the old one without deleting evidence. C12: Period lock and late receipt. Original occurrence date is retained; accounting effect goes to the current open period; locked entries cannot be silently changed.

### M44 · Accounting export batches

- [ ] INV-666 · `backend` · `M44·DATA` · Accounting export batches: schema and migrations
  - Depends on: INV-110, INV-665.
  - Deliverable: Create scoped tables account_mappings, accounting_export_batches, accounting_export_lines, export_acknowledgements, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Accounting export batches. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-667 · `backend` · `M44·API` · Accounting export batches: request and response contracts
  - Depends on: INV-666.
  - Deliverable: Implement and document 9 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /accounting/export-batches, GET /accounting/export-batches/{id}/download, POST /accounting/export-batches/{id}/acknowledge, POST /accounting/export-batches/{id}/retry, GET /accounting/export-batches, GET /accounting/export-batches/{id}, GET /accounting/mappings, GET /accounting/mappings/{id}, PUT /accounting/mappings. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-668 · `backend` · `M44·AUTHZ` · Accounting export batches: enforce access boundaries
  - Depends on: INV-666.
  - Deliverable: Enforce roles Valuation analyst, Integration operator and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Accounting export batches identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-669 · `backend` · `M44·LIFE` · Balanced export format
  - Depends on: INV-667, INV-668, INV-666.
  - Deliverable: Versioned CSV/JSON inventory journal proposals balance by currency and map every line to valuation evidence; missing external account mappings block release.
  - Acceptance: Versioned CSV/JSON inventory journal proposals balance by currency and map every line to valuation evidence; missing external account mappings block release. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Versioned CSV/JSON inventory journal proposals balance by currency and map every line to valuation evidence; missing external account mappings block release. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-670 · `backend` · `M44·LIFE` · Delivery acknowledgement
  - Depends on: INV-667, INV-668, INV-666.
  - Deliverable: Same batch ID and checksum replay safely; conflicting acknowledgement is rejected and partial rejection stays visible for reconciliation.
  - Acceptance: Same batch ID and checksum replay safely; conflicting acknowledgement is rejected and partial rejection stays visible for reconciliation. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Same batch ID and checksum replay safely; conflicting acknowledgement is rejected and partial rejection stays visible for reconciliation. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-671 · `backend` · `M44·LIFE` · Accounting boundary
  - Depends on: INV-667, INV-668, INV-666.
  - Deliverable: External ledger owns posting and financial statements; the product emits inventory proposals only and never claims to create invoices, bills or bank transactions.
  - Acceptance: External ledger owns posting and financial statements; the product emits inventory proposals only and never claims to create invoices, bills or bank transactions. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: External ledger owns posting and financial statements; the product emits inventory proposals only and never claims to create invoices, bills or bank transactions. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-672 · `design` · `M44·DESIGN` · Accounting export batches: screen design
  - Depends on: INV-668, INV-146.
  - Deliverable: Approve S-M44-01: list/work queue, detail/history and permitted action forms for Accounting export batches.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M44-01.

- [ ] INV-673 · `frontend` · `M44·BUILD` · Accounting export batches: accessible user workflows
  - Depends on: INV-667, INV-669, INV-670, INV-671, INV-672.
  - Deliverable: Build S-M44-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Accounting export batches feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M44-01.

- [ ] INV-674 · `backend` · `M44·NOTIFY` · Accounting export batches: actionable notifications
  - Depends on: INV-669, INV-670, INV-671.
  - Deliverable: Register m44.attention and m44.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-675 · `backend` · `M44·ADMIN` · Accounting export batches: administrative review controls
  - Depends on: INV-673.
  - Deliverable: Provide authorized history, exception review and safe recovery for Accounting export batches using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-676 · `backend` · `M44·AUDIT` · Accounting export batches: mutation evidence
  - Depends on: INV-669, INV-670, INV-671.
  - Deliverable: Declare audit actions for Balanced export format, Delivery acknowledgement, Accounting boundary; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-677 · `backend` · `M44·EVENTS` · Accounting export batches: versioned domain events
  - Depends on: INV-669, INV-670, INV-671.
  - Deliverable: Publish m44.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-678 · `backend` · `M44·PRIVACY` · Accounting export batches: data classification and retention
  - Depends on: INV-669, INV-670, INV-671.
  - Deliverable: Classify all fields in account_mappings, accounting_export_batches, accounting_export_lines, export_acknowledgements; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-679 · `backend` · `M44·INTEGRATION` · Accounting export batches: dependency integration
  - Depends on: INV-669, INV-670, INV-671, INV-667.
  - Deliverable: Exercise Accounting export batches with prerequisite modules M08, M43 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-680 · `devops` · `M44·OPERABILITY` · Accounting export batches: runbook and failure signals
  - Depends on: INV-679.
  - Deliverable: Document deployment/configuration, metrics and recovery for Accounting export batches; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-681 · `qa` · `M44·QA` · Accounting export batches: acceptance and invariants
  - Depends on: INV-666, INV-667, INV-668, INV-669, INV-670, INV-671, INV-672, INV-673, INV-674, INV-675, INV-676, INV-677, INV-678, INV-679, INV-680.
  - Deliverable: Execute the feature acceptance suite for Accounting export batches, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Versioned CSV/JSON inventory journal proposals balance by currency and map every line to valuation evidence; missing external account mappings block release. Same batch ID and checksum replay safely; conflicting acknowledgement is rejected and partial rejection stays visible for reconciliation. External ledger owns posting and financial statements; the product emits inventory proposals only and never claims to create invoices, bills or bank transactions. C13: Accounting acknowledgement replay. External references and checksum prevent duplicate proposals; rejected lines stay visible; reconciliation cannot falsely show fully accepted.

## Phase 12 — Reports, interfaces and migration

### M45 · Operational reports and analytics

- [ ] INV-682 · `backend` · `M45·DATA` · Operational reports and analytics: schema and migrations
  - Depends on: INV-518, INV-633, INV-665, INV-681.
  - Deliverable: Create scoped tables report_jobs, dashboard_preferences, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Operational reports and analytics. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-683 · `backend` · `M45·API` · Operational reports and analytics: request and response contracts
  - Depends on: INV-682.
  - Deliverable: Implement and document 8 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: GET /reports/stock-card, GET /reports/aging, GET /reports/expiry, GET /reports/fulfillment, GET /reports/supplier-performance, POST /reports/exports, GET /reports/jobs, GET /reports/jobs/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-684 · `backend` · `M45·AUTHZ` · Operational reports and analytics: enforce access boundaries
  - Depends on: INV-682.
  - Deliverable: Enforce roles Warehouse supervisor, Buyer, Sales manager, Valuation analyst, Auditor and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Operational reports and analytics identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-685 · `backend` · `M45·LIFE` · As-of stock and value
  - Depends on: INV-683, INV-684, INV-682.
  - Deliverable: Stock card, on-hand, reserved, transit, owner, aging and value reports reconcile to the ledger at the same as-of instant.
  - Acceptance: Stock card, on-hand, reserved, transit, owner, aging and value reports reconcile to the ledger at the same as-of instant. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Stock card, on-hand, reserved, transit, owner, aging and value reports reconcile to the ledger at the same as-of instant. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-686 · `backend` · `M45·LIFE` · Service metrics
  - Depends on: INV-683, INV-684, INV-682.
  - Deliverable: Fulfillment rate, backorder age, purchase lead-time variance and supplier acceptance rate have published numerator/denominator definitions.
  - Acceptance: Fulfillment rate, backorder age, purchase lead-time variance and supplier acceptance rate have published numerator/denominator definitions. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Fulfillment rate, backorder age, purchase lead-time variance and supplier acceptance rate have published numerator/denominator definitions. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-687 · `backend` · `M45·LIFE` · Secure exports
  - Depends on: INV-683, INV-684, INV-682.
  - Deliverable: Large reports run as scoped jobs; permissions are rechecked on download and expired export URLs cannot be reused.
  - Acceptance: Large reports run as scoped jobs; permissions are rechecked on download and expired export URLs cannot be reused. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Large reports run as scoped jobs; permissions are rechecked on download and expired export URLs cannot be reused. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-688 · `design` · `M45·DESIGN` · Operational reports and analytics: screen design
  - Depends on: INV-684, INV-146.
  - Deliverable: Approve S-M45-01: list/work queue, detail/history and permitted action forms for Operational reports and analytics.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M45-01.

- [ ] INV-689 · `frontend` · `M45·BUILD` · Operational reports and analytics: accessible user workflows
  - Depends on: INV-683, INV-685, INV-686, INV-687, INV-688.
  - Deliverable: Build S-M45-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Operational reports and analytics feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M45-01.

- [ ] INV-690 · `backend` · `M45·NOTIFY` · Operational reports and analytics: actionable notifications
  - Depends on: INV-685, INV-686, INV-687.
  - Deliverable: Register m45.attention and m45.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-691 · `backend` · `M45·ADMIN` · Operational reports and analytics: administrative review controls
  - Depends on: INV-689.
  - Deliverable: Provide authorized history, exception review and safe recovery for Operational reports and analytics using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-692 · `backend` · `M45·AUDIT` · Operational reports and analytics: mutation evidence
  - Depends on: INV-685, INV-686, INV-687.
  - Deliverable: Declare audit actions for As-of stock and value, Service metrics, Secure exports; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-693 · `backend` · `M45·EVENTS` · Operational reports and analytics: versioned domain events
  - Depends on: INV-685, INV-686, INV-687.
  - Deliverable: Publish m45.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-694 · `backend` · `M45·PRIVACY` · Operational reports and analytics: data classification and retention
  - Depends on: INV-685, INV-686, INV-687.
  - Deliverable: Classify all fields in report_jobs, dashboard_preferences; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-695 · `backend` · `M45·INTEGRATION` · Operational reports and analytics: dependency integration
  - Depends on: INV-685, INV-686, INV-687, INV-683.
  - Deliverable: Exercise Operational reports and analytics with prerequisite modules M34, M41, M43, M44 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-696 · `devops` · `M45·OPERABILITY` · Operational reports and analytics: runbook and failure signals
  - Depends on: INV-695.
  - Deliverable: Document deployment/configuration, metrics and recovery for Operational reports and analytics; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-697 · `qa` · `M45·QA` · Operational reports and analytics: acceptance and invariants
  - Depends on: INV-682, INV-683, INV-684, INV-685, INV-686, INV-687, INV-688, INV-689, INV-690, INV-691, INV-692, INV-693, INV-694, INV-695, INV-696.
  - Deliverable: Execute the feature acceptance suite for Operational reports and analytics, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Stock card, on-hand, reserved, transit, owner, aging and value reports reconcile to the ledger at the same as-of instant. Fulfillment rate, backorder age, purchase lead-time variance and supplier acceptance rate have published numerator/denominator definitions. Large reports run as scoped jobs; permissions are rechecked on download and expired export URLs cannot be reused.

### M46 · External APIs, imports and webhooks

- [ ] INV-698 · `backend` · `M46·DATA` · External APIs, imports and webhooks: schema and migrations
  - Depends on: INV-110, INV-125, INV-358, INV-406, INV-681.
  - Deliverable: Create scoped tables api_credentials, webhook_subscriptions, webhook_deliveries, import_batches, import_errors, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for External APIs, imports and webhooks. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-699 · `backend` · `M46·API` · External APIs, imports and webhooks: request and response contracts
  - Depends on: INV-698.
  - Deliverable: Implement and document 13 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /api-credentials, POST /webhook-subscriptions, POST /imports/dry-run, POST /imports/{id}/commit, GET /integration-deliveries, GET /api-credentials, GET /api-credentials/{id}, GET /webhook-subscriptions, GET /webhook-subscriptions/{id}, GET /imports, GET /imports/{id}, DELETE /api-credentials/{id}, POST /webhook-subscriptions/{id}/rotate-secret. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-700 · `backend` · `M46·AUTHZ` · External APIs, imports and webhooks: enforce access boundaries
  - Depends on: INV-698.
  - Deliverable: Enforce roles Integration operator and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every External APIs, imports and webhooks identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-701 · `backend` · `M46·LIFE` · Public API contracts
  - Depends on: INV-699, INV-700, INV-698.
  - Deliverable: API keys are hashed, scoped, expiring and revocable; cursor pagination, rate limits and documented error shapes apply consistently.
  - Acceptance: API keys are hashed, scoped, expiring and revocable; cursor pagination, rate limits and documented error shapes apply consistently. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: API keys are hashed, scoped, expiring and revocable; cursor pagination, rate limits and documented error shapes apply consistently. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-702 · `backend` · `M46·LIFE` · Signed webhooks
  - Depends on: INV-699, INV-700, INV-698.
  - Deliverable: HMAC signatures cover timestamp and raw body; replay window, secret rotation, destination validation and SSRF protection are tested.
  - Acceptance: HMAC signatures cover timestamp and raw body; replay window, secret rotation, destination validation and SSRF protection are tested. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: HMAC signatures cover timestamp and raw body; replay window, secret rotation, destination validation and SSRF protection are tested. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-703 · `backend` · `M46·LIFE` · Versioned imports
  - Depends on: INV-699, INV-700, INV-698.
  - Deliverable: Dry-run validates references and duplicates before commit; error CSV names exact rows and no partial stock posting is hidden.
  - Acceptance: Dry-run validates references and duplicates before commit; error CSV names exact rows and no partial stock posting is hidden. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Dry-run validates references and duplicates before commit; error CSV names exact rows and no partial stock posting is hidden. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-704 · `backend` · `M46·LIFE` · Connector boundary
  - Depends on: INV-699, INV-700, INV-698.
  - Deliverable: Generic CSV/API/webhook adapters ship; named accounting, courier and payment connectors remain explicit later-scope entries.
  - Acceptance: Generic CSV/API/webhook adapters ship; named accounting, courier and payment connectors remain explicit later-scope entries. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Generic CSV/API/webhook adapters ship; named accounting, courier and payment connectors remain explicit later-scope entries. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-705 · `design` · `M46·DESIGN` · External APIs, imports and webhooks: screen design
  - Depends on: INV-700, INV-146.
  - Deliverable: Approve S-M46-01: list/work queue, detail/history and permitted action forms for External APIs, imports and webhooks.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M46-01.

- [ ] INV-706 · `frontend` · `M46·BUILD` · External APIs, imports and webhooks: accessible user workflows
  - Depends on: INV-699, INV-701, INV-702, INV-703, INV-704, INV-705.
  - Deliverable: Build S-M46-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All External APIs, imports and webhooks feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M46-01.

- [ ] INV-707 · `backend` · `M46·NOTIFY` · External APIs, imports and webhooks: actionable notifications
  - Depends on: INV-701, INV-702, INV-703, INV-704.
  - Deliverable: Register m46.attention and m46.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-708 · `backend` · `M46·ADMIN` · External APIs, imports and webhooks: administrative review controls
  - Depends on: INV-706.
  - Deliverable: Provide authorized history, exception review and safe recovery for External APIs, imports and webhooks using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-709 · `backend` · `M46·AUDIT` · External APIs, imports and webhooks: mutation evidence
  - Depends on: INV-701, INV-702, INV-703, INV-704.
  - Deliverable: Declare audit actions for Public API contracts, Signed webhooks, Versioned imports, Connector boundary; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-710 · `backend` · `M46·EVENTS` · External APIs, imports and webhooks: versioned domain events
  - Depends on: INV-701, INV-702, INV-703, INV-704.
  - Deliverable: Publish m46.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-711 · `backend` · `M46·PRIVACY` · External APIs, imports and webhooks: data classification and retention
  - Depends on: INV-701, INV-702, INV-703, INV-704.
  - Deliverable: Classify all fields in api_credentials, webhook_subscriptions, webhook_deliveries, import_batches, import_errors; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-712 · `backend` · `M46·INTEGRATION` · External APIs, imports and webhooks: dependency integration
  - Depends on: INV-701, INV-702, INV-703, INV-704, INV-699.
  - Deliverable: Exercise External APIs, imports and webhooks with prerequisite modules M08, M09, M24, M27, M44 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-713 · `devops` · `M46·OPERABILITY` · External APIs, imports and webhooks: runbook and failure signals
  - Depends on: INV-712.
  - Deliverable: Document deployment/configuration, metrics and recovery for External APIs, imports and webhooks; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-714 · `qa` · `M46·QA` · External APIs, imports and webhooks: acceptance and invariants
  - Depends on: INV-698, INV-699, INV-700, INV-701, INV-702, INV-703, INV-704, INV-705, INV-706, INV-707, INV-708, INV-709, INV-710, INV-711, INV-712, INV-713.
  - Deliverable: Execute the feature acceptance suite for External APIs, imports and webhooks, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 4 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: API keys are hashed, scoped, expiring and revocable; cursor pagination, rate limits and documented error shapes apply consistently. HMAC signatures cover timestamp and raw body; replay window, secret rotation, destination validation and SSRF protection are tested. Dry-run validates references and duplicates before commit; error CSV names exact rows and no partial stock posting is hidden. Generic CSV/API/webhook adapters ship; named accounting, courier and payment connectors remain explicit later-scope entries. C16: Webhook security. Receiver deduplicates event IDs; tamper/expired signatures and SSRF destinations fail; retries do not duplicate side effects.

### M47 · Customer migration and onboarding

- [ ] INV-715 · `backend` · `M47·DATA` · Customer migration and onboarding: schema and migrations
  - Depends on: INV-325, INV-470, INV-665, INV-714.
  - Deliverable: Create scoped tables migration_runs, migration_mappings, migration_reconciliations, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Customer migration and onboarding. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-716 · `backend` · `M47·API` · Customer migration and onboarding: request and response contracts
  - Depends on: INV-715.
  - Deliverable: Implement and document 5 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /migration-runs, POST /migration-runs/{id}/validate, POST /migration-runs/{id}/approve-cutover, GET /migration-runs, GET /migration-runs/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-717 · `backend` · `M47·AUTHZ` · Customer migration and onboarding: enforce access boundaries
  - Depends on: INV-715.
  - Deliverable: Enforce roles Implementation operator, Tenant admin and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Customer migration and onboarding identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-718 · `backend` · `M47·LIFE` · Mapping and rehearsal
  - Depends on: INV-716, INV-717, INV-715.
  - Deliverable: Map master data, opening quantities, tracking, ownership, reservations and opening cost layers with source checksums and reconciliation reports.
  - Acceptance: Map master data, opening quantities, tracking, ownership, reservations and opening cost layers with source checksums and reconciliation reports. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Map master data, opening quantities, tracking, ownership, reservations and opening cost layers with source checksums and reconciliation reports. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-719 · `backend` · `M47·LIFE` · Cutover controls
  - Depends on: INV-716, INV-717, INV-715.
  - Deliverable: Freeze source writes, apply the final delta, reconcile totals and obtain named customer approval before enabling production posting.
  - Acceptance: Freeze source writes, apply the final delta, reconcile totals and obtain named customer approval before enabling production posting. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Freeze source writes, apply the final delta, reconcile totals and obtain named customer approval before enabling production posting. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-720 · `backend` · `M47·LIFE` · Rollback boundary
  - Depends on: INV-716, INV-717, INV-715.
  - Deliverable: Before first new live movement restore the rehearsed snapshot; afterward use forward corrections and replay accepted commands rather than deleting live history.
  - Acceptance: Before first new live movement restore the rehearsed snapshot; afterward use forward corrections and replay accepted commands rather than deleting live history. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Before first new live movement restore the rehearsed snapshot; afterward use forward corrections and replay accepted commands rather than deleting live history. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-721 · `design` · `M47·DESIGN` · Customer migration and onboarding: screen design
  - Depends on: INV-717, INV-146.
  - Deliverable: Approve S-M47-01: list/work queue, detail/history and permitted action forms for Customer migration and onboarding.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M47-01.

- [ ] INV-722 · `frontend` · `M47·BUILD` · Customer migration and onboarding: accessible user workflows
  - Depends on: INV-716, INV-718, INV-719, INV-720, INV-721.
  - Deliverable: Build S-M47-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Customer migration and onboarding feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M47-01.

- [ ] INV-723 · `backend` · `M47·NOTIFY` · Customer migration and onboarding: actionable notifications
  - Depends on: INV-718, INV-719, INV-720.
  - Deliverable: Register m47.attention and m47.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-724 · `backend` · `M47·ADMIN` · Customer migration and onboarding: administrative review controls
  - Depends on: INV-722.
  - Deliverable: Provide authorized history, exception review and safe recovery for Customer migration and onboarding using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-725 · `backend` · `M47·AUDIT` · Customer migration and onboarding: mutation evidence
  - Depends on: INV-718, INV-719, INV-720.
  - Deliverable: Declare audit actions for Mapping and rehearsal, Cutover controls, Rollback boundary; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-726 · `backend` · `M47·EVENTS` · Customer migration and onboarding: versioned domain events
  - Depends on: INV-718, INV-719, INV-720.
  - Deliverable: Publish m47.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-727 · `backend` · `M47·PRIVACY` · Customer migration and onboarding: data classification and retention
  - Depends on: INV-718, INV-719, INV-720.
  - Deliverable: Classify all fields in migration_runs, migration_mappings, migration_reconciliations; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-728 · `backend` · `M47·INTEGRATION` · Customer migration and onboarding: dependency integration
  - Depends on: INV-718, INV-719, INV-720, INV-716.
  - Deliverable: Exercise Customer migration and onboarding with prerequisite modules M22, M31, M43, M46 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-729 · `devops` · `M47·OPERABILITY` · Customer migration and onboarding: runbook and failure signals
  - Depends on: INV-728.
  - Deliverable: Document deployment/configuration, metrics and recovery for Customer migration and onboarding; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-730 · `qa` · `M47·QA` · Customer migration and onboarding: acceptance and invariants
  - Depends on: INV-715, INV-716, INV-717, INV-718, INV-719, INV-720, INV-721, INV-722, INV-723, INV-724, INV-725, INV-726, INV-727, INV-728, INV-729.
  - Deliverable: Execute the feature acceptance suite for Customer migration and onboarding, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Map master data, opening quantities, tracking, ownership, reservations and opening cost layers with source checksums and reconciliation reports. Freeze source writes, apply the final delta, reconcile totals and obtain named customer approval before enabling production posting. Before first new live movement restore the rehearsed snapshot; afterward use forward corrections and replay accepted commands rather than deleting live history.

## Phase 13 — Operational readiness and launch

### M48 · SaaS support and customer lifecycle

- [ ] INV-731 · `backend` · `M48·DATA` · SaaS support and customer lifecycle: schema and migrations
  - Depends on: INV-030, INV-062, INV-697, INV-714, INV-730.
  - Deliverable: Create scoped tables support_sessions, tenant_exports, offboarding_requests, usage_counters, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for SaaS support and customer lifecycle. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-732 · `backend` · `M48·API` · SaaS support and customer lifecycle: request and response contracts
  - Depends on: INV-731.
  - Deliverable: Implement and document 10 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /support-sessions, POST /tenant-exports, POST /offboarding-requests, GET /usage, GET /support-sessions, GET /support-sessions/{id}, GET /tenant-exports, GET /tenant-exports/{id}, GET /offboarding-requests, GET /offboarding-requests/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-733 · `backend` · `M48·AUTHZ` · SaaS support and customer lifecycle: enforce access boundaries
  - Depends on: INV-731.
  - Deliverable: Enforce roles Platform operator, Tenant admin and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every SaaS support and customer lifecycle identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-734 · `backend` · `M48·LIFE` · Support runbooks
  - Depends on: INV-732, INV-733, INV-731.
  - Deliverable: Customer-approved support access is time-bounded and logged; cross-tenant searching requires a platform purpose and exposes minimum metadata.
  - Acceptance: Customer-approved support access is time-bounded and logged; cross-tenant searching requires a platform purpose and exposes minimum metadata. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Customer-approved support access is time-bounded and logged; cross-tenant searching requires a platform purpose and exposes minimum metadata. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-735 · `backend` · `M48·LIFE` · Tenant portability
  - Depends on: INV-732, INV-733, INV-731.
  - Deliverable: Export includes master data, documents, stock and valuation ledgers, attachments manifest and schema version; completeness is reconciled before delivery.
  - Acceptance: Export includes master data, documents, stock and valuation ledgers, attachments manifest and schema version; completeness is reconciled before delivery. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Export includes master data, documents, stock and valuation ledgers, attachments manifest and schema version; completeness is reconciled before delivery. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-736 · `backend` · `M48·LIFE` · Offboarding and holds
  - Depends on: INV-732, INV-733, INV-731.
  - Deliverable: Offboarding revokes access, schedules configured deletion and respects documented legal holds; backup expiry and data-destruction evidence are tracked.
  - Acceptance: Offboarding revokes access, schedules configured deletion and respects documented legal holds; backup expiry and data-destruction evidence are tracked. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Offboarding revokes access, schedules configured deletion and respects documented legal holds; backup expiry and data-destruction evidence are tracked. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-737 · `design` · `M48·DESIGN` · SaaS support and customer lifecycle: screen design
  - Depends on: INV-733, INV-146.
  - Deliverable: Approve S-M48-01: list/work queue, detail/history and permitted action forms for SaaS support and customer lifecycle.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M48-01.

- [ ] INV-738 · `frontend` · `M48·BUILD` · SaaS support and customer lifecycle: accessible user workflows
  - Depends on: INV-732, INV-734, INV-735, INV-736, INV-737.
  - Deliverable: Build S-M48-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All SaaS support and customer lifecycle feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M48-01.

- [ ] INV-739 · `backend` · `M48·NOTIFY` · SaaS support and customer lifecycle: actionable notifications
  - Depends on: INV-734, INV-735, INV-736.
  - Deliverable: Register m48.attention and m48.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-740 · `backend` · `M48·ADMIN` · SaaS support and customer lifecycle: administrative review controls
  - Depends on: INV-738.
  - Deliverable: Provide authorized history, exception review and safe recovery for SaaS support and customer lifecycle using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-741 · `backend` · `M48·AUDIT` · SaaS support and customer lifecycle: mutation evidence
  - Depends on: INV-734, INV-735, INV-736.
  - Deliverable: Declare audit actions for Support runbooks, Tenant portability, Offboarding and holds; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-742 · `backend` · `M48·EVENTS` · SaaS support and customer lifecycle: versioned domain events
  - Depends on: INV-734, INV-735, INV-736.
  - Deliverable: Publish m48.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-743 · `backend` · `M48·PRIVACY` · SaaS support and customer lifecycle: data classification and retention
  - Depends on: INV-734, INV-735, INV-736.
  - Deliverable: Classify all fields in support_sessions, tenant_exports, offboarding_requests, usage_counters; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-744 · `backend` · `M48·INTEGRATION` · SaaS support and customer lifecycle: dependency integration
  - Depends on: INV-734, INV-735, INV-736, INV-732.
  - Deliverable: Exercise SaaS support and customer lifecycle with prerequisite modules M03, M05, M45, M46, M47 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-745 · `devops` · `M48·OPERABILITY` · SaaS support and customer lifecycle: runbook and failure signals
  - Depends on: INV-744.
  - Deliverable: Document deployment/configuration, metrics and recovery for SaaS support and customer lifecycle; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-746 · `qa` · `M48·QA` · SaaS support and customer lifecycle: acceptance and invariants
  - Depends on: INV-731, INV-732, INV-733, INV-734, INV-735, INV-736, INV-737, INV-738, INV-739, INV-740, INV-741, INV-742, INV-743, INV-744, INV-745.
  - Deliverable: Execute the feature acceptance suite for SaaS support and customer lifecycle, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Customer-approved support access is time-bounded and logged; cross-tenant searching requires a platform purpose and exposes minimum metadata. Export includes master data, documents, stock and valuation ledgers, attachments manifest and schema version; completeness is reconciled before delivery. Offboarding revokes access, schedules configured deletion and respects documented legal holds; backup expiry and data-destruction evidence are tracked.

### M49 · Security, privacy and localization release

- [ ] INV-747 · `backend` · `M49·DATA` · Security, privacy and localization release: schema and migrations
  - Depends on: INV-046, INV-062, INV-125, INV-599, INV-714, INV-746.
  - Deliverable: Create scoped tables privacy_requests, retention_rules, compliance_reviews, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Security, privacy and localization release. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-748 · `backend` · `M49·API` · Security, privacy and localization release: request and response contracts
  - Depends on: INV-747.
  - Deliverable: Implement and document 6 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: POST /privacy-requests, GET /privacy-requests/{id}, POST /compliance-reviews, GET /privacy-requests, GET /compliance-reviews, GET /compliance-reviews/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-749 · `backend` · `M49·AUTHZ` · Security, privacy and localization release: enforce access boundaries
  - Depends on: INV-747.
  - Deliverable: Enforce roles Security reviewer, Compliance reviewer and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Security, privacy and localization release identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-750 · `backend` · `M49·LIFE` · Isolation assessment
  - Depends on: INV-748, INV-749, INV-747.
  - Deliverable: Negative tests cover API, raw application-role SQL, jobs, files, reports, mobile and integrations across two tenants and two companies.
  - Acceptance: Negative tests cover API, raw application-role SQL, jobs, files, reports, mobile and integrations across two tenants and two companies. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Negative tests cover API, raw application-role SQL, jobs, files, reports, mobile and integrations across two tenants and two companies. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-751 · `backend` · `M49·LIFE` · Privacy rights and retention
  - Depends on: INV-748, INV-749, INV-747.
  - Deliverable: Export/anonymize contact data while retaining permitted transaction evidence; retention and hosting decisions require reviewed Ethiopian legal applicability, not assumed durations.
  - Acceptance: Export/anonymize contact data while retaining permitted transaction evidence; retention and hosting decisions require reviewed Ethiopian legal applicability, not assumed durations. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Export/anonymize contact data while retaining permitted transaction evidence; retention and hosting decisions require reviewed Ethiopian legal applicability, not assumed durations. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-752 · `backend` · `M49·LIFE` · Launch security
  - Depends on: INV-748, INV-749, INV-747.
  - Deliverable: Threat model, dependency/license scans, penetration-test findings and critical/high vulnerability closure are signed off before pilot.
  - Acceptance: Threat model, dependency/license scans, penetration-test findings and critical/high vulnerability closure are signed off before pilot. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Threat model, dependency/license scans, penetration-test findings and critical/high vulnerability closure are signed off before pilot. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-753 · `design` · `M49·DESIGN` · Security, privacy and localization release: screen design
  - Depends on: INV-749, INV-146.
  - Deliverable: Approve S-M49-01: list/work queue, detail/history and permitted action forms for Security, privacy and localization release.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M49-01.

- [ ] INV-754 · `frontend` · `M49·BUILD` · Security, privacy and localization release: accessible user workflows
  - Depends on: INV-748, INV-750, INV-751, INV-752, INV-753.
  - Deliverable: Build S-M49-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Security, privacy and localization release feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M49-01.

- [ ] INV-755 · `backend` · `M49·NOTIFY` · Security, privacy and localization release: actionable notifications
  - Depends on: INV-750, INV-751, INV-752.
  - Deliverable: Register m49.attention and m49.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-756 · `backend` · `M49·ADMIN` · Security, privacy and localization release: administrative review controls
  - Depends on: INV-754.
  - Deliverable: Provide authorized history, exception review and safe recovery for Security, privacy and localization release using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-757 · `backend` · `M49·AUDIT` · Security, privacy and localization release: mutation evidence
  - Depends on: INV-750, INV-751, INV-752.
  - Deliverable: Declare audit actions for Isolation assessment, Privacy rights and retention, Launch security; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-758 · `backend` · `M49·EVENTS` · Security, privacy and localization release: versioned domain events
  - Depends on: INV-750, INV-751, INV-752.
  - Deliverable: Publish m49.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-759 · `backend` · `M49·PRIVACY` · Security, privacy and localization release: data classification and retention
  - Depends on: INV-750, INV-751, INV-752.
  - Deliverable: Classify all fields in privacy_requests, retention_rules, compliance_reviews; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-760 · `backend` · `M49·INTEGRATION` · Security, privacy and localization release: dependency integration
  - Depends on: INV-750, INV-751, INV-752, INV-748.
  - Deliverable: Exercise Security, privacy and localization release with prerequisite modules M04, M05, M09, M39, M46, M48 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-761 · `devops` · `M49·OPERABILITY` · Security, privacy and localization release: runbook and failure signals
  - Depends on: INV-760.
  - Deliverable: Document deployment/configuration, metrics and recovery for Security, privacy and localization release; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-762 · `qa` · `M49·QA` · Security, privacy and localization release: acceptance and invariants
  - Depends on: INV-747, INV-748, INV-749, INV-750, INV-751, INV-752, INV-753, INV-754, INV-755, INV-756, INV-757, INV-758, INV-759, INV-760, INV-761.
  - Deliverable: Execute the feature acceptance suite for Security, privacy and localization release, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Negative tests cover API, raw application-role SQL, jobs, files, reports, mobile and integrations across two tenants and two companies. Export/anonymize contact data while retaining permitted transaction evidence; retention and hosting decisions require reviewed Ethiopian legal applicability, not assumed durations. Threat model, dependency/license scans, penetration-test findings and critical/high vulnerability closure are signed off before pilot. C06: Unauthorized scope everywhere. No foreign row, attachment, event or balance leaks; all mutation attempts are rejected and logged without leaking private data.

### M50 · Reliability, recovery and performance

- [ ] INV-763 · `backend` · `M50·DATA` · Reliability, recovery and performance: schema and migrations
  - Depends on: INV-110, INV-697, INV-714.
  - Deliverable: Create scoped tables operational_incidents, restore_drills, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Reliability, recovery and performance. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-764 · `backend` · `M50·API` · Reliability, recovery and performance: request and response contracts
  - Depends on: INV-763.
  - Deliverable: Implement and document 5 registered routes with validation, authorization hooks, pagination and typed errors.
  - Acceptance: Every registered route appears in generated OpenAPI and the typed client. Routes cover: GET /health, GET /health/ready, GET /operations/status, GET /operations/incidents, GET /operations/incidents/{id}. Posting endpoints require idempotency keys; edits require document version.
  - Tests: Contract happy path; 401/403/404/409/422; repeated request and schema drift.

- [ ] INV-765 · `backend` · `M50·AUTHZ` · Reliability, recovery and performance: enforce access boundaries
  - Depends on: INV-763.
  - Deliverable: Enforce roles Platform operator, Engineer and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Reliability, recovery and performance identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-766 · `backend` · `M50·LIFE` · Observability
  - Depends on: INV-764, INV-765, INV-763.
  - Deliverable: Metrics expose posting latency, lock conflicts, sync lag, dead letters, export failures, backup age and per-tenant resource saturation without PII.
  - Acceptance: Metrics expose posting latency, lock conflicts, sync lag, dead letters, export failures, backup age and per-tenant resource saturation without PII. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Metrics expose posting latency, lock conflicts, sync lag, dead letters, export failures, backup age and per-tenant resource saturation without PII. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-767 · `backend` · `M50·LIFE` · Backup and recovery
  - Depends on: INV-764, INV-765, INV-763.
  - Deliverable: Encrypted backups and point-in-time recovery are rehearsed to a separate environment; target RPO is 15 minutes and RTO is four hours.
  - Acceptance: Encrypted backups and point-in-time recovery are rehearsed to a separate environment; target RPO is 15 minutes and RTO is four hours. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Encrypted backups and point-in-time recovery are rehearsed to a separate environment; target RPO is 15 minutes and RTO is four hours. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-768 · `backend` · `M50·LIFE` · Performance budgets
  - Depends on: INV-764, INV-765, INV-763.
  - Deliverable: At the documented launch dataset, online reads meet p95 500ms and stock posting p95 one second; Android critical flows work on a mid-range device with intermittent connectivity.
  - Acceptance: At the documented launch dataset, online reads meet p95 500ms and stock posting p95 one second; Android critical flows work on a mid-range device with intermittent connectivity. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: At the documented launch dataset, online reads meet p95 500ms and stock posting p95 one second; Android critical flows work on a mid-range device with intermittent connectivity. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-769 · `backend` · `M50·LIFE` · Safe deployment
  - Depends on: INV-764, INV-765, INV-763.
  - Deliverable: Expand-contract migrations and tested rollback/forward-fix procedures preserve committed stock and valuation history.
  - Acceptance: Expand-contract migrations and tested rollback/forward-fix procedures preserve committed stock and valuation history. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Expand-contract migrations and tested rollback/forward-fix procedures preserve committed stock and valuation history. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-770 · `design` · `M50·DESIGN` · Reliability, recovery and performance: screen design
  - Depends on: INV-765, INV-146.
  - Deliverable: Approve S-M50-01: list/work queue, detail/history and permitted action forms for Reliability, recovery and performance.
  - Acceptance: Design artifact covers role-denied, loading, empty, failure, offline/pending where relevant and every lifecycle state. Responsive evidence covers 375/768/1280/1920/2560; design reviewer and artifact path recorded.
  - Tests: Keyboard and contrast review; state checklist; task/permission mapping review.
  - Screens: S-M50-01.

- [ ] INV-771 · `frontend` · `M50·BUILD` · Reliability, recovery and performance: accessible user workflows
  - Depends on: INV-764, INV-766, INV-767, INV-768, INV-769, INV-770.
  - Deliverable: Build S-M50-01 over the registered API and lifecycle commands; include list/detail/history/action states.
  - Acceptance: All Reliability, recovery and performance feature actions are reachable by the intended role and have clear validation feedback. No local UI calculation is treated as authoritative stock or monetary posting. Design approval exists before implementation starts.
  - Tests: E2E happy path and denied action; responsive widths; keyboard operation; error recovery.
  - Screens: S-M50-01.

- [ ] INV-772 · `backend` · `M50·NOTIFY` · Reliability, recovery and performance: actionable notifications
  - Depends on: INV-766, INV-767, INV-768, INV-769.
  - Deliverable: Register m50.attention and m50.completed categories for failures requiring action and successful governed completion.
  - Acceptance: Deliver only to currently authorized recipients; retries do not duplicate notices. No notification contains confidential cost or contact information without permission.
  - Tests: Recipient scope; event replay; preference suppression; actionable failure link.

- [ ] INV-773 · `backend` · `M50·ADMIN` · Reliability, recovery and performance: administrative review controls
  - Depends on: INV-771.
  - Deliverable: Provide authorized history, exception review and safe recovery for Reliability, recovery and performance using normal commands.
  - Acceptance: Support cannot directly edit posted balances, bypass approval or impersonate a user silently. Archived records remain inspectable to authorized auditors.
  - Tests: Denied override; approved recovery; audit evidence of support action.

- [ ] INV-774 · `backend` · `M50·AUDIT` · Reliability, recovery and performance: mutation evidence
  - Depends on: INV-766, INV-767, INV-768, INV-769.
  - Deliverable: Declare audit actions for Observability, Backup and recovery, Performance budgets, Safe deployment; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-775 · `backend` · `M50·EVENTS` · Reliability, recovery and performance: versioned domain events
  - Depends on: INV-766, INV-767, INV-768, INV-769.
  - Deliverable: Publish m50.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-776 · `backend` · `M50·PRIVACY` · Reliability, recovery and performance: data classification and retention
  - Depends on: INV-766, INV-767, INV-768, INV-769.
  - Deliverable: Classify all fields in operational_incidents, restore_drills; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-777 · `backend` · `M50·INTEGRATION` · Reliability, recovery and performance: dependency integration
  - Depends on: INV-766, INV-767, INV-768, INV-769, INV-764.
  - Deliverable: Exercise Reliability, recovery and performance with prerequisite modules M08, M45, M46 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-778 · `devops` · `M50·OPERABILITY` · Reliability, recovery and performance: runbook and failure signals
  - Depends on: INV-777.
  - Deliverable: Document deployment/configuration, metrics and recovery for Reliability, recovery and performance; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-779 · `qa` · `M50·QA` · Reliability, recovery and performance: acceptance and invariants
  - Depends on: INV-763, INV-764, INV-765, INV-766, INV-767, INV-768, INV-769, INV-770, INV-771, INV-772, INV-773, INV-774, INV-775, INV-776, INV-777, INV-778.
  - Deliverable: Execute the feature acceptance suite for Reliability, recovery and performance, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 4 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Metrics expose posting latency, lock conflicts, sync lag, dead letters, export failures, backup age and per-tenant resource saturation without PII. Encrypted backups and point-in-time recovery are rehearsed to a separate environment; target RPO is 15 minutes and RTO is four hours. At the documented launch dataset, online reads meet p95 500ms and stock posting p95 one second; Android critical flows work on a mid-range device with intermittent connectivity. Expand-contract migrations and tested rollback/forward-fix procedures preserve committed stock and valuation history.

### M51 · Pilot, training and production release

- [ ] INV-780 · `backend` · `M51·DATA` · Pilot, training and production release: schema and migrations
  - Depends on: INV-730, INV-746, INV-762, INV-779.
  - Deliverable: Create scoped tables pilot_acceptances, release_evidence, indexes, constraints and reversible migrations; see DATABASE_SCHEMA.md.
  - Acceptance: Schema includes the declared fields and scope keys for Pilot, training and production release. Cross-scope references are rejected; migration up/down/up preserves prerequisite schemas.
  - Tests: Migration round-trip; scope FK rejection; uniqueness and precision boundaries.

- [ ] INV-781 · `backend` · `M51·AUTHZ` · Pilot, training and production release: enforce access boundaries
  - Depends on: INV-780.
  - Deliverable: Enforce roles Product owner, Implementation operator and declared tenant/company/warehouse scope for module actions.
  - Acceptance: Default deny for undeclared actions. Every Pilot, training and production release identifier is checked against authorized scope before reads or writes. Non-product engineering artifacts are protected by repository/environment access instead of tenant RLS.
  - Tests: Allowed and denied role cases; cross-tenant/company/warehouse ID substitution where applicable.

- [ ] INV-782 · `ops` · `M51·LIFE` · Pilot scenario coverage
  - Depends on: INV-781, INV-780.
  - Deliverable: Distributor, retailer warehouse and lot/expiry business pilots each sign off purchase-to-stock, order-to-dispatch, returns, counts and exports.
  - Acceptance: Distributor, retailer warehouse and lot/expiry business pilots each sign off purchase-to-stock, order-to-dispatch, returns, counts and exports. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Distributor, retailer warehouse and lot/expiry business pilots each sign off purchase-to-stock, order-to-dispatch, returns, counts and exports. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-783 · `ops` · `M51·LIFE` · Training and support
  - Depends on: INV-781, INV-780.
  - Deliverable: Role-based quick starts, barcode-device setup, offline conflict guidance and escalation contacts are delivered and exercised.
  - Acceptance: Role-based quick starts, barcode-device setup, offline conflict guidance and escalation contacts are delivered and exercised. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: Role-based quick starts, barcode-device setup, offline conflict guidance and escalation contacts are delivered and exercised. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-784 · `ops` · `M51·LIFE` · Production go-live
  - Depends on: INV-781, INV-780.
  - Deliverable: All phase gates pass, critical defects are closed, restore evidence is current and customer acceptance is recorded; failed gates block release.
  - Acceptance: All phase gates pass, critical defects are closed, restore evidence is current and customer acceptance is recorded; failed gates block release. Define allowed transitions and prohibited retries/corrections in the module workflow evidence.
  - Tests: Given valid prerequisites, verify: All phase gates pass, critical defects are closed, restore evidence is current and customer acceptance is recorded; failed gates block release. Repeat, cancel or invalidate the prerequisite; verify rejection/rollback without orphaned effects.

- [ ] INV-785 · `backend` · `M51·AUDIT` · Pilot, training and production release: mutation evidence
  - Depends on: INV-782, INV-783, INV-784.
  - Deliverable: Declare audit actions for Pilot scenario coverage, Training and support, Production go-live; capture actor, scope, request and entity revision.
  - Acceptance: Mutation and audit commit together. Logs redact secrets and protect sensitive before/after fields; actions have stable registry codes.
  - Tests: Injected audit failure rolls back mutation; actor/scope attribution; append-only grants.

- [ ] INV-786 · `backend` · `M51·EVENTS` · Pilot, training and production release: versioned domain events
  - Depends on: INV-782, INV-783, INV-784.
  - Deliverable: Publish m51.changed.v1 after committed state changes through the transactional outbox.
  - Acceptance: Consumers receive tenant/company identifiers and aggregate sequence; no secrets in payload. Same event replay cannot duplicate any stock, notification or external export effect.
  - Tests: Outbox crash/retry; consumer deduplication; schema compatibility.

- [ ] INV-787 · `backend` · `M51·PRIVACY` · Pilot, training and production release: data classification and retention
  - Depends on: INV-782, INV-783, INV-784.
  - Deliverable: Classify all fields in pilot_acceptances, release_evidence; register export and retention/anonymization handlers for actor/contact links.
  - Acceptance: Personal fields are exported only to authorized subjects/admins. Deletion does not erase permitted immutable business evidence; retention policy and holds are explicit.
  - Tests: Subject export; anonymization; hold prevents deletion; tenant offboarding completeness.

- [ ] INV-788 · `backend` · `M51·INTEGRATION` · Pilot, training and production release: dependency integration
  - Depends on: INV-782, INV-783, INV-784.
  - Deliverable: Exercise Pilot, training and production release with prerequisite modules M47, M48, M49, M50 and versioned shared contracts.
  - Acceptance: Prerequisite failure leaves no partially committed business operation. No hidden dependency on a later phase; feature flags block unavailable optional workflows.
  - Tests: Dependency unavailable; end-to-end feature handoff; contract compatibility.

- [ ] INV-789 · `devops` · `M51·OPERABILITY` · Pilot, training and production release: runbook and failure signals
  - Depends on: INV-788.
  - Deliverable: Document deployment/configuration, metrics and recovery for Pilot, training and production release; add module-specific failure and reconciliation diagnostics.
  - Acceptance: An operator can identify failed operations from request IDs without exposing private payloads. Recovery instructions preserve committed records; feature availability and rollback limits are documented.
  - Tests: Runbook rehearsal; failure injection; bounded query/job latency.

- [ ] INV-790 · `qa` · `M51·QA` · Pilot, training and production release: acceptance and invariants
  - Depends on: INV-780, INV-781, INV-782, INV-783, INV-784, INV-785, INV-786, INV-787, INV-788, INV-789.
  - Deliverable: Execute the feature acceptance suite for Pilot, training and production release, plus applicable tenant isolation, precision, idempotency and lifecycle tests.
  - Acceptance: All 3 declared feature scenarios have positive and negative evidence. All applicable phase release gates are attached; no critical/high defect remains.
  - Tests: Distributor, retailer warehouse and lot/expiry business pilots each sign off purchase-to-stock, order-to-dispatch, returns, counts and exports. Role-based quick starts, barcode-device setup, offline conflict guidance and escalation contacts are delivered and exercised. All phase gates pass, critical defects are closed, restore evidence is current and customer acceptance is recorded; failed gates block release. C17: Restore and cutover. Stock, reservations, valuations and export references reconcile; measured RPO <=15 minutes and RTO <=4 hours; no blind restoration over new live movements.
