# Endpoint ownership registry

> Registry baseline 1.0 · 2026-11-04 · 51 modules · 790 tasks · 156 capabilities · 13 phases. Generated; edit registry.json and run `make plan-render`.

All paths are under /api/v1. API_REFERENCE.md supplies request conventions, command DTOs, resource contracts and error semantics. Each endpoint must receive a concrete Zod/OpenAPI schema in its API task before a client is built. Roles listed are personas; PERMISSIONS.md maps them to explicit actions and scope grants.

| Method | Path | Module | Owner task | Intended roles |
| --- | --- | --- | --- | --- |
| POST | /api/v1/tenants | M03 | INV-016 | Platform operator, Tenant admin |
| POST | /api/v1/tenants/{id}/activate | M03 | INV-016 | Platform operator, Tenant admin |
| PUT | /api/v1/tenants/{id}/entitlements | M03 | INV-016 | Platform operator, Tenant admin |
| POST | /api/v1/tenants/{id}/suspend | M03 | INV-016 | Platform operator, Tenant admin |
| POST | /api/v1/invitations | M04 | INV-032 | Tenant admin, Warehouse operator |
| POST | /api/v1/invitations/accept | M04 | INV-032 | Tenant admin, Warehouse operator |
| POST | /api/v1/auth/mfa/enroll | M04 | INV-032 | Tenant admin, Warehouse operator |
| POST | /api/v1/auth/mfa/verify | M04 | INV-032 | Tenant admin, Warehouse operator |
| DELETE | /api/v1/devices/{id}/session | M04 | INV-032 | Tenant admin, Warehouse operator |
| GET | /api/v1/permissions | M05 | INV-048 | Tenant admin |
| POST | /api/v1/roles | M05 | INV-048 | Tenant admin |
| PUT | /api/v1/roles/{id}/permissions | M05 | INV-048 | Tenant admin |
| POST | /api/v1/role-bindings | M05 | INV-048 | Tenant admin |
| POST | /api/v1/approval-policies | M06 | INV-064 | Tenant admin, Approver |
| POST | /api/v1/approvals/{id}/decisions | M06 | INV-064 | Tenant admin, Approver |
| GET | /api/v1/approvals | M06 | INV-064 | Tenant admin, Approver |
| GET | /api/v1/audit-records | M07 | INV-080 | Auditor, Platform operator |
| GET | /api/v1/events/{id} | M07 | INV-080 | Auditor, Platform operator |
| GET | /api/v1/jobs | M08 | INV-096 | Platform operator |
| POST | /api/v1/jobs/{id}/retry | M08 | INV-096 | Platform operator |
| POST | /api/v1/attachments/upload-tickets | M09 | INV-112 | Buyer, Sales clerk, Warehouse supervisor |
| POST | /api/v1/attachments/{id}/finalize | M09 | INV-112 | Buyer, Sales clerk, Warehouse supervisor |
| GET | /api/v1/attachments/{id}/download | M09 | INV-112 | Buyer, Sales clerk, Warehouse supervisor |
| POST | /api/v1/comments | M09 | INV-112 | Buyer, Sales clerk, Warehouse supervisor |
| GET | /api/v1/notifications | M10 | INV-127 | Tenant admin, All staff |
| PATCH | /api/v1/notification-preferences | M10 | INV-127 | Tenant admin, All staff |
| POST | /api/v1/notifications/{id}/read | M10 | INV-127 | Tenant admin, All staff |
| GET | /api/v1/me/context | M12 | INV-148 | All staff, Platform operator |
| PATCH | /api/v1/me/preferences | M12 | INV-148 | All staff, Platform operator |
| POST | /api/v1/sync/register | M13 | INV-164 | Warehouse operator |
| GET | /api/v1/sync/bootstrap | M13 | INV-164 | Warehouse operator |
| GET | /api/v1/sync/changes | M13 | INV-164 | Warehouse operator |
| POST | /api/v1/sync/commands | M13 | INV-164 | Warehouse operator |
| POST | /api/v1/companies | M14 | INV-181 | Tenant admin |
| POST | /api/v1/branches | M14 | INV-181 | Tenant admin |
| PATCH | /api/v1/companies/{id}/settings | M14 | INV-181 | Tenant admin |
| POST | /api/v1/partners | M15 | INV-197 | Buyer, Sales clerk, Tenant admin |
| PATCH | /api/v1/partners/{id} | M15 | INV-197 | Buyer, Sales clerk, Tenant admin |
| POST | /api/v1/partners/{id}/references | M15 | INV-197 | Buyer, Sales clerk, Tenant admin |
| POST | /api/v1/products | M16 | INV-213 | Catalog manager |
| POST | /api/v1/products/{id}/variants | M16 | INV-213 | Catalog manager |
| POST | /api/v1/products/{id}/barcodes | M16 | INV-213 | Catalog manager |
| POST | /api/v1/products/{id}/archive | M16 | INV-213 | Catalog manager |
| GET | /api/v1/units | M17 | INV-230 | Catalog manager |
| POST | /api/v1/units | M17 | INV-230 | Catalog manager |
| POST | /api/v1/exchange-rates | M17 | INV-230 | Catalog manager |
| POST | /api/v1/warehouses | M18 | INV-246 | Warehouse supervisor |
| POST | /api/v1/locations | M18 | INV-246 | Warehouse supervisor |
| POST | /api/v1/locations/{id}/archive | M18 | INV-246 | Warehouse supervisor |
| POST | /api/v1/lots | M19 | INV-262 | Catalog manager, Warehouse supervisor |
| POST | /api/v1/serials | M19 | INV-262 | Catalog manager, Warehouse supervisor |
| GET | /api/v1/tracking-identities | M19 | INV-262 | Catalog manager, Warehouse supervisor |
| GET | /api/v1/stock/moves | M20 | INV-278 | Warehouse supervisor, Auditor |
| GET | /api/v1/stock/balances | M20 | INV-278 | Warehouse supervisor, Auditor |
| POST | /api/v1/stock/moves/{id}/reverse | M20 | INV-278 | Warehouse supervisor, Auditor |
| POST | /api/v1/reservations | M21 | INV-295 | Sales clerk, Warehouse supervisor |
| POST | /api/v1/reservations/{id}/release | M21 | INV-295 | Sales clerk, Warehouse supervisor |
| GET | /api/v1/stock/availability | M21 | INV-295 | Sales clerk, Warehouse supervisor |
| GET | /api/v1/stock/forecast | M21 | INV-295 | Sales clerk, Warehouse supervisor |
| POST | /api/v1/stock/operations | M22 | INV-311 | Warehouse operator, Warehouse supervisor |
| POST | /api/v1/stock/operations/{id}/validate | M22 | INV-311 | Warehouse operator, Warehouse supervisor |
| POST | /api/v1/stock/opening-batches | M22 | INV-311 | Warehouse operator, Warehouse supervisor |
| POST | /api/v1/stock/operations/{id}/cancel | M22 | INV-311 | Warehouse operator, Warehouse supervisor |
| POST | /api/v1/transfers | M23 | INV-327 | Warehouse operator, Warehouse supervisor |
| POST | /api/v1/transfers/{id}/ship | M23 | INV-327 | Warehouse operator, Warehouse supervisor |
| POST | /api/v1/transfers/{id}/receive | M23 | INV-327 | Warehouse operator, Warehouse supervisor |
| POST | /api/v1/transfers/{id}/resolve-discrepancy | M23 | INV-327 | Warehouse operator, Warehouse supervisor |
| POST | /api/v1/purchase/requisitions | M24 | INV-343 | Requester, Buyer, Approver |
| POST | /api/v1/purchase/rfqs | M24 | INV-343 | Requester, Buyer, Approver |
| POST | /api/v1/purchase/rfqs/{id}/compare | M24 | INV-343 | Requester, Buyer, Approver |
| POST | /api/v1/purchase/orders | M24 | INV-343 | Requester, Buyer, Approver |
| POST | /api/v1/purchase/orders/{id}/submit | M24 | INV-343 | Requester, Buyer, Approver |
| POST | /api/v1/purchase/agreements | M24 | INV-343 | Requester, Buyer, Approver |
| POST | /api/v1/purchase/orders/{id}/receipts | M25 | INV-360 | Warehouse operator, Warehouse supervisor |
| POST | /api/v1/receipts/{id}/validate | M25 | INV-360 | Warehouse operator, Warehouse supervisor |
| GET | /api/v1/purchase/orders/{id}/receiving-status | M25 | INV-360 | Warehouse operator, Warehouse supervisor |
| POST | /api/v1/quality/plans | M26 | INV-376 | Quality inspector, Warehouse supervisor |
| POST | /api/v1/inspections/{id}/results | M26 | INV-376 | Quality inspector, Warehouse supervisor |
| POST | /api/v1/inspections/{id}/release | M26 | INV-376 | Quality inspector, Warehouse supervisor |
| POST | /api/v1/inspections/{id}/reject | M26 | INV-376 | Quality inspector, Warehouse supervisor |
| POST | /api/v1/sales/quotations | M27 | INV-392 | Sales clerk, Sales manager |
| POST | /api/v1/sales/quotations/{id}/confirm | M27 | INV-392 | Sales clerk, Sales manager |
| POST | /api/v1/sales/orders/{id}/allocate | M27 | INV-392 | Sales clerk, Sales manager |
| POST | /api/v1/sales/orders/{id}/cancel | M27 | INV-392 | Sales clerk, Sales manager |
| POST | /api/v1/sales/price-lists | M27 | INV-392 | Sales clerk, Sales manager |
| GET | /api/v1/pick-tasks | M28 | INV-408 | Picker, Packer, Dispatcher |
| POST | /api/v1/pick-tasks/{id}/confirm | M28 | INV-408 | Picker, Packer, Dispatcher |
| POST | /api/v1/packages | M28 | INV-408 | Picker, Packer, Dispatcher |
| POST | /api/v1/dispatches/{id}/validate | M28 | INV-408 | Picker, Packer, Dispatcher |
| POST | /api/v1/returns | M29 | INV-424 | Sales clerk, Buyer, Warehouse supervisor |
| POST | /api/v1/returns/{id}/authorize | M29 | INV-424 | Sales clerk, Buyer, Warehouse supervisor |
| POST | /api/v1/returns/{id}/receive | M29 | INV-424 | Sales clerk, Buyer, Warehouse supervisor |
| POST | /api/v1/returns/{id}/ship | M29 | INV-424 | Sales clerk, Buyer, Warehouse supervisor |
| GET | /api/v1/traceability | M30 | INV-440 | Quality inspector, Warehouse supervisor, Approver |
| POST | /api/v1/recalls | M30 | INV-440 | Quality inspector, Warehouse supervisor, Approver |
| POST | /api/v1/recalls/{id}/close | M30 | INV-440 | Quality inspector, Warehouse supervisor, Approver |
| POST | /api/v1/scrap | M30 | INV-440 | Quality inspector, Warehouse supervisor, Approver |
| POST | /api/v1/scrap/{id}/post | M30 | INV-440 | Quality inspector, Warehouse supervisor, Approver |
| POST | /api/v1/counts | M31 | INV-456 | Counter, Warehouse supervisor, Approver |
| POST | /api/v1/counts/{id}/start | M31 | INV-456 | Counter, Warehouse supervisor, Approver |
| POST | /api/v1/counts/{id}/lines | M31 | INV-456 | Counter, Warehouse supervisor, Approver |
| POST | /api/v1/counts/{id}/recount | M31 | INV-456 | Counter, Warehouse supervisor, Approver |
| POST | /api/v1/counts/{id}/approve | M31 | INV-456 | Counter, Warehouse supervisor, Approver |
| POST | /api/v1/counts/{id}/post | M31 | INV-456 | Counter, Warehouse supervisor, Approver |
| POST | /api/v1/warehouse-routes | M32 | INV-472 | Warehouse supervisor |
| POST | /api/v1/putaway-rules | M32 | INV-472 | Warehouse supervisor |
| POST | /api/v1/cross-dock-allocations | M32 | INV-472 | Warehouse supervisor |
| POST | /api/v1/picking-waves | M33 | INV-488 | Warehouse supervisor, Picker |
| POST | /api/v1/picking-waves/{id}/release | M33 | INV-488 | Warehouse supervisor, Picker |
| POST | /api/v1/pick-batches/{id}/assign | M33 | INV-488 | Warehouse supervisor, Picker |
| POST | /api/v1/reorder-rules | M34 | INV-504 | Buyer, Warehouse supervisor |
| POST | /api/v1/replenishment/run | M34 | INV-504 | Buyer, Warehouse supervisor |
| POST | /api/v1/replenishment/{id}/accept | M34 | INV-504 | Buyer, Warehouse supervisor |
| GET | /api/v1/stock/shortages | M34 | INV-504 | Buyer, Warehouse supervisor |
| POST | /api/v1/consignment-agreements | M35 | INV-520 | Buyer, Warehouse supervisor |
| POST | /api/v1/stock/ownership-changes | M35 | INV-520 | Buyer, Warehouse supervisor |
| GET | /api/v1/stock/by-owner | M35 | INV-520 | Buyer, Warehouse supervisor |
| POST | /api/v1/sales/orders/{id}/dropship | M36 | INV-536 | Buyer, Sales clerk |
| POST | /api/v1/dropships/{id}/confirm | M36 | INV-536 | Buyer, Sales clerk |
| POST | /api/v1/intercompany/orders | M37 | INV-552 | Company admin, Buyer, Sales manager |
| POST | /api/v1/intercompany/{id}/approve | M37 | INV-552 | Company admin, Buyer, Sales manager |
| GET | /api/v1/intercompany/{id}/reconciliation | M37 | INV-552 | Company admin, Buyer, Sales manager |
| POST | /api/v1/kits | M38 | INV-568 | Catalog manager, Sales clerk |
| POST | /api/v1/kits/{id}/activate | M38 | INV-568 | Catalog manager, Sales clerk |
| GET | /api/v1/kits/{id}/availability | M38 | INV-568 | Catalog manager, Sales clerk |
| GET | /api/v1/mobile/assignments | M39 | INV-584 | Warehouse operator, Counter |
| POST | /api/v1/mobile/conflicts/{id}/resolve | M39 | INV-584 | Warehouse operator, Counter |
| POST | /api/v1/mobile/assignments/{id}/acknowledge | M39 | INV-584 | Warehouse operator, Counter |
| POST | /api/v1/labels/preview | M40 | INV-601 | Warehouse operator, Warehouse supervisor |
| POST | /api/v1/print-jobs | M40 | INV-601 | Warehouse operator, Warehouse supervisor |
| POST | /api/v1/print-jobs/{id}/reprint | M40 | INV-601 | Warehouse operator, Warehouse supervisor |
| GET | /api/v1/valuation/layers | M41 | INV-618 | Valuation analyst, Auditor |
| GET | /api/v1/valuation/entries | M41 | INV-618 | Valuation analyst, Auditor |
| POST | /api/v1/valuation/rebuild | M41 | INV-618 | Valuation analyst, Auditor |
| POST | /api/v1/valuation/policies | M41 | INV-618 | Valuation analyst, Auditor |
| POST | /api/v1/landed-costs | M42 | INV-635 | Valuation analyst, Approver |
| POST | /api/v1/landed-costs/{id}/allocate | M42 | INV-635 | Valuation analyst, Approver |
| POST | /api/v1/landed-costs/{id}/post | M42 | INV-635 | Valuation analyst, Approver |
| POST | /api/v1/valuation/revaluations | M42 | INV-635 | Valuation analyst, Approver |
| POST | /api/v1/valuation/periods/{id}/reconcile | M43 | INV-651 | Valuation analyst, Approver, Auditor |
| POST | /api/v1/valuation/periods/{id}/close | M43 | INV-651 | Valuation analyst, Approver, Auditor |
| POST | /api/v1/valuation/periods/{id}/reopen | M43 | INV-651 | Valuation analyst, Approver, Auditor |
| POST | /api/v1/accounting/export-batches | M44 | INV-667 | Valuation analyst, Integration operator |
| GET | /api/v1/accounting/export-batches/{id}/download | M44 | INV-667 | Valuation analyst, Integration operator |
| POST | /api/v1/accounting/export-batches/{id}/acknowledge | M44 | INV-667 | Valuation analyst, Integration operator |
| POST | /api/v1/accounting/export-batches/{id}/retry | M44 | INV-667 | Valuation analyst, Integration operator |
| GET | /api/v1/reports/stock-card | M45 | INV-683 | Warehouse supervisor, Buyer, Sales manager, Valuation analyst, Auditor |
| GET | /api/v1/reports/aging | M45 | INV-683 | Warehouse supervisor, Buyer, Sales manager, Valuation analyst, Auditor |
| GET | /api/v1/reports/expiry | M45 | INV-683 | Warehouse supervisor, Buyer, Sales manager, Valuation analyst, Auditor |
| GET | /api/v1/reports/fulfillment | M45 | INV-683 | Warehouse supervisor, Buyer, Sales manager, Valuation analyst, Auditor |
| GET | /api/v1/reports/supplier-performance | M45 | INV-683 | Warehouse supervisor, Buyer, Sales manager, Valuation analyst, Auditor |
| POST | /api/v1/reports/exports | M45 | INV-683 | Warehouse supervisor, Buyer, Sales manager, Valuation analyst, Auditor |
| POST | /api/v1/api-credentials | M46 | INV-699 | Integration operator |
| POST | /api/v1/webhook-subscriptions | M46 | INV-699 | Integration operator |
| POST | /api/v1/imports/dry-run | M46 | INV-699 | Integration operator |
| POST | /api/v1/imports/{id}/commit | M46 | INV-699 | Integration operator |
| GET | /api/v1/integration-deliveries | M46 | INV-699 | Integration operator |
| POST | /api/v1/migration-runs | M47 | INV-716 | Implementation operator, Tenant admin |
| POST | /api/v1/migration-runs/{id}/validate | M47 | INV-716 | Implementation operator, Tenant admin |
| POST | /api/v1/migration-runs/{id}/approve-cutover | M47 | INV-716 | Implementation operator, Tenant admin |
| POST | /api/v1/support-sessions | M48 | INV-732 | Platform operator, Tenant admin |
| POST | /api/v1/tenant-exports | M48 | INV-732 | Platform operator, Tenant admin |
| POST | /api/v1/offboarding-requests | M48 | INV-732 | Platform operator, Tenant admin |
| GET | /api/v1/usage | M48 | INV-732 | Platform operator, Tenant admin |
| POST | /api/v1/privacy-requests | M49 | INV-748 | Security reviewer, Compliance reviewer |
| GET | /api/v1/privacy-requests/{id} | M49 | INV-748 | Security reviewer, Compliance reviewer |
| POST | /api/v1/compliance-reviews | M49 | INV-748 | Security reviewer, Compliance reviewer |
| GET | /api/v1/health | M50 | INV-764 | Platform operator, Engineer |
| GET | /api/v1/health/ready | M50 | INV-764 | Platform operator, Engineer |
| GET | /api/v1/operations/status | M50 | INV-764 | Platform operator, Engineer |
| GET | /api/v1/tenants | M03 | INV-016 | Platform operator, Tenant admin |
| GET | /api/v1/tenants/{id} | M03 | INV-016 | Platform operator, Tenant admin |
| GET | /api/v1/subscriptions | M03 | INV-016 | Platform operator, Tenant admin |
| GET | /api/v1/subscriptions/{id} | M03 | INV-016 | Platform operator, Tenant admin |
| GET | /api/v1/invitations | M04 | INV-032 | Tenant admin, Warehouse operator |
| GET | /api/v1/invitations/{id} | M04 | INV-032 | Tenant admin, Warehouse operator |
| GET | /api/v1/devices | M04 | INV-032 | Tenant admin, Warehouse operator |
| GET | /api/v1/devices/{id} | M04 | INV-032 | Tenant admin, Warehouse operator |
| POST | /api/v1/auth/sign-in | M04 | INV-032 | Tenant admin, Warehouse operator |
| POST | /api/v1/auth/sign-out | M04 | INV-032 | Tenant admin, Warehouse operator |
| GET | /api/v1/auth/session | M04 | INV-032 | Tenant admin, Warehouse operator |
| POST | /api/v1/auth/password-reset/request | M04 | INV-032 | Tenant admin, Warehouse operator |
| POST | /api/v1/auth/password-reset/confirm | M04 | INV-032 | Tenant admin, Warehouse operator |
| GET | /api/v1/roles | M05 | INV-048 | Tenant admin |
| GET | /api/v1/roles/{id} | M05 | INV-048 | Tenant admin |
| GET | /api/v1/role-bindings | M05 | INV-048 | Tenant admin |
| GET | /api/v1/role-bindings/{id} | M05 | INV-048 | Tenant admin |
| GET | /api/v1/approval-policies | M06 | INV-064 | Tenant admin, Approver |
| GET | /api/v1/approval-policies/{id} | M06 | INV-064 | Tenant admin, Approver |
| GET | /api/v1/approvals/{id} | M06 | INV-064 | Tenant admin, Approver |
| GET | /api/v1/audit-records/{id} | M07 | INV-080 | Auditor, Platform operator |
| GET | /api/v1/jobs/{id} | M08 | INV-096 | Platform operator |
| GET | /api/v1/attachments | M09 | INV-112 | Buyer, Sales clerk, Warehouse supervisor |
| GET | /api/v1/attachments/{id} | M09 | INV-112 | Buyer, Sales clerk, Warehouse supervisor |
| GET | /api/v1/comments | M09 | INV-112 | Buyer, Sales clerk, Warehouse supervisor |
| GET | /api/v1/comments/{id} | M09 | INV-112 | Buyer, Sales clerk, Warehouse supervisor |
| GET | /api/v1/notifications/{id} | M10 | INV-127 | Tenant admin, All staff |
| GET | /api/v1/saved-views | M12 | INV-148 | All staff, Platform operator |
| GET | /api/v1/saved-views/{id} | M12 | INV-148 | All staff, Platform operator |
| POST | /api/v1/saved-views | M12 | INV-148 | All staff, Platform operator |
| DELETE | /api/v1/saved-views/{id} | M12 | INV-148 | All staff, Platform operator |
| GET | /api/v1/companies | M14 | INV-181 | Tenant admin |
| GET | /api/v1/companies/{id} | M14 | INV-181 | Tenant admin |
| GET | /api/v1/branches | M14 | INV-181 | Tenant admin |
| GET | /api/v1/branches/{id} | M14 | INV-181 | Tenant admin |
| GET | /api/v1/partners | M15 | INV-197 | Buyer, Sales clerk, Tenant admin |
| GET | /api/v1/partners/{id} | M15 | INV-197 | Buyer, Sales clerk, Tenant admin |
| GET | /api/v1/products | M16 | INV-213 | Catalog manager |
| GET | /api/v1/products/{id} | M16 | INV-213 | Catalog manager |
| GET | /api/v1/product-categories | M16 | INV-213 | Catalog manager |
| GET | /api/v1/product-categories/{id} | M16 | INV-213 | Catalog manager |
| POST | /api/v1/product-categories | M16 | INV-213 | Catalog manager |
| PATCH | /api/v1/products/{id} | M16 | INV-213 | Catalog manager |
| PATCH | /api/v1/product-categories/{id} | M16 | INV-213 | Catalog manager |
| GET | /api/v1/units/{id} | M17 | INV-230 | Catalog manager |
| GET | /api/v1/exchange-rates | M17 | INV-230 | Catalog manager |
| GET | /api/v1/exchange-rates/{id} | M17 | INV-230 | Catalog manager |
| GET | /api/v1/warehouses | M18 | INV-246 | Warehouse supervisor |
| GET | /api/v1/warehouses/{id} | M18 | INV-246 | Warehouse supervisor |
| GET | /api/v1/locations | M18 | INV-246 | Warehouse supervisor |
| GET | /api/v1/locations/{id} | M18 | INV-246 | Warehouse supervisor |
| PATCH | /api/v1/warehouses/{id} | M18 | INV-246 | Warehouse supervisor |
| PATCH | /api/v1/locations/{id} | M18 | INV-246 | Warehouse supervisor |
| GET | /api/v1/lots | M19 | INV-262 | Catalog manager, Warehouse supervisor |
| GET | /api/v1/lots/{id} | M19 | INV-262 | Catalog manager, Warehouse supervisor |
| GET | /api/v1/serials | M19 | INV-262 | Catalog manager, Warehouse supervisor |
| GET | /api/v1/serials/{id} | M19 | INV-262 | Catalog manager, Warehouse supervisor |
| GET | /api/v1/stock/moves/{id} | M20 | INV-278 | Warehouse supervisor, Auditor |
| GET | /api/v1/reservations | M21 | INV-295 | Sales clerk, Warehouse supervisor |
| GET | /api/v1/reservations/{id} | M21 | INV-295 | Sales clerk, Warehouse supervisor |
| GET | /api/v1/stock/operations | M22 | INV-311 | Warehouse operator, Warehouse supervisor |
| GET | /api/v1/stock/operations/{id} | M22 | INV-311 | Warehouse operator, Warehouse supervisor |
| GET | /api/v1/stock/opening-batches | M22 | INV-311 | Warehouse operator, Warehouse supervisor |
| GET | /api/v1/stock/opening-batches/{id} | M22 | INV-311 | Warehouse operator, Warehouse supervisor |
| GET | /api/v1/transfers | M23 | INV-327 | Warehouse operator, Warehouse supervisor |
| GET | /api/v1/transfers/{id} | M23 | INV-327 | Warehouse operator, Warehouse supervisor |
| GET | /api/v1/purchase/requisitions | M24 | INV-343 | Requester, Buyer, Approver |
| GET | /api/v1/purchase/requisitions/{id} | M24 | INV-343 | Requester, Buyer, Approver |
| GET | /api/v1/purchase/rfqs | M24 | INV-343 | Requester, Buyer, Approver |
| GET | /api/v1/purchase/rfqs/{id} | M24 | INV-343 | Requester, Buyer, Approver |
| GET | /api/v1/purchase/orders | M24 | INV-343 | Requester, Buyer, Approver |
| GET | /api/v1/purchase/orders/{id} | M24 | INV-343 | Requester, Buyer, Approver |
| GET | /api/v1/purchase/agreements | M24 | INV-343 | Requester, Buyer, Approver |
| GET | /api/v1/purchase/agreements/{id} | M24 | INV-343 | Requester, Buyer, Approver |
| PATCH | /api/v1/purchase/orders/{id} | M24 | INV-343 | Requester, Buyer, Approver |
| POST | /api/v1/purchase/orders/{id}/cancel | M24 | INV-343 | Requester, Buyer, Approver |
| GET | /api/v1/receipts | M25 | INV-360 | Warehouse operator, Warehouse supervisor |
| GET | /api/v1/receipts/{id} | M25 | INV-360 | Warehouse operator, Warehouse supervisor |
| GET | /api/v1/quality/plans | M26 | INV-376 | Quality inspector, Warehouse supervisor |
| GET | /api/v1/quality/plans/{id} | M26 | INV-376 | Quality inspector, Warehouse supervisor |
| GET | /api/v1/inspections | M26 | INV-376 | Quality inspector, Warehouse supervisor |
| GET | /api/v1/inspections/{id} | M26 | INV-376 | Quality inspector, Warehouse supervisor |
| GET | /api/v1/sales/quotations | M27 | INV-392 | Sales clerk, Sales manager |
| GET | /api/v1/sales/quotations/{id} | M27 | INV-392 | Sales clerk, Sales manager |
| GET | /api/v1/sales/orders | M27 | INV-392 | Sales clerk, Sales manager |
| GET | /api/v1/sales/orders/{id} | M27 | INV-392 | Sales clerk, Sales manager |
| GET | /api/v1/sales/price-lists | M27 | INV-392 | Sales clerk, Sales manager |
| GET | /api/v1/sales/price-lists/{id} | M27 | INV-392 | Sales clerk, Sales manager |
| PATCH | /api/v1/sales/orders/{id} | M27 | INV-392 | Sales clerk, Sales manager |
| GET | /api/v1/pick-tasks/{id} | M28 | INV-408 | Picker, Packer, Dispatcher |
| GET | /api/v1/packages | M28 | INV-408 | Picker, Packer, Dispatcher |
| GET | /api/v1/packages/{id} | M28 | INV-408 | Picker, Packer, Dispatcher |
| GET | /api/v1/dispatches | M28 | INV-408 | Picker, Packer, Dispatcher |
| GET | /api/v1/dispatches/{id} | M28 | INV-408 | Picker, Packer, Dispatcher |
| GET | /api/v1/returns | M29 | INV-424 | Sales clerk, Buyer, Warehouse supervisor |
| GET | /api/v1/returns/{id} | M29 | INV-424 | Sales clerk, Buyer, Warehouse supervisor |
| GET | /api/v1/recalls | M30 | INV-440 | Quality inspector, Warehouse supervisor, Approver |
| GET | /api/v1/recalls/{id} | M30 | INV-440 | Quality inspector, Warehouse supervisor, Approver |
| GET | /api/v1/scrap | M30 | INV-440 | Quality inspector, Warehouse supervisor, Approver |
| GET | /api/v1/scrap/{id} | M30 | INV-440 | Quality inspector, Warehouse supervisor, Approver |
| GET | /api/v1/counts | M31 | INV-456 | Counter, Warehouse supervisor, Approver |
| GET | /api/v1/counts/{id} | M31 | INV-456 | Counter, Warehouse supervisor, Approver |
| GET | /api/v1/warehouse-routes | M32 | INV-472 | Warehouse supervisor |
| GET | /api/v1/warehouse-routes/{id} | M32 | INV-472 | Warehouse supervisor |
| GET | /api/v1/putaway-rules | M32 | INV-472 | Warehouse supervisor |
| GET | /api/v1/putaway-rules/{id} | M32 | INV-472 | Warehouse supervisor |
| GET | /api/v1/picking-waves | M33 | INV-488 | Warehouse supervisor, Picker |
| GET | /api/v1/picking-waves/{id} | M33 | INV-488 | Warehouse supervisor, Picker |
| GET | /api/v1/pick-batches | M33 | INV-488 | Warehouse supervisor, Picker |
| GET | /api/v1/pick-batches/{id} | M33 | INV-488 | Warehouse supervisor, Picker |
| GET | /api/v1/reorder-rules | M34 | INV-504 | Buyer, Warehouse supervisor |
| GET | /api/v1/reorder-rules/{id} | M34 | INV-504 | Buyer, Warehouse supervisor |
| GET | /api/v1/replenishment | M34 | INV-504 | Buyer, Warehouse supervisor |
| GET | /api/v1/replenishment/{id} | M34 | INV-504 | Buyer, Warehouse supervisor |
| GET | /api/v1/consignment-agreements | M35 | INV-520 | Buyer, Warehouse supervisor |
| GET | /api/v1/consignment-agreements/{id} | M35 | INV-520 | Buyer, Warehouse supervisor |
| GET | /api/v1/stock/ownership-changes | M35 | INV-520 | Buyer, Warehouse supervisor |
| GET | /api/v1/stock/ownership-changes/{id} | M35 | INV-520 | Buyer, Warehouse supervisor |
| GET | /api/v1/dropships | M36 | INV-536 | Buyer, Sales clerk |
| GET | /api/v1/dropships/{id} | M36 | INV-536 | Buyer, Sales clerk |
| GET | /api/v1/intercompany | M37 | INV-552 | Company admin, Buyer, Sales manager |
| GET | /api/v1/intercompany/{id} | M37 | INV-552 | Company admin, Buyer, Sales manager |
| GET | /api/v1/kits | M38 | INV-568 | Catalog manager, Sales clerk |
| GET | /api/v1/kits/{id} | M38 | INV-568 | Catalog manager, Sales clerk |
| PATCH | /api/v1/kits/{id} | M38 | INV-568 | Catalog manager, Sales clerk |
| GET | /api/v1/mobile/assignments/{id} | M39 | INV-584 | Warehouse operator, Counter |
| GET | /api/v1/mobile/conflicts | M39 | INV-584 | Warehouse operator, Counter |
| GET | /api/v1/mobile/conflicts/{id} | M39 | INV-584 | Warehouse operator, Counter |
| GET | /api/v1/print-jobs | M40 | INV-601 | Warehouse operator, Warehouse supervisor |
| GET | /api/v1/print-jobs/{id} | M40 | INV-601 | Warehouse operator, Warehouse supervisor |
| GET | /api/v1/label-templates | M40 | INV-601 | Warehouse operator, Warehouse supervisor |
| GET | /api/v1/label-templates/{id} | M40 | INV-601 | Warehouse operator, Warehouse supervisor |
| POST | /api/v1/label-templates | M40 | INV-601 | Warehouse operator, Warehouse supervisor |
| GET | /api/v1/valuation/policies | M41 | INV-618 | Valuation analyst, Auditor |
| GET | /api/v1/valuation/policies/{id} | M41 | INV-618 | Valuation analyst, Auditor |
| GET | /api/v1/valuation/layers/{id} | M41 | INV-618 | Valuation analyst, Auditor |
| POST | /api/v1/valuation/policies/{id}/approve | M41 | INV-618 | Valuation analyst, Auditor |
| GET | /api/v1/landed-costs | M42 | INV-635 | Valuation analyst, Approver |
| GET | /api/v1/landed-costs/{id} | M42 | INV-635 | Valuation analyst, Approver |
| GET | /api/v1/valuation/revaluations | M42 | INV-635 | Valuation analyst, Approver |
| GET | /api/v1/valuation/revaluations/{id} | M42 | INV-635 | Valuation analyst, Approver |
| GET | /api/v1/valuation/periods | M43 | INV-651 | Valuation analyst, Approver, Auditor |
| GET | /api/v1/valuation/periods/{id} | M43 | INV-651 | Valuation analyst, Approver, Auditor |
| GET | /api/v1/accounting/export-batches | M44 | INV-667 | Valuation analyst, Integration operator |
| GET | /api/v1/accounting/export-batches/{id} | M44 | INV-667 | Valuation analyst, Integration operator |
| GET | /api/v1/accounting/mappings | M44 | INV-667 | Valuation analyst, Integration operator |
| GET | /api/v1/accounting/mappings/{id} | M44 | INV-667 | Valuation analyst, Integration operator |
| PUT | /api/v1/accounting/mappings | M44 | INV-667 | Valuation analyst, Integration operator |
| GET | /api/v1/reports/jobs | M45 | INV-683 | Warehouse supervisor, Buyer, Sales manager, Valuation analyst, Auditor |
| GET | /api/v1/reports/jobs/{id} | M45 | INV-683 | Warehouse supervisor, Buyer, Sales manager, Valuation analyst, Auditor |
| GET | /api/v1/api-credentials | M46 | INV-699 | Integration operator |
| GET | /api/v1/api-credentials/{id} | M46 | INV-699 | Integration operator |
| GET | /api/v1/webhook-subscriptions | M46 | INV-699 | Integration operator |
| GET | /api/v1/webhook-subscriptions/{id} | M46 | INV-699 | Integration operator |
| GET | /api/v1/imports | M46 | INV-699 | Integration operator |
| GET | /api/v1/imports/{id} | M46 | INV-699 | Integration operator |
| DELETE | /api/v1/api-credentials/{id} | M46 | INV-699 | Integration operator |
| POST | /api/v1/webhook-subscriptions/{id}/rotate-secret | M46 | INV-699 | Integration operator |
| GET | /api/v1/migration-runs | M47 | INV-716 | Implementation operator, Tenant admin |
| GET | /api/v1/migration-runs/{id} | M47 | INV-716 | Implementation operator, Tenant admin |
| GET | /api/v1/support-sessions | M48 | INV-732 | Platform operator, Tenant admin |
| GET | /api/v1/support-sessions/{id} | M48 | INV-732 | Platform operator, Tenant admin |
| GET | /api/v1/tenant-exports | M48 | INV-732 | Platform operator, Tenant admin |
| GET | /api/v1/tenant-exports/{id} | M48 | INV-732 | Platform operator, Tenant admin |
| GET | /api/v1/offboarding-requests | M48 | INV-732 | Platform operator, Tenant admin |
| GET | /api/v1/offboarding-requests/{id} | M48 | INV-732 | Platform operator, Tenant admin |
| GET | /api/v1/privacy-requests | M49 | INV-748 | Security reviewer, Compliance reviewer |
| GET | /api/v1/compliance-reviews | M49 | INV-748 | Security reviewer, Compliance reviewer |
| GET | /api/v1/compliance-reviews/{id} | M49 | INV-748 | Security reviewer, Compliance reviewer |
| GET | /api/v1/operations/incidents | M50 | INV-764 | Platform operator, Engineer |
| GET | /api/v1/operations/incidents/{id} | M50 | INV-764 | Platform operator, Engineer |
