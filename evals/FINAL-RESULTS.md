# HumanScope — final evaluation summary (v1.1)

All results below come from **blind** model judging: outputs were shown as shuffled letters, judges
never saw any skill text, and the key was opened only after scoring. The judges are OpenAI models
(fresh GPT-6 Astra @ xhigh; Codex Sol in the fair re-test). The writers are Claude Opus subagents
with fresh context, run inside Claude Code, which is not the consumer chat app. Outputs, keys, judge
prompts, and verdicts are archived in the linked folders. Generation instructions are given in each
results page.

## Scorecard

| Question | Test | Result |
|---|---|---|
| How did **task + skill** compare with **task only** on writing prompts? | [write-x](../test-run/write-x/RESULTS.md): web page copy, blog, email, story | The judge ranked **every full-skill draft above every bare draft** within each of the 4 tasks |
| …with one casually worded request? | one bakery request, with vs without `/humanscope` | Without: =6th of 8. With: **1st, 5/5/5** (one run each) |
| How did it compare with a carefully written **"excellent editor" prompt** on editing? | [fair re-test](../test-run/fair-retest/RESULTS.md) (6 cases) | **No demonstrated advantage.** 1 win, 2 losses, 3 ties under each original judge; equal totals (51–51, later 52–52) don't establish equivalence. The outputs come from the **pre-R9** skill |
| Do the six lenses add value? | same (compact arm C) | **Untested.** Mixed results vs the compact package, which also omits other components besides the lenses |
| How did it compare with Alex Chen's *Human Scope*? | same | The pre-R9 skill **better preserved the requested meaning in the two fiction cases tested**; this doesn't establish general superiority |
| What happens when the **always-on snippet** is supplied as project instructions? | [always-on](../test-run/write-x/always-on/) | Its outputs ranked above the bare outputs on both tasks (web page copy 1st; blog 2nd behind `/humanscope`). **Automatic loading and continued application were not tested** |
| Patched v1.1 vs pre-patch, on new material | [held-out](heldout-v1.1-run/): 9 tasks from 8 source texts | Patched preferred on 4, pre-patch on 1, tied on 4. **Not regression-free** (see task 05) |

**Removed from the scorecard: the bare "can you edit this" arm.** Its judge was told that all
editors shared one preservation brief, but that arm never received it, so it was scored against rules
it hadn't been given. Those scores can't measure the bare arm, the brief, or the skill. The run is
kept as a [documented evaluation error](../test-run/fair-retest/RESULTS.md#re-judge-with-a-bare-edit-arm).

## What the writing results show
In the judge's explanations, bare Claude output was rarely "delve / tapestry" slop. Its weak points
were **owner-specific details nobody supplied**: recipes, sell-out rules, migration histories, lost
dashboards, trial periods, posting deadlines. The judge's explanations frequently favored outputs
with fewer such unsupported assertions. **This comparison does not identify which instructions in
the skill produced the difference.**

**Fidelity scores**, the judge's 1–5 rating of faithfulness to the owner's supplied facts:

| Task | Full-skill drafts | Bare drafts |
|---|---|---|
| Web page copy | 4, 3, 3, plus the casual `/humanscope` run: 5 | 2, 2, 2, plus the casual bare run: 2 |
| Blog | 3, 3, 3 | 1, 1, 1 |
| Email | 4, 5, 4 | 3, 3, 3 |

Across the three non-fiction tasks, every full-skill draft received a higher fidelity score than
every bare draft for that task. Only 2 of these 10 full-skill drafts scored 5/5, and one of the two
is the casual-prompt run, so among the 9 standard runs it is 1 of 9. A 5/5 is a judge score, not
independent verification that the text is error-free. Check facts before publishing.

**Other criteria were more mixed:** all six emails tied on the slop score, and the skill blog that
left `[placeholders]` scored lower on usefulness than the bare blogs. The overall ranking favored
the skill, but not on every axis. The writing judge's rubric also listed stock phrases and "tidy
triads" as slop, which is close to the skill's own taste, so treat the slop scores as provisional.
The fidelity criterion doesn't have that problem.

**Cost:** plainer copy, and sometimes placeholders where a fact is missing.

**A known failure:** in the preservation-focused fiction-a edit, the pre-R9 skill removed distinct
psychological information (a character's stated motive). The few fiction examples tested don't
establish a ranking of performance across genres. Fiction-b, where no change was needed, went fine.

## Held-out validation (patched v1.1 vs pre-patch)
Nine tasks from eight new source texts (02A and 02B share one source). The materials were hashed, and
the author reports they were frozen before any output was generated. EDIT and transformation tasks
included the **untouched source** (**U**) as a candidate, so "change nothing" could win; the
diagnosis task (06) compared only the two responses. One blind Astra judge scored fidelity / task /
reader benefit (1–5 each). One generation per arm.

| Task | What it tests | S (patched) | P (pre-patch) | U (unchanged) |
|---|---|---|---|---|
| 01 access notice | trim filler, keep every condition | **5/5/5 · 1st** | 4/4/4 · 2nd | 3rd |
| 02A motive (light edit) | keep a stated motive | =1st (unchanged) | =1st (unchanged) | =1st |
| 02B motive (make ambiguous) | do an authorized transformation | **4/4/4 · 1st** | 3/4/3 · 2nd | 3rd (fails task) |
| 03 apology | leave purposeful repetition alone | =1st (unchanged) | =1st (unchanged) | =1st |
| 04 redundancy | merge a duplicate, keep the exception | =1st | =1st | 3rd |
| 05 instructions | reorder steps, add none | 4/5/4 · 2nd | **5/5/5 · 1st** | 3rd |
| 06 knowledge (diagnose) | find a viewpoint leak | **2/3/3 · 1st** | 2/2/2 · 2nd | — |
| 07 correction | narrow claims to the evidence | **5/5/5 · 1st** | 5/5/4 · 2nd | 3rd |
| 08 notes → agenda | transform, keep owners/statuses | =1st | =1st | 3rd |
| **Sum /135** | | **123** | **117** | |

- In this single run, the judge preferred the patched output on four tasks, the predecessor on one,
  and tied them on four. **Task 05 scored lower for patched fidelity and reader benefit, so the run
  was not regression-free.** These observations don't establish that the patch systematically
  improves or worsens performance. The 123–117 sum is not a calibrated effect size.
- Task 01 improved on all three scores. Task 02B improved on fidelity and reader benefit, while task
  completion stayed at 4/5. Task 07 improved only on reader benefit; both versions scored 5/5 for
  fidelity and completion.
- Both versions preserved the motive under the light-edit brief (02A). The patched version ranked
  higher under the separate ambiguity-transformation brief (02B).
- Both versions changed nothing on 02A and 03, and the untouched source lost every task that required
  a change.
- **06:** both flagged the intended issue, but whether it was an actual error was disputed, and both
  diagnoses overstated the evidence. This is partly a case-design problem.
- This was a **reduced** run. The planned protocol was 4 arms × 9 tasks × 3 runs (108 outputs)
  including O and C\*. It was not completed.

## Limits (read before quoting any of this)
- Small samples: 1–3 runs per arm per task; a few dozen short texts in total.
- Model judges only (OpenAI), no human readers. All writing is by Claude, inside Claude Code.
- Comparisons test the **whole instruction package**, not individual rules or the lenses.
- The bare-edit arm was misjudged (see above) and is excluded from conclusions.
- Research grounding (StoryScope) is fiction-specific; non-fiction use is an editorial adaptation.
- Output quality with other assistants (e.g. ChatGPT) has not been evaluated. They can load SKILL.md,
  but that only shows they can read it.
- Not a detector-evasion tool. Nothing here measures or targets "AI detection" scores.
