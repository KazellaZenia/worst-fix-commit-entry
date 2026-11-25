#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message (make.fun).

Writes a single commit message, at most 100 characters, for a bug fix
that made everything worse, to $MAKEFUN_OUTPUT_DIR/entry.txt.

The line, 69 characters:
  fix: stop users deleting their accounts; now they can delete anyone's

Why this line: it reads as a real commit subject (imperative "fix: ...",
plain, the kind a tired engineer types at the end of a bad day); it names
one specific fix (stop users deleting their own accounts) and one specific,
worse breakage (they can now delete anyone's) -- the repair inverted the
very permission it was meant to restrict, so it broke strictly more than
it mended. The angle is fresh: no revert, no testing in production, no
generic "broke everything" -- the joke lands on its own, in one breath.
"""

import os

LINE = "fix: stop users deleting their accounts; now they can delete anyone's"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

# Reviser note: the repair inverts the very permission it was meant to restrict.
