#!/usr/bin/env python3
"""Copy this repository's entry.png to the output directory as entry.png.

The grader runs the program twice; both runs write identical bytes because
this is a plain byte-for-byte copy of the same source file. Outside the
grader, MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"
OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
DESTINATION = OUTPUT_DIR / "entry.png"


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DESTINATION)
    # Verify the copy: the grader runs the program twice and both runs must
    # write identical bytes, so fail loudly here rather than shipping a
    # partial or mismatched file.
    if DESTINATION.read_bytes() != SOURCE.read_bytes():
        raise SystemExit("entry.png copy does not match the source")
    print(f"wrote {DESTINATION} ({DESTINATION.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
