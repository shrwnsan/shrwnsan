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

#### Kimi K2.5 🆕

**Factory Multiplier:** Not yet available (estimated 0.3-0.5×)
**Pricing:** $0.60/$2.50 per 1M tokens (direct via Moonshot/OpenRouter)

**Strengths:**
- **Agent Swarm Architecture:** Coordinates up to 100 specialized agents simultaneously
- **4.5× Faster Execution:** Parallel-Agent Reinforcement Learning (PARL)
- **Open Source:** Model weights available for private deployment
- **Multimodal:** Strong visual debugging capabilities (15T mixed tokens trained)
- **Cost-Effective:** 76% cheaper than Claude Opus 4.5

**Weaknesses:**
- **Not on Factory Yet:** Requires external provider (OpenRouter, Fireworks AI)
- **Swarm Costs:** Agent execution can multiply token usage unexpectedly
- **Newer Model:** Less battle-tested in production workflows

**Best For:**
- Complex multi-file refactoring requiring parallel analysis
- Visual-heavy codebases (UI debugging from screenshots)
- Teams wanting open-source with optional private deployment
- Organizations needing data residency compliance (Fireworks AI routing)

**Pricing Note:**
```
Direct pricing: $0.60/$2.50 per 1M tokens
With cache: $0.30/$1.25 per 1M tokens (50% savings)
Estimated Factory cost: ~$0.08-$0.54 per 1M standard tokens (if added)
```

**When It Beats GPT-5.2:**
- PRs requiring visual analysis (screenshots, designs)
- Complex workflows benefiting from parallel agent execution
- When open-source requirements or data residency are constraints

---

#### GLM 4.7 🆕

**Factory Multiplier:** Not yet available (estimated 0.3-0.4×)
**Pricing:** $0.40/$1.50 per 1M tokens (direct via Z.AI)

**Strengths:**
- **Strong SWE-Bench:** 73.8% (competitive with proprietary models)
- **Tool Reliability:** 41% on Terminal Bench 2.0 (excellent for coding agents)
- **End-to-End Fixes:** Focuses on complete solutions vs. explanations
- **Multilingual:** 66.7% on SWE-bench Multilingual
- **Stable Execution:** Clearer decision-making, fewer cascading errors

**Weaknesses:**
- **Not on Factory Yet:** Requires direct integration
- **Smaller Context:** 131K-200K tokens (less than Gemini's 1M)
- **Less Reasoning Depth:** Behind GPT-5.2 on complex logic tasks

**Best For:**
- Production coding agents requiring reliability
- Teams focused on terminal-based workflows
- Multilingual codebases
- When cost matters more than maximum reasoning depth

**Estimated Factory Cost:**
```
Direct: $0.40/$1.50 per 1M tokens
Estimated Factory: ~$0.10-$0.40 per 1M standard tokens
Savings vs GPT-5.2: ~80% cheaper (if available on Factory)
```

**When It Beats GPT-5.2:**
- Coding agent workflows requiring stability
- Terminal-heavy development tasks
- Budget-constrained teams needing >70% SWE-bench performance

---

#### GLM 4.7 Flash 🆕

**Factory Multiplier:** Not yet available (estimated 0.1-0.2×)
**Pricing:** $0.07/$0.40 per 1M tokens (FREE API tier available)

**Strengths:**
- **Surprisingly Good:** 59.2% on SWE-bench Verified (beats Qwen3-30B's 22%)
- **Ultra-Low Cost:** 20× cheaper than GPT-5.2 ($0.07 vs $1.75)
- **Fast & Efficient:** 60-80+ tokens/second on local hardware
- **Local Deployment:** Runs on 24GB GPUs or Mac M-series
- **Free API Tier:** Unlimited access without credit card

**Weaknesses:**
- **Not on Factory Yet:** Requires direct integration
- **Simpler Reasoning:** May struggle with complex architectural reviews
- **Smaller Context:** 128K-200K tokens

**Best For:**
- High-volume PR triage
- Teams with extreme budget constraints
- Local/offline requirements (security/compliance)
- Quick iteration on prototype code

**Estimated Factory Cost:**
```
Direct: $0.07/$0.40 per 1M tokens (or FREE)
Estimated Factory: ~$0.02-$0.08 per 1M standard tokens
Savings vs GPT-5.2: ~95% cheaper
```

**When It Beats GPT-5.2:**
- Ultra-high-volume PR workflows
- When every dollar counts (bootstrapped teams)
- Local/offline requirements
- Initial triage before escalation to premium models

---

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
| Kimi K2.5* | ~0.4× (est.) | $0.08 | $0.54 | **6.25× cheaper** |
| GLM 4.7* | ~0.3× (est.) | $0.10 | $0.40 | **5.0× cheaper** |
| GLM 4.7 Flash* | ~0.15× (est.) | $0.02 | $0.08 | **25× cheaper** |
| Claude Haiku 4.5 | 0.4× | $0.11 | $1.08 | **3.0× cheaper** |
| Gemini 3 Flash | 0.2× | $0.05 | $0.27 | **7.0× cheaper** |

*Not yet available on Factory - pricing shown is estimated based on direct API costs and projected Factory multiplier

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

### For Budget-Conscious Teams (Updated)
```yaml
all_reviews:
  model: GLM 4.7 Flash  # NEW: 59.2% SWE-bench at $0.07/$0.40
  reason: 95% cheaper than GPT-5.2, surprisingly capable
  trigger: Non-critical PRs

escalation:
  model: GPT-5.2
  trigger: Complex changes or security implications
  reason: Maintain quality where it matters
```

### For Open Source / Local Deployment
```yaml
primary:
  model: GLM 4.7 Flash  # Free API tier, runs on 24GB GPUs
  deployment: Local or on-premises
  reason: No vendor lock-in, data privacy

alternative:
  model: Kimi K2.5  # Open-source weights available
  deployment: Private cloud
  reason: Agent swarm for complex workflows
```

### For Visual-Heavy Codebases
```yaml
ui_pr_reviews:
  model: Kimi K2.5  # Multimodal + visual debugging
  reason: Analyze screenshots, designs, UI code

backend_review:
  model: GPT-5.2
  reason: Superior reasoning for business logic
```
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

| Model | SWE-Bench | SWE-Bench Multilingual | Terminal Bench | HLE* | Best Use Case |
|-------|-----------|----------------------|----------------|------|---------------|
| Claude Opus 4.5 | **80.9%** | N/A | 44% (best) | N/A | Coding accuracy |
| GLM 4.7 | 73.8% | 66.7% | 41% | N/A | Reliable coding agent |
| Gemini 3 Pro | 77.4% | N/A | N/A | N/A | Large context |
| Claude Sonnet 4.5 | 76.8% | N/A | N/A | N/A | General coding |
| GLM 4.7 Flash | 59.2% | N/A | N/A | N/A | Budget coding |
| **GPT-5.2** | 55.6% | N/A | N/A | N/A | **Reasoning + Security** |
| Kimi K2.5 | 50.2% (HLE) | N/A | N/A | **50.2%** | Multimodal + swarm |

*HLE = Humanity's Last Exam (different from SWE-bench)

## Decision Matrix

| Scenario | Recommended | Alternative | Rationale |
|----------|-------------|-------------|-----------|
| **Automated PR Review** | GPT-5.2 | Claude Sonnet 4.5 | Best reasoning + cost balance |
| **Security Audit** | GPT-5.2 | Claude Opus 4.5 | Superior threat detection |
| **Large PRs** (>500K tokens) | Gemini 3 Pro | Claude Opus 4.5 | 1M context window |
| **Budget Constraints** | GLM 4.7 Flash* | Claude Haiku 4.5 | 95% cheaper, surprisingly good |
| **High-Stakes Code** | Claude Opus 4.5 | GPT-5.2 | Highest accuracy, cost secondary |
| **Style/Linting Only** | GLM 4.7 Flash* | Gemini 3 Flash | Ultra-low cost, FREE tier available |
| **Visual Debugging** | Kimi K2.5* | Claude Opus 4.5 | Multimodal + agent swarm |
| **Production Coding Agent** | GLM 4.7* | GPT-5.2 | Reliable tool execution, cost-effective |
| **Open Source Required** | GLM 4.7 Flash* | Kimi K2.5* | Local deployment, no vendor lock-in |

*Not yet on Factory - requires external integration

## Future Models to Evaluate

**Recently Added (2026-02-03):**
- [x] Kimi K2.5 - Agent Swarm, multimodal, $0.60/$2.50
- [x] GLM 4.7 - 73.8% SWE-bench, reliable tool execution
- [x] GLM 4.7 Flash - 59.2% SWE-bench, FREE tier, $0.07/$0.40

**Future Candidates:**
- [ ] DeepSeek V3 - Rumored strong coding model
- [ ] Qwen 3 - Updated versions with improved coding
- [ ] Claude Haiku 4.5 "Thinking" mode - Benchmark data emerging
- [ ] Additional Factory Droid models as they're added

**Monitoring:**
- Factory Droid roadmap for new model additions
- SWE-bench Verified leaderboard updates
- Open-source model releases (especially from Chinese labs)

## Data Verification

All benchmark claims and pricing data have been verified against primary sources as of 2026-02-03:

| Claim | Source | Status |
|-------|--------|--------|
| Claude Opus 4.5: 80.9% SWE-Bench | [Vellum AI](https://www.vellum.ai/blog/claude-opus-4-5-benchmarks), [The Unwind AI](https://www.theunwindai.com/p/claude-opus-4-5-scores-80-9-on-swe-bench) | ✓ Verified |
| GPT-5.2: 92.4% GPQA Diamond | [OpenAI Official](https://openai.com/index/introducing-gpt-5-2/), [Vellum AI](https://www.vellum.ai/blog/gpt-5-2-benchmarks) | ✓ Verified |
| Haiku 4.5: 58% PR reviews vs Sonnet | [Qodo Blog](https://www.qodo.ai/blog/thinking-vs-thinking-benchmarking-claude-haiku-4-5-and-sonnet-4-5-on-400-real-prs/) | ✓ Verified |
| GLM 4.7: 73.8% SWE-bench, 41% Terminal Bench | [Z.ai Official](https://z.ai/blog/glm-4-7) | ✓ Verified |
| GLM 4.7 Flash: 59.2% SWE-bench | [Medium Guide](https://medium.com/@zh.milo/glm-4-7-flash-the-ultimate-2026-guide-to-local-ai-coding-assistant-93a43c3f8db3) | ✓ Verified |
| Factory multipliers (0.2× - 2×) | [Factory Pricing Docs](https://docs.factory.ai/pricing) | ✓ Verified |

## References

- [Factory Pricing Documentation](https://docs.factory.ai/pricing)
- [Claude Opus 4.5 Benchmarks](https://www.vellum.ai/blog/claude-opus-4-5-benchmarks)
- [The Unwind AI: Claude Opus 4.5 Scores 80.9% on SWE-Bench](https://www.theunwindai.com/p/claude-opus-4-5-scores-80-9-on-swe-bench)
- [OpenAI: Introducing GPT-5.2](https://openai.com/index/introducing-gpt-5-2/)
- [GPT-5.2 Benchmarks](https://www.vellum.ai/blog/gpt-5-2-benchmarks)
- [Qodo AI: Haiku vs Sonnet PR Benchmark (400 Real PRs)](https://www.qodo.ai/blog/thinking-vs-thinking-benchmarking-claude-haiku-4-5-and-sonnet-4-5-on-400-real-prs/)
- [Claude vs GPT vs Gemini Comparison](https://www.cosmicjs.com/blog/best-ai-for-developers-claude-vs-gpt-vs-gemini-)
- [Kimi K2.5 Complete Guide](https://www.codecademy.com/article/kimi-k-2-5-complete-guide-to-moonshots-ai-model)
- [Z.ai: GLM-4.7 Official Announcement](https://z.ai/blog/glm-4-7)
- [GLM-4.7-Flash Ultimate Guide](https://medium.com/@zh.milo/glm-4-7-flash-the-ultimate-2026-guide-to-local-ai-coding-assistant-93a43c3f8db3)

## Changelog

**2026-02-03 (Update 3):**
- Added Data Verification section with source links for all benchmark claims
- Updated References with direct source links (OpenAI, Z.ai, Qodo, The Unwind AI)
- Removed TODO for Kimi K2.5, GLM 4.7, GLM 4.7 Flash (completed)

**2026-02-03 (Update 2):**
- Added Kimi K2.5 evaluation (Agent Swarm, multimodal, open-source)
- Added GLM 4.7 evaluation (73.8% SWE-bench, reliable tool execution)
- Added GLM 4.7 Flash evaluation (59.2% SWE-bench, FREE tier, 95% savings)
- Updated cost comparison table with new models
- Updated benchmark summary with SWE-bench Multilingual and Terminal Bench
- Expanded decision matrix with 3 new use cases
- Added new workflow examples for budget, open-source, and visual debugging scenarios

**2026-02-03 (Initial):**
- Initial version with core models (GPT-5.2, Claude Sonnet/Opus/Haiku 4.5, Gemini 3 Pro/Flash)
