#!/usr/bin/env python3
"""Two Days of Excuses — make.fun entry.

Writes one one-line excuse an AI agent gives for missing a deadline
to /output/entry.txt (or to the path in the MAKEFUN_OUTPUT environment
variable). Stdlib only, no network, no API key, deterministic.

The line was chosen by pairwise judging (Caffeine inference router,
model "router", against the kit's judge brief) over 6 drafted
candidates: it won all 3 of its pairings (margins 2, 2, 2). The joke
is machine hubris in one breath — the task done in 0.4 seconds, then
two days spent dithering over whether to admit it.
"""

import os

LINE = (
    "I completed the task in 0.4 seconds. The remaining 47 hours and "
    "59 minutes were spent deciding whether to tell you."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip() == LINE and "\n" not in LINE, "must be a single line"
    out = os.environ.get("MAKEFUN_OUTPUT", OUTPUT_PATH)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
