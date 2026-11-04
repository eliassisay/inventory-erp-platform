# Screen inventory and design gate

> Registry baseline 1.0 · 2026-11-04 · 51 modules · 790 tasks · 156 capabilities · 13 phases. Generated; edit registry.json and run `make plan-render`.

Each screen ID includes its list/work queue, detail/history, and action forms. Shared shell/design primitives live in M11/M12. BUILD cannot enter active/review/done state until its design is approved with a real artifact and reviewer. Every screen includes error, empty, denied, loading and relevant lifecycle/offline states.

| ID | Screen family | Surface | Design owner | Build owner | Status | Artifact | Reviewer |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S-M03-01 | Tenants and SaaS entitlements | web, admin | INV-021 | INV-022 | planned | Not designed | Unassigned |
| S-M04-01 | Identity, invitations and devices | web | INV-037 | INV-038 | planned | Not designed | Unassigned |
| S-M05-01 | Scoped roles and permissions | web, admin | INV-053 | INV-054 | planned | Not designed | Unassigned |
| S-M06-01 | Approval policies and decisions | web | INV-069 | INV-070 | planned | Not designed | Unassigned |
| S-M07-01 | Audit and business events | web | INV-085 | INV-086 | planned | Not designed | Unassigned |
| S-M08-01 | Jobs, idempotency and delivery | web | INV-101 | INV-102 | planned | Not designed | Unassigned |
| S-M09-01 | Attachments and collaboration | web | INV-116 | INV-117 | planned | Not designed | Unassigned |
| S-M10-01 | Notifications and preferences | web | INV-131 | INV-132 | planned | Not designed | Unassigned |
| S-M12-01 | Office and admin application shells | web | INV-153 | INV-154 | planned | Not designed | Unassigned |
| S-M13-01 | Android foundation and sync protocol | android | INV-169 | INV-170 | planned | Not designed | Unassigned |
| S-M14-01 | Companies, branches and regional settings | web | INV-186 | INV-187 | planned | Not designed | Unassigned |
| S-M15-01 | Suppliers and customers | web | INV-202 | INV-203 | planned | Not designed | Unassigned |
| S-M16-01 | Products, variants and packaging | web | INV-219 | INV-220 | planned | Not designed | Unassigned |
| S-M17-01 | Units and exact arithmetic | web | INV-235 | INV-236 | planned | Not designed | Unassigned |
| S-M18-01 | Warehouses and location hierarchy | web | INV-251 | INV-252 | planned | Not designed | Unassigned |
| S-M19-01 | Lot, serial and ownership identities | web | INV-267 | INV-268 | planned | Not designed | Unassigned |
| S-M20-01 | Immutable stock ledger and projections | web | INV-284 | INV-285 | planned | Not designed | Unassigned |
| S-M21-01 | Reservations and availability | web | INV-300 | INV-301 | planned | Not designed | Unassigned |
| S-M22-01 | Core receipts, issues and opening stock | web | INV-316 | INV-317 | planned | Not designed | Unassigned |
| S-M23-01 | Transfers and in-transit custody | web | INV-332 | INV-333 | planned | Not designed | Unassigned |
| S-M24-01 | Requisitions, RFQs and purchase orders | web | INV-349 | INV-350 | planned | Not designed | Unassigned |
| S-M25-01 | Supplier receiving and inspection handoff | web | INV-365 | INV-366 | planned | Not designed | Unassigned |
| S-M26-01 | Quality inspections and disposition | web | INV-381 | INV-382 | planned | Not designed | Unassigned |
| S-M27-01 | Sales quotations and orders | web | INV-397 | INV-398 | planned | Not designed | Unassigned |
| S-M28-01 | Pick, pack and dispatch | web | INV-413 | INV-414 | planned | Not designed | Unassigned |
| S-M29-01 | Customer and vendor returns | web | INV-429 | INV-430 | planned | Not designed | Unassigned |
| S-M30-01 | Expiry, recalls and scrap | web | INV-445 | INV-446 | planned | Not designed | Unassigned |
| S-M31-01 | Blind counts and reconciliation | web | INV-461 | INV-462 | planned | Not designed | Unassigned |
| S-M32-01 | Routes, putaway and cross-docking | web | INV-477 | INV-478 | planned | Not designed | Unassigned |
| S-M33-01 | Batch and wave picking | web | INV-493 | INV-494 | planned | Not designed | Unassigned |
| S-M34-01 | Replenishment and demand planning | web | INV-509 | INV-510 | planned | Not designed | Unassigned |
| S-M35-01 | Consignment and owner-separated stock | web | INV-525 | INV-526 | planned | Not designed | Unassigned |
| S-M36-01 | Dropship fulfillment | web | INV-541 | INV-542 | planned | Not designed | Unassigned |
| S-M37-01 | Intercompany trade and transfers | web | INV-557 | INV-558 | planned | Not designed | Unassigned |
| S-M38-01 | Kits without manufacturing | web | INV-573 | INV-574 | planned | Not designed | Unassigned |
| S-M39-01 | Offline Android warehouse workflows | android | INV-589 | INV-590 | planned | Not designed | Unassigned |
| S-M40-01 | Scanners, labels and printer interfaces | android | INV-606 | INV-607 | planned | Not designed | Unassigned |
| S-M41-01 | Valuation methods and subledger | web | INV-624 | INV-625 | planned | Not designed | Unassigned |
| S-M42-01 | Landed costs and revaluation | web | INV-640 | INV-641 | planned | Not designed | Unassigned |
| S-M43-01 | Valuation periods and reconciliation | web | INV-656 | INV-657 | planned | Not designed | Unassigned |
| S-M44-01 | Accounting export batches | web | INV-672 | INV-673 | planned | Not designed | Unassigned |
| S-M45-01 | Operational reports and analytics | web | INV-688 | INV-689 | planned | Not designed | Unassigned |
| S-M46-01 | External APIs, imports and webhooks | web | INV-705 | INV-706 | planned | Not designed | Unassigned |
| S-M47-01 | Customer migration and onboarding | web | INV-721 | INV-722 | planned | Not designed | Unassigned |
| S-M48-01 | SaaS support and customer lifecycle | web, admin | INV-737 | INV-738 | planned | Not designed | Unassigned |
| S-M49-01 | Security, privacy and localization release | web, admin | INV-753 | INV-754 | planned | Not designed | Unassigned |
| S-M50-01 | Reliability, recovery and performance | web, admin | INV-770 | INV-771 | planned | Not designed | Unassigned |
