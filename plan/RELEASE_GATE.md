# Phase release gates

Copy releases/TEMPLATE.md into a phase evidence file. The roadmap defines phase-specific exit criteria. Entry requires the prior phase gate and all task prerequisites; same-phase parallel work is allowed only when the dependency graph permits it. All 13 phases are required before general availability.

## Common gate for every phase

- Planning checker passes; task/screen/API/entity owners and change-control records agree.
- Phase tasks accepted with linked test/review evidence, or an approved scope change moves them and updates every dependent gate. No unchecked feature silently disappears.
- New API actions have scoped permission tests and OpenAPI/client parity; relevant raw database RLS checks pass.
- New lifecycle transitions, retry behavior, correction paths, audit and outbox effects are covered.
- New screens have approved design evidence and responsive/accessibility/state verification.
- Relevant stock/value invariants and all affected critical scenarios pass on real PostgreSQL.
- Privacy handlers and retention classification cover every new field/actor link.
- Runbooks, metrics, feature flags, migration and recovery boundaries are documented and rehearsed where changed.
- No unresolved critical/high security or data-integrity defect. Record lower severity risks with owner and target.

## Cross-phase blockers

- P1: product boundaries, architecture and localization evidence owners accepted.
- P2: two-tenant isolation, scoped jobs/files, identity/MFA and support boundary pass.
- P3: local mobile persistence and protocol fixtures pass; design gate enforced.
- P4: master-data import, unit precision, scope FKs and lot/serial identity pass.
- P5: C01/C02/C03/C05/C18; ledger/projection/cost-fact reconciliation pass.
- P6–P7: partial receipt, quality blocking and order-to-dispatch acceptance pass.
- P8–P9: return limits, expiry races, blind counts, owner separation and advanced routing pass.
- P10: C14 and real-device scanner/offline recovery pass.
- P11: C10–C13, cost replay, period locks and accounting export reconciliation pass.
- P12: customer import/cutover rehearsal, report reconciliation and webhook security pass.
- P13: all critical scenarios pass; legal/hosting evidence reviewed; backup restoration meets RPO/RTO; pilots and training accepted; rollback plan and support ownership recorded.

Intermediate demos must be labeled non-production. A phase-5 quantity demo cannot be sold as financially complete inventory. Legal applicability and infrastructure provider choices are explicit evidence gates, not blanket claims made by the plan checker.
