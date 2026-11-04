# Product requirements

## Outcome

Help businesses know what stock exists, where it is, who owns it, what is available, what must be purchased, what can ship, and what owned inventory is worth. Every number must be traceable to a business event and every exception must have an accountable resolution path.

## Personas and daily work

| Persona | Main job | Success evidence |
| --- | --- | --- |
| Tenant/company administrator | Configure companies, locations, users and rules | Tenant isolation and explicit scoped grants |
| Catalog manager | Maintain SKUs, units, tracking and packaging | No duplicate or ambiguous scan identity |
| Buyer/requester | Request, compare, order and follow up supply | Approved demand to partial receipt with no lost remainder |
| Sales clerk/manager | Quote, confirm and allocate orders | Honest availability and visible backorders |
| Warehouse supervisor | Route work, resolve shortages and reconcile stores | Ledger and physical operation agree |
| Receiver/picker/packer/dispatcher | Scan and execute assigned work | Correct product, location, tracking and quantity |
| Counter | Perform independent blind counts | Reconciled observations without seeing system quantity |
| Quality inspector | Inspect, quarantine, release and recall | Ineligible stock cannot ship |
| Valuation analyst/auditor | Reconcile value and export to accounting | Complete lineage and no duplicate export |
| Platform/support operator | Operate SaaS and support approved customer cases | Bounded access, recoverable service, no cross-tenant leak |

## Product boundaries

A tenant is a customer organization. It may contain multiple legal companies, each with a base currency, branches and warehouses. Tenants never share operational stock. Product catalogs and partner codes are company-scoped in the baseline; controlled cloning can reuse templates without sharing ownership.

Include purchasing commercial documents and sales fulfillment documents. Do not create customer tax invoices, vendor bills, payments, statutory accounting statements, payroll or manufacturing orders. Capture external financial references and acquisition cost evidence only. Packing slips and order confirmations must be labeled accordingly.

Initial language is English with an internationalization-ready string catalog. ETB and Africa/Addis_Ababa are defaults, not global constants. Native iOS, self-hosted delivery, checkout POS and ecommerce storefronts are outside baseline. SaaS subscriptions are manually administered; no automated provider is implied.

## Acceptance targets

- All 156 capability requirements and critical scenarios have implementation evidence before full launch.
- Zero known unauthorized cross-tenant access; stock conservation, exact valuation reconciliation and idempotency are release blockers.
- Pilot with a distributor, retailer warehouse and lot/expiry business. Their exact identities are operational inputs, not invented in this plan.
- Initial performance envelope: 20 active tenants, up to five companies and 20 warehouses per tenant, 100,000 SKUs and five million movement rows per company, 50 concurrently active warehouse operators per tenant. Benchmark with at least two noisy-neighbor tenants. These are test design targets, not advertised capacity promises.
- Read p95 <=500ms and posting p95 <=1s server-side under the benchmark; essential web flows usable within five seconds on throttled mobile connectivity. Report exports are asynchronous with progress.
- RPO <=15 minutes and RTO <=4 hours demonstrated by restoration, not documentation alone.

## Releases

All 13 phases are in the baseline; intermediate phases are internal increments. A smaller pilot cannot bypass identity, stock integrity, valuation, privacy and recovery gates. No schedule or delivery date is promised without team capacity and measured implementation estimates.
