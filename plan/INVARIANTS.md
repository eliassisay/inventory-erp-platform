# Stock and valuation invariants

1. For each controlled physical bucket, on_hand = sum(incoming posted quantity) - sum(outgoing posted quantity), and on_hand >= 0. Reserved >=0 and cannot exceed eligible on_hand.
2. Available = eligible on_hand - active reserved. Forecast = eligible on_hand + dated confirmed incoming supply - outstanding confirmed demand. Reservations are part of demand, not a second deduction.
3. Every physical transfer conserves quantity across source, transit and destination; approved loss/return resolves discrepancies explicitly.
4. Every posted operation has one durable idempotency result, audit evidence and outbox entry in the same transaction. A repeat yields the same committed IDs.
5. No mutable UI/server convenience field is the source of truth for stock. Projection rebuild must match the immutable ledger at a specified sequence.
6. Lot, serial, owner and condition cannot disappear on internal movement. Serial stock is integral and occupies one physical position.
7. Quarantine, recall and expiry eligibility are rechecked at reservation and dispatch, including after offline delay.
8. Returned quantity cannot exceed original posted quantity net of prior returns. Return valuation uses original allocation basis, not today's purchase price.
9. Tenant/company scope of all related documents, buckets, identities and movements must agree. Cross-company trade is explicitly paired; cross-tenant trade is not implicit.
10. Owned inventory value equals sum of owned valuation entries at the same as-of point. Vendor-owned custody is excluded. Transit value remains owned until the configured ownership event occurs.
11. FIFO costing consumes oldest company/product layers independently of physical picking. Moving-average receipt recomputes exact average. Standard price variance and later acquisition charges are explicit entries.
12. Allocation of landed cost sums exactly to the entered minor-unit amount. Equal remainders are assigned by stable receipt-line ID; consumed shares append adjustments.
13. Closed periods cannot be changed by ordinary posting. Late occurrences retain their true occurrence time while financial effect enters the current open period. Reopening requires independent approval and new export revision.
14. Export debit/credit proposals balance and reference each valuation effect once per active export revision. Delivery retries never create new accounting effects; external acknowledgement is reconciled explicitly.
15. Internal stock moves without ownership change do not create company-wide profit or inventory value. Intercompany price differences belong to separately reconciled company books; this product does not produce consolidated financial statements.
16. A phantom kit has component reservations and component cost; it has no independent finished-goods stock or production order.

## Locking and correction algorithm

Validate scope and expected version, claim/check idempotency key, resolve all affected buckets, lock them in sorted tenant/company/location/product/owner/tracking order, revalidate quantities and eligibility, write immutable facts and projections, write audit/outbox/result, commit. Retry serialization/deadlock failures at most three times under the same key; then return a retryable conflict. Never retry business validation as if it were a transient error.

Corrections must name original document/move, reason and authorized actor. Reverse only still-reversible quantities; downstream allocations/shipments require their own linked return/reversal first. No deletion of evidence or ad hoc SQL repair is a supported business operation.
