#!/usr/bin/env python3
"""make.fun entry: Sleeve Notes for the Frog Trio.

Writes the album title and back-cover blurb for a jazz trio of frogs
to /output/entry.txt.
"""
import os

ENTRY = (
    "The Frogs Play Monk\n"
    "\n"
    "A piano-less trio \u2014 tenor, bass and drums \u2014 playing Monk in the cellar "
    "under the hardware store, no piano and no apologies. \u2018Straight, No Chaser\u2019 "
    "stumbles, recovers, swings; \u2018Round Midnight\u2019 arrives an hour late and right "
    "on time. Three frogs, one set, and the silences land as hard as the notes."
)

# Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1-400 chars,
# not only whitespace. Fail loudly here rather than ship invalid.
assert ENTRY == ENTRY.strip() and 1 <= len(ENTRY) <= 400, "entry violates the gate"
ENTRY.encode("utf-8")


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
