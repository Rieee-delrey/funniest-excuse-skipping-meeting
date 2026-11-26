#!/usr/bin/env python3
"""The Funniest Excuse for Skipping a Meeting entry.

Writes one funny excuse for skipping a pointless meeting to /output/entry.txt.
Deterministic, no network, no secrets, reads nothing outside the repo.
"""

import os

LINE = "I already know how it ends: someone says 'let's take this offline' and we never do. I'm taking it offline now."

OUTPUT_PATH = "/output/entry.txt"


def check_single_line(line: str) -> None:
    """Own validation: the excuse must be exactly one line.

    No newline characters anywhere, so the file the judge reads is one
    tight line, and no trailing whitespace, so no byte is wasted on
    padding the joke.
    """
    if "\n" in line or "\r" in line:
        raise ValueError("line must contain no newline characters")
    if line != line.strip():
        raise ValueError("line must have no leading or trailing whitespace")


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line must be 1-200 characters, got {len(LINE)}")
    check_single_line(LINE)
    data = LINE.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != data:
        raise ValueError("bytes on disk do not match the line")


if __name__ == "__main__":
    main()
