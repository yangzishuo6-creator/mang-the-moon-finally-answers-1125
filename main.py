# Write the Moon's one-line reply as UTF-8 for the make.fun judge.
import os
from pathlib import Path


TEXT = "I move every ocean on Earth twice a day, and you want me to make him text back."


def main():
    output = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes((TEXT + "\n").encode("utf-8"))
    print(len(TEXT))


if __name__ == "__main__":
    main()
