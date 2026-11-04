# Ethiopia-first localization and validation

Confirmed product defaults: English UI, ETB base-currency default, Africa/Addis_Ababa company time zone and Gregorian ISO dates in APIs. Preserve original commercial currency and FX source/date for foreign purchases. Optional local calendar display is later scope, never a reinterpretation of stored timestamps.

Verified source: the [Ministry of Justice listing for Personal Data Protection Proclamation 1321/2024](https://justice.gov.et/en/law/personal-data-protection-proclamation/), checked 2026-11-04. This establishes a review source, not a legal interpretation. The official text and current implementing guidance must be reviewed for the actual hosting and business model before launch.

| Validation item | Evidence required | Owner / gate |
| --- | --- | --- |
| Inventory/order/dispatch document classification | Qualified review of required fields, numbering and retention; document wording clearly excludes tax invoices | M01 / baseline and M49 / pilot |
| Tax invoice boundary | Confirm integrations do not accidentally issue tax invoices or imply certified fiscal functionality | M49 / pilot |
| Personal data applicability | Reviewed notices, rights process, retention/holds and controller/processor roles | M49 / pilot |
| Hosting and transfers | Selected infrastructure region, subprocessors and applicable transfer safeguards reviewed | M01 and M49 / production |
| Export suitability | Customer accountant validates inventory journal proposal format and account mappings | M44 / customer onboarding |
| Language and formats | English strings, ETB display, decimal/grouping, local dates and address/contact fields checked with pilot users | M11 and M51 / pilot |
| Device/connectivity assumptions | Real Android scanner/printer tests on pilot connectivity, including offline recovery | M39/M40 / pilot |

No official Ethiopian e-invoicing API contract, statutory tax rates, legal retention schedule or sector certification has been verified or promised here. Such requirements must be researched as actual release evidence, not silently assumed away. If a requirement expands the agreed inventory-only boundary, record the decision through scope control before implementation.
