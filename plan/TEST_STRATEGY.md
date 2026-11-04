# Testing strategy

## Planning package checks

`make plan-check` checks registry structure, coverage, dependencies, ownership, states, source IDs, screen design gates, local document links and generated drift. `make plan-test` runs validator/renderer regression tests with intentionally corrupt fixtures. Neither command is proof that an application exists or is secure.

## Application test layers

1. Unit/property tests: quantity arithmetic, conversion round trips, cost layer consumption, rounding allocation, eligibility, approval routing, state machines and reference parsers.
2. Real PostgreSQL integration: migrations, app-role RLS, scoped FKs, locking races, command replay, atomic audit/outbox, ledger rebuild and period locks.
3. Contract tests: every route has request/response/error coverage and allowed/denied roles; generated client/OpenAPI must match route registration.
4. Web E2E: complete role workflows, approval failures, empty/error recovery, keyboard accessibility and all responsive breakpoints.
5. Android/device tests: local persistence, camera/wedge/intent scanning, process death, reboot, storage exhaustion, stale scopes and sync recovery on real devices.
6. Integration adapters: webhook signature/replay/SSRF, import preview/commit, external acknowledgement and dead-letter recovery.
7. Load/security/recovery: launch-volume noisy-neighbor tests, dependency/threat assessment, tenant isolation sweep, backup restore and customer migration rehearsal.

Every feature has a Given/When/Then and negative scenario in ACCEPTANCE.md. Critical scenarios C01–C19 are release blockers, including numeric expected results. Tests must verify behavior independently of implementation rather than reproduce the same calculations in assertions.

Use deterministic synthetic fixtures: at least two tenants, two companies each, warehouse staff with differing scopes, owned/consigned stock, fractional units, multiple currencies, expired/recall/quarantine lots, serials, partial deliveries, closed periods and conflicting devices. Never use production credentials or real customer personal data in CI.

Run focused checks while implementing, then affected regression suites and phase gates. CI must visibly report progress and store JUnit/log evidence. Full integration suites must not silently skip because Docker is missing; required CI jobs fail on missing infrastructure. Repeat unchanged suites only for new failures, changes or unresolved concerns.
