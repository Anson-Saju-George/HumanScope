"""Blind packet for the held-out suite: patched (S) vs pre-patch (P) vs untouched source (U)."""
import json, pathlib, random

SCR = pathlib.Path(__file__).parent
CASES = SCR / "heldout" / "cases"; OUT = SCR / "heldout-out"
rng = random.Random(20261004)
key, parts = {}, []
for case in sorted(p.name for p in CASES.iterdir()):
    brief = (CASES / case / "brief.txt").read_text(encoding="utf-8").strip()
    source = (CASES / case / "source.md").read_text(encoding="utf-8").strip()
    cands = {"S": (OUT / case / "S.md").read_text(encoding="utf-8").strip(),
             "P": (OUT / case / "P.md").read_text(encoding="utf-8").strip()}
    if case != "06-knowledge":  # a diagnosis task has no "unchanged" answer
        cands["U"] = source
    arms = list(cands); rng.shuffle(arms)
    labels = ["A", "B", "C"][:len(arms)]
    key[case] = dict(zip(labels, arms))
    parts.append(f"# TASK {case}\nUser's request: {brief}\n\n## SOURCE TEXT\n{source}\n")
    for l, a in zip(labels, arms):
        parts.append(f"## RESPONSE {l}\n{cands[a]}\n")
(SCR / "heldoutjudge").mkdir(exist_ok=True)
(SCR / "heldoutjudge" / "packet.md").write_text("\n".join(parts), encoding="utf-8")
(SCR / "heldout-private" / "_key-heldout.json").write_text(json.dumps({"seed": 20261004, "key": key}, indent=2), encoding="utf-8")
print("ok", sum(len(v) for v in key.values()), "candidates")
