# CodeQL Testing Guide

CodeQL scans code for security vulnerabilities automatically on every push.

## Setup
- Workflow: `.github/workflows/codeql.yml`
- Demo files: `vulnerable-demo.js`, `vulnerable-demo.py`

## Results ✅

**25 vulnerabilities detected:**

| Severity | Count |
|----------|-------|
| Critical | 7 |
| High | 14 |
| Medium | 4 |

**View alerts:** Security → Code scanning → filter `branch:security`

---
*Tested: February 20, 2026*
