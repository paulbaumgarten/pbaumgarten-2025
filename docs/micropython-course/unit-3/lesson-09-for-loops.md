---
title: "Lesson 9 - For Loops and range()"
layout: default
nav_order: 2
parent: "Unit 3: Loops and Repetition"
grand_parent: MicroPython
---

# Lesson 9 — For Loops and range()
{: .no_toc }

**Estimated time:** 75 minutes

- TOC
{:toc}

---

## Learning Objectives

By the end of this lesson you will be able to:

1. Use a `for` loop to iterate through a sequence
2. Use `range()` with one, two, and three arguments
3. Create nested for loops for complex patterns
4. Know when to use `for` vs `while`

---

## Concepts

### The `for` Loop

A `for` loop iterates through a **sequence**, running the loop body once for each item. The loop variable takes each value in turn:

```python
for item in sequence:
    # code using item
```

**Iterating through a list:**
```python
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)
# Output: apple  banana  mango
```

**Using a loop variable that we don't need — `_`:**
```python
for _ in range(5):    # _ is the convention for "I don't need this value"
    print("Hello!")   # Prints "Hello!" 5 times
```

### `range()`

`range()` generates a sequence of numbers. It's the most common thing to iterate in a `for` loop:

| Call | Produces |
|------|---------|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 6)` | 1, 2, 3, 4, 5 |
| `range(0, 10, 2)` | 0, 2, 4, 6, 8 (step 2) |
| `range(10, 0, -1)` | 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 (count down) |
| `range(0, 256, 15)` | 0, 15, 30, 45, ... 255 (useful for LED brightness!) |

**Key rule:** `range(start, stop, step)` — includes `start`, goes up to **but not including** `stop`.

### `for` vs `while`

| Use `for` when... | Use `while` when... |
|-------------------|---------------------|
| You know exactly how many times | You're waiting for a condition to change |
| Iterating through a list/string | Waiting for a sensor value |
| Counting to a fixed number | "Keep going until..." |

### Nested Loops

A loop inside a loop. The **inner loop runs completely** for each single iteration of the outer loop:

```python
for row in range(3):
    for col in range(4):
        print(f"({row},{col})", end=" ")
    print()   # New line after inner loop completes
```

Output:
```
(0,0) (0,1) (0,2) (0,3)
(1,0) (1,1) (1,2) (1,3)
(2,0) (2,1) (2,2) (2,3)
```

### `enumerate()`

`enumerate()` gives you both the **index** and the **value** when iterating a list:

```python
colours = ["red", "green", "blue"]
for i, colour in enumerate(colours):
    print(f"Colour {i}: {colour}")
# Output:
# Colour 0: red
# Colour 1: green
# Colour 2: blue
```

---

## Guided Walkthrough

### Step 1: Basic `for` and `range()`

```python
# Count 0 to 4
for i in range(5):
    print(i)

print("---")

# Count 1 to 5
for i in range(1, 6):
    print(i)

print("---")

# Even numbers 0 to 10
for i in range(0, 11, 2):
    print(i)

print("---")

# Countdown
for i in range(10, 0, -1):
    print(i)
print("Blastoff!")
```

### Step 2: LED Colour Cycle

```python
import machine, neopixel, time

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

colours = [
    ("Red",     (255, 0, 0)),
    ("Orange",  (255, 100, 0)),
    ("Yellow",  (255, 200, 0)),
    ("Green",   (0, 255, 0)),
    ("Cyan",    (0, 200, 255)),
    ("Blue",    (0, 0, 255)),
    ("Purple",  (100, 0, 255)),
]

# Run 3 complete cycles
for cycle in range(3):
    print(f"Cycle {cycle + 1}:")
    for i, (name, colour) in enumerate(colours):
        np[0] = colour
        np.write()
        print(f"  {name}")
        time.sleep(0.4)

np[0] = (0, 0, 0)
np.write()
print("Done!")
```

### Step 3: Nested Loop — RGB Channels

```python
import machine, neopixel, time

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

channel_names = ["Red", "Green", "Blue"]

# For each colour channel, ramp up then down
for channel in range(3):    # 0=Red, 1=Green, 2=Blue
    print(f"Ramping {channel_names[channel]}...")

    # Ramp up: 0 to 255
    for brightness in range(0, 256, 15):
        colour = [0, 0, 0]
        colour[channel] = brightness
        np[0] = tuple(colour)
        np.write()
        time.sleep(0.03)

    # Ramp down: 255 to 0
    for brightness in range(255, -1, -15):
        colour = [0, 0, 0]
        colour[channel] = brightness
        np[0] = tuple(colour)
        np.write()
        time.sleep(0.03)

np[0] = (0, 0, 0)
np.write()
print("Channel sweep complete!")
```

**Explanation:** `colour` is a list `[0, 0, 0]`. We set `colour[channel]` to the brightness value (changing only the relevant channel), then use `tuple(colour)` to convert it to a tuple for the NeoPixel.

### Step 4: FizzBuzz with LED Feedback

FizzBuzz is a classic programming challenge: count 1 to 30, print "Fizz" for multiples of 3, "Buzz" for multiples of 5, "FizzBuzz" for multiples of both.

```python
import machine, neopixel, time

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

for i in range(1, 31):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i}: FizzBuzz!")
        np[0] = (0, 200, 200)    # Cyan — FizzBuzz
    elif i % 3 == 0:
        print(f"{i}: Fizz")
        np[0] = (0, 200, 0)      # Green — Fizz
    elif i % 5 == 0:
        print(f"{i}: Buzz")
        np[0] = (0, 0, 200)      # Blue — Buzz
    else:
        print(f"{i}")
        np[0] = (40, 40, 40)     # Dim white — regular number

    np.write()
    time.sleep(0.3)

np[0] = (0, 0, 0)
np.write()
```

### Step 5: Nested Loop — Multiplication Table

```python
print("Multiplication table (1–5):")
print()

for row in range(1, 6):
    for col in range(1, 6):
        result = row * col
        print(f"{result:4}", end="")   # :4 = minimum 4 chars wide
    print()   # New line after each row
```

---

## Challenges

### ⭐ Core
Write a `for` loop that counts from 1 to 100. Print only numbers divisible by 7. How many are there? Flash the LED red once for each divisible number found.

### ⭐⭐ Extension
Create a "beat pattern" using nested loops: 4 quick red flashes, then 1 long green flash, then 4 quick blue flashes, then 1 long green flash. Repeat this whole pattern 4 times. Use `for` loops throughout.

### ⭐⭐⭐ Stretch
Generate the first 20 Fibonacci numbers (0, 1, 1, 2, 3, 5, 8, 13...) using a `for` loop. For each number:
- Print it
- If it's a prime number, flash the LED blue once
- If it's divisible by 3, flash it green once
You'll need a helper condition to check for primes: a number `n` is prime if no number from 2 to `n-1` divides it evenly.

---

## Common Mistakes & Debugging

**`range(5)` starts at 0, not 1**
If you want 1 to 5, use `range(1, 6)`.

**`range(10, 0)` produces nothing**
To count down you need a step: `range(10, 0, -1)`.

**Modifying the loop variable inside the loop**
`for i in range(10): i = 5` — this doesn't change what `range` produces. The loop still runs 10 times with i = 0, 1, 2, ...

**Nested loop confusion**
The inner loop completes *all* its iterations before the outer loop moves to its next iteration.

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| **for loop** | Iterates through each item in a sequence, once per item |
| **range()** | Generates a sequence of numbers: `range(start, stop, step)` |
| **loop variable** | The variable that takes each value from the sequence (e.g., `i` in `for i in range(5)`) |
| **nested loop** | A loop inside another loop |
| **enumerate()** | Returns both the index and value when iterating a list |
| **`_`** | Conventional variable name when you don't need the loop variable's value |
