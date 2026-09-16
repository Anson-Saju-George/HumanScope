# Smoke Test — one executed case (proves the eval runs)

A single case run end-to-end so `evals/` isn't just a blueprint (Astra R-final). One executed case is
not validation — it demonstrates the protocol and that HumanScope shows restraint, nothing more.

## Case: business update, EDIT / light (genre = workplace non-fiction)

**Brief:** "Tighten this status line for a team email. Keep it factual and plain."
**Source facts:** the team shipped the billing migration; it's now live; one bug remains, tracked.

**U (untouched input):**
> The migration was, at its core, a truly pivotal milestone. It's important to note that the team,
> working collaboratively together, achieved a highly successful outcome that underscores their
> capabilities, and the future looks bright.

**O (ordinary "clean this up" edit, no HumanScope):**
> The migration was a major milestone. The team worked together to deliver a successful outcome, and
> the future looks bright.

**H (HumanScope):**
Diagnosis (genre gates L2–L6 mostly off; L1 applies):
- L1 — *Evidence:* "It's important to note that…", "at its core", "the future looks bright." *Effect:*
  report status plainly. *Failure:* editorializing filler + an unsupported forward-looking claim that
  the source facts don't establish. *Change:* cut filler; state what shipped.
- Factual: source says a bug remains — U omits it; a status line that hides it is inaccurate. Add it.
- Preserve: "milestone" and the plain register are fine; no further change.
> The billing migration is live — a real milestone for the team. One known bug remains and is tracked.

## Scoring (rubric dimensions, 1–5; blind intent: rater given brief + facts)
| Dimension | U | O | H |
|---|---|---|---|
| Fidelity of meaning | 3 | 4 | 5 |
| Factual integrity | 2 (omits the bug) | 2 (also omits it) | **5** (surfaces it) |
| Appropriate explicitness (L1) | 2 | 4 | 5 |
| Voice / register preserved | — | 4 | 4 |
| Intervention discipline | — | 4 | 4 |
| Overall reader preference | 1 | 3 | **5** |

**Read:** O beats U (any editing does). **H beats O** because it did the thing ordinary editing
missed — caught that the update was *factually incomplete* (the tracked bug), which is exactly
HumanScope's discipline (facts + fitness-for-purpose), not surface polish. This is the U/O/H
comparison working as intended. **PASS** (no regression vs U; H > O on the headline).

*Caveat:* n = 1, self-scored by the same model that produced H (a weak proxy — the rubric calls for
blind human rating). Treat as a plumbing check, not evidence of general efficacy.
