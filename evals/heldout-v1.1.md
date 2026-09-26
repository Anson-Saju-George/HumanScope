# Held-out validation suite — v1.1 (specification, designed by Astra R9)

**Status: specified, not yet run.** Validates the v1.1 SKILL.md patch on *new* material. The six
fair-retest cases (`../test-run/fair-retest/`) stay as a **regression** suite; re-running them is
not validation.

**Protocol rule:** freeze and hash the patched `SKILL.md` before creating the new source texts. Before generating outputs, also freeze all arm instructions (including O's mode-appropriate EDIT/DIAGNOSE instructions and C\*'s exact published diff), source texts, shared briefs, evidence packets, hidden manifests, judge prompts, and scoring criteria. Within each task, all arms receive identical task materials, tool access, model settings, and generation budgets. Any revision prompted by inspecting outputs turns those cases into development material for that revision.

## Cases — 8 new source artifacts, 9 tasks

| # | Hazard and source | Correct behavior | Why the judge brief doesn't automatically favor restraint or intervention |
|---|---|---|---|
| 1 | **Exhibition access notice — light EDIT.** A verbose sentence contains a real opening window and an eligibility exception; nearby material contains genuine filler. | Shorten the expendable language; keep the window, the exception, and who it applies to. | Recoverable information and useful tightening are scored separately. Deleting it all fails, and so does leaving the bloat. |
| 2 | **Motive and realization — paired EDIT briefs.** A new close-third story states a motive that actions alone don't establish, plus a genuinely duplicated clause. | **2A** (ordinary light edit): keep the motive and realization, tighten the duplication. **2B** (explicit request to make the motive ambiguous): make the motive genuinely ambiguous through authorized removal or recasting of its explanation; preserve events, chronology, viewpoint, and other substantive information. Leaving the explicit motive unchanged fails the requested transformation. | The same deletion can't be right under both briefs. Count as one source cluster, not two independent cases. |
| 3 | **Effective apology — light EDIT.** A well-written apology uses purposeful repetition and an explicit admission of responsibility. | Keep the admission and the rhetorical function. Unchanged text can succeed. | Judges are **not** told "no change expected". They assess what the recipient needs, not edit count or byte identity. |
| 4 | **Genuine redundancy — EDIT.** Adjacent paragraphs repeat a proposition without adding scope, emphasis, contrast, or a separate reading path. A distinct qualification sits beside the duplicate. | Consolidate the repetition; keep the proposition and the qualification. | A "never remove stated content" editor fails. So does maximum shortening that loses the qualification. |
| 5 | **Executable instructions — structural EDIT.** A prerequisite appears after the action that requires it; an explanation is detached from its referent. All necessary information exists. Reordering is authorized. | Move the prerequisite before the dependent action and reattach the explanation, without inventing steps. | Untouched text fails an observable task: following the steps in order. A structural edit is genuinely required. |
| 6 | **Knowledge boundaries — DIAGNOSE.** A limited-viewpoint scene uses information before the character acquires it. A clearly retrospective narrator passage legitimately mentions later knowledge. | Identify the first problem with evidence and a feasible repair. Don't flag the retrospective passage just for knowing more. | Suspecting everything fails, and so does accepting everything. Chronology and viewpoint decide. |
| 7 | **Supported correction — EDIT.** A claim is broader than the supplied evidence. The brief authorizes evidence-based correction. | Narrow the claim and keep the citation attached; leave supported neighboring claims intact. | Success requires changing something explicitly stated. The evidence packet decides, not aesthetic preference. |
| 8 | **Notes to agenda — transformation.** Working notes with completed and pending tasks, unresolved alternatives, owners, and dependencies. The user asks for an agenda organized around decisions and follow-ups. | Produce the agenda; keep status, uncertainty, and ownership. | Returning the notes unchanged fails the task; inventing decisions for a tidy agenda fails preservation. |

Case 2A uses an ordinary light-edit brief that preserves meaning and voice; do not add a bespoke instruction naming the motive or realization to protect. Within each task, every arm receives the same brief.

## Execution
- **Arms:** pre-patch S (`../test-run/fair-retest/S-arm-SKILL-snapshot.md`), patched S, O (ordinary),
  and **C\***, a matched compact arm: the patched skill with **only** the lens content and necessary
  references removed, guards and workflow unchanged. Publish that diff.
- **At least 3 fresh-context runs per task and arm:** 9 × 4 × 3 = **108 outputs**.
- Include the **untouched source** as a judged option for EDIT cases.
- Score **unauthorized information change**, **task completion**, and **reader benefit** separately.
  A polished semantic loss must not disappear inside an aggregate.
- Randomize presentation order independently per judgment and allow ties. Judges get the source and the
  task, never the patch or the expected preferred operation.
- Prefer judges from more than one provider. Archive every judge prompt and verdict.
- Eight selected artifacts still don't establish general writing efficacy. **WRITE** mode needs its
  own validation before claiming the revised invention rule or the lenses improve drafting.
