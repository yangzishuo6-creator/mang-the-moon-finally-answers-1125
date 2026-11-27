# Write the Moon's reply for the make.fun contest.
import os
from pathlib import Path


TEXT = "Wish, howl, swear you'll change. Four billion years of phases, and I'm only full of it once a month."


def main():
    output = Path(os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt"))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes((TEXT + "\n").encode("utf-8"))
    print(len(TEXT))


if __name__ == "__main__":
    main()
