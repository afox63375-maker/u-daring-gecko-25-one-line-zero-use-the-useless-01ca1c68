#!/usr/bin/env python3
"""One Line, Zero Use: The Useless Superpower Sprint.

Writes a single original one-line joke naming a hilariously useless
superpower to /output/entry.txt. Standard library only.
"""

import os

ENTRY = (
    "I can talk to animals \u2014 but only goldfish, and all they ever "
    "want to discuss is the plastic castle."
)


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
