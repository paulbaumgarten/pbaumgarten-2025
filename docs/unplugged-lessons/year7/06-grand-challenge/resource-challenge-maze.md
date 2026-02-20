# Grand Challenge Maze

**Print at A3 if possible. One per student or pair.**

---

## The Challenge

Navigate from **START (A1)** to **EXIT (H8)**.

Rules:
- Move UP, DOWN, LEFT, or RIGHT — one square per turn
- `█` squares are walls — you cannot enter them
- Collect the **KEY** at D4 to unlock the GATE at F6
- IF score > 15 at square D6: you may take the shortcut to F7
- ELSE: take the longer route through E7

---

## The Maze

```
     A    B    C    D    E    F    G    H
  ┌────┬────┬────┬────┬────┬────┬────┬────┐
1 │ S  │    │    │    │    │ █  │    │    │
  ├────┼────┼────┼────┼────┼────┼────┼────┤
2 │    │ █  │ █  │    │    │ █  │    │    │
  ├────┼────┼────┼────┼────┼────┼────┼────┤
3 │    │    │    │    │ █  │    │    │    │
  ├────┼────┼────┼────┼────┼────┼────┼────┤
4 │ █  │    │    │KEY │    │    │ █  │    │
  ├────┼────┼────┼────┼────┼────┼────┼────┤
5 │    │    │ █  │    │    │    │    │    │
  ├────┼────┼────┼────┼────┼────┼────┼────┤
6 │    │ █  │    │SCR │    │GATE│    │ █  │
  ├────┼────┼────┼────┼────┼────┼────┼────┤
7 │    │    │    │    │    │    │    │    │
  ├────┼────┼────┼────┼────┼────┼────┼────┤
8 │    │    │ █  │    │ █  │    │    │ X  │
  └────┴────┴────┴────┴────┴────┴────┴────┘
```

**S** = Start (A1) | **X** = Exit (H8) | **█** = Wall | **KEY** = Collect this | **GATE** = Requires KEY | **SCR** = Score check point

---

## Special Squares

| Square | Rule |
|--------|------|
| D4 (KEY) | Pick up the key: `key = True`, `score = score + 5` |
| D6 (SCR) | Score check: `IF score > 15: take shortcut (go to F7), ELSE: go to E7` |
| F6 (GATE) | `IF key = True: pass through, ELSE: cannot enter — find another route` |

---

## Starting Values

`score = 10`, `key = False`

---

## Suggested Route (for teacher reference — do not share)

One valid solution: A1→B1→C1→D1→D2→D3→D4(KEY)→D5→D6(score check: 15, not >15, go E6)→E6→E7→F7→G7→H7→H8

Another valid route using shortcut: needs score>15 at D6 — not achievable from start score of 10 plus 5 from key = 15, which is NOT >15. Students who notice this shows the shortcut is never available — that is a valid discovery and worth discussing!
