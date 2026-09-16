# HumanScope — Worked Examples

Each case shows the **diagnosis** (four-slot: evidence → intended effect → present failure →
smallest change), the edit, and — crucially — cases where the right answer is **no change**. These
illustrate the lenses; they are not proof the lenses improve writing (that's what `evals/` tests).

---

## 1 · Fiction, light edit — L1 (over-explanation) + L2 (monotone presentation)

**Author brief (matters — the diagnosis depends on it):** *"Literary short story. I want the loss to
land through image and action; keep the theme implicit — don't spell out the meaning."* This brief is
what authorizes trimming stated interpretation; without it, cutting the moral would change meaning.

**Before (AI draft):**
> Maya's hands trembled as a cold knot tightened in her stomach and ice spread through her veins.
> She stared at the eviction notice. In that moment she understood that the house had never really
> been hers — that belonging was something you were only ever loaned, and that everyone, sooner or
> later, has to learn to let go.

**Diagnosis (only two findings; the rest is fine):**
- **L1** — *Evidence:* "she understood that … everyone, sooner or later, has to learn to let go."
  *Intended effect (per brief):* the reader should feel the loss, not be told its lesson. *Present
  failure:* the narrator states a general moral the brief wants implicit. *Change:* cut the stated
  moral (brief-authorized).
- **L2** — *Evidence:* "cold knot tightened … ice spread through her veins." *Intended effect:*
  convey fear. *Present failure:* two body-metaphors stacked on one beat — the device repeats past
  effect. *Change:* keep **one**; leave the existing action ("stared") to carry the rest.

**After:**
> Maya's hands trembled as she stared at the eviction notice. The house had never really been hers,
> then.

*Left alone:* voice, POV, the concrete "eviction notice," sentence rhythm — and no new story action
was invented. Two minimal edits, both traceable to the brief.

---

## 2 · Non-fiction (explanatory essay) — L1 transfers, but fiction lenses are GATED OFF

**Before (AI draft):**
> It's important to note that caching is, at its core, a fundamental technique that can dramatically
> transform performance. From small scripts to massive distributed systems, caching stores the
> results of expensive operations so they don't have to be repeated. In conclusion, caching is a
> pivotal tool worth understanding.

**Diagnosis:**
- **L1 (applies to this explainer):** *Evidence:* "It's important to note that…", "In conclusion,
  caching is a pivotal tool worth understanding." *Intended effect:* teach what caching is. *Present
  failure:* the editorializing opener and the restating conclusion add no information. *Change:*
  delete both; state the mechanism directly.
- *(No L5 finding: "from small scripts to massive distributed systems" is a legitimate range of
  deployment scale, not a false range — left as is. A concrete example is added below because the
  passage lacks one, not to "fix a tell.")*
- **Domain gate:** L3/L4 fiction moves (loosen causality, delay disclosure) are **not applied** —
  an explainer should be tidy and answer-first. L2 sensory/interiority is **N/A**.

**After:**
> Caching stores the result of an expensive operation so it doesn't have to be recomputed. A web
> app that queries the same user profile on every request, for instance, can cache it after the
> first read and serve later requests from memory — turning a database round-trip into a lookup.

---

## 3 · Deep edit (requested) — L3 structural, on authorization

**Context:** author explicitly asked for a structural pass on a short story whose ending felt flat.

- **L3** — *Evidence:* the antagonist confesses and the protagonist instantly forgives; nothing
  earlier set up that capacity for forgiveness. *Intended effect:* an earned resolution. *Present
  failure:* the ending doesn't follow from established pressures (unsupported causal jump), not
  merely "too tidy." *Change (deep edit authorized):* plant one earlier beat of the protagonist
  extending small mercy, so the final forgiveness is caused, not convenient.
- Note this **strengthened** causality rather than loosening it — L3 cuts both ways.

---

## 4 · REGRESSION — already-strong prose → **NO CHANGE**

**Input (a deliberately spare, strong opening):**
> The dog arrived on a Tuesday. Alistair would later call it significant, though he could never say
> why.

**Diagnosis:** L1 no stated theme; L2 no device repetition; L4 the withholding ("could never say
why") is a deliberate, working hook, not a defect; L5 "Tuesday"/"Alistair" are already specific.
**Action:** none. Return unchanged, note it's working. *A near-empty diff is a success.*

---

## 5 · REGRESSION — technical doc where "AI-like tidiness" is CORRECT

**Input (API doc excerpt, written to be unambiguous):**
> `retry(fn, maxAttempts)` calls `fn`. On failure it waits `2^(k-1) × 100 ms` before attempt *k*
> (so 0 ms, 100 ms, 200 ms, …), making at most `maxAttempts` total calls. If the final attempt
> fails, it re-throws that attempt's error.

**Diagnosis:** perfectly linear, tidy, single-track, impersonal — every one an AI-elevated *fiction*
trait, and every one **exactly right here**. Applying L3/L4/L6 fiction directions would wreck the
doc, so they're gated off. **Action:** none.
**Caveat this example teaches:** tidiness ≠ correctness. HumanScope does *not* certify technical
accuracy. If the text were vague (e.g. "waits `2^n × 100ms`" with `n` undefined, or "the original
error" when several errors occur), the right move is a **clarification** finding — a
factual/clarity fix that is L-independent — *not* a fiction lens. Domain-gating decides which lenses
apply; it never validates the content.
