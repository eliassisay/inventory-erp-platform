# Audit, events and notifications

Every module with persistent data owns its AUDIT/EVENTS tasks. Audit action payload: actor and acting support session, tenant/company/warehouse, action, entity ID/version, command/request ID, timestamp, reason and redacted change metadata. Store append-only evidence with restricted access. IP/device metadata is personal data with a separate approved retention purpose.

Write audit and outbox in the same transaction as the sensitive mutation. Domain events have event ID, schema version, aggregate sequence, scope, occurrence/posting times and minimum required payload. Events are facts, not permission grants. Consumers recheck scope and deduplicate by event ID.

Key business categories: stock posted/reversed; reservation released/short; PO submitted/decided/overdue; receipt inspection due; order short-picked/dispatched; transfer discrepancy; expiry soon; recall active; count variance ready; valuation exception; export rejected; sync conflict; device revoked; tenant suspended; backup late. Register stable schemas before use.

Notification routing maps events to in-app/email templates, required permissions, recipient rules and preference categories. Deduplicate recipient/event/channel. Do not email confidential costs or full customer contacts in ordinary notifications. Security and mandatory operational warnings have explicit non-disableable categories. Automatic external partner messaging is not implied by internal notification tasks.

Operational telemetry carries request IDs and timings without credentials, raw document payloads or personal data. Dead-letter inspection is permission-controlled and redacted. No administrator can edit an audit row to conceal an action.
