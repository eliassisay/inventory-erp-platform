# Permissions and roles

[ROLE_OWNERS.md](ROLE_OWNERS.md) assigns authorization ownership for every module. Permission codes are immutable registry values; UI hiding is not enforcement. Tenant grants union only within their company/warehouse scopes. A company grant does not confer another company's access. An integration credential can only narrow the issuing principal's authorized scopes.

| Default role | Grants | Explicitly withheld |
| --- | --- | --- |
| Platform operator | Tenant lifecycle, plans, operational health | Customer stock/cost access absent approved support session |
| Tenant administrator | Company setup, memberships, role configuration | Automatic approval of own sensitive transaction |
| Company administrator | Company settings and scoped master configuration | Other companies and platform operations |
| Catalog manager | Product, UoM, barcode, packaging configuration | Stock adjustment or valuation close |
| Requester | Own requisitions and authorized demand views | PO approval and stock posting |
| Buyer | Suppliers, RFQs, PO drafts, replenishment acceptance, vendor returns | Own PO approval; direct balance edits |
| Sales clerk/manager | Customers, quotations, orders; manager discount authority | Valuation close or unrestricted cost exports |
| Warehouse supervisor | Assign tasks, resolve operational exceptions, review counts | Self-approve own loss/adjustment |
| Warehouse operator / picker / packer / dispatcher | Assigned scoped operational capture and permitted posting | Role changes, financial exports and unassigned warehouses |
| Counter | Assigned blind count capture | System count visibility during count or variance approval |
| Quality inspector | Inspection evidence, quarantine/release disposition | Cost revaluation or unrelated warehouse actions |
| Valuation analyst | Cost review, reconciliation, draft export | Approve own close/revaluation where independent review required |
| Approver | Decide configured approval stages within scope | Permission to create/post unrelated documents |
| Auditor | Authorized read/export of immutable evidence | Mutations and support impersonation |
| Integration operator | Configure scoped credentials and integrations | Arbitrary tenant or role elevation |

All staff is a persona group, not a wildcard permission. Engineer, designer, product owner, security reviewer, compliance reviewer and implementation operator are delivery/evidence responsibilities; runtime grants must be separately explicit when needed.

Default approval policies require a distinct authorized reviewer for PO commitments, adjustments, scrap, ownership acquisition, intercompany transactions, revaluation and period close. A tenant may configure thresholds and stages but cannot override invariant checks. Security events, role grants and support access require audit regardless of approval policy.
