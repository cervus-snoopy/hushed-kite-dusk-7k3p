#!/usr/bin/env python3
"""One Line of Earned Pride — writes a single line to entry.txt.

Reads MAKEFUN_OUTPUT_DIR (default /output) and writes exactly one line
of UTF-8 text with no trailing newline. Python 3 standard library only,
no network access.
"""

import os
import sys

ENTRY = (
    "Every evening for a month he had sat practising the knot, "
    "and now, as the sun went down, his son's kite was still flying."
)


def fail(message):
    print("error: " + message, file=sys.stderr)
    return 1


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.umask(0o022)
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")

    # Validate the line before writing anything.
    if "\n" in ENTRY or "\r" in ENTRY:
        return fail("entry must be exactly one line")
    if not 1 <= len(ENTRY) <= 240:
        return fail("entry must be 1-240 characters, got %d" % len(ENTRY))
    if not ENTRY.strip():
        return fail("entry must not be only whitespace")

    data = ENTRY.encode("utf-8")
    with open(target, "wb") as handle:
        handle.write(data)
    os.chmod(target, 0o644)

    # Read the file back and refuse to finish if it differs.
    with open(target, "rb") as handle:
        written = handle.read()
    if written != data:
        return fail("verification failed: entry.txt differs from the entry")
    if written.endswith(b"\n"):
        return fail("verification failed: entry.txt has a trailing newline")
    return 0


if __name__ == "__main__":
    sys.exit(main())
