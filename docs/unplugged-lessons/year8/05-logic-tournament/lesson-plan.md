# Lesson Plan: Logic Tournament
**Year Group:** 8 | **Duration:** 50 minutes | **Topic:** Boolean Logic Applied to Search

---

## 1. Overview

**Core Concept:** Boolean logic applied to elimination search — using yes/no conditions to narrow a set, and evaluating which conditions are most efficient.

**Learning Objectives:**
- Apply AND logic to narrow a set using multiple conditions simultaneously
- Evaluate the efficiency of different yes/no questions
- Connect elimination search to binary search and database queries

**Key Vocabulary:**

| Term | Definition |
|------|-----------|
| Elimination | Removing items that don't match a condition |
| Condition | A yes/no question about an attribute |
| Boolean query | A question that returns TRUE or FALSE for each item |
| Efficient | Achieves the goal with minimum steps |
| Binary search | Repeatedly halving the search space to find an item |

---

## 2. Before the Lesson

**Print:**
- [ ] `resource-character-sheet.md` — 2 per student (one reference, one to mark off)
- [ ] `worksheet-strategy-analysis.md` — 1 per student

**Room Setup:** Pairs facing each other.

---

## 3. Timed Lesson Flow

### 0–5 min — Rules
1. Each student secretly picks a character from the grid.
2. Players take turns asking yes/no questions about ATTRIBUTES (not names).
3. Cross off eliminated characters after each answer.
4. First to correctly identify partner's character wins.
5. Track: how many questions did you need?

### 5–25 min — Round 1: Play!

### 25–32 min — Strategy Discussion
- What was your first question? Why?
- What's the ideal question? → one that eliminates exactly 12 characters regardless of the answer (50/50 split)

### 32–42 min — Worksheet: Efficiency Analysis
Calculate how many characters each question type eliminates.

### 42–48 min — Round 2 with strategy

### 48–50 min — Debrief: this IS binary search. Every optimal question halves the candidates. Databases use this logic.

---

## 4. Teacher Facilitation Notes

**What to look for:**
- Students asking "Is your character Alex?" — eliminates only 1 if NO. Very inefficient.
- Students not eliminating eliminated characters — keeping track is the whole game

**Common misconceptions:**
- The best question is the one most likely to be YES — no, the best question splits 50/50
- More attributes in one question = more efficient — a compound AND question may be too specific

---

## 5. Extension Tasks

1. Write a 3-attribute AND query. How many characters match?
2. Compare to SQL: `SELECT * FROM characters WHERE hair='blonde' AND glasses=TRUE`
3. Design a character sheet where it's harder to find the efficient questions

---

## 6. Key Takeaway

> **Efficient Boolean queries eliminate the most possibilities with the fewest conditions. This is how search engines and databases work — indexed yes/no filtering on attributes.**
