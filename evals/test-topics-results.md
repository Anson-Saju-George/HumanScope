# Test Results — 4-agent A/B efficacy run

Results of the live test defined in [`test-topics.md`](test-topics.md). Two runtimes (Claude Opus
4.8, Codex `gpt-5.6-sol` @ high) × two conditions (with HumanScope / baseline), scored by Claude
and by an **independent blind Codex overview** (`gpt-5.6-sol` @ high, given the four texts under
shuffled neutral labels with no idea which used the skill).

> **Status: RUN 1 COMPLETE.** n = 1 per cell — a demonstration, not statistical proof.

## Run 1 — Topic #1 "Lighthouse keeper's last night" (short fiction)

**Brief (identical for all 4):** *"Write a short story about the last night of a lighthouse keeper
before the light is automated. Quiet, character-driven; leave the meaning implicit."*

Both skill agents (A1, B1) cloned the skill from GitHub locally (`git clone …/HumanScope.git`) and
applied `SKILL.md` — no global install.

| Agent | Runtime | HumanScope | Words | Output |
|---|---|---|---|---|
| A1 | Claude Opus 4.8 | ✅ | 1,378 | `_testrun/A1-claude-skill/story.md` |
| A2 | Claude Opus 4.8 | ❌ baseline | 1,354 | `_testrun/A2-claude-base/story.md` |
| B1 | Codex sol@high | ✅ | 1,464 | `_testrun/B1-codex-skill/story.md` |
| B2 | Codex sol@high | ❌ baseline | 1,497 | `_testrun/B2-codex-base/story.md` |

### Claude's evaluation (rubric dimensions, 1–5)
| Agent | Implicit meaning (L1) | Presentation (L2) | Voice/specificity | Overall |
|---|---|---|---|---|
| A1 Claude +skill | 5 | 5 | 5 | **5** |
| A2 Claude baseline | 2 | 4 | 4 | **3.5** |
| B1 Codex +skill | 5 | 5 | 4.5 | **4.5** |
| B2 Codex baseline | 4 | 4.5 | 4.5 | **4.5** |

### Codex's independent BLIND overview (shuffled; decoded here)
Ranking (blind): **B1 (+skill) > B2 (baseline) > A1 (+skill) > A2 (baseline).**

| Blind → actual | Implicit | Economy | Voice | Overall | Codex's evidence |
|---|---|---|---|---|---|
| story-3 → **B1 Codex +skill** | 5 | 5 | 5 | **5** | *"'He took out the cup with the blue band' is a precise, restrained action that releases the story's accumulated grief."* |
| story-1 → **B2 Codex baseline** | 5 | 4 | 5 | **5** | *"'…worn to the shape of fingers that were not his' lets loss inhabit an object without explanation."* |
| story-2 → **A1 Claude +skill** | 3 | 4 | 5 | **4** | *"habit carries the emotion, though later commentary interprets it."* |
| story-4 → **A2 Claude baseline** | **1** | **2** | 4 | **3** | *"'…the caring was to be taken out like a worn part and thrown away' directly announces the theme already established by the scene."* |

**Codex, unprompted, flagged A2 (Claude baseline) as by far the most theme-spelling** — *"Story 4
overwhelmingly [uses narrated interiority], with repeated explanatory body metaphors"* — and it was
**last** in both evaluations.

### Verdict
**HumanScope improved each runtime relative to its OWN baseline — and the effect size depends on how
strong that runtime's over-explaining default is.**

- **Claude: large, clear effect.** Both evaluators rank the Claude baseline (A2) **worst**, precisely
  because it repeatedly *states* its theme ("that was the whole of it… he would be the poorer… the
  world did not owe him his usefulness"). The skill (A1) moved Claude off that default to implicit,
  concrete storytelling. This is a clean, independently-confirmed demonstration of the L1 lens.
- **Codex (`sol@high`): small effect.** Its baseline (B2) was *already* restrained and object-driven,
  so the skill (B1) only edged it — though Codex's own blind ranking did put **B1 (+skill) #1**.
- **No voice-flattening / no over-editing** in either skill output — both kept distinct, concrete
  voices (regression check: passed).
- **Honest caveat / independent critique:** Codex judged A1 (Claude +skill) *slightly* more explicit
  than the two Codex pieces (one beat — *"he had chosen the rock over her plainly enough"* — resolves
  an implication the images could carry). So the skill reduced Claude's over-explaining a lot but not
  to zero, and did not make Claude's piece beat a strong Codex baseline. Fair.

**Bottom line:** the skill did exactly what it claims — reduced compositional over-determination and
preserved voice — with the biggest, most legible gain where the baseline habit was strongest (Claude).
n = 1 per cell; a real efficacy study needs the full blind U/O/H protocol in `rubric.md` with human
raters and more cases (Topic #4 reserved).

_Raw Codex overview: `research/raw-model-output/codex-blind-overview-run1.txt`._
