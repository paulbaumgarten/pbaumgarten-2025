# Lesson Plan: Memory Box
**Year Group:** 7 | **Duration:** 50 minutes | **Topic:** Variables

---

## 1. Overview

**Core Concept:** Variables — named storage boxes that hold values which can change.

**Learning Objectives:**
- Define what a variable is (name + value)
- Trace variable values through a sequence of events
- Understand assignment (setting a value) and update (changing a value)
- Recognise that the name stays fixed while the value changes

**Key Vocabulary:**

| Term | Definition |
|------|-----------|
| Variable | A named storage location that holds a value |
| Value | The data stored inside a variable |
| Assign | Set a variable to a value for the first time |
| Update | Change the value stored in a variable |
| State | The current set of all variable values at a moment in time |
| Trace | Follow a program step by step, tracking variable values |

---

## 2. Before the Lesson

**Print:**
- [ ] `worksheet-variable-trace.md` — 1 copy per student
- [ ] `resource-variable-labels.md` — print and cut, 1 set per pair (laminate if possible)

**Gather:**
- [ ] Sticky notes or small whiteboard sections (for the live demo)
- [ ] Markers (so label values are readable from a distance)
- [ ] Pencils for tracing worksheet

**Room Setup:**
- Pairs of desks for the worksheet phase
- Clear space at front for 3 volunteers in the hook activity

---

## 3. Timed Lesson Flow

### 0–5 min — Hook: Live Variable Demo
1. Choose 3 volunteers. Give each a large label card from `resource-variable-labels.md`:
   - Student 1: **HEALTH** — write `10` on their value box
   - Student 2: **GOLD** — write `0` on their value box
   - Student 3: **ITEMS** — write `[]` (empty list) on their value box
2. Read events aloud:
   - *"You find a treasure chest. GOLD = GOLD + 20."* → Student 2 updates to `20`
   - *"A goblin attacks. HEALTH = HEALTH - 3."* → Student 1 updates to `7`
   - *"You pick up a sword. ITEMS = ITEMS + [sword]."* → Student 3 updates
3. Ask the class: *"What's staying the same? What's changing?"*
4. Key point: **The NAME stays fixed. The VALUE changes.**

### 5–10 min — Explain Variables
1. A variable is like a labelled box. The label (name) never changes.
2. The contents (value) can change any time you assign a new value.
3. When you write `GOLD = GOLD + 20`, the computer:
   - Reads the current value of GOLD (0)
   - Adds 20 (= 20)
   - Stores the result back in GOLD (now 20)

### 10–30 min — Worksheet: Text Adventure Trace
1. Distribute `worksheet-variable-trace.md`.
2. Students read the text adventure story and complete the trace table — filling in the value of each variable after every event.
3. Key discipline: fill in EVERY cell, even if the value didn't change for that variable.

### 30–40 min — Pair Comparison
1. Pairs compare their completed traces.
2. Discuss any cells where they disagree.
3. Work through the disagreement: which reading of the event is correct?

### 40–45 min — Teacher Reveals Correct Trace
Walk through the table on the board. Focus on the tricky events (negative gold, removing an item that wasn't there).

### 45–50 min — Debrief
- Where do variables appear in real life? (Game saves, shopping carts, user accounts, scores)
- What happens if a program forgets to update a variable? (Stale data, wrong results)
- What happens if you try to use a variable before assigning it a value?

---

## 4. Teacher Facilitation Notes

**What to look for:**
- Students who change the VARIABLE NAME instead of the value — the name is fixed!
- Students who forget to carry forward the previous value before adding (e.g., forgetting GOLD was 20 before subtracting 8)
- Students who skip cells — every event must be traced for every variable

**How to intervene minimally:**
- *"What was the value of GOLD BEFORE this event?"*
- *"The event says GOLD = GOLD + 20. What is GOLD right now? What do you add to it? What does GOLD become?"*
- *"Only the VALUE in the box changes. Cross out the old value and write the new one."*

**Common misconceptions:**
- The variable name changes when the value changes — NO. The name is permanent.
- You can skip variables that didn't change — NO. Always trace every variable every step.
- ITEMS = ITEMS - [sword] when ITEMS is empty crashes the program — YES! This is worth discussing.

---

## 5. Extension / Early Finisher Tasks

1. **Write 3 more events** that change the variables. What are the final values?
2. **Error events:** What should a program do if GOLD goes below 0? Write an IF statement to prevent it.
3. **Design your own:** Create a different text adventure with different variables (e.g., FUEL, PASSENGERS, DISTANCE for a space game).

---

## 6. Key Takeaway

> **A variable is a named storage box. The name is fixed — it never changes. The value inside can change at any time. Variables are how programs remember things.**
