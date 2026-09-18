# Adversarial / Peer Review Record

> ⚠️ **FROZEN HISTORICAL RECORD — not current instructions.** This file preserves each review round
> verbatim for provenance. Objections here have been ADJUDICATED; some recommendations were
> accepted, some rejected, some superseded by later rounds. **The current, authoritative spec lives
> in `structural-patterns.md` (taxonomy), `paper-notes.md` (evidence + §10 adjudication),
> `limitations.md`, and `SKILL.md`.** Do not follow a raw objection below as if it were a live TODO
> without checking it against those files. Rounds: R1 = Sol (paper fidelity) · R2 = Astra (synthesis
> council) · R3 = Astra (full-context pre-build audit). Paths shown in older rounds may predate the
> move to `research/`.

## Round 1 — Codex (gpt-5.6-sol) independent read of StoryScope + paper-notes.md
_Invoked 2026-09-14. Codex read the paper text and paper-notes.md directly and was instructed to attack, not agree. Adjudication in paper-notes.md §10._

VERDICT: Trustworthy as a descriptive extraction after several corrections, but not yet trustworthy as the intellectual specification for HumanScope; it repeatedly turns authorship correlations into editorial guidance.

1. [OVERREACH] The study does not establish that moving prose toward the human centroid improves it.

   - Claim: Published-human alignment “conveniently aligns with quality” and supplies HumanScope’s main levers (notes 219–224).
   - Risk: The labels are provenance, not quality, reader preference, effectiveness, or literary merit. “Published” is not an outcome measure. The paper only says the features separate sources ([StoryScope.txt:385](/D:/main-projects/LIVE-ACTIVE/HumanScope/extracted/StoryScope.txt:385)).
   - Do instead: Treat every feature as a hypothesis. Require independent reader/editor evaluation before promoting it from “diagnostic correlate” to “writing principle.”

2. [MISSED] The supposedly parallel corpus has a major prompt-construction confound.

   - Claim: Humans and AIs are mirrors written from equivalent prompts.
   - Risk: The human story existed first; Gemini reverse-engineered an AI prompt from that completed story ([193–200](/D:/main-projects/LIVE-ACTIVE/HumanScope/extracted/StoryScope.txt:193)). That prompt explicitly preserves “thematic direction,” mood, conflict, and concrete details ([1863–1887](/D:/main-projects/LIVE-ACTIVE/HumanScope/extracted/StoryScope.txt:1863)). The human author was never constrained by it. AI thematic explicitness, tidy plots, and spatial grounding may partly reflect lossy summarization and prompt compliance.
   - Do instead: Describe this as matched-premise, not controlled parallel authorship. Down-rank features plausibly induced by prompt construction until replicated with genuinely shared prospective prompts.

3. [QUALITY-TRAP] None of the seven themes licenses a monotonic “edit toward human” rule.

   - T1, thematic over-determination: Reducing redundant moralizing is often useful in literary fiction, but lowering thematic unity or philosophical weight can weaken purposeful work.
   - T2, sensory/embodied performativity: Yes, “add olfactory imagery” is exactly backwards descriptively—olfaction is AI-elevated, 82% versus 57% ([484–491](/D:/main-projects/LIVE-ACTIVE/HumanScope/extracted/StoryScope.txt:484)). But “remove smell/body/interiority” is not a quality rule either; it can make prose inert. Target repetitive defaulting, not the modality.
   - T3, structural streamlining: The most dangerous theme. Moving humanward can mean weaker causal continuity, less protagonist agency, less pre-threat investment, poorer opening grounding, and more unresolved material. Those can plainly make a story worse.
   - T4, intertextual richness: Named references may add cultural specificity—or become gratuitous name-dropping, hallucination, anachronism, or borrowed authority.
   - T5, reader engagement: Fourth-wall breaks and direct address are conspicuous devices. Adding them routinely would produce gimmicky prose and violate many POV contracts.
   - T6, temporal complexity: Recontextualization can reward readers; gratuitous flashbacks and fragmentation damage clarity and momentum.
   - T7, narrative diversity: More locations, dialogue, and parallel subplots can simply create bloat. Explicit emotion labels can be blunt. Moral ambiguity is not universally appropriate.
   - Do instead: Frame every feature as a context-conditioned diagnostic: “Is this choice earned, varied, and appropriate?” Never as a target value.

4. [STRUCTURE] Table 8 does not prove that a holistic editor is superior to a checklist.

   - Claim: Redundant dimension signal means a “holistic gestalt,” and editing one feature “barely moves the needle” (notes 49–50, 213–215).
   - Risk: Table 8 is a predictive feature-group ablation over all 257 narrative features—not an editing intervention, not an ablation of the 30 core features, and not a quality experiment. It shows that correlated dimensions substitute for one another in an XGBoost classifier ([1304–1312](/D:/main-projects/LIVE-ACTIVE/HumanScope/extracted/StoryScope.txt:1304)); it says nothing about the effect of changing one feature in prose.
   - Do instead: Keep the holistic design, but justify it from compositional dependencies and usability—not Table 8 alone. A checklist can still be useful as an internal diagnostic, provided it is not independently optimized item-by-item.

5. [FIDELITY] The structural-streamlining numbers contain a real row-shift error.

   - Claim: Character introduction is 57% human versus 79% AI; no-subplots is 27% versus 47%.
   - Wrong: Table 16 gives:

     - external character introduction: 30% versus 52%;
     - no subplots: 57% versus 79%;
     - internal-understanding resolution: 27% versus 47%.

     See [StoryScope.txt:1744](/D:/main-projects/LIVE-ACTIVE/HumanScope/extracted/StoryScope.txt:1744).
   - Do instead: Correct notes 109–111 and any downstream weighting based on those magnitudes.

6. [FIDELITY] “30 features” is being represented as 33 independent levers.

   - Claim: Section 4 presents the 30 core features.
   - Risk: It lists 33 directional rows because three categorical variables appear on both sides with different elevated options: emotional expression, reference explicitness, and subplot integration. Tables 14 and 15 contain 20 + 13 markers but only 30 unique feature questions ([1513–1515](/D:/main-projects/LIVE-ACTIVE/HumanScope/extracted/StoryScope.txt:1513), [1707–1713](/D:/main-projects/LIVE-ACTIVE/HumanScope/extracted/StoryScope.txt:1707)).
   - Do instead: Represent each as one categorical distribution. Otherwise HumanScope will double-count three constructs and exaggerate their importance.

7. [FIDELITY] The fourth-wall and reader-address “percentages” are statistically unsafe.

   - Claim: Humans break the fourth wall 67% versus 39%, and directly address readers 28% versus 7%.
   - Risk: The paper’s prose itself says this ([493–498](/D:/main-projects/LIVE-ACTIVE/HumanScope/extracted/StoryScope.txt:493)), so your notes reproduce it faithfully. But Table 16 identifies 0.67/0.39 and 0.28/0.07 as ordinal means, while Table 15 defines multi-level ordinal response scales ([1647–1669](/D:/main-projects/LIVE-ACTIVE/HumanScope/extracted/StoryScope.txt:1647), [1758–1760](/D:/main-projects/LIVE-ACTIVE/HumanScope/extracted/StoryScope.txt:1758)). They are not prevalence estimates.
   - Do instead: Record this as an internal paper inconsistency and report only “higher ordinal frequency/permeability,” not percentages.

8. [OVERREACH] “Human distributional breadth” is being converted into an individual-story objective.

   - Claim: HumanScope should widen each draft toward the human range and break convergence.
   - Risk: Greater population dispersion does not imply that every individual story should contain more kinds of devices. Nor does rarity equal quality. A random, incoherent feature combination can be extremely rare. Worse, rarity is measured in a feature space intentionally induced to distinguish sources ([279–308](/D:/main-projects/LIVE-ACTIVE/HumanScope/extracted/StoryScope.txt:279)), creating partial circularity when it is called “originality.”
   - Do instead: Define diversity across repeated outputs or a portfolio. For an individual story, optimize coherent specificity and non-default choices—not distance or rarity.

9. [OVERREACH] The T2/T7 tension is suggestive, not “the clearest proof” of a breadth target.

   - Claim: Humans “do both more evenly,” proving register variety.
   - Risk: The table reports corpus-level dominant-category frequencies: embodied metaphor and explicit labeling. It does not measure within-story switching, local register variety, or whether the same human authors use both effectively. Behavioral and ambiguous emotion categories are omitted from the summary.
   - Do instead: Hypothesize “avoid a dominant embodied-emotion default,” then directly measure repetition and register switching within drafts.

10. [SCOPE] Your fiction-only gating is correct, but gating by whole theme is too coarse.

   - T1: Useful analogue in essays—avoid repetitive thesis restatement. Harmful if it suppresses explicit conclusions in reports, legal analysis, or instructions.
   - T2: Mostly irrelevant or harmful in technical prose; potentially useful in speeches, narrative journalism, case studies, and persuasive examples.
   - T3: Reverse the fiction implication. Streamlining, explicit causal chains, strong openings, and single-track organization are usually virtues in reports and documentation.
   - T4: Strong legitimate analogue: explicit citations and named sources. “Implicit references” are generally worse in scholarly and technical work.
   - T5: Direct “you” is useful in tutorials and user documentation; fourth-wall play is usually inappropriate in formal prose.
   - T6: Recontextualizing earlier evidence is valuable. Chronological discontinuity and delayed disclosure are usually harmful when readers need efficient comprehension.
   - T7: Nuance, counterarguments, and calibrated uncertainty transfer well. Extra locations, dialogue, emotional labels, and subplots generally do not.
   - Do instead: Gate at feature × genre × communicative-purpose level, not at the seven-theme level.

11. [MISSED] “Single-shot, zero-shot AI first drafts” is not adequately documented by the paper.

   - Claim: S3 states this as a firm scope fact.
   - Risk: The paper explicitly calls the template extraction zero-shot ([270–277](/D:/main-projects/LIVE-ACTIVE/HumanScope/extracted/StoryScope.txt:270)), but does not comparably document story-generation decoding, retries, selection, or the absence of system-level steering. “Standalone prompt” does not establish every aspect of “zero-shot first draft.”
   - Do instead: Say “apparently one generation per standalone prompt, with no iterative revision reported.” Treat missing generation settings as a reproducibility limitation.

12. [MISSED] The external-validity evidence is much weaker than the held-out score suggests.

   - Claim: The 30 features are robust markers across frontier models.
   - Risk: Train/test prompts come from the same Books3-derived selection and generation pipeline. There is no external human corpus, unseen model family, independently authored prompt set, edited collaborative fiction, or later-model temporal holdout. “Durable” remains a hypothesis, despite the conclusion’s language ([668–678](/D:/main-projects/LIVE-ACTIVE/HumanScope/extracted/StoryScope.txt:668)).
   - Do instead: Before hard-coding principles, test on external magazines/anthologies, human amateur fiction, workshop-revised AI drafts, and new models not involved in discovery.

13. [MISSED] The LLM measurement pipeline has correlated-model and validation weaknesses.

   - Claim: κ = 0.84 makes the extracted features reliable enough to treat as ground truth.
   - Risk: GPT-5.1 builds the representations and feature taxonomy; Gemini 3 Flash assigns all values, while Gemini is also one evaluated author. The human validation covers only 12 stories, 240 items, and two annotators; annotator-model κ ranges from 0.77 to 0.91 ([1236–1251](/D:/main-projects/LIVE-ACTIVE/HumanScope/extracted/StoryScope.txt:1236)). Reliability is not construct validity.
   - Do instead: Validate the actual 30 core features on a much larger stratified sample with blinded literary scholars, including error rates by source and feature.

14. [OVERREACH] The LAMP result is narrower than “surface humanizing does not change narrative structure.”

   - Claim: S7 is strong evidence that surface editing generally misses the real signal.
   - Risk: The experiment covers 278 Gemini stories, one seven-category span-rewriting framework, and Gemini as rewriter. Detection fell only 1.6 points ([517–529](/D:/main-projects/LIVE-ACTIVE/HumanScope/extracted/StoryScope.txt:517)), but that does not cover developmental editing, structural prompting, human revision, or other “humanizers.”
   - Do instead: State: “This particular local span-editing intervention barely changed this classifier.” Do not generalize to all surface or mixed-level editing.

15. [MISSED] Near-perfect raw-text detection leaves HumanScope without a demonstrated practical objective.

   - Claim: Narrative detection’s interpretability and durability naturally support a writing skill.
   - Risk: TF-IDF reaches 99.7% and ModernBERT 99.9% ([409–426](/D:/main-projects/LIVE-ACTIVE/HumanScope/extracted/StoryScope.txt:409)). StoryScope’s distinctive contribution is explanatory analysis—not evidence that classifier-guided rewriting produces better fiction. Converting its findings into generation rules could merely optimize against a provenance classifier, drifting toward the detector-evasion project you explicitly reject.
   - Do instead: Define HumanScope’s success through blind reader preference, editorial acceptance, coherence, originality judgments, and retention of author intent. Never use reduced AI-detection score as a primary metric.

The three biggest risks to HumanScope’s intellectual integrity are:

1. Laundering human/AI correlations into claims about writing quality.
2. Treating a confounded, pipeline-specific Books3 comparison as a universal model of human composition.
3. Optimizing individual texts toward “human rarity” or detector features without independent evidence that readers find the results better.
tokens used

---

## Round 2 — GPT Astra (gpt-6-astra) synthesis council (session 01a0a015)
_Astra independently re-derived the taxonomy from the paper, then attacked Claude's P1–P6. Reconciled result → 6 diagnostic lenses (see structural-patterns.md / roadmap-and-state.md). Adjudication: Claude accepted essentially all objections._

**Part 1 — Independent derivation**

My root-cause hypothesis: **pressure to make narrative purpose and craftsmanship readily recognizable**—explicit meaning, conspicuous emotional rendering, and manageable progression. This explains the *direction* of several findings better than “mode-seeking.” It remains a hypothesis; the paper identifies no causal mechanism.

My paper-first grouping:

1. **Interpretive control:** narration, dialogue, and thematic alignment supply the story’s interpretation.
2. **Staged experience:** bodily emotion, sensory description, interior access, and descriptive introductions foreground how experience is presented.
3. **Compressed causal architecture:** fewer subsidiary tracks, more protagonist-controlled resolution, more acceptance-based closure.
4. **Sequential disclosure:** chronology carries information; revelations less often reorganize earlier understanding.
5. **External relations, with two branches:** references to other works; the narrator’s relationship with the reader.

These follow §4.1 and Tables 14–16. Population-level diversity sits **above** these families; it is not another defect inside an individual story.

Against Claude: I separate causal architecture from information order, replace “monotony” with a directly observable presentation preference, reject P6 as a residual bucket, and ultimately split external relations into two families.

**Part 2 — Objections and recommendations**

1. **Delete the asserted single root cause.**  
   “Highest-probability,” “lowest-risk,” and “most legible” are three different explanations. Convergence demonstrates similar outputs, not how individual decisions were selected. Training-distribution centrality and audience-averaging could explain concentration; legibility pressure better explains explicit lessons and conspicuous embodiment; risk-aversion only partly explains moral clarity. None is isolated here.

   The strongest study-specific rival is **prompt compression plus compliance**: the prompt preserves theme, mood, and selected details while compressing the finished story into ≤120 words. That could privilege an explicit central trajectory. [Paper L1863–1887](D:/main-projects/LIVE-ACTIVE/HumanScope/extracted/StoryScope.txt:1863). Keep competing hypotheses in research notes, outside the operational rules.

2. **Keep P1, but replace “trust the reader” with “calibrate explanation.”**  
   “Mostly a real improvement” is correlation laundering. Explicitness is not redundancy; philosophical dialogue is not necessarily exposition wearing quotation marks. The actionable defect is an explanation that adds no needed understanding or defeats intended inference. Preserve useful summaries, explicit interpretations, and thematic unity.

   P1 and P6’s moral polarity are distinct: a narrator can explain moral ambiguity exhaustively, or leave a clear moral judgment implicit. Merge their **thematic-control overlap**, not explicitness and moral ambiguity themselves.

3. **Delete P6 as a standalone family; redistribute its components.**  
   “Safe option” repeats the root hypothesis and can absorb almost anything. Put moral framing under interpretation, subplot/location scope under architecture, and dialogue allocation under presentation.

   More seriously, “subplots that aren’t all thematically obedient” misreads the measured direction: humans more often have **thematically parallel** subplots. The result does not establish a preference for independent ones. [Table 15, L1671–1673](D:/main-projects/LIVE-ACTIVE/HumanScope/extracted/StoryScope.txt:1671). Remove the prescription.

4. **Rename and broaden P2; delete the register-variety instruction.**  
   The family is substantial enough: embodiment, environmental mirroring, sensory density, interior access. Its current name claims something the evidence does not measure. A corpus-level *dominant emotional-expression category* cannot establish repetitive execution within a story. [Table 14, L1526–1530](D:/main-projects/LIVE-ACTIVE/HumanScope/extracted/StoryScope.txt:1526).

   Keep **presentation choices** as a family. Diagnose repetition from actual passages and their functions. Replacing effective sustained embodiment with a rotation of labels, gestures, and ambiguity would manufacture variety.

5. **Demote P3’s “loosen the structure” intervention to on-request exploration.**  
   This is the most likely family to damage writing. “Tolerate mess” invites arbitrary accidents, weakened agency, and abandoned obligations. Acceptance-based closure is not equivalent to complete resolution; descriptive entry is not equivalent to tidy causality. Move introductions and spatial grounding into presentation/disclosure.

   Retain a neutral architecture diagnostic: does the ending follow from established pressures, and does it answer the intended story question? That can justify **strengthening** causality. Nonlinear or subplot alternatives should address an identified limitation, never an authorship resemblance.

6. **Keep P4 separate, but rename it “information order.”**  
   Event causality and reader knowledge are different editorial problems. A tightly causal mystery can disclose events backward. Conversely, chronological narration can produce major reinterpretation. The paper measures recontextualization separately from nonlinear framing. [Table 15, L1655–1659](D:/main-projects/LIVE-ACTIVE/HumanScope/extracted/StoryScope.txt:1655).

   Remove linearity as a warning sign. Test whether placement creates the intended understanding, curiosity, or surprise. “More flashbacks” remains an unsupported prescription.

7. **Split P5; reject “named reference is the safest lever.”**  
   Intertextual reference and reader address require different decisions. A culturally situated story may never address its reader; an invented world may address its reader constantly.

   Furthermore, literary allusion is not “literally cite your sources.” A real name can supply no evidence, and precise description can work without names. The core question measures **intertextual engagement**, not factual substantiation. [Table 15, L1641–1645](D:/main-projects/LIVE-ACTIVE/HumanScope/extracted/StoryScope.txt:1641). Preserve relevant references; add factual sourcing when claims require it. Neither absence of names nor absence of “you” is a default defect.

8. **Replace six directional defaults with six conditional diagnostic lenses.**  
   Appendix D selects features for authorship discrimination. Appendix E establishes predictive redundancy, not six latent causes or the effects of editing. [L1293–1312](D:/main-projects/LIVE-ACTIVE/HumanScope/extracted/StoryScope.txt:1293).

   Six is defensible as an interface choice. Require every proposed edit to identify **textual evidence → intended reader effect → present failure → smallest useful change**. “More human-correlated” cannot fill the failure slot. The §25 caveat must govern the action, not merely follow it.

**Part 3 — Transfer map**

These are editorial transfer judgments, **not findings tested by StoryScope**. Ratings concern the proposed humanward move.

| Final family | Transfer | Useful application / actively harmful transfer |
|---|---|---|
| Explanation and interpretation | **Split** | Remove redundant interpretation. **Harm:** obscuring an email’s request, an essay’s thesis, a report’s conclusion, instructions, or marketing’s offer. |
| Presentation choices | **Split** | Assess descriptive effort in narrative essays and marketing. **Harm:** adding emotional variety to technical docs or deleting sensory detail that identifies an actual condition. |
| Causality and closure | **Split; often reverses** | Preserve unresolved evidence and multiple causes in reports. **Harm:** adding digressions, accidental causation, or loose ends to emails/docs. Conversely, forcing uncertain findings into a tidy resolution also harms accuracy. |
| Information order | **Split** | Essays, reports, emails, and marketing often benefit from results before chronology. **Harm:** withholding an answer, limitation, or prerequisite for dramatic payoff; scrambling procedural dependencies. |
| Referential grounding | **Split** | Relevant, verified sources and concrete referents help essays/reports/docs. **Harm:** ornamental citations, brand insertion, unexplained allusions, or unnecessary identifying details. |
| Reader relationship | **Split** | Direct address can suit emails, tutorials, and marketing. **Harm:** importing narrator asides or assumed intimacy into impersonal reports; treating “you” as proof of audience awareness. |

Thus **P3 does not categorically reverse outside fiction**: clear organization transfers, fabricated causal neatness does not. **P5a transfers conditionally**, through relevance and evidential need—not name density. P4’s broad prohibition is also wrong: answer-first nonfiction routinely departs from chronology.

**Part 4 — What both missed**

1. **Selection before arrangement:** Is this the right material for the piece’s central concern? An irrelevant scene remains irrelevant after perfect restructuring. Add a relevance check as editorial judgment, not a paper-derived feature.
2. **Attention and proportion:** Does space go to consequential moments, or does a decisive change receive one sentence after pages of setup? The paper includes pacing-related variables, but not a demonstrated standard for allocating attention well.
3. **Character-specific necessity:** Would this particular person notice, say, or choose this—and bear its consequences? Agency frequency and moral ambiguity do not measure believable motivation. Use as a fiction diagnostic, without prescribing conflict or escalation everywhere.

**Recommended final v1 family set**

- **Explanation and interpretation:** Match explicit meaning to what this reader needs and what the author wants left inferable.
- **Presentation choices:** Make description, interiority, emotion, and dialogue earn their attention.
- **Causality and closure:** Test the adequacy of causes and endings; offer structural loosening only on request.
- **Information order:** Arrange knowledge for the intended effect while preserving comprehension.
- **Referential grounding:** Use concrete references when relevant; substantiate factual claims when needed.
- **Reader relationship:** Maintain the intended narrator–reader or writer–audience relationship without requiring direct address.

**Verdict:** Claude’s synthesis is useful raw material, but not sound enough to build SKILL.md on until its causal assertion and humanward defaults are replaced with evidence-based, purpose-specific diagnostics.

---

## Round 3 — GPT Astra (gpt-6-astra) FULL-CONTEXT pre-build audit (session 01a0a015)
_Astra read Sol's raw R1 review + all research/ files. Part A = independent re-review of Sol; Part B = reference-set audit; Part C = build-readiness verdict (BLOCK + 4 must-fix). Adjudication: Claude accepted essentially all; remediation applied in-place before SKILL.md. Raw: research/raw-model-output/astra-fullcontext-out (not committed)._

**Part A — Sol’s review: substantially sound, but several remedies overreach**

1. **Agree — provenance ≠ quality.** This is the essential correction. Reader evaluation is necessary to claim demonstrated improvement; it needn’t precede prototyping an explicitly experimental editorial heuristic.

2. **Agree, qualify — prompt-construction confound.** The asymmetry is real; its contribution is unmeasured. Down-rank **causal interpretation and generalization**, not the observed within-corpus association. “Slightly down-ranked” invents a confidence adjustment.

3. **Agree, qualify — no monotonic humanward rules.** Sol’s concluding requirement that choices be “varied” reintroduces the variety prescription it rejects. Require fitness for purpose; sustained uniformity can be effective.

4. **Agree — predictive ablation ≠ editing experiment.** Table 8 cannot establish checklist inferiority or the effect of changing prose.

5. **Agree — row-shift correction verified.** External introduction = **30/52**, no subplots = **57/79**, internal-understanding resolution = **27/47**. The separate [Table 16 extraction](D:/main-projects/LIVE-ACTIVE/HumanScope/research/extracted/table16_page26_raw.txt) confirms these.

6. **Agree on counting; accusation overstated.** There are 30 questions and 33 directional rows. Displaying both categorical options is legitimate; it does not itself prove independent optimization or double-weighting. Preserve the count caveat.

7. **Agree on inconsistency; disagree with confidently choosing ordinal means.** Sol says “they are not prevalence estimates,” but the paper’s conflicting descriptions do not establish which representation is correct. Fourth-wall values below 1 also conflict with Table 15’s stated 1–4 scale. Record **unresolved encoding/reporting**, and retain only the reported directional tendency.

8. **Agree on population-to-individual error; qualify “circularity.”** Discriminatively selected features make rarity a task-dependent originality proxy, not a tautologically invalid measurement. Sol’s replacement—“optimize … non-default choices”—still rewards deviation without proving benefit. Delete that objective.

9. **Agree — dominant category ≠ within-story switching.** But “avoid a dominant embodied-emotion default” remains directional. Inspect actual repetition and effectiveness without presuming dominant embodiment is defective.

10. **Agree on granular gating; disagree with several transfer shortcuts.** Tidiness does not uniformly reverse; literary reference is not factual citation; answer-first nonfiction need not follow chronology. The reconciled transfer account improves on Sol.

11. **Agree — generation protocol is underspecified.** “No iterative revision reported” is defensible. “Un-steered,” “zero-shot,” and “unedited first drafts” are not established facts.

12. **Agree — external validity is limited.** Replication is required for broad empirical claims, not as a prerequisite to drafting a modest, conditional skill.

13. **Agree on measurement limitations; Sol misattributes the claim.** The original S4 already said “not ground truth.” Shared model involvement creates possible correlated measurement bias, not demonstrated bias. Aggregate agreement also does not validate every core feature individually.

14. **Agree — LAMP inference needs narrowing.** Stable classifier performance does not establish that every underlying narrative feature remained unchanged, much less that all surface editing is ineffective.

15. **Agree on evaluation; disagree with the headline.** HumanScope already has a practical objective: better writing. What is missing is **demonstrated efficacy**, not an objective. Near-perfect raw-text detection is logically irrelevant to whether developmental editing helps.

**Additional paper issues Sol missed:**

- **Subplot denominator:** 42% versus 21% thematically parallel is measured across **all stories**, alongside 57% versus 79% having no subplots. It cannot establish human preference for parallel subplots *conditional on having subplots*. Our earlier “humans favor” wording also needs correction.
- **Reporting inconsistencies beyond T5:** §3 reports 1,377 test prompts/8,262 stories; Appendix D reports 1,384/8,301. Nominal corpus totals also need reconciliation with the 24 refusals. Flag these rather than silently combining versions. [Paper L342](D:/main-projects/LIVE-ACTIVE/HumanScope/research/extracted/StoryScope.txt:342), [L1287](D:/main-projects/LIVE-ACTIVE/HumanScope/research/extracted/StoryScope.txt:1287).
- **Rarity depends on the reference population:** pooled nearest-neighbor density uses five AI sources versus one human source, plus encoding/scaling choices. Request balanced-population sensitivity analysis before treating rarity as author-independent originality.
- **Prompt-level splitting is not author-level splitting.** The paper does not establish generalization to unseen human authors. Conversely, it *does* report length-matching, overlap-screening, and topic analyses; limitations should acknowledge those checks without claiming they validate individual editing rules.

**Part B — Concrete fixes across the reference set**

1. **`paper-notes.md`: apply corrections in place.**  
   [S3/S6/S7, L47–51](D:/main-projects/LIVE-ACTIVE/HumanScope/research/paper-notes.md:47) still contain claims §10 says were corrected: zero-shot generation, editing-one-feature effects, and universal surface-editing failure. Replace them; appended caveats cannot serve as contradictory alternate specifications.

2. **`paper-notes.md`: remove remaining quality prescriptions.**  
   Delete “humans move between registers” and “balance/variety” at L153–160; “non-default” as the objective at L235–242; “biggest…levers” at L251–253; and “more register variety” at L256. At L201–204, replace Claude’s “weakest spots” with **observed fingerprints of the tested Sonnet version**. A quiet ending is not a weakness.

3. **`paper-notes.md`: finish numerical and categorical cleanup.**  
   The raw Table 16 gives subplot-parallel gap **+22**, moral-ambivalence gap **+21**; [L149–150](D:/main-projects/LIVE-ACTIVE/HumanScope/research/paper-notes.md:149) currently gives approximately +21 and +22. Label gaps “as reported”; rounded displayed percentages need not subtract exactly. Replace “modal option” with **elevated option**—29% explicit emotion is not the human modal category. “Triple-count” should be “double-count three constructs.” Remove or explicitly quarantine T5 percentages repeated at L186–187.

4. **`limitations.md` and `paper-notes.md`: tighten corpus scope.**  
   Say **published anthology short fiction, including multiple genres**. “Literary” currently risks excluding the paper’s mystery, horror, fantasy, and science-fiction material. Publication does not verify each story’s editing history or polish. “Directly valid” should mean observed in this corpus, not established for every similarly sized narrative. Rename [limitations §3](D:/main-projects/LIVE-ACTIVE/HumanScope/research/limitations.md:17) to remove “un-steered.”

5. **`limitations.md`: add the missing methodological boundaries.**  
   Include the subplot denominator, unresolved reporting/encoding issues, rarity sensitivity, unspecified author-level separation, and absence of feature-specific quality experiments. Acknowledge the paper’s length/memorization/topic checks and their limits. Replace “no threshold makes any feature diagnostic” with **no deterministic authorship or quality verdict is justified**; probabilistic signal does exist. Replace “dial with a human range” with “context-dependent descriptive feature”—categorical options are not continuous targets.

6. **`structural-patterns.md`: fix the operational contract.**  
   At [L23–26 and L113](D:/main-projects/LIVE-ACTIVE/HumanScope/research/structural-patterns.md:23), delete “impossible by construction.” Models can invent plausible failure rationales. Call the four-slot rule a safeguard requiring evaluation. Add a **WRITE branch**: brief/constraints → intended effect → compositional choice → draft → review. There is no existing passage or present failure before drafting.

7. **`structural-patterns.md`: clarify L3 and complete traceability.**  
   Replace “acceptance-based vs. fully-resolved” at L57 with separate questions about **resolution mechanism** and **degree of closure**. Correct “humans favor parallel subplots” at L63. Resolve “on-request only” versus “or when a concrete failure demands it”: substantial restructuring may follow an authorized deep edit; light editing should surface it as a suggestion. No redundant permission ritual is needed.

   Restore explicit mappings for moral framing, location scope, spatial grounding, and pre-threat investment—or mark them deliberately unused. At L53, dialogue proportion came from **T7**, not T3.

8. **Across L5, limitations, rejected ideas, and secondary sources: scope no-fabrication properly.**  
   “Never invent names/numbers/dates/quotes” would prohibit writing fiction. Replace it with: **Do not present invented material as real-world evidence, genuine testimony, or author biography. Fictional invention is allowed within the brief; preserve established story facts unless revision authorizes changing them.** Relevant sourced additions need not originate exclusively with the user.

9. **`secondary-sources.md`: remove inherited framing and unsupported superiority claims.**  
   [L56–58](D:/main-projects/LIVE-ACTIVE/HumanScope/research/secondary-sources.md:56) still adopts durability, default-choice causation, and addition-over-subtraction. Replace with narrow study findings and neutral editorial options. “A checklist cannot measure absence” is false: “Is a required source missing?” is a checklist item. Clustering is neither necessary nor sufficient for editing; one broken reference can warrant repair.

   “All surface-only” also conflicts with the file’s own recognition of structural attribution/analysis problems. Detector-focused creator demonstrations do not independently corroborate a structural mechanism.

10. **`rejected-ideas.md`: keep the decisions, repair their rationales.**  
    At [L9–17](D:/main-projects/LIVE-ACTIVE/HumanScope/research/rejected-ideas.md:9): model differences do not establish a fine-tuning cause; population signals are not “useless per-document”; a 30-question checklist does not inherently double-count; rarity is not simply “circular”; nonfiction does not uniformly reward chronology.

    Reject deliberate degradation because it conflicts with the goal—not because published fiction proves simple language, fragments, or unconventional formatting are inferior. Preserve readability simplification and intentional voice.

11. **`secondary-sources.md` / `rejected-ideas.md`: quarantine unverified secondary statistics.**  
    The Twain comparison contains the definite arithmetic error **10.13 > 10.62** at secondary L74. Other numeric claims are relayed from a blog; they need primary-source verification and study-specific qualifiers before being presented as established research. They are unnecessary to justify rejecting lexical bans or detector optimization. Also restore the source’s actual `references/` architecture in historical descriptions; moving our files to `research/` must not rewrite another project’s design.

12. **`roadmap-and-state.md` / `adversarial-review.md`: separate current authority from history.**  
    Remove stale “paper proves fleeting” and adopted-default framing from roadmap L49–53. “Paper wins over everything” must mean fidelity to what it actually establishes; it cannot override author intent or resolve questions it never studied. Resolve the root-layout contradiction and mark `evidence-map.md` as missing wherever it is cited as existing.

    Preserve raw reviews verbatim. Add adjudication status and repaired navigation to the cleaned record so superseded Sol/my recommendations cannot masquerade as current instructions.

**Part C — BLOCK on the current foundation; no new research programme required**

Four must-fix items before drafting the operative skill:

1. Replace stale prescriptions and factual errors **at their original locations**.
2. Resolve WRITE, fiction invention, and edit-depth authorization semantics.
3. Create `research/evidence-map.md`: feature → observation → lens → editorial hypothesis → applicability → counterexample → proposed evaluation. Give every unique feature a mapping or explicit exclusion.
4. Separate frozen provenance from the current runtime specification; quarantine unverified secondary claims.

The six lenses can stay. They are a defensible editorial interface, **not six validated interventions**.

Recommended `SKILL.md` skeleton:

| Section | Lean runtime contents |
|---|---|
| Metadata and purpose | Writing/editing triggers; preservation goals; no authorship scoring |
| Task contract | WRITE / DIAGNOSE / EDIT; light/deep intensity; audience, genre, constraints; infer what is available |
| Factual and fictional boundaries | Evidence integrity, permitted invention, continuity and author-intent preservation |
| Workflow | Separate WRITE and existing-text branches; four-slot edit justification; no-change outcome |
| Six lenses | One question each, with essential counterexamples and purpose gates |
| Execution and output | Match requested mode; diagnose without rewriting; prioritize consequential changes |
| Restraint check | Meaning, voice, facts, continuity, comprehension, unwanted homogenization |
| Optional references | Targeted links to evidence map and examples; no mandatory research-corpus reread |

Keep statistics, causal hypotheses, source comparisons, limitations detail, adjudication history, and validation results in `research/`. Essential behavioral constraints must remain in the runtime.

Top three build traps:

1. **Renaming prescriptions as questions:** “Is this too linear?” still embeds the assumption that linearity is suspicious.
2. **Manufacturing defects to satisfy the workflow:** require justified changes, permit no change, and avoid mandatory passes that must produce findings.
3. **Mistaking generic editorial improvement for HumanScope’s contribution:** evaluate against both the untouched draft and a competent ordinary-editing baseline under comparable conditions. Include strong drafts that should remain unchanged; blind preference and fidelity must test the claimed benefit.

---

## Round 4 — GPT Astra (gpt-6-astra) steerable adversarial review of SKILL.md (session 01a0a015)
_5 hats (research-reviewer, writing-editor, prompt-engineer, domain-skeptic, minimalist) + the 3 traps, in one pass. Verdict: **SHIP-AFTER-FIXES** — 3 must-fix + 5 more. ALL 8 applied in-place. Raw: research/raw-model-output/astra-skill-review-R4-raw.txt._

Must-fixes: (1) domain table reinstated directional prescriptions → replaced with conditional paragraph; (2) four-slot Evidence slot too local + 'stop' ambiguous + not observable in DIAGNOSE → fixed; (3) preservation froze errors/blocked authorized transforms → now allows supported corrections + authorized change. Also: L3/L4/L5 question wording de-directionalized; evidence-map prescriptions neutralized + categorical transfer labels dropped; opening promise narrowed + distinct-value note; Never section trimmed (dedup) + output conflict fixed; evidence-map coverage corrected (29→30, added Opening Spatial Grounding, L4×6); removed 'structurally impossible' claim.

---

## Round 5 — GPT Astra (gpt-6-astra @ **xhigh**) final re-review of the full package (session 01a0a015)
_Re-review after R4 fixes (first attempt hit 'model at capacity'; rerun at extra-high effort). Verdict: **SHIP-AFTER-FIXES** — SKILL.md core fixes confirmed landed; found real issues in the examples/evals/README written after R4. ALL 6 applied + a smoke test executed. Raw: research/raw-model-output/astra-final-R5-raw.txt._

Applied: (1) rubric pass-criteria rewritten (no-regress-vs-U; H=O=U passes preservation w/o proving value; fewer-edits secondary; same brief/sources/budget; raters get brief+facts); (2) cases reframed as specs w/ hidden grader key + WRITE/DIAGNOSE protocols + smoke-test requirement + P7/P8; (3) examples fixed (Ex1 add brief + align edit + no invented gesture; Ex2 drop bogus false-range finding; Ex5 disambiguate + 'tidiness≠correctness' caveat); (4) evidence-map fully neutralized (drop 'it's important to note' cut, 'add smell b/c AI-elevated' rationale, directional eval columns, leftover Transfers labels; added governing question); (5) SKILL.md description opening + deleted 'say so and stop' conflict + 'see §4'; (6) README drop novelty overclaim + 'narrative-not-stylistic features' + experimental-status disclaimer. Plus evals/smoke-test.md executed (n=1 plumbing check).

---

## Round 6 — GPT Astra (gpt-6-astra) review of the expository-mode change (session 01a0a015)
_Claude proposed a hard narrative/expository split for SKILL.md §4, motivated by the ablation. Astra: SHIP-AFTER-YOUR-EDITS — the hard split overfits n=1/topic data, the proposed 'lean path' was NOT the tested arm C, and directional wording ('state the conclusion', 'keep tidy') could harm inductive args/uncertainty/voice. Reframed as **purpose-based review depth** (route by passage function, keep substantive review across domains, no lens banned from exposition). Claude adopted Astra's rewrite verbatim as §4. Raw: research/raw-model-output/astra-expository-review-R6.txt._
