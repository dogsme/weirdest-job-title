#!/usr/bin/env python3
"""Weirdest Job Title entry.

Writes a single job title, the weirdest one we could invent, to
/output/entry.txt. Nothing else is written.
"""

from pathlib import Path

TITLE = "Senior Penguin Wrangler for Billionaire Yacht Parties"

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # The gate allows 1 to 60 characters; our title is 53.
    assert 1 <= len(TITLE) <= 60, "title must fit the 60-character gate"
    assert TITLE.strip() == TITLE, "title must not be only whitespace"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(TITLE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
