---
title: "Lesson 11 - Introduction to Lists"
layout: default
nav_order: 1
parent: "Unit 4: Collections of Data"
grand_parent: MicroPython Course
---

# Lesson 11 — Introduction to Lists
{: .no_toc }

**Estimated time:** 60 minutes

- TOC
{:toc}

---

## Learning Objectives

By the end of this lesson you will be able to:

1. Create a list and access elements by index
2. Use negative indexing and slicing on lists
3. Use `len()` with lists
4. Iterate through a list using a `for` loop

---

## Concepts

### What is a List?

A **list** is an ordered collection of values stored in a single variable. Think of it like a numbered shelf — each item has a position (slot number), and you can access any item by its slot number.

```python
scores = [85, 72, 91, 68, 77]
#          0   1   2   3   4   ← indices
```

Lists use **square brackets** `[]`, with items separated by commas.

**Lists can hold any type** (or even mixed types):
```python
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
mixed = [42, "hello", True, 3.14]    # Possible, though unusual
colours = [(255,0,0), (0,255,0), (0,0,255)]   # List of tuples
```

### Accessing Items — Indexing

Use `list[index]` to access an item. Indexing starts at **0**:

```python
fruits = ["apple", "banana", "mango", "cherry"]
#           0         1        2         3

print(fruits[0])   # "apple"
print(fruits[2])   # "mango"
print(fruits[-1])  # "cherry"  (last item)
print(fruits[-2])  # "mango"   (second-to-last)
```

**Negative indexing** counts from the end:
- `-1` = last item
- `-2` = second-to-last
- etc.

### Slicing

Extract a portion of a list with `[start:end]` (same as string slicing):

```python
nums = [10, 20, 30, 40, 50, 60]

print(nums[1:4])    # [20, 30, 40]  (index 1, 2, 3 — not 4)
print(nums[:3])     # [10, 20, 30]  (from start to index 2)
print(nums[3:])     # [40, 50, 60]  (from index 3 to end)
print(nums[::2])    # [10, 30, 50]  (every other item)
print(nums[::-1])   # [60, 50, 40, 30, 20, 10]  (reversed)
```

Slicing **never raises an IndexError** — it just gives you as much as exists.

### `len()`

`len()` returns the number of items in a list:

```python
fruits = ["apple", "banana", "mango"]
print(len(fruits))   # 3
```

Last valid index is always `len(list) - 1`.

### Modifying Items

Lists are **mutable** — you can change individual items:

```python
temperatures = [22, 24, 19, 28, 21]
temperatures[2] = 20    # Change index 2 from 19 to 20
print(temperatures)     # [22, 24, 20, 28, 21]
```

### Iterating — `for` Loop Over a List

The most natural way to process every item:

```python
# Method 1: iterate values directly
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# Method 2: iterate by index (useful when you need the index)
for i in range(len(fruits)):
    print(f"Item {i}: {fruits[i]}")

# Method 3: enumerate (gives both)
for i, fruit in enumerate(fruits):
    print(f"Item {i}: {fruit}")
```

---

## Guided Walkthrough

### Step 1: Creating and Accessing Lists

```python
scores = [85, 72, 91, 68, 77]

print("All scores:", scores)
print("First score:", scores[0])        # 85
print("Third score:", scores[2])        # 91
print("Last score:", scores[-1])        # 77
print("Second to last:", scores[-2])    # 68
print("Number of scores:", len(scores)) # 5
```

### Step 2: Slicing

```python
colours = ["red", "orange", "yellow", "green", "blue", "purple"]

print(colours[1:4])    # ['orange', 'yellow', 'green']
print(colours[:3])     # ['red', 'orange', 'yellow']
print(colours[3:])     # ['green', 'blue', 'purple']
print(colours[::2])    # ['red', 'yellow', 'blue']
print(colours[::-1])   # Reversed
```

### Step 3: Modifying and Iterating

```python
temps = [22, 24, 19, 28, 21]

# Increase all temperatures by 2 degrees
for i in range(len(temps)):
    temps[i] = temps[i] + 2

print("Updated:", temps)   # [24, 26, 21, 30, 23]
```

### Step 4: LED Colour Palette

```python
import machine, neopixel, time

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

# A list of (name, RGB) tuples
palette = [
    ("Red",     (255, 0, 0)),
    ("Orange",  (255, 100, 0)),
    ("Yellow",  (255, 200, 0)),
    ("Green",   (0, 255, 0)),
    ("Cyan",    (0, 200, 200)),
    ("Blue",    (0, 0, 255)),
    ("Purple",  (100, 0, 200)),
]

print(f"Palette has {len(palette)} colours")

# Show each colour using indexing
print("First colour:", palette[0][0])
np[0] = palette[0][1]   # Access the RGB tuple inside the outer tuple
np.write()
time.sleep(1)

print("Last colour:", palette[-1][0])
np[0] = palette[-1][1]
np.write()
time.sleep(1)

# Show all colours in order
for name, colour in palette:
    np[0] = colour
    np.write()
    print(f"  {name}")
    time.sleep(0.5)

np[0] = (0, 0, 0)
np.write()
```

### Step 5: Analysing a List

```python
test_scores = [85, 72, 91, 68, 77, 83, 95, 61, 78, 88]

print(f"Number of scores: {len(test_scores)}")
print(f"Highest score: {max(test_scores)}")
print(f"Lowest score: {min(test_scores)}")
print(f"Total: {sum(test_scores)}")
print(f"Average: {sum(test_scores) / len(test_scores):.1f}")

# Count scores above 80
high_scores = 0
for score in test_scores:
    if score >= 80:
        high_scores += 1

print(f"Scores above 80: {high_scores}")
```

`max()`, `min()`, `sum()` are built-in functions that work on lists of numbers.

---

## Challenges

### ⭐ Core
Create a list of 5 of your favourite things (strings). Print each item on its own line with its index number, like "0: pizza". Then print the list reversed (using slicing). Finally, print the first and last items.

### ⭐⭐ Extension
Create a list of at least 8 LED colours (tuples). Display each colour for 0.3 seconds, printing the index and colour values. Then display the list in reverse order. Print the index count before you start.

### ⭐⭐⭐ Stretch
Create two parallel lists — one of colour names (strings) and one of RGB values (tuples). They must have the same length with matching indices (e.g., `names[2]` and `colours[2]` are the same colour). Ask the user to type a colour name. If it's in the names list, find its index and display the matching colour on the LED. If not found, print "not found" and list all available colours.

---

## Common Mistakes & Debugging

**`IndexError: list index out of range`**
You tried to access an index that doesn't exist. A 5-item list has indices 0–4. Accessing index 5 raises this error. Check `len()` and remember the last index is `len(list) - 1`.

**Confusing slicing with indexing**
`list[2]` returns one item. `list[1:3]` returns a list (even if it contains only one item).

**`TypeError: 'int' object is not subscriptable`**
You wrote `scores[0][1]` but `scores[0]` is just an integer, not a list. Use this syntax only when you have a list of lists or list of tuples.

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| **list** | An ordered, mutable collection of values |
| **index** | The position of an item in a list (starts at 0) |
| **negative index** | Counting from the end: `-1` = last item |
| **slicing** | Extracting a portion of a list using `[start:end:step]` |
| **mutable** | Can be changed after creation — lists are mutable, strings are not |
| **len()** | Returns the number of items in a list |
| **max() / min() / sum()** | Built-in functions for lists of numbers |
