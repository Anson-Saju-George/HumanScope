# Changelog

## v1.1 (in progress) — evaluation-integrity corrections (Astra R8 audit)

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
- **Planned:** a confound-free re-test (identical briefs across arms, neutral judges); a versioned
  eval harness + constraint manifests; a regression suite.

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
- **A/B efficacy** (4 topics × 2 runtimes): blind model-judge ranked HumanScope above its own
  baseline in all 8 cells.
- **Ablation** (full vs compact four-slot vs ordinary): lenses win on narrative; compact wins on
  expository → validated domain-gating.
- **Generalization** (academic / marketing / notes / technical × 3 arms): 10/12 clean, 2 minor
  non-harmful; guards hold across genres and model families.
- Three-way blind **human-eval protocol** scaffolded (`evals/human-eval-protocol.md`).

### Honest scope
Research grounding is fiction-specific; evidence is preliminary and model-judged. HumanScope is
**safe and useful** across prose genres; **distinctive value over a competent ordinary editor is not
yet demonstrated with human raters** — that is the next milestone.
