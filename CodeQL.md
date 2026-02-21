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

## Test Results ✅

**CodeQL successfully detected 25 security vulnerabilities!**

### By Severity:
| Severity | Count | Examples |
|----------|-------|----------|
| **Critical** | 7 | Command injection, SSRF, SSTI, Deserialization, LDAP injection |
| **High** | 14 | SQL injection, XSS, Path traversal, Weak crypto, Debug mode |
| **Medium** | 4 | Server-side XSS, URL redirection |

### Sample Alerts Detected:
- **Server-side request forgery** (Critical) - vulnerable-demo.js:160
- **Uncontrolled command line** (Critical) - vulnerable-demo.py:43,56 & vulnerable-demo.js:47
- **Server Side Template Injection** (Critical) - vulnerable-demo.py:70
- **Deserialization of user-controlled data** (Critical) - vulnerable-demo.py:115
- **SQL query built from user-controlled sources** (High) - vulnerable-demo.py:29
- **Reflected cross-site scripting** (High) - vulnerable-demo.js:60
- **Flask app is run in debug mode** (High) - vulnerable-demo.py:195
- **Use of weak cryptographic hashing (MD5)** (High) - vulnerable-demo.py:156

### How to View Alerts:
1. Go to **Security** → **Code scanning alerts**
2. Change filter from `branch:main` to `branch:security`
3. See all 25 detected vulnerabilities

## Important Note

⚠️ The default CodeQL setup was disabled to allow our custom workflow. The workflow uses **advanced configuration** via `.github/workflows/codeql.yml`.

## Clean Up

After testing, delete the vulnerable demo files - they are for demonstration only.

---
*Tested: February 20, 2026*  
*Last Updated: February 20, 2026 - CodeQL alerts confirmed working!*
