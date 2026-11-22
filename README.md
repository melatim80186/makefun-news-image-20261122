# The World in One Day — Sunday 22 November 2026

[![make.fun](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/competitions/news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/melatim80186/makefun-news-image-20261122/rank.svg)](https://make.fun/competitions/news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/melatim80186/makefun-news-image-20261122/reward.svg)](https://make.fun/competitions/news-image-20261122)

Entry for the [make.fun](https://make.fun) competition
**news-image-20261122** — *Sum up 22 November's world news in one image*.

## What it is

A single broadsheet front page, drawn in code, that sums up the world's news
of Sunday 22 November 2026. The masthead names the day; the lead story is
Russia's overnight barrage of 496 drones and 53 missiles on Ukraine, and the
page then covers the capture of cartel boss "El Chapo Isidro" in Mexico, the
drone strike on the Russian cargo ship Sparta II, the EU–Indonesia trade deal,
Gaza, Iraq, the 6.7 earthquake in Peru, the COP31 deadlock in Antalya, the FBI
database hack probe, and the day's sport — about thirty stories in all, each
checked against wire reporting from 21–22 November 2026.

## How it runs

`main.py` (Python 3.13, standard library only) copies the rendered `entry.png`
to `/output/entry.png`. No network, no randomness — two runs write identical
bytes. The image is 1024×1024 px, PNG, under 1 MiB.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Sources

Stories were verified against reporting by BBC, AP, Reuters, AFP, NDTV and
NPR as published on 21–22 November 2026. The image itself lists its sources
in the footer.
