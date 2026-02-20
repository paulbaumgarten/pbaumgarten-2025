# Lesson Plan: Map Problem
**Year Group:** 9 | **Duration:** 50 minutes | **Topic:** Graph Theory & Shortest Path

---

## 1. Overview

**Core Concept:** Graphs model connections and distances. Systematic exploration finds shortest paths — the basis of every navigation algorithm.

**Learning Objectives:**
- Represent a map as a weighted graph (nodes + edges + weights)
- Find shortest paths using systematic exploration (Dijkstra-like thinking)
- Understand why the greedy nearest-neighbour approach doesn't always find the overall shortest route
- Connect to real-world navigation algorithms

**Key Vocabulary:**

| Term | Definition |
|------|-----------|
| Graph | A structure of nodes connected by edges |
| Node | A point in the graph (e.g., a town) |
| Edge | A connection between two nodes (e.g., a road) |
| Weight | The cost of an edge (e.g., distance in km) |
| Path | A sequence of nodes connected by edges |
| Shortest path | The path with the minimum total weight |
| Dijkstra's algorithm | A systematic method for finding shortest paths in a weighted graph |

---

## 2. Before the Lesson

**Print:**
- [ ] `resource-island-map.md` — 1 per pair (A3 if possible)
- [ ] `worksheet-route-finder.md` — 1 per student

**Room Setup:** Pairs with a shared map.

---

## 3. Timed Lesson Flow

### 0–5 min — Hook: The Delivery Driver
1. *"You're a delivery driver on the island of Computia. You start in Port Alpha. You need to deliver packages to three different towns. What route do you take to drive the least distance?"*
2. Show the map. Give students 30 seconds to look at it. First impressions?

### 5–10 min — Graph Vocabulary
1. Towns = nodes, roads = edges, distances = weights.
2. *"This map IS a graph. We can draw it as a diagram with circles and lines."*
3. Students draw the graph representation on the worksheet.

### 10–20 min — Challenge 1: Intuitive Shortest Paths
Students try to find the shortest path from Port Alpha to each other town by intuition. Record their guess routes.

### 20–35 min — Challenge 2: Systematic Exploration
1. Guide students toward a systematic approach:
   - Start at Alpha (distance=0)
   - Look at all connected nodes; note their distances
   - Always visit the unvisited node with the smallest known distance
   - Update distances to its neighbours if a shorter path is found
2. Work through the first 2 steps together; then pairs complete the worksheet.

### 35–43 min — Challenge 3: Delivery Tour
Visit 4 specific towns and return to Alpha. Find the minimum total distance. Try different orderings.

### 43–48 min — Discussion
- Did everyone find the same shortest paths? (Yes for point-to-point — Dijkstra gives correct answer)
- Did everyone find the same tour? (No — the travelling salesman problem is NP-hard)

### 48–50 min — Real world: sat-nav, Google Maps, network packet routing.

---

## 4. Teacher Facilitation Notes

**What to look for:**
- Students who jump to intuitive answers without checking — the "obvious" route isn't always shortest
- Students confused by systematic approach — walk through step by step: "What's the closest unvisited node to Alpha right now?"

**Common misconceptions:**
- The shortest road = the shortest route — NO, the shortest path may go via more nodes with shorter individual edges
- Dijkstra's is the only way — it's one correct method; students may find correct answers via other approaches

---

## 5. Extension Tasks

1. If road Alpha–Delta Bay is closed, does the shortest path change? Find the alternative.
2. Research: what is A* search? How is it different from Dijkstra's?
3. Why is the travelling salesman problem (visiting all towns optimally) so much harder than shortest path?

---

## 6. Key Takeaway

> **Graphs model connections and distances. Systematic exploration always finds shortest paths — this is how every navigation app works, from sat-nav to Google Maps to network routing.**
