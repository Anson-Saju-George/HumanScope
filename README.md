<div align="center">

<img src="assets/banner.svg" alt="HumanScope — preserve the author, rethink the structure" width="100%">

# HumanScope

A research-informed writing skill for composition, clarity, and author intent.

[![Version: 1.1.1](https://img.shields.io/badge/version-1.1.1-blue)](CHANGELOG.md)
[![Status: experimental](https://img.shields.io/badge/status-experimental-orange)](#evaluation)
[![Research: StoryScope](https://img.shields.io/badge/research-StoryScope-blue)](#research-and-limits)
[![Format: Claude skill](https://img.shields.io/badge/format-Claude%20skill-8A2BE2)](#install)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

[Install](#install) · [ChatGPT](chatgpt/README.md) · [Examples](examples/examples.md) · [Skill](SKILL.md) · [Evaluation](#evaluation)

</div>

---

HumanScope reviews how a piece is composed: what it explains, how it presents experience,
where it places information, and how its parts work together. It proposes changes only when
they serve the reader and the author's purpose. **Leaving effective writing alone is a valid
outcome.**

There are no word bans, em-dash rules, or “% human” targets. HumanScope is an experimental
editorial workflow, not an AI-detector-evasion tool.

## Why I built this

It started with a YouTube video: an Indian creator walking through AI tools, humanizer
workflows, and a research paper called **StoryScope**. I wanted to understand what remained
after the familiar advice to remove em-dashes or avoid particular words.

I read the paper alongside humanizer skills, Wikipedia's *Signs of AI Writing*, and related
blogs. StoryScope offered a different angle: narrative choices can distinguish AI-generated
fiction from published human fiction even when stylistic features are excluded from the
classifier. That suggested questions about composition worth testing as editorial prompts.

HumanScope is my attempt to explore those questions without treating a statistical
human/AI difference as a reason to change someone's writing.

## What it does

| Mode | Use it to | Expected output |
| --- | --- | --- |
| **WRITE** | Draft from a brief, audience, and constraints | Finished prose |
| **EDIT** | Revise existing text at a light or deep level | Revised prose, or unchanged text when appropriate |
| **DIAGNOSE** | Examine structural problems before revising | Evidence, intended effect, problem, and suggested change |

The skill prioritizes author intent, factual accuracy, and minimum effective intervention.
Fictional invention is allowed within the brief; invented material must not be presented as
real evidence, testimony, or citations.

## How it works

Every proposed edit must answer four questions:

1. **Evidence:** Which passage, relationship, or omission supports the finding?
2. **Intended effect:** What should this reader understand or experience?
3. **Present failure:** How does the current text fall short of that purpose?
4. **Smallest useful change:** What would address the problem while preserving the piece?

“It sounds like AI” is not an acceptable failure. This check is a restraint on editing,
not a guarantee of good judgment. For an authorized transformation (summarize, change register,
rewrite), the bar is the requested target rather than a defect in the original.

### Six lenses

| Lens | Editorial question |
| --- | --- |
| Explanation and interpretation | Does the amount of stated meaning fit the reader's needs? |
| Presentation | Do description, emotion, interiority, and dialogue serve the passage? |
| Causality and closure | Are connections supported, and does the degree of closure fit? |
| Information order | Does placement help the intended understanding, pace, or surprise? |
| Referential grounding | Are references relevant and factual claims supported where needed? |
| Reader relationship | Does the writer's or narrator's stance fit the intended audience? |

These are questions, not preferred directions. A report may need explicit conclusions;
a story may benefit from either closure or ambiguity. Apply each lens to the passage's
purpose. See the [runtime instructions](SKILL.md) and [worked examples](examples/examples.md).

## Install

### Claude Code

With Git installed, run this from the project where you want to use HumanScope:

```bash
git clone https://github.com/Anson-Saju-George/HumanScope.git .claude/skills/humanscope
```

To pin this release, add `--branch v1.1.1`. This installs a project skill at
`.claude/skills/humanscope/SKILL.md`. In Claude Code, invoke it
with `/humanscope` and your request. See the
[official Claude Code skill guide](https://code.claude.com/docs/en/skills) for personal
installation and other loading options.

```text
/humanscope Light-edit this email for clarity. Keep my voice and all factual details.

/humanscope Diagnose the ending of this story. Suggest changes, but do not rewrite it.

/humanscope Write a product update from these facts. Audience: existing customers.
```

**Optional always-on mode:** to apply the core writing rules without typing `/humanscope`, paste
the block in [`always-on/CLAUDE-snippet.md`](always-on/CLAUDE-snippet.md) into your project's
`CLAUDE.md` (or `~/.claude/CLAUDE.md`). It covers reader-facing prose only, not code or chat.
When supplied as project instructions in a small blind test, it ranked above bare prompts on web
page copy and a blog post. Automatic loading and continued application were not tested.

**Optional author-controlled workflow:** request DIAGNOSE first, choose the suggested changes you want, then request EDIT implementing those choices. Direct editing remains available without a separate approval step when the changes are already authorized.

### Claude.ai

Download or clone the repository, package the skill folder as a ZIP containing `SKILL.md`
and its supporting files, and upload it through Claude's custom-skills interface. Follow the
[official upload instructions](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
for the required archive layout and account settings.

### ChatGPT

ChatGPT can't install skills from GitHub, but you can set HumanScope up once as a **Custom GPT** or a
**Project**: paste a short instructions block and attach `SKILL.md`. Step-by-step:
**[chatgpt/README.md](chatgpt/README.md)**. Output quality in ChatGPT hasn't been evaluated; all
tests were run on Claude.

### Other assistants

`SKILL.md` is plain instructions, so it can be supplied to other assistants: upload the file and
ask the assistant to apply HumanScope for the rest of the conversation. Reliable application and
output quality there remain unestablished.

## Research and limits

HumanScope is informed by **StoryScope: Investigating idiosyncrasies in AI fiction**
(Russell, Rajendhran, Pham, Iyyer, and Wieting; COLM 2026).

- **The study concerns fiction.** It compares published anthology stories with AI stories
  generated from reverse-engineered prompts. Nonfiction applications are editorial judgments.
- **Authorship differences are not quality rules.** The study does not show that moving a
  feature toward its human-associated value improves a piece.
- **The six lenses are editorial groupings.** Their interventions are not validated by the
  paper. They require evaluation against the author's purpose and reader outcomes.

See the [paper notes](research/paper-notes.md), [evidence map](research/evidence-map.md), and
[scope limitations](research/limitations.md).

## Evaluation

All results come from **blind** model judging: outputs shown as shuffled letters, judges never saw
the skill, and the key was opened only after scoring. Full scorecard, numbers, and limits:
**[evals/FINAL-RESULTS.md](evals/FINAL-RESULTS.md)**.

| Comparison | Result |
| --- | --- |
| Task + skill vs task only, on writing prompts (web page copy, blog, email, story) | The judge ranked **every full-skill draft above every bare draft** within each task ([results](test-run/write-x/RESULTS.md)) |
| One casually worded request, with vs without `/humanscope` | Without: =6th of 8. With: **1st, 5/5/5** (one run each) |
| Editing, vs a carefully written "excellent editor" prompt | **No demonstrated advantage:** 1 win, 2 losses, 3 ties per judge, with the pre-R9 skill ([results](test-run/fair-retest/RESULTS.md)) |
| The six lenses | **Untested.** The compact comparison changed more than the lenses |
| Alex Chen's *Human Scope* | The pre-R9 skill better preserved meaning in the two fiction cases tested; not a general result |
| Patched v1.1 vs pre-patch, on new material | Patched preferred on 4 tasks, pre-patch on 1, tied on 4; **not regression-free** ([held-out](evals/heldout-v1.1-run/)) |

**What the writing results show.** Bare output was rarely "delve / tapestry" slop. Its weak point was
**owner-specific details nobody supplied**: recipes, store policies, migration histories, team rules.
Across the three non-fiction tasks, **every full-skill draft received a higher fidelity score than
every bare draft**. That isn't a guarantee: only 2 of 10 full-skill drafts scored 5/5, so check facts
before publishing. The comparisons test the whole package; which instructions cause the difference is
not identified. The cost is plainer copy, and sometimes `[placeholders]` where a fact is missing.

**Limits.** Small samples (1–3 runs per arm), model judges only (OpenAI), and all writing by Claude
inside Claude Code. No human-reader evaluation yet. One known failure: in a preservation-focused
fiction edit, the pre-R9 skill removed a character's stated motive. A bare "can you edit this" arm was
**misjudged** (its judge was told it had a brief it never received), so it is excluded from the
results and kept as a [documented error](test-run/fair-retest/RESULTS.md#re-judge-with-a-bare-edit-arm).
An earlier v1.0 A/B was also **confounded** and is kept only as a
[corrected historical record](evals/test-topics-results.md).

## Related work / prior art

HumanScope is **not the first** skill to build on StoryScope, and it stands on a shared lineage —
credit where due:

- **[Human Scope](https://chen.media/guides/human-scope-storyscope-claude-writing-skill)** by Alex
  Chen (Chen Media), the companion skill to his SCOPE reel. It is prior art we found during
  development: a concise, fiction-focused StoryScope checklist. HumanScope is a
  separate, unaffiliated implementation informed by the same paper. The v1.1 knowledge-boundary
  check draws on Chen's editorial checklist.
- **[NulightJens/humanizer-stack](https://github.com/NulightJens/humanizer-stack)** — a two-pass
  (surface + structural) Claude-skill pipeline grounded in StoryScope, with **deterministic Python
  scanners**. Ahead of us on reproducibility and inspectability.
- **[ccf/humanize](https://github.com/ccf/humanize)** — a StoryScope-grounded skill drawing on ~13
  peer-reviewed sources, multi-platform, and explicit about avoiding authorship inference.
- **[blader/humanizer](https://github.com/blader/humanizer)** and
  **[Matt-Payne/content-humanizer](https://github.com/Matt-Payne/content-humanizer)** — the
  surface-level humanizers our secondary-source analysis studied.

**What HumanScope contributes is a *discipline*, not a first-mover claim:** every edit must clear the
four-slot test (evidence → intended effect → present failure → smallest change), "AI-like" is not an
allowed reason to edit, "no change" is valid when the brief is already satisfied, and lenses are gated by genre and purpose — with
an explicit refusal to optimize for detectors. In blind model-judged tests, that discipline clearly beat bare prompts and tied a
well-instructed ordinary editor. Whether it reads better *to people* is the open question.

## 🗺️ Roadmap

- [x] Experimental skill with six conditional lenses
- [x] Worked examples, evaluation rubric, and exploratory model-judged runs
- [x] [Prior-art acknowledgment](#related-work--prior-art)
- [x] Matched-brief blind comparisons, bare-prompt tests, and held-out validation ([summary](evals/FINAL-RESULTS.md))
- [x] Opt-in always-on mode ([`always-on/CLAUDE-snippet.md`](always-on/CLAUDE-snippet.md))
- [ ] **Decisive test:** 3-way blind *human* eval — HumanScope vs. a matched variant removing only
  the lenses vs. competent ordinary editing ([protocol](evals/human-eval-protocol.md)); answers both "beats
  ordinary editing?" and "what do the lenses add?"
- [ ] **Proposed v1.2 (from Astra R10; test before shipping):** drop "less AI-shaped" from the skill
  description (may change when the skill triggers); move the authorized-transformation exception into
  slot 3 of the four-slot rule; restore the full skill's protections in the always-on snippet
  (fiction EDIT limits, function-based phrasing, deletion check, style constraints)
- [ ] Chrome extension for editing text in context
- [ ] Further evaluation and guidance for nonfiction genres

The Chrome extension is planned; it is not included in the current package.

## Project files

| Path | Contents |
| --- | --- |
| [SKILL.md](SKILL.md) | Runtime instructions |
| [examples/](examples/examples.md) | Worked edits and preservation cases |
| [evals/FINAL-RESULTS.md](evals/FINAL-RESULTS.md) | One-page summary of every blind test |
| [evals/](evals/rubric.md) | Evaluation protocol, cases, and recorded runs |
| [always-on/](always-on/CLAUDE-snippet.md) | Optional CLAUDE.md block for always-on use |
| [chatgpt/](chatgpt/README.md) | Setup for ChatGPT (Custom GPT or Project) |
| [CHANGELOG.md](CHANGELOG.md) | Release history |
| [research/](research/roadmap-and-state.md) | Research notes, decisions, and project state |
| [Review record](research/adversarial-review.md) | Adversarial reviews by GPT Sol and GPT Astra |

Model reviews checked the specification and identified problems in the evidence and proposed
rules. They do not substitute for independent reader evaluation.

## License

HumanScope's original code and documentation are available under the [MIT License](LICENSE).
Third-party papers, videos, and blog source materials are not distributed in this repository.

---

**Preserve what works. Change what the piece needs.**
