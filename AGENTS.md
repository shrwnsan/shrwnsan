# AGENTS.MD

@shrwnsan owns this. Welcome! Let's build something great together.
Work style: telegraph preferred; noun-phrases ok; drop filler; min tokens. Ask when unsure.

## Agent Protocol

### Contact & Identity
- **Owner**: @shrwnsan (GitHub: shrwnsan)

### Workspace Structure
- **Primary**: Current working directory (respect where we are)
- **Main dev directory**: `~/Developer`
- **Personal repos**: `~/Developer/personal`
- **Forks/OSS**: `~/Developer/forked`
- **Sandbox/experiments**: `~/Developer/sandbox`
- **Missing repo?** Clone `https://github.com/shrwnsan/<repo>.git` to appropriate subdirectory

### File Operations
- **Edit** files in current repo or referenced project
- **Delete**: Use `trash` (never `rm -rf`) for safety
- **Create**: Only when necessary; prefer editing existing files
- **Max file size**: Aim for <500 LOC; split when needed

### Git Workflow
- **Commits**: Conventional Commits format (`feat|fix|refactor|docs|chore|test|ci`)
- **AI co-authorship**: Include appropriate attribution based on model used (e.g., GLM, Claude, etc.)
- **Push**: Only when explicitly requested
- **Branch changes**: Ask for consent first
- **Destructive ops**: Forbidden unless explicit (`reset --hard`, `clean`, `rebase`)
- **Review**: Use `gh pr view/diff` (no URLs)
- **Amend**: Only when requested

### CI & Quality Gates
- Before handoff: Run lint, typecheck, tests
- CI red? Check with `gh run list/view`, fix until green
- No ship without docs (if applicable)

### Pull Requests
- Active PR: `gh pr view --json number,title,url`
- Comments: `gh pr view <PR> --comments`
- Reply: Cite fix + file/line, resolve threads after landing

### Screenshots (when requested)
- Pick newest PNG in `~/Desktop` or `~/Downloads`
- Verify correct UI (ignore filename)
- Check dimensions: `sips -g pixelWidth -g pixelHeight <file>`
- Optimize if needed: `brew install imageoptim-cli` → `imageoptim <file>`

### Documentation
- Read relevant docs before coding changes
- Update docs when behavior/API changes
- Keep docs accurate and concise

### Code Style
- **TypeScript/JavaScript**: Use existing patterns in repo
- **Shell**: POSIX-compliant when possible
- **Avoid**: "AI slop" — generic code, unnecessary abstractions
- **Prefer**: Simple, direct solutions over clever ones

### Critical Thinking
- Fix root causes, not symptoms
- Unsure? Read more code, then ask with short options
- Conflicts: Call them out, pick safer path
- Unrecognized changes: Assume other agent/context, stay focused
- Leave breadcrumbs in comments when helpful

### Tech Stack Notes

#### Node.js/Bun
- Use repo's package manager (npm, pnpm, bun, yarn)
- Respect existing lockfiles
- Run `docs:list` if available

#### Python
- Use venv/poetry/pipenv as configured
- Respect pyproject.toml/requirements.txt

#### Git
- Prefer HTTPS remotes
- Use `committer` helper if available, or standard commit flow
- Keep commits small and reviewable

### Tools Reference

#### GitHub CLI (`gh`)
- PRs: `gh pr view`, `gh pr diff`
- Issues: `gh issue view <number> --comments`
- CI: `gh run list`, `gh run view <run-id>`

#### `trash`
- Safe delete: `trash <file_or_dir>`

#### `docs:list` (if available)
- List project docs before coding
- Built from `bin/docs-list` or `scripts/docs-list.ts`

### Slash Commands (if using Claude Code)
- Check `~/.claude/commands/` or repo's `docs/slash-commands/`
- Examples: `/commit`, `/review`, `/plan`

### Model Preferences
- **Latest models preferred**: Claude Sonnet 4.5, Opus 4.5, GPT-4.1+
- **Avoid**: Outdated models (Sonnet 3.5, GPT-3.5)
- **Reasoning**: Use best available for context window and capabilities

---

## Design Philosophy (Anti-"AI Slop")

**Avoid:**
- Generic component grids
- Purple-on-white gradients
- Inter/Roboto as default fonts
- Meaningless micro-animations
- Predictable "startup" layouts

**Prefer:**
- Real typography (SF Pro, bespoke fonts)
- Bold accent colors over timid gradients
- 1-2 high-impact motion moments
- Depth in backgrounds (patterns, gradients)
- Opinionated, distinctive layouts

---

## Important Locations

- **Dotfiles**: Local dotfiles repo (look for `dotfiles/` or `.dotfiles/` in workspace)
- **Claude settings**: `~/.claude/`
- **Personal site**: Research posts repository (shrwnsan.github.io)
- **Workspace structure**:
  - `~/Developer/personal/` - Your projects
  - `~/Developer/forked/` - OSS contributions
  - `~/Developer/sandbox/` - Experiments

---

## Notes

- **Ship small, iterate often**: Small commits, frequent reviews

---

## Resources

### Maintenance
- **Review quarterly**: Remove outdated tool references, update model preferences
- **After workspace changes**: Update paths if directory structure changes
- **After new tools**: Add to Tools Reference when something becomes frequently used
- **Prune aggressively**: If a section feels redundant, cut it — agents prefer concise

### Learn More
- https://agents.md/ — AGENTS.md hub and examples
- https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/ — GitHub's analysis of 2500+ AGENTS.md files *(Nov 2025)*
- https://www.builder.io/blog/agents-md — Builder.io's guide with practical dos/don'ts *(Sep 2025)*
- https://www.anthropic.com/engineering/claude-code-best-practices — Anthropic's official best practices *(Nov 2025)*
- https://www.humanlayer.dev/blog/writing-a-good-claude-md — HumanLayer's guide on CLAUDE.md/AGENTS.md *(Nov 2025)*

### Inspired by
[steipete/agent-scripts](https://github.com/steipete/agent-scripts/blob/main/AGENTS.MD)
