#!/usr/bin/env python3
"""Generate the blind input benchmark-blind.md and the map benchmark-map.md from evals/benchmark.md.

Why blind (2026-07-11 deep-review conclusion): each case in benchmark.md carries its own
`Expected` / `Reason`, which hands the answer to the model under test; the ID prefix (SF / SNF)
and the symptom in the title also leak "should it change or not". A real run tests rule
behavior on unfamiliar text, so the model under test may see only: an anonymized ID + scene +
original text, with the order shuffled by a fixed seed.

Usage: run `python3 automation/eval/make_blind.py` in the repo root.
After adding/removing cases in benchmark.md, re-run this script; hand-editing the generated
files has no effect and will be overwritten.
"""

import random
import re
import sys
from pathlib import Path

# Fixed seed keeps generation reproducible; changing it reshuffles the blind IDs and
# cross-version batches can no longer be compared directly.
SEED = 20260711

# Rubric-label allowlist: SF must be Expected, SNF must be Reason. Any other bold label
# is treated as format drift — better to fail than silently generate a wrong blind set.
RUBRIC_LABELS = {"SF": ("Expected",), "SNF": ("Reason",)}


def parse_cases(text):
    """Cut out each case: (id, scene, input quote block). Only quote lines are allowed before Expected/Reason."""
    parts = re.split(r"(?m)^### (?=(?:SF|SNF)-\d)", text)
    cases = []
    for chunk in parts[1:]:
        lines = chunk.splitlines()
        fields = [f.strip() for f in lines[0].split("|")]
        if len(fields) != 3:
            sys.exit(f"Title line is not the three-part 'id | scene | note': {lines[0]!r}")
        cid, scene, _title = fields
        kind = cid.split("-")[0]
        input_lines = []
        rubric_seen = False
        for ln in lines[1:]:
            if ln.startswith("**"):
                m = re.match(r"\*\*([^*]+)\*\*", ln)
                label = m.group(1) if m else None
                if label not in RUBRIC_LABELS[kind]:
                    sys.exit(f"{cid}: rubric label {label!r} not in the {kind} allowset {RUBRIC_LABELS[kind]}; benchmark format drift or a mis-written case")
                rubric_seen = True
                break
            if ln.startswith("### ") or ln.startswith("## "):
                break
            if ln.startswith(">") or not ln.strip():
                input_lines.append(ln)
            else:
                sys.exit(f"{cid}: a non-quote line appears before Expected/Reason; confirm the format before adjusting the script: {ln!r}")
        quote = "\n".join(input_lines).strip("\n")
        if not quote:
            sys.exit(f"{cid}: no input quote block parsed")
        if not rubric_seen:
            sys.exit(f"{cid}: no Expected/Reason field found")
        cases.append((cid, scene, quote))
    ids = [c[0] for c in cases]
    if len(ids) != len(set(ids)):
        sys.exit("duplicate case IDs")
    return cases


def main():
    root = Path(__file__).resolve().parents[2]
    src = root / "evals" / "benchmark.md"
    cases = parse_cases(src.read_text(encoding="utf-8"))

    sf = sum(1 for c in cases if c[0].startswith("SF-"))
    snf = len(cases) - sf

    order = list(range(len(cases)))
    random.Random(SEED).shuffle(order)

    # The blind file header stays minimal: it does not mention the source, seed, map, or
    # benchmark.md — isolation currently relies on prompt discipline alone, so we give the
    # model under test no hint that "the answer file is right next door".
    width = max(2, len(str(len(cases))))
    blind = [
        "# Blind Benchmark Input",
        "",
        f"> {len(cases)} cases. Process each case's quote block by the klartext rules: change what should change, and for what the rules say should not change, keep the original and explain why.",
        "> Output contract in `automation/eval/rewrite-prompt.md`.",
        "",
    ]
    maprows = [
        "# Blind Map",
        "",
        f"> Generated from `benchmark.md` by `automation/eval/make_blind.py` (seed {SEED}); this file and `benchmark-blind.md` are both generated — hand edits have no effect and re-running the script overwrites them.",
        "> Before scoring, the judge maps the blind IDs back to `benchmark.md` case IDs with this table.",
        "> ⚠️ The model under test must not read this file.",
        f"> {len(cases)} cases = {sf} SF + {snf} SNF.",
        "",
        "| Blind ID | Case ID | Scene |",
        "|----------|---------|-------|",
    ]
    for i, idx in enumerate(order, 1):
        cid, scene, quote = cases[idx]
        bid = f"B-{i:0{width}d}"
        blind += [f"### {bid} | {scene}", "", quote, ""]
        maprows.append(f"| {bid} | {cid} | {scene} |")

    (root / "evals" / "benchmark-blind.md").write_text("\n".join(blind).rstrip() + "\n", encoding="utf-8")
    (root / "evals" / "benchmark-map.md").write_text("\n".join(maprows) + "\n", encoding="utf-8")
    print(f"Done: {len(cases)} cases ({sf} SF + {snf} SNF) → evals/benchmark-blind.md, evals/benchmark-map.md")


if __name__ == "__main__":
    main()
