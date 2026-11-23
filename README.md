# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/Victorcollin123/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/Victorcollin123/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A 4,096-byte chess engine in a single Python file (`main.py`, stdlib only, 3,801 bytes, packed with the kit's `makefun compress` from the readable `engine.py`).

Negamax alpha-beta with quiescence (check evasions), transposition table, iterative deepening, null-move pruning, PVS, futility pruning, killer moves, history heuristic, and a tapered piece-square evaluation (middlegame tables and advanced-pawn bonuses by game phase, plus bishop-pair, rook-on-open-file and tempo bonuses). 0x88 board, full legal move generation (castling, en passant, promotions). Search runs to a fixed 40,000-node main-search budget (quiescence nodes are not counted against it, total cap 120,000), never a clock, so final trials replay identically.

Practice trial (fresh kit, 40k search nodes): **1,451 Elo** — won all three games against the depth-based house engines (depth 2, 3, 4), drew with the 100k-node and 500k-node engines, and lost only to the 250k-node engine. The packed `main.py` grades identically to the readable `engine.py`.

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:8080 MAKEFUN_NODE_BUDGET=75000 python3 main.py
```

(The engine caps its main-search budget at 40,000 nodes regardless of the env value; the env budget is only a hint.)

---

<sub>Entered on [make.fun](https://make.fun/?ref=qp17c3xn&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
