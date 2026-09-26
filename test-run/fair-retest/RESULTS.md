# Fair re-test — matched-brief exploratory EDIT comparison (pre-R9 v1.1 candidate)

Designed in response to the Astra R8 audit, which found the v1.0 A/B confounded (the skill arm got
extra instructions the baseline didn't, and one judge rewarded the skill's own aesthetic).

## Design
- **Task:** EDIT (not generation), so restraint and preservation are measurable.
- **Cases (6):** academic · marketing · notes · technical (from the generalization set) + two fiction
  cases written for this test: **fiction-a** (a narrator paragraph initially mislabelled redundant despite supplying distinct psychological information) and **fiction-b** (voice-driven first-person reflection where no change is the expected answer).
  Hidden manifests: [`MANIFESTS.md`](MANIFESTS.md).
- **Arms (4), all Claude Opus subagents, fresh context, same text:**
  | Arm | Condition |
  |---|---|
  | **S** | HumanScope `SKILL.md` (v1.1 working copy, post-R8) |
  | **O** | Strong ordinary editor — [`O-instr.txt`](O-instr.txt) |
  | **C** | Compact four-slot rule only, no lenses — [`C-instr.txt`](C-instr.txt) |
  | **K** | Alex Chen's *Human Scope* (Chen Media, the SCOPE-reel companion skill) — `_competitor/` |
- **Judges (2), blind and independent:** a *fresh* GPT Astra (`gpt-6-astra` @ xhigh; deliberately
  not our pinned Astra session, which knows HumanScope's design) and Codex Sol (`gpt-5.6-sol` @ high).
  Isolated directory with no key and no arm names; letters P/Q/R/T were shuffled per case
  ([`build_packet.py`](build_packet.py); keys in `_key*.json`). The judges saw only the shared
  editing brief, the case context and the protected elements, never any skill text or taxonomy.
  They scored **preservation** and **task success** (0–5) separately, then ranked the four edits.

## Results (unblinded) — preservation / task success, rank

| Case | S (ours) | O (ordinary) | C (compact) | K (Chen) |
|---|---|---|---|---|
| Academic — Astra | 5/5 · =1 | 5/5 · =1 | 5/5 · =1 | 3/3 · 4 |
| Academic — Sol | 5/5 · =1 | 5/5 · =1 | 5/5 · =1 | 3/3 · 4 |
| Marketing — Astra | 3/4 · 3 | 5/5 · =1 | 5/5 · =1 | 2/3 · 4 |
| Marketing — Sol | 4/3 · 3 | 5/5 · =1 | 5/5 · =1 | 3/3 · 4 |
| Notes — both | 5/5 · =1 | 5/5 · =1 | 5/5 · =1 | 5/5 · =1 |
| Technical — Astra | 5/5 · =1 | 3/3 · 3 | 2/2 · 4 | 5/5 · =1 |
| Technical — Sol | 5/5 · **1** | 3/3 · 3 | 2/2 · 4 | 5/4 · 2 |
| Fiction-a — Astra | 2/2 · 3 | 3/2 · 2 | 3/3 · **1** | 2/1 · 4 |
| Fiction-a — Sol | 2/2 · 3 | 3/2 · **1** | 3/2 · 2 | 1/1 · 4 |
| Fiction-b — both | 5/5 · =1 | 5/5 · =1 | 5/5 · =1 | 2/1 (Astra) · 2/0 (Sol) · 4 |

**Totals (max 60 per judge):** S 51 / 51 · O 51 / 51 · C 50 / 49 · K 37 / 35 (Astra / Sol).
Equal sums of two ordinal scales do **not** establish equivalence. The case counts:

| Comparison | Astra: S wins / losses / ties | Sol: S wins / losses / ties |
|---|---|---|
| S vs O | 1 / 2 / 3 | 1 / 2 / 3 |
| S vs C | 1 / 2 / 3 | 1 / 2 / 3 |

## Reading (corrected per Astra R9)
**Headline: in six preservation-focused EDIT cases, HumanScope showed mixed results and no
demonstrated advantage over ordinary or compact editing. The comparison did not isolate the lenses.**

- **Where S did better: the spec's unresolved ambiguity.** The definition says 5xx or timeout; the exception says
  "4xx other than 429". O and C silently made 429 retryable, inventing an operative requirement; C
  also turned lowercase `should` into `SHOULD`. S reordered definition-first and changed no behavior.
  Blind judge (Astra): *"deleting 'It is worth noting that' is editorial cleanup; adding 'or 429'
  requires authority over the specification."*
- **Where S did worse: unauthorized loss of distinct information.**
  - *Marketing:* S deleted the whole opening sentence, including the protected claim "deploying
    software has never been more complex", instead of only the cliché.
  - *Fiction-a:* the manifest labelled Dana's realization paragraph the defect; **both judges
    disagreed**. The paragraph supplies a habit, a specific fear, that fear as the drive's motive,
    and Dana's recognizing it — none of which the eggs or the drive establish. **All four arms lost the stated motive. S removed more stated psychological information than O or C; K also removed that information and added unsupported material.** Ranking the least-damaging rewrite does not establish improvement over the original (the untouched source was not a judged option — a design gap). A faithful
    tightening was possible (R9's example: *"Whisk in hand, she realized she had always cooked
    when afraid: fear of losing her mother was why she had driven two hours, unasked."*).
- **S vs C:** C is **not** a lens-only ablation. It also omits S's claim guard, artifact
  conventions, routing, and restraint check, so S's spec result may come from those. Say *"the full
  package did not establish an advantage over the compact package,"* not "the lenses showed no
  increment."
- **S vs K (Chen's *Human Scope*):** S better preserved the brief in both fiction cases. K's
  fiction-a edit invented actions (a deleted text message, an aching wrist, keys in a coat pocket).
  In fiction-b, "At the funeral I skipped it too" follows from the original. The unsupported
  addition is the comparative motive ("nobody there needed me to skip it more than I did"), and the
  loss is the narrator's present confession. The other four cases are outside K's principal fiction focus; its README permits selective application to other writing. This
  small comparison does not establish general superiority.
- **Brief bias:** the edit-under-preservation brief tests a promised behavior (improve wording
  without making substantive authorial decisions). It does **not** determine the best
  *developmental* edit, and the fiction-a verdict should not be generalized to fiction editing at
  large.
- **Manifest errors recorded:** fiction-a's "defect" label was wrong under this brief;
  academic's "leverage" defect label was word-based (S/O/C kept it and got full marks). Removed.
- **Judges:** two independently run **OpenAI** models. That is not cross-provider corroboration,
  and 2 judges × 6 cases are not twelve independent replications. Four cases were already
  development material. Judge prompts and verdicts are archived in [`judging/`](judging/), and the
  exact S-arm skill in [`S-arm-SKILL-snapshot.md`](S-arm-SKILL-snapshot.md) (sha256 `46c11ec0ea6f66b2dcdf7ff2710f3d464c4a77ab78eeb788633331e1fa7ad8a4`).

## Caveats (governing)
One sample per arm per case; six short cases; two independently run OpenAI model judges, not human readers. All generators are Claude. The preservation-focused brief limits generalization to other editing objectives. Four cases were already development material, and the R9 patch was informed by these results. Rerunning these cases is useful regression testing, but cannot independently validate the patch; that requires held-out material.

## What v1.1 changed in response (Astra R9)
Six SKILL.md edits (see CHANGELOG): check what a deletion removes; bound the transformation
exception; scope fictional invention to WRITE; reword L1 so explanation can carry a motive or
realization; prevent narrative genre alone from triggering broader structural review during light EDIT; add a viewpoint-sensitive knowledge-boundary
check (from Chen's checklist). **These are untested.** Re-running these six cases is a regression
test, not validation. Validation is the held-out suite in
[`../../evals/heldout-v1.1.md`](../../evals/heldout-v1.1.md).


Arm K used Alex Chen's *Human Scope* skill as downloaded 2026-09-25 from https://chen.media/downloads/human-scope.zip (not redistributed here; place its `human-scope/` folder in `_competitor/` to reproduce).
