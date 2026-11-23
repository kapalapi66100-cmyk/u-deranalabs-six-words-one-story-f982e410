"""Six Words, One Story — make.fun entry.

Writes one complete story in exactly six words to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).

The story text is fixed: "She buried him. Then answered him."
(6 words, 34 characters, no trailing newline, no BOM.)
Stdlib only (os, sys). Deterministic: repeated runs produce
byte-identical output. Writes nothing into the repo.
"""

import os
import sys

TEXT = "She buried him. Then answered him."


def main():
    words = TEXT.split()
    if len(words) != 6:
        sys.exit("entry must be exactly 6 words, got %d" % len(words))
    if not 1 <= len(TEXT) <= 60:
        sys.exit("entry must be 1-60 characters, got %d" % len(TEXT))

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "wb") as f:
        f.write(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
