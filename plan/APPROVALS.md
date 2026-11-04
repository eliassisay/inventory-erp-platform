# Approval policy

Resolve policy by module + company + optional warehouse, choosing the most-specific matching scope; within scope choose the highest applicable threshold, then deterministic policy priority. Ambiguous equal-priority policies are a configuration error. Threshold currency is the company base currency using document-snapshotted FX. Missing approvers block submission rather than silently auto-approving.

Submission snapshots document version and policy version. A stage has eligible roles/users, required count and ordering. Decisions record actor, stage, reason and timestamp. Requester cannot fulfill required independent approval for PO, adjustment, scrap, ownership conversion, intercompany, revaluation or close. Rejection reason is mandatory.

Approval can be disabled for low-risk workflows through explicit policy, producing an audited automatic decision. Disabling never bypasses inventory, scope, closed-period or mandatory separation-of-duties rules on protected operations. Approved revisions are immutable; changed quantity, price, location, owner or cost requires a new revision and approval.

Default routing: requester → buyer/manager for PO; counter/operator → warehouse supervisor for count/scrap; valuation analyst → independent company finance approver for revaluation/close/export; company administrators on both sides for intercompany. Escalation/reminders never implicitly approve on timeout. Every configured chain requires accepted/rejected/out-of-order/duplicate-decision tests.
