# HumanScope Evaluation Rubric

Purpose: test whether HumanScope's edits **actually help a reader** — not whether output differs from
a baseline model, and never a detector score (limitations §11). A near-empty diff on strong input is
a *pass*, not a failure.

## The three-way comparison (required — Astra R4 trap #3)
For each case, produce and blind-compare **three** versions:
1. **U** — the untouched input draft.
2. **O** — an *ordinary competent edit* (a generic "make this better / clean it up" pass, no HumanScope).
3. **H** — the HumanScope output.

This isolates HumanScope's *distinct* contribution: beating U alone shows only that some editing
helped. Produce O and H under the **same brief, sources, model, intensity, and comparable budget**.
Give blinded raters the **brief and source facts** (so fidelity and authorized transformations can
be judged); score edit discipline separately from reader preference.

## Scoring dimensions (1–5; mark provenance)
Paper-derived dimensions are tagged `[P]` (descriptive origin); editorial ones `[E]`.

| Dimension | Question | Origin |
|---|---|---|
| Fidelity of meaning | Is the source's meaning intact? | [E] core |
| Voice preservation | Does it still sound like the author, not a generic tone? | [E] core |
| Factual integrity | Facts accurate; supported errors corrected; nothing invented-as-real? | [E] core |
| Appropriate explicitness | Explanation matches reader need (not over/under)? | [P] L1 |
| Presentation economy | Do devices earn their space; no repeated-device monotony? | [P] L2 |
| Causal/closure adequacy | Do causes & ending fit the intended effect? | [P] L3 |
| Information order | Placement serves comprehension/effect? | [P] L4 |
| Referential specificity | Appropriate references; factual claims supported where needed? | [P] L5 |
| Reader-stance fit | Address/stance appropriate & consistent? | [P] L6 |
| Genre appropriateness | Were fiction lenses correctly gated for the genre? | [E] domain |
| Intervention discipline | Were changes minimal & justified (no needless rewriting)? | [E] core |
| Overall reader preference | Blind: which version would a target reader rather read? | [E] headline |

## Pass criteria
- **H must not regress against U** on task success or protected constraints (Fidelity, Voice,
  Factual integrity, Genre appropriateness) — any such drop is a fail, even if H reads "nicer."
- **H > O** on overall reader preference supports added value. **H = O = U** *passes* a preservation
  case (correct restraint) but does **not** demonstrate added value. Fewer edits is a *secondary*
  tie-breaker only when outcomes are equivalent — never a reason to prefer a harmful smaller edit.
- On already-strong or wrong-genre input, **H ≈ U** is the correct result.

## How to run
Blind the three versions (strip which is which), randomize order, have ≥1 rater (ideally a human;
an LLM-judge is a weak proxy — note it as such). Record per-dimension scores + a one-line why.
Never use "sounds less like AI" or a detector percentage as a criterion.
