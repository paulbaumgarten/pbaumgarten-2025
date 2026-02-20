# Trigger Cards — Print and Cut

**Instructions:** Print this page, cut out the 12 cards, and place them face-down on maze grid squares before the lesson. One card per square (you won't use all squares).

---

```
┌──────────────────────┐  ┌──────────────────────┐  ┌──────────────────────┐
│   BONUS SQUARE       │  │   TRAP SQUARE        │  │   KEY SQUARE         │
│                      │  │                      │  │                      │
│ IF score < 10:       │  │ IF key = True:       │  │ You find a key!      │
│   score = score + 5  │  │   skip trap safely   │  │                      │
│ ELSE:                │  │ ELSE:                │  │ key = True           │
│   score = score + 2  │  │   health = health-3  │  │ score = score + 5    │
└──────────────────────┘  └──────────────────────┘  └──────────────────────┘

┌──────────────────────┐  ┌──────────────────────┐  ┌──────────────────────┐
│   SHORTCUT           │  │   HEALING POTION     │  │   ICY FLOOR          │
│                      │  │                      │  │                      │
│ IF health > 5:       │  │ health = health + 4  │  │ Flip a coin:         │
│   skip 2 squares     │  │                      │  │ HEADS: slip back     │
│ ELSE:                │  │ (No condition —      │  │   1 square           │
│   normal move        │  │  always applies)     │  │ TAILS: proceed       │
└──────────────────────┘  └──────────────────────┘  └──────────────────────┘

┌──────────────────────┐  ┌──────────────────────┐  ┌──────────────────────┐
│   LOCKED BRIDGE      │  │   GOLD COINS         │  │   GUARD              │
│                      │  │                      │  │                      │
│ IF key = True:       │  │ score = score + 10   │  │ IF score > 20:       │
│   cross bridge       │  │                      │  │   guard lets you     │
│ ELSE:                │  │ (No condition —      │  │   pass freely        │
│   return to row      │  │  always applies)     │  │ ELSE: wait 1 turn    │
│   start              │  │                      │  │   (lose a move)      │
└──────────────────────┘  └──────────────────────┘  └──────────────────────┘

┌──────────────────────┐  ┌──────────────────────┐  ┌──────────────────────┐
│   TELEPORT           │  │   DOUBLE BONUS       │  │   SAFE SQUARE        │
│                      │  │                      │  │                      │
│ Move directly to     │  │ score = score × 2    │  │ Nothing happens.     │
│ square B3.           │  │                      │  │                      │
│                      │  │ (No condition —      │  │ Take a breath.       │
│ (No condition)       │  │  always applies)     │  │                      │
└──────────────────────┘  └──────────────────────┘  └──────────────────────┘
```
