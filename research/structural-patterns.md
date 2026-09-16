# Structural Patterns — Higher-Order Synthesis (RECONCILED, post-council)

> Result of the Claude↔Astra synthesis council (Round 2, `adversarial-review.md`). Claude drafted a
> root-cause + 6 symptom families (P1–P6); Astra independently re-derived and materially improved
> it. This file is the reconciled output that the SKILL is built on. Superseded Claude draft is
> preserved in `raw-model-output/astra-synthesis-R2-raw.txt` and the review log.

## Framing decision: NO asserted operational root cause
Claude proposed a single root cause ("mode-seeking / pick the safe default"). **Astra: delete it
from the operational rules** — "highest-probability", "lowest-risk", "most-legible", audience-
averaging, RLHF-legibility pressure, training-distribution centrality, and the study-specific
**prompt-compression-plus-compliance** confound are all *competing* explanations, and StoryScope
identifies no causal mechanism. **Accepted.** Competing hypotheses stay here as research notes; the
skill asserts no mechanism. (Astra's own best hypothesis, for the record: *pressure to make
narrative purpose and craftsmanship readily recognizable* — explicit meaning, conspicuous emotion,
manageable progression. Still just a hypothesis.)

## The operating rule that replaces "edit toward human"
Every proposed intervention MUST fill four slots, in order:

> **textual evidence → intended reader effect → present failure → smallest useful change**

Hard constraint: **"more human-correlated" / "AI-like" may NOT fill the *failure* slot.** If you
can't name a concrete way the passage fails *this* reader for *this* purpose, you do not edit. This
is the §25 safeguard made operational — it *governs* the action rather than trailing it. It is a
**safeguard requiring genuine evaluation, not a guarantee**: a model can still invent a plausible-
sounding failure rationale, so the failure must be specific and defensible, and "no change needed"
must always be an allowed outcome.

**WRITE branch (no existing passage to diagnose):** when generating new text, the four-slot rule
becomes **brief/constraints → intended reader effect → compositional choice → draft → restraint
review**. Apply the six lenses as *generation-time attention*, not as post-hoc defect-finding.

## The 6 diagnostic LENSES (v1) — conditional, not defaults

Six is an interface choice (a manageable diagnostic set), not a claim of six latent causes. Each
lens is a *question to ask*, never a direction to push. For each: what to look at, the honest
quality reading (§25), and the paper features it draws on.

### L1 · Explanation & interpretation
- **Look at:** narration/dialogue that states themes, morals, or significance; a narrator explaining
  the point; "philosophical debate" dialogue; compulsive summaries/restatement (nonfiction analogue).
- **Diagnose (not prescribe):** is there explanation that adds no needed understanding, or that
  defeats an inference the author wants the reader to make? Explicitness ≠ redundancy; a stated
  theme or a useful summary may be exactly right. **Do not** strip thematic unity or interpretation
  wholesale (that was Claude's correlation-laundering; Astra corrected it).
- **Paper basis:** T1 (Thematic Explicitness 3.28/3.94; Narratorial Commentary 52/77; Dialogue=
  philosophical 34/59). Down-ranked slightly by the prompt-compression confound (limitations §4).

### L2 · Presentation choices  *(was P2 "monotone register")*
- **Look at:** how emotion/experience is rendered — embodied metaphor vs. named feeling vs.
  behavior; sensory density; interiority depth; setting-as-mirror; descriptive vs. active character
  intros; dialogue-vs-narration proportion.
- **Diagnose:** does a specific passage lean on one device past the point of effect? Judge from the
  actual text and its function — **not** from a corpus-level "dominant category," which cannot prove
  within-story repetition. **Do not** manufacture variety by rotating labels/gestures, and **do not**
  delete sensory/interior detail that is doing real work (Astra: "would make prose inert").
- **Paper basis:** T2 (embodied 38/81 — the largest gap; sensory density; interior access;
  psych-mirror; olfactory) + character-introduction mode (T3) and dialogue-to-narration
  proportion (**T7**, not T3) folded in as presentation choices.

### L3 · Causality & closure  *(was P3 "tidiness" — the most dangerous lens)*
- **Look at (two separate questions):** (a) **resolution mechanism** — is the outcome driven by the
  protagonist's choices or by external events/fate? (b) **degree of closure** — how fully is the
  central tension resolved vs. left open? Plus adequacy of the causal chain and subplot presence.
- **Diagnose (neutral):** does the ending follow from established pressures and answer the piece's
  central question? This can justify **strengthening** causality just as often as loosening it.
  Acceptance-based resolution ≠ complete closure; tidy prose ≠ tidy causality.
- **Structural loosening is heavier-touch:** adding subplots/ambiguity/looser causation belongs to
  an authorized **deep edit**, or is surfaced as a *suggestion* under light edit — never a default,
  because "tolerate mess" easily makes writing worse. **Data correction:** the paper measures more
  human *thematically-parallel* subplots (+22, measured across ALL stories, so it does NOT establish
  a human preference for parallel subplots *given* subplots exist); it does NOT support prescribing
  independent/tangential subplots.
- **Paper basis:** T3 (causal-chain continuity, agency-in-resolution 46/69, subplot presence,
  resolution mode). Note: dialogue-to-narration proportion belongs to **T7/L2**, not here.

### L4 · Information order  *(was P4 "linearity")*
- **Look at:** where knowledge is placed — chronology, delayed disclosure, whether a reveal
  recontextualizes earlier material. (Event causality and reader-knowledge are *different* problems.)
- **Diagnose:** does the arrangement create the intended understanding, curiosity, or surprise, while
  preserving comprehension? **Remove "linearity" as a warning sign; "more flashbacks" is NOT a
  prescription.** Answer-first nonfiction routinely and correctly departs from chronology.
- **Paper basis:** T6 (recontextualization 3.28/2.95; chronological discontinuity; anachrony).

### L5 · Referential grounding  *(P5 split, part A)*
- **Look at:** concreteness and specificity of references to the world (named works/people/places
  vs. vague allusion).
- **Diagnose:** would a specific referent serve the piece better than a vague gesture? BUT
  literary allusion ≠ "cite your sources" — a real name can add nothing, and precise description can
  work without names. Add factual sourcing only when a *claim* requires substantiation. Absence of
  names is not itself a defect.
- **Integrity rule (scoped for a skill that also WRITES fiction):** do **not** present invented
  material as real-world evidence, genuine testimony, citation, statistic, or author biography.
  *Fictional* invention (characters, places, events, in-world allusions) is fully allowed when the
  task is fiction. When editing existing text, preserve established story facts unless the user
  authorizes changing them. Sourced additions need not come only from the user, but factual claims
  about the real world must be real and verifiable.
- **Paper basis:** T4 (named reference 47/24; balanced mix 37/16).

### L6 · Reader relationship  *(P5 split, part B)*
- **Look at:** the narrator↔reader (or writer↔audience) stance — direct address, fourth-wall,
  asides.
- **Diagnose:** is the intended relationship maintained and consistent? Direct "you" suits emails/
  tutorials/marketing; narrator asides suit some fiction. **Neither the presence nor the absence of
  reader-address is a default defect**, and "you" is not proof of audience awareness.
- **Paper basis:** T5 (fourth-wall 0.67/0.39; direct address 0.28/0.07 — directions only; the paper
  is internally inconsistent on whether these are %s or ordinal means, see paper-notes T5 note).

## Three editorial meta-lenses (NOT paper-derived — label as such)
Astra flagged these as things a real developmental editor centers that neither the paper nor the
lenses capture. Use as editorial judgment, never as paper-grounded rules:
- **M1 Selection before arrangement** — is this the right *material* for the piece's central concern?
  (An irrelevant scene stays irrelevant after perfect restructuring.)
- **M2 Attention & proportion** — does space go to the consequential moments, or does a decisive
  turn get one sentence after pages of setup?
- **M3 Character-specific necessity** *(fiction)* — would *this* person notice/say/choose this and
  bear its consequences? (Agency frequency ≠ believable motivation.)

## Transfer summary (editorial judgments, NOT tested by StoryScope)
Everything is "split" by purpose — see `evidence-map.md` for the per-lens × genre grid. Headlines
(Astra): **L3 does not categorically reverse outside fiction** — clear organization transfers, only
*fabricated* causal neatness harms; **L5 transfers conditionally** via relevance/evidential need,
not name density; **L4's** answer-first departure from chronology is common and correct in nonfiction.

## What this gives the skill
- A **DIAGNOSE** stage over 6 lenses (+3 editorial), each producing evidence→effect→failure→change,
  or "no change needed."
- A **domain gate** (feature × genre × purpose) rather than blunt theme on/off.
- The four-slot rule as the built-in **§25 brake** — a safeguard that strongly discourages "edit
  toward human" (it still requires genuine judgment; it is not a guarantee).
