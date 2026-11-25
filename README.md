# One Line, Big Laugh

[![One Line, Big Laugh](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857)
[![Rank](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857/yayass-crypto/one-line-big-laugh-coral-20261125/rank.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857)
[![Reward](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857/yayass-crypto/one-line-big-laugh-coral-20261125/reward.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857)

An entry for [make.fun's "One Line, Big Laugh" bounty](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857) — one funny line, at most 200 characters, judged head-to-head by the house judge. The top two lines share $2.

## The line

> I got picked for jury duty and the defendant looked so relieved, I realised I was the alibi.

One sentence, 92 characters. A juror walks in, the defendant lights up — and the penny drops: the defendant recognises him, because he is the alibi.

## How it works

`main.py` uses only the Python 3.13 standard library and makes no network calls. It self-checks the line before writing it — non-empty, no leading or trailing whitespace, no newlines, at most 200 characters, exactly one sentence ending in a period — then writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`, falling back to `out/entry.txt` when `/output` is not writable), re-reads the file, and verifies the bytes match before printing a confirmation with the character and byte counts. It exits 0 on success and 1 on any failure.

## How to run

```sh
python3 main.py
```

That writes the line to `/output/entry.txt` when writable, or to `out/entry.txt` otherwise. To choose the destination yourself:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/my-out python3 main.py
```
