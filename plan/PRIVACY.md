# Privacy and data lifecycle

Personal data includes users, invitations, partner contacts, addresses, comments, attachments, support evidence, device identifiers and audit actor metadata. Each persistent module has a field-classification and exporter/deleter task, including modules that contain only actor references. Do not declare a module PII-free merely because its primary data is stock.

Registry of handlers must support authorized subject export, tenant portability, correction and approved anonymization/deletion. An export cannot expose another tenant's records. Posted transaction evidence must not cascade-delete with users or partners. Separate legal/business retention purposes from application convenience.

At onboarding, select an approved retention profile. Local legal review determines required durations and holds; this plan deliberately does not invent statutory periods. Operational defaults that are not legal retention: transient sync changes 30 days, draft command receipt 30 days, report download links at most 15 minutes and generated report objects seven days unless held. Immutable business command IDs remain with retained transaction history.

Offboarding: verify requester → produce reconciled export → review holds → revoke access → delete/anonymize live personal data under schedule → record object-store and backup expiry → provide evidence. Backups are encrypted with restricted access and a finite documented expiry; deletion completion must distinguish live removal from backup expiration.

Before pilot, document controller/processor roles, notices, lawful processing rationale, subprocessors, incident response, hosting region and cross-border transfer applicability. Required evidence is assigned to M01/M49. No compliance certification is asserted by this package.
