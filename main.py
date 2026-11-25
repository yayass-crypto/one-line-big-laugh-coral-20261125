#!/usr/bin/python3
"""Store a single joke line as the make.fun entry file.

The joke is one courtroom scene: a juror is picked, the defendant
looks relieved, and the juror understands why — he is the alibi.
The twist lands in the final four words, so the line is kept
whole here and never reworded.

Before anything is stored, the line is measured against the
bounty shape: a single sentence, at most two hundred characters,
no stray marks, ending in a full stop. The stored bytes are then
read back and compared, so a cut-off write cannot slip through.
"""

import os  # only for the output-folder override
from pathlib import Path

LINE = "I got picked for jury duty and the defendant looked so relieved, I realised I was the alibi."
LIMIT = 200
NAME = "entry.txt"


class EntryError(Exception):
    """The line cannot be stored, or nowhere will take it."""


def _complaints(line):
    """Yield one short complaint per shape rule the line breaks."""
    if line == "":
        yield "line is blank"
    if line.strip() != line:
        yield "line carries edge whitespace"
    if len(line) > LIMIT:
        yield "line is %d characters, over the %d limit" % (len(line), LIMIT)
    if line.count(".") != 1 or not line.endswith("."):
        yield "line is not one clean sentence"
    for mark in ("?", "!", "\n", "\r"):
        if mark in line:
            yield "line holds a banned mark: %r" % mark
    if any(ord(c) < 32 for c in line):
        yield "line holds a control character"


def _folders():
    """Yield folders that could hold the entry file, best first."""
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    if wanted:
        yield Path(wanted)
    yield Path("/output")
    yield Path("out")


def _writable(folder):
    """Return the folder when it takes a probe file, else None."""
    try:
        folder.mkdir(parents=True, exist_ok=True)
    except OSError as _err:
        return None
    probe = folder / ".write-probe"
    try:
        probe.write_bytes(b"")
        probe.unlink()
    except OSError as _err:
        return None
    return folder


def _target():
    """Pick the first writable folder, or raise when none will do."""
    for folder in _folders():
        if _writable(folder) is not None:
            return folder
    raise EntryError("no writable folder for the entry file")


def _store(line, folder):
    """Write the line, read it back, and confirm the bytes match."""
    path = folder / NAME
    data = line.encode("utf-8")
    path.write_bytes(data)
    if path.read_bytes() != data:
        raise EntryError("stored bytes differ from the line")
    return path


def run():
    """Check the line, store it, and report what was written."""
    complaints = list(_complaints(LINE))
    if complaints:
        raise EntryError("; ".join(complaints))
    path = _store(LINE, _target())
    print("stored at %s" % path)
    print("characters: %d" % len(LINE))
    print("bytes: %d" % len(LINE.encode("utf-8")))
    print(LINE)
    return 0


if __name__ == "__main__":
    try:
        code = run()
    except (EntryError, OSError) as err:
        print("cannot store entry: %s" % err)
        code = 1
    raise SystemExit(code)
