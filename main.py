#!/usr/bin/env python3
"""One Line, Big Laugh - make.fun entry.

Writes a single funny line (at most 200 characters) to /output/entry.txt.
Deterministic: the same bytes on every run. No network, no randomness,
no input read from anywhere - the line is baked into this file.
"""
import os

LINE = "My bank called about a suspicious charge: it was me, buying a $400 candle called 'Financial Stability'."

# Why this line: a bank fraud call is a familiar setup, then the twist lands
# on the punchline - the "suspicious charge" is the narrator buying a $400
# candle ironically named "Financial Stability". One specific absurd detail,
# no wasted words, and it reads as a complete joke on its own.

OUTPUT_DIR = "/output"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Leave the file readable by every user (the grader collects it as
    # another user). Never chmod the output directory itself.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
