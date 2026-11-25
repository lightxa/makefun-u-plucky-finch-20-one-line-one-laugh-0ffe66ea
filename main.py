"""One Line, One Laugh entry.

Writes a single original funny line of text to /output/entry.txt.
Pure standard library, deterministic, no network access at runtime.
"""

from pathlib import Path

# The entry: one self-contained funny line. A mundane autocorrect slip
# turns a loving message into a debt, and the mother treats it like one.
# Original wording, written for this competition.
LINE = "My phone autocorrected 'I love you' to 'I owe you,' and now my mother wants a payment plan."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    """Write the entry line to /output/entry.txt as exact UTF-8 text."""
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(
            f"entry line must be 1-200 characters, got {len(text)}"
        )
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
