# Limitations & Scope Boundaries

The honest boundary of what StoryScope licenses HumanScope to claim. Every SKILL.md rule must
survive these caveats. Sources: the paper itself + the Codex/Sol peer review (paper-notes §10).

## 1. Domain: published anthology short fiction (multiple genres)
- Corpus = short stories averaging **4,753 words**, spanning genres (mystery, horror, fantasy, SF,
  literary). Findings are **observed in this corpus**, not established for every similarly-sized
  narrative, and not for non-fiction. Micro-fiction, novels, poetry, scripts were not studied.
  Everything non-fiction is **transfer inference**, rated per feature × genre × purpose.

## 2. "Human" = PUBLISHED anthology fiction (editing history unverified)
- Human stories come from **Books3 anthologies** (Presser, 2020) — *published* short fiction. This
  is NOT "how everyday people write." But **publication does not verify each story's editing history
  or polish**, so HumanScope's fiction target ("write like a published author") is an approximation
  that *may* correlate with quality but is **not demonstrated to** — the label is provenance, not
  merit (Codex #1).

## 3. "AI" = one generation per reverse-engineered prompt (protocol under-specified)
- Five frontier models (Gemini 3 Flash, Kimi K2.5, DeepSeek V3.2, Claude Sonnet 4.6, GPT-5.4),
  **one generation per standalone prompt, no iterative revision reported** (Codex #11). The paper
  documents only *template extraction* as zero-shot; **"un-steered / zero-shot / unedited first
  draft" are NOT established facts** — decoding, retries, selection, and system steering are
  unspecified. Says little about heavily human-directed or edited AI.

## 4. Prompt-construction confound — matched-premise, not controlled parallel (Codex #2, important)
- The "parallel corpus" was built by **reverse-engineering an AI prompt from each finished human
  story** (Gemini 2.5 Flash), and that prompt explicitly preserves theme, mood, conflict, and
  concrete details (paper L1863–1887). The human author was never constrained by it.
- **Consequence:** some AI "tells" — thematic explicitness, tidy plots, spatial grounding — may be
  partly artifacts of *lossy premise summarization + prompt compliance*, not intrinsic AI style.
  → Features plausibly induced this way (parts of P1 over-determination, P3 tidiness) are
  **down-ranked** until replicated with genuinely shared prospective prompts.

## 5. Features are LLM-extracted, not ground truth
- GPT-5.1 builds the templates and the 304-feature taxonomy; **Gemini 3 Flash assigns every
  feature value — and Gemini is also one of the five evaluated authors** (Codex #13). Repeatability
  is high (Krippendorff α=0.90) and human agreement decent (Cohen's κ=0.84), but validation covers
  only **12 stories / 240 items / 2 annotators**. Reliability ≠ construct validity.

## 6. Correlation, not causation or quality
- Every feature is a **descriptive classifier signal** that separates sources. The paper does NOT
  test whether any feature causes better/worse writing, or whether readers prefer the human
  direction. **A feature being "AI-like" is not evidence it is bad** (brief §25). This is the single
  most load-bearing caveat in HumanScope.

## 7. "Durable" is a hypothesis, not a result (Codex #12)
- No external-validity test: train and test prompts share the same Books3-derived pipeline; no
  unseen model family, no independently authored prompt set, no temporal/next-model holdout, no
  human-amateur or workshop-edited corpus. The claim that narrative features stay diagnostic as
  models evolve is plausible but **unproven**.

## 8. Distributional, heavily overlapping — no per-text verdict
- Even the largest gap (embodied emotion, 81% vs 38%) is a tendency with wide overlap. **No
  deterministic authorship or quality verdict is justified for any single text** — though a
  probabilistic signal does exist at the population level. HumanScope treats each feature as a
  *context-dependent descriptive feature*, never a pass/fail test and never a continuous target
  (categorical options are not dials).

## 9. The LAMP robustness result is narrow (Codex #14)
- "Surface editing doesn't remove the narrative signal" rests on **one** span-rewriter (Gemini) over
  278 Gemini stories, dropping detection 1.6 pts. Stable *classifier* performance does not prove
  every underlying narrative feature was unchanged. Real support for the thesis, but do not
  generalize to *all* editing (developmental edits, structural prompting, human revision untested).

## 10. Additional methodological boundaries (Astra R3)
- **Confound scope:** the prompt-construction asymmetry (§4) means *causal interpretation and
  generalization* are down-ranked — NOT the observed within-corpus association. Avoid inventing a
  numeric "confidence adjustment"; just don't read the association as intrinsic AI style.
- **Subplot denominator:** "thematically-parallel subplots 42% vs 21%" is measured across ALL
  stories (alongside 57%/79% having *no* subplots), so it cannot establish a human preference for
  parallel subplots *conditional on having subplots*.
- **Reporting/encoding inconsistencies:** §3 reports 1,377 test prompts / 8,262 stories; Appendix D
  reports 1,384 / 8,301; 24 model refusals; T5 fourth-wall/reader-address values conflict between
  Table 16 (ordinal means <1) and §4.1 prose (percentages) and Table 15's stated 1–4 scale. Flag,
  don't silently reconcile.
- **Rarity is reference-population dependent:** pooled nearest-neighbor density uses 5 AI sources
  vs. 1 human source plus scaling/encoding choices; treat "human writing is rarer/more original"
  cautiously, not as author-independent fact.
- **Prompt-level split ≠ author-level split:** the paper does not establish generalization to
  unseen human authors.
- **Checks the paper DID run (credit where due):** length-matching, memorization/overlap screening,
  and topic analyses — these strengthen the *detection* result but do NOT validate any individual
  feature as an editing rule.
- **No feature-specific quality experiment exists** — the gap from "feature separates sources" to
  "editing this feature improves writing" is entirely unbridged by the paper.

## 11. What HumanScope therefore must NOT do
- Must not present fiction findings as universal writing law.
- Must not treat the human direction of any feature as automatically better.
- Must not optimize toward any detector/classifier (raw-text baselines already hit 99.7–99.9%;
  chasing them = detector evasion, which we reject).
- Must not present **invented material as real-world evidence, testimony, citation, or author
  biography** — though *fictional* invention is allowed when the task is fiction (scoped integrity
  rule, not a blanket no-invention ban).
- Must not "add imperfection / lower the reading level" to seem human — that folklore conflicts with
  the *goal* (better writing); the published-corpus fact is secondary (see rejected-ideas.md).
