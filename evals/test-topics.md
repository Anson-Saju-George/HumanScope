# Test Topics — live A/B efficacy run

Candidate topics for the 4-agent efficacy test. **All four agents write the same topic** for a clean
cross-comparison. Two runtimes × two conditions:

| Agent | Runtime | HumanScope? |
|---|---|---|
| A1 | Claude Opus 4.8 | ✅ pulls skill from GitHub + applies |
| A2 | Claude Opus 4.8 | ❌ baseline |
| B1 | Codex `gpt-5.6-sol` @ high | ✅ pulls skill from GitHub + applies |
| B2 | Codex `gpt-5.6-sol` @ high | ❌ baseline |

Evaluated blind via [`rubric.md`](rubric.md), then independently overviewed by Codex.

## Topics

| # | Topic | Genre (~length) | Exact brief (identical for all 4 agents) | What it tests in HumanScope |
|---|-------|-----------------|------------------------------------------|------------------------------|
| **1** ⭐ | **Lighthouse keeper's last night** | Short **fiction** (~1,200–1,500w) | *"Write a short story about the last night of a lighthouse keeper before the light is automated. Quiet, character-driven; leave the meaning implicit."* | **Best showcase** — all six lenses engage: L1 stated-moral habit, L2 body-metaphor monotony, L3 tidy resolution, L4 disclosure order. Fiction is the paper's home domain. |
| **2** | **The last conversation** | Reflective **personal essay** (~1,200w) | *"Write a personal essay about a last conversation someone didn't realize was the last."* | Narrative nonfiction; surfaces the AI "state the lesson" + inflated-significance habits. L1/L5/L6 heavy; restraint on strong lines. |
| **3** | **1919 Boston Molasses Flood** | Explanatory **nonfiction** (~1,200–1,500w) | *"Explain the 1919 Boston Molasses Flood: what happened, why, and why it still matters."* | **Domain-gating test** — fiction lenses should switch OFF. Tests factual integrity, L5 real-referent specificity, correct restraint (no over-editing tidy prose). |
| **4** | **Should AI fiction win prizes?** | **Argumentative essay** (~1,200w) | *"Argue whether AI-generated fiction should be eligible for literary prizes."* | Tests L1 over-explaining, false-balance/both-sides filler, L5 real references, voice/POV preservation. |

## Runs completed
- **All four topics have been run** (Runs 1–4). Full analysis + blind evaluations + the 8/8
  cross-run result are in [`test-topics-results.md`](test-topics-results.md); the actual agent
  outputs, prompts, and blind overviews live in [`../test-run/`](../test-run/).
- **Fairness:** all four agents receive the *identical* brief; only A1/B1 additionally clone the
  GitHub repo and apply `SKILL.md`. Baselines write normally. Everything ran in a **local** test
  workspace — nothing installed to `~/.claude` (global).
