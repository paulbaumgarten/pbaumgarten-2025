---
title: "Lesson 12 - List Operations and Methods"
layout: default
nav_order: 2
parent: "Unit 4: Collections of Data"
grand_parent: MicroPython Course
---

# Lesson 12 — List Operations and Methods
{: .no_toc }

**Estimated time:** 60 minutes

- TOC
{:toc}

---

## Learning Objectives

By the end of this lesson you will be able to:

1. Add items with `.append()` and `.insert()`
2. Remove items with `.remove()` and `.pop()`
3. Search a list using the `in` operator and `.index()`
4. Sort lists with `.sort()` and `sorted()`
5. Build a dynamic list that grows as data is collected

---

## Concepts

### Adding Items

**`.append(value)`** — adds an item to the **end** of a list:
```python
shopping = ["bread", "milk"]
shopping.append("eggs")
print(shopping)   # ["bread", "milk", "eggs"]
```

**`.insert(index, value)`** — adds an item at a **specific position**:
```python
shopping.insert(1, "butter")  # Insert at index 1
print(shopping)   # ["bread", "butter", "milk", "eggs"]
```

### Removing Items

**`.remove(value)`** — removes the **first occurrence** of a value:
```python
shopping.remove("milk")   # Removes "milk"
```
⚠️ Raises `ValueError` if the item isn't in the list! Check first with `in`.

**`.pop(index)`** — removes and **returns** the item at an index:
```python
last = shopping.pop()       # Remove last item, return it
item = shopping.pop(0)      # Remove first item, return it
```

### Searching

**`in` operator** — checks if a value is in a list:
```python
fruits = ["apple", "banana", "mango"]
print("banana" in fruits)    # True
print("grape" in fruits)     # False

if "apple" in fruits:
    print("Apple is available!")
```

**`.index(value)`** — returns the index of the first occurrence:
```python
print(fruits.index("banana"))   # 1
```
⚠️ Raises `ValueError` if not found! Check with `in` first.

**`.count(value)`** — counts how many times a value appears:
```python
nums = [1, 2, 3, 2, 1, 2]
print(nums.count(2))   # 3
```

### Sorting

**`.sort()`** — sorts the list **in place** (modifies the original):
```python
scores = [45, 87, 23, 91, 56]
scores.sort()                  # Ascending
print(scores)   # [23, 45, 56, 87, 91]

scores.sort(reverse=True)      # Descending
print(scores)   # [91, 87, 56, 45, 23]
```

**`sorted(list)`** — returns a **new** sorted list, leaving the original unchanged:
```python
original = [45, 87, 23]
sorted_copy = sorted(original)
print(original)      # [45, 87, 23]  — unchanged!
print(sorted_copy)   # [23, 45, 87]
```

**Rule:** Use `.sort()` when you want to modify the list in place. Use `sorted()` when you need to keep the original.

### Building Lists Dynamically

Start with an empty list `[]`, then use `.append()` as you go:

```python
readings = []   # Start empty

for i in range(5):
    value = int(input(f"Enter reading {i+1}: "))
    readings.append(value)

print("All readings:", readings)
print("Average:", sum(readings) / len(readings))
```

---

## Guided Walkthrough

### Step 1: append, insert, remove, pop

```python
# Start with a list
shopping = ["apples", "bread", "milk"]
print("Start:", shopping)

shopping.append("eggs")
print("After append:", shopping)

shopping.insert(1, "butter")   # Insert at position 1
print("After insert:", shopping)

shopping.remove("bread")
print("After remove:", shopping)

removed = shopping.pop()        # Remove last
print(f"Popped: '{removed}'")
print("After pop:", shopping)
```

### Step 2: Searching

```python
fruits = ["apple", "banana", "cherry", "apple", "mango"]

print("banana" in fruits)        # True
print("grape" in fruits)         # False
print(fruits.index("cherry"))    # 2
print(fruits.count("apple"))     # 2

# Safe search pattern
search = "cherry"
if search in fruits:
    pos = fruits.index(search)
    print(f"Found '{search}' at index {pos}")
else:
    print(f"'{search}' not in list")
```

### Step 3: Sorting

```python
scores = [45, 87, 23, 91, 56, 78, 34]
print("Original:", scores)

sorted_scores = sorted(scores)    # New sorted copy
print("Sorted copy:", sorted_scores)
print("Original unchanged:", scores)

scores.sort(reverse=True)         # Sort in place, descending
print("In-place descending:", scores)

names = ["Charlie", "Alice", "Diana", "Bob"]
print("Names sorted:", sorted(names))   # Alphabetical
```

### Step 4: Dynamic Sensor Reading Log

This simulates collecting readings and analysing them:

```python
import machine, neopixel, time
import random

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

readings = []
print("Simulating 15 sensor readings...")

for i in range(15):
    # Simulate a reading (replace with actual sensor later)
    reading = random.randint(10, 100)
    readings.append(reading)
    print(f"Reading {i+1:2d}: {reading}")
    time.sleep(0.2)

print(f"\n--- Analysis of {len(readings)} readings ---")
print(f"Min:     {min(readings)}")
print(f"Max:     {max(readings)}")
print(f"Average: {sum(readings)/len(readings):.1f}")

sorted_readings = sorted(readings)
print(f"Sorted:  {sorted_readings}")

# Visual feedback
avg = sum(readings) / len(readings)
if avg > 70:
    np[0] = (255, 0, 0)    # Red — high
    print("HIGH average")
elif avg > 40:
    np[0] = (255, 150, 0)  # Orange — medium
    print("MEDIUM average")
else:
    np[0] = (0, 255, 0)    # Green — low
    print("LOW average")

np.write()
time.sleep(3)
np[0] = (0, 0, 0)
np.write()
```

### Step 5: Top-5 High Scores List

```python
import random

high_scores = []

for round_num in range(10):
    score = random.randint(0, 100)
    print(f"Round {round_num+1}: scored {score}")

    # Insert in sorted order
    high_scores.append(score)
    high_scores.sort(reverse=True)

    # Keep only top 5
    if len(high_scores) > 5:
        high_scores.pop()   # Remove last (lowest)

    print(f"  Top scores so far: {high_scores}")

print("\nFinal top 5:", high_scores)
```

---

## Challenges

### ⭐ Core
Ask the user to enter 5 numbers one at a time. Store them in a list. Then print: the sorted list (ascending), the maximum, the minimum, and whether the number 42 is in the list.

### ⭐⭐ Extension
Create a "to-do list" manager using a `while True` loop. Each iteration, ask the user to type "add", "remove", "show", or "done". Implement each command. When "done" is typed, print the final list and exit. Handle errors gracefully (e.g., trying to remove something that isn't in the list).

### ⭐⭐⭐ Stretch
Simulate a leaderboard: run 20 "game rounds" with random scores (0–100). After each round, maintain a "top 5 leaderboard" list (sorted, max 5 items). If the new score makes the leaderboard, flash the LED green; otherwise red. After all 20 rounds, print the final leaderboard. Also track: how many times a score made the leaderboard, and the average of the final top-5.

---

## Common Mistakes & Debugging

**`ValueError: list.remove(x): x not in list`**
You tried to remove something that isn't there. Use `if value in my_list:` to check first.

**`.sort()` vs `sorted()` confusion**
`.sort()` modifies the original, returns `None`. Don't write `x = my_list.sort()` — `x` will be `None`. Use `x = sorted(my_list)` if you need a new list.

**`max()` on an empty list raises `ValueError`**
Check `if len(readings) > 0:` before calling `max()`, `min()`, or `sum()`.

**Forgetting that `.pop()` also returns the value**
`x = my_list.pop()` both removes the last item AND stores it in `x`. If you just want to delete: `my_list.pop()` without assignment is fine.

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| **append()** | Adds an item to the end of a list |
| **insert()** | Adds an item at a specific index |
| **remove()** | Removes the first occurrence of a value |
| **pop()** | Removes and returns the item at a given index (default: last) |
| **in operator** | Checks whether a value exists in a list — returns True or False |
| **sort()** | Sorts a list in place (modifies the original) |
| **sorted()** | Returns a new sorted list without changing the original |
| **dynamic list** | A list that grows over time by appending items |
