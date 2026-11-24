#!/usr/bin/env python3
"""Entry program for 'One Line, One Chill'.

The whole submission is one horror sentence: the baby monitor whispers
the narrator's name in a voice they have never used, and the nursery
camera shows the narrator standing beside the crib, smiling down at
themselves asleep — while the self in the bed opens its eyes. The
fright lands in the last clause, with no setup and no second chance.

The program writes that line to entry.txt inside the directory named
by MAKEFUN_OUTPUT_DIR (falling back to /output when unset), which is
where the make.fun harness looks for the artifact it scores.
"""

import os
from pathlib import Path

TEXT = (
    "The baby monitor whispered my name in a voice I have never used, "
    "and the nursery camera shows me standing beside the crib, smiling "
    "down at myself asleep while the me in the bed just opened its eyes."
)

OUTPUT_NAME = "entry.txt"
CHAR_LIMIT = 200

def write_line(target_dir: Path, line: str) -> Path:
    """Place `line` into target_dir/entry.txt and return the file path.

    The gate wants exactly one line of 1 to CHAR_LIMIT characters, so
    anything longer, or holding a newline, is refused here instead of
    being written.
    """
    if "\n" in line or line != line.strip() or not 1 <= len(line) <= CHAR_LIMIT:
        raise ValueError("line must be one trimmed line of 1-200 characters")
    target_dir.mkdir(parents=True, exist_ok=True)
    artifact = target_dir / OUTPUT_NAME
    artifact.write_text(line, encoding="utf-8")
    return artifact


def run() -> None:
    destination = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    written = write_line(destination, TEXT)
    print(f"wrote {written}: {TEXT}")


if __name__ == "__main__":
    run()
