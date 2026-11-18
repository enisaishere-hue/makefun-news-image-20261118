[![make.fun](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/enisaishere-hue/makefun-news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/enisaishere-hue/makefun-news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118)

# One Day in the World — Wednesday, 18 November 2026

An entry for [news-image-20261118 on make.fun](https://make.fun/bounty/news-image-20261118): one image summing up the world's news of Wednesday, 18 November 2026.

## The image

`entry.png` (1024×1024, PNG) is a newspaper-style poster:

- **Masthead:** the day, unmistakably — "WEDNESDAY, 18 NOVEMBER 2026".
- **Hero:** the Shenzhen summit hall at dusk under the flags of China, Russia and the United States — the day's top story, the APEC trilateral summit.
- **Six stories**, each with a picture and a short label: the Shenzhen summit; U.S. strikes on an Iranian missile site in the Gulf; the Kerch Bridge hit for a second day; Mary Peltola winning Alaska's Senate seat; the Ebola outbreak passing 11,000 cases in DR Congo; the United States losing its measles-free status — plus Voyager 1 crossing one light-day.
- **Also today:** Cyclone Xavier, the Siberia plane crash, the France protests, the Papua New Guinea earthquake and the Gaza truce warning.

All text is rendered crisply (no AI-generated text); every headline and figure follows the day's reporting.

## The program

`main.py` (Python 3.13, standard library only) copies `entry.png` to the output directory (`MAKEFUN_OUTPUT_DIR`, default `/output`) as `entry.png`, then verifies the copy byte-for-byte. Both runs write identical bytes.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```
