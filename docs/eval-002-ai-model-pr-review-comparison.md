# eval-002: AI Model Comparison for PR Reviews

**Date:** February 3, 2026
**Status:** Draft - Initial Version
**Context:** Optimizing Factory Droid's automated PR review workflow
**Related:** [eval-001-documentation-essentials.md](./eval-001-documentation-essentials.md)

## Executive Summary

Evaluation of AI models for automated pull request reviews to balance code quality, security vulnerability detection, and cost efficiency. Based on Factory Droid pricing multipliers and 2026 benchmark performance.

**Key Finding:** **GPT-5.2** (0.7× multiplier) provides the optimal balance for PR reviews - superior reasoning capabilities at 2.7× lower cost than Claude Sonnet 4.5.

## Evaluation Criteria

| Criterion | Weight | Description |
|-----------|--------|-------------|
| **Code Review Accuracy** | High | SWE-Bench Verified scores, real-world PR performance |
| **Security Analysis** | Critical | Ability to detect vulnerabilities, GHSA-level threat detection |
| **Reasoning Depth** | High | GPQA Diamond, complex multi-file analysis |
| **Speed/Latency** | Medium | Response time for iterative review cycles |
| **Cost Efficiency** | Medium | Factory pricing multiplier per 1M standard tokens |
| **Context Window** | Medium | Ability to handle large PRs (>5000 LOC) |

## Models Evaluated

### Tier 1: Recommended for PR Reviews

#### GPT-5.2 ⭐ Recommended

**Factory Multiplier:** 0.7×
**Pricing:** $1.75/$14 per 1M tokens (~$0.50-$3.80 via Factory)

**Strengths:**
- **Superior Reasoning:** 92.4% on GPQA Diamond (vs Claude's 37.6%)
- **Perfect Math Logic:** 100% on AIME 2025
- **Strong Coding:** 55.6% on SWE-Bench Pro
- **Fast Iteration:** Optimized for agentic task chains
- **Multi-file Analysis:** Excels at complex cross-file refactoring reviews

**Weaknesses:**
- Slightly lower raw coding score than Claude Opus 4.5 (80.9% vs 55.6%)
- Smaller context window than some competitors

**Best For:**
- Security-focused PR reviews
- Complex refactoring across multiple files
- Automated review workflows requiring speed

**Factory Cost Example:**
```
100K token PR review:
- GPT-5.2: ~70 standard tokens = $0.19
- Claude Sonnet 4.5: ~120 standard tokens = $0.51
- Savings: 63% with GPT-5.2
```

---

#### Claude Opus 4.5

**Factory Multiplier:** 2×
**Pricing:** $5/$25 per 1M tokens (~$1.35-$6.75 via Factory)

**Strengths:**
- **Highest Coding Accuracy:** 80.9% on SWE-Bench Verified (first AI >80%)
- **Cleaner Code:** Up to 76% fewer tokens in complex tasks
- **Low Hallucination:** Highest accuracy in knowledge assessments
- **Best Terminal Performance:** 44% on Terminal-Bench Hard

**Weaknesses:**
- **2.7× More Expensive** than GPT-5.2 (2× vs 0.7× multiplier)
- Slower iteration on code changes
- Higher latency for real-time workflows

**Best For:**
- Critical security audits where cost is secondary
- Complex debugging scenarios requiring deep analysis
- Final approval reviews on high-stakes PRs

**When to Use Over GPT-5.2:**
- PRs involving security-critical code
- Complex architectural changes
- When budget is not a constraint

---

### Tier 2: Good for Specific Use Cases

#### Gemini 3 Pro

**Factory Multiplier:** 0.8×
**Pricing:** $2/$12 per 1M tokens (~$0.57-$2.16 via Factory)

**Strengths:**
- **Highest Raw SWE-Bench:** 77.4% (slightly better than Claude Opus)
- **Massive Context:** 1M token context window
- **Best for Large PRs:** Handles extensive codebases efficiently

**Weaknesses:**
- Less sophisticated reasoning than GPT-5.2
- Not as strong on security-focused analysis

**Best For:**
- Very large PRs (>500K tokens)
- Frontend-heavy codebases (1487 Elo in WebDev Arena)
- When context window matters more than reasoning depth

---

### Tier 3: Budget-Friendly Options

#### Claude Haiku 4.5

**Factory Multiplier:** 0.4×
**Pricing:** $1/$10 per 1M tokens (~$0.11-$1.08 via Factory)

**Strengths:**
- **Surprisingly Effective:** Beat Sonnet 4.5 in 58% of PR reviews (thinking mode)
- **Extremely Fast:** Optimized for rapid iteration
- **3× Cheaper** than GPT-5.2 (0.4× vs 0.7×)

**Weaknesses:**
- Less capable on complex architectural reviews
- May miss edge cases in critical code

**Best For:**
- Initial PR triage and quick scans
- Documentation-only changes
- High-volume, low-risk reviews

**Use Case:** Run Haiku 4.5 first for quick triage, escalate to GPT-5.2 for complex changes.

---

#### Gemini 3 Flash

**Factory Multiplier:** 0.2×
**Pricing:** $0.50/$3 per 1M tokens (~$0.05-$0.27 via Factory)

**Strengths:**
- **Ultra-Low Cost:** 3.5× cheaper than GPT-5.2
- **Fast Response:** Optimized for real-time workflows
- **Good for Simple Tasks:** Formatting, style checks

**Weaknesses:**
- Limited reasoning capabilities
- Not suitable for security reviews

**Best For:**
- Style guide enforcement
- Linting suggestion reviews
- Simple refactoring PRs

---

## Cost Comparison Table

| Model | Factory Multiplier | Input Cost | Output Cost | Relative to GPT-5.2 |
|-------|-------------------|------------|-------------|---------------------|
| **GPT-5.2** | 0.7× | $0.50 | $3.80 | **Baseline (1.0×)** |
| Claude Sonnet 4.5 | 1.2× | $0.86 | $6.51 | 2.3× more expensive |
| Claude Opus 4.5 | 2× | $1.35 | $6.75 | 2.7× more expensive |
| Gemini 3 Pro | 0.8× | $0.57 | $3.40 | 1.1× more expensive |
| Claude Haiku 4.5 | 0.4× | $0.11 | $1.08 | **3.0× cheaper** |
| Gemini 3 Flash | 0.2× | $0.05 | $0.27 | **7.0× cheaper** |

*Approximate costs via Factory based on typical cache ratios (4-8×)*

## Recommended Workflow

### For Security-Critical Projects
```yaml
primary_review:
  model: GPT-5.2
  reason: Superior threat detection + cost efficiency

escalation:
  model: Claude Opus 4.5
  trigger: High-risk patterns detected
  reason: Deepest analysis for critical code
```

### For High-Volume Projects
```yaml
triage:
  model: Claude Haiku 4.5
  reason: Fast, cheap initial scan

standard_review:
  model: GPT-5.2
  trigger: Triage passes
  reason: Balanced quality + cost

deep_dive:
  model: Claude Opus 4.5
  trigger: Complex architectural changes
  reason: Maximum accuracy when needed
```

### For Budget-Conscious Teams
```yaml
all_reviews:
  model: GPT-5.2
  reason: Best balance of quality and cost

occasional_audit:
  model: Claude Opus 4.5
  frequency: Weekly sample of 10% of PRs
  reason: Quality assurance without constant high cost
```

## Benchmark Summary

| Model | SWE-Bench | GPQA Diamond | AIME 2025 | Best Use Case |
|-------|-----------|--------------|-----------|---------------|
| Claude Opus 4.5 | **80.9%** | 37.6% | 83.3% | Coding accuracy |
| **GPT-5.2** | 55.6% | **92.4%** | **100%** | **Reasoning + Security** |
| Gemini 3 Pro | 77.4% | 31.1% | 70.0% | Large context |
| Claude Sonnet 4.5 | 76.8% | N/A | N/A | General coding |

## Decision Matrix

| Scenario | Recommended | Alternative | Rationale |
|----------|-------------|-------------|-----------|
| **Automated PR Review** | GPT-5.2 | Claude Sonnet 4.5 | Best reasoning + cost balance |
| **Security Audit** | GPT-5.2 | Claude Opus 4.5 | Superior threat detection |
| **Large PRs** (>500K tokens) | Gemini 3 Pro | Claude Opus 4.5 | 1M context window |
| **Budget Constraints** | Claude Haiku 4.5 | GPT-5.2 | 3× cheaper, surprisingly effective |
| **High-Stakes Code** | Claude Opus 4.5 | GPT-5.2 | Highest accuracy, cost secondary |
| **Style/Linting Only** | Gemini 3 Flash | Claude Haiku 4.5 | Ultra-low cost for simple tasks |

## Future Models to Evaluate

**To Be Added:**
- [ ] Kimi K2.5 - Agent Swarm architecture, $0.60/$3 pricing
- [ ] GLM 4.7 - $0.40/$1.50, strong coding capabilities
- [ ] GLM 4.7 Flash - $0.07/$0.40, 59.2% SWE-bench
- [ ] Additional Claude variants (Haiku thinking modes)

## References

- [Factory Pricing Documentation](https://docs.factory.ai/pricing)
- [Claude Opus 4.5 Benchmarks](https://www.vellum.ai/blog/claude-opus-4-5-benchmarks)
- [GPT-5.2 Benchmarks](https://www.vellum.ai/blog/gpt-5-2-benchmarks)
- [Qodo AI: Haiku vs Sonnet PR Benchmark](https://www.qodo.ai/blog/thinking-vs-thinking-benchmarking-claude-haiku-4-5-a)
- [Claude vs GPT vs Gemini Comparison](https://www.cosmicjs.com/blog/best-ai-for-developers-claude-vs-gpt-vs-gemini-)

## Changelog

**2026-02-03:** Initial version with core models (GPT-5.2, Claude Sonnet/Opus/Haiku 4.5, Gemini 3 Pro/Flash)

**TODO:** Add Kimi K2.5, GLM 4.7, GLM 4.7 Flash evaluation
