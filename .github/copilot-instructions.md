# Copilot Instructions for pm-playbook

## Repository Purpose

This is a **PM Playbook** repository — a demonstration and reference site for how Project Managers and Scrum Masters integrate GitHub security tools (CodeQL, Dependabot, Secret Scanning) into agile workflows. It contains:

- A static marketing/demo website (`website/`) built with vanilla HTML, CSS, and JS
- Intentionally vulnerable demo files (`website/vulnerable-demo.js`, `website/vulnerable-demo.py`) used to trigger CodeQL alerts — **do not "fix" these vulnerabilities**
- Copilot agent definitions (`.github/agents/`) for PM/product management advisory personas
- Copilot skills (`.github/skills/`) for various specialized capabilities

## Architecture

- **`website/`** — Static site (no build step, no bundler). Plain HTML + CSS + inline `<script>`. Open `index.html` directly in a browser to preview.
- **`website/vulnerable-demo.js`** and **`website/vulnerable-demo.py`** — Express/Flask apps with intentional security vulnerabilities (SQL injection, XSS, command injection, etc.) for CodeQL scanning demos. These files exist solely to generate CodeQL alerts and must remain vulnerable.
- **`.github/workflows/codeql.yml`** — Runs CodeQL analysis on `main` and `security` branches for JavaScript/TypeScript and Python using the `security-extended` query suite.
- **`.github/agents/`** — Markdown-based Copilot agent definitions for PM advisory roles (sprint planning, trust & safety, seller activation, etc.).

## Key Conventions

- **Never fix vulnerabilities in `vulnerable-demo.*` files.** They are intentional test cases for CodeQL. Adding new vulnerability examples should follow the existing pattern: numbered section header, CodeQL rule ID in comment, clearly marked `VULNERABLE` inline comment.
- **No build system.** The website is plain static files — no npm, no pip, no bundler. Do not introduce a build step.
- **Agent files** in `.github/agents/` follow a structured markdown format with mission statement, step-by-step guidance, templates, and escalation criteria.

## CI/CD

CodeQL runs automatically on pushes to `main` and `security` branches, on PRs to `main`, and weekly on Mondays at 6 AM UTC. It scans both `javascript-typescript` and `python` languages.
