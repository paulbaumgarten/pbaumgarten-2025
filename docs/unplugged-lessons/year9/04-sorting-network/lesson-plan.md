# Lesson Plan: Sorting Network
**Year Group:** 9 | **Duration:** 50 minutes | **Topic:** Parallel Sorting & Sorting Networks

---

## 1. Overview

**Core Concept:** Sorting networks — a fixed sequence of compare-and-swap operations where multiple comparisons happen simultaneously (in parallel), sorting faster than sequential algorithms.

**Learning Objectives:**
- Follow a sorting network correctly as a physical activity
- Explain why sorting networks can be faster than sequential sorting algorithms
- Count layers (parallel steps) vs total comparisons
- Connect to parallel processing in hardware

**Key Vocabulary:**

| Term | Definition |
|------|-----------|
| Sorting network | A fixed circuit of compare-and-swap operations that always sorts, regardless of input |
| Comparator | A single compare-and-swap operation between two specific positions |
| Layer | A group of comparators that can execute simultaneously (no shared positions) |
| Parallel processing | Performing multiple operations at the same time |
| Sequential | Operations performed one after another |

---

## 2. Before the Lesson

**Print:**
- [ ] `resource-sorting-network-diagram.md` — 1 large copy for display; also chalk/tape the network on the floor
- [ ] `resource-number-cards.md` — 6 large cards (numbers 1–6), cut out

**Room Setup:**
- Clear a large floor area (or book the gym/hall)
- Use chalk or tape to mark 6 parallel lanes and the comparator crossing points
- Alternatively, draw the network large on the whiteboard and do a desk-version with small cards

---

## 3. Timed Lesson Flow

### 0–5 min — Setup and Rules
1. 6 volunteers stand at the 6 input positions, each holding a number card (shuffled).
2. Rules: at each comparator, the two people meeting compare their numbers — **smaller goes to the lower-numbered lane, larger to the higher-numbered lane**.
3. All comparators in the same LAYER happen SIMULTANEOUSLY.

### 8–25 min — Walk the Network
1. Teacher calls each layer. All comparators in that layer execute at the same time.
2. Students physically move (or swap cards) at comparator points.
3. After all layers: are the 6 people standing in sorted order?
4. Try again with a different shuffled input.

### 25–32 min — Count the Steps
Back at desks: how many LAYERS did the network have? How many total COMPARATORS?

### 32–40 min — Compare with Bubble Sort
Bubble sort on 6 items: worst case = 15 comparisons, 5 sequential passes.
Sorting network: 12 comparators BUT in only 5 layers — and layers are PARALLEL.

### 40–47 min — Why Does This Matter?
CPUs have multiple cores. GPUs have thousands of cores. Sorting networks are implemented directly in hardware — fixed logic gates, nanosecond speed.

### 47–50 min — Key Takeaway

---

## 4. Teacher Facilitation Notes

**What to look for:**
- Students who don't move simultaneously — emphasise: in a real chip, all comparators in a layer fire at the exact same nanosecond
- Students confused about which direction to move — smaller always goes to the LOWER-numbered lane (left)

**Common misconceptions:**
- Sorting networks are faster because they do fewer comparisons — no, they often do MORE comparisons than sequential sorts, but fewer TIME STEPS (layers)
- Parallel means random — no, it's a fixed, deterministic circuit

---

## 5. Extension Tasks

1. Design a sorting network for just 4 inputs. What's the minimum number of comparators? Layers?
2. Research: can a sorting network be proven correct mathematically? (Yes — the zero-one principle)
3. What is a GPU? How does it relate to sorting networks and parallel processing?

---

## 6. Key Takeaway

> **Sorting networks run comparisons in parallel — multiple comparisons at the exact same instant. This is how hardware sorts at nanosecond speeds. Fewer time steps, not fewer comparisons.**
