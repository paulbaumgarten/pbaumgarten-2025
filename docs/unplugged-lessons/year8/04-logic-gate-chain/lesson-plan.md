# Lesson Plan: Logic Gate Chain
**Year Group:** 8 | **Duration:** 50 minutes | **Topic:** Boolean Logic & Logic Gates

---

## 1. Overview

**Core Concept:** Boolean logic — every value is TRUE or FALSE, and AND, OR, NOT gates combine these to make decisions.

**Learning Objectives:**
- Evaluate AND, OR, and NOT with TRUE/FALSE inputs using truth tables
- Trace values through a chain of logic gates
- Predict the output of a combined gate circuit
- Connect logic gates to real computer hardware and IF statements

**Key Vocabulary:**

| Term | Definition |
|------|-----------|
| Boolean | A value that is either TRUE or FALSE — nothing in between |
| AND gate | Output is TRUE only if BOTH inputs are TRUE |
| OR gate | Output is TRUE if AT LEAST ONE input is TRUE |
| NOT gate | Output is the OPPOSITE of the input |
| Truth table | A table showing every possible input combination and the resulting output |
| Gate chain | A sequence of gates where one gate's output feeds the next |

---

## 2. Before the Lesson

**Print and Cut:**
- [ ] `resource-gate-cards.md` — 1 full set for the class physical activity (gate rule cards + TRUE/FALSE hand cards). 1 reduced set per group for desk work.

**Room Setup:**
- Clear space at front of room for the physical gate chain (5 students in a line)
- Standard seating for desk work

---

## 3. Timed Lesson Flow

### 0–5 min — Hook: Real-World AND and OR
1. *"Stand up if you are a student AND you have a bag with you."* (both conditions must be true)
2. *"Now: stand up if you are taller than 160cm OR you are wearing something blue."* (either condition works)
3. *"Why did more people stand for the OR rule?"* Because OR is generous — only one must be true.

### 5–12 min — Truth Tables
1. Draw AND, OR, and NOT truth tables on the board.
2. Work through 2–3 examples together as a class.
3. Key insight: **these three gates can be combined to make any logical decision a computer ever needs.**

### 12–25 min — Physical Gate Chain
1. 5 volunteers: Input A, Input B, NOT gate, AND gate, Output.
2. NOT gate takes Input A and outputs the opposite.
3. AND gate takes NOT's output and Input B — outputs TRUE only if both are TRUE.
4. Output student shows the final result.
5. Run 4 different input combinations.

### 25–40 min — Desk Activity
Groups draw a gate chain (NOT → AND → OR with third input C) and complete the full truth table for all input combinations.

### 40–47 min — Reverse Challenge
Given output = TRUE, find ALL valid input combinations.

### 47–50 min — Real-world connections: CPU arithmetic, memory, security access, IF statements.

---

## 4. Teacher Facilitation Notes

**What to look for:**
- Students applying AND logic to OR gates — always check the gate card rule first
- Confusion with chained gates — trace one step at a time, left to right
- Students who "just know" without tracing — insist on showing each step

**Common misconceptions:**
- OR means only one input matters — both TRUE + TRUE → TRUE for OR (not exclusive OR)
- NOT changes the gate type — NOT only changes the value passing through it

---

## 5. Extension Tasks

1. Design a 3-gate chain that outputs TRUE only when EXACTLY ONE of three inputs is TRUE.
2. Research: what is a NAND gate? Why can all logic be built from NAND gates alone?
3. Write an IF statement in pseudocode using AND and OR. Which gates would it compile to?

---

## 6. Key Takeaway

> **Every decision a computer makes is built from AND, OR, and NOT gates — billions of them, at nanosecond speed. Every IF statement you write compiles down to gate logic.**
