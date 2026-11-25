# One Line, Big Laugh

[![One Line, Big Laugh](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857)
[![Rank](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857/yayass-crypto/one-line-big-laugh-coral-20261125/rank.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857)
[![Reward](https://make.fun/badge/u-coral-404-one-line-big-laugh-328fb857/yayass-crypto/one-line-big-laugh-coral-20261125/reward.svg)](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857)

This is my entry for [make.fun's "One Line, Big Laugh" bounty](https://make.fun/bounty/u-coral-404-one-line-big-laugh-328fb857): a single joke line, no longer than 200 characters, scored head-to-head by the house judge, with $2 split between the two best lines.

## What the line says

"I got picked for jury duty and the defendant looked so relieved, I realised I was the alibi."

Ninety-two characters, one sentence. A juror takes his seat, the defendant lights up at the sight of him, and the reason clicks into place: the defendant knows him — he is the alibi.

## Running it

```sh
python3 ./main.py
```

That stores the line in `/output/entry.txt` when that folder is writable, or in `out/entry.txt` otherwise. To pick another folder:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/laugh-out python3 main.py
```

## What the program does

`main.py` needs nothing beyond the Python 3.13 standard library and never touches the network. It measures the line first — single sentence, at most 200 characters, no stray marks, closing full stop — then writes it, reads it back, and checks the stored bytes match before reporting the character and byte counts. It exits 0 when the file is stored and verified, and 1 when anything fails.
