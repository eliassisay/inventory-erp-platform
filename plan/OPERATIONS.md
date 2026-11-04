# Operations and recovery

## Service ownership and signals

Platform operations owns API/worker/database/object storage availability, releases and incident coordination. Tenant admins own their company configuration and delegated users; inventory exceptions remain business approvals, not infrastructure edits.

Monitor p50/p95 posting/read latency, DB locks/deadlocks, command conflicts, outbox backlog, dead letters, sync queue age, expiry/reorder job timeliness, export rejection rates, backup age and disk/resource saturation. Attach tenant-scoped correlation IDs without PII. Initial alert triggers: API 5xx >2% for five minutes, outbox oldest >5 minutes, any posting reconciliation mismatch, backup age >15 minutes beyond target, or persistent sync conflict growth. Tune thresholds from pilot evidence.

## Runbook requirements

| Incident | Immediate action | Recovery evidence |
| --- | --- | --- |
| Stock projection mismatch | Disable affected posting scope; preserve immutable history | Rebuild at fixed sequence, reconcile, review root cause before resume |
| Duplicate/failed external delivery | Inspect original event/batch ID and acknowledgement | Replay same ID, not a new business transaction |
| Sync backlog | Check device authorization, schema, lease and command dependencies | Explicit conflicts resolved without discarding evidence |
| Expired/recall shipment risk | Block eligibility and dispatch scope | Trace affected lots/serials and customer disposition |
| Compromised tenant/device key | Revoke, restrict support access, preserve audit | Incident review, scoped reauthentication and credential rotation |
| DB outage/data loss | Stop posting and invoke measured recovery plan | Isolated restore, replay/reconciliation, RPO/RTO evidence |

Backups are encrypted and restoration is tested before pilot and after material schema changes. Record actual recovery point/time. Proposed production default is daily base backup plus continuous WAL/PITR with a 30-day operational backup window, subject to the reviewed privacy/retention profile. Separate credentials and restore environment; never test restore over a live customer database.

Deploy through staging and tenant-scoped canary flags. Expand schema before code rollout; contract after compatibility window. Require mobile schema compatibility and queued-command handling. On degradation disable new commands for affected feature, keep read/export access where safe, and repair forward when rollback would invalidate posted records.

Monthly operational review: restore drill evidence, entitlement abuse/noisy-neighbor metrics, access/support sessions, subprocessor changes, expiring keys and unresolved customer incidents. Owners and escalation contacts are real deployment inputs to complete before production.
