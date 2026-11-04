# Lifecycle and command rules

| Aggregate | States / transitions | Guard and correction |
| --- | --- | --- |
| Tenant | provisioning → active ↔ suspended → offboarding → closed | Operator manages entitlements; suspension blocks new posting but permits authorized export |
| Master data | active → archived | Cannot archive occupied/referenced live location or reuse historical identity codes ambiguously |
| Approval | draft → submitted → approved/rejected; approved → superseded by revision | Document and policy version snapshots; no self-approval for governed sensitive actions |
| Requisition/RFQ | draft → submitted/sent → approved/selected/rejected/cancelled | Only approved demand creates committed PO; offer evidence retained |
| Purchase order | draft → submitted → approved → partially_received → received → closed | Cancel unreceived remainder only; amendments create revisions |
| Sales order | draft → confirmed → partially_allocated/allocated → partially_fulfilled → fulfilled → closed | Price/discount rules enforced; shipped quantities require returns, not cancellation |
| Stock operation | draft → ready → posted; draft/ready → cancelled | Immutable after posting; linked reversal after downstream checks |
| Transfer | draft → approved → partially_shipped/shipped → partially_received/received → reconciled | Discrepancies remain explicit; no receipt greater than net shipped quantity |
| Inspection | pending → in_progress → passed/failed/partial → disposed | Required evidence; accepted + rejected = inspected quantity |
| Return | requested → authorized → partially_processed/processed → closed | Original net quantity and tracking cap; inspected disposition required |
| Recall | draft → active → contained → closed | Closing requires affected inventory/customer disposition evidence |
| Count | planned → counting → reconciling → recount_required/review → approved → posted | Blind observations; movement ambiguity prevents posting |
| Wave | draft → released → in_progress → completed/cancelled | Cancel only uncompleted tasks, preserving scan evidence |
| Replenishment suggestion | proposed → accepted/rejected/superseded | Accepted suggestion creates one linked demand/supply document |
| Valuation period | open → reconciling → closed → reopened by approval | Financial backdating blocked; re-close creates new evidence revision |
| Accounting export | draft → validated → released → delivered → acknowledged/partially_rejected/rejected → superseded if corrected | Immutable released checksum; retries reuse batch ID |
| Mobile command | queued → sending → acknowledged OR conflict/blocked_dependency | Transient failures retry; conflicts require rebase/new command or cancel, never silent overwrite |
| Migration | draft → validated → rehearsed → approved → cutover → reconciled → accepted | Restore rollback only before new live postings; afterward controlled forward correction |

Each LIFE task implements its named transition subset and declares forbidden transitions in executable tests. Enum values are finalized in the module contract task using this vocabulary; direct client status edits are prohibited.
