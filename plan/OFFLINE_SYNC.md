# Offline Android synchronization protocol

## Persistence and authorization

Flutter repository combines encrypted local SQLite data and remote API. Secrets live in Android secure storage, never in SQLite queue payloads. User must authenticate online before bootstrap. Device registration binds a device key, tenant, user and selected warehouse scope; offline unlock lease lasts at most 24 hours. This does not grant server authorization after revocation.

Cache only assigned operational work and necessary master data; omit costs unless the role needs them. Tenant switching requires a complete local wipe and fresh bootstrap. Logout removes credentials and accessible cache. Unsynced command evidence may be exported to an encrypted administrator recovery package only through an explicit authorized recovery flow.

## Pull protocol

`GET /sync/bootstrap` returns schemaVersion, scopeHash, snapshotCursor, paged master data and task assignments. Bootstrap pages belong to one consistent snapshot. `GET /sync/changes?cursor=...` returns ordered changes and tombstones plus nextCursor/hasMore. A cursor is signed/scoped to tenant, user/device and permission-scope version. Expired cursors return SYNC_RESET_REQUIRED; preserve queued commands while rebuilding cache, then revalidate each against fresh state.

Changes are retained for 30 days for sync, independent of immutable ledger retention. A permission reduction invalidates the scope hash and purges now-unauthorized cache on next connection. Offline lease expiry locks local access pending renewed authentication.

## Push protocol

`POST /sync/commands` accepts up to 100 commands with `{commandId, schemaVersion, aggregateType, aggregateId, expectedVersion, occurredAt, deviceSequence, dependsOn[], payload}`. Server derives actor/tenant and checks permissions again. Each command is independently atomic and idempotent; a batch is not one global transaction. Dependent commands wait for acknowledged predecessors. Return per-command `{commandId,status,result?,conflict?}` plus authoritative versions and server time.

Persist local command before showing queued success. Mark sending without deleting it. Only a durable acknowledgement marks completion. Lost acknowledgements trigger replay with the same ID/hash. Clock time never decides stock authority; deviceSequence and command dependencies order observations, while server posting sequence orders committed stock.

## Conflict behavior

| Conflict | Resolution |
| --- | --- |
| Changed document version | Fetch current record, show differences, require explicit rebase and a new command referencing the old one |
| Insufficient or newly blocked stock | Reallocate/reduce through authorized workflow; never force local quantity into server balance |
| Revoked user/device/scope | Block upload, require valid sign-in and supervisor recovery; cached permission cannot override denial |
| Lot/serial mismatch | Correct capture or reject; retain original scan evidence |
| Expired assignment/lease | Supervisor reassignment and explicit revalidation |
| Missing dependency | Hold successor until predecessor is acknowledged or cancelled |
| Ambiguous count observation time | Recount; never infer a variance from stale quantities |
| Unsupported schema version | Require compatible app update; preserve recoverable queue |

Connectivity changes trigger sync; background execution is best-effort under Android restrictions. Provide foreground sync status and manual retry. Transient network/503 errors use bounded exponential backoff; business conflicts stop retries. Offline receipt/pick/count capture cannot execute approval, close a valuation period, change entitlements or claim a final financial posting.

Required tests: airplane mode, process kill, reboot, storage full, expired credential, revoked scope, duplicate/reordered batch, missing predecessor, lost acknowledgement, cursor reset, unsupported schema, partial batch failure and same SKU consumed by another device. Use real handheld and camera devices at pilot, not emulator-only evidence.
