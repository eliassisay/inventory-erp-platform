# Risk register

| Risk | Consequence | Mitigation / gate | Owner |
| --- | --- | --- | --- |
| Odoo parity assumption | Unbounded scope | Feature disposition and explicit exclusions; scope-change review | Product owner, M01 |
| Cross-tenant leak | Confidentiality and trust failure | RLS plus authorization across every indirect path; C06 | Security reviewer, M05/M49 |
| Concurrent overselling | Invalid physical stock | Ordered row locks, reservations, idempotent posting; C01/C02 | Stock engineer, M20/M21 |
| Missing early costs | Impossible later valuation | Immutable cost facts from phase 5; block go-live until replay reconciles | Valuation analyst, M20/M41 |
| Offline stale commands | Duplicate or unauthorized movement | Durable queue, server authority, conflict review and device lease; C14 | Mobile engineer, M13/M39 |
| Slow/costly all-suite testing | Delayed feedback | Focused module tests, progress logs, isolated integration CI and required gates | Delivery engineer, M02 |
| Country obligations misunderstood | Invalid launch claims or data handling | Qualified review of exact deployment/document scope; no guessed tax rates/retention | Compliance reviewer, M01/M49 |
| Rounding and costing errors | Incorrect inventory value | Exact arithmetic, original return basis, reconciliation fixtures; C10/C11 | Valuation engineer, M17/M41 |
| External acknowledgement ambiguity | Duplicate or unreconciled accounting | Stable batch/checksum, explicit line acknowledgement; C13 | Integration operator, M44 |
| Tenant noisy neighbor | Poor service for other customers | Scoped quotas, fair jobs, per-tenant telemetry and load benchmark | Platform operator, M50 |
| Blind restoration after go-live | Lost accepted transactions | Restore boundary and command replay rehearsal; C17 | Implementation operator, M47/M50 |
| Device/printer incompatibility | Warehouse adoption failure | Supported-device matrix and physical pilot tests | Warehouse lead, M40 |
| Incomplete source migration | Wrong opening stock/value | Dry-run and signed source/target reconciliation | Implementation operator, M47 |

Review risks at every phase gate. A mitigation plan is not evidence that the risk has been eliminated. No critical/high unresolved integrity/security issue may be accepted silently.
