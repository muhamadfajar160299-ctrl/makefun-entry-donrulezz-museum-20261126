#!/usr/bin/env python3
"""Museum of the Year 3000 — writes the museum label to entry.txt.

The label is a deadpan museum placard from the year 3000, placed beside
an ordinary object from today. One line, at most 200 characters.
"""

import os

LINE = "Parking Meter, c. 2025. Citizens fed it coins to rent the ground their car was already standing on."


def main():
    text = LINE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1 to 200 characters"
    # Written with no trailing newline so the file is byte-identical to
    # the label itself: the gate counts the file's characters as-is.
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    if os.path.isdir("/output"):
        with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
            f.write(text)


if __name__ == "__main__":
    main()
