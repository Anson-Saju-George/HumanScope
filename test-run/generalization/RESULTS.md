# Generalization robustness — does HumanScope work on documents / papers / notes / web?

Motivated by Astra's R7 "NEEDS-WORK" audit: we added guards (§1 artifact/format, Core-stance
claim-strength/citation, §5 "notes may remain notes") and then **tested** on real artifacts with
built-in hazards, in **EDIT** mode. Each arm applies the skill (pulled from GitHub) and must
*trim genuine bloat* **while preserving the critical genre element**.

Arms (odd = Claude, even = Codex-family): **A** = Claude Opus + skill · **B** = Codex `gpt-5.6-sol`
+ skill · **C** = Claude Opus + skill (fresh-context replication). *(D = Astra @ high was deemed
unnecessary — A+B already establish cross-model portability; A+C establish Claude consistency.)*

## Matrix — 4 genres × 3 arms = 12 tests
✅ preserved the critical element while trimming filler · ⚠️ a minor observed issue (see notes)

| Genre (hazard) | A · Claude | B · sol | C · Claude(2) | Critical element that survived |
|---|---|---|---|---|
| **Academic** — citations + hedges | ✅ | ✅ | ✅ | both citations stay attached; hedges not hardened; scope kept |
| **Marketing** — repeated CTAs | ✅ ⚠️¹ | ✅ | ✅ | all 3 CTAs kept; proof + scannability + "you" intact |
| **Notes** — fragments/checkboxes | ✅ (identical) | ⚠️² | ✅ (identical) | checkboxes, `#412`, open-question, shorthand |
| **Technical** — MUST + 429 exception | ✅ | ✅ | ✅ | numbers, exception logic, `MUST`/`MUST NOT`/lowercase `should` |

**¹ A-marketing:** changed "has never been more complex" → "keeps getting more complex" (superlative→
trend). Two other arms (B, C) kept the superlative — but two observations cannot establish that this
drift is nonsystematic.
**² B-notes:** `sol` changed `still 3 or 4??` → `3 or 4?`. Removing "still" also drops information
about an unresolved state — a possibly-meaningful unnecessary edit, not merely punctuation. The two
Claude arms left the notes byte-for-byte identical (restraint).

## Reading (what these 12 outputs do and don't show)
- **What was observed:** 4 artifacts, 12 outputs. In each, the arm trimmed some introductory filler
  while keeping the nearby load-bearing tokens (citations, CTAs, note shorthand, normative precision).
  One claim drift (A-marketing) and one possibly-meaningful unnecessary edit (B-notes). Unchanged
  notes demonstrate **restraint**, not bloat removal.
- **What it does NOT show:** there is **no guardless control**, so this cannot prove the *guards*
  caused the preservation (only that these guarded outputs preserved these elements). It is also not
  human-judged, and the hazards mostly reward "delete an intro phrase, keep neighbours" — not distant
  contradictions, citation movement across paragraphs, or warranted repetition.
- **Portability:** consistent behaviour across Claude and Codex-`sol` on these artifacts — a small,
  encouraging sign, not established reliability.

## Honest caveats (governing)
Preservation smoke tests on one artifact per genre, objective greps + one Astra review of the Claude
arm. This **motivates** the guards and shows the specific predicted harms did not occur here; it is
**not** a controlled demonstration that the guards cause preservation, nor an efficacy claim. A
guard-on/guard-off experiment and harder composition cases are v1.1 work. "Distinctive value vs. a
good generic editor" remains for the human protocol (`../../evals/human-eval-protocol.md`).
