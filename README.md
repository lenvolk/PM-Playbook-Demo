# Copilot PM Workflow Agents (Retail Marketplace Expansion)

This folder contains **workflow-specific Copilot agent instruction files** for PMs working on a **retail marketplace** with a primary goal of **expansion**, delivered via **weekly sprints with user stories**.

## How to use
In GitHub Copilot Chat, start a session and explicitly reference the agent you want. For example:

- "Use `.github/agents/expansion-metrics-kpi-architect.md` and build a metric tree for orders per buyer."
- "Follow `.github/agents/sprint-story-execution-orchestrator.md` and convert this initiative into sprint-ready stories."

## Available agents
- `expansion-metrics-kpi-architect.md`
- `category-assortment-strategist.md`
- `seller-activation-expansion-coach.md`
- `liquidity-matchmaking-diagnostician.md`
- `trust-safety-quality-guardian.md`
- `promotions-fees-unit-economics-modeler.md`
- `discovery-search-personalization-pm.md`
- `sprint-story-execution-orchestrator.md`

## Conventions across all agents
Each agent:
- Starts by asking a small set of **clarifying questions**.
- Produces outputs with **explicit metric definitions**, **segmentation**, and **guardrails**.
- Avoids "GMV at all costs" by including **trust** and **unit economics** checks.
- Produces **sprint-ready artifacts** whenever possible (epics, user stories, acceptance criteria, instrumentation).

## Escalation guidance
If any workflow touches:
- Legal/policy interpretation (refund laws, consumer protection, tax, AML, etc.)
- Active fraud or safety incidents
- Material pricing/fee changes

…the agent should propose options and questions, but recommend human review/approval.



## 🎥 Video

- **YouTube**
  https://www.youtube.com/watch?v=TOAAKp9NYDw

> Reference video related to AI, Copilot workflows, and product thinking.

---

## 🧩 Custom Prompts

- **Awesome GitHub Copilot – Project Planning Collection**
  https://github.com/github/awesome-copilot/blob/main/collections/project-planning.md

> A curated set of prompt ideas and patterns focused on project and product planning using GitHub Copilot.

---

## 🧠 Product Brain Repository

- **Product Brain (digitarald)**
  https://github.com/digitarald/product-brain

> An open-source approach for capturing product strategy, decisions, constraints, and context in a structured repository.

---
