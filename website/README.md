# GitHub Push Protection Testing Guide

This guide documents how to test GitHub's Secret Scanning Push Protection feature.

## Overview

GitHub Push Protection prevents secrets (API keys, tokens, credentials) from being accidentally committed and pushed to repositories. When enabled, GitHub scans commits during `git push` and blocks the push if secrets are detected.

## Prerequisites

- GitHub repository with admin access
- GitHub Advanced Security enabled (free for public repos, requires license for private repos)

## Step-by-Step Instructions

### Step 1: Enable Secret Scanning and Push Protection

1. Navigate to your repository on GitHub
2. Go to **Settings** → **Code security and analysis** (or **Security** → **Code security**)
3. Enable **Secret scanning**
4. Enable **Push protection** checkbox

![Push Protection Settings](https://docs.github.com/assets/images/help/repository/secret-scanning-push-protection.png)

### Step 2: Create a Test Token

1. Go to **GitHub Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)** or **Fine-grained tokens**
2. Click **Generate new token**
3. Give it a name like "push-protection-test"
4. Select **NO permissions/scopes** (for safety)
5. Generate and copy the token

Example token format:
```
ghp_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

In our test, we used: `ghp_XyFd...RRFc` (40 characters, deleted after testing)

> ⚠️ **Note:** Always delete test tokens immediately after testing. The token used in this test has been revoked.

### Step 3: Add the Secret to a File

Add the token to any file in your repository:

```html
<!-- ghp_YOUR_ACTUAL_TOKEN_HERE -->
```

Or in a config file:
```
GITHUB_TOKEN=ghp_YOUR_ACTUAL_TOKEN_HERE
```

### Step 4: Commit and Push

```bash
git add .
git commit -m "Test push protection"
git push origin <branch-name>
```

### Step 5: Observe the Block

If push protection is working correctly, you'll see an error like this:

```
remote: error: GH013: Repository rule violations found for refs/heads/security.
remote:
remote: - GITHUB PUSH PROTECTION
remote:   ─────────────────────────────────────────────
remote:     Resolve the following violations before pushing again
remote:
remote:     - Push cannot contain secrets
remote:
remote:       ── GitHub Personal Access Token ─────────────────────
remote:        locations:
remote:          - commit: 7d40d8a660e8c553a58ea96edcbd25a22f6b3871
remote:            path: website/index.html:369
remote:
remote:        (?) To push, remove secret from commit(s) or follow this URL to allow the secret.
remote:        https://github.com/<owner>/<repo>/security/secret-scanning/unblock-secret/...
remote:
To https://github.com/<owner>/<repo>.git
 ! [remote rejected] security -> security (push declined due to repository rule violations)
error: failed to push some refs to 'https://github.com/<owner>/<repo>.git'
```

### Step 6: Clean Up

Remove the commit with the secret:

```bash
git reset --hard HEAD~1
```

Then delete the test token from GitHub:
1. Go to **Settings** → **Developer settings** → **Personal access tokens**
2. Find your test token and click **Delete**

## Key Learnings

| Scenario | Result |
|----------|--------|
| Push with real, active token | **BLOCKED** ✅ |
| Push with fake/invalid token | Allowed (not detected) |
| Push with already-revoked token | May be allowed |
| Push your own token (owner) | May need "Block admins" enabled |

## Why Some Tokens Aren't Detected

GitHub validates that tokens are **real and active** before blocking. This prevents false positives:

1. **Fake tokens** that don't pass checksum validation are ignored
2. **Already-revoked tokens** may not trigger blocks
3. **Example tokens** from documentation are usually in an allowlist

## Irony: This README Was Also Blocked! 

When we first tried to commit this README with the actual test token included for documentation purposes, **push protection blocked it too!** This proves the system works even for tokens in documentation files.

We had to obfuscate the token (showing only `ghp_XyFd...RRFc`) to push this guide.

## Supported Secret Types

GitHub detects 200+ secret types including:
- GitHub tokens (PAT, OAuth, App)
- AWS keys
- Azure credentials
- Slack tokens
- Stripe keys
- Database connection strings
- And many more...

See full list: https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns

## Additional Settings

### Block Repository Administrators
To prevent admins from bypassing push protection:
1. Go to **Settings** → **Code security and analysis**
2. Under Push protection, enable **Block pushes from repository administrators**

### Dry Run Mode
To test without blocking:
1. Enable push protection in "Audit mode" first
2. Review alerts before enforcing blocks

## References

- [GitHub Secret Scanning Documentation](https://docs.github.com/en/code-security/secret-scanning)
- [Push Protection Documentation](https://docs.github.com/en/code-security/secret-scanning/push-protection-for-repositories-and-organizations)
- [Working with Push Protection from CLI](https://docs.github.com/en/code-security/secret-scanning/working-with-secret-scanning-and-push-protection/working-with-push-protection-from-the-command-line)

---

*Tested on: February 20, 2026*  
*Repository: PM-Playbook-Demo*  
*Branch: security*
