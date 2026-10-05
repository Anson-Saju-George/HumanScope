# Using HumanScope in ChatGPT

ChatGPT can't install a skill from GitHub the way Claude Code does. It can keep instructions
and files attached, though, so you set HumanScope up once and it applies every time. There are two
ways to do it. Both use the same two files:

- [`instructions.txt`](instructions.txt): a short instructions block (about 2,000 characters).
  It tells ChatGPT to follow SKILL.md and quotes the core rules from it word for word.
- [`../SKILL.md`](../SKILL.md): the full method. At about 12,700 characters it's too long for an
  instructions box, so it goes in as an attached file.

Download SKILL.md on its own (no need to clone the repo): open
[SKILL.md on GitHub](https://github.com/Anson-Saju-George/HumanScope/blob/main/SKILL.md) and use
the download button, or get the raw file at
`https://raw.githubusercontent.com/Anson-Saju-George/HumanScope/main/SKILL.md`.

## Option A: a Custom GPT (reusable, shareable by link)

1. In ChatGPT, open **GPTs → Create**, then the **Configure** tab.
2. **Name:** HumanScope. **Description:** "Writes and edits without inventing facts or overwriting
   your voice."
3. **Instructions:** paste the whole of `instructions.txt`.
4. **Knowledge:** upload `SKILL.md`.
5. Save. Keep it private, or share the link.

## Option B: a Project (your own chats)

1. Create a **Project**, then open its settings.
2. Paste `instructions.txt` into the project **instructions**.
3. Add `SKILL.md` to the project **files**.
4. Start your writing and editing chats inside that project.

## One-off (no setup)

Upload `SKILL.md` into a chat and say: *"Follow this file as your instructions for the rest of this
conversation."* It works, but you have to repeat it in every new chat.

## Be aware

- Menu names in ChatGPT change over time; if a step doesn't match what you see, look for "custom
  instructions", "knowledge", or "project files".
- **Untested for quality.** All HumanScope evaluations were run on Claude. ChatGPT has read SKILL.md
  and summarized the approach correctly, but how well it *applies* it hasn't been measured.
- `instructions.txt` adds no new rules. It only points to SKILL.md and quotes it, so the method is
  the same one that was tested.
