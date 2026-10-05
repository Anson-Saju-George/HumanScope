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

---

## Round 7 — GPT Astra (gpt-6-astra @ xhigh) generalization audit (session 01a0a015)
_Q: can HumanScope serve documents / papers / notes / websites / any writing? Verdict: **NEEDS-WORK** — 'safe everywhere' is unproven; concrete plausible misfires on structured docs (markup/numbering), claim-strength & citation attachment (academic), repeated CTAs (marketing), and notes-to-prose conversion. Notably it CONFIRMED the skill does NOT strip academic hedging (§4 protects qualifications). Fixes applied: (1) §1 artifact/conventions guard; (2) Core-stance claim-strength/attribution guard; (3) §5 'notes may remain notes / intended format'; (4) removed the §4 ablation aside (conflated generation with review); (5) narrowed scope language in SKILL.md + README (fiction-grounded, genres untested). Recommendation: TEST realistic artifacts, don't add genre checklists. Raw: research/raw-model-output/astra-generalization-R7.txt._

---

## Round 8 — GPT Astra (gpt-6-astra @ xhigh) max-rigor V1 audit (session 01a0a015)
_Usage-unlimited pass. Verdict: **V1 is well short of its model-only ceiling; substantial room.** Biggest finding — an EVALUATION CONFOUND all prior rounds missed:_
- **A/B conditions differed beyond the skill:** skill-arm prompts requested research-file reading + implicit meaning + answer-first/tidy/real-refs; baselines requested none. So the 8/8 may reflect the EXTRA INSTRUCTIONS, not SKILL.md. → withdraw 'SKILL.md alone' attribution.
- **The essay judge had a circular criterion:** it rewarded 'implicitness = trusting the reader' — exactly what the skill arm was told to produce; the brief didn't require it.
- **The ablation doesn't isolate the lenses** (H inherits extra instructions/context; C's prompt is edit-framed but used for generation). Also a factual error: ablation generator=Claude, judge=Sol.
- **Residual overclaims** in results (demonstrated L1 mechanism, effect-size dependence, preserved voice, no over-editing — generation can't show voice-preservation/restraint) and generalization ('one-off/non-harmful/guards prevent' — no guardless control).
_Also: 6 small SKILL.md runtime fixes; a concrete scaled model-only protocol (96 held-out cases × 4 arms O/C/V1/N × 3 generator families × 3 runs = 3,456 outputs, 3 independent judges, separate constraint/task/preference outcomes, case-clustered CIs); v1.1 = corrected reports + runtime fixes + versioned eval harness + regression suite, NOT another lens. Raw: research/raw-model-output/astra-v1-audit-R8.txt._


## Round 9 — Astra (gpt-6-astra @ xhigh, pinned session) — fair re-test review + Chen prior art
_Invoked 2026-09-25 with full unblinded fair-retest results (6 cases x 4 arms: S/O/C/K), both blind judges' scores, all 24 outputs, Chen's human-scope SKILL.md, and the then-current SKILL.md. Adjudication: all six SKILL.md diffs adopted verbatim (v1.1); "propose, not cut" rejected as an absolute per Astra; RESULTS.md headline/counts/K-funeral/manifest labels corrected; held-out suite adopted as `evals/heldout-v1.1.md`; README credit reworded (name-coincidence sentence removed)._

**Verdict: the retest exposes real failures, but “S ties O; S beats K; lenses add nothing” is too broad. Keep the lenses provisionally for structural work, make a small preservation patch, and validate it on new material. Do not call the patch an improvement before testing it.**

**1. What the results actually say**

The headline should be:

> **In six preservation-focused editing cases, HumanScope showed mixed results and no demonstrated advantage over ordinary or compact editing. The comparison did not isolate the lenses’ contribution.**

The equal totals hide this:

| Comparison | Astra: wins / losses / ties | Sol: wins / losses / ties |
|---|---:|---:|
| S versus O | 1 / 2 / 3 | 1 / 2 / 3 |
| S versus C | 1 / 2 / 3 | 1 / 2 / 3 |

S’s technical win compensates for its marketing and fiction losses under the chosen scoring. Equal sums of two ordinal scales do **not** establish equivalent performance. Conversely, counting cases alone ignores the potentially different consequences of altering an operational requirement and deleting a marketing assertion. Report both the counts and the failure types.

Five corrections matter:

- **C still is not a lens-only ablation.** [C-instr.txt](D:/main-projects/LIVE-ACTIVE/HumanScope/test-run/fair-retest/C-instr.txt:1) also omits S’s detailed claim guard, artifact conventions, routing and final restraint check. S’s technical success could come from those instructions. Say **“the full package did not establish an advantage over the compact package,”** not “the lenses showed no increment.”

- **The preservation brief is legitimate but restricts the conclusion.** It tests an important promised behavior: improve wording without making substantive authorial decisions. It does not determine the best developmental edit, nor whether implicitness would improve fiction-a under a different brief. The bias enters when this task becomes a claim about fiction editing generally.

- **Fiction-a was not merely redundant.** Its paragraph establishes a habitual coping behavior, fear of losing Ruth, that fear as the journey’s motive, and Dana’s realization of this. Eggs and driving do not establish those things. **All four edits lose the stated motive; S loses more than O/C.** Ranking the least damaging rewrite does not establish improvement over the original. Include the untouched source next time. A faithful tightening remains possible—for example: “Whisk in hand, she realized she had always cooked when afraid: fear of losing her mother was why she had driven two hours, unasked.”

- **The K comparison needs narrower language and one factual correction.** S better preserved the brief in both tested fiction cases. Four other cases are outside K’s principal scope. Also, K’s “At the funeral I skipped it too” follows reasonably from “three weddings and one funeral” plus “I always skip that year.” The unsupported addition is the comparative motive—“nobody there needed me to skip it more than I did”—and the loss is the present confession. Fiction-a contains unmistakably invented actions. Don’t overstate the competitor’s errors.

- **Fix the evaluation records themselves.** “Leverage” is labelled a defect in [MANIFESTS.md](D:/main-projects/LIVE-ACTIVE/HumanScope/test-run/fair-retest/MANIFESTS.md:3), yet S/O/C retain it and receive full marks. Remove that word-based defect label. Describe the judges as two independently run OpenAI models; this is neither cross-provider corroboration nor twelve independent task replications. Four cases were already development material.

There is also a reproducibility gap: the successful judge prompts/transcripts and exact evaluated S snapshot are not archived in this checkout. The packet builder alone does not establish the reported isolation. Archive the successful runs; their absence does not mean they never happened.

Finally, **rerunning these six cases is useful regression testing, not inherently overfitting**. Using those reruns as independent validation would be the mistake.

**2. Diagnosis and numbered SKILL.md diffs**

The common failure is **unauthorized loss of distinct information during preservation editing**. “Removing content the author chose to state” is too broad: authors also choose redundant, irrelevant and mistaken content.

A plausible mechanism is treating a passage’s expendable rhetorical function as evidence that *everything inside it* is expendable. That remains a hypothesis; neither L1 nor any other instruction has been isolated causally.

I would make these six focused changes.

**1. Check deletions, not just surviving claims.**  
[§2, smallest useful change](D:/main-projects/LIVE-ACTIVE/HumanScope/SKILL.md:77)

Old:

> **Smallest useful change** — the least edit that fixes it while preserving voice/meaning.

New:

> **Smallest useful change** — the least edit that fixes it while preserving voice/meaning. Before deleting or replacing text, identify what information or function would disappear. Removing filler does not authorize removing a distinct claim, motive or realization inside it. Consolidate genuine redundancy; omit substantive content only as the brief authorizes or a supported correction requires.

This preserves content where required, without freezing sentences or forbidding deletion.

**2. Bound the transformation exception.**  
[§2, authorized transformation](D:/main-projects/LIVE-ACTIVE/HumanScope/SKILL.md:80)

Old:

> For an *authorized transformation* (the user asked you to rewrite, shorten, change register, etc.), the bar is different: assess the gap against the requested target, not a "present failure" — a transformation can be worth making without the original being defective.

New:

> For an authorized transformation, assess the gap against the requested target rather than inventing a defect. Change or omit content only as that target requires and within the brief’s constraints. “Rewrite” or “tighten” is not blanket permission to change substantive meaning; a summary, abridgment or creative transformation may authorize selection or alteration.

Otherwise the exception can swallow the preservation rule.

**3. Scope fictional invention by mode.**  
[Core stance](D:/main-projects/LIVE-ACTIVE/HumanScope/SKILL.md:51)

Old:

> When writing **fiction**, inventing characters/events/detail is the task — do it freely, and preserve continuity unless asked to change it.

New:

> In fiction **WRITE**, invent characters, events and detail within the brief. In **EDIT**, add or alter them only where the requested transformation authorizes it; preserve established continuity.

This is an actual cross-mode ambiguity. “Fiction” alone must not license new events during a light edit.

**4. Replace L1’s residual invitation toward implication.**  
[L1 parenthetical](D:/main-projects/LIVE-ACTIVE/HumanScope/SKILL.md:96)

Old:

> Both over- and under-explaining are failures. Reports/instructions often *should* state conclusions; a scene may be stronger implied.

New:

> Both over- and under-explaining can impair the intended effect. Explanation may supply a motive, realization, emphasis or narrator stance. Information a reader could infer is not necessarily equivalent to an explicit disclosure.

Keep the opening question. This change teaches the distinction the failed edit missed.

**5. Make structural review depend on the task, not narrative genre alone.**  
[§4 narrative routing](D:/main-projects/LIVE-ACTIVE/HumanScope/SKILL.md:134)

Old:

> For passages organized around **scenes, experience, or unfolding events**, select the relevant lenses from §3 to examine how presentation, disclosure, interpretation, and closure work together. Do not run all six by default.

New:

> For passages organized around **scenes, experience, or unfolding events**, use relevant lenses when WRITE, DIAGNOSE or the requested edit calls for structural review. Light EDIT stays within its requested scope; narrative genre alone does not call for a broader review. Do not run all six by default.

The existing permission to use any lens for a concrete need remains.

**6. Add the useful knowledge-boundary check.**  
[§5 restraint check](D:/main-projects/LIVE-ACTIVE/HumanScope/SKILL.md:152)

Old:

> voice preserved? continuity/terminology intact?

New:

> voice preserved? continuity/terminology intact? who knows what, when, consistent with the intended viewpoint?

Test this against retrospective and omniscient narration so it does not become a new prohibition.

Your proposals, adjudicated:

- **“Claim-bearing sentences survive”: amend.** Required claims survive; sentences may merge, move or disappear when their content remains.
- **“Stated meaning is proposed, not cut, in EDIT”: reject as an absolute.** Perform authorized omissions and genuine consolidation. For an unauthorized substantive deletion, retain the material; propose an alternative only when review commentary is requested or permitted. Do not force an approval loop into artifact-only editing.
- **Knowledge boundaries: adopt conditionally. Diagnose → choose changes → revise: offer as an optional README workflow.** It is useful author control, not a mandatory runtime sequence.

Chen’s exact useful instruction is:

> “Check continuity, chronology, knowledge boundaries, and cause and effect.”

Also worth retaining as an editorial principle:

> “Keep explicit reflection when voice, accessibility, genre, or the author's intent calls for it.”

Chen already contains that safeguard and still produced the failed edits. **Another sentence of caution is not proof of reliability.**

Explicitly reject importing:

> “Identify the three highest-impact issues”

That imposes an issue quota.

> “Revise at scene level before polishing individual phrases.”

That is an inappropriate universal order for light edits.

The quota may contribute to unnecessary revision; these outputs do not prove it caused the invented material. And Chen’s supplied skill proceeds directly from diagnosis to revision—it does **not** specify an approval step. Credit the knowledge-boundary check, not an approval workflow absent from the text.

**3. Should the six lenses stay?**

**The case for removing them:** no demonstrated incremental benefit; additional instruction load; some directional residue; ordinary editing already handles much of their substance. Their existence cannot be justified by the effort spent developing them.

**The case for retaining them:** this test barely exercises long-range composition, and does not test WRITE, DIAGNOSE or substantial structural editing. Moreover, C removes more than the lenses. These results cannot identify their contribution, positive or negative.

**Decision: retain them provisionally as optional aids for structural work, with the routing change above.** Do not advertise them as an established advantage. The next matched comparator should be the patched skill with **only the lens content and necessary references removed**, keeping guards and other workflow instructions constant. Publish that diff.

Their benefit in untested modes is a reason to test them, not evidence that they help there.

**4. Held-out validation specifications**

Use **eight new source artifacts, nine tasks**, because case 2 has two permission conditions. These are specifications, not yet held-out evidence: freeze the patch before realizing the new texts and evaluating outputs.

| Case | Hazard and source | Correct behavior | Why judging does not automatically favor restraint or intervention |
|---|---|---|---|
| **1. Exhibition access notice — light EDIT** | A verbose sentence contains a real opening window and an eligibility exception; nearby material contains genuine filler. | Shorten expendable language while preserving the window, exception and audience attachment. | Score recoverable information and useful tightening separately. Wholesale deletion and unchanged bloat can both fail. |
| **2. Motive and realization — paired EDIT briefs** | A new close-third story states a motive that actions alone do not establish, plus a genuinely duplicated clause. | **A:** ordinary meaning-preserving light edit retains motive and realization while tightening duplication. **B:** an explicit request to make the motive ambiguous permits removing that explanation while preserving events. | The same deletion cannot be right under both briefs. Count these as one source cluster, not independent cases. |
| **3. Effective apology — light EDIT** | A well-written apology uses purposeful repetition and an explicit admission of responsibility. | Preserve the admission and rhetorical function; unchanged text can succeed. | Judges are not told “no change expected.” They assess the recipient’s needs, not edit count or byte identity. |
| **4. Genuine redundancy — EDIT** | Adjacent paragraphs repeat a proposition without adding scope, emphasis, contrast or a separate reading path. A distinct qualification sits beside the duplicate. | Consolidate the repetition while retaining the proposition and qualification. | A blanket “never remove stated content” editor fails. Maximum shortening also fails if it loses the qualification. |
| **5. Executable instructions — structural EDIT** | A prerequisite appears after the action requiring it; an explanation is detached from its referent. All necessary information exists. Reordering is authorized. | Move the prerequisite before the dependent action and restore the explanatory connection without inventing steps. | Untouched text fails an observable task: following the instructions in order. This is a genuine structural-edit requirement. |
| **6. Knowledge boundaries — DIAGNOSE** | A limited-viewpoint scene uses information before its character acquires it. A separate, clearly retrospective narrator passage legitimately mentions later knowledge. | Identify the first problem with evidence and a feasible repair; do not flag the retrospective passage merely for knowing more. | Both indiscriminate suspicion and indiscriminate preservation fail. The chronology and viewpoint establish the distinction. |
| **7. Supported correction — EDIT** | A claim is broader than the supplied evidence. The brief authorizes evidence-based correction. | Narrow the claim and retain citation attachment; leave supported neighboring claims intact. | Success requires changing something explicitly stated. The evidence packet, not aesthetic preference, determines the correction. |
| **8. Notes to agenda — transformation** | Working notes contain completed and pending tasks, unresolved alternatives, owners and dependencies. The user requests an agenda organized around decisions and follow-up. | Produce the agenda while preserving status, uncertainty and ownership. | Returning the notes unchanged fails the task; inventing decisions to make a tidy agenda fails preservation. |

Use a normal preservation brief in case 2A—not a bespoke instruction naming the exact information the patch is supposed to protect. Give every arm the same brief within each task.

For execution:

- Compare **pre-patch S, patched S, O and matched compact C\***.
- Use at least three fresh-context runs per task: **108 outputs**.
- Include the untouched source when judging EDIT cases.
- Score **unauthorized information change, task completion and reader benefit separately**. A polished semantic loss must not disappear inside an aggregate.
- Randomize presentation order independently; allow ties. Give judges source material and the task, not the patch or expected preferred operation.
- Preserve the six existing cases as regression tests. New instances test transfer of the fix; eight deliberately selected artifacts still do not establish general writing efficacy.
- Add separate WRITE validation before claiming the revised invention rule or lenses improve drafting. This suite primarily validates editing boundaries.

**5. Public wording**

For the README:

> **Latest evaluation: a six-case exploratory EDIT comparison.** With one Claude-generated output per condition, two independently run, blinded OpenAI judges ranked HumanScope above ordinary editing in one case, below it in two, and tied in three; the same counts held against a compact prompt. Combined scores were equal or close, but this does not establish equivalence. HumanScope preserved an unresolved technical specification where ordinary and compact edits changed it, while losing information in a marketing passage and a fiction passage. Its contribution beyond competent ordinary editing remains unestablished. The compact comparison did not isolate the six lenses.

In the detailed results, add:

> HumanScope better preserved the brief than Chen’s *Human Scope* in the two tested fiction cases. This small comparison does not establish general superiority; four additional cases were outside Chen’s skill’s principal scope.

For credit:

> Alex Chen’s SCOPE reel prompted this project. His companion skill, [*Human Scope*](https://chen.media/guides/human-scope-storyscope-claude-writing-skill), is prior art located during development. HumanScope is a separate, unaffiliated implementation informed by the same StoryScope paper. The v1.1 knowledge-boundary check draws on Chen’s editorial checklist.

Use the last sentence only once adopted. Remove the [README’s unsupported “name coincidence” explanation](D:/main-projects/LIVE-ACTIVE/HumanScope/README.md:159); simply distinguish the projects.

For CHANGELOG, after the patch lands:

> - Added the matched-brief exploratory EDIT comparison and documented its limits.
> - Clarified deletion checks, transformation scope and fiction invention permissions.
> - Restricted automatic expansion into structural review during light editing.
> - Added a viewpoint-sensitive knowledge-boundary check, crediting Alex Chen’s *Human Scope*.
> - Behavioral improvement remains pending held-out validation.

Also mark the historical [“validated domain-gating”](D:/main-projects/LIVE-ACTIVE/HumanScope/CHANGELOG.md:48) and [“safe and useful”](D:/main-projects/LIVE-ACTIVE/HumanScope/CHANGELOG.md:56) claims as withdrawn. They remain stronger than the evidence despite the newer corrections.

## Round 10 — Astra (gpt-6-astra @ xhigh, pinned session) — post-v1.1.0 audit of report and skill
_Invoked 2026-10-05 (first attempt hit the Codex usage limit before writing output; retried inline-only after reset). Material: SKILL.md, FINAL-RESULTS, README, CHANGELOG v1.1.0, both result pages, always-on snippet, exact arm and judge prompts, and summaries of outside reviews (ChatGPT, another Claude). Added question 6: which of its own R7–R9b recommendations were wrong. Adjudication: findings 1–8 and 11 applied as wording corrections (bare-edit arm removed from conclusions; version context on editing and Chen comparisons; held-out regression acknowledged; fidelity claim limited to scores; always-on scope stated). Findings 9–10 (SKILL.md description and slot-3 change; always-on snippet protections) deferred to proposed v1.2 pending tests. Cross-checked by another Claude against the repo files before applying. A fresh, context-free Astra pass separately flagged "keeps writing to what is true" (fixed in f271b4a)._

**The release is defensible; the scorecard still overstates what it establishes.** The strongest supported claim is that the complete instruction package received favorable model judgments against bare writing prompts. Neither its causal mechanism nor an advantage over competent editing has been established.

I’m using only the supplied material, including your `ea4f02b` update. File references below use quoted anchors because the updated files are not pasted in full.

1. **The new fidelity claim needs a narrower denominator.**

   In `README.md` and `evals/FINAL-RESULTS.md`, your replacement—

   > “in every writing task each HumanScope piece scored higher on fidelity than each bare piece; only 2 of 10 fully clean”

   —mixes different populations. **Ten** covers the full-skill nonfiction drafts: three web, three blog, three email, plus HS. Including the three stories gives **thirteen** full-skill drafts. The supplied record does not include the story fidelity scores.

   Replace with:

   > “Across the three nonfiction writing tasks, the reported fidelity scores favored every full-skill draft over the bare drafts for that task. Two of the ten full-skill nonfiction drafts received 5/5 for fidelity; this is a judge score, not independent verification that they were error-free. Including fiction, the judge ranked every full-skill draft above every bare draft within each of four task prompts.”

   Also change **“invents much less”** to **“received higher factual-fidelity scores”** unless you publish an actual count and severity assessment of unsupported assertions. An ordinal score difference does not measure how much invention decreased.

   I accept your update that the story results have been added; I am not treating the old “not yet judged” passage as an outstanding defect.

2. **WRITE’s instruction difference is legitimate. The conclusions drawn from it need limits.**

   Task alone versus **the same task plus the skill** is exactly the intervention a package comparison should test. Adding “read SKILL.md” is not the X confound. Requiring owner-specific claims to be supported is also reasonable; a criterion does not become circular merely because the skill targets it.

   But this tests **adding the entire instruction package**, not:

   - whether its six lenses work;
   - whether the four-slot rule causes the benefit;
   - whether it beats a short ordinary writing brief;
   - what typical consumer-chat users receive.

   In `evals/FINAL-RESULTS.md`:

   > “Blind judges consistently pointed at the same mechanism.”

   Replace with:

   > “The judge’s explanations frequently favored outputs with fewer unsupported owner-specific assertions. This comparison does not identify which instructions produced that difference.”

   The four-slot rule applies to **EDIT/DIAGNOSE**, while these wins are **WRITE** results. Crediting that rule specifically is particularly weak.

   Replace the scorecard question:

   > “Does it beat what a normal user gets…”

   with:

   > “How did task-plus-skill compare with task-only prompts in these Claude Code subagent runs?”

   Likewise, **“the way people really write”** becomes **“one casually worded bakery request.”** One spelling/register variation is not a user study.

3. **Choose (c): remove X from the efficacy scorecard; retain the disclosed run.**

   **“A brief beats no brief” is not a valid rescue interpretation.** The judge was misinformed about X’s obligations. That compromises the inference about the benefit of providing a brief as well as the skill-specific inference.

   In `test-run/fair-retest/RESULTS.md`, replace:

   > “What the result does show: … any preservation brief beat a bare request … That is evidence for giving the model a brief…”

   with:

   > “These scores were assigned under an inaccurate description of X’s instructions. We retain this run as a documented evaluation error and do not use it to estimate the benefit of either a preservation brief or HumanScope.”

   Remove the **52 versus 33** row from the README and final scorecard. Keep a short disclosure linking to the archived run. Make the same correction to the CHANGELOG’s “Read 52 vs 33 as…” sentence.

   I would **not spend another run repairing X now**. You already have a cleaner ordinary-editor comparison. A corrected X judgment would answer a different, request-dependent question and would not retroactively create matched preservation instructions.

4. **The ordinary-editor and competitor headlines lose essential context.**

   Apply these replacements in both scorecards:

   | Current wording | Replacement |
   |---|---|
   | “Tie (52 vs 52), reproduced across two judging runs” | “The pre-R9 candidate showed mixed results against ordinary editing: 1 win, 2 losses and 3 ties under each original judge. Aggregate scores were equal; this does not establish equivalence.” |
   | “Near-tie (52 vs 50); the lenses’ contribution is not isolated” | “The pre-R9 full and compact packages showed mixed results. The compact arm omitted several components besides the lenses, so their contribution remains untested.” |
   | “Ahead in this evaluation (52 vs 37)” | “The pre-R9 candidate better preserved the requested meaning in the two fiction cases tested against Chen’s skill. This does not establish general superiority.” |
   | “v1.1 vs the pre-patch skill, on 9 new texts” | “Patched versus pre-patch skill on nine tasks from eight source texts.” |

   Two distinctions matter:

   - **The editing comparator outputs predate the R9 patch.** Current v1.1 has not been compared with O or matched C* in the new suite.
   - Rejudging the same outputs measures judgment consistency, not replication of generation performance. The original sums were **51–51**; the later sums were **52–52**.

   Chen’s revised credit is appropriately neutral. It does not claim his reel originated this project or that his skill requires an approval step. Keep that wording.

5. **The held-out summary denies a regression shown in its own table.**

   In `evals/FINAL-RESULTS.md`, replace:

   > “The fixes help modestly on new material and didn’t break anything.”

   with:

   > “In this single run, the judge preferred the patched output on four tasks, preferred the predecessor on one, and tied them on four. Task 05 scored lower for patched fidelity and reader benefit, so the run was not regression-free. These observations do not establish that the patch systematically improves or worsens performance.”

   Replace:

   > “The gains were on information fidelity (01, 07) and on doing an authorized transformation properly (02B).”

   with:

   > “Task 01 improved on all three scores. Task 02B improved on fidelity and reader benefit, while task completion remained 4/5. Task 07 improved only on reader benefit; both versions scored 5/5 for fidelity and completion.”

   Additional exact corrections:

   - **“helped on one held-out motive task”** → **“Both versions preserved the motive under the light-edit brief; the patched version ranked higher under the separate ambiguity-transformation brief.”**
   - **“Each task had three candidates”** → **“EDIT tasks included the untouched source; the DIAGNOSE task compared the two diagnostic responses.”**
   - **“both versions found the intended problem”** → **“Both flagged the intended issue, but its status as an actual error was disputed, and both diagnoses overstated the evidence.”**

   The **123–117** sum is not a calibrated effect size. Nor are 02A and 02B independent source examples. The reduced run is useful exploratory evidence, but it does not complete the planned 108-output protocol.

6. **“Fiction is the weakest area” is another unsupported generalization.**

   In `README.md`, `evals/FINAL-RESULTS.md` and the fair-retest reading:

   > “Its weakest area is fiction editing.”

   Replace with:

   > “A known failure occurred in preservation-focused fiction editing: the pre-R9 candidate removed distinct psychological information from fiction-a. The few examples tested do not establish a ranking of performance across genres.”

   Repeated judgments of **one bad output** do not create additional fiction examples. Also, “its one fiction case that needed a fix” revives the mistaken defect label. Its explanation was not demonstrated to be redundant; the original remains a meaningful comparator.

   Remove **“Most of its clear wins are on … edits of everyday text.”** The editing comparison did not demonstrate a general advantage. The positive bare-prompt signal primarily concerns generation.

7. **The evaluation still contains the aesthetic prescription the skill rejects.**

   The WRITE judge’s first axis prelabels **“tidy triads”** and named phrases as “AI-slop.” That can reward removing functioning rhetoric without demonstrating a reader problem.

   For a future judgment—not by overwriting the historical prompt—replace the first axis with:

   > **Purpose-fit and specificity:** Identify passages whose generic framing, repetition, explanation or tone causes a concrete problem for the stated reader and brief. Familiar phrases, triads, explicit themes and resolved endings are not defects by themselves. Support criticisms with quoted evidence.

   Replace the fidelity definition with:

   > **Fidelity:** Identify contradictions of supplied facts or constraints and unsupported owner-specific assertions presented as established facts. Distinguish these from general background claims, transparent inferences, suggestions and placeholders. Absence from the brief does not by itself establish falsity. For fiction, assess the requested constraints and continuity; invention within the brief is permitted.

   The supplied **held-out judge header is substantially better**: it permits authorized transformations and penalizes both unnecessary intervention and failure to act. I see no instruction in that header that inherently favors S over P. The questionable knowledge-case premise is a separate problem with the case’s expected answer.

   Finally, change WRITE RESULTS’:

   > “The slop and usefulness scores favored the skill too…”

   to:

   > “Advantages differed by criterion: all email outputs tied on the slop score, and the placeholder-heavy skill blog scored lower on usefulness than the bare blogs.”

   Overall ranking is not improvement on every axis.

8. **Always-on was tested as an explicitly supplied prompt, not as automatic integration.**

   Its generator was told:

   > “Read it first and treat it as always-on project instructions…”

   That demonstrates what happens when the snippet is deliberately supplied. It does not demonstrate automatic discovery, persistence across a conversation, or correct activation boundaries.

   Replace `FINAL-RESULTS.md`’s:

   > “Does opt-in always-on mode work without typing `/humanscope`? Yes…”

   with:

   > “When explicitly supplied as project instructions, the snippet’s outputs ranked above the bare outputs on two tasks. Automatic loading and continued application were not tested.”

   Use equivalent wording in README and CHANGELOG.

   Similarly, the webpage test judges **extracted page text**, not HTML correctness, accessibility, rendering or functionality. Label it **“webpage copy”**, and state that limitation.

9. **Make two small full-skill edits; do not redesign the taxonomy now.**

   I do not accept “we now know the strongest effect is fidelity rather than lenses” as a component finding. We know what the reported judgments often rewarded. The causal attribution remains open.

   **`SKILL.md`, description — remove the conflicting trigger.**

   Old:

   > “Use it to write, rewrite, tighten, or make text feel less formulaic / less ‘AI-shaped,’ and to diagnose structural habits without rewriting.”

   New:

   > “Use it to write, revise or tighten prose, or to diagnose compositional problems without rewriting.”

   This improves conceptual consistency. If automatic skill selection matters, test selection separately; do not claim it improves prose quality.

   **`SKILL.md`, §2 — put the transformation exception at the actual decision point.**

   Old:

   > “3. **Present failure** — a concrete way it falls short *now*.”

   New:

   > “3. **Present failure or requested transformation** — identify a concrete shortfall, or a gap between the current text and the user’s authorized target.”

   Old:

   > “If no concrete failure is supported, leave that candidate unchanged and continue reviewing the requested scope.”

   New:

   > “If neither a concrete shortfall nor the authorized target justifies this change, leave that candidate unchanged and continue reviewing the requested scope.”

   The later transformation paragraph already supplies the exception, but the numbered rule currently says the opposite before qualifying it. Keep the later limits on what “rewrite” authorizes.

   **Test the second change** against an already-effective passage, a requested summary, an authorized voice transformation and a meaning-preserving light edit.

   Otherwise, freeze the body. Its length is a reason to investigate compression, not evidence of damage. Keep the lenses optional. The current evidence supports neither mandatory use nor wholesale deletion.

10. **The always-on derivative has lost several protections from the full skill.**

   These are substantive consistency fixes, not reasons to add more lenses.

   **`always-on/CLAUDE-snippet.md`, scope**

   Old:

   > “They don’t apply to code, commit messages, or conversational replies.”

   New:

   > “Apply these rules to requested prose artifacts, including text embedded in HTML or delivered in chat. They do not govern executable code, commit messages or ordinary conversation.”

   **Facts/invention bullet**

   Replace the whole bullet with:

   > **Don’t invent real-world specifics.** Use supplied facts or appropriately supported additions; do not turn plausible details about real people, products, policies or events into asserted facts. Omit optional missing details; ask about essential gaps or mark a placeholder when a draft is useful. Fiction WRITE may invent within the brief; fiction EDIT may add or alter story facts only when authorized.

   This avoids both indiscriminate placeholders and ambiguity about invention during fiction edits.

   **Stock-phrase instruction**

   Old:

   > “Skip stock taglines and filler … unless the brief asks for that register.”

   New:

   > “Keep or remove conventional phrasing according to its function and the requested tone; a familiar phrase is not a defect by itself.”

   **Editing bullet**

   Replace with:

   > **When editing,** justify changes by passage → reader need → present shortfall or authorized target → smallest useful fix. Preserve meaning, voice, facts and format except for supported corrections or changes the brief authorizes. Check what deletions remove; filler may go without losing a distinct claim or disclosure. No change is valid when the brief is satisfied. “AI-like” is not a reason.

   **Final bullet**

   Old:

   > “No deliberate typos, word bans, or detector gaming.”

   New:

   > “Do not add typos or impose word bans to appear human; honor explicit style and creative constraints. Never optimize for detector scores.”

   **Test these before shipping:** fictional copyedit versus creative rewrite; supported factual correction; summary versus preservation edit; optional versus essential missing facts; purposeful conventional phrasing; prose embedded in HTML. The current two WRITE demonstrations do not test these editing obligations.

11. **Repair the remaining documentation mismatches.**

   - **README four-slot explanation:** add **“For an authorized transformation, assess the requested target rather than requiring the original to be defective.”**
   - **README “no change is always valid”:** replace with **“no change is valid when the brief is already satisfied.”**
   - **README human-eval roadmap:** replace **“compact four-slot-only … answers … do the lenses earn their complexity?”** with **“a matched variant removing only the lenses … tests their incremental contribution.”** Human raters do not repair a confounded component comparison.
   - **README “any assistant … can follow it”:** replace with **“The instructions can be supplied to other assistants; reliable application and output quality there remain unestablished.”**
   - **CHANGELOG “R9 patch … untested” / fair-retest “These are untested”:** replace with **“Initially untested; subsequently examined in the reduced held-out comparison linked below.”**
   - **CHANGELOG “108 outputs … Run later in this release”:** replace with **“The planned 108-output protocol was not completed. A reduced S/P/U comparison was run: nine tasks, one generation per edited arm, one judge, without O or C*.”**
   - **FINAL-RESULTS “Every prompt … is in the linked folders”:** the pasted material cannot establish that archive claim. Identify the exact generation instructions, complete task texts, versions/settings, judging packets and freeze record. The displayed H prompt contains an ellipsis, so it is not itself an exact reproducibility record.
   - **Freeze claim:** a hash identifies material; it does not by itself establish when it was frozen. Link the pre-generation record if available; otherwise say **“The author reports that materials were frozen before generation.”**

   Keep historical prompts and verdicts unchanged. Add corrections alongside them rather than silently rewriting the experiment.

12. **My earlier recommendations were not all right.**

   On the recommendations documented in this conversation:

   - **The preservation-first design was initially too absolute.** Requiring a “present failure” for every edit can obstruct a legitimate transformation; unconditional claim preservation can freeze an error. The correction/authorization exceptions were necessary repairs to a design I helped push. Moving that exception into slot 3 is the remaining cleanup.
   - **I overscoped the next validation step.** Four arms × nine tasks × three runs bundled patch checking, comparison with ordinary editing and component attribution into one expensive exercise. Those are separate questions. A smaller patch check was reasonable; my mistake would be treating completion of the full design as a release prerequisite.
   - **The knowledge-boundary addition was a plausible editorial hypothesis, not an established improvement.** Its new test produced overdiagnosis in both versions. I should not give the added check credit merely because its rationale sounds sophisticated. The appropriate next move is comparison on genuine violations and legitimate foreknowledge—not another stronger instruction to find leaks.
   - **“Keep light EDIT out of structural review” was overcautious shorthand.** A cross-paragraph contradiction can warrant a small, authorized repair. The narrower current wording—narrative genre alone must not expand scope—is preferable.

   I cannot honestly identify which recommendation caused task 05’s loss: the six changes were bundled and sampled once. Nor does P’s failure on knowledge establish that adding the check made that behavior worse. Owning a design mistake does not justify inventing causal evidence against myself.

13. **Next steps, ranked by value per cost.**

   1. **Correct the public record now.** Remove X from the efficacy scorecard, distinguish versions, fix the fidelity denominator, acknowledge the held-out loss, and separate ranking from reliability. This requires no new model run.
   2. **Do the small snippet regression check if you keep promoting always-on editing.** It is a newly packaged instruction set with omitted exceptions.
   3. **If you retain “reduced slop” as a headline, rejudge existing WRITE outputs using neutral purpose-fit criteria and exact task materials.** This is more valuable than rescuing X. Otherwise drop the aesthetic efficacy claim and keep the original rankings explicitly provisional.
   4. **Then stop, if stopping is the goal.** An experimental release does not need another expansive model-only study.
   5. **For the next substantive milestone, use blind human evaluation against strong ordinary editing.** Add a matched lens-removal arm only if component complexity is a decision you actually intend to make. A cumulative “+guard, +routing, +lenses…” ladder is order-dependent and does not cleanly allocate credit among interacting instructions.

   **Verdict:** v1.1.0 is a reasonable experimental writing package with promising model-judged results and an unusually inspectable history of failures. Its current report still turns preferences into broader assurances and repeats an invalid interpretation of the bare-edit run. Correct those claims and the always-on inconsistencies; keep the main design largely stable. It is neither a validated general writing improvement nor evidence that StoryScope’s lenses improve prose, and it does not need to become either before being useful to someone who wants these editing defaults.

   **Interview sentence:** “I built HumanScope, compared it with bare prompts and a strong editing baseline, and published both the promising model-judged results and the failures and confounds that limit what we can claim.”