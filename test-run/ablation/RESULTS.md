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
| 4 · argument | _pending_ | | | | |

## Interim reading (after Topics 1–3) — the design's domain-gate premise is showing up
- **Fiction (H>C>O)** and **essay (H>O>C)** → the full six lenses win: narrative genres are where the
  lenses have real work, and the bare four-slot rule is inconsistent there (last on the essay).
- **Nonfiction (C>H>O)** → the **compact version wins**; the full skill comes 2nd and reads as
  "occasionally overconfident." The fiction-derived lenses add little here (they're gated off anyway),
  and the leaner discipline avoids the full skill's slight overreach.
- **This is the honest, useful headline:** *the six lenses earn their keep for narrative/fiction, but
  for tidy nonfiction the compact four-slot discipline matches or beats them.* That **validates the
  domain-gating design** — and hints the nonfiction path could be simplified toward the compact rule.
- **Ordinary editing (O) never won** (last in fiction & nonfiction, middle in essay) — so *some*
  disciplined conditioning helps regardless.
- Caveat unchanged: preliminary, model-judged, one sample per topic. The human protocol is the real test.
