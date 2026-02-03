# Writing PRDs for AI-Assisted Development

**Date**: 2026-02-03
**Context**: Best practices for structuring PRDs that work well with Claude Code and other AI coding assistants

## Overview

PRDs for AI-assisted development serve a dual purpose:
1. **Human-readable** requirements document for developers
2. **Machine-parseable** specification for AI agents

When structured with clear sections, AI can fetch and reference specific PRD sections directly—keeping implementation aligned with requirements.

## Core Principles

### 1. Use Clear, Predictable Sections

AI agents work best with consistent headings:

- Introduction
- Problem Statement
- Solution/Feature Overview
- User Stories
- Technical Requirements
- Acceptance Criteria
- Constraints & Non-Negotiables

This allows prompts like "Implement per PRD section 3.2" to fetch precise context.

### 2. Write Atomic User Stories

Keep each story focused on ONE requirement.

**Format:**
```
As a [role]
I want to [action]
So that [benefit]
```

**Bad**: Blended requirements
> As a user, I want to filter tasks by priority and category and export them.

**Good**: Atomic stories
> US1: Filter tasks by priority
> US2: Filter tasks by category
> US3: Export filtered tasks

### 3. Explicit Acceptance Criteria

List criteria as bullet points—these become discrete "checkboxes" for AI to implement:

- The "High Priority" tag appears in red
- Tasks can be filtered by priority on the main dashboard
- Filtering persists on page refresh
- Filter state is shareable via URL

### 4. State Constraints as Non-Negotiables

Call out hard technical/business boundaries so AI doesn't suggest violating them:

- **Must** use OAuth 2.0 for authentication
- **Must not** store PII without explicit consent
- **Must support** 10,000 concurrent sessions
- **Must not** use external cloud services (compliance)

### 5. Include Technical Specs

Document APIs, data models, and business logic explicitly:

```typescript
interface Task {
  id: string;
  title: string;
  priority: "low" | "medium" | "high";
  category: string;
  completedAt?: Date;
}
```

This prevents AI from inventing details or misinterpreting requirements.

## PRD Template

```markdown
# PRD-[NNN]: [Feature Name]

## Introduction
[2-3 sentences: what this feature is and why it matters]

## Problem Statement
[Current pain points, what users can't do today]

## Solution Overview
[High-level approach: 3-5 bullet points]

## User Stories

### US1: [Story Title]
**As a** [role]
**I want to** [action]
**So that** [benefit]

**Acceptance Criteria:**
- [ ] Criterion 1
- [ ] Criterion 2
- [ ] Criterion 3

[Repeat US2, US3, ...]

## Technical Requirements

### Data Models
[TypeScript interfaces or database schema]

### API Endpoints
```
METHOD /path
Description
```

### External Dependencies
[Third-party services, APIs, libraries]

## Constraints & Non-Negotiables
- **Must** [requirement]
- **Must not** [prohibition]

## Success Metrics
- [Quantifiable outcomes]
- [Performance targets]

## Open Questions
1. [Question]
   - *Recommendation*: [Proposed answer, or leave blank if truly open]

> **Tip**: Leave answers blank when uncertain. Use `*Recommendation*: [your suggestion]` when you have a preferred direction but want feedback.

## Timeline
| Week | Deliverable |
|------|-------------|
| 1 | [Milestone] |

---

*Last Updated: [DATE]*
*Status: [Draft | Approved | Deprecated]*
```

## Common Mistakes

| Mistake | Why It Fails | Fix |
|---------|--------------|-----|
| Vague user stories | AI misses blended requirements | One requirement per story |
| Paragraph-style criteria | Hard to parse as checkboxes | Use bullet points |
| Missing constraints | AI suggests invalid approaches | Add "Non-Negotiables" section |
| Inconsistent formatting | AI can't fetch by section | Use template headings |
| Unstructured PRDs | Can't reference by section | Number sections, use headings |
| Missing technical specs | AI invents data structures | Include TypeScript interfaces |

## Pairing with AGENTS.md / CLAUDE.md

| Document | Purpose |
|----------|---------|
| **PRD** | What to build (requirements, features) |
| **AGENTS.md / CLAUDE.md** | How to build it (tech stack, code style, conventions) |

Together, they ensure AI produces code that matches both requirements and implementation standards.

## References

- ChatPRD: [Best Practices for PRDs with Claude Code](https://www.chatprd.ai/resources/PRD-for-Claude-Code)
- Diátaxis Framework: https://diataxis.fr/
- ADR Pattern: See `eval-001-documentation-essentials.md`
