# HumanScope

> **Preserve the author. Fix the structure.** — research-grounded compositional editing for AI prose.

A research-informed writing & editing skill that works on the **composition** of prose — how
meaning, structure, presentation, information order, references, and reader-stance are handled —
rather than on surface tells. It diagnoses systematic compositional habits common in AI drafts and
fixes them **only where a specific, concrete improvement serves the reader**, while preserving the
author's voice, meaning, facts, and intent.

It is **not** a "ban em-dashes / avoid 'delve'" humanizer, and **not** an AI-detector-evasion tool.
It never optimizes for a "% human" score.

## Why it's different
Most humanizers edit the *surface* (word bans, em-dash rules, formatting). HumanScope targets the
**discourse level** — the layer a peer-reviewed study found separates AI from published human
fiction using features classified as narrative rather than stylistic. It adds research-informed
narrative diagnosis, gated by genre and purpose, with a built-in brake against turning a statistical
difference into an edit.

> **Status:** HumanScope is an *experimental editorial workflow*. Independent peer review has checked
> its specification and evidence; improved reader outcomes over ordinary editing have **not yet been
> demonstrated** (see `evals/`).

## Research foundation (and its honest limits)
Built on **StoryScope** (Russell, Rajendhran, Pham, Iyyer, Wieting — *Investigating idiosyncrasies
in AI fiction*, COLM 2026). Critical caveats, baked into the skill:
- The study is **fiction-only** (published anthology short stories). Non-fiction use is an editorial
  judgment, not a tested finding — so fiction lenses are **domain-gated**, and several apply
  differently (or not at all) outside fiction, decided by the passage's purpose rather than a
  genre-wide rule.
- Its features are **descriptive** differences between sources — **not** proven quality rules. "More
  human-like" is never, by itself, a reason to edit.
- Full scope boundaries: [`research/limitations.md`](research/limitations.md).

## How it works — six lenses, as questions
HumanScope diagnoses through six lenses, each an **open question gated by purpose**, never a
direction to push:
1. **Explanation & interpretation** · 2. **Presentation** · 3. **Causality & closure** ·
4. **Information order** · 5. **Referential grounding** · 6. **Reader relationship**

Every edit must fill four slots — *evidence → intended effect → present failure → smallest useful
change* — and **"no change needed" is always a valid outcome**. Modes: **WRITE**, **EDIT**,
**DIAGNOSE** (and light vs. deep intensity). See [`SKILL.md`](SKILL.md).

## Use it
This is a Claude skill. The runtime spec is [`SKILL.md`](SKILL.md) at the repo root.
- **Claude Code / plugins:** place this directory where your skills live, or install per your skill
  loader; invoke by asking to write/rewrite/tighten/diagnose text and naming HumanScope.
- **Claude.ai:** upload as a skill (SKILL.md + this folder).
Examples: [`examples/`](examples/). Success criteria & tests: [`evals/`](evals/).

## Supported writing
Directly grounded for **literary/narrative fiction**. Usable, with domain-gating, for essays,
reports, explanatory/technical writing, marketing, email, and docs — where several lenses change or
switch off. It will decline to degrade quality, fabricate real-world facts, or chase a detector.

## Philosophy
> A research-informed editor that notices systematic compositional habits of LLMs and selectively
> corrects them while preserving the author's intent — **not** a bag of tricks for making text
> "sound human." Preserve first, diagnose second, intervene least.

## Provenance
Everything under [`research/`](research/) is the full build record: the paper extraction
(`paper-notes.md`), the synthesis (`structural-patterns.md`), the feature→lens map
(`evidence-map.md`), secondary-source analysis, rejected folklore (`rejected-ideas.md`), limits, and
the complete peer/adversarial-review log (`adversarial-review.md`) — this skill was pressure-tested
across four review rounds by independent models (GPT Sol and GPT Astra). Start at
[`research/roadmap-and-state.md`](research/roadmap-and-state.md).
