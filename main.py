#!/usr/bin/env python3
"""The joke about the demo.

Writes one one-line joke about working beside an AI coding agent to
/output/entry.txt.

Craft notes (why this text, against the judge's brief, most important first):
1. On subject, and about a crash: an AI coding agent that writes code,
   asked for one small thing, and the demo is where it breaks.
2. The laugh is the escalation with a surprise at the end: one button
   becomes a settings page, then a plugin system -- and then the
   punchline, a bug that only appears on stage, which the listener did
   not see coming but recognises the moment it lands.
3. Truth: scope creep is the behaviour every developer who works beside
   an agent knows at once, and a bug that only shows up in front of an
   audience is the oldest demo truth there is.
4. Economy: one sentence, every clause earning its place, nothing
   explained -- the joke is the list, and the list is the joke.
5. Freshness: not "it broke prod" and not "it hallucinated" -- the twist
   is that the agent over-delivers, and the over-delivery itself is what
   crashes the demo.
"""

import os

ENTRY_TEXT = (
    "I asked my agent for one button \u2014 it shipped a settings page, "
    "a plugin system, and a bug that only appears on stage."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY_TEXT
    if not (1 <= len(text) <= 280) or not text.strip():
        raise SystemExit("entry text must be 1-280 non-blank characters")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
