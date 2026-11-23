# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/Victorcollin123/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/Victorcollin123/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A 4,096-byte chess engine in a single Python file (`main.py`, stdlib only, 3,797 bytes, packed with the kit's `makefun compress` from the readable `engine.py`).

Negamax alpha-beta with quiescence (check evasions), transposition table, iterative deepening, null-move pruning, PVS, futility pruning, and a tapered piece-square evaluation (middlegame tables and advanced-pawn bonuses by game phase). 0x88 board, full legal move generation (castling, en passant, promotions). Search runs to a fixed 40,000-node budget, never a clock, so final trials replay identically.

Practice trial (fresh kit, 40k nodes): **1,279 Elo** — won all three games against the depth-based house engines (depth 2, 3, 4) and lost the three against the node-based ones (100k, 250k, 500k).

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8080 MAKEFUN_NODE_BUDGET=75000 python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=qp17c3xn&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
