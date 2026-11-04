# Research and source register

> Registry baseline 1.0 · 2026-11-04 · 51 modules · 790 tasks · 156 capabilities · 13 phases. Generated; edit registry.json and run `make plan-render`.

Research date: 2026-11-04 (Africa/Addis_Ababa). Official references only. Odoo 19.0 is a versioned functional baseline, not a claim to be its newest release or match its editions. Findings below are short paraphrases; the adopted behavior is our product decision. Recheck links and version/license support before implementation.

## S00 — Agreed product decisions

Version: 2026-11-04 conversation. Checked: 2026-11-04.

Finding: User-confirmed scope: independent inventory SaaS, Ethiopia first, web plus offline Android, valuation/export finance only.

Decision / difference: Product decision; not an external capability claim.

Coverage: M02, M06, M08, M10, M11, M12, M14, M17, M37, M38, M45, M47, M50, M51.

## S01 — [Odoo supply chain reference](https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp.html)

Version: 19.0. Checked: 2026-11-04.

Finding: Inventory, purchase and fulfillment workflows provide a reference taxonomy.

Decision / difference: Use as a feature comparison, not a parity or licensing promise.

Coverage: M15, M21, M27, M36.

## S02 — [Odoo warehouse routes](https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/inventory/warehouses_storage/inventory_management/use_routes.html)

Version: 19.0. Checked: 2026-11-04.

Finding: Location-based routes support staged inbound/outbound operations.

Decision / difference: Adopt explicit templates and route versions; do not copy Odoo internals.

Coverage: M18, M22, M23, M25, M26, M28, M32, M33.

## S03 — [Odoo tracking barcodes](https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/barcode/setup/serial_numbers_lots.html)

Version: 19.0. Checked: 2026-11-04.

Finding: Lot and serial identifiers can be captured through barcode operations.

Decision / difference: Require server-side identity validation independently of scanner input.

Coverage: M19.

## S04 — [Odoo stock valuation operations](https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/inventory/inventory_valuation/operations_valuation.html)

Version: 19.0. Checked: 2026-11-04.

Finding: Stock valuation and accounting-entry timing are distinct concerns.

Decision / difference: Our immutable inventory subledger exports proposals to an external ledger; no Odoo accounting timing is copied.

Coverage: M20, M29, M41, M43, M44.

## S05 — [Odoo FEFO removal](https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/inventory/shipping_receiving/removal_strategies/fefo.html)

Version: 19.0. Checked: 2026-11-04.

Finding: Removal dates can prioritize stock selection before expiry.

Decision / difference: Physical selection and financial costing remain separate policies.

Coverage: M30.

## S06 — [GS1 application identifiers](https://www.gs1.org/sites/default/files/docs/barcodes/GS1%20Application%20Identifiers.pdf)

Version: GS1 official reference. Checked: 2026-11-04.

Finding: Application identifiers distinguish product, batch, serial and date data within supported symbols.

Decision / difference: Implement a tested subset and preserve separators; no invented GS1 prefixes.

Coverage: M16, M40.

## S07 — [Odoo purchase templates](https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/purchase/manage_deals/purchase_templates.html)

Version: 19.0. Checked: 2026-11-04.

Finding: Purchase templates and blanket agreements serve different repeat-purchase purposes.

Decision / difference: Implement explicit supplier agreements and approved releases; omit vendor billing.

Coverage: M24.

## S08 — [Odoo cycle counts](https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/cycle_counts.html)

Version: 19.0. Checked: 2026-11-04.

Finding: Location-based periodic counting supports physical/system reconciliation.

Decision / difference: Add blind observations, movement-aware reconciliation and independent variance approval.

Coverage: M31.

## S09 — [PostgreSQL row security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html)

Version: 18, current URL checked. Checked: 2026-11-04.

Finding: RLS filters row access, but superusers/BYPASSRLS and normally table owners can bypass it.

Decision / difference: Use a non-owner application role, FORCE RLS for scoped tables and raw-role isolation tests.

Coverage: M03, M05.

## S10 — [Flutter offline-first architecture](https://docs.flutter.dev/app-architecture/design-patterns/offline-first)

Version: Living documentation. Checked: 2026-11-04.

Finding: Repositories can combine local persistence and remote synchronization.

Decision / difference: Warehouse commands stay pending until authoritative validation; never merge stock with last-write-wins.

Coverage: M13, M39.

## S11 — [Odoo replenishment](https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/inventory/warehouses_storage/replenishment.html)

Version: 19.0. Checked: 2026-11-04.

Finding: Reorder rules derive replenishment from forecast shortages.

Decision / difference: Suggestions require buyer acceptance and normal purchasing approvals.

Coverage: M34.

## S12 — [OWASP API object authorization](https://api-security.owasp.org/editions/2023/en/0xa1-broken-object-level-authorization/)

Version: API Security Top 10 2023. Checked: 2026-11-04.

Finding: Manipulated object identifiers expose missing authorization checks.

Decision / difference: Test every identifier-bearing route and indirect worker/export/mobile path.

Coverage: M04, M07, M09, M46, M49.

## S13 — [Odoo consignment](https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/inventory/warehouses_storage/advanced_operations_warehouse/owned_stock.html)

Version: 19.0. Checked: 2026-11-04.

Finding: Custody and ownership differ for consigned goods.

Decision / difference: Maintain owner dimension in all stock buckets and exclude partner-owned stock from company value.

Coverage: M35.

## S14 — [Ethiopian Personal Data Protection Proclamation](https://justice.gov.et/en/law/personal-data-protection-proclamation/)

Version: 1321/2024 official listing. Checked: 2026-11-04.

Finding: The Ministry of Justice lists the Personal Data Protection Proclamation.

Decision / difference: Applicability, hosting, retention, rights handling and cross-border transfer require qualified review before pilot; no legal interpretation or certification asserted.

Coverage: M01, M48.

## S15 — [Odoo landed costs](https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/inventory/inventory_valuation/landed_costs.html)

Version: 19.0. Checked: 2026-11-04.

Finding: Additional acquisition charges can be assigned to stock valuation.

Decision / difference: Accept external charge evidence without implementing vendor bills; allocate and reconcile exact totals.

Coverage: M42.

## Research limits and implementation gates

No official Ethiopian e-invoicing interface or sector-specific certification was verified for this package. Tax invoice issuance is excluded. The localization review must establish whether inventory documents, hosting, personal data transfers and retention impose additional requirements, record qualified review and block launch on unresolved applicability. No tax rates, legal retention periods or statutory compliance certification are assumed. See LOCALIZATION.md.
