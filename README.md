# Inventory ERP

Independent, inventory-focused hosted SaaS for wholesalers, distributors, retailers and company warehouses. Ethiopia first; office/admin web and offline Android; stock valuation and accounting exports only.

**This repository is a planning package, not a working application.** It contains 51 modules, 790 implementation tasks, 156 capability requirements and 13 delivery phases. All software tasks start planned. No Odoo parity or legal certification is claimed.

## Start here

1. Read [product requirements](plan/PRODUCT_REQUIREMENTS.md) and [architecture](plan/ARCHITECTURE.md).
2. Follow [the roadmap](plan/ROADMAP.md), then select a dependency-ready task from [tasks](plan/tasks.md).
3. Use [module coverage](plan/MODULES.md), [research](plan/RESEARCH.md) and [critical scenarios](plan/ACCEPTANCE.md) to check scope and correctness.
4. Run `make plan-check` and `make plan-test` before and after any planning change. Python 3.10+ and Make are sufficient; no third-party packages or network are needed.

## Planning commands

- `make plan-check`: validate the registry, dependency graph, ownership, coverage, design gates, local links and generated document drift.
- `make plan-test`: run regression tests of the planning validator and renderer. These are not application tests.
- `make plan-render`: regenerate derived documents without changing task IDs or statuses.
- `make task-status ID=INV-001 STATUS=~`: safely change task status in the canonical registry and regenerate documents.

The source of truth is `plan/registry.json`. The renderer never allocates or renumbers IDs. Append new IDs through reviewed change control; preserve the baseline ID list. Generated Markdown must not be edited by hand.

[Engineering instructions](AGENTS.md) govern future implementation. [Plan index](plan/README.md) explains every artifact. The original construction repository remains separate; this project has no runtime dependency on it.
