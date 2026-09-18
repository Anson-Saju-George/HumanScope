# Human Evaluation Protocol (the decisive test)

**Status: designed, not yet run.** This is the study that would move HumanScope from "models prefer
its output" to "humans are better served" — the single highest-value thing left to do (agreed by both
review models). It is deliberately a **3-way** comparison so it answers *two* questions at once.

## The two questions
1. **Does HumanScope beat competent ordinary editing** *for a human reader*? (efficacy)
2. **Do the six lenses earn their complexity, or is the four-slot rule doing all the work?** (ablation)

## The three arms (same input, same model, same budget)
| Arm | What the editor gets |
|---|---|
| **H — HumanScope (full)** | The full `SKILL.md` (six lenses + domain gate + four-slot rule + restraint). |
| **C — Compact** | *Only* the brief, preservation constraints, and the four-slot rule (below). **No six lenses.** |
| **O — Ordinary** | A strong, non-HumanScope instruction: "You are an excellent editor. Improve this for its reader; preserve the author's voice, meaning, and facts; change only what genuinely helps." |

> **Arm C ("Compact") spec** — the ablation control. Give the editor exactly this and nothing else:
> *"Edit the text below for its stated reader and purpose. Preserve meaning, voice, facts, and intent.
> Make a change only when you can name (1) the specific passage, (2) the intended effect, (3) a
> concrete way it currently falls short — 'it sounds AI' does not count — and (4) the smallest fix.
> If nothing clears that bar, return the text unchanged and say so."*

Run O and C from the **same model** as H, at comparable effort, with the **same brief and source
facts** available. WRITE tasks compare fresh generations; EDIT tasks compare edits of an identical draft.

## Materials
- **≥ 12 items** spanning genres: literary fiction, personal essay, explanatory nonfiction, argument,
  plus everyday (email, product update). Reuse `test-run/` topics + add new unseen ones.
- **Author brief + source facts** attached to every item (raters need them to judge fidelity).
- **≥ 4 "preservation" items that are already strong** and should be returned ~unchanged. These test
  restraint directly — the arm that mangles them loses, even if its edits read "nicer" elsewhere.

## Raters & blinding
- **Human raters** (≥ 3; ideally including a writer/editor). An LLM judge may run *in parallel* as a
  weak secondary signal, clearly labelled — it does not count as the result.
- Strip all arm identity; randomize order per item; raters never see which arm produced which text,
  nor the mapping. (Run the LLM judge in an **isolated dir** with no mapping present — the Run-4 fix.)

## What raters score (per item, blind)
Judge **reader benefit, not preferred devices** (do NOT reward implicitness for its own sake):
1. Overall: which version would you rather read / would best serve its purpose? (rank the 3)
2. Fidelity of meaning · Voice preserved · **Factual accuracy** (errors fixed, none introduced)
3. Restraint: on preservation items, did it correctly leave the text alone?
4. One-line why.

## Reading the result
- **H > O** on blind human preference *without* fidelity/voice/factual regressions → HumanScope earns
  its keep vs ordinary editing.
- **H ≈ C** → the six lenses are mostly scaffolding; **ship the compact version** and cut complexity.
- **H > C** → the lenses add real value; keep them.
- **Any arm that damages preservation items** fails regardless of its wins elsewhere.
- Report effect sizes and disagreement, not just a tally. State n and rater count honestly.

## Why this over building a scanner
A deterministic scanner (à la humanizer-stack) improves *reproducibility of counting*, not *editorial
judgment*, and risks turning the four-slot rule into a rationalization for editing conspicuous
devices. Prove reader benefit and lens-value **first**; only then consider deterministic assistance,
and only for neutral location/measurement — never severity-from-frequency or "AI scores."
