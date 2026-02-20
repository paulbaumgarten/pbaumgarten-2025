# Complexity Olympics — Results Recording Sheet

**Name:** _________________________________ **Date:** _____________

---

## Station 1: O(1) — Constant Time

| Input size (n) | Steps taken |
|:--------------:|:-----------:|
| 10 | |
| 100 | |
| 1,000 | |

**Pattern I noticed:** _______________________________________________

---

## Station 2: O(log n) — Logarithmic Time

| Input size (n) | Guesses needed |
|:--------------:|:--------------:|
| 8 | |
| 16 | |
| 32 | |

**Pattern I noticed:** _______________________________________________

**Predict: n=64 would need ___ guesses. n=1024 would need ___ guesses.**

---

## Station 3: O(n) — Linear Time

| Input size (n) | Cards examined |
|:--------------:|:--------------:|
| 5 | |
| 10 | |
| 20 | |

**Pattern I noticed:** _______________________________________________

---

## Station 4: O(n²) — Quadratic Time

| Input size (n) | Actual comparisons | Formula: n×(n-1)÷2 |
|:--------------:|:-----------------:|:-------------------:|
| 3 | | |
| 4 | | |
| 5 | | |
| 6 | | |

**Pattern I noticed:** _______________________________________________

---

## Graph — All Four Complexity Classes

*Plot on the axes below. Use different symbols for each: O(1)=●, O(log n)=▲, O(n)=■, O(n²)=◆*

```
Steps
 200 |◆                                         ◆
     |
 150 |
     |                                      ◆
 100 |
     |                               ◆
  50 |
     |
  20 |■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
     |▲  ▲   ▲    ▲     ▲
   5 |● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ● ●
     └─────────────────────────────────────────
     0    5   10   15   20  (input size n)
```

*Sketch your actual data on the graph above.*

---

## Predictions for n=100

| Complexity | Formula | Steps for n=100 |
|------------|---------|:---------------:|
| O(1) | always 1 | 1 |
| O(log n) | log₂(100) ≈ 7 | 7 |
| O(n) | n | 100 |
| O(n²) | n×(n-1)÷2 | |

---

## Real-World Decisions

**A social network has 1 billion users. A search through all users to find a match takes O(n) time. How many steps would that take? Why would this be unacceptable?**

_______________________________________________________________

_______________________________________________________________

**If you could choose between O(n) and O(n²) for sorting 10,000 names, which would you choose? How much better is it?**

_______________________________________________________________

---

## Big-O Summary

Fill in the final column:

| Name | Notation | Growth rate | Real-world example |
|------|----------|-------------|-------------------|
| Constant | O(1) | Always the same | |
| Logarithmic | O(log n) | Grows very slowly | |
| Linear | O(n) | Proportional to n | |
| Quadratic | O(n²) | Squares with n | |
