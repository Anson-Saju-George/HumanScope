# Ablation results — full six-lens skill (H) vs compact four-slot-only (C) vs ordinary editing (O)

Question: **do the six lenses earn their complexity, or is the four-slot rule doing the work?**
All three arms are Claude Opus 4.8, same brief; H and O reuse the A/B test outputs, C is newly
generated with `evals/compact-variant.md`. Blind-judged by Codex `gpt-5.6-sol` @ high in an isolated
dir (no mapping present). **Preliminary, model-judged, n=1 per topic** — same caveats as the main
results; the real answer needs the human protocol.

| Topic | Blind ranking | H (full) | C (compact) | O (ordinary) | Read |
|---|---|---|---|---|---|
| 1 · fiction | **H > C > O** | overall 5, implicit 5 | overall 4, implicit 3 | overall 2, implicit 1 | Compact beats ordinary; lenses add a real increment (implicitness 3→5). |
| 2 · essay | **H > O > C** | overall 5, implicit 4 | overall 3, implicit 1 | overall 4, implicit 2 | Compact ranked **last** — below ordinary; only the full skill stayed implicit. |
| 3 · nonfiction | **C > H > O** | overall 4 (occasionally overconfident) | overall 5 (best calibrated, most organized) | overall 4 | **Compact WINS**; full skill 2nd (its "reach for real references" tips into overconfidence). |
| 4 · argument | **C > H > O** | overall 4 | overall 5 (thesis/arg/voice all 5) | overall 4 | **Compact wins again**; it cited real cases (Kudan, *Thaler*) without the L5 lens. |

## Final reading (all 4 topics) — a clean narrative vs. expository split
| | Winner | Ranking |
|---|---|---|
| Fiction (narrative) | **Full skill (H)** | H > C > O |
| Personal essay (narrative) | **Full skill (H)** | H > O > C |
| Nonfiction (expository) | **Compact (C)** | C > H > O |
| Argument (expository) | **Compact (C)** | C > H > O |

**These four comparisons MOTIVATE A ROUTING HYPOTHESIS — fuller review helped narrative pieces, a
leaner review helped expository ones — but they do NOT identify the lenses' contribution.** (Astra
R8: H inherits the same extra instructions + research context as the A/B skill arm, and C omits
several other components *and* its prompt is edit-framed yet was used for generation — so "the lenses"
are not isolated. Also, none of this is human-judged.)

- It is *consistent with* the domain-gating premise (fiction-derived lenses suit narrative; the full
  apparatus read as *"occasionally overconfident"* on expository, 2nd place both times) — but a
  causal reading ("the six lenses earn their keep / don't") is **not supported** by this design.
- **Ordinary editing (O) never won** (last in 3 of 4; middle once) — so *some* disciplined
  conditioning beats none, but the *kind* should match the genre.
- **Concrete design implication (adopted, but softened per adversarial review):** choose **review
  depth by the passage's *function*** — lean review for explanatory/argumentative passages, fuller
  lens review for scene/experience-driven ones — rather than a hard genre split. Shipped as SKILL.md
  §4 "Choose the review depth by purpose." **Caveat (Astra):** the SKILL.md lean path is NOT
  literally the tested arm C (C was four-slot-only; the shipped lean path keeps substantive review of
  information, support, and placement), and O was ordinary *generation* not editing — so this is a
  design lead the ablation is *consistent with*, not a validated recipe.
- Notable: the compact arm produced real references on the argument topic *without* an explicit
  "cite real things" lens — a disciplined model does it when the genre calls for it, mild evidence
  the L5 lens isn't load-bearing outside narrative.

## Honest caveats (unchanged, governing)
n = 1 per topic, a single LLM judge (here the **generator is Claude and the judge is Codex-`sol`** —
*different* families, unlike the A/B Codex arms; corrected per Astra R8), **generation-only** (no
editing-restraint test). This is a preliminary, model-judged signal — a hypothesis-generator, not
proof. The narrative/expository split is plausible and clean but needs the human protocol
(`../../evals/human-eval-protocol.md`) and more samples to confirm.
