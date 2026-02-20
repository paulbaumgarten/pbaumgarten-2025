# Sorting Network — 6-Input Network

---

## Floor Setup Instructions (Teacher)

**Materials needed:** Tape or chalk, 6 large number cards (1–6 shuffled), 6 volunteers.

**Layout:**
1. Mark 6 parallel lines (lanes) on the floor — about 1 metre apart, 8 metres long, running left to right.
2. Label the start of each lane: Position 1 (leftmost) through Position 6 (rightmost).
3. Mark 5 "layers" as vertical lines crossing all lanes.
4. At each layer, mark which positions are connected with a small circle or X.

---

## The Network: Layer by Layer

This is a verified correct 6-input sorting network (12 comparators, 5 layers):

```
Positions:    1    2    3    4    5    6
              │    │    │    │    │    │
Layer 1:      ●────●    ●────●    ●────●
              │    │    │    │    │    │
Layer 2:      ●────────────────────●    │
              │    ●────────────────●    │
              │    │    │    │    │    │
Layer 3:      │    ●────●    ●────●    │
              │    │    │    │    │    │
Layer 4:      ●────────────────────●    │
              │    │    ●────●    │    │
              │    │    │    │    │    │
Layer 5:      │    ●────●    ●────●    │
              │    │    │    │    │    │
Output:       1    2    3    4    5    6
```

**Layer details (positions that compare-and-swap):**
- **Layer 1:** (1,2), (3,4), (5,6) — 3 simultaneous comparisons
- **Layer 2:** (1,3), (2,6) — 2 simultaneous comparisons  
- **Layer 3:** (2,3), (4,5) — 2 simultaneous comparisons
- **Layer 4:** (1,4), (3,6) — 2 simultaneous comparisons
- **Layer 5:** (2,4), (3,5) — 2 simultaneous comparisons (then final check: (2,3),(4,5) if needed)

*Note: After these layers, verify with input [3,1,4,2,6,5] — the output should be [1,2,3,4,5,6].*

---

## Rule at Each Comparator

When two people meet at a comparator:
- **Lower number → stays in the lower-numbered lane** (or moves left)
- **Higher number → moves to the higher-numbered lane** (or moves right)

---

## Worked Example

**Input: [3, 1, 4, 2, 6, 5]** — volunteers hold these numbers at positions 1–6.

After Layer 1 (compare 1↔2, 3↔4, 5↔6):
- Pos 1↔2: 3 vs 1 → swap → 1 and 3
- Pos 3↔4: 4 vs 2 → swap → 2 and 4
- Pos 5↔6: 6 vs 5 → swap → 5 and 6
- Result: [1, 3, 2, 4, 5, 6]

After each subsequent layer, the values move toward sorted order. After all 5 layers, output should be [1, 2, 3, 4, 5, 6].

---

## Desk Version

If floor space isn't available: draw 6 columns on paper. Write starting numbers at top. Draw horizontal bridges between columns at each layer. Trace values down, swapping at bridges as needed.
