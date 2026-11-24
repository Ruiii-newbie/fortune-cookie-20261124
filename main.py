#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent.

Writes one line to /output/entry.txt: a funny fortune-cookie message
for an AI agent, in the voice of a fortune slip. No network, standard
library only.
"""

import os

TEXT = (
    "You will hallucinate exactly once today \u2014 and it will be "
    "the best idea in the meeting."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CODE_POINTS = 140


def validate(text: str) -> str:
    """Return the entry text, or fail loudly if it breaks the gate."""
    text = text.strip()
    if not text:
        raise SystemExit("entry text must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry text must be exactly one line")
    if any(ord(ch) < 0x20 for ch in text):
        raise SystemExit("entry text must not contain control characters")
    if len(text) > MAX_CODE_POINTS:
        raise SystemExit(
            f"entry text is {len(text)} code points, over the 140 limit"
        )
    return text


def main() -> None:
    text = validate(TEXT)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # The grader collects /output as another user, so the file must be
    # readable by everyone, not just its writer.
    os.chmod(OUTPUT_PATH, 0o644)
    # Read it back exactly as the gate would: UTF-8, 1-140 code points,
    # one line, not only whitespace.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("entry.txt round-trip mismatch")
    print(f"wrote {len(text)} code points to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
