# Work breakdown by discipline

> Registry baseline 1.0 · 2026-11-04 · 51 modules · 790 tasks · 156 capabilities · 13 phases. Generated; edit registry.json and run `make plan-render`.

## backend

| Task | Phase | Module / lens | Deliverable |
| --- | --- | --- | --- |
| INV-008 | 2 | M02 / AUTHZ | Repository and delivery tooling: enforce access boundaries |
| INV-012 | 2 | M02 / INTEGRATION | Repository and delivery tooling: dependency integration |
| INV-015 | 2 | M03 / DATA | Tenants and SaaS entitlements: schema and migrations |
| INV-016 | 2 | M03 / API | Tenants and SaaS entitlements: request and response contracts |
| INV-017 | 2 | M03 / AUTHZ | Tenants and SaaS entitlements: enforce access boundaries |
| INV-018 | 2 | M03 / LIFE | Tenant onboarding |
| INV-019 | 2 | M03 / LIFE | Operator-managed plans |
| INV-020 | 2 | M03 / LIFE | Suspension and reactivation |
| INV-023 | 2 | M03 / NOTIFY | Tenants and SaaS entitlements: actionable notifications |
| INV-024 | 2 | M03 / ADMIN | Tenants and SaaS entitlements: administrative review controls |
| INV-025 | 2 | M03 / AUDIT | Tenants and SaaS entitlements: mutation evidence |
| INV-026 | 2 | M03 / EVENTS | Tenants and SaaS entitlements: versioned domain events |
| INV-027 | 2 | M03 / PRIVACY | Tenants and SaaS entitlements: data classification and retention |
| INV-028 | 2 | M03 / INTEGRATION | Tenants and SaaS entitlements: dependency integration |
| INV-031 | 2 | M04 / DATA | Identity, invitations and devices: schema and migrations |
| INV-032 | 2 | M04 / API | Identity, invitations and devices: request and response contracts |
| INV-033 | 2 | M04 / AUTHZ | Identity, invitations and devices: enforce access boundaries |
| INV-034 | 2 | M04 / LIFE | Invite and recovery |
| INV-035 | 2 | M04 / LIFE | MFA and sessions |
| INV-036 | 2 | M04 / LIFE | Device revocation |
| INV-039 | 2 | M04 / NOTIFY | Identity, invitations and devices: actionable notifications |
| INV-040 | 2 | M04 / ADMIN | Identity, invitations and devices: administrative review controls |
| INV-041 | 2 | M04 / AUDIT | Identity, invitations and devices: mutation evidence |
| INV-042 | 2 | M04 / EVENTS | Identity, invitations and devices: versioned domain events |
| INV-043 | 2 | M04 / PRIVACY | Identity, invitations and devices: data classification and retention |
| INV-044 | 2 | M04 / INTEGRATION | Identity, invitations and devices: dependency integration |
| INV-047 | 2 | M05 / DATA | Scoped roles and permissions: schema and migrations |
| INV-048 | 2 | M05 / API | Scoped roles and permissions: request and response contracts |
| INV-049 | 2 | M05 / AUTHZ | Scoped roles and permissions: enforce access boundaries |
| INV-050 | 2 | M05 / LIFE | Permission catalog |
| INV-051 | 2 | M05 / LIFE | Tenant company warehouse boundaries |
| INV-052 | 2 | M05 / LIFE | Support access |
| INV-055 | 2 | M05 / NOTIFY | Scoped roles and permissions: actionable notifications |
| INV-056 | 2 | M05 / ADMIN | Scoped roles and permissions: administrative review controls |
| INV-057 | 2 | M05 / AUDIT | Scoped roles and permissions: mutation evidence |
| INV-058 | 2 | M05 / EVENTS | Scoped roles and permissions: versioned domain events |
| INV-059 | 2 | M05 / PRIVACY | Scoped roles and permissions: data classification and retention |
| INV-060 | 2 | M05 / INTEGRATION | Scoped roles and permissions: dependency integration |
| INV-063 | 2 | M06 / DATA | Approval policies and decisions: schema and migrations |
| INV-064 | 2 | M06 / API | Approval policies and decisions: request and response contracts |
| INV-065 | 2 | M06 / AUTHZ | Approval policies and decisions: enforce access boundaries |
| INV-066 | 2 | M06 / LIFE | Policy routing |
| INV-067 | 2 | M06 / LIFE | Separation of duties |
| INV-068 | 2 | M06 / LIFE | Approval versioning |
| INV-071 | 2 | M06 / NOTIFY | Approval policies and decisions: actionable notifications |
| INV-072 | 2 | M06 / ADMIN | Approval policies and decisions: administrative review controls |
| INV-073 | 2 | M06 / AUDIT | Approval policies and decisions: mutation evidence |
| INV-074 | 2 | M06 / EVENTS | Approval policies and decisions: versioned domain events |
| INV-075 | 2 | M06 / PRIVACY | Approval policies and decisions: data classification and retention |
| INV-076 | 2 | M06 / INTEGRATION | Approval policies and decisions: dependency integration |
| INV-079 | 2 | M07 / DATA | Audit and business events: schema and migrations |
| INV-080 | 2 | M07 / API | Audit and business events: request and response contracts |
| INV-081 | 2 | M07 / AUTHZ | Audit and business events: enforce access boundaries |
| INV-082 | 2 | M07 / LIFE | Transactional audit |
| INV-083 | 2 | M07 / LIFE | Append-only evidence |
| INV-084 | 2 | M07 / LIFE | Event privacy |
| INV-087 | 2 | M07 / NOTIFY | Audit and business events: actionable notifications |
| INV-088 | 2 | M07 / ADMIN | Audit and business events: administrative review controls |
| INV-089 | 2 | M07 / AUDIT | Audit and business events: mutation evidence |
| INV-090 | 2 | M07 / EVENTS | Audit and business events: versioned domain events |
| INV-091 | 2 | M07 / PRIVACY | Audit and business events: data classification and retention |
| INV-092 | 2 | M07 / INTEGRATION | Audit and business events: dependency integration |
| INV-095 | 2 | M08 / DATA | Jobs, idempotency and delivery: schema and migrations |
| INV-096 | 2 | M08 / API | Jobs, idempotency and delivery: request and response contracts |
| INV-097 | 2 | M08 / AUTHZ | Jobs, idempotency and delivery: enforce access boundaries |
| INV-098 | 2 | M08 / LIFE | Idempotent commands |
| INV-099 | 2 | M08 / LIFE | Outbox processing |
| INV-100 | 2 | M08 / LIFE | Retries and dead letters |
| INV-103 | 2 | M08 / NOTIFY | Jobs, idempotency and delivery: actionable notifications |
| INV-104 | 2 | M08 / ADMIN | Jobs, idempotency and delivery: administrative review controls |
| INV-105 | 2 | M08 / AUDIT | Jobs, idempotency and delivery: mutation evidence |
| INV-106 | 2 | M08 / EVENTS | Jobs, idempotency and delivery: versioned domain events |
| INV-107 | 2 | M08 / PRIVACY | Jobs, idempotency and delivery: data classification and retention |
| INV-108 | 2 | M08 / INTEGRATION | Jobs, idempotency and delivery: dependency integration |
| INV-111 | 2 | M09 / DATA | Attachments and collaboration: schema and migrations |
| INV-112 | 2 | M09 / API | Attachments and collaboration: request and response contracts |
| INV-113 | 2 | M09 / AUTHZ | Attachments and collaboration: enforce access boundaries |
| INV-114 | 2 | M09 / LIFE | Private attachments |
| INV-115 | 2 | M09 / LIFE | Comments and evidence |
| INV-118 | 2 | M09 / NOTIFY | Attachments and collaboration: actionable notifications |
| INV-119 | 2 | M09 / ADMIN | Attachments and collaboration: administrative review controls |
| INV-120 | 2 | M09 / AUDIT | Attachments and collaboration: mutation evidence |
| INV-121 | 2 | M09 / EVENTS | Attachments and collaboration: versioned domain events |
| INV-122 | 2 | M09 / PRIVACY | Attachments and collaboration: data classification and retention |
| INV-123 | 2 | M09 / INTEGRATION | Attachments and collaboration: dependency integration |
| INV-126 | 2 | M10 / DATA | Notifications and preferences: schema and migrations |
| INV-127 | 2 | M10 / API | Notifications and preferences: request and response contracts |
| INV-128 | 2 | M10 / AUTHZ | Notifications and preferences: enforce access boundaries |
| INV-129 | 2 | M10 / LIFE | Notification routing |
| INV-130 | 2 | M10 / LIFE | Delivery and preferences |
| INV-133 | 2 | M10 / NOTIFY | Notifications and preferences: actionable notifications |
| INV-134 | 2 | M10 / ADMIN | Notifications and preferences: administrative review controls |
| INV-135 | 2 | M10 / AUDIT | Notifications and preferences: mutation evidence |
| INV-136 | 2 | M10 / EVENTS | Notifications and preferences: versioned domain events |
| INV-137 | 2 | M10 / PRIVACY | Notifications and preferences: data classification and retention |
| INV-138 | 2 | M10 / INTEGRATION | Notifications and preferences: dependency integration |
| INV-141 | 3 | M11 / AUTHZ | Design system and accessibility: enforce access boundaries |
| INV-144 | 3 | M11 / INTEGRATION | Design system and accessibility: dependency integration |
| INV-147 | 3 | M12 / DATA | Office and admin application shells: schema and migrations |
| INV-148 | 3 | M12 / API | Office and admin application shells: request and response contracts |
| INV-149 | 3 | M12 / AUTHZ | Office and admin application shells: enforce access boundaries |
| INV-150 | 3 | M12 / LIFE | Office context switching |
| INV-151 | 3 | M12 / LIFE | Platform admin separation |
| INV-152 | 3 | M12 / LIFE | Search and navigation |
| INV-155 | 3 | M12 / NOTIFY | Office and admin application shells: actionable notifications |
| INV-156 | 3 | M12 / ADMIN | Office and admin application shells: administrative review controls |
| INV-157 | 3 | M12 / AUDIT | Office and admin application shells: mutation evidence |
| INV-158 | 3 | M12 / EVENTS | Office and admin application shells: versioned domain events |
| INV-159 | 3 | M12 / PRIVACY | Office and admin application shells: data classification and retention |
| INV-160 | 3 | M12 / INTEGRATION | Office and admin application shells: dependency integration |
| INV-163 | 3 | M13 / DATA | Android foundation and sync protocol: schema and migrations |
| INV-164 | 3 | M13 / API | Android foundation and sync protocol: request and response contracts |
| INV-165 | 3 | M13 / AUTHZ | Android foundation and sync protocol: enforce access boundaries |
| INV-166 | 3 | M13 / LIFE | Durable local repository |
| INV-167 | 3 | M13 / LIFE | Sync protocol foundation |
| INV-168 | 3 | M13 / LIFE | Pending versus posted |
| INV-171 | 3 | M13 / NOTIFY | Android foundation and sync protocol: actionable notifications |
| INV-172 | 3 | M13 / ADMIN | Android foundation and sync protocol: administrative review controls |
| INV-173 | 3 | M13 / AUDIT | Android foundation and sync protocol: mutation evidence |
| INV-174 | 3 | M13 / EVENTS | Android foundation and sync protocol: versioned domain events |
| INV-175 | 3 | M13 / PRIVACY | Android foundation and sync protocol: data classification and retention |
| INV-176 | 3 | M13 / INTEGRATION | Android foundation and sync protocol: dependency integration |
| INV-177 | 3 | M13 / OFFLINE | Android foundation and sync protocol: interrupted-device recovery |
| INV-180 | 4 | M14 / DATA | Companies, branches and regional settings: schema and migrations |
| INV-181 | 4 | M14 / API | Companies, branches and regional settings: request and response contracts |
| INV-182 | 4 | M14 / AUTHZ | Companies, branches and regional settings: enforce access boundaries |
| INV-183 | 4 | M14 / LIFE | Company and branch setup |
| INV-184 | 4 | M14 / LIFE | Regional defaults |
| INV-185 | 4 | M14 / LIFE | Currency governance |
| INV-188 | 4 | M14 / NOTIFY | Companies, branches and regional settings: actionable notifications |
| INV-189 | 4 | M14 / ADMIN | Companies, branches and regional settings: administrative review controls |
| INV-190 | 4 | M14 / AUDIT | Companies, branches and regional settings: mutation evidence |
| INV-191 | 4 | M14 / EVENTS | Companies, branches and regional settings: versioned domain events |
| INV-192 | 4 | M14 / PRIVACY | Companies, branches and regional settings: data classification and retention |
| INV-193 | 4 | M14 / INTEGRATION | Companies, branches and regional settings: dependency integration |
| INV-196 | 4 | M15 / DATA | Suppliers and customers: schema and migrations |
| INV-197 | 4 | M15 / API | Suppliers and customers: request and response contracts |
| INV-198 | 4 | M15 / AUTHZ | Suppliers and customers: enforce access boundaries |
| INV-199 | 4 | M15 / LIFE | Partner directory |
| INV-200 | 4 | M15 / LIFE | Partner commercial references |
| INV-201 | 4 | M15 / LIFE | Contact privacy |
| INV-204 | 4 | M15 / NOTIFY | Suppliers and customers: actionable notifications |
| INV-205 | 4 | M15 / ADMIN | Suppliers and customers: administrative review controls |
| INV-206 | 4 | M15 / AUDIT | Suppliers and customers: mutation evidence |
| INV-207 | 4 | M15 / EVENTS | Suppliers and customers: versioned domain events |
| INV-208 | 4 | M15 / PRIVACY | Suppliers and customers: data classification and retention |
| INV-209 | 4 | M15 / INTEGRATION | Suppliers and customers: dependency integration |
| INV-212 | 4 | M16 / DATA | Products, variants and packaging: schema and migrations |
| INV-213 | 4 | M16 / API | Products, variants and packaging: request and response contracts |
| INV-214 | 4 | M16 / AUTHZ | Products, variants and packaging: enforce access boundaries |
| INV-215 | 4 | M16 / LIFE | Product and variant catalog |
| INV-216 | 4 | M16 / LIFE | Tracking configuration |
| INV-217 | 4 | M16 / LIFE | Packaging and barcode aliases |
| INV-218 | 4 | M16 / LIFE | Catalog import |
| INV-221 | 4 | M16 / NOTIFY | Products, variants and packaging: actionable notifications |
| INV-222 | 4 | M16 / ADMIN | Products, variants and packaging: administrative review controls |
| INV-223 | 4 | M16 / AUDIT | Products, variants and packaging: mutation evidence |
| INV-224 | 4 | M16 / EVENTS | Products, variants and packaging: versioned domain events |
| INV-225 | 4 | M16 / PRIVACY | Products, variants and packaging: data classification and retention |
| INV-226 | 4 | M16 / INTEGRATION | Products, variants and packaging: dependency integration |
| INV-229 | 4 | M17 / DATA | Units and exact arithmetic: schema and migrations |
| INV-230 | 4 | M17 / API | Units and exact arithmetic: request and response contracts |
| INV-231 | 4 | M17 / AUTHZ | Units and exact arithmetic: enforce access boundaries |
| INV-232 | 4 | M17 / LIFE | Unit conversions |
| INV-233 | 4 | M17 / LIFE | Quantity precision |
| INV-234 | 4 | M17 / LIFE | Monetary precision |
| INV-237 | 4 | M17 / NOTIFY | Units and exact arithmetic: actionable notifications |
| INV-238 | 4 | M17 / ADMIN | Units and exact arithmetic: administrative review controls |
| INV-239 | 4 | M17 / AUDIT | Units and exact arithmetic: mutation evidence |
| INV-240 | 4 | M17 / EVENTS | Units and exact arithmetic: versioned domain events |
| INV-241 | 4 | M17 / PRIVACY | Units and exact arithmetic: data classification and retention |
| INV-242 | 4 | M17 / INTEGRATION | Units and exact arithmetic: dependency integration |
| INV-245 | 4 | M18 / DATA | Warehouses and location hierarchy: schema and migrations |
| INV-246 | 4 | M18 / API | Warehouses and location hierarchy: request and response contracts |
| INV-247 | 4 | M18 / AUTHZ | Warehouses and location hierarchy: enforce access boundaries |
| INV-248 | 4 | M18 / LIFE | Location hierarchy |
| INV-249 | 4 | M18 / LIFE | Operational areas |
| INV-250 | 4 | M18 / LIFE | Archival and capacity |
| INV-253 | 4 | M18 / NOTIFY | Warehouses and location hierarchy: actionable notifications |
| INV-254 | 4 | M18 / ADMIN | Warehouses and location hierarchy: administrative review controls |
| INV-255 | 4 | M18 / AUDIT | Warehouses and location hierarchy: mutation evidence |
| INV-256 | 4 | M18 / EVENTS | Warehouses and location hierarchy: versioned domain events |
| INV-257 | 4 | M18 / PRIVACY | Warehouses and location hierarchy: data classification and retention |
| INV-258 | 4 | M18 / INTEGRATION | Warehouses and location hierarchy: dependency integration |
| INV-261 | 4 | M19 / DATA | Lot, serial and ownership identities: schema and migrations |
| INV-262 | 4 | M19 / API | Lot, serial and ownership identities: request and response contracts |
| INV-263 | 4 | M19 / AUTHZ | Lot, serial and ownership identities: enforce access boundaries |
| INV-264 | 4 | M19 / LIFE | Lot and serial identity |
| INV-265 | 4 | M19 / LIFE | Ownership dimensions |
| INV-266 | 4 | M19 / LIFE | Receipt tracking requirements |
| INV-269 | 4 | M19 / NOTIFY | Lot, serial and ownership identities: actionable notifications |
| INV-270 | 4 | M19 / ADMIN | Lot, serial and ownership identities: administrative review controls |
| INV-271 | 4 | M19 / AUDIT | Lot, serial and ownership identities: mutation evidence |
| INV-272 | 4 | M19 / EVENTS | Lot, serial and ownership identities: versioned domain events |
| INV-273 | 4 | M19 / PRIVACY | Lot, serial and ownership identities: data classification and retention |
| INV-274 | 4 | M19 / INTEGRATION | Lot, serial and ownership identities: dependency integration |
| INV-277 | 5 | M20 / DATA | Immutable stock ledger and projections: schema and migrations |
| INV-278 | 5 | M20 / API | Immutable stock ledger and projections: request and response contracts |
| INV-279 | 5 | M20 / AUTHZ | Immutable stock ledger and projections: enforce access boundaries |
| INV-280 | 5 | M20 / LIFE | Posting transaction |
| INV-281 | 5 | M20 / LIFE | No negative physical stock |
| INV-282 | 5 | M20 / LIFE | Reversal and rebuild |
| INV-283 | 5 | M20 / LIFE | Cost fact capture |
| INV-286 | 5 | M20 / NOTIFY | Immutable stock ledger and projections: actionable notifications |
| INV-287 | 5 | M20 / ADMIN | Immutable stock ledger and projections: administrative review controls |
| INV-288 | 5 | M20 / AUDIT | Immutable stock ledger and projections: mutation evidence |
| INV-289 | 5 | M20 / EVENTS | Immutable stock ledger and projections: versioned domain events |
| INV-290 | 5 | M20 / PRIVACY | Immutable stock ledger and projections: data classification and retention |
| INV-291 | 5 | M20 / INTEGRATION | Immutable stock ledger and projections: dependency integration |
| INV-294 | 5 | M21 / DATA | Reservations and availability: schema and migrations |
| INV-295 | 5 | M21 / API | Reservations and availability: request and response contracts |
| INV-296 | 5 | M21 / AUTHZ | Reservations and availability: enforce access boundaries |
| INV-297 | 5 | M21 / LIFE | Atomic allocation |
| INV-298 | 5 | M21 / LIFE | Partial allocation and release |
| INV-299 | 5 | M21 / LIFE | Availability and forecast |
| INV-302 | 5 | M21 / NOTIFY | Reservations and availability: actionable notifications |
| INV-303 | 5 | M21 / ADMIN | Reservations and availability: administrative review controls |
| INV-304 | 5 | M21 / AUDIT | Reservations and availability: mutation evidence |
| INV-305 | 5 | M21 / EVENTS | Reservations and availability: versioned domain events |
| INV-306 | 5 | M21 / PRIVACY | Reservations and availability: data classification and retention |
| INV-307 | 5 | M21 / INTEGRATION | Reservations and availability: dependency integration |
| INV-310 | 5 | M22 / DATA | Core receipts, issues and opening stock: schema and migrations |
| INV-311 | 5 | M22 / API | Core receipts, issues and opening stock: request and response contracts |
| INV-312 | 5 | M22 / AUTHZ | Core receipts, issues and opening stock: enforce access boundaries |
| INV-313 | 5 | M22 / LIFE | Opening stock |
| INV-314 | 5 | M22 / LIFE | Receipt and internal issue |
| INV-315 | 5 | M22 / LIFE | Partial operations and backorders |
| INV-318 | 5 | M22 / NOTIFY | Core receipts, issues and opening stock: actionable notifications |
| INV-319 | 5 | M22 / ADMIN | Core receipts, issues and opening stock: administrative review controls |
| INV-320 | 5 | M22 / AUDIT | Core receipts, issues and opening stock: mutation evidence |
| INV-321 | 5 | M22 / EVENTS | Core receipts, issues and opening stock: versioned domain events |
| INV-322 | 5 | M22 / PRIVACY | Core receipts, issues and opening stock: data classification and retention |
| INV-323 | 5 | M22 / INTEGRATION | Core receipts, issues and opening stock: dependency integration |
| INV-326 | 5 | M23 / DATA | Transfers and in-transit custody: schema and migrations |
| INV-327 | 5 | M23 / API | Transfers and in-transit custody: request and response contracts |
| INV-328 | 5 | M23 / AUTHZ | Transfers and in-transit custody: enforce access boundaries |
| INV-329 | 5 | M23 / LIFE | Immediate and staged transfers |
| INV-330 | 5 | M23 / LIFE | Partial receipt and discrepancy |
| INV-331 | 5 | M23 / LIFE | Transfer conservation |
| INV-334 | 5 | M23 / NOTIFY | Transfers and in-transit custody: actionable notifications |
| INV-335 | 5 | M23 / ADMIN | Transfers and in-transit custody: administrative review controls |
| INV-336 | 5 | M23 / AUDIT | Transfers and in-transit custody: mutation evidence |
| INV-337 | 5 | M23 / EVENTS | Transfers and in-transit custody: versioned domain events |
| INV-338 | 5 | M23 / PRIVACY | Transfers and in-transit custody: data classification and retention |
| INV-339 | 5 | M23 / INTEGRATION | Transfers and in-transit custody: dependency integration |
| INV-342 | 6 | M24 / DATA | Requisitions, RFQs and purchase orders: schema and migrations |
| INV-343 | 6 | M24 / API | Requisitions, RFQs and purchase orders: request and response contracts |
| INV-344 | 6 | M24 / AUTHZ | Requisitions, RFQs and purchase orders: enforce access boundaries |
| INV-345 | 6 | M24 / LIFE | Requisition and quotation comparison |
| INV-346 | 6 | M24 / LIFE | Approved PO revisions |
| INV-347 | 6 | M24 / LIFE | Blanket order releases |
| INV-348 | 6 | M24 / LIFE | Purchase cancellation |
| INV-351 | 6 | M24 / NOTIFY | Requisitions, RFQs and purchase orders: actionable notifications |
| INV-352 | 6 | M24 / ADMIN | Requisitions, RFQs and purchase orders: administrative review controls |
| INV-353 | 6 | M24 / AUDIT | Requisitions, RFQs and purchase orders: mutation evidence |
| INV-354 | 6 | M24 / EVENTS | Requisitions, RFQs and purchase orders: versioned domain events |
| INV-355 | 6 | M24 / PRIVACY | Requisitions, RFQs and purchase orders: data classification and retention |
| INV-356 | 6 | M24 / INTEGRATION | Requisitions, RFQs and purchase orders: dependency integration |
| INV-359 | 6 | M25 / DATA | Supplier receiving and inspection handoff: schema and migrations |
| INV-360 | 6 | M25 / API | Supplier receiving and inspection handoff: request and response contracts |
| INV-361 | 6 | M25 / AUTHZ | Supplier receiving and inspection handoff: enforce access boundaries |
| INV-362 | 6 | M25 / LIFE | PO receipt matching |
| INV-363 | 6 | M25 / LIFE | Receive to quarantine |
| INV-364 | 6 | M25 / LIFE | Receipt cost snapshot |
| INV-367 | 6 | M25 / NOTIFY | Supplier receiving and inspection handoff: actionable notifications |
| INV-368 | 6 | M25 / ADMIN | Supplier receiving and inspection handoff: administrative review controls |
| INV-369 | 6 | M25 / AUDIT | Supplier receiving and inspection handoff: mutation evidence |
| INV-370 | 6 | M25 / EVENTS | Supplier receiving and inspection handoff: versioned domain events |
| INV-371 | 6 | M25 / PRIVACY | Supplier receiving and inspection handoff: data classification and retention |
| INV-372 | 6 | M25 / INTEGRATION | Supplier receiving and inspection handoff: dependency integration |
| INV-375 | 6 | M26 / DATA | Quality inspections and disposition: schema and migrations |
| INV-376 | 6 | M26 / API | Quality inspections and disposition: request and response contracts |
| INV-377 | 6 | M26 / AUTHZ | Quality inspections and disposition: enforce access boundaries |
| INV-378 | 6 | M26 / LIFE | Inspection execution |
| INV-379 | 6 | M26 / LIFE | Split disposition |
| INV-380 | 6 | M26 / LIFE | Reinspection and evidence |
| INV-383 | 6 | M26 / NOTIFY | Quality inspections and disposition: actionable notifications |
| INV-384 | 6 | M26 / ADMIN | Quality inspections and disposition: administrative review controls |
| INV-385 | 6 | M26 / AUDIT | Quality inspections and disposition: mutation evidence |
| INV-386 | 6 | M26 / EVENTS | Quality inspections and disposition: versioned domain events |
| INV-387 | 6 | M26 / PRIVACY | Quality inspections and disposition: data classification and retention |
| INV-388 | 6 | M26 / INTEGRATION | Quality inspections and disposition: dependency integration |
| INV-391 | 7 | M27 / DATA | Sales quotations and orders: schema and migrations |
| INV-392 | 7 | M27 / API | Sales quotations and orders: request and response contracts |
| INV-393 | 7 | M27 / AUTHZ | Sales quotations and orders: enforce access boundaries |
| INV-394 | 7 | M27 / LIFE | Quotation and pricing |
| INV-395 | 7 | M27 / LIFE | Sales confirmation |
| INV-396 | 7 | M27 / LIFE | Order changes |
| INV-399 | 7 | M27 / NOTIFY | Sales quotations and orders: actionable notifications |
| INV-400 | 7 | M27 / ADMIN | Sales quotations and orders: administrative review controls |
| INV-401 | 7 | M27 / AUDIT | Sales quotations and orders: mutation evidence |
| INV-402 | 7 | M27 / EVENTS | Sales quotations and orders: versioned domain events |
| INV-403 | 7 | M27 / PRIVACY | Sales quotations and orders: data classification and retention |
| INV-404 | 7 | M27 / INTEGRATION | Sales quotations and orders: dependency integration |
| INV-407 | 7 | M28 / DATA | Pick, pack and dispatch: schema and migrations |
| INV-408 | 7 | M28 / API | Pick, pack and dispatch: request and response contracts |
| INV-409 | 7 | M28 / AUTHZ | Pick, pack and dispatch: enforce access boundaries |
| INV-410 | 7 | M28 / LIFE | Pick verification |
| INV-411 | 7 | M28 / LIFE | Packing control |
| INV-412 | 7 | M28 / LIFE | Dispatch and delivery records |
| INV-415 | 7 | M28 / NOTIFY | Pick, pack and dispatch: actionable notifications |
| INV-416 | 7 | M28 / ADMIN | Pick, pack and dispatch: administrative review controls |
| INV-417 | 7 | M28 / AUDIT | Pick, pack and dispatch: mutation evidence |
| INV-418 | 7 | M28 / EVENTS | Pick, pack and dispatch: versioned domain events |
| INV-419 | 7 | M28 / PRIVACY | Pick, pack and dispatch: data classification and retention |
| INV-420 | 7 | M28 / INTEGRATION | Pick, pack and dispatch: dependency integration |
| INV-423 | 8 | M29 / DATA | Customer and vendor returns: schema and migrations |
| INV-424 | 8 | M29 / API | Customer and vendor returns: request and response contracts |
| INV-425 | 8 | M29 / AUTHZ | Customer and vendor returns: enforce access boundaries |
| INV-426 | 8 | M29 / LIFE | Linked return entitlement |
| INV-427 | 8 | M29 / LIFE | Customer return inspection |
| INV-428 | 8 | M29 / LIFE | Vendor returns |
| INV-431 | 8 | M29 / NOTIFY | Customer and vendor returns: actionable notifications |
| INV-432 | 8 | M29 / ADMIN | Customer and vendor returns: administrative review controls |
| INV-433 | 8 | M29 / AUDIT | Customer and vendor returns: mutation evidence |
| INV-434 | 8 | M29 / EVENTS | Customer and vendor returns: versioned domain events |
| INV-435 | 8 | M29 / PRIVACY | Customer and vendor returns: data classification and retention |
| INV-436 | 8 | M29 / INTEGRATION | Customer and vendor returns: dependency integration |
| INV-439 | 8 | M30 / DATA | Expiry, recalls and scrap: schema and migrations |
| INV-440 | 8 | M30 / API | Expiry, recalls and scrap: request and response contracts |
| INV-441 | 8 | M30 / AUTHZ | Expiry, recalls and scrap: enforce access boundaries |
| INV-442 | 8 | M30 / LIFE | Expiry and FEFO |
| INV-443 | 8 | M30 / LIFE | Recall genealogy |
| INV-444 | 8 | M30 / LIFE | Approved scrap |
| INV-447 | 8 | M30 / NOTIFY | Expiry, recalls and scrap: actionable notifications |
| INV-448 | 8 | M30 / ADMIN | Expiry, recalls and scrap: administrative review controls |
| INV-449 | 8 | M30 / AUDIT | Expiry, recalls and scrap: mutation evidence |
| INV-450 | 8 | M30 / EVENTS | Expiry, recalls and scrap: versioned domain events |
| INV-451 | 8 | M30 / PRIVACY | Expiry, recalls and scrap: data classification and retention |
| INV-452 | 8 | M30 / INTEGRATION | Expiry, recalls and scrap: dependency integration |
| INV-455 | 8 | M31 / DATA | Blind counts and reconciliation: schema and migrations |
| INV-456 | 8 | M31 / API | Blind counts and reconciliation: request and response contracts |
| INV-457 | 8 | M31 / AUTHZ | Blind counts and reconciliation: enforce access boundaries |
| INV-458 | 8 | M31 / LIFE | Blind and cycle counting |
| INV-459 | 8 | M31 / LIFE | Moving-stock reconciliation |
| INV-460 | 8 | M31 / LIFE | Variance approval |
| INV-463 | 8 | M31 / NOTIFY | Blind counts and reconciliation: actionable notifications |
| INV-464 | 8 | M31 / ADMIN | Blind counts and reconciliation: administrative review controls |
| INV-465 | 8 | M31 / AUDIT | Blind counts and reconciliation: mutation evidence |
| INV-466 | 8 | M31 / EVENTS | Blind counts and reconciliation: versioned domain events |
| INV-467 | 8 | M31 / PRIVACY | Blind counts and reconciliation: data classification and retention |
| INV-468 | 8 | M31 / INTEGRATION | Blind counts and reconciliation: dependency integration |
| INV-471 | 9 | M32 / DATA | Routes, putaway and cross-docking: schema and migrations |
| INV-472 | 9 | M32 / API | Routes, putaway and cross-docking: request and response contracts |
| INV-473 | 9 | M32 / AUTHZ | Routes, putaway and cross-docking: enforce access boundaries |
| INV-474 | 9 | M32 / LIFE | Multi-step routes |
| INV-475 | 9 | M32 / LIFE | Putaway and capacity |
| INV-476 | 9 | M32 / LIFE | Cross-docking |
| INV-479 | 9 | M32 / NOTIFY | Routes, putaway and cross-docking: actionable notifications |
| INV-480 | 9 | M32 / ADMIN | Routes, putaway and cross-docking: administrative review controls |
| INV-481 | 9 | M32 / AUDIT | Routes, putaway and cross-docking: mutation evidence |
| INV-482 | 9 | M32 / EVENTS | Routes, putaway and cross-docking: versioned domain events |
| INV-483 | 9 | M32 / PRIVACY | Routes, putaway and cross-docking: data classification and retention |
| INV-484 | 9 | M32 / INTEGRATION | Routes, putaway and cross-docking: dependency integration |
| INV-487 | 9 | M33 / DATA | Batch and wave picking: schema and migrations |
| INV-488 | 9 | M33 / API | Batch and wave picking: request and response contracts |
| INV-489 | 9 | M33 / AUTHZ | Batch and wave picking: enforce access boundaries |
| INV-490 | 9 | M33 / LIFE | Batch and wave formation |
| INV-491 | 9 | M33 / LIFE | Picking strategies |
| INV-492 | 9 | M33 / LIFE | Replanning exceptions |
| INV-495 | 9 | M33 / NOTIFY | Batch and wave picking: actionable notifications |
| INV-496 | 9 | M33 / ADMIN | Batch and wave picking: administrative review controls |
| INV-497 | 9 | M33 / AUDIT | Batch and wave picking: mutation evidence |
| INV-498 | 9 | M33 / EVENTS | Batch and wave picking: versioned domain events |
| INV-499 | 9 | M33 / PRIVACY | Batch and wave picking: data classification and retention |
| INV-500 | 9 | M33 / INTEGRATION | Batch and wave picking: dependency integration |
| INV-503 | 9 | M34 / DATA | Replenishment and demand planning: schema and migrations |
| INV-504 | 9 | M34 / API | Replenishment and demand planning: request and response contracts |
| INV-505 | 9 | M34 / AUTHZ | Replenishment and demand planning: enforce access boundaries |
| INV-506 | 9 | M34 / LIFE | Min-max and safety stock |
| INV-507 | 9 | M34 / LIFE | Buyer approval |
| INV-508 | 9 | M34 / LIFE | Pick-face replenishment |
| INV-511 | 9 | M34 / NOTIFY | Replenishment and demand planning: actionable notifications |
| INV-512 | 9 | M34 / ADMIN | Replenishment and demand planning: administrative review controls |
| INV-513 | 9 | M34 / AUDIT | Replenishment and demand planning: mutation evidence |
| INV-514 | 9 | M34 / EVENTS | Replenishment and demand planning: versioned domain events |
| INV-515 | 9 | M34 / PRIVACY | Replenishment and demand planning: data classification and retention |
| INV-516 | 9 | M34 / INTEGRATION | Replenishment and demand planning: dependency integration |
| INV-519 | 9 | M35 / DATA | Consignment and owner-separated stock: schema and migrations |
| INV-520 | 9 | M35 / API | Consignment and owner-separated stock: request and response contracts |
| INV-521 | 9 | M35 / AUTHZ | Consignment and owner-separated stock: enforce access boundaries |
| INV-522 | 9 | M35 / LIFE | Consignment custody |
| INV-523 | 9 | M35 / LIFE | Ownership acquisition |
| INV-524 | 9 | M35 / LIFE | Owner returns |
| INV-527 | 9 | M35 / NOTIFY | Consignment and owner-separated stock: actionable notifications |
| INV-528 | 9 | M35 / ADMIN | Consignment and owner-separated stock: administrative review controls |
| INV-529 | 9 | M35 / AUDIT | Consignment and owner-separated stock: mutation evidence |
| INV-530 | 9 | M35 / EVENTS | Consignment and owner-separated stock: versioned domain events |
| INV-531 | 9 | M35 / PRIVACY | Consignment and owner-separated stock: data classification and retention |
| INV-532 | 9 | M35 / INTEGRATION | Consignment and owner-separated stock: dependency integration |
| INV-535 | 9 | M36 / DATA | Dropship fulfillment: schema and migrations |
| INV-536 | 9 | M36 / API | Dropship fulfillment: request and response contracts |
| INV-537 | 9 | M36 / AUTHZ | Dropship fulfillment: enforce access boundaries |
| INV-538 | 9 | M36 / LIFE | Linked supplier fulfillment |
| INV-539 | 9 | M36 / LIFE | Supplier delivery evidence |
| INV-540 | 9 | M36 / LIFE | Dropship returns |
| INV-543 | 9 | M36 / NOTIFY | Dropship fulfillment: actionable notifications |
| INV-544 | 9 | M36 / ADMIN | Dropship fulfillment: administrative review controls |
| INV-545 | 9 | M36 / AUDIT | Dropship fulfillment: mutation evidence |
| INV-546 | 9 | M36 / EVENTS | Dropship fulfillment: versioned domain events |
| INV-547 | 9 | M36 / PRIVACY | Dropship fulfillment: data classification and retention |
| INV-548 | 9 | M36 / INTEGRATION | Dropship fulfillment: dependency integration |
| INV-551 | 9 | M37 / DATA | Intercompany trade and transfers: schema and migrations |
| INV-552 | 9 | M37 / API | Intercompany trade and transfers: request and response contracts |
| INV-553 | 9 | M37 / AUTHZ | Intercompany trade and transfers: enforce access boundaries |
| INV-554 | 9 | M37 / LIFE | Paired commercial documents |
| INV-555 | 9 | M37 / LIFE | Company-local ledgers |
| INV-556 | 9 | M37 / LIFE | Independent permissions |
| INV-559 | 9 | M37 / NOTIFY | Intercompany trade and transfers: actionable notifications |
| INV-560 | 9 | M37 / ADMIN | Intercompany trade and transfers: administrative review controls |
| INV-561 | 9 | M37 / AUDIT | Intercompany trade and transfers: mutation evidence |
| INV-562 | 9 | M37 / EVENTS | Intercompany trade and transfers: versioned domain events |
| INV-563 | 9 | M37 / PRIVACY | Intercompany trade and transfers: data classification and retention |
| INV-564 | 9 | M37 / INTEGRATION | Intercompany trade and transfers: dependency integration |
| INV-567 | 9 | M38 / DATA | Kits without manufacturing: schema and migrations |
| INV-568 | 9 | M38 / API | Kits without manufacturing: request and response contracts |
| INV-569 | 9 | M38 / AUTHZ | Kits without manufacturing: enforce access boundaries |
| INV-570 | 9 | M38 / LIFE | Phantom kit definitions |
| INV-571 | 9 | M38 / LIFE | Kit allocation and fulfillment |
| INV-572 | 9 | M38 / LIFE | Kit returns |
| INV-575 | 9 | M38 / NOTIFY | Kits without manufacturing: actionable notifications |
| INV-576 | 9 | M38 / ADMIN | Kits without manufacturing: administrative review controls |
| INV-577 | 9 | M38 / AUDIT | Kits without manufacturing: mutation evidence |
| INV-578 | 9 | M38 / EVENTS | Kits without manufacturing: versioned domain events |
| INV-579 | 9 | M38 / PRIVACY | Kits without manufacturing: data classification and retention |
| INV-580 | 9 | M38 / INTEGRATION | Kits without manufacturing: dependency integration |
| INV-583 | 10 | M39 / DATA | Offline Android warehouse workflows: schema and migrations |
| INV-584 | 10 | M39 / API | Offline Android warehouse workflows: request and response contracts |
| INV-585 | 10 | M39 / AUTHZ | Offline Android warehouse workflows: enforce access boundaries |
| INV-586 | 10 | M39 / LIFE | Offline operational capture |
| INV-587 | 10 | M39 / LIFE | Conflict review |
| INV-588 | 10 | M39 / LIFE | Reconnect recovery |
| INV-591 | 10 | M39 / NOTIFY | Offline Android warehouse workflows: actionable notifications |
| INV-592 | 10 | M39 / ADMIN | Offline Android warehouse workflows: administrative review controls |
| INV-593 | 10 | M39 / AUDIT | Offline Android warehouse workflows: mutation evidence |
| INV-594 | 10 | M39 / EVENTS | Offline Android warehouse workflows: versioned domain events |
| INV-595 | 10 | M39 / PRIVACY | Offline Android warehouse workflows: data classification and retention |
| INV-596 | 10 | M39 / INTEGRATION | Offline Android warehouse workflows: dependency integration |
| INV-597 | 10 | M39 / OFFLINE | Offline Android warehouse workflows: interrupted-device recovery |
| INV-600 | 10 | M40 / DATA | Scanners, labels and printer interfaces: schema and migrations |
| INV-601 | 10 | M40 / API | Scanners, labels and printer interfaces: request and response contracts |
| INV-602 | 10 | M40 / AUTHZ | Scanners, labels and printer interfaces: enforce access boundaries |
| INV-603 | 10 | M40 / LIFE | Camera and handheld scanning |
| INV-604 | 10 | M40 / LIFE | GS1 parsing |
| INV-605 | 10 | M40 / LIFE | Label generation and reprints |
| INV-608 | 10 | M40 / NOTIFY | Scanners, labels and printer interfaces: actionable notifications |
| INV-609 | 10 | M40 / ADMIN | Scanners, labels and printer interfaces: administrative review controls |
| INV-610 | 10 | M40 / AUDIT | Scanners, labels and printer interfaces: mutation evidence |
| INV-611 | 10 | M40 / EVENTS | Scanners, labels and printer interfaces: versioned domain events |
| INV-612 | 10 | M40 / PRIVACY | Scanners, labels and printer interfaces: data classification and retention |
| INV-613 | 10 | M40 / INTEGRATION | Scanners, labels and printer interfaces: dependency integration |
| INV-614 | 10 | M40 / OFFLINE | Scanners, labels and printer interfaces: interrupted-device recovery |
| INV-617 | 11 | M41 / DATA | Valuation methods and subledger: schema and migrations |
| INV-618 | 11 | M41 / API | Valuation methods and subledger: request and response contracts |
| INV-619 | 11 | M41 / AUTHZ | Valuation methods and subledger: enforce access boundaries |
| INV-620 | 11 | M41 / LIFE | FIFO costing |
| INV-621 | 11 | M41 / LIFE | Weighted-average costing |
| INV-622 | 11 | M41 / LIFE | Standard costing |
| INV-623 | 11 | M41 / LIFE | Returns and replay |
| INV-626 | 11 | M41 / NOTIFY | Valuation methods and subledger: actionable notifications |
| INV-627 | 11 | M41 / ADMIN | Valuation methods and subledger: administrative review controls |
| INV-628 | 11 | M41 / AUDIT | Valuation methods and subledger: mutation evidence |
| INV-629 | 11 | M41 / EVENTS | Valuation methods and subledger: versioned domain events |
| INV-630 | 11 | M41 / PRIVACY | Valuation methods and subledger: data classification and retention |
| INV-631 | 11 | M41 / INTEGRATION | Valuation methods and subledger: dependency integration |
| INV-634 | 11 | M42 / DATA | Landed costs and revaluation: schema and migrations |
| INV-635 | 11 | M42 / API | Landed costs and revaluation: request and response contracts |
| INV-636 | 11 | M42 / AUTHZ | Landed costs and revaluation: enforce access boundaries |
| INV-637 | 11 | M42 / LIFE | Charge allocation |
| INV-638 | 11 | M42 / LIFE | Remainder and consumed stock |
| INV-639 | 11 | M42 / LIFE | Approved revaluation |
| INV-642 | 11 | M42 / NOTIFY | Landed costs and revaluation: actionable notifications |
| INV-643 | 11 | M42 / ADMIN | Landed costs and revaluation: administrative review controls |
| INV-644 | 11 | M42 / AUDIT | Landed costs and revaluation: mutation evidence |
| INV-645 | 11 | M42 / EVENTS | Landed costs and revaluation: versioned domain events |
| INV-646 | 11 | M42 / PRIVACY | Landed costs and revaluation: data classification and retention |
| INV-647 | 11 | M42 / INTEGRATION | Landed costs and revaluation: dependency integration |
| INV-650 | 11 | M43 / DATA | Valuation periods and reconciliation: schema and migrations |
| INV-651 | 11 | M43 / API | Valuation periods and reconciliation: request and response contracts |
| INV-652 | 11 | M43 / AUTHZ | Valuation periods and reconciliation: enforce access boundaries |
| INV-653 | 11 | M43 / LIFE | Period reconciliation |
| INV-654 | 11 | M43 / LIFE | Close prerequisites |
| INV-655 | 11 | M43 / LIFE | Controlled reopen |
| INV-658 | 11 | M43 / NOTIFY | Valuation periods and reconciliation: actionable notifications |
| INV-659 | 11 | M43 / ADMIN | Valuation periods and reconciliation: administrative review controls |
| INV-660 | 11 | M43 / AUDIT | Valuation periods and reconciliation: mutation evidence |
| INV-661 | 11 | M43 / EVENTS | Valuation periods and reconciliation: versioned domain events |
| INV-662 | 11 | M43 / PRIVACY | Valuation periods and reconciliation: data classification and retention |
| INV-663 | 11 | M43 / INTEGRATION | Valuation periods and reconciliation: dependency integration |
| INV-666 | 11 | M44 / DATA | Accounting export batches: schema and migrations |
| INV-667 | 11 | M44 / API | Accounting export batches: request and response contracts |
| INV-668 | 11 | M44 / AUTHZ | Accounting export batches: enforce access boundaries |
| INV-669 | 11 | M44 / LIFE | Balanced export format |
| INV-670 | 11 | M44 / LIFE | Delivery acknowledgement |
| INV-671 | 11 | M44 / LIFE | Accounting boundary |
| INV-674 | 11 | M44 / NOTIFY | Accounting export batches: actionable notifications |
| INV-675 | 11 | M44 / ADMIN | Accounting export batches: administrative review controls |
| INV-676 | 11 | M44 / AUDIT | Accounting export batches: mutation evidence |
| INV-677 | 11 | M44 / EVENTS | Accounting export batches: versioned domain events |
| INV-678 | 11 | M44 / PRIVACY | Accounting export batches: data classification and retention |
| INV-679 | 11 | M44 / INTEGRATION | Accounting export batches: dependency integration |
| INV-682 | 12 | M45 / DATA | Operational reports and analytics: schema and migrations |
| INV-683 | 12 | M45 / API | Operational reports and analytics: request and response contracts |
| INV-684 | 12 | M45 / AUTHZ | Operational reports and analytics: enforce access boundaries |
| INV-685 | 12 | M45 / LIFE | As-of stock and value |
| INV-686 | 12 | M45 / LIFE | Service metrics |
| INV-687 | 12 | M45 / LIFE | Secure exports |
| INV-690 | 12 | M45 / NOTIFY | Operational reports and analytics: actionable notifications |
| INV-691 | 12 | M45 / ADMIN | Operational reports and analytics: administrative review controls |
| INV-692 | 12 | M45 / AUDIT | Operational reports and analytics: mutation evidence |
| INV-693 | 12 | M45 / EVENTS | Operational reports and analytics: versioned domain events |
| INV-694 | 12 | M45 / PRIVACY | Operational reports and analytics: data classification and retention |
| INV-695 | 12 | M45 / INTEGRATION | Operational reports and analytics: dependency integration |
| INV-698 | 12 | M46 / DATA | External APIs, imports and webhooks: schema and migrations |
| INV-699 | 12 | M46 / API | External APIs, imports and webhooks: request and response contracts |
| INV-700 | 12 | M46 / AUTHZ | External APIs, imports and webhooks: enforce access boundaries |
| INV-701 | 12 | M46 / LIFE | Public API contracts |
| INV-702 | 12 | M46 / LIFE | Signed webhooks |
| INV-703 | 12 | M46 / LIFE | Versioned imports |
| INV-704 | 12 | M46 / LIFE | Connector boundary |
| INV-707 | 12 | M46 / NOTIFY | External APIs, imports and webhooks: actionable notifications |
| INV-708 | 12 | M46 / ADMIN | External APIs, imports and webhooks: administrative review controls |
| INV-709 | 12 | M46 / AUDIT | External APIs, imports and webhooks: mutation evidence |
| INV-710 | 12 | M46 / EVENTS | External APIs, imports and webhooks: versioned domain events |
| INV-711 | 12 | M46 / PRIVACY | External APIs, imports and webhooks: data classification and retention |
| INV-712 | 12 | M46 / INTEGRATION | External APIs, imports and webhooks: dependency integration |
| INV-715 | 12 | M47 / DATA | Customer migration and onboarding: schema and migrations |
| INV-716 | 12 | M47 / API | Customer migration and onboarding: request and response contracts |
| INV-717 | 12 | M47 / AUTHZ | Customer migration and onboarding: enforce access boundaries |
| INV-718 | 12 | M47 / LIFE | Mapping and rehearsal |
| INV-719 | 12 | M47 / LIFE | Cutover controls |
| INV-720 | 12 | M47 / LIFE | Rollback boundary |
| INV-723 | 12 | M47 / NOTIFY | Customer migration and onboarding: actionable notifications |
| INV-724 | 12 | M47 / ADMIN | Customer migration and onboarding: administrative review controls |
| INV-725 | 12 | M47 / AUDIT | Customer migration and onboarding: mutation evidence |
| INV-726 | 12 | M47 / EVENTS | Customer migration and onboarding: versioned domain events |
| INV-727 | 12 | M47 / PRIVACY | Customer migration and onboarding: data classification and retention |
| INV-728 | 12 | M47 / INTEGRATION | Customer migration and onboarding: dependency integration |
| INV-731 | 13 | M48 / DATA | SaaS support and customer lifecycle: schema and migrations |
| INV-732 | 13 | M48 / API | SaaS support and customer lifecycle: request and response contracts |
| INV-733 | 13 | M48 / AUTHZ | SaaS support and customer lifecycle: enforce access boundaries |
| INV-734 | 13 | M48 / LIFE | Support runbooks |
| INV-735 | 13 | M48 / LIFE | Tenant portability |
| INV-736 | 13 | M48 / LIFE | Offboarding and holds |
| INV-739 | 13 | M48 / NOTIFY | SaaS support and customer lifecycle: actionable notifications |
| INV-740 | 13 | M48 / ADMIN | SaaS support and customer lifecycle: administrative review controls |
| INV-741 | 13 | M48 / AUDIT | SaaS support and customer lifecycle: mutation evidence |
| INV-742 | 13 | M48 / EVENTS | SaaS support and customer lifecycle: versioned domain events |
| INV-743 | 13 | M48 / PRIVACY | SaaS support and customer lifecycle: data classification and retention |
| INV-744 | 13 | M48 / INTEGRATION | SaaS support and customer lifecycle: dependency integration |
| INV-747 | 13 | M49 / DATA | Security, privacy and localization release: schema and migrations |
| INV-748 | 13 | M49 / API | Security, privacy and localization release: request and response contracts |
| INV-749 | 13 | M49 / AUTHZ | Security, privacy and localization release: enforce access boundaries |
| INV-750 | 13 | M49 / LIFE | Isolation assessment |
| INV-751 | 13 | M49 / LIFE | Privacy rights and retention |
| INV-752 | 13 | M49 / LIFE | Launch security |
| INV-755 | 13 | M49 / NOTIFY | Security, privacy and localization release: actionable notifications |
| INV-756 | 13 | M49 / ADMIN | Security, privacy and localization release: administrative review controls |
| INV-757 | 13 | M49 / AUDIT | Security, privacy and localization release: mutation evidence |
| INV-758 | 13 | M49 / EVENTS | Security, privacy and localization release: versioned domain events |
| INV-759 | 13 | M49 / PRIVACY | Security, privacy and localization release: data classification and retention |
| INV-760 | 13 | M49 / INTEGRATION | Security, privacy and localization release: dependency integration |
| INV-763 | 13 | M50 / DATA | Reliability, recovery and performance: schema and migrations |
| INV-764 | 13 | M50 / API | Reliability, recovery and performance: request and response contracts |
| INV-765 | 13 | M50 / AUTHZ | Reliability, recovery and performance: enforce access boundaries |
| INV-766 | 13 | M50 / LIFE | Observability |
| INV-767 | 13 | M50 / LIFE | Backup and recovery |
| INV-768 | 13 | M50 / LIFE | Performance budgets |
| INV-769 | 13 | M50 / LIFE | Safe deployment |
| INV-772 | 13 | M50 / NOTIFY | Reliability, recovery and performance: actionable notifications |
| INV-773 | 13 | M50 / ADMIN | Reliability, recovery and performance: administrative review controls |
| INV-774 | 13 | M50 / AUDIT | Reliability, recovery and performance: mutation evidence |
| INV-775 | 13 | M50 / EVENTS | Reliability, recovery and performance: versioned domain events |
| INV-776 | 13 | M50 / PRIVACY | Reliability, recovery and performance: data classification and retention |
| INV-777 | 13 | M50 / INTEGRATION | Reliability, recovery and performance: dependency integration |
| INV-780 | 13 | M51 / DATA | Pilot, training and production release: schema and migrations |
| INV-781 | 13 | M51 / AUTHZ | Pilot, training and production release: enforce access boundaries |
| INV-785 | 13 | M51 / AUDIT | Pilot, training and production release: mutation evidence |
| INV-786 | 13 | M51 / EVENTS | Pilot, training and production release: versioned domain events |
| INV-787 | 13 | M51 / PRIVACY | Pilot, training and production release: data classification and retention |
| INV-788 | 13 | M51 / INTEGRATION | Pilot, training and production release: dependency integration |

## design

| Task | Phase | Module / lens | Deliverable |
| --- | --- | --- | --- |
| INV-021 | 2 | M03 / DESIGN | Tenants and SaaS entitlements: screen design |
| INV-037 | 2 | M04 / DESIGN | Identity, invitations and devices: screen design |
| INV-053 | 2 | M05 / DESIGN | Scoped roles and permissions: screen design |
| INV-069 | 2 | M06 / DESIGN | Approval policies and decisions: screen design |
| INV-085 | 2 | M07 / DESIGN | Audit and business events: screen design |
| INV-101 | 2 | M08 / DESIGN | Jobs, idempotency and delivery: screen design |
| INV-116 | 2 | M09 / DESIGN | Attachments and collaboration: screen design |
| INV-131 | 2 | M10 / DESIGN | Notifications and preferences: screen design |
| INV-153 | 3 | M12 / DESIGN | Office and admin application shells: screen design |
| INV-169 | 3 | M13 / DESIGN | Android foundation and sync protocol: screen design |
| INV-186 | 4 | M14 / DESIGN | Companies, branches and regional settings: screen design |
| INV-202 | 4 | M15 / DESIGN | Suppliers and customers: screen design |
| INV-219 | 4 | M16 / DESIGN | Products, variants and packaging: screen design |
| INV-235 | 4 | M17 / DESIGN | Units and exact arithmetic: screen design |
| INV-251 | 4 | M18 / DESIGN | Warehouses and location hierarchy: screen design |
| INV-267 | 4 | M19 / DESIGN | Lot, serial and ownership identities: screen design |
| INV-284 | 5 | M20 / DESIGN | Immutable stock ledger and projections: screen design |
| INV-300 | 5 | M21 / DESIGN | Reservations and availability: screen design |
| INV-316 | 5 | M22 / DESIGN | Core receipts, issues and opening stock: screen design |
| INV-332 | 5 | M23 / DESIGN | Transfers and in-transit custody: screen design |
| INV-349 | 6 | M24 / DESIGN | Requisitions, RFQs and purchase orders: screen design |
| INV-365 | 6 | M25 / DESIGN | Supplier receiving and inspection handoff: screen design |
| INV-381 | 6 | M26 / DESIGN | Quality inspections and disposition: screen design |
| INV-397 | 7 | M27 / DESIGN | Sales quotations and orders: screen design |
| INV-413 | 7 | M28 / DESIGN | Pick, pack and dispatch: screen design |
| INV-429 | 8 | M29 / DESIGN | Customer and vendor returns: screen design |
| INV-445 | 8 | M30 / DESIGN | Expiry, recalls and scrap: screen design |
| INV-461 | 8 | M31 / DESIGN | Blind counts and reconciliation: screen design |
| INV-477 | 9 | M32 / DESIGN | Routes, putaway and cross-docking: screen design |
| INV-493 | 9 | M33 / DESIGN | Batch and wave picking: screen design |
| INV-509 | 9 | M34 / DESIGN | Replenishment and demand planning: screen design |
| INV-525 | 9 | M35 / DESIGN | Consignment and owner-separated stock: screen design |
| INV-541 | 9 | M36 / DESIGN | Dropship fulfillment: screen design |
| INV-557 | 9 | M37 / DESIGN | Intercompany trade and transfers: screen design |
| INV-573 | 9 | M38 / DESIGN | Kits without manufacturing: screen design |
| INV-589 | 10 | M39 / DESIGN | Offline Android warehouse workflows: screen design |
| INV-606 | 10 | M40 / DESIGN | Scanners, labels and printer interfaces: screen design |
| INV-624 | 11 | M41 / DESIGN | Valuation methods and subledger: screen design |
| INV-640 | 11 | M42 / DESIGN | Landed costs and revaluation: screen design |
| INV-656 | 11 | M43 / DESIGN | Valuation periods and reconciliation: screen design |
| INV-672 | 11 | M44 / DESIGN | Accounting export batches: screen design |
| INV-688 | 12 | M45 / DESIGN | Operational reports and analytics: screen design |
| INV-705 | 12 | M46 / DESIGN | External APIs, imports and webhooks: screen design |
| INV-721 | 12 | M47 / DESIGN | Customer migration and onboarding: screen design |
| INV-737 | 13 | M48 / DESIGN | SaaS support and customer lifecycle: screen design |
| INV-753 | 13 | M49 / DESIGN | Security, privacy and localization release: screen design |
| INV-770 | 13 | M50 / DESIGN | Reliability, recovery and performance: screen design |

## devops

| Task | Phase | Module / lens | Deliverable |
| --- | --- | --- | --- |
| INV-009 | 2 | M02 / LIFE | Reproducible development stack |
| INV-010 | 2 | M02 / LIFE | CI and contract generation |
| INV-011 | 2 | M02 / LIFE | Environment separation |
| INV-013 | 2 | M02 / OPERABILITY | Repository and delivery tooling: runbook and failure signals |
| INV-029 | 2 | M03 / OPERABILITY | Tenants and SaaS entitlements: runbook and failure signals |
| INV-045 | 2 | M04 / OPERABILITY | Identity, invitations and devices: runbook and failure signals |
| INV-061 | 2 | M05 / OPERABILITY | Scoped roles and permissions: runbook and failure signals |
| INV-077 | 2 | M06 / OPERABILITY | Approval policies and decisions: runbook and failure signals |
| INV-093 | 2 | M07 / OPERABILITY | Audit and business events: runbook and failure signals |
| INV-109 | 2 | M08 / OPERABILITY | Jobs, idempotency and delivery: runbook and failure signals |
| INV-124 | 2 | M09 / OPERABILITY | Attachments and collaboration: runbook and failure signals |
| INV-139 | 2 | M10 / OPERABILITY | Notifications and preferences: runbook and failure signals |
| INV-145 | 3 | M11 / OPERABILITY | Design system and accessibility: runbook and failure signals |
| INV-161 | 3 | M12 / OPERABILITY | Office and admin application shells: runbook and failure signals |
| INV-178 | 3 | M13 / OPERABILITY | Android foundation and sync protocol: runbook and failure signals |
| INV-194 | 4 | M14 / OPERABILITY | Companies, branches and regional settings: runbook and failure signals |
| INV-210 | 4 | M15 / OPERABILITY | Suppliers and customers: runbook and failure signals |
| INV-227 | 4 | M16 / OPERABILITY | Products, variants and packaging: runbook and failure signals |
| INV-243 | 4 | M17 / OPERABILITY | Units and exact arithmetic: runbook and failure signals |
| INV-259 | 4 | M18 / OPERABILITY | Warehouses and location hierarchy: runbook and failure signals |
| INV-275 | 4 | M19 / OPERABILITY | Lot, serial and ownership identities: runbook and failure signals |
| INV-292 | 5 | M20 / OPERABILITY | Immutable stock ledger and projections: runbook and failure signals |
| INV-308 | 5 | M21 / OPERABILITY | Reservations and availability: runbook and failure signals |
| INV-324 | 5 | M22 / OPERABILITY | Core receipts, issues and opening stock: runbook and failure signals |
| INV-340 | 5 | M23 / OPERABILITY | Transfers and in-transit custody: runbook and failure signals |
| INV-357 | 6 | M24 / OPERABILITY | Requisitions, RFQs and purchase orders: runbook and failure signals |
| INV-373 | 6 | M25 / OPERABILITY | Supplier receiving and inspection handoff: runbook and failure signals |
| INV-389 | 6 | M26 / OPERABILITY | Quality inspections and disposition: runbook and failure signals |
| INV-405 | 7 | M27 / OPERABILITY | Sales quotations and orders: runbook and failure signals |
| INV-421 | 7 | M28 / OPERABILITY | Pick, pack and dispatch: runbook and failure signals |
| INV-437 | 8 | M29 / OPERABILITY | Customer and vendor returns: runbook and failure signals |
| INV-453 | 8 | M30 / OPERABILITY | Expiry, recalls and scrap: runbook and failure signals |
| INV-469 | 8 | M31 / OPERABILITY | Blind counts and reconciliation: runbook and failure signals |
| INV-485 | 9 | M32 / OPERABILITY | Routes, putaway and cross-docking: runbook and failure signals |
| INV-501 | 9 | M33 / OPERABILITY | Batch and wave picking: runbook and failure signals |
| INV-517 | 9 | M34 / OPERABILITY | Replenishment and demand planning: runbook and failure signals |
| INV-533 | 9 | M35 / OPERABILITY | Consignment and owner-separated stock: runbook and failure signals |
| INV-549 | 9 | M36 / OPERABILITY | Dropship fulfillment: runbook and failure signals |
| INV-565 | 9 | M37 / OPERABILITY | Intercompany trade and transfers: runbook and failure signals |
| INV-581 | 9 | M38 / OPERABILITY | Kits without manufacturing: runbook and failure signals |
| INV-598 | 10 | M39 / OPERABILITY | Offline Android warehouse workflows: runbook and failure signals |
| INV-615 | 10 | M40 / OPERABILITY | Scanners, labels and printer interfaces: runbook and failure signals |
| INV-632 | 11 | M41 / OPERABILITY | Valuation methods and subledger: runbook and failure signals |
| INV-648 | 11 | M42 / OPERABILITY | Landed costs and revaluation: runbook and failure signals |
| INV-664 | 11 | M43 / OPERABILITY | Valuation periods and reconciliation: runbook and failure signals |
| INV-680 | 11 | M44 / OPERABILITY | Accounting export batches: runbook and failure signals |
| INV-696 | 12 | M45 / OPERABILITY | Operational reports and analytics: runbook and failure signals |
| INV-713 | 12 | M46 / OPERABILITY | External APIs, imports and webhooks: runbook and failure signals |
| INV-729 | 12 | M47 / OPERABILITY | Customer migration and onboarding: runbook and failure signals |
| INV-745 | 13 | M48 / OPERABILITY | SaaS support and customer lifecycle: runbook and failure signals |
| INV-761 | 13 | M49 / OPERABILITY | Security, privacy and localization release: runbook and failure signals |
| INV-778 | 13 | M50 / OPERABILITY | Reliability, recovery and performance: runbook and failure signals |
| INV-789 | 13 | M51 / OPERABILITY | Pilot, training and production release: runbook and failure signals |

## frontend

| Task | Phase | Module / lens | Deliverable |
| --- | --- | --- | --- |
| INV-022 | 2 | M03 / BUILD | Tenants and SaaS entitlements: accessible user workflows |
| INV-038 | 2 | M04 / BUILD | Identity, invitations and devices: accessible user workflows |
| INV-054 | 2 | M05 / BUILD | Scoped roles and permissions: accessible user workflows |
| INV-070 | 2 | M06 / BUILD | Approval policies and decisions: accessible user workflows |
| INV-086 | 2 | M07 / BUILD | Audit and business events: accessible user workflows |
| INV-102 | 2 | M08 / BUILD | Jobs, idempotency and delivery: accessible user workflows |
| INV-117 | 2 | M09 / BUILD | Attachments and collaboration: accessible user workflows |
| INV-132 | 2 | M10 / BUILD | Notifications and preferences: accessible user workflows |
| INV-142 | 3 | M11 / LIFE | Accessible visual system |
| INV-143 | 3 | M11 / LIFE | Screen state contracts |
| INV-154 | 3 | M12 / BUILD | Office and admin application shells: accessible user workflows |
| INV-187 | 4 | M14 / BUILD | Companies, branches and regional settings: accessible user workflows |
| INV-203 | 4 | M15 / BUILD | Suppliers and customers: accessible user workflows |
| INV-220 | 4 | M16 / BUILD | Products, variants and packaging: accessible user workflows |
| INV-236 | 4 | M17 / BUILD | Units and exact arithmetic: accessible user workflows |
| INV-252 | 4 | M18 / BUILD | Warehouses and location hierarchy: accessible user workflows |
| INV-268 | 4 | M19 / BUILD | Lot, serial and ownership identities: accessible user workflows |
| INV-285 | 5 | M20 / BUILD | Immutable stock ledger and projections: accessible user workflows |
| INV-301 | 5 | M21 / BUILD | Reservations and availability: accessible user workflows |
| INV-317 | 5 | M22 / BUILD | Core receipts, issues and opening stock: accessible user workflows |
| INV-333 | 5 | M23 / BUILD | Transfers and in-transit custody: accessible user workflows |
| INV-350 | 6 | M24 / BUILD | Requisitions, RFQs and purchase orders: accessible user workflows |
| INV-366 | 6 | M25 / BUILD | Supplier receiving and inspection handoff: accessible user workflows |
| INV-382 | 6 | M26 / BUILD | Quality inspections and disposition: accessible user workflows |
| INV-398 | 7 | M27 / BUILD | Sales quotations and orders: accessible user workflows |
| INV-414 | 7 | M28 / BUILD | Pick, pack and dispatch: accessible user workflows |
| INV-430 | 8 | M29 / BUILD | Customer and vendor returns: accessible user workflows |
| INV-446 | 8 | M30 / BUILD | Expiry, recalls and scrap: accessible user workflows |
| INV-462 | 8 | M31 / BUILD | Blind counts and reconciliation: accessible user workflows |
| INV-478 | 9 | M32 / BUILD | Routes, putaway and cross-docking: accessible user workflows |
| INV-494 | 9 | M33 / BUILD | Batch and wave picking: accessible user workflows |
| INV-510 | 9 | M34 / BUILD | Replenishment and demand planning: accessible user workflows |
| INV-526 | 9 | M35 / BUILD | Consignment and owner-separated stock: accessible user workflows |
| INV-542 | 9 | M36 / BUILD | Dropship fulfillment: accessible user workflows |
| INV-558 | 9 | M37 / BUILD | Intercompany trade and transfers: accessible user workflows |
| INV-574 | 9 | M38 / BUILD | Kits without manufacturing: accessible user workflows |
| INV-625 | 11 | M41 / BUILD | Valuation methods and subledger: accessible user workflows |
| INV-641 | 11 | M42 / BUILD | Landed costs and revaluation: accessible user workflows |
| INV-657 | 11 | M43 / BUILD | Valuation periods and reconciliation: accessible user workflows |
| INV-673 | 11 | M44 / BUILD | Accounting export batches: accessible user workflows |
| INV-689 | 12 | M45 / BUILD | Operational reports and analytics: accessible user workflows |
| INV-706 | 12 | M46 / BUILD | External APIs, imports and webhooks: accessible user workflows |
| INV-722 | 12 | M47 / BUILD | Customer migration and onboarding: accessible user workflows |
| INV-738 | 13 | M48 / BUILD | SaaS support and customer lifecycle: accessible user workflows |
| INV-754 | 13 | M49 / BUILD | Security, privacy and localization release: accessible user workflows |
| INV-771 | 13 | M50 / BUILD | Reliability, recovery and performance: accessible user workflows |

## mobile

| Task | Phase | Module / lens | Deliverable |
| --- | --- | --- | --- |
| INV-170 | 3 | M13 / BUILD | Android foundation and sync protocol: accessible user workflows |
| INV-590 | 10 | M39 / BUILD | Offline Android warehouse workflows: accessible user workflows |
| INV-607 | 10 | M40 / BUILD | Scanners, labels and printer interfaces: accessible user workflows |

## ops

| Task | Phase | Module / lens | Deliverable |
| --- | --- | --- | --- |
| INV-001 | 1 | M01 / AUTHZ | Product baseline and localization: enforce access boundaries |
| INV-002 | 1 | M01 / LIFE | Research baseline |
| INV-003 | 1 | M01 / LIFE | Ethiopia localization review |
| INV-004 | 1 | M01 / LIFE | Dependency and version decisions |
| INV-005 | 1 | M01 / INTEGRATION | Product baseline and localization: dependency integration |
| INV-006 | 1 | M01 / OPERABILITY | Product baseline and localization: runbook and failure signals |
| INV-782 | 13 | M51 / LIFE | Pilot scenario coverage |
| INV-783 | 13 | M51 / LIFE | Training and support |
| INV-784 | 13 | M51 / LIFE | Production go-live |

## qa

| Task | Phase | Module / lens | Deliverable |
| --- | --- | --- | --- |
| INV-007 | 1 | M01 / QA | Product baseline and localization: acceptance and invariants |
| INV-014 | 2 | M02 / QA | Repository and delivery tooling: acceptance and invariants |
| INV-030 | 2 | M03 / QA | Tenants and SaaS entitlements: acceptance and invariants |
| INV-046 | 2 | M04 / QA | Identity, invitations and devices: acceptance and invariants |
| INV-062 | 2 | M05 / QA | Scoped roles and permissions: acceptance and invariants |
| INV-078 | 2 | M06 / QA | Approval policies and decisions: acceptance and invariants |
| INV-094 | 2 | M07 / QA | Audit and business events: acceptance and invariants |
| INV-110 | 2 | M08 / QA | Jobs, idempotency and delivery: acceptance and invariants |
| INV-125 | 2 | M09 / QA | Attachments and collaboration: acceptance and invariants |
| INV-140 | 2 | M10 / QA | Notifications and preferences: acceptance and invariants |
| INV-146 | 3 | M11 / QA | Design system and accessibility: acceptance and invariants |
| INV-162 | 3 | M12 / QA | Office and admin application shells: acceptance and invariants |
| INV-179 | 3 | M13 / QA | Android foundation and sync protocol: acceptance and invariants |
| INV-195 | 4 | M14 / QA | Companies, branches and regional settings: acceptance and invariants |
| INV-211 | 4 | M15 / QA | Suppliers and customers: acceptance and invariants |
| INV-228 | 4 | M16 / QA | Products, variants and packaging: acceptance and invariants |
| INV-244 | 4 | M17 / QA | Units and exact arithmetic: acceptance and invariants |
| INV-260 | 4 | M18 / QA | Warehouses and location hierarchy: acceptance and invariants |
| INV-276 | 4 | M19 / QA | Lot, serial and ownership identities: acceptance and invariants |
| INV-293 | 5 | M20 / QA | Immutable stock ledger and projections: acceptance and invariants |
| INV-309 | 5 | M21 / QA | Reservations and availability: acceptance and invariants |
| INV-325 | 5 | M22 / QA | Core receipts, issues and opening stock: acceptance and invariants |
| INV-341 | 5 | M23 / QA | Transfers and in-transit custody: acceptance and invariants |
| INV-358 | 6 | M24 / QA | Requisitions, RFQs and purchase orders: acceptance and invariants |
| INV-374 | 6 | M25 / QA | Supplier receiving and inspection handoff: acceptance and invariants |
| INV-390 | 6 | M26 / QA | Quality inspections and disposition: acceptance and invariants |
| INV-406 | 7 | M27 / QA | Sales quotations and orders: acceptance and invariants |
| INV-422 | 7 | M28 / QA | Pick, pack and dispatch: acceptance and invariants |
| INV-438 | 8 | M29 / QA | Customer and vendor returns: acceptance and invariants |
| INV-454 | 8 | M30 / QA | Expiry, recalls and scrap: acceptance and invariants |
| INV-470 | 8 | M31 / QA | Blind counts and reconciliation: acceptance and invariants |
| INV-486 | 9 | M32 / QA | Routes, putaway and cross-docking: acceptance and invariants |
| INV-502 | 9 | M33 / QA | Batch and wave picking: acceptance and invariants |
| INV-518 | 9 | M34 / QA | Replenishment and demand planning: acceptance and invariants |
| INV-534 | 9 | M35 / QA | Consignment and owner-separated stock: acceptance and invariants |
| INV-550 | 9 | M36 / QA | Dropship fulfillment: acceptance and invariants |
| INV-566 | 9 | M37 / QA | Intercompany trade and transfers: acceptance and invariants |
| INV-582 | 9 | M38 / QA | Kits without manufacturing: acceptance and invariants |
| INV-599 | 10 | M39 / QA | Offline Android warehouse workflows: acceptance and invariants |
| INV-616 | 10 | M40 / QA | Scanners, labels and printer interfaces: acceptance and invariants |
| INV-633 | 11 | M41 / QA | Valuation methods and subledger: acceptance and invariants |
| INV-649 | 11 | M42 / QA | Landed costs and revaluation: acceptance and invariants |
| INV-665 | 11 | M43 / QA | Valuation periods and reconciliation: acceptance and invariants |
| INV-681 | 11 | M44 / QA | Accounting export batches: acceptance and invariants |
| INV-697 | 12 | M45 / QA | Operational reports and analytics: acceptance and invariants |
| INV-714 | 12 | M46 / QA | External APIs, imports and webhooks: acceptance and invariants |
| INV-730 | 12 | M47 / QA | Customer migration and onboarding: acceptance and invariants |
| INV-746 | 13 | M48 / QA | SaaS support and customer lifecycle: acceptance and invariants |
| INV-762 | 13 | M49 / QA | Security, privacy and localization release: acceptance and invariants |
| INV-779 | 13 | M50 / QA | Reliability, recovery and performance: acceptance and invariants |
| INV-790 | 13 | M51 / QA | Pilot, training and production release: acceptance and invariants |
