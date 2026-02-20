# Logic Gate Cards — Print and Cut

---

## GATE RULE CARDS (Laminate if possible)

### AND GATE

```
  A ──┐
      ├──[ AND ]──── Output
  B ──┘
```

**Rule:** Output = TRUE **only if BOTH inputs are TRUE.**

| Input A | Input B | Output |
|:-------:|:-------:|:------:|
| TRUE | TRUE | **TRUE** |
| TRUE | FALSE | FALSE |
| FALSE | TRUE | FALSE |
| FALSE | FALSE | FALSE |

*Memory: AND is strict — everyone must qualify.*

---

### OR GATE

```
  A ──┐
      ├──[ OR ]───── Output
  B ──┘
```

**Rule:** Output = TRUE if **AT LEAST ONE input is TRUE.**

| Input A | Input B | Output |
|:-------:|:-------:|:------:|
| TRUE | TRUE | **TRUE** |
| TRUE | FALSE | **TRUE** |
| FALSE | TRUE | **TRUE** |
| FALSE | FALSE | FALSE |

*Memory: OR is generous — anyone can qualify.*

---

### NOT GATE

```
  A ──[ NOT ]────── Output
```

**Rule:** Output = the **OPPOSITE** of the input.

| Input A | Output |
|:-------:|:------:|
| TRUE | **FALSE** |
| FALSE | **TRUE** |

*Memory: NOT flips the value.*

---

## TRUE / FALSE HAND CARDS

*Print 16 copies of each. Cut out. Use during the physical activity.*

```
┌─────────────────┐     ┌─────────────────┐
│                 │     │                 │
│      TRUE       │     │     FALSE       │
│                 │     │                 │
│  (hold up when  │     │  (hold up when  │
│  your value     │     │  your value     │
│  is TRUE)       │     │  is FALSE)      │
│                 │     │                 │
└─────────────────┘     └─────────────────┘
```

---

## Practice Chains

**Chain 1:** A → [NOT] → AND with B

- A=TRUE, B=FALSE: NOT(TRUE)=FALSE → FALSE AND FALSE = **FALSE**
- A=FALSE, B=TRUE: NOT(FALSE)=TRUE → TRUE AND TRUE = **TRUE**

**Chain 2:** A OR B → [NOT]

- A=FALSE, B=FALSE: FALSE OR FALSE=FALSE → NOT(FALSE) = **TRUE**
- A=TRUE, B=FALSE: TRUE OR FALSE=TRUE → NOT(TRUE) = **FALSE**

**Chain 3:** (A AND B) OR C

- A=TRUE, B=FALSE, C=TRUE: (TRUE AND FALSE)=FALSE → FALSE OR TRUE = **TRUE**
- A=FALSE, B=FALSE, C=FALSE: FALSE AND FALSE=FALSE → FALSE OR FALSE = **FALSE**
