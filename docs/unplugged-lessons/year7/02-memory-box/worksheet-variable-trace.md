# The Memory Box — Variable Trace Worksheet

**Name:** _________________________________ **Date:** _____________

---

## Your Quest

You are a hero on an adventure. As events happen, the values of your variables change. Your job: **trace every variable value after every event**.

**Rule:** Fill in EVERY cell — even if a variable didn't change for that event. Carry the value forward.

---

## The Story

**Starting values:**
- `HEALTH = 10`
- `GOLD = 0`
- `ITEMS = []`   *(an empty list — you have no items yet)*

---

**Event 1:** You find a healing potion on the ground.
`ITEMS = ITEMS + [potion]`

**Event 2:** A goblin throws a rock at you.
`HEALTH = HEALTH - 3`

**Event 3:** You discover a treasure chest!
`GOLD = GOLD + 20`

**Event 4:** You buy a map from a travelling merchant.
`GOLD = GOLD - 8`
`ITEMS = ITEMS + [map]`

**Event 5:** You try to buy a shield. It costs 15 gold.
`GOLD = GOLD - 15`
`ITEMS = ITEMS + [shield]`
*(Careful — does your GOLD go negative? Note this in the discussion section below.)*

**Event 6:** You use the healing potion to recover health.
`HEALTH = HEALTH + 5`
`ITEMS = ITEMS - [potion]`

**Event 7:** You sell the map to another traveller.
`GOLD = GOLD + 6`
`ITEMS = ITEMS - [map]`

**Event 8:** You reach the castle. Final check!

---

## Trace Table

| Event | HEALTH | GOLD | ITEMS |
|-------|:------:|:----:|-------|
| Start | 10 | 0 | [] |
| Event 1 | | | |
| Event 2 | | | |
| Event 3 | | | |
| Event 4 | | | |
| Event 5 | | | |
| Event 6 | | | |
| Event 7 | | | |
| Event 8 (Final) | | | |

---

## Discussion Questions

**Event 5 — GOLD goes negative:**
After buying the shield, GOLD = ___. Is this a problem?

In a real game, what should the program do to PREVENT the player from spending gold they don't have?

_______________________________________________________________

_______________________________________________________________

**Event 6 — Removing an item:**
After using the potion, ITEMS = ___. This worked fine.
But what if you had tried to remove the [potion] in Event 2 (before you picked it up)?

What should a program do if you try to remove something that isn't in the list?

_______________________________________________________________

_______________________________________________________________

**General reflection:**
If you were writing this as a real program, which variable would be hardest to manage? Why?

_______________________________________________________________

_______________________________________________________________
