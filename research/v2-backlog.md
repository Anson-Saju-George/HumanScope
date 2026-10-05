# v2 backlog (parked 2026-10-05)

Not needed for v1.1, which is complete. Pick these up when starting v2.

## 1. Competitor review: Anthropic Directory writing skills
Seen in the claude.ai directory on 2026-10-05. Descriptions are the listings' own words; nothing
below has been tested yet.

| Listing | Their pitch | Why it matters for HumanScope |
|---|---|---|
| **ProseShape** | "Rewrite or write prose so it reads as chosen by a person, not defaulted by a model, while keeping every fact, quotation, plot event, and the writer's voice." | **Closest competitor.** Same fidelity and voice-preservation niche. Test first. |
| **writing-quality** | "Intent-aware drafting, rewriting, detect-only review, claim boundaries, and final prose validation." | Overlaps DIAGNOSE mode and claim-strength preservation. Compare the "claim boundaries" approach. |
| **humanizer** (Files & documents) | Wikipedia *Signs of AI Writing* plus "a statistical voice fingerprint built from the author's own corpus". | Voice fingerprinting from the author's own writing is an idea HumanScope lacks (we only "match supplied voice samples"). |
| **Humanizer** (Writing) | "Rewrite AI-sounding text so it reads like the writer without changing what it says." | Surface humanizer; likely the blader-style lineage we already credit. |
| **Humanize Kit** | Three skills (humanize, humanize-ig, voice-profiler); a free gateway to a paid skill lineup. | Voice-profiler again; also a packaging/marketing model (free core, paid add-ons). |
| **unslop** | "Writing guardrail against AI slop." | An always-on guardrail framing, comparable to our always-on snippet. |

**Plan (when picked up):**
1. Read each listing's SKILL.md and decide which are honest comparators (rewrite/edit skills, not
   detector evasion).
2. Run them as extra arms on the **existing frozen tasks** (write-x and the held-out set), judged
   blind with the same prompts, so the results compare like for like.
3. Decide whether voice fingerprinting (from humanizer and Humanize Kit) is worth adding, and only if
   a blind test shows it helps.
4. Credit anything adopted in the README's Related work, as with Chen.

## 2. Already planned (from the README roadmap)
- **v1.2 proposal (Astra R10, test before shipping):** drop "less AI-shaped" from the description
  (check it doesn't break skill triggering); move the authorized-transformation exception into slot 3;
  restore the full skill's protections in the always-on snippet.
- **Human evaluation:** 3-way blind, with HumanScope vs a variant with only the lenses removed vs
  competent ordinary editing ([protocol](../evals/human-eval-protocol.md)).
- Chrome extension; more non-fiction evaluation.

## 3. Publishing left to do
- **ChatGPT GPT Store:** build the GPT from [`chatgpt/README.md`](../chatgpt/README.md), run the
  6-case smoke test on the real GPT, then publish to Everyone.
- **Anthropic Directory:** submit at claude.ai/directory/manage (needs a paid plan; reviewed). The
  listings above show community writing skills are accepted.
- **README roadmap:** tick the items finished on 2026-10-05 (Claude Code plugin marketplace, ChatGPT
  packaging, GitHub release with the claude.ai ZIP).

## 4. Lessons to carry into v2 evaluation
- Give every arm the **same** instructions except the thing being tested, and tell the judge the
  truth about each arm. (The v1.0 A/B and the bare-edit arm both broke this.)
- Judge rubrics must not encode the skill's own taste (the "tidy triads as slop" problem).
- Report scores as scores ("higher fidelity scores"), not as guarantees ("keeps writing true").
- Retry usage-limited Astra calls after the reset, and inline material instead of letting it
  explore the repo.
