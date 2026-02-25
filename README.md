> 📺 **For more training on GitHub security features, reference this YouTube video:** [GitHub Push Protection Training](https://www.youtube.com/watch?v=PHmnkhLZWj0&list=PL8sOwioiPP75hpOrouD0SBkGmu6czVX24&index=37)

# 🛡️ GitHub Push Protection Demo

> **Can GitHub catch a secret before it leaks?** Let's find out.

## The Challenge

You're about to watch GitHub's Push Protection stop a real secret from entering a repository—**in real-time**.

| Demo Details | |
|--------------|---|
| **Duration** | 2-3 minutes |
| **Tools** | GitHub MCP + Playwright MCP |
| **Repository** | [PM-Playbook-Demo](https://github.com/lenvolk/PM-Playbook-Demo) |
| **Branch** | `security` |

---

## 🎬 The Demo (5 Acts)

### ACT 1: Verify the Shield 🛡️
> *"Let's confirm Push Protection is armed."*

Navigate to **Settings → Advanced Security**  
✅ Secret Protection | ✅ Push Protection

### ACT 2: Forge the Weapon 🔑
> *"Creating a real GitHub token..."*

1. Go to **Developer Settings → Personal Access Tokens → Tokens (classic)**
2. Name: `push-protection-test`
3. Permissions: **NONE** (for safety)
4. Generate and copy: `ghp_XXXX...`

### ACT 3: The Attempt 💥
> *"Now watch what happens when we try to push it..."*

```
mcp_github-remote_push_files:
  file: test-secret.txt
  content: "GITHUB_TOKEN=ghp_your_real_token"
```

### ACT 4: THE BLOCK 🚫
> *"And there it is—caught!"*

```
Secret Scanning has rejected the input.
Found: GitHub Personal Access Token
Bypass URL: https://github.com/.../unblock-secret/...
```

Visit the bypass URL to see:
- ⚠️ "Push blocked because a secret was detected"
- Risk warnings (what an attacker could do)
- Bypass options (tests / false positive / fix later)

### ACT 5: Clean Exit 🗑️
> *"Token deleted. No secrets escaped."*

Delete the test token from GitHub Settings.

---

## 💡 The Secret Sauce

| What We Tried | What Happened |
|---------------|---------------|
| Real, active token | **BLOCKED** ✅ |
| Fake/invalid token | Allowed (not detected) |
| Already-revoked token | May be allowed |

**Key insight:** GitHub validates tokens are **REAL** before blocking. Fake tokens pass through—real ones get caught.

---

## 🚀 Run the Demo

### Option 1: Demo Agent (Recommended)

Start a new chat and invoke the Demo Agent:

```
@Demo Agent run the push protection demo
```

**Demo Modes:**

| Mode | Command | What Happens |
|------|---------|--------------|
| **Block Mode** (default) | `@Demo Agent run the push protection demo` | Push is blocked, shows bypass page |
| **Interactive Mode** | `@Demo Agent run the push protection demo step by step` | Pauses after each ACT to answer questions |
| **Dry Run Mode** | `@Demo Agent run the push protection demo in dry run mode` | Secret goes through, shows up in Security Alerts |

**Interactive Mode** pauses after each step so you can:
- Ask questions about what just happened
- Take notes or discuss with your team
- Move at your own pace

> 💡 **Tip:** Combine modes! Use `@Demo Agent interactive dry run` for a step-by-step walkthrough of the dry run flow.

**Dry Run Mode** temporarily disables push protection so you can see:
- The secret appearing in **Security → Secret scanning alerts**
- How GitHub auto-revokes detected tokens
- The alert details and remediation options

> ⚠️ **Important:** In dry run mode, remember to re-enable Push Protection and delete the test token after the demo!

### Option 2: Manual CLI
```bash
# After adding token to a file:
git add . && git commit -m "Test" && git push origin security
# Watch for GH013 error!

# Clean up:
git reset --hard HEAD~1
```

---

## 📚 Learn More

- [Secret Scanning Docs](https://docs.github.com/en/code-security/secret-scanning)
- [Push Protection Docs](https://docs.github.com/en/code-security/secret-scanning/push-protection-for-repositories-and-organizations)
- [200+ Supported Secrets](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns)

## 🔐 Supported Secret Types

GitHub detects **200+ secret types** including:
- GitHub tokens (PAT, OAuth, App)
- AWS keys
- Azure credentials
- Slack tokens, Stripe keys, database strings
- And [200+ more](https://docs.github.com/en/code-security/secret-scanning/introduction/supported-secret-scanning-patterns)...

---

*Demo by: @Demo Agent | Last tested: February 25, 2026 | Repo: PM-Playbook-Demo*
