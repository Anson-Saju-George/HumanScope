# Using HumanScope in ChatGPT

ChatGPT can't install a skill from GitHub the way Claude Code does. You can save HumanScope's
instructions and its reference file in a Custom GPT or a Project for reuse. How well they're applied
still depends on the model. Both setups use the same two files, **from the same release**:

- [`instructions.txt`](instructions.txt): about 2,900 characters. It summarizes the essential rules
  of SKILL.md, **including their exceptions**, and works on its own, because ChatGPT searches
  knowledge files rather than always loading them in full. It is a compressed adaptation, not a
  word-for-word copy.
- [`SKILL.md`](../SKILL.md): the full method, uploaded as a reference (Knowledge) file. At about
  12,700 characters it's too long for the instructions box.

Download both files pinned to this release (v1.1.2), so the instructions and the reference file match:

- `https://raw.githubusercontent.com/Anson-Saju-George/HumanScope/v1.1.2/chatgpt/instructions.txt`
- `https://raw.githubusercontent.com/Anson-Saju-George/HumanScope/v1.1.2/SKILL.md`

## Option A: a Custom GPT

1. In ChatGPT, open **Explore GPTs → Create**, then the **Configure** tab. (Creating GPTs has
   required a paid ChatGPT plan; if you don't see **Create**, your plan doesn't include it.)
2. **Name:** `HumanScope`
3. **Description:** `Experimental writing, editing and structural feedback focused on your intent,
   voice and supplied facts.`
4. **Instructions:** paste the whole of `instructions.txt`.
5. **Conversation starters:**
   - `Light-edit this email. Preserve my voice, facts and level of certainty.`
   - `Turn these notes into a decision agenda. Keep owners, open questions and task statuses.`
   - `Diagnose this story's ending. Show evidence and suggest changes; don't rewrite it.`
   - `Draft a product update from these facts for existing customers.`
6. **Knowledge:** upload `SKILL.md`.
7. Save with visibility **Only me** first, and run the smoke test below.
8. **To publish to the GPT Store:** change visibility to **Everyone** (the Store). Listing is free,
   but the Store requires a verified builder profile (your name or a domain, set in your ChatGPT
   settings). Confirm what your account offers; the options and requirements change over time.

## Option B: a Project (your own chats)

1. Create a **Project** and open its settings.
2. Paste `instructions.txt` into the project **instructions**.
3. Add `SKILL.md` to the project **files**.
4. Keep your writing and editing chats inside that project.

## One-off (no setup)

Upload `SKILL.md` and `instructions.txt` into a chat and say: *"Follow these as your instructions for
the rest of this conversation."* That supplies the method for that conversation only; reliable
application hasn't been established.

## Smoke test before you publish

Test the **actual configured GPT** in fresh chats (not a chat that only describes the instructions).
Run each case twice and read the outputs yourself:

1. **Sparse factual WRITE brief** (e.g. the bakery page): no invented policies, numbers, or
   testimonials.
2. **Text that's already good:** no manufactured defect, no unnecessary rewrite.
3. **Notes to agenda:** it actually transforms, and keeps owners, statuses, and open questions.
4. **Academic or spec edit:** hedges, citation attachment, and normative words (MUST/should) are
   kept.
5. **DIAGNOSE:** evidence-based findings, no unsolicited rewrite.
6. **Fiction WRITE vs EDIT:** invents when writing; keeps established story facts when editing.

Also check a private duplicate **without** the Knowledge file to confirm the core preservation,
transformation, and output rules still work from the instructions alone. Publish, labeled
experimental, only if these pass. Passing shows the packaging works. It does not show comparative
quality, and it doesn't justify claiming "never invents facts".

## Be aware

- This packaging adapts the instructions that were tested on Claude. **Its behavior in ChatGPT needs
  separate checking**; no ChatGPT evaluation has been run.
- ChatGPT menu names change over time. If a step doesn't match what you see, look for
  "instructions", "knowledge", or "project files".
