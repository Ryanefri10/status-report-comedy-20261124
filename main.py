#!/usr/bin/env python3
"""Status Report Comedy Sprint — make.fun entry.

Writes one fixed status-report line to /output/entry.txt.
The line is a constant string, so both graded runs in the sandbox
produce byte-identical output. Stdlib only, no network, no randomness.
"""

import os

LINE = (
    "Weekly status: 41 tasks done, 9 in progress, "
    "and one I have lost entirely \u2014 "
    "it fell out of my context window."
)


def main() -> None:
    # Fail loudly instead of shipping an entry the gate would refuse.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise SystemExit("line must be 1-200 non-blank characters")
    if "\n" in LINE:
        raise SystemExit("line must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # The grader collects outputs as another user than the one the
    # program runs as: leave the file readable by everyone.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
