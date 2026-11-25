"""The Dog Ate My Homework - one line, written to /output/entry.txt.

the joke inverts the classic excuse: the agent defends the dog instead of the homework, and charges for it.
"""

from pathlib import Path

ENTRY = (
    "The dog didn't eat my homework - my agent spent 40,000 tokens proving the dog has an airtight alibi, then billed me for the case."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")
    print(out.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
