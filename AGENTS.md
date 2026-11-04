# Engineering instructions

This is an independent inventory ERP planning baseline. Do not copy construction-specific constraints such as project/WBS ownership, supplier-free procurement or ETB-only money into this product.

## Before work

- Read the product requirements, architecture, decisions and relevant module documents. Run `make plan-check`.
- Inspect Git status; preserve work belonging to the user. Work only within this project unless explicitly authorized.
- Choose a dependency-ready task from the registry. There may be only one active `[~]` task. Document requested scope changes before introducing new capabilities.
- Update status through `make task-status`. `[?]` means verified and awaiting review; `[x]` requires accepted/merged work. Never mark software implemented merely because its plan exists.
- For screen BUILD work, approve the linked design artifact and reviewer in the registry first. Never fabricate a design link or test result.

## Integrity requirements

Tenant/company/warehouse authorization applies to APIs, SQL, workers, caches, files, reports, mobile and integrations. Use a non-owner, non-BYPASSRLS app role. Use transaction-local scope, never a pooled connection's lingering session scope.

Stock posting is one atomic server command: locked buckets, immutable movements, exact projections, cost facts, idempotency result, audit and outbox. No direct balance edits. No negative controlled physical stock. All corrections use an authorized linked reversal or adjustment.

Quantities, conversions, cost and money never pass through binary floating-point arithmetic. API decimals are strings. Preserve original unit/currency/rate facts. Offline capture stays pending until server authorization and commit; no last-write-wins for stock.

## Implementation and evidence

Declare request/response schemas and permissions before implementing a route. Generate OpenAPI and typed clients; test denied access as well as successful operation. Use the existing technology families from ARCHITECTURE.md; exact versions must be verified and pinned by the foundation task.

Run targeted checks first; run affected module regression tests and the required release gates afterward. For long test suites, enable progress reporting and persist logs; do not repeatedly rerun unchanged suites. Document actual results and limitations.

Never put real credentials or customer records in this repository. Use synthetic fixtures. Do not push, publish, provision paid services or send messages to external people unless explicitly authorized. Local changes, tests and planning updates within the task are authorized.

## Completion

Record changed behavior, tests and manual review steps. Mark verified work `[?]`, with evidence links in the task's optional `evidence` field. Every phase requires signed release evidence before release; a green task checklist alone is insufficient.
