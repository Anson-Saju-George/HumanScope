# Ablation — does the compact four-slot rule match the full six-lens skill?

Per topic, three arms (all Claude Opus 4.8, same brief), blind-judged:
- **H (full skill):** reuses the A/B test's skill output (`../run*/A1-claude-skill/story.md`).
- **O (ordinary):** reuses the A/B test's baseline output (`../run*/A2-claude-base/story.md`).
- **C (compact):** four-slot rule + preservation only, NO six lenses (`evals/compact-variant.md`).

If H ≈ C, the six lenses are mostly scaffolding. Paced one topic/hour. Model-judged, preliminary
(same caveats as `../../evals/test-topics-results.md`). The real test needs humans
(`../../evals/human-eval-protocol.md`).
