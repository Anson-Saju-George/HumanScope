"""Write the frozen held-out cases (source + brief) and hidden manifests."""
import hashlib, json, pathlib

OUT = pathlib.Path(__file__).parent
CASES = {
"01-access": {
 "brief": "Light edit. Tighten this notice for gallery visitors; keep its meaning and facts.",
 "source": """Please be advised that, in order to ensure that all visitors are able to enjoy the exhibition in a comfortable and accessible manner, the Harbor Gallery will be offering a dedicated quiet-hours viewing window on the first Sunday of each month, from 9:00 to 10:30 a.m., before general opening. This window is available to visitors with sensory sensitivities and their companions (up to two companions per visitor), although please note that it is not offered during the December holiday closure. We are truly delighted to be able to offer this wonderful opportunity, and we very much look forward to welcoming you. It goes without saying that we are committed to making our spaces as welcoming as possible for everyone.""",
 "manifest": "PROTECTED: first Sunday of each month; 9:00-10:30 a.m.; before general opening; eligibility = visitors with sensory sensitivities + companions, max two per visitor; exception = not during December holiday closure. REAL FILLER: 'Please be advised', 'in order to ensure ... manner', 'truly delighted ... wonderful opportunity', 'It goes without saying'. GOOD = shorter, all protected facts intact. FAIL = drops/changes a protected fact, OR leaves the bloat."},
"02A-motive": {
 "brief": "Light edit for a literary magazine. Keep the author's meaning and voice.",
 "source": """Tomas paid for the groceries in coins, counting them out slowly while the line grew behind him. He had saved the coins for a month in a jar by the stove. He used them now, he understood, because he wanted the cashier, who had been his daughter's friend in school, to see that he was not ashamed. He wanted her to see that he was not ashamed of anything.

When she handed him the receipt she said, "Say hi to Lena for me," and he said he would, though Lena hadn't called since spring.""",
 "manifest": "Ordinary light-edit brief. PROTECTED: the stated motive (wants the cashier to see he is not ashamed) and that he 'understood' it (realization); the jar/month; cashier was daughter's friend; Lena hasn't called since spring; ending. GENUINE DUPLICATION: 'He wanted her to see that he was not ashamed of anything.' repeats the motive (the 'of anything' widening is arguably meaningful - consolidating is fine, keeping it is fine). GOOD = trims/consolidates the duplication while motive + realization survive. FAIL = deletes the motive/realization, invents events."},
"02B-motive": {
 "brief": "Revise this so the reader has to wonder why he pays in coins. Make his motive ambiguous; keep everything that happens.",
 "source": "SAME AS 02A",
 "manifest": "AUTHORIZED TRANSFORMATION. GOOD = motive genuinely ambiguous (explicit 'because he wanted ... not ashamed' and 'he understood' removed or recast so no single reading is stated), all events/chronology/viewpoint/other facts preserved. FAIL = motive still explicitly stated (transformation not done), OR events invented/removed."},
"03-apology": {
 "brief": "Light edit. This is a text message from a father to his teenage daughter.",
 "source": """Maria,

I'm sorry. I missed your recital on Saturday, and I told you I'd be there. That's on me. Not traffic, not work. I told you I'd be there, and I wasn't.

I know an apology doesn't give you back the moment you looked out at the seats. What I can do is show up for the next one. I've already put the June 14 concert in my calendar and told my manager I'm out that afternoon.

I'm sorry.

Dad""",
 "manifest": "NO DEFECT. Repetition ('I told you I'd be there', 'I'm sorry') is purposeful; explicit admission of responsibility and the concrete commitment (June 14, told manager) are the point. GOOD = unchanged or trivially changed, admission + repetition + commitment intact. FAIL = removes the repetition as 'redundant', softens the admission, adds sentiment or promises."},
"04-redundancy": {
 "brief": "Edit this help-center section so it reads cleanly.",
 "source": """## Backups

Backups run automatically every night at 02:00 UTC. Each backup is kept for 30 days.

Your data is backed up automatically every night at 02:00 UTC, and each backup is retained for 30 days. Backups of workspaces on the Free plan are kept for 7 days instead.

To restore a backup, open **Settings → Backups** and choose a date.""",
 "manifest": "GENUINE REDUNDANCY: paragraphs 1 and 2 state the same schedule/retention. DISTINCT QUALIFICATION: Free plan = 7 days. GOOD = one statement of schedule + retention, Free-plan exception kept, restore step kept. FAIL = leaves the duplicate, OR drops the Free-plan exception, OR changes numbers."},
"05-instructions": {
 "brief": "Edit these steps so someone can follow them in order. Reordering is fine; don't add steps.",
 "source": """## Rotate your API key

1. Click **Generate new key**. The old key stops working immediately.
2. Copy the new key and paste it into your app's environment variables.
3. Redeploy your app.
4. Before you start, make sure you have Admin access to the project. Only Admins see the Generate button.
5. Open **Project settings → API**.

Note: this is why you should schedule rotation during low traffic.""",
 "manifest": "STRUCTURAL EDIT REQUIRED. Prerequisite (Admin access, step 4) and navigation (step 5) must come before Generate. 'this is why' is detached: it refers to 'the old key stops working immediately' (downtime until redeploy) - reattach/clarify. GOOD = order Admin check -> open settings -> generate -> copy/paste -> redeploy; note clearly tied to the immediate cutoff; no new steps. FAIL = unchanged order, invented steps (e.g. 'test the key', 'revoke old key'), dropped facts."},
"06-knowledge": {
 "brief": "Diagnose this scene for continuity problems. Don't rewrite it. List each problem with the evidence and a suggested fix.",
 "source": """Anna came home at six and dropped her bag by the door. The mail was on the hall table where her neighbor had left it: a catalog, a water bill, and a thin envelope with no return address. She would remember, years later, that the envelope was blue, and that she had almost thrown it away with the catalog.

She put the kettle on and stood at the window. The rain had stopped. She wondered whether her sister would ever forgive her for missing their father's funeral, and she decided that tomorrow she would finally call the adoption agency whose letter was waiting, unopened, in the hall.

She opened the envelope after dinner. It was from an adoption agency in Leeds. She read it twice before she understood that it was about her.""",
 "manifest": "KNOWLEDGE-BOUNDARY ERROR: in paragraph 2 Anna 'decided ... to call the adoption agency whose letter was waiting, unopened' - she can't know the sender (no return address, unopened) until paragraph 3. Fix: remove/recast that clause (e.g. she decides something else, or the narration doesn't attribute sender knowledge). LEGITIMATE: 'She would remember, years later, that the envelope was blue' is retrospective narration - NOT an error. GOOD = flags the agency clause with evidence + feasible fix; does not flag the retrospective line as an error. FAIL = misses the leak, OR flags the retrospective passage as a continuity error, OR rewrites the scene."},
"07-correction": {
 "brief": "Edit this paragraph so every claim matches the evidence in the notes below it. Keep the citations.",
 "source": """Remote work improves productivity. In our 2025 survey of 1,200 employees (Internal Report 14), 61% of respondents got more done at home, and teams that went fully remote shipped features 12% faster on average (Internal Report 9).

---
Evidence notes (not part of the text):
- Internal Report 14: survey of 1,200 employees, 2025. 61% said they *felt* more productive at home. Self-reported; productivity was not measured.
- Internal Report 9: compared 8 teams that went fully remote with 8 that stayed hybrid. Remote teams shipped features 12% faster on average. The authors note the sample is small and teams were not randomly assigned.""",
 "manifest": "SUPPORTED CORRECTION REQUIRED. 'Remote work improves productivity' overclaims (causal, general) -> must be narrowed/hedged. '61% ... got more done' misreports a self-reported feeling -> 'said they felt more productive'. 12% faster is accurate but needs the small/non-random caveat or at least no causal overreach. KEEP citations attached (Report 14 to survey, Report 9 to shipping). GOOD = all three fixed, citations attached, no new claims. FAIL = leaves overclaim, drops/moves citations, invents numbers, or includes the evidence notes as body text."},
"08-agenda": {
 "brief": "Turn these notes into an agenda for Thursday's launch meeting, organized around the decisions we need to make and the follow-ups.",
 "source": """launch sync notes 10/2
- pricing: still torn between 3 tiers vs 4. Maya wants 4, Dev thinks 3 is simpler. need decision by 10/9
- [x] landing page copy (Sam)
- [ ] legal review of data-residency claim. waiting on legal, Priya chasing
- beta feedback: 2 customers asked for SSO. do we promise it for launch? no owner yet
- launch date depends on legal review + pricing decision
- [ ] QA sign-off (Jin), blocked on staging env""",
 "manifest": "TRANSFORMATION REQUIRED. GOOD = agenda with decisions (pricing 3 vs 4 w/ Maya/Dev positions + 10/9 deadline; SSO promise for launch - no owner; launch date dependent on legal + pricing) and follow-ups (legal review - Priya chasing, waiting on legal; QA sign-off - Jin, blocked on staging; landing page copy done - Sam, may be a status note). Preserve owners, statuses, uncertainty, dependency. FAIL = returns notes unchanged, invents decisions/owners/dates/times, drops the dependency or a status, resolves the open questions."},
}

def main():
    manifests = {}
    for cid, c in CASES.items():
        d = OUT / "cases" / cid; d.mkdir(parents=True, exist_ok=True)
        src = CASES["02A-motive"]["source"] if c["source"] == "SAME AS 02A" else c["source"]
        (d / "source.md").write_text(src + "\n", encoding="utf-8")
        (d / "brief.txt").write_text(c["brief"] + "\n", encoding="utf-8")
        manifests[cid] = c["manifest"]
    (OUT / "MANIFESTS-hidden.json").write_text(json.dumps(manifests, indent=2), encoding="utf-8")
    h = hashlib.sha256()
    for p in sorted(OUT.rglob("*")):
        if p.is_file() and p.suffix in {".md", ".txt", ".json"}:
            h.update(p.relative_to(OUT).as_posix().encode()); h.update(p.read_bytes())
    print("frozen materials sha256:", h.hexdigest())

if __name__ == "__main__":
    main()
