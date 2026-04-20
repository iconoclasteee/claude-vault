---
name: business-case-builder
description: >
  Build compelling business cases that get approved. Structured framework for justifying
  investments, initiatives, and strategic decisions with financial rigor and executive-ready
  presentation. Use when users need to: (1) justify a budget request or investment,
  (2) get approval for a new initiative or project, (3) make a build vs. buy decision,
  (4) propose a new hire or team expansion, (5) recommend a vendor or tool purchase,
  (6) present a strategic recommendation to leadership. Triggers on: "business case for",
  "justify this investment", "get approval for", "ROI on", "make the case for",
  "should we invest in", "build vs buy", "cost-benefit analysis", "payback period".
---

# Business Case Builder

Structured framework for building business cases that get approved. Combines financial rigor with clear executive communication.

## When to Use

- Requesting budget for a new initiative
- Proposing a tool, vendor, or technology investment
- Justifying headcount or team expansion
- Making build vs. buy recommendations
- Any decision requiring executive/finance approval

## Core Workflow

```
1. FRAME — What decision are we enabling?
      ↓
2. QUANTIFY — What are the costs and benefits?
      ↓
3. COMPARE — What are the alternatives?
      ↓
4. RISK — What could go wrong?
      ↓
5. RECOMMEND — What should we do and why?
      ↓
OUTPUT: Executive-ready business case
```

---

## Step 1: FRAME the Decision

Before any numbers, clarify what we're actually deciding.

**Key questions:**
- What is the specific decision or approval being requested?
- What problem does this solve or opportunity does it capture?
- Why now? What's the cost of delay or inaction?
- Who are the stakeholders and what do they care about?
- What's the decision timeline?

**Output:**
```
DECISION REQUESTED
[Specific approval or decision needed]

PROBLEM/OPPORTUNITY
[What this addresses — be specific]

STRATEGIC ALIGNMENT
[How this connects to company/team priorities]

COST OF INACTION
[What happens if we don't do this]
```

---

## Step 2: QUANTIFY Costs and Benefits

The heart of any business case. Be specific, be honest, include ranges.

### Cost Categories

**One-Time Costs:**
- Purchase/licensing fees
- Implementation/setup
- Training
- Migration/transition
- Integration work

**Ongoing Costs:**
- Subscription/maintenance fees
- Headcount (fully loaded: salary + benefits + overhead)
- Infrastructure/hosting
- Support and maintenance
- Opportunity cost (what else could this money do?)

**Hidden Costs (often missed):**
- Management attention
- Change management
- Productivity dip during transition
- Technical debt if cutting corners
- Vendor lock-in implications

### Benefit Categories

**Hard Benefits (directly measurable):**
- Revenue increase (new sales, upsell, retention)
- Cost reduction (headcount, tools, infrastructure)
- Time savings (hours × hourly rate)
- Error/defect reduction
- Compliance/risk avoidance (quantify potential penalties)

**Soft Benefits (real but harder to measure):**
- Employee satisfaction/retention
- Customer experience improvement
- Strategic positioning
- Competitive advantage
- Optionality/flexibility

**Quantification guidance:**
- Use ranges (conservative / expected / optimistic)
- State assumptions explicitly
- Time savings: Hours saved × number of people × frequency × hourly cost
- Revenue: Pipeline × conversion rate × average deal size
- Retention: Customers at risk × average LTV × probability of save

**Output:**
```
INVESTMENT REQUIRED

One-Time Costs:
| Item | Conservative | Expected | Optimistic |
|------|--------------|----------|------------|
| [Cost item] | $X | $X | $X |
| [Cost item] | $X | $X | $X |
| **Total One-Time** | $X | $X | $X |

Ongoing Costs (Annual):
| Item | Conservative | Expected | Optimistic |
|------|--------------|----------|------------|
| [Cost item] | $X | $X | $X |
| [Cost item] | $X | $X | $X |
| **Total Annual** | $X | $X | $X |

EXPECTED BENEFITS

Hard Benefits (Annual):
| Benefit | Conservative | Expected | Optimistic | Assumptions |
|---------|--------------|----------|------------|-------------|
| [Benefit] | $X | $X | $X | [Assumption] |
| [Benefit] | $X | $X | $X | [Assumption] |
| **Total Annual** | $X | $X | $X | |

Soft Benefits:
• [Benefit]: [Why it matters, even if not quantified]
```

---

## Step 3: COMPARE Alternatives

Every business case needs options — including "do nothing."

**Standard options to evaluate:**
1. **Status quo** — Do nothing, continue as-is
2. **Proposed solution** — Your recommendation
3. **Alternative A** — Different approach to same problem
4. **Alternative B** — Scaled-down or phased version

**For each alternative, assess:**
- Total cost (one-time + ongoing over time horizon)
- Expected benefits
- Time to value
- Risk level
- Strategic fit

**Build vs. Buy special considerations:**
| Factor | Build | Buy |
|--------|-------|-----|
| Upfront cost | Higher | Lower |
| Ongoing cost | Maintenance burden | Subscription fees |
| Time to value | Longer | Shorter |
| Customization | Full control | Limited |
| Risk | Execution risk | Vendor risk |
| Core competency | Is this what we should be building? | Focus on core business |

**Output:**
```
OPTIONS ANALYSIS

| Criteria | Status Quo | Proposed | Alternative A | Alternative B |
|----------|------------|----------|---------------|---------------|
| 3-Year Total Cost | $X | $X | $X | $X |
| Annual Benefit | $X | $X | $X | $X |
| Time to Value | N/A | X months | X months | X months |
| Risk Level | [H/M/L] | [H/M/L] | [H/M/L] | [H/M/L] |
| Strategic Fit | [H/M/L] | [H/M/L] | [H/M/L] | [H/M/L] |

Why not Status Quo: [Specific reason]
Why not Alternative A: [Specific reason]
Why not Alternative B: [Specific reason]
```

---

## Step 4: Calculate Key Metrics

Decision-makers want specific financial metrics. Calculate these:

### ROI (Return on Investment)
```
ROI = (Total Benefits - Total Costs) / Total Costs × 100%

Example:
Benefits over 3 years: $500,000
Costs over 3 years: $200,000
ROI = ($500K - $200K) / $200K = 150%
```

### Payback Period
```
Payback = Total Investment / Annual Net Benefit

Example:
Total investment: $100,000
Annual net benefit: $40,000
Payback = $100K / $40K = 2.5 years
```

### Net Present Value (NPV)
For larger investments, account for time value of money:
```
NPV = Sum of (Cash Flow / (1 + discount rate)^year) - Initial Investment

Use 10-15% discount rate for most corporate decisions.
Positive NPV = good investment.
```

### Break-Even Analysis
```
At what point do cumulative benefits exceed cumulative costs?
Month X: Cumulative benefits > Cumulative costs
```

**Output:**
```
FINANCIAL SUMMARY

| Metric | Conservative | Expected | Optimistic |
|--------|--------------|----------|------------|
| Total 3-Year Investment | $X | $X | $X |
| Total 3-Year Benefit | $X | $X | $X |
| Net Benefit | $X | $X | $X |
| ROI | X% | X% | X% |
| Payback Period | X months | X months | X months |
| NPV (at 10%) | $X | $X | $X |

Break-even: Month X (expected case)
```

---

## Step 5: ASSESS Risks

Every honest business case acknowledges what could go wrong.

**Risk categories:**
- **Execution risk**: Can we actually do this?
- **Adoption risk**: Will people use it?
- **Technical risk**: Will it work as expected?
- **Vendor risk**: Will the vendor deliver/survive?
- **Market risk**: Will conditions change?
- **Financial risk**: Will costs exceed estimates?

**For each risk:**
1. Describe the risk specifically
2. Rate likelihood: High / Medium / Low
3. Rate impact: High / Medium / Low
4. Define mitigation strategy
5. Identify early warning signs

**Output:**
```
RISK ASSESSMENT

| Risk | Likelihood | Impact | Mitigation | Early Warning |
|------|------------|--------|------------|---------------|
| [Risk 1] | H/M/L | H/M/L | [Action] | [Signal] |
| [Risk 2] | H/M/L | H/M/L | [Action] | [Signal] |
| [Risk 3] | H/M/L | H/M/L | [Action] | [Signal] |

Contingency plan: If [trigger], then [response]
Kill criteria: We stop/reverse if [condition]
```

---

## Step 6: BUILD the Recommendation

Pull everything together into a clear recommendation.

**Executive Summary structure (lead with this):**
1. What we're recommending (one sentence)
2. Why it matters (the problem/opportunity)
3. What it costs (total investment)
4. What we get (key benefits and ROI)
5. What we need (specific approval requested)

**Implementation overview:**
- Key phases and milestones
- Timeline
- Resource requirements
- Success metrics
- Review checkpoints

**Output:**
```
RECOMMENDATION

[One clear sentence: We recommend X because Y]

EXECUTIVE SUMMARY
• Decision requested: [Specific approval]
• Investment required: $X over Y years
• Expected return: $X benefit, X% ROI, X-month payback
• Strategic rationale: [Why this matters now]
• Key risk: [Biggest concern and mitigation]

IMPLEMENTATION OVERVIEW
| Phase | Timeline | Key Milestones | Resources |
|-------|----------|----------------|-----------|
| Phase 1 | Months 1-2 | [Milestone] | [Resources] |
| Phase 2 | Months 3-4 | [Milestone] | [Resources] |
| Phase 3 | Months 5-6 | [Milestone] | [Resources] |

SUCCESS METRICS
• [Metric 1]: Target X by [date]
• [Metric 2]: Target Y by [date]
• [Metric 3]: Target Z by [date]

DECISION NEEDED BY: [Date] — [Reason for timeline]
```

---

## Quick Commands

| Command | Action |
|---------|--------|
| `business case for [initiative]` | Full business case workflow |
| `ROI on [investment]` | Focus on financial analysis |
| `compare [option A] vs [option B]` | Options comparison |
| `build vs buy [solution]` | Build vs. buy analysis |
| `justify [headcount/tool/budget]` | Tailored to request type |
| `risks for [initiative]` | Risk assessment focus |
| `executive summary for [case]` | Just the summary |

---

## Business Case Formats

### Quick Business Case (1 page)
For smaller investments (<$50K) or time-sensitive decisions:
- Decision requested
- Cost and benefit summary (one table)
- ROI and payback
- Top 3 risks
- Recommendation

### Standard Business Case (2-3 pages)
For medium investments ($50K-$500K):
- Full workflow above
- All sections included
- Appendix with detailed assumptions

### Comprehensive Business Case (5+ pages)
For major investments (>$500K) or strategic decisions:
- Full workflow with deep detail
- Multiple scenario analyses
- Sensitivity testing
- Detailed implementation plan
- Stakeholder analysis
- Change management considerations

---

## Common Pitfalls to Avoid

**Overstating benefits:**
- Don't double-count (e.g., time savings AND productivity gains from same source)
- Be conservative on adoption rates
- Discount "soft" benefits appropriately

**Understating costs:**
- Include fully-loaded headcount costs (1.3-1.5x salary)
- Account for management time
- Include transition/migration costs
- Factor in training and change management

**Ignoring alternatives:**
- Always include "do nothing" option
- Show you've considered other approaches
- Explain why alternatives were rejected

**Weak risk assessment:**
- Don't just list risks — quantify impact
- Include mitigation strategies
- Define what would make you reverse the decision

---

## Tailoring by Audience

**For Finance/CFO:**
- Lead with numbers
- Show sensitivity analysis
- Emphasize payback period and cash flow
- Compare to hurdle rate / cost of capital

**For Operations/COO:**
- Lead with efficiency gains
- Emphasize implementation feasibility
- Show resource requirements clearly
- Address change management

**For CEO/Board:**
- Lead with strategic alignment
- Emphasize competitive implications
- Show optionality created
- Keep financial detail in appendix

**For Technical leadership:**
- Include technical risk assessment
- Address integration complexity
- Show build vs. buy analysis
- Discuss technical debt implications
