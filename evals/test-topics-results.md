# Test Results — 4-agent A/B efficacy run

> ## ⚠️ CONFOUND NOTICE (added after Astra R8 audit — read first)
> These A/B runs do **not** cleanly isolate `SKILL.md`. Two confounds, missed by the first 7 review
> rounds:
> 1. **The conditions differed by more than the skill.** The skill-arm prompts also told the agent to
>    *read the research files*, *leave meaning implicit*, and (for nonfiction) *use answer-first
>    structure, keep tidy, cite real references*. The baseline prompts requested none of that. So the
>    wins may reflect **those extra instructions + research context**, not the skill file itself.
> 2. **One judge had a circular criterion.** The essay judge was told to reward *"implicitness =
>    trusting the reader"* — exactly what the skill arm was instructed to produce — though the shared
>    brief did not require implicitness.
>
> **What still stands:** across 4 topics × 2 runtimes, a blind judge ranked the *"skill + extra
> instructions + research context"* treatment above a bare baseline in all 8 cells — an encouraging
> but **confounded** observation. It is **not** attributable to `SKILL.md` alone, and the essay result
> in particular used a treatment-favoring criterion. A confound-free re-test (identical briefs for all
> arms; judges given the brief, not the skill's aesthetic) is the fix — see v1.1 work.

Results of the live test defined in [`test-topics.md`](test-topics.md). Two runtimes (Claude Opus
4.8, Codex `gpt-5.6-sol` @ high) × two conditions (with HumanScope / baseline), scored by Claude
and by an **independent blind Codex overview** (`gpt-5.6-sol` @ high, given the four texts under
shuffled neutral labels with no idea which used the skill).

> **Status: RUN 1 COMPLETE.** n = 1 per cell — a demonstration, not statistical proof.
> **See the CONFOUND NOTICE above — the treatment is "skill + extra instructions + research context," not the skill alone.**

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

### Verdict (corrected per the confound notice above)
**The *"skill + extra instructions + research context"* treatment ranked above its bare baseline in
this run — a confounded observation, not a demonstrated `SKILL.md` effect or a demonstrated mechanism.**

- The Claude baseline (A2) ranked **last** with both evaluators; the treatment (A1) produced more
  implicit, concrete prose. But A1's prompt *told it* to leave meaning implicit and read the research
  files, and one judge *rewarded* implicitness — so this does not isolate the skill, and does not
  establish "the L1 lens works." (Rankings can't identify a mechanism.)
- **Codex (`sol`):** its baseline (B2) was already restrained, so the treatment (B1) only edged it.
- **Not shown:** these are **generation** runs, so they cannot demonstrate *voice preservation* or
  *editing restraint* (there is no pre-existing author voice to preserve, and nothing was edited).
- *Independent critique (Codex):* A1 was judged *slightly* more explicit than the two Codex pieces
  (one beat resolved an implication the images could carry), so even the implicitness push was partial.

**Bottom line:** encouraging but confounded. A clean claim needs identical briefs across arms (no
treatment-only "be implicit / cite / answer-first" reminders), judges given the brief rather than the
skill's aesthetic, and — for preservation/restraint — actual EDIT tasks. See the v1.1 eval plan.

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

**Takeaways (honest — and deliberately not overstated; see the caveats, which govern):**
- **What the data actually licenses:** across 4 prompts × 2 runtimes, a single blinded LLM judge
  ranked each HumanScope-conditioned output **above its own baseline in all 8 cells**. That is
  encouraging preliminary evidence of useful steering — nothing more.
- **What it does NOT license (per adversarial review):**
  - Not "8 independent replications" and not "8 decisive score improvements" — several *overall
    scores tied* (e.g. skill/baseline both 5 in some runs); the 8/8 is on **ranking**, not margin.
  - Rankings **cannot identify a mechanism**. The judge's *stated reasons* differed by genre
    (implicitness on fiction/essay; sourcing/restraint on nonfiction; real references on argument) —
    that is a description of the judge's rationale, **not** a demonstrated per-genre mechanism, and
    not evidence that "effect size scales with the baseline's habit."
  - These were **generation (WRITE) tests**; they do **not** test the skill's *editing restraint*
    (whether it correctly leaves strong existing text alone) — a core claim still unverified.
  - "Preserved voice" is not shown: freshly generated text can't demonstrate preservation of an
    existing author's voice.
- **The judge is itself an LLM** sharing a model family with one generator; it may favor the skill's
  aesthetics. Fact-checking (Runs 3–4) added substance, but skill outputs still contained factual
  overstatements (the contested "5%").
- **Blindness:** Runs 1–3 judges never referenced the label map and produced non-monotonic rankings,
  which is **consistent with** blindness (it does not *prove* it); Run 4 additionally used an
  isolated judge dir with no map present.
- **Bottom line:** **n = 1 per cell, single LLM judge, generation-only.** A demonstration that models
  prefer the conditioned output — NOT evidence that a human reader is better served, nor that the six
  lenses beat a compact four-slot-only version. Those are exactly what
  [`human-eval-protocol.md`](human-eval-protocol.md) is designed to test.

_Raw overviews: `research/raw-model-output/codex-blind-overview-run2.txt` … `run4.txt`._
