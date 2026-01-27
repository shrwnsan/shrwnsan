0;545;1378m# Claude Code Assistant Workflow

GitHub Action workflow that enables Claude-powered PR reviews and issue handling via `@claude` mentions.

## Features

### PR Review with Triage

Triggered by mentioning `@claude` in:
- PR comments
- Review comments
- Review submissions

**Triage Categories:**

| Priority | Category | Action |
|----------|----------|--------|
| 🚨 Critical | Security, breaking changes, data loss, critical bugs | Block merge, require fix |
| ⚠️ Medium | Performance, refactoring, test gaps, docs | Creates follow-up issue |
| 💡 Minor | Style, naming, optimizations | Inline suggestions |

### Issue Handler

Triggered by `@claude` in:
- Issue comments
- New issue body/title
- Assigned issues

Claude can answer questions, implement features, debug, or explain code.

## Setup

1. **Install Claude GitHub App**: [github.com/apps/claude](https://github.com/apps/claude)
2. **Add secret**: `ANTHROPIC_API_KEY` in repository settings
3. **Deploy workflow**: Copy `claude.yml` to `.github/workflows/`

## Usage

```markdown
@claude please review this PR

@claude what does the auth module do?

@claude implement the feature described in this issue
```

## Files

- [`claude.yml`](claude.yml) — Workflow definition

## References

### Primary Documentation

- [Claude Code Action](https://github.com/anthropics/claude-code-action) — Official GitHub Action repository
- [Claude Code GitHub Actions Guide](https://code.claude.com/docs/en/github-actions) — Integration docs
- [Example Workflows](https://github.com/anthropics/claude-code-action/tree/main/examples) — Official examples

### Guides

- [Setup Guide](https://github.com/anthropics/claude-code-action/blob/main/docs/setup.md)
- [Usage Guide](https://github.com/anthropics/claude-code-action/blob/main/docs/usage.md)
- [Solutions Guide](https://github.com/anthropics/claude-code-action/blob/main/docs/solutions.md)
- [Configuration](https://github.com/anthropics/claude-code-action/blob/main/docs/configuration.md)
- [Custom Automations](https://github.com/anthropics/claude-code-action/blob/main/docs/custom-automations.md)

### Security & Reference

- [Security Documentation](https://github.com/anthropics/claude-code-action/blob/main/docs/security.md)
- [Capabilities & Limitations](https://github.com/anthropics/claude-code-action/blob/main/docs/capabilities-and-limitations.md)
- [FAQ](https://github.com/anthropics/claude-code-action/blob/main/docs/faq.md)

### Related

- [Claude GitHub App](https://github.com/apps/claude) — Required app installation
- [Anthropic Console](https://console.anthropic.com) — API key management
- [CLAUDE.md Memory Docs](https://code.claude.com/docs/en/memory) — Repository-level instructions
