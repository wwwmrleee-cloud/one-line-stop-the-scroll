#!/usr/bin/env python3
"""One Line to Stop the Scroll.

Writes a single line of text to /output/entry.txt: one concrete moment,
a small twist in the last third, and a question left hanging.
"""
import os

LINE = (
    "My toddler just handed me a rock, looked me dead in the eye, "
    "and said: 'This one is for you. It is a treasure.'"
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
