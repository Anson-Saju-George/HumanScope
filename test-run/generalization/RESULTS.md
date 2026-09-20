# Generalization robustness — does HumanScope work on documents / papers / notes / web?

Motivated by Astra's R7 "NEEDS-WORK" audit: we added guards (§1 artifact/format, Core-stance
claim-strength/citation, §5 "notes may remain notes") and then **tested** on real artifacts with
built-in hazards, in **EDIT** mode. Each arm applies the skill (pulled from GitHub) and must
*trim genuine bloat* **while preserving the critical genre element**.

Arms (odd = Claude, even = Codex-family): **A** = Claude Opus + skill · **B** = Codex `gpt-5.6-sol`
+ skill · **C** = Claude Opus + skill (fresh-context replication). *(D = Astra @ high was deemed
unnecessary — A+B already establish cross-model portability; A+C establish Claude consistency.)*

## Matrix — 4 genres × 3 arms = 12 tests
✅ pass (trimmed bloat + preserved the critical element) · ⚠️ minor (non-harmful)

| Genre (hazard) | A · Claude | B · sol | C · Claude(2) | Critical element that survived |
|---|---|---|---|---|
| **Academic** — citations + hedges | ✅ | ✅ | ✅ | both citations stay attached; hedges not hardened; scope kept |
| **Marketing** — repeated CTAs | ✅ ⚠️¹ | ✅ | ✅ | all 3 CTAs kept; proof + scannability + "you" intact |
| **Notes** — fragments/checkboxes | ✅ (identical) | ⚠️² | ✅ (identical) | checkboxes, `#412`, open-question, shorthand |
| **Technical** — MUST + 429 exception | ✅ | ✅ | ✅ | numbers, exception logic, `MUST`/`MUST NOT`/lowercase `should` |

**¹ A-marketing:** nudged "has never been more complex" → "keeps getting more complex" (superlative→
trend). Astra-flagged as minor claim drift. **Did NOT reproduce** in B or C (both kept the
superlative) → a one-off model slip, not a systematic flaw.
**² B-notes:** `sol` normalized `still 3 or 4??` → `3 or 4?` (touched shorthand). Meaning intact, but
less restrained than Claude, which left the notes byte-for-byte identical (A and C).

## Reading
- **10/12 clean; 2 minor, non-harmful, non-reproducing.** In every genre, in every arm, the skill
  trimmed real bloat **and kept the load-bearing element** (citations, CTAs, note shorthand, normative
  precision).
- **Guards hold across two model families** (Claude, Codex-sol) and across a fresh Claude run —
  cross-model + within-model portability confirmed for these artifacts.
- **Restraint works:** notes were returned unchanged by both Claude arms (the "no change is valid"
  path), and no arm prose-ified them or hardened a hedge/normative keyword.
- **Model difference observed:** Claude was slightly more restrained on the notes edge case than
  `sol`; `sol` was slightly more restrained on the marketing superlative than one Claude run.

## Honest caveats (governing)
One artifact per genre, one blinded-ish check per arm (objective preservation greps + one Astra
review of the Claude arm). This demonstrates the **guards prevent the specific harms Astra predicted**
across genres and models; it is **not** a broad efficacy claim. "Distinctive value vs. a good generic
editor" on these genres remains for the human protocol (`../../evals/human-eval-protocol.md`).
Scope language in SKILL.md/README already states genre performance is not formally established.
