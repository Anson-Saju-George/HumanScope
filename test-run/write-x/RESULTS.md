# Write-mode test — bare everyday prompts vs HumanScope

**Question:** a person with no prompt-writing know-how types an ordinary request ("make a web page
for my bakery…") into a fresh chat. Is the output generic or invented, and does installing
HumanScope change that?

This complements the [fair re-test](../fair-retest/RESULTS.md). There, every arm, including the
"ordinary editor", got a careful, quality-oriented editing instruction. Here the baseline gets
**only the task**.

## Design
- **Tasks (3 judged):** bakery web page (single HTML file), company blog post (Jira → Linear),
  team email (standup change). Briefs with the supplied facts: [`TASKS.md`](TASKS.md).
- **Arms, all Claude Opus subagents with fresh context:**
  | Arm | Prompt |
  |---|---|
  | **X1–X3** | The task only, as a tidy request (3 runs per task) |
  | **S1–S3** | "Use the HumanScope skill: read `SKILL.md`…" + the same task (3 runs per task) |
  | **H** (web page only) | The task **as a person would type it**: lowercase, run-on, no instructions about quality |
  | **HS** (web page only) | `/humanscope` + the same casual text |
- **Skill version:** `SKILL.md` at commit `5c06c24` (R9 patch; sha256 `a7de6a7f…8fce`).
- **Judging:** one blind **fresh GPT Astra** (`gpt-6-astra` @ xhigh), not the project's pinned
  review session. It saw only the visible text (HTML stripped), with labels shuffled per task
  ([`build_packet.py`](build_packet.py), key in [`_key.json`](_key.json)). It scored
  **generic/"slop"**, **reader usefulness** and **fidelity to the supplied facts** (1–5), then
  ranked the pieces. It never saw any skill text. Prompt and verdict: [`judging/`](judging/).
  Claude also scored the pieces blind before unblinding; that is a same-family, author-side
  opinion and is reported only where it disagreed.

## Results (unblinded) — slop / usefulness / fidelity, rank

**Web page**
| Rank | Arm | Scores |
|---|---|---|
| **1** | **HS** (casual + `/humanscope`) | 5 / 5 / 5 |
| 2 | S1 | 4 / 4 / 4 |
| 3 | S2 | 4 / 4 / 3 |
| 4 | S3 | 4 / 4 / 3 |
| 5 | X1 | 3 / 4 / 2 |
| =6 | **H** (casual, no skill) | 3 / 4 / 2 |
| =6 | X3 | 3 / 4 / 2 |
| 8 | X2 | 3 / 4 / 2 |

**Blog:** S1 1st (4/4/3) · S3 2nd (4/4/3) · S2 3rd (4/2/3, left `[bracketed]` placeholders instead
of inventing the lost reports; honest, but not publishable as-is) · X1, X2, X3 all =4th
(fidelity **1**: "fabricates an entire migration account and reporting response").

**Email:** S2 1st (5/5/5, "without adding substantive policy") · S1 2nd · S3 3rd · X1, X3 =4th ·
X2 6th. Every email scored 5 for slop. The bare emails lost on invented policy: trial periods,
posting deadlines, "meeting-free mornings". *(Claude's blind read called the emails a tie. Astra's
finer fidelity check found a consistent difference.)*

**In all three tasks, every HumanScope output ranked above every bare-prompt output.**

## Reading
- **What bare prompts produce is less "slop" than confident invention.** Astra: *"the slop
  problem is moderate, not catastrophic … the bigger failure is confident invention. The worst
  pieces sound more informative because they manufacture evidence."* Examples from the bare
  arms: "long fermented, baked dark", "laminated dough rolled with sugar and spice", "when
  something sells out, it's gone for the day", "no phone orders", named lost dashboards, migration
  steps, a "shortcut cheat sheet". There were also stock lines: "Bread worth getting up for",
  "Three things, done well", "The problem wasn't Jira. It was how Jira made us work."
- **Prompt style didn't rescue the bare arm.** The casual, human-typed prompt (H) behaved like
  the tidy one (=6th of 8). The same casual text with `/humanscope` (HS) ranked 1st with a clean
  sheet.
- **The mechanism is consistent with the skill's integrity and four-slot rules** (no invented
  material presented as real; no additions without a reader need). This design does not isolate
  which instruction is responsible.
- **Cost:** skill outputs were plainer and shorter (for example "Our morning buns." with nothing
  more), and one blog post needed the owner to fill in facts.

## Caveats (governing)
- **Small.** Three runs per arm for the tidy prompts and **one** each for H and HS. Three short tasks.
- **One external judge** (an OpenAI model), no human readers. All writing is by Claude.
- **The fidelity criterion overlaps the skill's own integrity rule.** "Don't present unsupplied
  facts as real" is a reasonable, neutral standard for owner-facing copy, but it is the axis the
  skill explicitly targets. The slop and usefulness scores favored the skill too, by smaller margins.
- **The baseline is Claude inside a Claude Code subagent**, not the consumer chat app, and it
  was told where to save the file.
- **Story arm not judged:** all six stories (X1–X3, S1–S3) were generated but not yet judged. The
  run was interrupted by a usage limit.
- This supports "HumanScope reduces invented detail and stock phrasing in everyday WRITE tasks".
  It does not establish broader writing quality, and it does not replace the held-out suite.
