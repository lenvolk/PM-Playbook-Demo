# How to link this playbook to Azure DevOps (ADO)

This repo is the knowledge hub; ADO is the system of record for requirements.

## The linking contract (recommended)

### In GitHub docs (PRDs, decisions, notes)
Include a small **Traceability** section:

**Traceability**
- ADO work items: <paste links>
- Area path: <optional>
- Iteration: <optional>
- Owner: <name>
- Last updated: YYYY-MM-DD

### In ADO work items
Add a line in the Description (or a custom field if you have one):

**GitHub context:** <link to the relevant PRD / decision record / checklist>

## Why this matters
- Makes context discoverable from the work item.
- Prevents duplicating long narrative requirements in two places.
- Preserves decision history with review/comment audit trail in GitHub.
