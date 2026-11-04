# Architecture and product decisions

All decisions below are adopted planning defaults; implementation evidence may change a decision only through scope control.

| ADR | Decision | Why / consequence |
| --- | --- | --- |
| D01 | Independent SaaS, not an Odoo addon | Research informs capabilities without runtime dependency or parity claim |
| D02 | Modular monolith, PostgreSQL-backed jobs | Transactional stock integrity before distributed-service complexity |
| D03 | Tenant > company > branch/warehouse > location | Legal ownership and customer isolation are explicit |
| D04 | Shared schema with RLS and non-owner roles | Application checks plus database backstop; raw-role testing mandatory |
| D05 | Immutable stock ledger plus rebuildable projections | Corrections remain attributable; no administrator balance editing |
| D06 | No negative controlled physical stock | Reservation and posting concurrency cannot oversell physical buckets |
| D07 | Quantities NUMERIC(24,6); unit costs/FX NUMERIC(30,12) | Reject excess precision before persistence; no binary floats |
| D08 | Amounts in currency minor units, half-up boundary rounding | ETB is a default; currency exponent is snapshotted |
| D09 | Basic tracking before stock; advanced recalls later | Avoid missing identity history in early operations |
| D10 | Cost facts captured at first movement | Valuation phase can replay complete acquisition and issue history |
| D11 | Offline capture, authoritative server commit | Stale mobile data cannot override quantities or approvals |
| D12 | 24-hour maximum offline unlock lease | Lost/revoked devices cannot retain indefinite interactive access |
| D13 | Valuation and exports only | No invoices, payments, general ledger or tax-compliance claims |
| D14 | FIFO, moving average and standard cost per company/category | Policy changes require open-period approved conversion/revaluation |
| D15 | Purchase/sales prices exclude statutory invoice issuance | Commercial documents may store estimates/references but are not tax documents |
| D16 | Manual SaaS subscriptions initially | No assumed payment provider or settlement workflow |
| D17 | Phantom kits only | Component stock and cost without manufacturing production orders |
| D18 | Same-tenant intercompany only | Independent permissions and ledgers; cross-tenant trading is a future integration |
| D19 | Hosted SaaS and Android only | Self-hosting and native iOS require separate operations scope |
| D20 | Release decisions require legal/hosting evidence | Exact country obligations and retention periods are not guessed |

## Deployment inputs to resolve in implementation

The foundation and launch tasks must record supported/pinned dependency versions; selected infrastructure region and processors; approved retention schedule; customer pilot identities; and external account mappings. These are required environment/customer inputs with named task owners, not missing product behavior. Unresolved evidence blocks the relevant release gate. No assumption that an inventory-only product is exempt from local document or privacy obligations is made.
