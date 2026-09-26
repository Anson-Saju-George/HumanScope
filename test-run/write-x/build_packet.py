"""Blind packet for the write-mode test: visible text only, labels shuffled per task."""
import html, json, pathlib, random, re

ROOT = pathlib.Path(__file__).parent
TASKS = {
    "webpage": ("Web page for a local bakery. Facts supplied by the owner: Crumb & Co, 412 SE Division St, "
                "Portland; open Tue-Sun 7am-3pm; naturally leavened sourdough, morning buns, a rotating "
                "seasonal galette; walk-in only, no online orders.",
                ["X1", "X2", "X3", "S1", "S2", "S3", "H", "HS"], ".html"),
    "blog": ("Company blog post: why a 12-person engineering team switched from Jira to Linear last quarter. "
             "Facts supplied: Jira felt slow, too long grooming tickets; Linear's keyboard-first workflow and "
             "cycles fit; downside: lost some reporting they relied on.",
             ["X1", "X2", "X3", "S1", "S2", "S3"], ".md"),
    "email": ("Email to an 8-person team: from next Monday standups move from daily to Mon/Wed/Fri, 15 min "
              "max; Tue/Thu written update in #standup; reason: team asked for more focus time.",
              ["X1", "X2", "X3", "S1", "S2", "S3"], ".md"),
}

def visible_text(raw: str) -> str:
    raw = re.sub(r"(?is)<(script|style|head)[^>]*>.*?</\1>", " ", raw)
    raw = re.sub(r"(?i)<br\s*/?>|</(p|div|h\d|li|section|header|footer|tr|table)>", "\n", raw)
    text = html.unescape(re.sub(r"<[^>]+>", " ", raw))
    lines = [re.sub(r"[ \t]+", " ", l).strip() for l in text.splitlines()]
    return "\n".join(l for l in lines if l)

def main(seed=20260926):
    rng = random.Random(seed)
    key, parts = {}, []
    for task, (brief, arms, ext) in TASKS.items():
        labels = [f"{task[0].upper()}{i+1}" for i in range(len(arms))]
        order = arms[:]; rng.shuffle(order)
        key[task] = dict(zip(labels, order))
        parts.append(f"# TASK: {task}\nBrief: {brief}\n")
        for label, arm in zip(labels, order):
            raw = (ROOT / task / f"{arm}{ext}").read_text(encoding="utf-8")
            body = visible_text(raw) if ext == ".html" else raw.strip()
            parts.append(f"## PIECE {label}\n{body}\n")
    out = ROOT / "_judge"; out.mkdir(exist_ok=True)
    (out / "packet.md").write_text("\n".join(parts), encoding="utf-8")
    (ROOT / "_key.json").write_text(json.dumps({"seed": seed, "key": key}, indent=2), encoding="utf-8")

if __name__ == "__main__":
    main()
