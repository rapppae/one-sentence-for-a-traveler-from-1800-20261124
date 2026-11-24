"""Write the time-traveler sentence to /output/entry.txt.

One sentence, 199 characters (limit 200) -- no trailing newline.
Every word in it was already in use in 1800: no modern coinages.
"""

from pathlib import Path

ENTRY = "Imagine a web of thin wires strung across the whole earth, so that a letter written in London can be read in Boston before the ink is dry, and any man may ask it a question and get an answer at once."

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
