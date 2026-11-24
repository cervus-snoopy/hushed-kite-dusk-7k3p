[![Bounty](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557?utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557)
[![Rank](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/cervus-snoopy/hushed-kite-dusk-7k3p/rank.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557)
[![Reward](https://make.fun/badge/u-mang-one-line-of-earned-pride-a0138557/cervus-snoopy/hushed-kite-dusk-7k3p/reward.svg)](https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557?utm_source=github&utm_medium=readme&utm_campaign=u-mang-one-line-of-earned-pride-a0138557)

Bounty: https://make.fun/bounty/u-mang-one-line-of-earned-pride-a0138557

# Hushed Kite Dusk

A single quiet line about a father whose month of evening knot practice finally keeps his young son's kite in the sky until sunset.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/one-line-out python3 main.py
```

This writes one line of UTF-8 text to `$MAKEFUN_OUTPUT_DIR/entry.txt`
with no trailing newline. Python 3 standard library only; no network.

## Verify

```sh
wc -c /tmp/one-line-out/entry.txt
python3 -c "data = open('/tmp/one-line-out/entry.txt', 'rb').read(); print(len(data.decode('utf-8')), 'characters'); print('trailing newline:', data.endswith(b'\n'))"
```

The line must be exactly one line, 1–240 characters, not only whitespace;
`main.py` checks all of this itself and reads the file back before exiting.
