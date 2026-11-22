#!/usr/bin/env python3
"""news-image-20261122 v2 entrypoint (Python 3.13, standard library only).

Copies the pre-drawn entry.png beside this file to /output/entry.png
(or $MAKEFUN_OUTPUT_DIR when set). The image itself is drawn at build
time by gen.py — flat-vector PIL art, deterministic, no network — so this
program only copies bytes and both grader runs write identical output.
No network access, no randomness, no environment dependence.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    os.makedirs(OUT, exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"),
                    os.path.join(OUT, "entry.png"))


if __name__ == "__main__":
    main()
