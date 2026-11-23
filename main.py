#!/usr/bin/env python3
"""One Word, First Thought — writes exactly one word to /output/entry.txt.

The word is the first that came to mind: petrichor — the scent of rain
on dry earth. Surprising, vivid, and specific.
"""

import os

WORD = "petrichor"

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
