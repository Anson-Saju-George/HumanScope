# HumanScope — final evaluation summary (v1.1)

All results below come from **blind** judging: outputs were shown as shuffled letters, judges never
saw any skill text, and the key was opened only after scoring. The judges are OpenAI models (fresh
GPT-6 Astra @ xhigh; Codex Sol for the fair re-test). The writers are Claude Opus subagents with
fresh context. Every prompt, output, key, and verdict is in the linked folders.

## Scorecard

| Question | Test | Result |
|---|---|---|
| Does it beat what a normal user gets from a bare **writing** prompt? | [write-x](../test-run/write-x/RESULTS.md): web page, blog, email, story (26 pieces) | **Yes, in all 4 tasks:** every HumanScope piece ranked above every bare piece |
| …even when the prompt is typed casually, the way people really write? | web page, casual prompt with vs without `/humanscope` | **Yes:** without it, =6th of 8; with it, **1st with 5/5/5** |
| Does a preservation brief beat a bare **"can you edit this"**? | [5-editor re-judge](../test-run/fair-retest/RESULTS.md#re-judge-with-a-bare-edit-arm) (6 cases) | **Confounded.** Any brief (the skill, or a one-paragraph prompt) beat the bare request, 52 and 52 vs 33, but the judge was told all arms shared the brief, so the bare edit was scored against rules it never received |
| Does it beat a carefully written "excellent editor" prompt? | same | **No, a tie** (52 vs 52), reproduced across two judging runs |
| Do the six lenses add value over the four-slot rule alone? | same (compact arm C) | **Not shown** (52 vs 50); the comparison doesn't isolate the lenses |
| How does it compare with Alex Chen's *Human Scope*? | same | **Ahead in this evaluation** (52 vs 37); Chen's skill invented events in fiction |
| Does opt-in **always-on** mode work without typing `/humanscope`? | [always-on](../test-run/write-x/always-on/) | **Yes:** web page 1st (5/5/5); blog 2nd behind `/humanscope`, ahead of bare |
| Did Astra R9's six fixes help, on texts never seen before? | [held-out](heldout-v1.1-run/) (9 tasks) | **Modestly yes:** patched 4 wins, 1 loss, 4 ties vs pre-patch (123 vs 117 of 135) |

## What the skill actually does
Blind judges consistently pointed at the same mechanism. Bare Claude output is rarely "delve /
tapestry" slop. It is fluent copy that **confidently invents facts** the owner never gave: recipes,
sell-out rules, migration histories, lost dashboards, trial periods, posting deadlines. It also leans
on stock taglines. In these tests HumanScope **reduced** those unsupported additions, though
not to zero: its blog drafts still scored 3/5 for fidelity (bare: 1/5), with some invented outcomes.
It also cut the stock phrasing, and in edits mostly left voice and meaning alone (personal notes, a narrator's "I think", a spec's open ambiguity).
In Astra's words, the worst bare pieces *"sound more informative because they manufacture
evidence."*

**Its cost:** plainer copy, and sometimes placeholders where facts are missing. That is honest, but
it means the owner must fill them in.

**Its weakest area is fiction editing**, the domain the StoryScope research comes from. In the
fiction-a edit case it ranked 3rd under every judgment and removed more of a character's stated motive
than the plain editors did; the R9 fixes target this and helped on one held-out motive task, but it is
not settled. Most of its clear wins are on web pages, blogs, emails, and edits of everyday text.

## Held-out validation (patched v1.1 vs pre-patch)
Nine new tasks, written and frozen (hash recorded) before any output existed. Each task had three
candidates: patched skill (**S**), pre-patch skill (**P**), and the **untouched source** (**U**), so
"change nothing" could win where it should. One blind Astra judge scored fidelity / task / reader
benefit (1–5 each).

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
| **Total /135** | | **123** | **117** | |

- **Patched vs pre-patch: 4 wins, 1 loss, 4 ties.** The fixes help modestly on new material and
  didn't break anything. The gains were on information fidelity (01, 07) and on doing an authorized
  transformation properly (02B).
- **Both versions changed nothing where nothing needed changing** (02A, 03) and did the real
  structural work where it was required (04, 05, 07, 08). The untouched source lost every task that
  required a change.
- **06 caveat:** both versions found the intended problem but over-stated it. Astra also judged the
  planted error weaker than intended: Anna *could* plausibly know the sender. That is a weakness in
  the case design as well as in the outputs.
- One judge, one run per arm, nine tasks. This is a consistency check, not proof.

## Limits (read before quoting any of this)
- **Confound in the bare-edit comparison:** its judge prompt said all arms shared one preservation
  brief, which the bare arm never received. Treat 52 vs 33 as "a brief beats no brief", not as a
  HumanScope-specific result. The writing comparison doesn't have this problem: there, the judges were
  given the owner's supplied facts, and every arm got the same request.
- Small samples: 1–3 runs per arm per task; a few dozen short texts in total.
- Model judges only (OpenAI), no human readers. All writing is by Claude.
- The fidelity criterion overlaps the skill's own integrity rule. "Don't present unsupplied facts as
  real" is a fair standard for owner-facing copy, but it is the axis the skill targets.
- Research grounding (StoryScope) is fiction-specific; non-fiction use is an editorial adaptation.
- Output quality with other assistants (e.g. ChatGPT) has not been evaluated; they can load
  SKILL.md, but that only shows they can read it.
- Not a detector-evasion tool. Nothing here measures or targets "AI detection" scores.
