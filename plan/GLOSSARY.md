# Glossary

| Term | Meaning |
| --- | --- |
| Tenant | Customer organization and primary isolation boundary |
| Company | Legal/commercial entity with its own base currency and owned stock |
| Branch | Organizational/geographic grouping within a company |
| Warehouse / location | Physical facility / addressable zone, bin or virtual movement endpoint |
| SKU / variant | Stock identity / concrete attribute combination of a product template |
| Unit / packaging | Measurement unit / fixed number of units identified for handling |
| Lot / serial | Batch identity / individual-unit identity |
| Owner / custodian | Legal stock owner / party holding the goods physically |
| On hand / reserved / available | Physical balance / allocated eligible stock / eligible balance less reservations |
| Forecast | Dated eligible balance plus confirmed supply minus outstanding demand |
| Movement / projection | Immutable physical fact / rebuildable balance for fast reads |
| Transit | Controlled custody between shipment and destination receipt |
| Quarantine | Physically held but unavailable stock pending disposition |
| FEFO / FIFO | Earliest-removal physical selection / oldest-layer valuation or separately configured physical selection |
| Backorder | Explicit unfulfilled remainder of a confirmed operation |
| Consignment | Custody of partner-owned goods |
| Dropship | Supplier-to-customer fulfillment without internal warehouse receipt |
| Phantom kit | Commercial bundle fulfilled from component stock without manufacture |
| Landed cost | Additional acquisition charge allocated to inventory/consumed cost evidence |
| Valuation subledger | Inventory-only value evidence, not a general ledger |
| Accounting export | Versioned inventory journal proposal awaiting external acceptance |
| Posting | Authoritative atomic server commit; offline capture is not posting |
| Idempotency | Repeating one command returns its original result without repeating effects |
| Scope delta | Approved task/capability added beyond the frozen baseline |
