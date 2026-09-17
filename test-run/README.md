# test-run — HumanScope A/B efficacy tests

Real, reproducible A/B runs testing whether pulling and applying HumanScope actually improves a
model's writing versus the same model's un-helped baseline. Summarized in
[`../evals/test-topics-results.md`](../evals/test-topics-results.md); topics defined in
[`../evals/test-topics.md`](../evals/test-topics.md).

## Design
For each topic, four agents write the **same brief** — two runtimes × two conditions:

| Agent | Runtime | Condition |
|---|---|---|
| `A1-claude-skill` | Claude Opus 4.8 | pulled the skill from GitHub + applied it |
| `A2-claude-base`  | Claude Opus 4.8 | baseline (no skill) |
| `B1-codex-skill`  | Codex `gpt-5.6-sol` @ high | pulled the skill from GitHub + applied it |
| `B2-codex-base`   | Codex `gpt-5.6-sol` @ high | baseline (no skill) |

Only A1/B1 clone the repo and apply `SKILL.md`; baselines get the bare brief only. Every agent's
prompt is saved (`A1-prompt.txt` … `B2-prompt.txt`) and its output is `story.md`. Each run's
`eval-blind/` holds the four stories under shuffled neutral labels, the judge prompt, the private
label→agent mapping, and the blind Codex overview (`overview-out.txt`).

## Runs
| Dir | Topic | Genre |
|---|---|---|
| `run1-fiction/`     | Last night of a lighthouse keeper before automation | short fiction |
| `run2-essay/`       | A last conversation someone didn't realize was the last | personal essay |
| `run3-nonfiction/`  | The 1919 Boston Molasses Flood | explanatory nonfiction (domain-gate test) |
| `run4-argument/`    | Should AI fiction be eligible for literary prizes? | argumentative essay |

## Headline result (blind-judged)
Within every runtime, on every topic, the HumanScope output outranked its own baseline. Effect is
largest where the baseline's over-explaining habit is strongest (fiction/essay); for nonfiction the
skill's win is factual/structural discipline and the domain gate held. **n = 1 per cell — a
demonstration, not a statistical or human-rated study.** Full analysis + caveats in
`../evals/test-topics-results.md`.

## Reproduce
Clone the skill, then run each agent's saved prompt on the corresponding runtime and compare via
`../evals/rubric.md`. Not committed here: the working skill clone (`skill-clone/`, a copy of this
repo) and raw model run logs.
