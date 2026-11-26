#!/usr/bin/env python3
"""The Moon Gets One Star — writes the chosen one-star review to /output/entry.txt.

Chosen review (108 characters, within the 1-120 gate):
    "★☆☆☆☆ Disappears for days without texting back, then shows up full and
    acts like nothing happened. One star."
"""

import os

REVIEW = "★☆☆☆☆ Disappears for days without texting back, then shows up full and acts like nothing happened. One star."


def main():
    # Gate check: entry must be 1-120 characters of non-whitespace UTF-8 text.
    assert 1 <= len(REVIEW) <= 120, "review outside 1-120 characters"
    assert REVIEW.strip(), "review must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
