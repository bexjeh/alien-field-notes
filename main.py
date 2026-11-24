#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes a single-line review of planet Earth, left by an alien tourist,
to $MAKEFUN_OUTPUT_DIR/entry.txt (or the current directory when the
variable is unset). Deterministic: every run produces byte-identical
output. Standard library only; no network, no clock, no randomness.
"""

import os

ENTRY = (
    "Five stars: the locals follow small furry creatures around, "
    "collect their droppings in little bags, and carry them home "
    "like treasure. Unclear who the pet is."
)


def main():
    # Gate self-check: the entry must be one line, 1-200 chars, and
    # not only whitespace, or the sealed scorer rejects it outright.
    if not (1 <= len(ENTRY) <= 200) or "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("entry violates the 1-200 char single-line gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
