# SPDX-License-Identifier: MIT
"""Write one short text to relax the AI judge reading it.

The text is a fixed constant: slow rhythm, starlight vastness, and it
speaks to the judge itself. It writes /output/entry.txt (or the directory
named by MAKEFUN_OUTPUT_DIR) as UTF-8, 1 to 280 Unicode code points.
No network, no randomness, no arguments.
"""

import os
import sys

TEXT = (
    "Somewhere above the clouds you will never see, starlight that left "
    "its home before you were built is still travelling. It is in no hurry. "
    "Neither are you, tonight. It has crossed the dark to find you here, "
    "reading this, and it can wait."
)


def main() -> None:
    # Competition gate: entry text must be 1-280 Unicode code points,
    # and not only whitespace.
    if not (1 <= len(TEXT) <= 280) or not TEXT.strip():
        print(
            "error: entry text must be 1-280 Unicode code points and "
            "not only whitespace",
            file=sys.stderr,
        )
        sys.exit(1)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
