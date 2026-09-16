# HumanScope — Roadmap & Current State (single source of truth)

This is the project map + where we've reached, so any agent (Claude or Astra) can pick up with
full context. Condensed from the original build brief.

## The mission (from the brief)
Build **HumanScope**: a research-grounded writing/editing skill that makes AI prose resemble
strong human writing at the level of **composition/structure**, using the supplied paper as the
primary authority. NOT a surface "ban em-dashes / avoid 'delve'" humanizer. NOT an AI-detector
evasion tool. Preserve author voice, meaning, intent. Minimum effective intervention. Domain-aware.
Success = blind reader/editor preference + fidelity to author intent — **never a detector score**.

### Non-negotiable principles from the brief
- **Source hierarchy:** Tier 1 = the paper (StoryScope). Tier 2 = authors' code/data. Tier 3 =
  other humanizer repos/skills/prompts. Tier 4 = creator videos. Tier 5 = general writing knowledge.
  The paper is authoritative **for what it actually establishes** — it does not override author
  intent, writing-quality judgment, or questions it never studied (it's a fiction *detection* study,
  not a quality or generation study).
- **§25 safeguard (the most important):** a statistical human/AI difference is NOT automatically a
  quality target. For every feature distinguish AI-correlated vs. bad-writing vs. useful-intervention.
- **Domain caution:** the paper studies *fiction*. Do not silently generalize to email/essay/report/
  technical/marketing. Classify: directly-supported / plausibly-transferable / domain-specific /
  unsupported.
- **Two stages:** Diagnose (find research-supported tendencies) THEN intervene (only what improves).
- **Modes:** WRITE, REWRITE, DIAGNOSE, LIGHT EDIT, DEEP EDIT, DOMAIN-AWARE (inferred, not CLI flags).
- **Use Codex/GPT Astral as an independent PEER + adversary**, and run steerable
  `/codex:adversarial-review` before finalizing. Reject ideas from any source, incl. the brief.
- **Deliverables:** SKILL.md; paper-notes; evidence-map; secondary-source analysis; rejected-ideas;
  examples; eval rubric; regression tests; README; peer/adversarial-review record; final build report.

## Evidence base (Tier 1)
**Paper:** *StoryScope: Investigating idiosyncrasies in AI fiction* (Russell, Rajendhran, Pham,
Iyyer, Wieting — UMD + Google DeepMind, COLM 2026). Narrative structure alone separates human vs
AI fiction at 93.2% macro-F1; 30 core features in ~7 themes; surface style editing barely dents it.
**Domain = published literary short fiction (~5k words).** Full extraction in `paper-notes.md`.

## Agents & sessions
- **Claude (Opus 4.8):** lead researcher/implementer.
- **GPT Astra = `gpt-6-astra`** (user's "GPT Astral"): independent peer/adversary. **SINGLE persistent
  session `01a0a015-6da6-7121-b18c-55892ce0945a`** — always `codex exec resume` it, never spawn a new
  Astra session (see `.astra-session`).
- **Sol = `gpt-5.6-sol`:** ran ONE early paper-fidelity review (a separate one-off session, now closed).
  Its 15 objections are recorded in `adversarial-review.md` Round 1. Astra had NOT seen these until now.

## Phase status
- **A Environment** ✅ — repo is a git repo; paper + sources located; all `research-materials/`
  converted to text in `research/research-materials/codex-converted/` (PDFs, docx, 4 video transcripts).
- **B Paper deep-read** ✅ — `paper-notes.md` (30 core features, 7 themes, scope caveats).
- **B-review Sol peer review** ✅ — 15 objections; adjudicated in `paper-notes.md §10`; a real
  row-shift error was fixed via pypdf re-extraction; confound + validity caveats added.
- **C Secondary sources** ✅ — `secondary-sources.md` (provenance ledger). Key finding: existing
  humanizers work mostly at the *surface/lexical* layer; the genuine gap they leave is
  discourse-level narrative diagnosis. We adapt their architecture/stance (blader "default-choice"
  heuristic + weak-alone + rescoped integrity rule; Matt-Payne mode-detection + carve-outs +
  references/ layout; humanizeai "also check what's missing / flag don't flatten"); we reject their
  folklore and don't inherit their overstated claims.
- **D Synthesis council (Claude ↔ Astra)** ✅ — Astra independently re-derived and improved the
  taxonomy. Reconciled to **6 conditional diagnostic lenses** (below). Logged in
  `adversarial-review.md` Round 2. `structural-patterns.md` being updated to the reconciled version.
- **D-remediation (Astra R3 pre-build gate)** ✅ — all 12 Part-B fixes applied in-place: stale
  prescriptions removed from paper-notes (S3/S6/S7, §9), corpus scope widened to multi-genre,
  deterministic-verdict language removed, no-fabrication rescoped for fiction, secondary-sources
  de-overstated (Twain arithmetic, checklist-absence, sed damage), rejected-ideas rationales
  repaired, provenance separated from authority. `evidence-map.md` created (must-fix #3).
- **E Build** ✅ — `SKILL.md` (root), `README.md`, `evidence-map.md`, `examples/examples.md`.
- **F Evals** ✅ — `evals/rubric.md` (three-way U/O/H comparison), `evals/cases.md` (positive +
  regression + adversarial cases).
- **G Adversarial review** ✅ — **R4** (Astra, 5-hat, SKILL.md) → SHIP-AFTER-FIXES, 8 fixes applied;
  **R5** (Astra @ **xhigh**, full package) → SHIP-AFTER-FIXES, 6 more fixes applied (examples/evals/
  README honesty + residual directional wording). Final Astra sign-off DID run (extra-high) and its
  fixes are in. `evals/smoke-test.md` executed (n=1 plumbing check).
- **H Polish** ✅ — reference set remediated, provenance/authority separated, all directional residue
  neutralized across SKILL/evidence-map/examples/evals/README.
- **STATUS: HumanScope v1 COMPLETE & reviewed.** 5 independent review rounds (Sol ×1, Astra ×4).
  All brief deliverables produced. Remaining future work (not blocking): run the full blind U/O/H
  eval with human raters to test *efficacy* (spec only so far).

## Current reconciled taxonomy (end of Phase D) — 6 diagnostic LENSES, not defaults
Each edit must fill: **textual evidence → intended reader effect → present failure → smallest useful
change** ("more human-correlated" may NOT fill the failure slot; §25 governs the action).
1. **Explanation & interpretation** — match explicit meaning to what this reader needs / author wants inferable.
2. **Presentation choices** — description, interiority, emotion, dialogue must earn their attention.
3. **Causality & closure** — test adequacy of causes/endings; structural loosening only on request.
4. **Information order** — arrange knowledge for intended effect while preserving comprehension.
5. **Referential grounding** — concrete references when relevant; substantiate facts when needed (real only).
6. **Reader relationship** — keep the intended narrator/reader relationship; direct address not required.
Plus 3 editorial (non-paper) lenses to consider: selection/relevance, attention/proportion,
character-specific necessity (fiction).

## Repo layout (user directive: ONLY the skill is visible in root; all model-generated /
## research artifacts live under `research/`)
```
HumanScope/
├── SKILL.md            # the skill (root, visible)   — Phase E, not yet written
├── README.md           # front door                   — Phase E, not yet written
├── examples/           # skill before/after cases     — Phase F
├── evals/              # cases · rubric · regression  — Phase F
└── research/           # ALL provenance + model-generated output
    ├── roadmap-and-state.md   (this file — source of truth)
    ├── paper-notes.md         (Tier-1 extraction + Sol adjudication §10)
    ├── evidence-map.md        (all 30 features → lens → hypothesis → applies → counterexample → eval) ✅
    ├── structural-patterns.md (higher-order synthesis → 6 lenses)
    ├── secondary-sources.md   (Tier 3/4 provenance ledger)
    ├── limitations.md         (10 scope/validity boundaries)
    ├── rejected-ideas.md      (13 folklore items killed)
    ├── adversarial-review.md  (Sol R1 + Astra R2, cleaned)
    ├── raw-model-output/      (verbatim Sol/Astra dumps)
    ├── extracted/             (paper text, table re-extractions)
    └── research-materials/    (original sources + codex-converted transcripts)
```
Paths inside research/*.md are written relative to repo root (e.g. `research/extracted/StoryScope.txt`).
Astra session pin lives in root `.astra-session` (hidden).
