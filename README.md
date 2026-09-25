<div align="center">

<img src="assets/banner.svg" alt="HumanScope — preserve the author, rethink the structure" width="100%">

# HumanScope

A research-informed writing skill for composition, clarity, and author intent.

[![Status: experimental](https://img.shields.io/badge/status-experimental-orange)](#evaluation)
[![Research: StoryScope](https://img.shields.io/badge/research-StoryScope-blue)](#research-and-limits)
[![Format: Claude skill](https://img.shields.io/badge/format-Claude%20skill-8A2BE2)](#install)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

[Install](#install) · [Examples](examples/examples.md) · [Skill](SKILL.md) · [Evaluation](#evaluation)

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
not a guarantee of good judgment.

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

This installs a project skill at `.claude/skills/humanscope/SKILL.md`. In Claude Code, invoke it
with `/humanscope` and your request. See the
[official Claude Code skill guide](https://code.claude.com/docs/en/skills) for personal
installation and other loading options.

```text
/humanscope Light-edit this email for clarity. Keep my voice and all factual details.

/humanscope Diagnose the ending of this story. Suggest changes, but do not rewrite it.

/humanscope Write a product update from these facts. Audience: existing customers.
```

### Claude.ai

Download or clone the repository, package the skill folder as a ZIP containing `SKILL.md`
and its supporting files, and upload it through Claude's custom-skills interface. Follow the
[official upload instructions](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)
for the required archive layout and account settings.

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

**Status: experimental.** Better reader outcomes than ordinary editing have not been
established. Research grounding is **fiction-specific**; all testing so far is on literary/
narrative and short expository prose. **Performance on academic papers, structured documents,
websites/marketing, and notes has not been established** — the skill applies careful,
reader-focused editing there (with guards for structure, claim-strength, and format), but its
distinctive value on those genres is untested.

One exploratory generation run compared four lighthouse-keeper stories: two models, each
with and without HumanScope. A blinded model judge ranked the outputs **skill > baseline >
skill > baseline** across the two models. **This comparison is confounded** (a later audit found
the skill arms also received extra instructions — read the research files, be implicit, cite,
answer-first — that the baselines did not, and one judge rewarded the skill's own aesthetic), so it
does **not** isolate `SKILL.md`, and it is one sample per condition. See the
[confound notice and corrected results](evals/test-topics-results.md).

**Latest evaluation: a six-case exploratory EDIT comparison** ([results](test-run/fair-retest/RESULTS.md)).
With one Claude-generated output per condition, two independently run, blinded OpenAI judges ranked
HumanScope above ordinary editing in one case, below it in two, and tied in three; the same counts
held against a compact prompt. Combined scores were equal or close, but this does not establish
equivalence. HumanScope left an unresolved technical specification as written, where the ordinary and compact
edits changed its requirements, but it lost information in a marketing passage and a fiction passage.
**Its contribution beyond competent ordinary editing remains unestablished.** The compact
comparison did not isolate the six lenses. HumanScope preserved the brief better than Chen's
*Human Scope* in the two fiction cases tested; that small comparison does not establish general
superiority. v1.1 patches the observed information-loss failures, and those patches are untested until
the [held-out suite](evals/heldout-v1.1.md) runs.

Earlier testing was: **exploratory generation comparisons** (the confounded
A/B above), a **generation ablation** (full vs compact vs ordinary — motivates the review-depth
routing, does not isolate the lenses), and **preservation smoke tests** across genres/models (the
guards held on the artifacts tried, with no guardless control). The intended rigorous design —
untouched vs ordinary vs HumanScope, independent judges, constraint/task/preference scored
separately — is specified in the [rubric](evals/rubric.md) and [human-eval protocol](evals/human-eval-protocol.md);
also [test cases](evals/cases.md), [smoke test](evals/smoke-test.md).

## Related work / prior art

HumanScope is **not the first** skill to build on StoryScope, and it stands on a shared lineage —
credit where due:

- **[Human Scope](https://chen.media/guides/human-scope-storyscope-claude-writing-skill)** by Alex
  Chen (Chen Media). Chen's SCOPE reel prompted this project, and his companion skill is prior art
  we found during development. It is a concise, fiction-focused StoryScope checklist. HumanScope is a
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
allowed reason to edit, "no change" is always valid, and lenses are gated by genre and purpose — with
an explicit refusal to optimize for detectors. Whether that discipline produces *better reading for a
human* than a well-instructed ordinary edit is the open question our evaluation is built to answer.

## 🗺️ Roadmap

- [x] Experimental skill with six conditional lenses
- [x] Worked examples, evaluation rubric, and exploratory model-judged runs
- [x] [Prior-art acknowledgment](#related-work--prior-art)
- [ ] **Decisive test:** 3-way blind *human* eval — HumanScope vs. a compact four-slot-only variant
  vs. competent ordinary editing ([protocol](evals/human-eval-protocol.md)); answers both "beats
  ordinary editing?" and "do the six lenses earn their complexity?"
- [ ] Chrome extension for editing text in context
- [ ] Further evaluation and guidance for nonfiction genres

The Chrome extension is planned; it is not included in the current package.

## Project files

| Path | Contents |
| --- | --- |
| [SKILL.md](SKILL.md) | Runtime instructions |
| [examples/](examples/examples.md) | Worked edits and preservation cases |
| [evals/](evals/rubric.md) | Evaluation protocol, cases, and recorded runs |
| [research/](research/roadmap-and-state.md) | Research notes, decisions, and project state |
| [Review record](research/adversarial-review.md) | Adversarial reviews by GPT Sol and GPT Astra |

Model reviews checked the specification and identified problems in the evidence and proposed
rules. They do not substitute for independent reader evaluation.

## License

HumanScope's original code and documentation are available under the [MIT License](LICENSE).
Third-party papers, videos, and blog source materials are not distributed in this repository.

---

**Preserve what works. Change what the piece needs.**
