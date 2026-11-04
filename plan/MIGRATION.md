# Migration, onboarding and cutover

1. Inventory source systems and agree a source namespace, extraction time, warehouse/owner mapping, unit conversion, tracking completeness and external account references.
2. Import masters in dependency order: tenant/company → partners/units/categories → products/variants → locations → lots/serials/owners. Dry-run every file, preserve source keys and hashes, resolve duplicates explicitly.
3. Reconcile opening physical quantities by bucket, open demand/reservations, in-transit transfers and ownership. Opening balances need acquisition cost basis for FIFO layers or approved aggregate basis for moving average/standard method. Never invent missing costs; obtain customer-approved remediation.
4. Rehearse in an isolated tenant. Compare source and target quantities, value, tracking, open quantities and record counts. Customer and implementation operator sign the reconciliation.
5. Schedule source-write freeze and device sync cutoff. Reject/suspend old source-device commands after cutoff. Apply final delta, repeat reconciliation, take verified backup and obtain go-live approval.
6. Enable production posting only after valuation, exports, permissions, mobile and recovery gates pass. Monitor first receipt, shipment, return, count and export with customer users.

Before new live operations, rollback can restore the rehearsed pre-cutover snapshot. After new live postings, a blind rollback would lose business history: preserve accepted commands and use forward repair or a separately approved restore-and-replay recovery. Do not delete/re-import posted stock merely to make totals match.

Migration evidence includes signed source totals, target totals, differences, mappings, source checksums, rejected rows, cutover timestamps, backup reference, customer approver and follow-up issues. Retain only approved necessary source data under the privacy schedule.
