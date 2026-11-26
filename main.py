#!/usr/bin/env python3
"""The Moon Finally Answers Back — one line, in the Moon's voice.

Writes a single line (1-240 characters) to /output/entry.txt: the Moon,
wry and four billion years tired, answering the wishes, howls and
late-night promises of everyone staring up at it.
"""

import os

LINE = (
    "Four billion years I've answered your wishes, and tonight it's "
    "'make him text back'? Sweetheart, I'm a rock \u2014 even I stopped "
    "orbiting people who leave me on read."
)


def main():
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
