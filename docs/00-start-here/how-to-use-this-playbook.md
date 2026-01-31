# How to use this playbook

This repo is designed to help Product Managers consistently capture context and apply cross-cutting guidance (compliance, accessibility, design, architecture) **while writing requirements in Azure DevOps (ADO)**.

## What belongs here vs. ADO

### Put in GitHub (this repo)
- Org-wide guidance and checklists
- Templates and copy/paste blocks for ADO work items
- Decision records (why we chose something)
- Discovery notes and research summaries
- Reusable examples of good requirements and acceptance criteria

### Put in ADO
- Epics/Features/User Stories and their iteration planning
- Implementation tasks
- Work item state transitions and delivery tracking

## Suggested workflow
1. Start with a **PRD (lite)** in this repo to capture the outcome and context.
2. Copy the relevant **ADO snippets** into your ADO Feature/User Story.
3. Link ADO  GitHub both ways (see [How to link to ADO](how-to-link-to-ado.md)).
4. As decisions are made, add **Decision records** and link them from the PRD and ADO items.
5. When guidance changes, update the checklist **and** the associated ADO snippet.

## How to search
- Use GitHub search with keywords like `PRD`, `decision`, `accessibility`, `compliance`, `telemetry`.
- Keep titles consistent (e.g., `PRD: <initiative>`, `Decision: <topic>`). 
