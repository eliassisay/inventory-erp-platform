# Inventory ERP — Roadmap

> Registry baseline 1.0 · 2026-11-04 · 51 modules · 790 tasks · 156 capabilities · 13 phases. Generated; edit registry.json and run `make plan-render`.

All phases belong to the full baseline. No production stock go-live occurs before valuation, migration and launch gates pass. Planning artifacts exist; application work is not implemented. Phase gates are documented in RELEASE_GATE.md.

| Phase | Name | Modules | Tasks | Entry gate |
| --- | --- | --- | --- | --- |
| 1 | Research baseline and architecture | M01 | 7 | Approved baseline |
| 2 | SaaS foundations | M02, M03, M04, M05, M06, M07, M08, M09, M10 | 133 | Previous phase gate passed; same-phase task dependencies completed |
| 3 | Design system and application shells | M11, M12, M13 | 39 | Previous phase gate passed; same-phase task dependencies completed |
| 4 | Companies and inventory master data | M14, M15, M16, M17, M18, M19 | 97 | Previous phase gate passed; same-phase task dependencies completed |
| 5 | Stock integrity and core operations | M20, M21, M22, M23 | 65 | Previous phase gate passed; same-phase task dependencies completed |
| 6 | Purchasing and inbound quality | M24, M25, M26 | 49 | Previous phase gate passed; same-phase task dependencies completed |
| 7 | Sales orders and fulfillment | M27, M28 | 32 | Previous phase gate passed; same-phase task dependencies completed |
| 8 | Traceability, returns and inventory control | M29, M30, M31 | 48 | Previous phase gate passed; same-phase task dependencies completed |
| 9 | Advanced warehouse and supply workflows | M32, M33, M34, M35, M36, M37, M38 | 112 | Previous phase gate passed; same-phase task dependencies completed |
| 10 | Warehouse Android and hardware | M39, M40 | 34 | Previous phase gate passed; same-phase task dependencies completed |
| 11 | Valuation and accounting boundary | M41, M42, M43, M44 | 65 | Previous phase gate passed; same-phase task dependencies completed |
| 12 | Reports, interfaces and migration | M45, M46, M47 | 49 | Previous phase gate passed; same-phase task dependencies completed |
| 13 | Operational readiness and launch | M48, M49, M50, M51 | 60 | Previous phase gate passed; same-phase task dependencies completed |

## Phase 1 — Research baseline and architecture

Tasks: INV-001–INV-007 (7).

**Exit:** Scope and source register reviewed; architecture, accounting boundary and launch evidence owners recorded.

- M01 Product baseline and localization: Research baseline; Ethiopia localization review; Dependency and version decisions.

## Phase 2 — SaaS foundations

Tasks: INV-008–INV-140 (133).

**Exit:** Two tenants provisioned; identity, scoped roles, approvals, audit and durable jobs pass isolation tests.

- M02 Repository and delivery tooling: Reproducible development stack; CI and contract generation; Environment separation.
- M03 Tenants and SaaS entitlements: Tenant onboarding; Operator-managed plans; Suspension and reactivation.
- M04 Identity, invitations and devices: Invite and recovery; MFA and sessions; Device revocation.
- M05 Scoped roles and permissions: Permission catalog; Tenant company warehouse boundaries; Support access.
- M06 Approval policies and decisions: Policy routing; Separation of duties; Approval versioning.
- M07 Audit and business events: Transactional audit; Append-only evidence; Event privacy.
- M08 Jobs, idempotency and delivery: Idempotent commands; Outbox processing; Retries and dead letters.
- M09 Attachments and collaboration: Private attachments; Comments and evidence.
- M10 Notifications and preferences: Notification routing; Delivery and preferences.

## Phase 3 — Design system and application shells

Tasks: INV-141–INV-179 (39).

**Exit:** Responsive office/admin shells and Android local store operate; screen design gates and sync protocol fixtures pass.

- M11 Design system and accessibility: Accessible visual system; Screen state contracts.
- M12 Office and admin application shells: Office context switching; Platform admin separation; Search and navigation.
- M13 Android foundation and sync protocol: Durable local repository; Sync protocol foundation; Pending versus posted.

## Phase 4 — Companies and inventory master data

Tasks: INV-180–INV-276 (97).

**Exit:** Companies, partners, SKUs, units, warehouse locations and tracking identities import without orphaned references.

- M14 Companies, branches and regional settings: Company and branch setup; Regional defaults; Currency governance.
- M15 Suppliers and customers: Partner directory; Partner commercial references; Contact privacy.
- M16 Products, variants and packaging: Product and variant catalog; Tracking configuration; Packaging and barcode aliases; Catalog import.
- M17 Units and exact arithmetic: Unit conversions; Quantity precision; Monetary precision.
- M18 Warehouses and location hierarchy: Location hierarchy; Operational areas; Archival and capacity.
- M19 Lot, serial and ownership identities: Lot and serial identity; Ownership dimensions; Receipt tracking requirements.

## Phase 5 — Stock integrity and core operations

Tasks: INV-277–INV-341 (65).

**Exit:** Opening stock, receipt, issue, reservation and transfer reconcile exactly under concurrency and retries.

- M20 Immutable stock ledger and projections: Posting transaction; No negative physical stock; Reversal and rebuild; Cost fact capture.
- M21 Reservations and availability: Atomic allocation; Partial allocation and release; Availability and forecast.
- M22 Core receipts, issues and opening stock: Opening stock; Receipt and internal issue; Partial operations and backorders.
- M23 Transfers and in-transit custody: Immediate and staged transfers; Partial receipt and discrepancy; Transfer conservation.

## Phase 6 — Purchasing and inbound quality

Tasks: INV-342–INV-390 (49).

**Exit:** Requisition through approved PO, partial receipt and quality release works; rejected stock cannot be allocated.

- M24 Requisitions, RFQs and purchase orders: Requisition and quotation comparison; Approved PO revisions; Blanket order releases; Purchase cancellation.
- M25 Supplier receiving and inspection handoff: PO receipt matching; Receive to quarantine; Receipt cost snapshot.
- M26 Quality inspections and disposition: Inspection execution; Split disposition; Reinspection and evidence.

## Phase 7 — Sales orders and fulfillment

Tasks: INV-391–INV-422 (32).

**Exit:** Quotation through partial pick/pack/dispatch works with correct reservation release and backorders.

- M27 Sales quotations and orders: Quotation and pricing; Sales confirmation; Order changes.
- M28 Pick, pack and dispatch: Pick verification; Packing control; Dispatch and delivery records.

## Phase 8 — Traceability, returns and inventory control

Tasks: INV-423–INV-470 (48).

**Exit:** Returns link originals; recalled/expired stock is blocked; blind counts and variances reconcile to ledger.

- M29 Customer and vendor returns: Linked return entitlement; Customer return inspection; Vendor returns.
- M30 Expiry, recalls and scrap: Expiry and FEFO; Recall genealogy; Approved scrap.
- M31 Blind counts and reconciliation: Blind and cycle counting; Moving-stock reconciliation; Variance approval.

## Phase 9 — Advanced warehouse and supply workflows

Tasks: INV-471–INV-582 (112).

**Exit:** Routes, waves, replenishment, consignment, dropship, intercompany and kits preserve quantity and ownership.

- M32 Routes, putaway and cross-docking: Multi-step routes; Putaway and capacity; Cross-docking.
- M33 Batch and wave picking: Batch and wave formation; Picking strategies; Replanning exceptions.
- M34 Replenishment and demand planning: Min-max and safety stock; Buyer approval; Pick-face replenishment.
- M35 Consignment and owner-separated stock: Consignment custody; Ownership acquisition; Owner returns.
- M36 Dropship fulfillment: Linked supplier fulfillment; Supplier delivery evidence; Dropship returns.
- M37 Intercompany trade and transfers: Paired commercial documents; Company-local ledgers; Independent permissions.
- M38 Kits without manufacturing: Phantom kit definitions; Kit allocation and fulfillment; Kit returns.

## Phase 10 — Warehouse Android and hardware

Tasks: INV-583–INV-616 (34).

**Exit:** Real-device offline receipt/pick/count capture survives process death and sync conflicts without double posting.

- M39 Offline Android warehouse workflows: Offline operational capture; Conflict review; Reconnect recovery.
- M40 Scanners, labels and printer interfaces: Camera and handheld scanning; GS1 parsing; Label generation and reprints.

## Phase 11 — Valuation and accounting boundary

Tasks: INV-617–INV-681 (65).

**Exit:** All costing methods and landed costs reconcile; periods lock; exports are acknowledged without duplicates.

- M41 Valuation methods and subledger: FIFO costing; Weighted-average costing; Standard costing; Returns and replay.
- M42 Landed costs and revaluation: Charge allocation; Remainder and consumed stock; Approved revaluation.
- M43 Valuation periods and reconciliation: Period reconciliation; Close prerequisites; Controlled reopen.
- M44 Accounting export batches: Balanced export format; Delivery acknowledgement; Accounting boundary.

## Phase 12 — Reports, interfaces and migration

Tasks: INV-682–INV-730 (49).

**Exit:** As-of reports match ledgers; imports dry-run; signed webhooks replay safely; customer migration reconciles.

- M45 Operational reports and analytics: As-of stock and value; Service metrics; Secure exports.
- M46 External APIs, imports and webhooks: Public API contracts; Signed webhooks; Versioned imports; Connector boundary.
- M47 Customer migration and onboarding: Mapping and rehearsal; Cutover controls; Rollback boundary.

## Phase 13 — Operational readiness and launch

Tasks: INV-731–INV-790 (60).

**Exit:** Security assessment, localization review, backup restoration, load tests and pilot acceptance are evidenced before production.

- M48 SaaS support and customer lifecycle: Support runbooks; Tenant portability; Offboarding and holds.
- M49 Security, privacy and localization release: Isolation assessment; Privacy rights and retention; Launch security.
- M50 Reliability, recovery and performance: Observability; Backup and recovery; Performance budgets; Safe deployment.
- M51 Pilot, training and production release: Pilot scenario coverage; Training and support; Production go-live.

## Deliberate boundaries

| ID | Capability | Disposition | Reason | Revisit trigger |
| --- | --- | --- | --- | --- |
| X01 | Customer tax invoices and credit notes | excluded | External accounting owns issuance and legal numbering. | A separately approved invoicing scope and verified localization. |
| X02 | Vendor bills and payment settlement | excluded | Only external cost evidence and references enter valuation. | A separately approved finance expansion. |
| X03 | General ledger, bank reconciliation and financial statements | excluded | Inventory proposals are exported to the accounting system. | A separately approved full accounting product. |
| X04 | Payroll, HR, CRM campaigns and project management | excluded | Outside inventory-focused ERP boundaries. | Demonstrated customer demand and independent module plan. |
| X05 | Full manufacturing and production scheduling | excluded | Kits explode components without production orders, work centers or labor costing. | A manufacturing extension with its own costing and traceability scope. |
| X06 | POS checkout and ecommerce storefront | excluded | Sales order fulfillment is included; checkout and payment collection are not. | Named channel integration contract and acceptance scope. |
| X07 | Automated SaaS payment collection | later phase | Operator-managed subscription entitlements ship first. | Selected provider, settlement model and reviewed payment requirements. |
| X08 | Named accounting and courier connectors | later phase | Versioned CSV/API/webhooks are the initial integration boundary. | Named vendor, API access, sandbox and contract tests are available. |
| X09 | Self-hosted installations and native iOS | excluded | Hosted SaaS and Android are confirmed delivery targets. | Separate operations/device support budget and rollout decision. |
| X10 | RFID, robotics and warehouse automation | excluded | Camera, handheld scanners, PDF and ZPL interfaces cover launch hardware. | A selected device protocol and customer pilot. |
| X11 | Odoo feature or edition parity | excluded | Odoo is a reference; this is independently specified software. | No automatic parity commitment; evaluate individual requested capabilities. |
