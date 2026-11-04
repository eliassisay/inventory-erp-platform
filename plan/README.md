# Plan index

## Scope and evidence

- [Product requirements](PRODUCT_REQUIREMENTS.md): audience, boundaries and success criteria.
- [Research](RESEARCH.md): dated official sources, adopted decisions and limits.
- [Coverage](COVERAGE.md): every capability, owner, task and acceptance test.
- [Roadmap](ROADMAP.md), [tasks](tasks.md), [modules](MODULES.md), [discipline work breakdown](WBS.md).

## Implementation contracts

- [Architecture](ARCHITECTURE.md) and [decisions](DECISIONS.md).
- [Database rules](DATABASE_SCHEMA.md) and [entity registry](ENTITIES.md).
- [API contracts](API_REFERENCE.md) and [endpoint registry](ENDPOINTS.md).
- [Workflows](WORKFLOWS.md), [lifecycles](LIFECYCLES.md), [stock and valuation invariants](INVARIANTS.md).
- [Offline synchronization](OFFLINE_SYNC.md).
- [Permission rules](PERMISSIONS.md), [role ownership](ROLE_OWNERS.md), [approval policy](APPROVALS.md).
- [Screens](SCREENS.md), [design system](DESIGN_SYSTEM.md), [audit/events/notifications](EVENTS_AUDIT.md).
- [Privacy](PRIVACY.md), [localization](LOCALIZATION.md), [glossary](GLOSSARY.md).

## Delivery and operations

- [Planning validation results](VALIDATION.md).

- [Test strategy](TEST_STRATEGY.md), [acceptance scenarios](ACCEPTANCE.md), [release gates](RELEASE_GATE.md).
- [Migration/cutover](MIGRATION.md), [operations](OPERATIONS.md), [environment and setup](SETUP.md).
- [Risk register](RISKS.md), [scope control](SCOPE_CONTROL.md), [inbox](INBOX.md).
- [Release evidence template](releases/TEMPLATE.md).

`registry.json` owns IDs, status, dependencies, coverage and ownership. Eleven generated documents are checked byte-for-byte against it. Narrative specifications are reviewed alongside registry changes. The checker validates traceability and structural integrity; it cannot prove legal compliance, implementation correctness or commercial suitability.
