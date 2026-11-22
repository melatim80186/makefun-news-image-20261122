#!/usr/bin/env python3
"""Entry program for make.fun competition news-image-20261122.

Writes the pre-rendered front page for Sunday 22 November 2026 to
/output/entry.png. Standard library only, no network, deterministic:
the same bytes are written on every run.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT / "entry.png")
