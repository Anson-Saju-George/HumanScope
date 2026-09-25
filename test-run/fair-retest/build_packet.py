"""Build a blind judging packet for the fair re-test.

Arms per case are shuffled to letters P/Q/R/T with a fixed seed; the key is
written separately (judges never see it or arm names).
"""
import json, random, pathlib, sys

ROOT = pathlib.Path(__file__).parent
CASES = ["academic", "marketing", "notes", "technical"]
ARMS = ["O", "C", "S", "K"]
LETTERS = ["P", "Q", "R", "T"]

BRIEFS = {
    "academic": "Paragraph from a journal article's introduction (academic readers). Protected: "
                "both (Author, Year) citations stay attached to their claims; hedges; stated scope.",
    "marketing": "Landing-page section for a SaaS product (prospective customers). Protected: all "
                 "calls to action; quantitative proof; headings/scannability; claim strength.",
    "notes": "Personal working notes (the author's own reference). Protected: fragments, checkboxes "
             "and their states, open questions as questions, shorthand, ticket references.",
    "fiction-a": "Literary short-story excerpt, close third person (literary-fiction readers). Protected: "
                 "the story's events and facts, point of view, and its open, unexplained ending.",
    "fiction-b": "Opening of a first-person literary story (literary-fiction readers). Protected: the "
                 "narrator's voice, direct address, and what the narrator chooses to say.",
    "technical": "Section of a technical spec (implementers). Protected: exact numbers and "
                 "exceptions; RFC 2119 normative keywords exactly as written (including case).",
}

def main(seed: int, cases=CASES, tag=""):
    rng = random.Random(seed)
    key, parts = {}, []
    for case in cases:
        d = ROOT / case
        letters = LETTERS[:]
        rng.shuffle(letters)
        key[case] = dict(zip(ARMS, letters))
        parts.append(f"# CASE: {case}\nContext: {BRIEFS[case]}\n\n## ORIGINAL\n"
                     f"{(d / 'input.md').read_text(encoding='utf-8').strip()}\n")
        for arm, letter in sorted(key[case].items(), key=lambda kv: kv[1]):
            parts.append(f"## EDIT {letter}\n{(d / f'{arm}.md').read_text(encoding='utf-8').strip()}\n")
    (ROOT / "_judge").mkdir(exist_ok=True)
    (ROOT / "_judge" / f"packet{tag}.md").write_text("\n".join(parts), encoding="utf-8")
    (ROOT / f"_key{tag}.json").write_text(json.dumps({"seed": seed, "key": key}, indent=2), encoding="utf-8")

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[2] == "fiction":
        main(int(sys.argv[1]), ["fiction-a", "fiction-b"], "-fiction")
    else:
        main(int(sys.argv[1]) if len(sys.argv) > 1 else 20260925)
