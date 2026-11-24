#!/usr/bin/env python3
"""The One-Line Exit — writes one funny resignation line to /output/entry.txt."""

import os

ENTRY = "I hereby resign as a wedding singer \u2014 after forty divorces, I finally took the hint from 'I Will Survive.'"
MAX_CHARS = 140


def validate(text: str) -> str:
    """One line, non-empty, within the 140-char gate."""
    line = text.strip()
    if not line:
        raise ValueError("entry must not be empty")
    if "\n" in line:
        raise ValueError("entry must be exactly one line")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} cap")
    return line


def write_entry(text: str, path: str = "/output/entry.txt") -> str:
    line = validate(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    return line


def main() -> None:
    line = write_entry(ENTRY)
    print(f"Wrote {len(line)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()
