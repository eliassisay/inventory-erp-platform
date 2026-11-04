# Permission and role ownership

> Registry baseline 1.0 · 2026-11-04 · 51 modules · 790 tasks · 156 capabilities · 13 phases. Generated; edit registry.json and run `make plan-render`.

Each module permission family uses `<module>.view`, `.manage`, `.submit`, `.approve`, `.post`, `.export` only where the action exists. The AUTHZ task declares concrete route/action permissions before use; roles never bypass scope checks. See PERMISSIONS.md for default persona grants and independent approval rules.

| Module | Roles | AUTHZ task | Approval/lifecycle owners |
| --- | --- | --- | --- |
| M01 Product baseline and localization | Product owner, Compliance reviewer | INV-001 | INV-002, INV-003, INV-004 |
| M02 Repository and delivery tooling | Engineer | INV-008 | INV-009, INV-010, INV-011 |
| M03 Tenants and SaaS entitlements | Platform operator, Tenant admin | INV-017 | INV-018, INV-019, INV-020 |
| M04 Identity, invitations and devices | Tenant admin, Warehouse operator | INV-033 | INV-034, INV-035, INV-036 |
| M05 Scoped roles and permissions | Tenant admin | INV-049 | INV-050, INV-051, INV-052 |
| M06 Approval policies and decisions | Tenant admin, Approver | INV-065 | INV-066, INV-067, INV-068 |
| M07 Audit and business events | Auditor, Platform operator | INV-081 | INV-082, INV-083, INV-084 |
| M08 Jobs, idempotency and delivery | Platform operator | INV-097 | INV-098, INV-099, INV-100 |
| M09 Attachments and collaboration | Buyer, Sales clerk, Warehouse supervisor | INV-113 | INV-114, INV-115 |
| M10 Notifications and preferences | Tenant admin, All staff | INV-128 | INV-129, INV-130 |
| M11 Design system and accessibility | Designer | INV-141 | INV-142, INV-143 |
| M12 Office and admin application shells | All staff, Platform operator | INV-149 | INV-150, INV-151, INV-152 |
| M13 Android foundation and sync protocol | Warehouse operator | INV-165 | INV-166, INV-167, INV-168 |
| M14 Companies, branches and regional settings | Tenant admin | INV-182 | INV-183, INV-184, INV-185 |
| M15 Suppliers and customers | Buyer, Sales clerk, Tenant admin | INV-198 | INV-199, INV-200, INV-201 |
| M16 Products, variants and packaging | Catalog manager | INV-214 | INV-215, INV-216, INV-217, INV-218 |
| M17 Units and exact arithmetic | Catalog manager | INV-231 | INV-232, INV-233, INV-234 |
| M18 Warehouses and location hierarchy | Warehouse supervisor | INV-247 | INV-248, INV-249, INV-250 |
| M19 Lot, serial and ownership identities | Catalog manager, Warehouse supervisor | INV-263 | INV-264, INV-265, INV-266 |
| M20 Immutable stock ledger and projections | Warehouse supervisor, Auditor | INV-279 | INV-280, INV-281, INV-282, INV-283 |
| M21 Reservations and availability | Sales clerk, Warehouse supervisor | INV-296 | INV-297, INV-298, INV-299 |
| M22 Core receipts, issues and opening stock | Warehouse operator, Warehouse supervisor | INV-312 | INV-313, INV-314, INV-315 |
| M23 Transfers and in-transit custody | Warehouse operator, Warehouse supervisor | INV-328 | INV-329, INV-330, INV-331 |
| M24 Requisitions, RFQs and purchase orders | Requester, Buyer, Approver | INV-344 | INV-345, INV-346, INV-347, INV-348 |
| M25 Supplier receiving and inspection handoff | Warehouse operator, Warehouse supervisor | INV-361 | INV-362, INV-363, INV-364 |
| M26 Quality inspections and disposition | Quality inspector, Warehouse supervisor | INV-377 | INV-378, INV-379, INV-380 |
| M27 Sales quotations and orders | Sales clerk, Sales manager | INV-393 | INV-394, INV-395, INV-396 |
| M28 Pick, pack and dispatch | Picker, Packer, Dispatcher | INV-409 | INV-410, INV-411, INV-412 |
| M29 Customer and vendor returns | Sales clerk, Buyer, Warehouse supervisor | INV-425 | INV-426, INV-427, INV-428 |
| M30 Expiry, recalls and scrap | Quality inspector, Warehouse supervisor, Approver | INV-441 | INV-442, INV-443, INV-444 |
| M31 Blind counts and reconciliation | Counter, Warehouse supervisor, Approver | INV-457 | INV-458, INV-459, INV-460 |
| M32 Routes, putaway and cross-docking | Warehouse supervisor | INV-473 | INV-474, INV-475, INV-476 |
| M33 Batch and wave picking | Warehouse supervisor, Picker | INV-489 | INV-490, INV-491, INV-492 |
| M34 Replenishment and demand planning | Buyer, Warehouse supervisor | INV-505 | INV-506, INV-507, INV-508 |
| M35 Consignment and owner-separated stock | Buyer, Warehouse supervisor | INV-521 | INV-522, INV-523, INV-524 |
| M36 Dropship fulfillment | Buyer, Sales clerk | INV-537 | INV-538, INV-539, INV-540 |
| M37 Intercompany trade and transfers | Company admin, Buyer, Sales manager | INV-553 | INV-554, INV-555, INV-556 |
| M38 Kits without manufacturing | Catalog manager, Sales clerk | INV-569 | INV-570, INV-571, INV-572 |
| M39 Offline Android warehouse workflows | Warehouse operator, Counter | INV-585 | INV-586, INV-587, INV-588 |
| M40 Scanners, labels and printer interfaces | Warehouse operator, Warehouse supervisor | INV-602 | INV-603, INV-604, INV-605 |
| M41 Valuation methods and subledger | Valuation analyst, Auditor | INV-619 | INV-620, INV-621, INV-622, INV-623 |
| M42 Landed costs and revaluation | Valuation analyst, Approver | INV-636 | INV-637, INV-638, INV-639 |
| M43 Valuation periods and reconciliation | Valuation analyst, Approver, Auditor | INV-652 | INV-653, INV-654, INV-655 |
| M44 Accounting export batches | Valuation analyst, Integration operator | INV-668 | INV-669, INV-670, INV-671 |
| M45 Operational reports and analytics | Warehouse supervisor, Buyer, Sales manager, Valuation analyst, Auditor | INV-684 | INV-685, INV-686, INV-687 |
| M46 External APIs, imports and webhooks | Integration operator | INV-700 | INV-701, INV-702, INV-703, INV-704 |
| M47 Customer migration and onboarding | Implementation operator, Tenant admin | INV-717 | INV-718, INV-719, INV-720 |
| M48 SaaS support and customer lifecycle | Platform operator, Tenant admin | INV-733 | INV-734, INV-735, INV-736 |
| M49 Security, privacy and localization release | Security reviewer, Compliance reviewer | INV-749 | INV-750, INV-751, INV-752 |
| M50 Reliability, recovery and performance | Platform operator, Engineer | INV-765 | INV-766, INV-767, INV-768, INV-769 |
| M51 Pilot, training and production release | Product owner, Implementation operator | INV-781 | INV-782, INV-783, INV-784 |
