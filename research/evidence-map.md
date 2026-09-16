# Evidence Map — every core feature → lens, hypothesis, applicability, counterexample, eval

Traceability layer required by the brief (§19) and Astra R3 (must-fix #3). Maps **all 30 unique
StoryScope core features** (Table 16; 33 rows = 30 features + 3 categoricals shown on both sides) to
a diagnostic lens, or marks it deliberately unused. Columns:

- **Feature (H/AI)** — the measured feature and human/AI values (means for `s`/`o`; prevalence for
  categorical). Directions only where the paper is internally inconsistent.
- **Lens** — L1 Explanation·interpretation · L2 Presentation · L3 Causality·closure · L4 Information
  order · L5 Referential grounding · L6 Reader relationship · M = editorial meta-lens.
- **Editorial hypothesis (conditional)** — a *question to ask*, never a direction to push. All are
  hypotheses; none is a validated intervention.
- **Applies** — describe the *particular purpose* where the move helps; avoid categorical "transfers/reverses" labels.
- **Counterexample (do NOT act when…)** — the §25 brake for this feature.
- **Eval** — how we'd test whether acting actually helps (see `evals/`).

> Reminder: values are *descriptive classifier signals*, not quality targets (limitations §6, §8).
> "More human-correlated" may never be the reason to edit. Every edit fills evidence→effect→
> failure→smallest-change, or nothing changes.
>
> **Governing question for every row:** "Does this choice improve the intended effect while
> preserving the brief?" Judge *neither* a choice's frequency in AI writing *nor* its conformity to
> a preferred device. Directional labels below are candidate complaints requiring independent
> justification, not targets.

## L1 · Explanation & interpretation
| Feature (H/AI) | Editorial hypothesis | Applies | Counterexample | Eval |
|---|---|---|---|---|
| Thematic Explicitness & Moralizing s 3.28/3.94 | Is the theme/moral *stated* where the scene already implies it, defeating an intended inference? | Purpose-dependent (explicit thesis is wanted in many essays/reports) | A stated theme the author wants explicit; didactic genres | Blind readers rate "over-explained?" pre/post; author-intent preserved |
| Moral/Philosophical Weighting s 3.26/3.68 | Is philosophical weight *added* beyond what the piece needs? | Fiction only | Purposefully philosophical work | Reader "feels preachy?" delta |
| Thematic Unity s 4.41/4.74 | Does the degree of thematic alignment serve the intended effect? | Fiction only | Tightly-themed short forms where unity is a virtue | — (weak lever; observe only) |
| Narratorial Thematic Commentary =yes 52%/77% | Does the narrator/text explain meaning the reader could otherwise infer, and does that serve the purpose? | Purpose-dependent (explicit conclusions are wanted in some non-fiction) | Essay conclusions; instructional summaries | Reader inference test |
| Dialogue Function =philosophical debate 34%/59% | Is dialogue carrying argument the scene doesn't need? | Fiction only | Idea-driven fiction (Le Guin, dialogues) | Reader "on-the-nose?" delta |
| Moral Polarity =ambivalent/mixed (H) 59% / 38% AI | Is the protagonist's moral status *flattened* to clearly good/bad where ambiguity would be truer? | Fiction only | Fable/parable/genre where clarity is the point | Reader "moral richness / believability" |

## L2 · Presentation choices
| Feature (H/AI) | Editorial hypothesis | Applies | Counterexample | Eval |
|---|---|---|---|---|
| Emotional Expression =embodied 81% AI / explicit-labels 29% H | Does one passage render *every* feeling as body-metaphor past the point of effect? (NOT "name feelings more.") | Fiction mostly | Sustained embodiment that works; a single scene | Reader "repetitive device?" from the text |
| Setting as Psychological Mirror s 3.58/4.07 | Is setting *reflexively* mirroring mood in every scene? | Fiction only | Deliberate pathetic-fallacy style | — observe |
| Environmental/Ecological Emphasis s 2.83/3.21 | Is nature description doing narrative work or padding? | Fiction only | Eco/nature-centered work | — observe |
| Sensory Modalities =olfactory 57%/82% | Does the mix of sensory channels serve the passage, or does one channel crowd out others? (Judge by effect, not by any channel's frequency in AI writing.) | Fiction only | Scent-centered scenes | Reader "sensory balance?" |
| Sensory Density s 3.66/3.93 | Is description lush past the point of clarity/purpose? | Fiction only | Lush style done well; genre expectation | Reader "overwritten?" delta |
| Depth of Interior Access s 3.67/3.93 | Does the chosen access to interior experience serve this passage? | Fiction only | Interior-driven literary POV | Reader "interiority fits?" |
| Character Introduction =external description 30%/52% | Is the lead introduced via static description where action/voice would be stronger? | Fiction only | Deliberate portrait opening | Reader engagement of opening |
| Spatial Granularity o 2.27/2.53 | Is physical space over-specified beyond what the scene needs? | Purpose-dependent (precise detail is wanted in technical prose) | Procedurals; spatial stories | — observe |
| Dialogue-to-Narration Proportion s 2.95/2.70 (T7) | Is the balance serving pace, or is narration crowding out scene? | Fiction only | Narration-heavy styles | Reader pacing |

## L3 · Causality & closure  *(heaviest-touch; loosening only on authorized deep edit / as suggestion)*
| Feature (H/AI) | Editorial hypothesis | Applies | Counterexample | Eval |
|---|---|---|---|---|
| Causal Chain Continuity s 3.92/4.20 | Does the ending follow from established pressures? (May justify *strengthening* causality.) | Purpose-dependent (clear causation usually wanted in nonfiction) | Mysteries/literary work using ellipsis on purpose | Reader "earned ending?" |
| Agency in Resolution =protagonist choice 46%/69% | Is the outcome *mechanically* protagonist-driven where external forces would be truer? | Fiction only | Agency-driven arcs (most genre) | Reader "believable resolution?" |
| Resolution Mode =internal understanding 27%/47% | Do the resolution mechanism and degree of closure fit the established tension? | Fiction only | Stories that earn catharsis | Reader "resolution fits?" delta |
| Subplot Integration =no-subplots 79% AI / thematically-parallel 42% H | Is a necessary secondary development missing, or would another thread dilute the piece? (Do NOT prescribe *independent* subplots — data is across all stories.) | Fiction only | Tight single-thread short stories | Reader "richness vs bloat" |
| Location Variety Scope o 1.34/1.08 (T7) | Does the location scope serve the story? | Fiction only | Bottle episodes; unity-of-place | — observe |

## L4 · Information order
| Feature (H/AI) | Editorial hypothesis | Applies | Counterexample | Eval |
|---|---|---|---|---|
| Depth of Recontextualization After Surprise s 3.28/2.95 | Does a later reveal reward re-reading earlier scenes? (Placement, not "add twists.") | Purpose-dependent (revisiting evidence helps some essays) | Straightforward narratives | Reader "satisfying reframe?" |
| Chronological Discontinuity s 2.40/2.12 | Is strict chronology the best order for the intended effect? (NOT "add flashbacks.") | Purpose-dependent (much non-fiction is answer-first, not chronological) | Procedures needing step order | Reader comprehension + interest |
| Nonlinear Framing for Delayed Disclosure s 1.96/1.68 | Would delaying a disclosure create intended curiosity — without harming clarity? | Fiction only | Info the reader needs up front | Reader curiosity vs confusion |
| Anachrony Intensity s 2.58/2.31 | Are flashbacks/forwards earning their disruption? | Fiction only | Linear stories that work | — observe |
| Pre-Threat Character Investment s 2.76/2.99 | Does space go to building stakes before jeopardy, or is a decisive turn rushed? (pacing/proportion → see M2) | Fiction only | Deliberately abrupt openings (in medias res) | Reader stakes/engagement |
| Opening Spatial Grounding o 2.12/2.33 | Does the opening provide the orientation this reader needs? | Fiction only | Preserve deliberate disorientation when it serves the brief | Reader "grounded at start?" |

## L5 · Referential grounding
| Feature (H/AI) | Editorial hypothesis | Applies | Counterexample | Eval |
|---|---|---|---|---|
| Intertextual Strategy =explicit named reference 47% H / 24% AI | Would changing reference specificity solve an identified problem? (Allusion ≠ citation; substantiate real-world claims; never invent real refs.) | Purpose-dependent (real sources/citation matter in nonfiction) | Works that avoid allusion by design; ornamental name-drops | Reader "concrete vs vague"; fact-check |
| Reference Explicitness =balanced-mix 37% H / implicit-echoes 72% AI | Is every reference a vague gesture where some should be named? | Transfers | Deliberately allusive styles | Same as above |

## L6 · Reader relationship
| Feature (H/AI) | Editorial hypothesis | Applies | Counterexample | Eval |
|---|---|---|---|---|
| Fourth-Wall Permeability o (H>AI, direction only) | Is the intended narrator↔reader stance consistent? (Neither presence nor absence is a default defect.) | Fiction/informal only | Impersonal formal prose | Reader "voice consistency" |
| Direct Reader Address o (H>AI, direction only) | Direct "you" — fitting for this form or intrusive? | Transfers (tutorials/marketing use "you") | Formal reports | Reader appropriateness |

## Editorial meta-lenses (NOT paper-derived — Astra)
| Lens | Question | Applies | Eval |
|---|---|---|---|
| M1 Selection before arrangement | Is this the right *material* for the central concern? | All | Reader relevance |
| M2 Attention & proportion | Does space go to the consequential moments? | All | Reader "well-paced?" |
| M3 Character-specific necessity | Would *this* person notice/say/choose this? | Fiction | Reader "believable motivation?" |

## Deliberately unused / observe-only
- **NarraBench Style dimension features** (39) — excluded from our narrative focus by design; these
  are the surface tells other humanizers already cover (see secondary-sources.md), handled only via
  the lightweight non-fiction surface layer, never as the core.
- **Per-model fingerprint features** (75, Table 17) — descriptive author signatures (e.g. Claude's
  flat escalation, GPT's gossip). **Not** editing targets; kept only as "habits to notice."
- Any feature whose only rationale would be "more human-correlated" is **excluded from action** by
  the four-slot rule.

## Coverage check
30 unique core features mapped: L1×6, L2×9, L3×5, L4×6, L5×2, L6×2 (categoricals counted once;
several features cross-listed by theme). No core feature is left without a lens or an explicit
observe-only status.
