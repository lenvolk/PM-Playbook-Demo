# Compliance (PM checklist)

Use this page to ensure your requirements consider common compliance dimensions. This is **starting guidance** and should evolve as your org formalizes policies.

## What PMs should capture
- **Data classification:** What data is collected/processed/stored?
- **PII/PHI:** Does the feature handle personal or sensitive data?
- **Consent & notice:** How are users informed? Is consent required?
- **Data retention & deletion:** How long is data retained? How is deletion handled?
- **Access control:** Who can access the data and how is access audited?
- **Logging & auditability:** What events must be logged for audit/security investigations?
- **Third parties:** Are there integrations that share data externally?
- **Regional requirements:** Are there geo/sovereignty constraints?

## Triggers: when to involve compliance/privacy/security
Involve specialists when any of the following are true:
- Collecting new user data fields
- Processing PII/PHI or sensitive identifiers
- Exporting/sharing data outside the system boundary
- Introducing new telemetry that may identify a user
- Changing retention/deletion behavior
- Adding admin capabilities that increase access

## Evidence / artifacts to link
- Data flow diagram (even a simple box/arrow sketch)
- Data inventory (fields and purpose)
- Retention/deletion plan
- Audit logging plan

## ADO copy/paste block
Use: [Compliance prompts snippet](../../20-templates/ado-snippets/compliance-prompts.md)
