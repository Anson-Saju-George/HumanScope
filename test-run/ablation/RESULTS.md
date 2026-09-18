# Ablation results — full six-lens skill (H) vs compact four-slot-only (C) vs ordinary editing (O)

Question: **do the six lenses earn their complexity, or is the four-slot rule doing the work?**
All three arms are Claude Opus 4.8, same brief; H and O reuse the A/B test outputs, C is newly
generated with `evals/compact-variant.md`. Blind-judged by Codex `gpt-5.6-sol` @ high in an isolated
dir (no mapping present). **Preliminary, model-judged, n=1 per topic** — same caveats as the main
results; the real answer needs the human protocol.

| Topic | Blind ranking | H (full) | C (compact) | O (ordinary) | Read |
|---|---|---|---|---|---|
| 1 · fiction | **H > C > O** | overall 5, implicit 5 | overall 4, implicit 3 | overall 2, implicit 1 | Compact already beats ordinary; the lenses add a real increment (implicitness 3→5). |
| 2 · essay | _pending_ | | | | |
| 3 · nonfiction | _pending_ | | | | |
| 4 · argument | _pending_ | | | | |

## Interim reading (after Topic 1)
- **The four-slot discipline alone carries most of the value** — compact (C) beat ordinary (O)
  decisively (4 vs 2), mostly by not stating the moral outright.
- **The six lenses are not mere scaffolding** — full skill (H) beat compact (C) on the margin that
  matters for fiction (implicitness 5 vs 3, overall 5 vs 4).
- Need Topics 2–4 before concluding: the lenses' added value may differ by genre (e.g. nonfiction,
  where the win was sourcing/restraint rather than implicitness).
