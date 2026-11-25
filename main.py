# The Absurd Clause Contest — make.fun entry
# Writes the entry's single clause to /output/entry.txt.
# Deterministic: the same bytes on every run. No network, no secrets,
# no environment reads, no randomness, no dependency on process.cwd().
from pathlib import Path

LINE = (
    "12.4 By using this service you agree that, in the event of a dispute, "
    "both parties shall settle the matter by competitive duck herding, "
    "winner takes the Terms, loser keeps the ducks."
)

# The gate allows 1 to 200 characters: refuse to emit a line that would fail it.
if not 1 <= len(LINE) <= 200:
    raise SystemExit(f"entry line is {len(LINE)} characters, must be 1-200")

OUT_FILE = Path("/output/entry.txt")
OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
OUT_FILE.write_text(LINE, encoding="utf-8")
print(f"wrote {len(LINE)} characters to {OUT_FILE}")
