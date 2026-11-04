# End-to-end workflows

| Flow | Steps | Exceptions and accounting boundary |
| --- | --- | --- |
| Onboard tenant | Platform provisions tenant → verified admin → company/branch → roles → warehouses → catalog import → opening stock rehearsal | Entitlements and scoped access enforced before posting; no SaaS payment processor |
| Purchase to stock | Requisition → approval → RFQs/comparison → approved PO → partial receipt → quarantine if required → inspection → putaway | Overdelivery requires approval; rejected stock stays blocked; no vendor bill |
| Order to dispatch | Quotation → price/discount validation → confirmed order → reservation → pick → pack → dispatch | Partial supply becomes explicit backorder; short-picks release missing allocation; no tax invoice/payment |
| Transfer | Request → approval where configured → source shipment → transit → destination receipt → discrepancy resolution | Partial receipt leaves transit balance; approved scrap/return explains losses |
| Customer return | Original shipment → authorization → return receipt into quarantine → inspection → restock/scrap | Net return capped by shipped quantity and original serial; external credit handled elsewhere |
| Vendor return | Original receipt/rejection → authorization → supplier shipment → replace-or-close PO choice | Stock decreases through ledger; external vendor credit is a reference only |
| Count to adjustment | Scheduled scope → blind observation → movement reconciliation → recount if ambiguous → independent approval → signed adjustment | No overwrite of current balance; count snapshots and movement timestamps retained |
| Recall | Select lot/serial → block eligibility → trace remaining/shipped quantities → notify authorized team → returns/disposal → evidenced closure | Already-reserved goods rechecked at dispatch; no automatic external customer email without configured workflow |
| Replenish | Dated demand/supply → min/max/lead-time rules → suggestion → buyer acceptance → purchase approval or internal move | Suggestion is not confirmed supply; repeated run deduplicates |
| Consignment | Receive partner-owned → custody stock → approved acquisition or owner return | Custody excluded from owned valuation; ownership conversion has cost evidence |
| Dropship | Sales order → linked supplier PO → supplier delivery evidence → customer fulfillment | No internal warehouse increase; external-location history remains traceable |
| Intercompany | Approved request → linked seller order/buyer PO → shipment → transit/reconciliation → buyer receipt | Separate company grants, currency snapshots and valuation; no cross-tenant automatic trade |
| Kit | Versioned component definition → component availability/reservation → complete pick/dispatch | No finished-goods manufacturing; component shortage blocks complete-kit shipment |
| Value to export | Cost facts → method/layers → landed costs/revaluation → period reconciliation → approved export → external acknowledgement | Missing basis/mapping blocks release; this is not a general ledger |
| Offline work | Bootstrap assigned scope → capture local commands → durable queue → reconnect → validate/replay → acknowledged or conflict | Local screen never implies server stock committed; unresolved conflicts retain evidence |
| Offboard | Customer request → authorized export → holds review → revoke access → staged deletion → backup expiry evidence | Transaction retention follows reviewed schedule; no guessed legal period |

Map every flow to the capability registry and critical scenarios. Pilot scripts must use synthetic then customer-approved data, including partial quantities, more than one warehouse, and conflicting offline work.
