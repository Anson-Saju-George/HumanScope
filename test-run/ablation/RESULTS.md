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
| 3 · nonfiction | _pending_ | | | | |
| 4 · argument | _pending_ | | | | |

## Interim reading (after Topics 1–2)
- **Full skill (H) won both topics** — consistently the most restrained / highest overall.
- **The compact four-slot rule alone is INCONSISTENT** — 2nd in fiction, **last** in essay (below
  ordinary). This is the surprising, useful finding: the bare discipline ("edit only on a concrete
  failure") is too abstract on its own; it does not reliably tell the model *what to look for*.
- **Tentative implication (n=1/topic, single judge):** the six lenses appear to **earn their keep**
  by supplying the specific diagnostic targets (esp. L1 "is stated meaning defeating an inference")
  that the four-slot rule leaves unspecified. If this holds across Topics 3–4, "just ship the compact
  version" is NOT supported.
- Caveat unchanged: preliminary, model-judged, one sample per topic. Needs the human protocol.
