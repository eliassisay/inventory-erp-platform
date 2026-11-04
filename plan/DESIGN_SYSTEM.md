# Design and interaction requirements

Office workspace prioritizes inventory work queues, stock lookup, purchasing, fulfillment, counts and reports. Platform administration is a distinct surface. Android prioritizes assigned tasks, large scan targets, quantity confirmation, pending work and conflict resolution. Company and warehouse context must be visible before any posting action.

Use shared typography, spacing, semantic colors, tables/cards, forms, dialogs, toast/error patterns and lifecycle badges. Light/dark themes must preserve contrast. Target WCAG 2.2 AA: keyboard access, visible focus, semantic labels, non-color-only status, screen-reader announcements and adequate touch targets. Do not make a barcode scanner the only input option.

Every screen family needs list/work queue, detail/history and action forms where applicable. Define default/loading/empty/invalid/permission-denied/error/archived/locked states, plus offline/queued/conflicted for warehouse screens. Dangerous actions show scope, quantity and consequence before confirmation; they never silently post on barcode lookup alone.

Design at 375, 768, 1280, 1920 and 2560 CSS pixels. Tables become prioritized cards or controlled table scrolling on narrow screens; page-level horizontal overflow is a defect. Large monitors use available workspace; only long-form content is width-limited. Numeric columns align and use explicit units/currencies. Costs are permission-gated.

A design artifact may be a checked-in HTML/prototype/spec or accessible reviewed external design URL. Registry records artifact and named reviewer. The design task must be accepted before the linked BUILD task starts; screen status then progresses designed → built. No placeholder/fabricated links satisfy this gate.
