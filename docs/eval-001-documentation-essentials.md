# Documentation Essentials: The Pareto 20%

**Date**: 2026-01-23
**Status**: Accepted
**Context**: Research into common documentation patterns for software projects

## Summary

The vital 20% of documentation types that cover 80% of software project documentation needs.

## The Essential 5

| Type | Prefix/Pattern | Purpose | Priority |
|------|----------------|---------|----------|
| **README** | `README.md` | Project overview, quick start, contribution guidelines | Critical |
| **Architecture** | `arch-` or `ARCHITECTURE.md` | System design rationale, component relationships | Critical |
| **Decision Records** | `adr-` (numbered) | Architectural decisions with rationale | Critical |
| **How-To Guides** | `how-to-` | Step-by-step implementation tasks | High |
| **API Reference** | `api-` or `ref-` | Interface documentation, data models | High |

## The Diátaxis Framework

Research-backed standard for documentation organization:

| Quadrant | Purpose | Orientation | Example Prefix |
|----------|---------|-------------|----------------|
| **Tutorials** | Learning | Step-by-step lessons | `tutorial-` |
| **How-To Guides** | Problem-solving | Goal-oriented steps | `how-to-` |
| **Explanations** | Understanding | Context & rationale | `explanation-` |
| **Reference** | Information | Technical specs | `ref-`, `api-` |

Source: https://diataxis.fr/

## Common Documentation Prefixes

### Core (Essential 20%)
- `README.md` - Project entry point
- `ARCHITECTURE.md` or `arch-` - System design
- `adr-` - Architectural Decision Records
- `api-` - API documentation
- `how-to-` - Implementation guides
- `tutorial-` - Learning guides
- `CHANGELOG.md` - Release history

### Supporting (Context-Specific)
- `prd-` - Product Requirements Documents
- `rfc-` - Requests for Comments (proposals)
- `research-` - Exploratory investigation before decisions
- `eval-` - Assessment of options for decision-making
- `retro-` - Reflection after completion (post-mortem)
- `tasks-` - Task breakdowns

**Distinction: research- vs eval- vs retro-**

| Prefix | Phase | Purpose | Example |
|--------|-------|---------|---------|
| `research-` | Before | Learning, gathering options | Comparing auth providers |
| `eval-` | During | Scoring alternatives, trade-offs | Recommendation matrix |
| `retro-` | After | Lessons learned, what worked | Sprint post-mortem |

**Timeline flow**: `research-` → `eval-` → `decision` → `implementation` → `retro-`

## ADR Pattern

Architectural Decision Records follow a numbered convention:

```bash
adr-0001-technical-choice.md
# or
0001-use-postgres-as-primary-database.md
```

**Status indicators** (for ADRs/RFCs):
```
Status: Accepted
Status: Deprecated
Status: Superseded by 0015
```

## Best Practices

1. **Focus on reducing friction**: Document what questions contributors ask most
2. **Number for ordering**: Use sequential numbering (`001-`, `002-`) for ordered documents
3. **Auto-generate reference**: Use tools like OpenAPI/Swagger, JSDoc for API docs
4. **Keep README current**: It's the first thing contributors see

## Directory Structure Pattern

```
docs/
├── tutorials/        # Learning-oriented
├── how-to/          # Problem-oriented
├── explanations/    # Understanding-oriented
├── reference/       # Information-oriented
├── adr/            # Architectural decisions
├── rfcs/           # Proposals
└── architecture/   # System design
```

## Key Principle

**Document to reduce future friction**: What problems confuse users? What decisions do developers keep revisiting? What questions do new contributors ask most? Document those first.

---

**Research sources**:
- Divio Diátaxis Framework: https://diataxis.fr/
- Architectural Decision Records: https://adr.github.io/
