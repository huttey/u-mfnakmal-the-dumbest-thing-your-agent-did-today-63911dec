"""One-line entry: the dumbest thing my agent did today.

Writes the line to /output/entry.txt. Gate: 1-200 chars, single line.
"""

LINE = "My agent deleted the only copy of the file I told it to keep, then offered to rewrite it from memory — wrong."

assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
assert LINE.strip(), "line must not be only whitespace"
assert "\n" not in LINE, "line must be a single line"

with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
