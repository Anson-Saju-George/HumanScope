# Paper Notes — StoryScope (Tier 1, PRIMARY AUTHORITY)

> **Full read completed.** This file is a rigorous extraction of the primary paper, not a
> summary of the abstract. Every HumanScope principle must trace back to a row here.
> Where I infer beyond what the paper shows, it is flagged `[INFERENCE]`.

## 0. Bibliographic identity (confirmed from the document itself)

- **Title:** *StoryScope: Investigating idiosyncrasies in AI fiction*
- **Authors:** Jenna Russell, Rishanth Rajendhran, Chau Minh Pham, Mohit Iyyer, John Wieting
- **Affiliations:** University of Maryland, College Park; Google DeepMind
- **Venue:** Published as a conference paper at **COLM 2026**. arXiv:2604.03136v6 [cs.CL], 10 Aug 2026.
- **Code/data:** https://github.com/jenna-russell/storyscope

The prior clue ("StoryScope") was **correct** on paper identity. It is NOT the name of our
skill — our skill is *HumanScope*, and it is *not* required to reproduce anyone's prior
implementation.

---

## 1. What the paper actually is (and is not)

**Central question:** Can AI-generated *fiction* be distinguished from human-written fiction
using **discourse-level narrative choices** (plot, agency, temporal structure, revelation) —
i.e. *without* relying on surface style (word choice, sentence rhythm, em-dashes, "delve")?

**Answer:** Yes. Narrative features alone reach **93.2% macro-F1** for human-vs-AI detection
(vs. 96.0% with style added) — retaining >97% of the full model's performance. A compact
**30 "core" features** retain ~91% of the narrative model's signal (84.8% macro-F1).

**What it is NOT:**
- NOT a study of emails, essays, reports, marketing, academic prose, docs, or social media.
- NOT a study of "good vs bad" writing. Its labels are **authorship** (human vs AI), not quality.
- NOT a causal study. Every feature is a **descriptive / correlational classifier signal**.
- NOT a claim that these features *should* be edited. That inference is ours to justify or reject.

---

## 2. CRITICAL SCOPE FACTS (read before trusting any finding)

These govern how far ANY finding can travel. They are the backbone of `limitations.md`.

| # | Fact | Why it matters for HumanScope |
|---|------|------------------------------|
| S1 | **Domain = published anthology short fiction, multiple genres** (incl. mystery, horror, fantasy, SF). Stories avg **4,753 words** (~5,000). | Findings are *observed in this corpus* of narrative fiction — NOT established for every similarly-sized narrative, and NOT for non-fiction. Everything outside is transfer inference (B/C/D tiers). "Literary" alone would wrongly exclude the genre material. |
| S2 | **"Human" = PUBLISHED anthology fiction** extracted from Books3 (Presser, 2020). | The "human" side is *published* short fiction — not average/everyday writing. Publication does **not** verify each story's editing history or polish, so "write like a published author" is an approximation, not a guarantee of craft. |
| S3 | **"AI" = one generation per reverse-engineered prompt** from 5 frontier models (Gemini 3 Flash, Kimi K2.5, DeepSeek V3.2, Claude Sonnet 4.6, GPT-5.4); prompts inferred from each human story by Gemini 2.5 Flash. | The paper reports **no iterative revision**; but "un-steered / zero-shot / unedited first draft" are **not established facts** (decoding, retries, selection, system steering are unspecified — Codex #11). Says nothing about heavily human-directed or edited AI. |
| S4 | **Features are LLM-extracted**, not human-coded. GPT-5.1 builds templates/features; Gemini 3 Flash assigns feature values (**Gemini is also one of the 5 authors** → possible correlated measurement bias). Validated: Krippendorff α=0.90 (repeatability), human–model κ=0.84 on 240 items / 12 stories / 2 annotators. | Reliable but **not ground truth**, and aggregate agreement does not validate every core feature individually. |
| S5 | **All results are distributional means with heavy overlap.** Even the biggest gap (embodied emotion, 81% vs 38%) is a *tendency*. AI-AI centroid distance 4.3 vs human-AI 6.6. | **No deterministic authorship or quality verdict is justified** for any single text (a probabilistic signal does exist). Treat each feature as a *context-dependent descriptive feature*, never a target value — categorical options are not continuous dials. |
| S6 | **Signal is redundant across dimensions** (Table 8 ablation): no single NarraBench dimension is sufficient (best: agents 80.2%) or necessary (worst removal −1.2). Features **co-occur**. | Table 8 is a *predictive* ablation, NOT an editing experiment — it does **not** show that editing one feature "barely moves the needle," and does **not** establish checklist inferiority. It supports a *holistic* reading only as a usability/compositional-dependency argument. |
| S7 | Narrative features are **robust to one span-level style rewriter** (LAMP on 278 Gemini stories drops detection 1.6 pts). | Evidence that *this particular* local span-editing barely changed *this* classifier — real support for "surface edits ≠ structural change," but do **not** generalize to all surface/mixed/developmental editing, nor claim every underlying feature was unchanged. |

---

## 3. Method (compressed)

- **Corpus:** 10,272 human stories × (1 human + 5 LLM) = **61,608 stories**, 304 features each.
- **Framework:** NarraBench taxonomy (Hamilton et al. 2025); 10 of 12 dimensions adopted:
  Agent, Social Network, Event, Plot, Structure, Setting, Time, Revelation, Perspective, Style.
  (Excluded: Paratext, Motivation — need external context.)
- **Pipeline:** (1) prose → structured JSON template per dimension (strips surface style);
  (2) cross-source comparative analysis over 600-story discovery pool → observations;
  (3) feature discovery → 408 candidate closed-form questions → dedup to **304 features**.
- **Classifier:** XGBoost + SHAP for per-feature importance. Bootstrap SHAP (B=50) →
  **30 core features** (stable, important, hold across all 5 AI models) + **75 fingerprint features**.
- **Core-feature bar (App. D):** stable-important quadrant, null significance, stability ≥0.55,
  top-quartile ≥0.60, **|human−AI mean gap| ≥ 0.20**, cross-model AI spread ≤ 0.35.

Text-based baselines (ModernBERT, stylometric/TF-IDF XGB) hit ~99.7–99.9% — raw text is
trivially separable. The paper's *point* is interpretability + durability, not beating them.

---

## 4. THE 30 CORE FEATURES (Table 16) — grouped into 7 themes

Values: `s` = 1–5 Likert mean; `o` = ordinal mean; `%` = prevalence of a categorical option.
**Gap = Human − AI.** Negative = AI does MORE of it. (AI column = avg across all 5 models.)
Note: PDF extraction slightly misaligned a few numeric cells; directions/themes are exact,
a couple of individual magnitudes are approximate and marked `~`.

### AI-ELEVATED themes (AI overdoes these vs. published human authors)

**T1 — Thematic over-determination** (AI spells out meaning instead of trusting the reader)
| Feature | Human | AI | Gap |
|---|---|---|---|
| Thematic Explicitness & Moralizing (s) | 3.28 | 3.94 | −0.65 |
| Moral/Philosophical Weighting (s) | 3.26 | 3.68 | −0.42 |
| Thematic Unity — subplots serve one central theme (s) | 4.41 | 4.74 | −0.33 |
| Narratorial Thematic Commentary = yes | 52% | 77% | −25 |
| Dialogue Function = philosophical debate | 34% | 59% | −25 |
| Reference Explicitness = implicit echoes | 50% | 72% | −22 |

**T2 — Sensory & embodied performativity** (AI renders emotion through the body/senses/setting)
| Feature | Human | AI | Gap |
|---|---|---|---|
| Dominant Emotional Expression = embodied metaphors | 38% | 81% | **−42** (largest gap) |
| Setting as Psychological Mirror (s) | 3.58 | 4.07 | −0.49 |
| Environmental & Ecological Emphasis (s) | 2.83 | 3.21 | −0.38 |
| Dominant Sensory Modalities = olfactory (smell) | 57% | 82% | −26 |
| Sensory Density (s) | 3.66 | 3.93 | −0.26 |
| Depth of Interior Access (s) | 3.67 | 3.93 | −0.26 |

**T3 — Structural streamlining** (AI = tidy, linear, single-track, protagonist-resolved)
*(Values re-verified against pypdf raw extraction of Table 16, page 26 — the earlier
`-layout` dump had row-shifted two rows; corrected here.)*
| Feature | Human | AI | Gap |
|---|---|---|---|
| Continuity of Main Causal Chain (s) | 3.92 | 4.20 | −0.28 |
| Spatial Granularity (o) | 2.27 | 2.53 | −0.26 |
| Agency in Resolution = protagonist choice | 46% | 69% | −23 |
| Character Introduction = external description | **30%** | **52%** | −22 |
| Subplot Integration = no subplots | **57%** | **79%** | −22 |
| Mode of Resolution = internal understanding/acceptance | 27% | 47% | −21 |
| Opening Spatial Grounding (o) | 2.12 | 2.33 | −0.20 |
| Pre-Threat Character Investment (s) | 2.76 | 2.99 | −0.23 |

### HUMAN-ELEVATED themes (published authors do MORE of these)

**T4 — Intertextual richness** (real, named references to the outside world)
| Feature | Human | AI | Gap |
|---|---|---|---|
| Intertextual Strategy = explicit named reference | 47% | 24% | +23 |
| Reference Explicitness = balanced mix (explicit+implicit) | 37% | 16% | +21 |

**T5 — Reader engagement** (breaking the fourth wall, addressing the reader)
| Feature | Human | AI | Gap |
|---|---|---|---|
| Fourth-Wall Permeability (o) | 0.67 | 0.39 | +0.28 |
| Frequency of Direct Reader Address (o) | 0.28 | 0.07 | +0.21 |
> ⚠️ **Paper-internal inconsistency (Codex-flagged, verified):** Table 16 lists these as
> *ordinal means* (0.67/0.39, 0.28/0.07 over integer codes). But §4.1 prose reports the same
> features as *prevalence percentages* — "break the fourth wall far more often (67% vs 39%)"
> and "address the reader directly more frequently (28% vs 7%)." These cannot both be literal.
> HumanScope should rely only on the **direction** (humans do more), not the magnitude.

**T6 — Temporal complexity** (nonlinearity, flashbacks, delayed disclosure)
| Feature | Human | AI | Gap |
|---|---|---|---|
| Depth of Recontextualization After Surprise (s) | 3.28 | 2.95 | +0.34 |
| Degree of Chronological Discontinuity (s) | 2.40 | 2.12 | +0.28 |
| Nonlinear Framing for Delayed Disclosure (s) | 1.96 | 1.68 | +0.28 |
| Anachrony Intensity — flashbacks/flash-forwards (s) | 2.58 | 2.31 | +0.27 |

**T7 — Narrative diversity** (breadth of locations, dialogue, subplots, moral ambiguity)
| Feature | Human | AI | Gap |
|---|---|---|---|
| Location Variety Scope (o) | 1.34 | 1.08 | +0.26 |
| Dialogue-to-Narration Proportion (s) | 2.95 | 2.70 | +0.24 |
| Subplot Integration = thematically parallel | 42% | 21% | +22 (as reported) |
| Moral Polarity toward Protagonist = ambivalent/mixed | 59% | 38% | +21 (as reported) |
| Dominant Emotional Expression = explicit labels | 29% | 8% | +21 |

> **Note the T2/T7 relationship (descriptive only):** across the corpus, AI's *dominant* way of
> conveying emotion is embodied metaphor (81%) while its explicit-label rate is low (8% vs 29%
> human). This is a **corpus-level dominant-category frequency, NOT a within-story measurement** —
> the paper does not show the same author switching registers inside one story, nor that dominant
> embodiment is a defect. So this is NOT evidence for a "name feelings more" or "balance/variety"
> rule. The only defensible, still-hypothetical reading: *inspect whether a specific passage leans
> on one device past the point of effect* — judged from the text, not from this statistic.

> **Count caveat (verified):** These are **30 unique features**, not 33 independent levers. Three
> *categorical* variables appear on BOTH sides with a different **elevated option** per source:
> **Emotional Expression** (AI→embodied 81% / Human→explicit labels 29% — note explicit labels is
> the human-*elevated* option, not the human *modal* category), **Reference Explicitness**
> (AI→implicit echoes 72% / Human→balanced mix 37%), and **Subplot Integration** (AI→no subplots
> 79% / Human→thematically parallel 42%). Treat each as ONE categorical distribution, not two
> separate rules, or it will **double-count these three constructs** and overstate their weight.

---

## 5. Prose findings (§4.1) — the paper's own plain-language summary

- **"AI over-explains its themes."** Narrators state the lesson 77% vs 52%; philosophical
  dialogue 59% vs 34%; vague allusions 72% vs 50%. *"AI spells out meaning rather than
  trusting the reader to infer it."* (over-determination)
- **"Human authors subvert linearity."** Tighter causal chains, protagonist-driven resolutions
  (69% vs 46%), fewer subplots (79% "no subplots" vs 57%), internal-acceptance endings
  (47% vs 27%). Humans use time jumps/flashbacks/nonlinearity; are comfortable with
  ambiguous endings. *"A human mystery might open at the funeral and spiral backward; AI
  tells it from first clue to grand reveal."*
- **"AI over-writes the body and senses."** Emotion via physical sensation 81% vs 38%;
  smell imagery 82% vs 57%; setting-as-inner-state heavier. Explicit emotion labels 8% vs 29%.
  *"Where a human writes a character 'felt afraid,' AI renders tightening chest, cold sweat,
  dimming lamplight."*
- **"Human authors engage the outside world."** Named texts/authors 47% vs 24%; fourth-wall
  breaks 67% vs 39%; direct reader address 28% vs 7% *(⚠ these two %s conflict with Table 16's
  ordinal means for the same features — see the T5 quarantine note above; use direction only)*.
  *"AI writes as though no one is watching."*
- **"AI has less diverse narrative features."** Humans span more locations, more dialogue,
  integrate subplots into theme (42% vs 21%), morally ambivalent protagonists (59% vs 38%).

## 6. Diversity / convergence findings (§5)

- **AI models converge** into one shared narrative region; **human stories are more dispersed**
  (human radius 22% larger; 10-NN radius 1.13×).
- **Human stories are rarer:** mean rarity percentile 0.71 vs 0.49 (Cohen's d = 0.83). The human
  version is the rarest of the six 57.8% of the time (vs 16.7% chance).
- The 6 most-confused source pairs are all **AI–AI**. AI ≈ "a shared house style."

## 7. Per-model fingerprints (Table 17) — of interest because our host is Claude

- **Claude:** most distinctive AI model. **Flattest event escalation**, most uniform narrative
  voice, *reverent/continuist* toward tradition (62%), favors epilogues, avoids dream sequences,
  quiet endings over "avalanche" endings. → *These are observed **fingerprints of the tested
  Claude Sonnet 4.6 version** — descriptive tendencies, NOT defects. A quiet ending or flat
  escalation can be exactly right; note them as habits to stay aware of, not things to "fix."*
- **GPT:** gossip/rumor as plot (64%), distant retrospective framing, subverts expectations more.
- **Gemini:** external character description default; tidiest/extended denouements; bleak settings.
- **DeepSeek:** front-loads crucial context; narrator presence high.
- **Kimi:** fewest fingerprints; "generic center" of the AI distribution; in-action introductions.

---

## 8. Evidence-strength ledger (feeds evidence-map.md)

| Claim | Evidence type | Strength |
|---|---|---|
| Narrative features separate human/AI fiction | Supervised classifier, 93.2% F1, large corpus, CIs | **Strong** (descriptive) |
| The 7 themes/30 features characterize the gap | SHAP + bootstrap stability, held-out test | **Strong** (descriptive/correlational) |
| Differences survive style editing | LAMP rewrite experiment, −1.6 pts | **Strong** |
| Human writing is rarer/more diverse | Distance/rarity stats, Cohen's d=0.83 | **Strong** |
| These features are *causal* drivers of quality | — | **None. Not tested.** |
| These features should be edited toward human values | — | **None — our design inference, must be justified per §25 of brief** |
| Findings transfer to non-fiction | — | **None — paper is fiction-only** |
| The corpus is a *controlled parallel* of authorship | — | **Weak — matched-premise only; AI prompt was reverse-engineered from the finished human story (confound, see §10.2)** |
| The 30 features are *durable* across future models | Conclusion language | **Overstated — no external/temporal holdout; "durable" is a hypothesis (§10.12)** |

---

## 9. Immediate implications for HumanScope (revised after Codex peer review)

1. **The paper's real thesis is our thesis.** Surface "humanizers" (ban em-dashes, kill "delve")
   miss the actual human/AI gap, which lives in *narrative construction*. HumanScope should be
   built on structure, not lexical bans (§4 of brief vindicated by finding S7). *(Codex #14:
   scope S7 precisely — one span-level rewriter barely moved one classifier; state it that way,
   don't overgeneralize to "all surface editing.")*
2. **No optimization objective — diagnose per instance.** ~~Widen toward the human distribution~~
   and even ~~"prefer non-default choices"~~ were both overreach (Codex #8/#9; Astra #8): a
   "non-default" or "rarer" choice is not shown to be *better* (a random incoherent combination is
   also rare/non-default; rarity is a task-dependent originality proxy measured in a space built to
   separate sources). Corrected stance: **for a specific passage, ask whether a more specific,
   coherent, purpose-appropriate choice would serve THIS reader better — and if you cannot name the
   failure, change nothing.** Diversity is a property of a *body of work*, never a per-piece target.
   "Minimum effective intervention" (brief §8) holds.
3. **Domain gating is mandatory — and must be per feature × genre × purpose, not per theme.**
   (Codex #10.) Directly valid only for fiction (S1/S2). Some features *reverse* outside fiction:
   e.g. T3 "structural streamlining" is a *virtue* in reports/docs; T4's human-direction (named,
   explicit references) transfers *well* to non-fiction; T2/T5/T6 are mostly wrong for a memo.
4. **The "human" target is *published literary* fiction (S2) — treat alignment-with-quality as a
   HYPOTHESIS, not a fact.** (Codex #1.) The labels are *provenance*, not quality/preference/merit.
   "Published" is not an outcome measure. Every feature enters HumanScope as a *diagnostic
   correlate*, and may only be promoted to a "principle" with an independent quality rationale.
5. **Largest, most stable *differences*** (by gap × stability, descriptive only — NOT "levers to
   pull"): embodied-emotion dominance (−42), thematic explicitness (−0.65 / 77%), the
   structural-streamlining cluster, and the human diversity/temporal-complexity/intertextual
   clusters. These are candidate *diagnostic lenses*, each gated by the §25 audit below.
6. **§25 audit is the core safeguard.** For each difference: is a human-ward move a *quality* move
   or merely *AI-correlated*? "More olfactory imagery" is backwards (smell is AI-elevated); but
   "strip all interiority/senses" makes prose inert (Codex #3); and "add register variety" is
   itself an unsupported prescription (Astra) — a corpus statistic can't prove within-story
   repetition. The only defensible action is: *inspect the actual passage for a device leaned on
   past the point of effect*, never a directional rule. Full per-feature audit lives
   in `evidence-map.md`.
7. **Success metric is NEVER a detector score.** (Codex #15, brief §10/§23.) Raw-text baselines
   already hit 99.7–99.9%; optimizing toward the narrative classifier would just be dressed-up
   detector evasion. HumanScope's success = blind reader/editor preference, fidelity to author
   intent, coherence, specificity — measured in `evals/`.

---

## 10. Codex independent peer-review — adjudication log

Codex (`gpt-5.6-sol`) independently read `research/extracted/StoryScope.txt` + my notes and returned 15
objections. Full raw output: `research/adversarial-review.md`. Verdict (Codex, quoted):
> *"Trustworthy as a descriptive extraction after several corrections, but not yet trustworthy as
> the intellectual specification for HumanScope; it repeatedly turns authorship correlations into
> editorial guidance."*

**Accepted — FIDELITY (fixed above):**
- **10.5** T3 row-shift: Character Introduction = 30/52 (not 57/79); no-subplots = 57/79 (not
  27/47). ✅ corrected via pypdf re-extraction.
- **10.6** 30 *unique* features, not 33 — three categoricals double-listed. ✅ count caveat added.
- **10.7** Fourth-wall/reader-address are ordinal means in Table 16 but %s in §4.1 prose —
  paper-internal inconsistency; use direction only. ✅ flagged.

**Accepted — interpretation (design changes above):**
- **10.1 / 10.3 / 10.15** Provenance ≠ quality; every feature is a hypothesis; success ≠ detector
  score. → §9.4, §9.6, §9.7.
- **10.2 CONFOUND (important, I missed it):** the corpus is *matched-premise*, not controlled
  parallel authorship. The AI prompt was **reverse-engineered by Gemini from the finished human
  story** (paper L193–200) and explicitly preserves theme/mood/conflict/details (L1863–87). The
  human author was never constrained by that prompt. So AI's thematic explicitness, tidy plots,
  and spatial grounding may **partly be artifacts of lossy summarization + prompt compliance**,
  not intrinsic AI style. → down-rank those features; documented in `limitations.md`.
- **10.4** Table 8 is a *predictive* ablation, not an editing experiment — it does NOT prove
  "editing one feature barely moves the needle." Keep the holistic design, but justify it from
  *compositional dependencies + usability*, and it's fine to use a checklist as an internal
  diagnostic (just don't optimize items independently). → corrected my S6 overclaim.
- **10.8 / 10.9** "Widen toward human breadth / rarity" reframed to "avoid default, choose
  coherent specificity." → §9.2.
- **10.10** Gate at feature × genre × purpose. → §9.3, drives `domain` handling in SKILL.md.

**Accepted — limitations to document (→ `limitations.md`):**
- **10.11** "Single-shot zero-shot AI draft" is under-documented by the paper (only *template
  extraction* is stated zero-shot); say "one generation per standalone prompt, no iterative
  revision reported."
- **10.12** No external-validity corpus (same Books3 pipeline for train/test; no unseen model
  family, no temporal holdout) → "durable" is a hypothesis, not a result.
- **10.13** Measurement pipeline: GPT-5.1 builds features, Gemini 3 Flash assigns them *and* is
  one of the evaluated authors; human validation is only 12 stories / 240 items / 2 annotators.
  Reliability (κ=0.84) ≠ construct validity.
- **10.14** LAMP = one span-rewriter (Gemini) on 278 Gemini stories; don't generalize to all editing.

**Net effect on the build:** no finding was invented or discarded, but the *framing* shifts
decisively from "edit prose toward the human values" to "**diagnose default/AI-correlated habits;
intervene only where a more specific, coherent, genre-appropriate choice improves the writing;
prove it with reader preference, never a detector.**" This is exactly the safeguard the brief's
§25 demanded, now hard-coded into the design.
