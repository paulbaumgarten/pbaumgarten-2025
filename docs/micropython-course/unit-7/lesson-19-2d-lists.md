---
title: "Lesson 19 - Two-Dimensional Lists"
layout: default
nav_order: 1
parent: "Unit 7: The Grid"
grand_parent: MicroPython Course
---

# Lesson 19 — Two-Dimensional Lists
{: .no_toc }

**Estimated time:** 75 minutes

- TOC
{:toc}

---

## Learning Objectives

By the end of this lesson you will be able to:

1. Create a 2D list (list of lists)
2. Access elements using double indexing `[row][col]`
3. Use nested loops to process all elements
4. Represent a grid of data as a 2D list

---

## Concepts

### What is a 2D List?

A **2D list** is a list where each element is itself a list. Think of it like a spreadsheet — rows and columns.

```python
grid = [
    [1, 2, 3],    # Row 0
    [4, 5, 6],    # Row 1
    [7, 8, 9],    # Row 2
]
```

This is a 3×3 grid. `grid` is a list of 3 rows. Each row is a list of 3 numbers.

**Analogy:** A cinema seating plan. `seats[2][5]` means "row 2, seat 5". First you select the row, then the seat within it.

### Double Indexing

Access an element with `grid[row][col]`:
- First index `[row]` — selects a row (gives you a 1D list)
- Second index `[col]` — selects an element within that row

```python
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(grid[0])       # [1, 2, 3]  — entire row 0
print(grid[1][2])    # 6          — row 1, col 2
print(grid[2][0])    # 7          — row 2, col 0
print(grid[0][-1])   # 3          — row 0, last column
```

**Row first, column second.** Always.

### Nested Loops for 2D Lists

To visit every element, use a loop for rows and inside it a loop for columns:

```python
for row in range(3):
    for col in range(3):
        print(f"grid[{row}][{col}] = {grid[row][col]}")
```

Or iterate the values directly:
```python
for row in grid:          # row is a 1D list
    for value in row:     # value is a single element
        print(value, end=" ")
    print()   # New line after each row
```

### Creating a 2D List Safely

{: .important }
**Don't do this:** `grid = [[0] * 3] * 3`
This creates 3 references to the **same** inner list. Changing one row changes all rows!

**Do this instead:**
```python
grid = [[0] * 3 for _ in range(3)]   # Three independent lists
```

Or for the 8×8 grid:
```python
grid = [[0] * 8 for _ in range(8)]
```

**Why the difference?**
- `[[0]*3]*3` — multiplies the SAME list object 3 times
- `[[0]*3 for _ in range(3)]` — creates 3 NEW, independent lists

Test this in the REPL:
```python
>>> a = [[0]*3]*3
>>> a[0][1] = 99
>>> print(a)
[[0, 99, 0], [0, 99, 0], [0, 99, 0]]   # All rows changed!

>>> b = [[0]*3 for _ in range(3)]
>>> b[0][1] = 99
>>> print(b)
[[0, 99, 0], [0, 0, 0], [0, 0, 0]]   # Only row 0 changed ✓
```

### Modifying Elements

```python
grid = [[0]*4 for _ in range(3)]   # 3 rows, 4 cols, all zeros

grid[1][2] = 5    # Set row 1, col 2 to 5
grid[0][0] = 1    # Set row 0, col 0 to 1

for row in grid:
    print(row)
```

---

## Guided Walkthrough

### Step 1: Basic 2D List

```python
# A 3x4 grid (3 rows, 4 columns)
data = [
    [1,   2,   3,   4],   # Row 0
    [5,   6,   7,   8],   # Row 1
    [9,  10,  11,  12],   # Row 2
]

print(data[0])          # [1, 2, 3, 4]
print(data[1][2])       # 7
print(data[2][-1])      # 12
print(data[-1][0])      # 9  (last row, first column)

# Modify a value
data[1][1] = 99
print(data[1])          # [5, 99, 7, 8]
```

### Step 2: Nested Loops

```python
grid = [[1,2,3],[4,5,6],[7,8,9]]

# Print every element with position
for row in range(len(grid)):
    for col in range(len(grid[row])):
        print(f"[{row}][{col}]={grid[row][col]}", end="  ")
    print()   # New line after each row

print()

# Pretty print as a table
for row in grid:
    for val in row:
        print(f"{val:3}", end="")
    print()
```

### Step 3: Visual Grid (Pixel Art)

```python
# A 6x8 bitmap — 1 = lit, 0 = dark
# This spells an "H"
LETTER_H = [
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
]

for row in LETTER_H:
    for cell in row:
        print("█" if cell == 1 else ".", end=" ")
    print()
```

### Step 4: Creating Patterns with Nested Loops

```python
SIZE = 8
grid = [[0] * SIZE for _ in range(SIZE)]

# Fill main diagonal
for i in range(SIZE):
    grid[i][i] = 1

# Fill anti-diagonal
for i in range(SIZE):
    grid[i][SIZE - 1 - i] = 2   # 2 where anti-diag (and 3 where they cross)

# Fix the crossing point
grid[SIZE//2 - 1][SIZE//2 - 1] = 3
grid[SIZE//2][SIZE//2] = 3

# Print
for row in grid:
    for val in row:
        chars = {0: ".", 1: "\\", 2: "/", 3: "X"}
        print(chars[val], end=" ")
    print()
```

### Step 5: Counting and Searching

```python
# A grid of temperatures
temps = [
    [22, 23, 21, 24],
    [25, 20, 22, 23],
    [21, 22, 26, 20],
]

# Count cells above 23°C
hot_count = 0
for row in temps:
    for temp in row:
        if temp > 23:
            hot_count += 1
print(f"Cells above 23°C: {hot_count}")

# Find max temperature position
max_temp = temps[0][0]
max_row, max_col = 0, 0
for r in range(len(temps)):
    for c in range(len(temps[r])):
        if temps[r][c] > max_temp:
            max_temp = temps[r][c]
            max_row, max_col = r, c
print(f"Max temp: {max_temp}°C at [{max_row}][{max_col}]")
```

---

## Challenges

### ⭐ Core
Create a 6×6 2D list. Fill it so the border cells (row 0, row 5, col 0, col 5) are 1 and all inner cells are 0. Print it as a visual grid using `█` for 1 and `.` for 0.

### ⭐⭐ Extension
Create a 8×8 checkerboard: cell is 1 if `(row + col) % 2 == 0`, else 0. Print it visually. Count how many 1s and how many 0s. Then create a second grid where you swap the 1s and 0s (complementary pattern) and print both side by side.

### ⭐⭐⭐ Stretch
Implement one step of **Conway's Game of Life** on a 6×6 grid:
- Start with a random grid (`import random; cell = random.randint(0, 1)`)
- For each cell, count its live neighbours (up to 8 surrounding cells — handle edges carefully)
- Apply rules: live cell with <2 or >3 live neighbours dies; dead cell with exactly 3 neighbours comes alive
- Print the grid before and after one step

---

## Common Mistakes & Debugging

**`grid[col][row]` instead of `grid[row][col]`**
Row first, column second — always. This is the single most common mistake with 2D lists.

**`[[0]*8]*8` creates shared references**
Use `[[0]*8 for _ in range(8)]` instead. Test this in the REPL with the example shown above if unsure.

**Off-by-one in nested loops**
Use `range(len(grid))` for rows and `range(len(grid[0]))` for columns to avoid hardcoding sizes.

**`for row in grid:` vs `for row in range(len(grid)):`**
The first gives you the actual row list. The second gives you the row index. Use the index version when you need to modify values.

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| **2D list** | A list whose elements are themselves lists — represents a grid |
| **row** | The outer (first) index of a 2D list |
| **column** | The inner (second) index of a 2D list |
| **double indexing** | Using `grid[row][col]` to access a specific cell |
| **nested loop** | A loop inside another loop — needed to visit every cell in a 2D grid |
| **list comprehension** | `[expression for variable in iterable]` — creates a list in one line |
