# API and integration contracts

[ENDPOINTS.md](ENDPOINTS.md) owns every planned route and implementation task. These contracts are a blueprint; each API task produces exact Zod/OpenAPI schemas and generated clients before UI build.

## Common protocol

- Prefix `/api/v1`; JSON UTF-8. Browser uses secure HttpOnly session cookies with CSRF protection; Android uses scoped device tokens. Public integration credentials are scoped, hashed and revocable.
- Authentication exceptions: sign-in, invitation acceptance and password-reset requests are unauthenticated but rate-limited and non-enumerating; MFA challenge must complete before a normal session is issued. Liveness `/health` is public and reveals only service status; `/health/ready` and operational detail are infrastructure-restricted. All other routes require authenticated scope unless their API task explicitly documents a narrower exception.
- Tenant/company context is derived and validated from authenticated membership plus requested context. Warehouse IDs are authorized independently. Cross-tenant object lookups return 404; known but forbidden actions return 403.
- Success: `{data, meta: {requestId, nextCursor?}}`. Error: `{error: {code,message,details?,retryable}, meta:{requestId}}`. Never expose raw SQL or private cross-tenant identifiers.
- Cursor pagination uses stable `(created_at,id)` order; default limit 50, maximum 200. Filtering/sorting use allowlists. Export large datasets asynchronously.
- All mutation requests use `Idempotency-Key`. Mutable aggregate actions additionally include `expectedVersion`. Key scope includes tenant/company/action; payload hash mismatch returns 409. Posted command identifiers are retained with transaction history; non-posting draft command receipts retain 30 days.
- Dates use ISO date or UTC timestamps. IDs are strings; quantity/cost/rate decimals and minor-unit amounts are strings. Omit server-derived totals, actor IDs and balances from writable DTOs.
- Error codes: 401 UNAUTHENTICATED; 403 FORBIDDEN; 404 NOT_FOUND; 409 VERSION_CONFLICT, IDEMPOTENCY_CONFLICT, INSUFFICIENT_STOCK, CLOSED_PERIOD, DUPLICATE_SERIAL; 422 VALIDATION_ERROR, INVALID_TRANSITION, APPROVAL_REQUIRED; 429 RATE_LIMITED with Retry-After; 503 TEMPORARILY_UNAVAILABLE. Business conflicts are never blindly retried.

## Resource and command DTO families

| Family | Required input and behavior | Result |
| --- | --- | --- |
| Master resource creation/edit | Approved domain fields from ENTITIES; validated codes, references and expectedVersion for edits; no stock totals | Authorized resource DTO with ID, version, timestamps |
| Purchase requisition/RFQ/order | Supplier where applicable, currency, requested dates, lines `{productId,quantity,uomId,quotedUnitCost?}`, supplier reference, agreement ID if used | Versioned commercial document, line totals and approval state |
| Sales quotation/order | Customer, currency, price-list reference, requested delivery date, lines `{productId,quantity,uomId,discountRequest?}` | Server-priced document, stock availability and outstanding demand |
| Approval submit/decision | Entity ID/version; decision `{stageId,decision,reason?}`; reject requires reason | Approval instance, document state and next authorized action |
| Receipt/issue validate | Operation ID/version, lines `{lineId,doneQuantity,sourceLocationId?,destinationLocationId,lotId?,serialIds?,ownerId}`, backorder choice, occurrence time | Posted operation, move IDs, new version and backorder reference |
| Reservation | Demand line ID, requested quantity, eligible warehouse, allowPartial | Allocated bucket quantities and unallocated remainder |
| Transfer ship/receive | Transfer version, line quantities, tracking identities and discrepancy reason where applicable | Linked source/transit/destination operations and unresolved remainder |
| Quality disposition | Inspection version, completed checklist/evidence, accepted/rejected quantities, reason | Released/quarantined quantities and linked moves |
| Return authorization/post | Original move IDs, requested quantities, reason and disposition | Cumulative return entitlement and posted return/remaining authorization |
| Counts | Scope/schedule, observations `{bucketIdentity,countedQuantity,observedAt,deviceSequence}`, recount/approval version | Variances, ambiguous observations, approval state and adjustment IDs |
| Routes/waves/replenishment | Versioned rules/steps and scoped inputs; execution commands reference existing task/rule IDs | Draft plan, exception list or linked operation IDs |
| Ownership/intercompany/kit | Source owners/companies/products and explicit quantities, agreement/version, cost basis where ownership changes | Linked documents/moves; never silently merges company ledgers |
| Valuation and landed cost | Open period, method/version or external charge evidence, amount/currency and allocation method | Preview/reconciliation before approved immutable entry IDs |
| Export batch | Period/scope, mapping version, schema version; acknowledgement includes batch ID/checksum/external reference and line statuses | Immutable batch/download metadata and reconciliation state |
| Import | Schema version, file hash/object key, source namespace, dry-run token | Row errors or approved atomic chunks with replay-safe IDs |
| Async jobs | Authorized module request and scoped parameters | 202 `{jobId,statusUrl}`; polling returns pending/running/failed/completed and protected result link |

Every registered endpoint chooses its matching DTO family and defines explicit allowed fields and response schema in its owned API task. Unknown properties are rejected. Entity-generated IDs and domain totals are read-only. Status transitions are commanded, not arbitrary status PATCH values.

## Webhooks and accounting formats

Webhook envelope: `{eventId,eventType,schemaVersion,occurredAt,tenantId,companyId,aggregateId,sequence,data}`. Sign timestamp + raw body with HMAC-SHA256; allow a five-minute clock window, verify constant-time, deduplicate event IDs and allow overlapping secret versions during rotation. Block private/link-local destinations and revalidate redirects/DNS to prevent SSRF.

Accounting CSV v1 columns: batch_id, line_id, entry_id, company_code, business_date, currency, debit_account, credit_account, debit_minor, credit_minor, source_document, source_move, mapping_version. One line may carry only debit or credit; totals balance by batch/currency. UTF-8, quoted fields, explicit schema/version manifest and checksum. Spreadsheet formula prefixes in text cells are escaped. Delivery is not acceptance; acknowledgements identify accepted and rejected line IDs.

Core events include stock.posted.v1, reservation.changed.v1, receipt.inspection_required.v1, order.fulfillment_changed.v1, recall.activated.v1, count.variance_ready.v1 and accounting.batch_ready.v1. Module-specific changed events use the module registry names; all schemas are versioned before publication.

Rate-limit initial defaults: interactive user 120 requests/minute, integration key 300/minute, sync batch at most 100 commands. Posting endpoints also limit concurrent commands per aggregate. Tune only with measured workload and tenant fairness evidence.
