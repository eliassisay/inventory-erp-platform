# Scope and task change control

The baseline is registry version 1.0 with the frozen task ID list. It is complete relative to the agreed inventory-focused scope, not all ERP domains. Never renumber or reuse an ID. Append newly approved IDs above the current maximum and mark them `scope_delta: true` with reason and decision reference.

Before adding a capability, search COVERAGE, exclusions and modules. If already covered, clarify the existing task; if not, record proposal in INBOX with problem, user evidence, affected workflows, accounting/privacy/offline implications and owner. Product owner decides included change, future scope or rejected with a revisit trigger.

An approved change updates registry feature/module/task ownership, dependencies, entity/API/screen registries, acceptance scenarios and affected narrative contracts. Regenerate Markdown and run checker/tests. New modules must fill all 15 lenses with tasks or meaningful N/A reasons. Scope delta is reported separately from the original baseline.

Use registry task status as the single authority. Renderer cannot infer status from Markdown. `make task-status` validates dependencies and design gates before writing and preserves all IDs. `[~]` active, `[?]` implementation verified awaiting review, `[x]` accepted/merged. Optional evidence links attach test logs, review and release artifacts.

Design status becomes designed only with a reviewed artifact; actual implementation artifacts may be checked-in or valid reviewed URLs. No generated placeholder is accepted. Architecture changes require updating DECISIONS and the affected release criteria, not silently changing implementation behavior.
