"""Entry point for the Houseplant Out-of-Office bounty.

Writes one out-of-office auto-reply, as if a houseplant had written it,
to /output/entry.txt. The line is at most 120 characters, deterministic,
and needs no network access.
"""
from pathlib import Path

LINE = (
    "Out of office: I'm a fern. Ignored since March, thriving on "
    "neglect. Back when someone remembers the watering can."
)

TARGET = Path("/output/entry.txt")


def main():
    text = LINE.strip()
    assert 1 <= len(text) <= 120, f"line is {len(text)} characters"
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(text + "\n", encoding="utf-8")
    print(f"wrote {len(text)} characters to {TARGET}")


if __name__ == "__main__":
    main()
