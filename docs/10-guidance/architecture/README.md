# Architecture (PM checklist)

Use this page to ensure requirements include key system constraints and quality attributes.

## What PMs should capture
- **System boundaries:** what changes vs. what stays the same
- **Dependencies:** services, APIs, identity, data stores
- **Non-functional requirements:** performance, reliability, scale
- **Observability:** what must be measured/logged/alerted
- **Rollout/rollback:** feature flags, safe deployment, migration strategy
- **Security constraints:** authn/authz, threat considerations

## Triggers: when to involve architects/tech leads
- New integration with another system
- New data store or major schema change
- High-scale scenarios or strict latency needs
- Business-critical workflows requiring resiliency guarantees

## Evidence / artifacts to link
- Sequence diagram (happy path + failure modes)
- SLO/SLA proposal
- Dependency list and owners
