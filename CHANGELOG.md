# Changelog

## v1.1.2 — 2026-10-05 — Claude Code plugin and reviewed ChatGPT packaging (skill unchanged)

`SKILL.md` is byte-identical to v1.1.0.

- **Claude Code plugin marketplace** (`.claude-plugin/`): install with
  `claude plugin marketplace add Anson-Saju-George/HumanScope`, then
  `claude plugin install humanscope@humanscope`. Validated with `claude plugin validate --strict` and
  test-installed locally (loads one skill, `humanscope`).
- **ChatGPT packaging revised after Astra R11:** the v1.1.1 `instructions.txt` wrongly claimed to quote
  SKILL.md word for word, and its excerpts dropped the transformation exception and the intended-format
  rule. It is replaced by a self-contained compressed adaptation (about 2,900 characters) that keeps
  those exceptions. The setup guide adds an accurate GPT description, conversation starters, files
  pinned to this release, GPT Store notes, and a six-case smoke test to run before publishing.

## v1.1.1 — 2026-10-05 — docs and ChatGPT setup (skill unchanged)

`SKILL.md` is byte-identical to v1.1.0. This release carries the corrected public record and adds
ChatGPT setup.

- **ChatGPT setup** (`chatgpt/`): a short instructions block (about 2,000 characters) that points to
  SKILL.md and quotes its core rules word for word, plus steps for a Custom GPT, a Project, or a
  one-off chat. No new rules. Quality in ChatGPT hasn't been evaluated.
- **Corrected evaluation record** after outside review and Astra R10: the bare-edit arm was excluded
  as an evaluation error; editing vs a strong prompt is "no demonstrated advantage" (pre-R9 outputs);
  the held-out task-05 regression is acknowledged; the fidelity claim is limited to scores; always-on
  is described as tested only when supplied explicitly. See the v1.1.0 entries below, corrected in
  place.

## v1.1.0 — 2026-10-05 — evaluation integrity, R9 fixes, and blind validation

A max-rigor audit found an evaluation confound the first 7 rounds missed. Correcting the record and
tightening the runtime; no new lenses/scanners.

- **Disclosed the A/B confound:** the skill arms also received extra instructions (read research
  files, be implicit, cite real refs, answer-first) that baselines did not, and one judge rewarded
  the skill's own aesthetic (implicitness). **Withdrew attribution of the 8/8 to `SKILL.md` alone;**
  the treatment is "skill + extra instructions + research context."
- **Corrected residual overclaims:** removed "demonstrated mechanism / effect-size dependence /
  preserved voice / no over-editing" (generation can't show voice-preservation or restraint); fixed
  the ablation model-family error (generator Claude, judge Sol); neutralized generalization causal
  language (no guardless control).
- **6 SKILL.md runtime fixes:** authorized-transformation clause in the four-slot rule; claim-
  preservation exempts supported corrections/authorized transforms and broadens to meaning/scope/
  time/modality/negation/exceptions/attribution; "no change is valid *when the text meets the brief*";
  removed a redundant output bullet; reworded "Never" to honor explicit style/creative constraints;
  softened the distinctiveness claim.
- **Updated README** testing inventory (exploratory generation / confounded ablation / preservation
  smoke tests).
- **Ran the matched-brief exploratory EDIT comparison** (`test-run/fair-retest/`): 6 EDIT cases × 4 arms (HumanScope,
  strong ordinary editor, compact four-slot, and Alex Chen's *Human Scope*) with identical briefs and
  two blind OpenAI judges. **Result: mixed, no demonstrated advantage over ordinary or compact
  editing** (1 win / 2 losses / 3 ties against each). HumanScope made no unauthorized change to a spec
  where the ordinary and compact arms changed its requirements. It lost information in a marketing
  passage and a fiction passage, and it preserved the brief better than Chen's skill in both fiction cases.
- **Astra R9 patch (6 SKILL.md edits; initially untested, later examined in the reduced held-out comparison below):** check what a deletion removes (filler ≠ a
  distinct claim, motive, or realization); bound the authorized-transformation exception; scope
  fictional invention to WRITE (EDIT alters events only when authorized); reword L1 so explanation
  can carry a motive or realization; prevent narrative genre alone from triggering broader structural review during light EDIT; add a viewpoint-sensitive
  knowledge-boundary check, crediting Alex Chen's *Human Scope*.
- **Ran an everyday WRITE-prompt comparison** (`test-run/write-x/`): bare task prompts (tidy and
  casually typed) vs the same prompts plus HumanScope; web page copy, blog, and email; one blind
  Astra judge. Every full-skill draft ranked above every bare draft within each task, with the
  biggest gap on fidelity to the supplied facts (bare outputs added recipes, policies, and
  histories). This tests the whole package, not which rule causes it. Small sample (1–3 runs per arm).
- **Judged the story arm:** all three HumanScope stories ranked above all three bare stories.
- **Added a bare "can you edit this" arm** to the edit comparison and re-judged all five editors.
  **Evaluation error (disclosed after release):** the judge prompt said all arms shared one
  preservation brief, which the bare arm never received, so its scores can't measure the bare arm,
  the brief, or the skill. Excluded from the results and kept as a documented error. The re-judge's
  52–52 for HumanScope and the excellent-editor prompt is judgment consistency on the same pre-R9
  outputs, not a replication.
- **Added opt-in always-on mode** (`always-on/CLAUDE-snippet.md`): a short CLAUDE.md block for
  reader-facing prose. Blind test, with the snippet supplied explicitly as project instructions:
  1st on web page copy and 2nd on the blog (it left placeholders), ahead of bare in both. Automatic
  loading and continued application were not tested.
- **Ran the held-out validation** (`evals/heldout-v1.1-run/`): 9 new frozen tasks, patched vs
  pre-patch vs untouched. The judge preferred patched on 4, pre-patch on 1 (task 05, so it was not
  regression-free), and tied 4. One judge, one generation per arm.
- **Final summary:** `evals/FINAL-RESULTS.md`.
- **Credited prior art:** Alex Chen's *Human Scope*, the companion skill to his SCOPE reel.
- **Archived for reproducibility:** judge prompts and verdicts, exact S-arm skill snapshot, shuffle keys.
- **Held-out validation specified** (`evals/heldout-v1.1.md`: 8 new artifacts, 9 tasks, 108
  outputs). The planned 108-output protocol was not completed. A reduced S/P/U comparison was run
  (nine tasks, one generation per arm, one judge, without O or C*): see the entry above.
- **Astra R10 review (post-release):** corrected the public record (bare-edit arm removed, version
  context added to the editing and Chen comparisons, held-out regression acknowledged, fidelity
  claim limited to scores). Proposed SKILL.md and always-on changes deferred to v1.2 pending tests.

## v1.0.0 — 2026-09-20

First tagged release of **HumanScope** — a research-grounded, composition-focused writing & editing
skill. Built from the *StoryScope* paper (Russell et al., COLM 2026), pressure-tested across seven
independent adversarial-review rounds (GPT Sol ×1, GPT Astra ×6), and evaluated in the open.

### Skill
- `SKILL.md` — six diagnostic lenses (as questions, gated by purpose), the four-slot intervention
  rule (no edit without a concrete reader-need failure; "AI-like" is never a valid reason;
  "no change" is always valid), purpose-based review depth (lean for expository, fuller for
  narrative), and generalization guards (§1 artifact/format, claim-strength & citation attachment,
  "notes may remain notes").
- Explicit stance: preserves voice/meaning/facts; **not** an AI-detector-evasion tool; never
  optimizes a "% human" score.

### Research provenance (`research/`)
- Paper notes, evidence map (30 core features → lens), higher-order synthesis, secondary-source
  analysis, rejected-ideas log, limitations, and the full adversarial-review record (7 rounds).

### Evaluation (`evals/`, `test-run/`)
- **Exploratory A/B generation comparison** (4 topics × 2 runtimes): blind model-judge ranked HumanScope above its own
  baseline in all 8 cells *(confounded; does not isolate SKILL.md)*.
- **Ablation** (full vs compact four-slot vs ordinary): lenses win on narrative; compact wins on
  expository → validated domain-gating. *(Withdrawn: the ablation did not isolate the lenses — see
  v1.1.)*
- **Preservation smoke tests** (four artifacts, twelve outputs): reported ten clean outputs and two deviations. *(The earlier descriptions "non-harmful" and "guards hold across genres and model families" are withdrawn; the tests did not establish harmlessness, causal guard effectiveness, or broad reliability.)*
- Three-way blind **human-eval protocol** scaffolded (`evals/human-eval-protocol.md`).

### Honest scope
Research grounding is fiction-specific; evidence is preliminary and model-judged. HumanScope is
**safe and useful** across prose genres *(withdrawn: stronger than the evidence — see v1.1)*; **distinctive value over a competent ordinary editor is not
yet demonstrated with human raters** — that is the next milestone.
