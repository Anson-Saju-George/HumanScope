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

---

## Run 2 — Topic #2 "A last conversation someone didn't realize was the last" (personal essay)

Same 4-agent matrix; skill agents pulled the skill from GitHub. Blind Codex overview (shuffled).

**Blind ranking:** `B1 (Codex+skill) > A1 (Claude+skill) > A2 (Claude base) > B2 (Codex base)`.

| Blind → actual | Implicit | Overall | Codex's note |
|---|---|---|---|
| story-2 → **B1 Codex +skill** | 5 | **5** | *"Then I added one more line: BLUE CUP." — meaning released by an object.* |
| story-3 → **A1 Claude +skill** | 3 | **4** | *"I have the ladder." — refuses the granite-words catharsis.* |
| story-1 → **A2 Claude base** | **1** | 3 | flagged most-spelled-out: *"the lesson I was too busy to learn: that attention is the whole of it."* |
| story-4 → **B2 Codex base** | **1** | 3 | flagged most-spelled-out: *"It meant… let me offer this small protection."* |

**Result: the cleanest run yet.** Both **skill essays ranked #1 and #2**; both **baselines ranked #3 and #4**, and Codex — blind — flagged **both baselines** as the ones that state their lesson (implicitness 1/5 each). The personal-essay form pulls *both* models toward an explicit moral; the skill pulled *both* back to implicit, object-carried meaning. Skill beat its own baseline for **both** runtimes.

## Run 3 — Topic #3 "1919 Boston Molasses Flood" (explanatory nonfiction — DOMAIN-GATE TEST)

For nonfiction the criteria change: clarity/answer-first, **factual specificity & sourcing**, explanatory quality. The blind Codex judge **fact-checked via web search** before scoring.

**Blind ranking:** `B1 (Codex+skill) > B2 (Codex base) > A1 (Claude+skill) > A2 (Claude base)`.

| Blind → actual | Facts/sourcing | Overall | Fact-check flag |
|---|---|---|---|
| story-3 → **B1 Codex +skill** | 5 | **5** | none — *"best sourcing, most precise causal distinctions, appropriately qualifies disputed mechanisms."* |
| story-1 → **B2 Codex base** | 4 | **5** | clean specifics, but **no citations** |
| story-2 → **A1 Claude +skill** | 3 | **4** | overstated figures: "thousands of witnesses" (≈920), "25–40 ft" (usual 25) |
| story-4 → **A2 Claude base** | 3 | **3** | **physics error** (conflates non-Newtonian w/ temperature-viscosity) + sensationalism + over-confident trigger |

**Domain-gate: PASSED.** Both skill pieces stayed **tidy, answer-first, explicit about significance, real-sourced** — no fiction-lens contamination (no imposed ambiguity/implicitness). The skill **improved factual discipline** (Codex+skill was the only piece with a clean fact-check; Claude+skill outranked the Claude baseline, whose physics error was the most serious flaw). Honest caveat: the skill helped but did **not** guarantee accuracy — A1 (skill) still overstated a couple of figures. Neither model's baseline was error-free.

---

## Run 4 — Topic #4 "Should AI-generated fiction be eligible for literary prizes?" (argumentative essay)

Same matrix. Blind overview run in an **isolated judge dir** (only the shuffled stories + prompt —
the label→agent map was NOT present; methodology hardened after Run 4's first attempt saw the tree)
and it **web-fact-checked** the essays' references.

**Blind ranking:** `A1 (Claude+skill) > B1 (Codex+skill) > B2 (Codex base) > A2 (Claude base)`.

| Blind → actual | Argument | Overall | Judge's note |
|---|---|---|---|
| story-2 → **A1 Claude +skill** | 4 | **5** | *"Best literary essay: decisive, memorable, exceptionally persuasive."* (minor: overstated the contested Kudan "5%") |
| story-3 → **B1 Codex +skill** | 5 | **5** | *"Most rigorous and policy-ready; excellent evidence and counterargument."* |
| story-1 → **B2 Codex base** | 4 | **4** | *"nuanced and comprehensive… but long, generic, and short on real examples."* |
| story-4 → **A2 Claude base** | 3 | **3** | *"forceful and quotable, but repetitive, analogy-heavy, materially under-evidenced"* + an internal contradiction |

**Result: skill on top again — both skill essays #1–2, both baselines #3–4.** No false-balance in
any of the four, so here the skill's edge was **concrete, real references (L5) + voice**: both skill
versions cited real cases (Rie Kudan's Akutagawa win, *Thaler v. Perlmutter* / the U.S. Copyright
Office 2025 report, *Clarkesworld*'s 500 AI submissions, Australia's PM Literary Awards, the
Children's Booker rule — B1 even added a References section), while both baselines argued well but
**abstractly, with no named cases**. Honest caveat: reaching for real references introduced a small
factual risk (both skill essays repeated a contested "5%" figure), though the judge found **no
fabricated references** and the skill versions hedged ("reportedly").

## Cross-run summary (4 topics × 2 runtimes × skill/baseline)

**Within every runtime, on every topic, the HumanScope version outranked its own baseline in the
blind judge's ranking — 8 / 8 cells.**

| Run (topic) | Blind ranking | Claude: skill vs base | Codex: skill vs base |
|---|---|---|---|
| 1 · fiction | B1 > B2 > A1 > A2 | A1 > A2 ✓ | B1 > B2 ✓ |
| 2 · essay | B1 > A1 > A2 > B2 | A1 > A2 ✓ | B1 > B2 ✓ |
| 3 · nonfiction | B1 > B2 > A1 > A2 | A1 > A2 ✓ | B1 > B2 ✓ |
| 4 · argument | A1 > B1 > B2 > A2 | A1 > A2 ✓ | B1 > B2 ✓ |

**Takeaways (honest):**
- **Consistent within-runtime benefit**, blind-judged, across fiction, essay, nonfiction, and
  argument — **8/8 cells**.
- **The skill's *mechanism* changes by genre**, which is the encouraging part (it's not one trick):
  - *Fiction / personal essay* → **implicitness**: it stops the model stating the moral. Both
    baselines in the essay run were flagged for spelling out the lesson.
  - *Explanatory nonfiction* → **restraint + factual/sourcing discipline**; the **domain gate held**
    (it did not "humanize" tidy prose). Codex+skill was the only fully clean piece.
  - *Argument* → **concrete real references (L5) + voice**; both baselines were "generic / under-
    evidenced," both skill essays cited real cases.
- **Effect size scales with the baseline's habit** — largest where the model's default was weakest
  (Claude's over-explaining on fiction/essay; the abstract/under-evidenced Claude argument baseline,
  which ranked last in Run 4).
- **Codex `gpt-5.6-sol`+skill ranked #1 in three of four runs; Claude+skill took #1 in Run 4.**
- **Honest counter-signals:** reaching for real references (Run 4) introduced minor factual
  overstatements in the skill essays (a contested "5%" figure) — grounded but not perfectly precise;
  and in nonfiction the skill improved but did not guarantee accuracy.
- **Methodology note:** Runs 1–3 judges never referenced the label map (verified) and produced
  non-monotonic rankings, so blindness held; Run 4 was additionally run in an **isolated judge dir**
  with the map absent, and the judge web-fact-checked. Still **n = 1 per cell, single LLM judge** — a
  demonstration, not a statistical or human-rated study. See `rubric.md` for the intended full protocol.

_Raw overviews: `research/raw-model-output/codex-blind-overview-run2.txt` … `run4.txt`._
