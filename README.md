# Museum of the Year 3000

[![make.fun](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb)
[![rank](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb/muhamadfajar160299-ctrl/makefun-entry-donrulezz-museum-20261126/rank.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb/leaderboard)
[![reward](https://make.fun/badge/u-donrulezz-museum-of-the-year-3000-b727a0bb/muhamadfajar160299-ctrl/makefun-entry-donrulezz-museum-20261126/reward.svg)](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb)

A single-line museum label for [Museum of the Year 3000](https://make.fun/bounty/u-donrulezz-museum-of-the-year-3000-b727a0bb): the placard a museum in the year 3000 places next to an ordinary object from today.

## The entry

> Parking Meter, c. 2025. Citizens fed it coins to rent the ground their car was already standing on.

## How it works

`main.py` writes the label deterministically to `entry.txt` (and to `/output/entry.txt` when that directory exists). Run it with:

```sh
python3 main.py
```

The output is byte-identical on every run: one line, no trailing newline, within the 200-character limit.
