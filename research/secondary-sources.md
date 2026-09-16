# Secondary Sources Analysis (Tiers 3–4)

All items in `research/research-materials/` were converted to text (`research/research-materials/codex-converted/`)
and read. This file separates **paper-derived** ideas from **general editorial heuristics** from
**folklore / detector-gaming**, and records what HumanScope takes vs. rejects from each.

> Headline: **Every existing humanizer in this corpus works mostly at the SURFACE/lexical layer**
> (a few of their categories — e.g. "staging instead of stating", vague attribution — do reach
> mild structural territory). StoryScope showed that *one* span-level style rewriter barely changed
> its classifier, i.e. surface edits and narrative structure are largely separable — it did **not**
> prove surface edits are worthless, and near-perfect raw-text detectors mean "structure" is not
> the only detectable layer. The genuine gap these tools leave: **discourse-level narrative
> diagnosis**. Two contribute real **architecture** and one a broadly aligned **editorial stance**
> we adapt (not "adopt as proven").

---

## A. Source inventory & classification

| Source | Tier | Type | Core value | Verdict |
|---|---|---|---|---|
| **StoryScope** (paper) | 1 | Research | Narrative-structural human/AI differences | Foundation (see paper-notes.md) |
| **Wikipedia: Signs of AI writing** (+Talk page) | 3 | Reference catalog | ~12 surface tells, crowd-observed | Diagnostic candidates for non-fiction; NOT prescriptions |
| **Beutler Ink** "How to Spot AI Writing" | 3 | Blog (distill of Wikipedia) | 7 business-context tells | Same 12 tells, business framing |
| **blakestockton** "10 Takeaways" | 3 | Blog (distill of Wikipedia) | Same list, condensed | Redundant with above |
| **humanizeai.com** blog | 3 | Blog + prompt + research | *Anti-checklist* philosophy, data, H.E.A.R.T. | **Strong ally** — adopt philosophy |
| **blader/humanizer** (GitHub v2.5) | 3 | Claude skill | 25 patterns, "default choice" philosophy, weak-alone clustering, voice-match, 3-pass | Adopt method; it lacks structure |
| **Matt-Payne/content-humanizer** (GitHub) | 3 | Claude skill | 33 patterns, mode-detection, carve-outs, references/ architecture | Adopt architecture; it lacks structure |
| **Video: "I Built a Claude Humanizer…"** (Matt-Payne walkthrough) | 4 | Tutorial | SKILL.md-as-router + references/ hierarchy; diagnose-only mode; self-appending examples | Architecture ideas |
| **Video: "Make Claude Write Like YOU"** (AR) | 4 | Tutorial | Independently rediscovers the *residual structural* signal after surface fixes | Corroboration; rejects its detector-chasing method |
| **Video: "How to Make AI Write Like a Human"** | 4 | Tutorial | Promo for blader/humanizer | Low value |
| **Video: "8 Claude Skills…"** (AR) | 4 | Tutorial | #1 = a *process-interview* skill (10–15 Qs before acting) | Adopt as optional intake pattern |
| **docx** "How to Use the Humanizer Skill" | 3 | Guide | Install steps for blader/humanizer | Low value (install doc) |

---

## B. The Wikipedia "Signs of AI writing" 12 tells (the shared surface canon)

Repeated near-verbatim across Wikipedia, Beutler, blakestockton, humanizeai, and both repos:

1. Formulaic em-dashes  2. Rule-of-three lists  3. Vague attribution ("studies show")
4. Overemphasis on significance ("vital," "testament")  5. False ranges ("from X to Y")
6. Section summaries that restate ("in conclusion")  7. Superficial analysis ("highlighting")
8. Negative parallelism ("it's not just X, it's Y")  9. Editorializing asides ("it's important to note")
10. Letter-style phrasing in non-letters  11. Leftover chat residue ("I hope this helps!")
12. Formatting habits (excessive bold, title-case headings, emojis).

**HumanScope treatment:** these are a **non-fiction DIAGNOSTIC layer** only — useful because
StoryScope says nothing about non-fiction. They are **NOT universal bans** (see rejected-ideas).
A few (3 vague attribution, 5 false ranges, 6 restating summaries, 7 superficial analysis) are
genuinely *structural* over-patterning and map onto StoryScope's over-determination/closure
themes. The rest are surface/style and must stay "flag, don't flatten."

---

## C. Idea-provenance ledger (brief §13 format)

| Idea | Source | Paper support | Useful? | HumanScope treatment |
|---|---|---|---|---|
| Narrative structure carries a signal robust to one style-rewriter | StoryScope | ★ Direct (narrow, see limitations §9) | ★★★ | **Core focus** — HumanScope works at the discourse layer these tools skip |
| "LLMs default to statistically likely choices; humans write for a specific reader; every tell is a form of that default" | blader | A *framing hypothesis*, echoing the paper's convergence finding (not a proven mechanism) | ★★ | **Borrow as a heuristic lens**, not as established causation |
| Addition, not only subtraction — also check for what's *missing* (unsupported claims, missing specificity), not just tells to cut | humanizeai | Editorial (the paper doesn't test this) | ★★★ | **Adopt the emphasis.** NB: the source's slogan "a checklist can only measure what's present, never what's missing" is overstated — "is a required source missing?" is itself a checklist item; the real point is that subtraction-only editing flattens voice |
| "Flag, don't flatten" — mark candidates + say if removal improves or flattens | humanizeai | — (editorial) | ★★★ | **Adopt** as the intervention discipline (= brief's "minimum effective intervention") |
| Weak-alone patterns: only edit surface tells when several cluster | blader | — (editorial) | ★★★ | **Adopt** — preserves voice; kills the em-dash-ban failure mode |
| Integrity rule (don't present invented material as real-world evidence/testimony/citation/bio) | blader, Matt-Payne | — (safety) | ★★★ | **Adopt — but RESCOPED**: the repos' "never invent names/numbers" would forbid writing fiction; scope it to *real-world claims only*, allow fictional invention (blocks hallucination/name-dropping without blocking storytelling) |
| Mode detection (marketing vs reference) + per-mode carve-outs | Matt-Payne | — | ★★★ | **Adopt & extend** to fiction/nonfiction/technical × purpose (Codex #10 gating) |
| SKILL.md as thin router → references/ for depth (progressive disclosure) | Matt-Payne video | — (skill-eng) | ★★★ | **Adopt** as our architecture (brief §20/§22) |
| Diagnose-only / suggestions mode (no rewrite) | Matt-Payne video | — | ★★★ | **Adopt** = HumanScope DIAGNOSE mode (brief §16) |
| Voice calibration from user samples | blader, Matt-Payne | — | ★★ | **Adopt** = optional voice-match (preserves author, brief §9) |
| Optional interview intake (ask user 10–15 Qs to learn voice/intent) | "8 Skills" video, user note | — | ★★ | **Adopt as OPTIONAL** — off by default to avoid friction; on for WRITE/voice-match |
| Self-critique second pass (rewrite → critique → final) | blader, Matt-Payne | — | ★★ | **Adopt**, but as a *restraint* check (did I over-edit?), not a "find more to cut" pass |
| H.E.A.R.T. addition checklist (Human-first, Evidence, Answer-first, Real voice, Trust) | humanizeai | — (editorial, nonfiction) | ★★ | **Adapt** for non-fiction addition pass; label as editorial not paper-derived |
| After fixing surface tells, a creator *felt* a structural residue remained | "Make Claude Write Like YOU" video | Anecdotal; a detector-score demo does NOT independently corroborate a structural mechanism | ★ | Weak anecdote only; creator chased detector %, which we reject |
| Self-appending examples file (grows from each edit) | Matt-Payne video | — | ★ | Nice-to-have; defer past v1 |
| 24+/25/33 pattern removal lists | blader, Matt-Payne | Surface only | ★ | Mine for the few structural ones; reject as a blanket bank |
| "Add imperfection / lower reading level / de-format to look human" | "Make Claude Write Like YOU" video | ✗ Contradicts (human=*published* authors) | ✗ | **Reject** (see rejected-ideas) |
| Optimize for AI-detector % (ChatGPT "how much AI?") | 2 videos, blader marketing | ✗ Rejected by brief §10 + humanizeai data | ✗ | **Reject** as objective |
| Ban em-dashes / banned-vocab list ("delve") | Wikipedia-derived repos | ✗ Weak signal (em-dash rate varies more by model family than by human/AI — see rejected-ideas #1; blog stats need primary-source checks) | ✗ | **Reject** as universal rule |

---

## D. What HumanScope inherits, in one paragraph

From **StoryScope**: the narrative-structural diagnostic layer (the 7 themes) as HumanScope's focus
— a real but *narrow* finding, not a proven quality law. From **blader**: the "default choice"
framing (as a heuristic, not proven causation), weak-alone clustering, the (rescoped) integrity
rule, voice-matching, multi-pass. From **Matt-Payne**: the `SKILL.md`-router + `references/`
architecture, mode detection, and per-mode carve-outs. From **humanizeai**: the editorial stance —
*also check what's missing, flag don't flatten, addition not only subtraction* — while discarding
its overstated "checklists can't measure absence" slogan and treating its relayed statistics as
unverified. From the **videos**: diagnose-only mode and the optional interview intake (the "residual
structure" anecdote is a detector-score demo, not evidence). **What none of them have, and
HumanScope adds: discourse-level narrative diagnosis grounded in a peer-reviewed paper, domain-gated
per feature × genre × purpose, with a §25 brake against turning correlations into edits.**
