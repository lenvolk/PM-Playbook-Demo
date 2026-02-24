# Copilot Instructions for pm-playbook

## Repository Purpose

This is a **Product Manager Playbook** repository focused on GitHub security features education and PM best practices. It contains:

- A static website (`website/`) demonstrating GitHub security tooling (Secret Scanning, Push Protection, CodeQL)
- Copilot agent definitions (`.github/agents/`) for marketplace/e-commerce PM domains
- Copilot skill definitions (`.github/skills/`) covering Azure, .NET, design, MCP, Power BI, and security topics

## Architecture

- **`website/`** — Static HTML/CSS/JS site (no build system or framework). Includes intentionally vulnerable demo files (`vulnerable-demo.js`, `vulnerable-demo.py`) used for CodeQL scanning demos. Do not "fix" these files — they exist to trigger security alerts.
- **`.github/agents/`** — Copilot agent `.md` files for specialized PM advisor roles (e-commerce/marketplace domain). Each file is a standalone agent prompt.
- **`.github/skills/`** — Copilot skill definitions with `SKILL.md` entry points, reference docs, and helper scripts.
- **`.github/workflows/codeql.yml`** — CodeQL analysis for JavaScript/TypeScript and Python on `main` and `security` branches.

## Key Conventions

- **Branches**: `main` is the primary branch. `security` branch is used for security feature testing/demos.
- **CODEOWNERS**: `@lenvolk` owns all files. Guidance subdirectories under `/docs/10-guidance/` have explicit ownership.
- **Agent files**: Use `.agent.md` or plain `.md` extension in `.github/agents/`. Follow the existing pattern of structured prompt engineering with mission, steps, and templates.
- **Issue creation**: Follow the PM advisor pattern — every feature needs a user story with acceptance criteria, required labels (component + size + phase), and definition of done. See `.github/agents/se-product-manager-advisor.agent.md` for the full template.

## CI/CD

- **CodeQL**: Runs on push to `main`/`security`, on PRs to `main`, and weekly (Monday 6 AM). Scans `javascript-typescript` and `python` with `security-extended` query suite.
- No other build, test, or lint pipelines exist. The website has no build step — it's plain HTML/CSS/JS.
