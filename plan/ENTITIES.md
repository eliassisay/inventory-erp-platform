# Entity ownership and conceptual schema

> Registry baseline 1.0 · 2026-11-04 · 51 modules · 790 tasks · 156 capabilities · 13 phases. Generated; edit registry.json and run `make plan-render`.

Read DATABASE_SCHEMA.md for common column types, scope constraints, invariants and relationships. Every row below has a migration owner. These are planned entities, not deployed tables.

| Entity | Module | Migration task | Scope | Domain fields |
| --- | --- | --- | --- | --- |
| tenants | M03 | INV-015 | platform | slug, status, region |
| tenant_memberships | M03 | INV-015 | tenant | user_id, tenant_id, status |
| subscriptions | M03 | INV-015 | platform | tenant_id, plan_code, status, valid_until |
| entitlements | M03 | INV-015 | platform | tenant_id, key, limit_value |
| users | M04 | INV-031 | tenant | auth_subject, email, status |
| invitations | M04 | INV-031 | tenant | tenant_id, email, expires_at, accepted_at |
| device_sessions | M04 | INV-031 | tenant | user_id, device_id, revoked_at |
| roles | M05 | INV-047 | tenant | tenant_id, name |
| permissions | M05 | INV-047 | global-reference | code |
| role_permissions | M05 | INV-047 | tenant | role_id, permission_code |
| role_bindings | M05 | INV-047 | tenant | user_id, company_id, warehouse_id, role_id |
| approval_policies | M06 | INV-063 | tenant | module, scope, threshold, version |
| approval_instances | M06 | INV-063 | tenant | entity_id, policy_version, state |
| approval_decisions | M06 | INV-063 | tenant | instance_id, stage, actor_id, decision |
| audit_records | M07 | INV-079 | tenant | actor_id, action, entity_id, request_id, before_hash, after_hash |
| outbox_events | M07 | INV-079 | tenant | event_type, aggregate_id, sequence, payload_version |
| command_receipts | M08 | INV-095 | tenant | idempotency_key, request_hash, result, status |
| job_attempts | M08 | INV-095 | tenant | job_key, attempt, status, next_attempt_at |
| dead_letters | M08 | INV-095 | tenant | job_id, error_code, resolution |
| attachments | M09 | INV-111 | tenant | object_key, sha256, size, scan_state, entity_type, entity_id |
| comments | M09 | INV-111 | tenant | entity_type, entity_id, author_id, body |
| notification_preferences | M10 | INV-126 | tenant | user_id, category, channel |
| notifications | M10 | INV-126 | tenant | recipient_id, event_id, read_at |
| notification_deliveries | M10 | INV-126 | tenant | notification_id, channel, status |
| saved_views | M12 | INV-147 | tenant | user_id, screen_id, filters |
| sync_devices | M13 | INV-163 | tenant | user_id, device_key, last_seen_at |
| sync_cursors | M13 | INV-163 | tenant | device_id, scope_hash, cursor |
| sync_commands | M13 | INV-163 | tenant | device_id, command_id, status |
| companies | M14 | INV-180 | tenant | tenant_id, code, base_currency, time_zone |
| branches | M14 | INV-180 | company | company_id, code, address |
| regional_settings | M14 | INV-180 | company | company_id, locale, quantity_scale, tax_reference |
| partners | M15 | INV-196 | company | company_id, code, name, supplier, customer, status |
| partner_contacts | M15 | INV-196 | company | partner_id, name, email, phone |
| partner_references | M15 | INV-196 | company | partner_id, product_id, external_code, lead_time_days |
| product_templates | M16 | INV-212 | company | company_id, code, name, category_id |
| product_variants | M16 | INV-212 | company | template_id, sku, attributes, tracking_mode |
| product_categories | M16 | INV-212 | company | company_id, parent_id, name |
| product_barcodes | M16 | INV-212 | company | variant_id, code, symbology |
| packaging | M16 | INV-212 | company | variant_id, uom_id, quantity |
| uom_categories | M17 | INV-229 | global-reference | code |
| units | M17 | INV-229 | company | category_id, code, ratio_numerator, ratio_denominator, step |
| currency_definitions | M17 | INV-229 | global-reference | code, minor_digits |
| exchange_rates | M17 | INV-229 | company | company_id, pair, effective_at, rate, source |
| warehouses | M18 | INV-245 | company | company_id, branch_id, code |
| locations | M18 | INV-245 | company | warehouse_id, parent_id, code, type, active |
| location_capacities | M18 | INV-245 | company | location_id, unit, max_quantity |
| lots | M19 | INV-261 | company | company_id, product_id, code, manufactured_on, expires_on |
| serials | M19 | INV-261 | company | company_id, product_id, serial, status |
| stock_owners | M19 | INV-261 | company | company_id, partner_id, kind |
| stock_moves | M20 | INV-277 | company | company_id, product_id, source_id, destination_id, owner_id, lot_id, serial_id, quantity, source_document_id, posted_at, reverses_id |
| stock_buckets | M20 | INV-277 | company | location_id, product_id, owner_id, lot_id, serial_id, on_hand, reserved, version |
| cost_facts | M20 | INV-277 | company | move_id, unit_cost, currency, fx_rate, source |
| reservations | M21 | INV-294 | company | document_line_id, bucket_id, quantity, state, expires_at |
| reservation_allocations | M21 | INV-294 | company | reservation_id, move_id, quantity |
| stock_operations | M22 | INV-310 | company | type, company_id, state, version, business_date |
| stock_operation_lines | M22 | INV-310 | company | operation_id, product_id, planned_qty, done_qty, tracking |
| opening_batches | M22 | INV-310 | company | company_id, cutoff_at, reconciled_at |
| transfers | M23 | INV-326 | company | source_warehouse_id, destination_warehouse_id, state, version |
| transfer_lines | M23 | INV-326 | company | transfer_id, product_id, requested_qty, shipped_qty, received_qty |
| transfer_discrepancies | M23 | INV-326 | company | line_id, quantity, reason, resolution |
| purchase_requisitions | M24 | INV-342 | company | requester_id, state |
| rfqs | M24 | INV-342 | company | supplier_id, currency, state |
| rfq_lines | M24 | INV-342 | company | rfq_id, product_id, quantity, price |
| purchase_orders | M24 | INV-342 | company | supplier_id, agreement_id, state, version |
| purchase_order_lines | M24 | INV-342 | company | order_id, product_id, ordered_qty, received_qty, unit_cost |
| purchase_agreements | M24 | INV-342 | company | supplier_id, valid_from, valid_until, ceiling_qty |
| receipts | M25 | INV-359 | company | purchase_order_id, reference, state |
| receipt_lines | M25 | INV-359 | company | receipt_id, po_line_id, received_qty, accepted_qty, rejected_qty |
| quality_plans | M26 | INV-375 | company | product_category_id, checklist, version |
| inspections | M26 | INV-375 | company | receipt_id, plan_version, state |
| inspection_results | M26 | INV-375 | company | inspection_id, check_id, result, evidence_id |
| quality_dispositions | M26 | INV-375 | company | inspection_id, accepted_qty, rejected_qty, reason |
| price_lists | M27 | INV-391 | company | company_id, currency, valid_from, valid_until |
| price_rules | M27 | INV-391 | company | list_id, product_id, min_qty, unit_price |
| quotations | M27 | INV-391 | company | customer_id, state, version |
| sales_orders | M27 | INV-391 | company | customer_id, currency, state, version |
| sales_order_lines | M27 | INV-391 | company | order_id, product_id, ordered_qty, fulfilled_qty, price |
| pick_tasks | M28 | INV-407 | company | order_id, warehouse_id, state |
| pick_lines | M28 | INV-407 | company | task_id, reservation_id, planned_qty, picked_qty |
| packages | M28 | INV-407 | company | company_id, code, weight |
| package_contents | M28 | INV-407 | company | package_id, product_id, quantity, lot_id, serial_id |
| dispatches | M28 | INV-407 | company | order_id, carrier_reference, state |
| return_authorizations | M29 | INV-423 | company | direction, source_operation_id, reason, state |
| return_lines | M29 | INV-423 | company | return_id, source_move_id, quantity, disposition |
| return_receipts | M29 | INV-423 | company | return_id, operation_id |
| recalls | M30 | INV-439 | company | product_id, lot_id, reason, state |
| recall_targets | M30 | INV-439 | company | recall_id, move_id, partner_id, status |
| scrap_requests | M30 | INV-439 | company | location_id, product_id, quantity, reason, state |
| expiry_policies | M30 | INV-439 | company | product_id, removal_days, alert_days |
| count_sessions | M31 | INV-455 | company | warehouse_id, snapshot_at, state |
| count_lines | M31 | INV-455 | company | session_id, bucket_key, system_qty, counted_qty, recount_qty |
| count_movements | M31 | INV-455 | company | session_id, move_id |
| count_adjustments | M31 | INV-455 | company | line_id, variance, operation_id |
| warehouse_routes | M32 | INV-471 | company | name, version, active |
| route_steps | M32 | INV-471 | company | route_id, sequence, source_type, destination_type, operation_type |
| putaway_rules | M32 | INV-471 | company | category_id, source_location_id, target_location_id, priority |
| picking_waves | M33 | INV-487 | company | warehouse_id, cutoff_at, state |
| wave_tasks | M33 | INV-487 | company | wave_id, pick_task_id, assignee_id |
| pick_batches | M33 | INV-487 | company | wave_id, route_order, state |
| reorder_rules | M34 | INV-503 | company | product_id, warehouse_id, min_qty, max_qty, safety_qty, order_multiple, lead_days |
| replenishment_suggestions | M34 | INV-503 | company | rule_id, forecast_date, quantity, status |
| internal_replenishments | M34 | INV-503 | company | source_id, destination_id, quantity |
| consignment_agreements | M35 | INV-519 | company | partner_id, scope, valid_until |
| ownership_changes | M35 | INV-519 | company | bucket_key, quantity, from_owner_id, to_owner_id, cost_basis, reference |
| dropship_links | M36 | INV-535 | company | sales_line_id, purchase_line_id, quantity |
| dropship_confirmations | M36 | INV-535 | company | link_id, supplier_reference, delivered_qty, confirmed_at |
| intercompany_links | M37 | INV-551 | company | seller_company_id, buyer_company_id, sales_order_id, purchase_order_id, state |
| intercompany_shipments | M37 | INV-551 | company | link_id, seller_move_id, buyer_move_id, reference |
| kit_definitions | M38 | INV-567 | company | product_id, version, active |
| kit_components | M38 | INV-567 | company | kit_id, component_product_id, quantity |
| mobile_assignments | M39 | INV-583 | company | device_id, task_id, scope, lease_until |
| sync_conflicts | M39 | INV-583 | company | command_id, reason, server_version, resolution |
| label_templates | M40 | INV-600 | company | type, version, format |
| print_jobs | M40 | INV-600 | company | template_id, entity_id, printer_id, copies, status |
| scanner_profiles | M40 | INV-600 | company | device_type, symbologies, separator_rules |
| valuation_policies | M41 | INV-617 | company | company_id, category_id, method, effective_from |
| valuation_layers | M41 | INV-617 | company | move_id, quantity, remaining_qty, unit_cost, currency |
| valuation_entries | M41 | INV-617 | company | move_id, layer_id, amount_minor, kind, period_id |
| landed_cost_batches | M42 | INV-634 | company | company_id, currency, state, external_reference |
| landed_cost_lines | M42 | INV-634 | company | batch_id, charge_type, amount_minor |
| landed_cost_allocations | M42 | INV-634 | company | line_id, receipt_move_id, amount_minor |
| revaluations | M42 | INV-634 | company | product_id, amount_minor, reason, state |
| valuation_periods | M43 | INV-650 | company | company_id, start_date, end_date, state |
| valuation_reconciliations | M43 | INV-650 | company | period_id, stock_total, subledger_total, difference |
| period_close_checks | M43 | INV-650 | company | period_id, check_code, result |
| account_mappings | M44 | INV-666 | company | company_id, event_kind, external_account |
| accounting_export_batches | M44 | INV-666 | company | period_id, schema_version, checksum, state |
| accounting_export_lines | M44 | INV-666 | company | batch_id, entry_id, debit_minor, credit_minor |
| export_acknowledgements | M44 | INV-666 | company | batch_id, external_reference, status |
| report_jobs | M45 | INV-682 | company | report_type, scope, as_of, status, object_key |
| dashboard_preferences | M45 | INV-682 | company | user_id, layout, filters |
| api_credentials | M46 | INV-698 | tenant | tenant_id, scopes, expires_at, key_hash |
| webhook_subscriptions | M46 | INV-698 | tenant | tenant_id, url, secret_version, events |
| webhook_deliveries | M46 | INV-698 | tenant | event_id, subscription_id, status |
| import_batches | M46 | INV-698 | company | schema_version, checksum, state |
| import_errors | M46 | INV-698 | company | batch_id, row_number, code |
| migration_runs | M47 | INV-715 | tenant | tenant_id, source, cutoff_at, state |
| migration_mappings | M47 | INV-715 | tenant | run_id, source_key, target_id |
| migration_reconciliations | M47 | INV-715 | tenant | run_id, metric, expected, actual, approved_by |
| support_sessions | M48 | INV-731 | tenant | tenant_id, approved_by, expires_at, scope |
| tenant_exports | M48 | INV-731 | tenant | tenant_id, requested_by, state, expires_at |
| offboarding_requests | M48 | INV-731 | tenant | tenant_id, state, hold_reason |
| usage_counters | M48 | INV-731 | tenant | tenant_id, metric, period, value |
| privacy_requests | M49 | INV-747 | tenant | user_id, kind, state |
| retention_rules | M49 | INV-747 | tenant | record_class, period_days, hold_policy |
| compliance_reviews | M49 | INV-747 | tenant | topic, source_url, reviewer, reviewed_at, result |
| operational_incidents | M50 | INV-763 | tenant | severity, started_at, resolved_at |
| restore_drills | M50 | INV-763 | tenant | backup_reference, started_at, result, rpo_minutes, rto_minutes |
| pilot_acceptances | M51 | INV-780 | tenant | tenant_id, scenario_id, reviewer, result |
| release_evidence | M51 | INV-780 | tenant | version, gate, artifact, approved_by |
