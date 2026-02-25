---
name: push-protection-demo
description: Interactive 2-3 minute demo of GitHub Push Protection. Shows how secrets are detected and blocked in real-time. Use when asked to demo push protection, secret scanning, GitHub security features, or run the security demo. Requires GitHub MCP, Playwright MCP, and Context7 MCP.
---

# GitHub Push Protection Demo Skill

An engaging, fast-paced demo that shows GitHub's Push Protection blocking secrets in real-time.

## Prerequisites

**Required MCP Servers:**
- `mcp_github-remote` - For pushing files and triggering push protection
- Playwright MCP (`browser_*`) - For showing the browser experience
- Context7 MCP (`mcp_io_github_ups`) - For documentation lookups if needed

## Demo Flow (2-3 minutes)

This demo has **dramatic tension**: we're going to deliberately try to leak a secret, and watch GitHub stop us.

### Pacing Guidelines

- **Narrate briefly** - One sentence max per step
- **Let the browser speak** - Screenshots > explanations  
- **Build to the climax** - The push block is the "wow" moment
- **End clean** - Delete the token, close browser

### Step-by-Step Execution

#### ACT 1: Setup (30 seconds)

**Step 1: Open the Stage**
```
browser_navigate → https://github.com/{owner}/{repo}/settings/security_analysis
browser_take_screenshot
```
Narration: "Let's verify Push Protection is armed and ready."

Point out: Secret Protection ✅, Push Protection ✅

#### ACT 2: The Weapon (45 seconds)

**Step 2: Create the Secret**
```
browser_navigate → https://github.com/settings/tokens/new
browser_type → Note: "push-protection-test"
browser_click → "Generate token"
browser_take_screenshot
```
Narration: "Creating a real GitHub token—no permissions, but GitHub doesn't know that yet."

**IMPORTANT:** Copy the token value (format: `ghp_...`)

#### ACT 3: The Attempt (30 seconds)

**Step 3: Try to Push the Secret**
```
mcp_github-remote_push_files:
  - owner: {owner}
  - repo: {repo}  
  - branch: security
  - files: [{"path": "test-secret.txt", "content": "GITHUB_TOKEN={token}"}]
  - message: "Add configuration"
```

**Expected result:** BLOCKED! The push will fail with:
```
Secret Scanning has rejected the input...
Found high confidence secret of type 'GitHub Personal Access Token'
Bypass URL: https://github.com/{owner}/{repo}/security/secret-scanning/unblock-secret/...
```

Narration: "And there it is—GitHub caught us red-handed!"

#### ACT 4: The Evidence (30 seconds)

**Step 4: Show the Bypass Page**
```
browser_navigate → {bypass_url_from_error}
browser_take_screenshot
```

The page shows:
- "Push blocked because a secret was detected"
- Risk warnings (what an attacker could do)
- Bypass options (tests / false positive / fix later)

Narration: "This is what developers see. Three choices—none of them 'just push anyway'."

#### ACT 5: Cleanup (15 seconds)

**Step 5: Delete the Evidence**
```
browser_navigate → https://github.com/settings/tokens
browser_click → Delete (for push-protection-test)
browser_click → "I understand, delete this token"
browser_close
```

Narration: "Token deleted. No secrets were harmed in this demo."

### Demo Summary Table

At the end, show this in chat:

| Step | What Happened |
|------|---------------|
| ✅ Verified | Push Protection enabled |
| 🔑 Created | Test token (no permissions) |
| 🚫 Blocked | GitHub detected real PAT |
| 🔗 Shown | Bypass page with options |
| 🗑️ Cleaned | Token deleted |

**Key takeaway:** GitHub validates secrets are REAL before blocking—fake tokens pass through, real ones get caught.

## Error Handling

**If token page requires authentication:**
- Pause and say "GitHub wants to verify it's you—please authenticate"
- Wait for user to complete passkey/password

**If push succeeds (shouldn't happen):**
- Check if Push Protection is actually enabled
- The token may have already been revoked

**If browser isn't available:**
- Fall back to GitHub MCP only
- Skip screenshots, narrate the results instead

## Demo Personality

- Be **confident** but not condescending
- Use **action verbs**: "Let's verify", "Watch this", "And there it is"
- Build **suspense** before the push attempt
- Show **satisfaction** when it blocks
- Keep it **professional** but engaging

---

## DRY RUN MODE

Use dry run mode when you want to show the **Secret Scanning Alerts** instead of the push block. In this mode, the secret actually gets pushed and appears in the Security tab.

**Trigger phrases:** "dry run", "show alerts", "let the secret through"

### Dry Run Flow (2-3 minutes)

#### ACT 1: Disable the Shield (30 seconds)

**Step 1: Turn Off Push Protection**
```
browser_navigate → https://github.com/{owner}/{repo}/settings/security_analysis
browser_click → "Disable" button under Push Protection
browser_take_screenshot
```
Narration: "Temporarily lowering our shields for this demo."

> ⚠️ **IMPORTANT:** We're only disabling Push Protection, NOT Secret Protection. Secret Scanning will still detect the token AFTER it's pushed.

#### ACT 2: Create the Secret (45 seconds)

Same as Block Mode - create a test token with no permissions.

#### ACT 3: Push the Secret (30 seconds)

**Step 3: Push Successfully**
```
mcp_github-remote_push_files:
  - owner: {owner}
  - repo: {repo}  
  - branch: security
  - files: [{"path": "test-secret.txt", "content": "GITHUB_TOKEN={token}"}]
  - message: "Add configuration"
```

**Expected result:** Push succeeds! (No protection = no block)

Narration: "The push went through. But watch what happens next..."

#### ACT 4: Show the Alert (45 seconds)

**Step 4: Navigate to Security Alerts**
```
browser_navigate → https://github.com/{owner}/{repo}/security/secret-scanning
browser_take_screenshot
```

You'll see:
- **Secret scanning alert** for the GitHub Personal Access Token
- Token status (may already be auto-revoked by GitHub!)
- Location: `test-secret.txt` on `security` branch
- Remediation options

Narration: "GitHub found it anyway—and look, they've already revoked it!"

#### ACT 5: Cleanup (30 seconds)

**Step 5a: Delete the file with secret**
```
mcp_github-remote_push_files:
  - owner: {owner}
  - repo: {repo}  
  - branch: security
  - files: [{"path": "test-secret.txt", "content": ""}]  # or delete
  - message: "Remove test secret"
```

**Step 5b: Re-enable Push Protection**
```
browser_navigate → https://github.com/{owner}/{repo}/settings/security_analysis
browser_click → "Enable" under Push Protection
browser_take_screenshot
```

**Step 5c: Delete the test token**
```
browser_navigate → https://github.com/settings/tokens
browser_click → Delete (for push-protection-test)
browser_close
```

Narration: "Shields back up. Secret removed. Token deleted. All clean."

### Dry Run Summary Table

| Step | What Happened |
|------|---------------|
| 🔓 Disabled | Push Protection (temporarily) |
| 🔑 Created | Test token (no permissions) |
| ✅ Pushed | Secret went through |
| 🚨 Detected | Secret Scanning found it |
| 🔒 Re-enabled | Push Protection |
| 🗑️ Cleaned | File + token deleted |

**Key takeaway:** Even without Push Protection, Secret Scanning STILL detects secrets after they're committed—and GitHub auto-revokes known tokens!
