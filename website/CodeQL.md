# CodeQL Testing Guide

## What We're Testing

CodeQL scans code for security vulnerabilities automatically on every push.

## Setup

1. Added `.github/workflows/codeql.yml` - runs on push to main/security branches
2. Added intentionally vulnerable demo files to trigger alerts

## Vulnerable Test Files

| File | Language | Vulnerabilities |
|------|----------|-----------------|
| `vulnerable-demo.js` | JavaScript | SQL injection, XSS, command injection, path traversal, SSRF |
| `vulnerable-demo.py` | Python | SQL injection, XSS, command injection, insecure deserialization, weak crypto |

## How to Test

1. Push code to `main` or `security` branch
2. Go to **Actions** tab → watch "CodeQL Analysis" run (~5-10 min)
3. Go to **Security** → **Code scanning alerts** to see results

## Expected Results

CodeQL should detect and alert on the intentional vulnerabilities in the demo files.

## Clean Up

After testing, delete the vulnerable demo files - they are for demonstration only.

---
*Tested: February 20, 2026*
