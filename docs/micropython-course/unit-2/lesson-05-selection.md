---
title: "Lesson 5 - Selection with if and else"
layout: default
nav_order: 1
parent: "Unit 2: Making Decisions"
grand_parent: MicroPython Course
---

# Lesson 5 — Selection with if and else
{: .no_toc }

**Estimated time:** 60 minutes

- TOC
{:toc}

---

## Learning Objectives

By the end of this lesson you will be able to:

1. Use `if` and `else` to make a program choose between two paths
2. Write comparison operators correctly: `==`, `!=`, `<`, `>`, `<=`, `>=`
3. Understand why indentation is critical in Python
4. Change the NeoPixel colour based on a condition

---

## Concepts

### What is Selection?

**Selection** is a programming concept where the program chooses between different paths depending on a condition. Think of it like a roundabout — depending on where you're heading, you take a different exit.

Without selection, every program runs the same way every time. With selection, your program can respond to different situations.

### The `if` Statement

An `if` statement checks a condition. If the condition is `True`, it runs the indented block underneath. If `False`, it skips that block.

```python
temperature = 30

if temperature > 25:
    print("It's hot!")
    print("Drink some water.")

print("This always runs.")   # Not indented — always executes
```

**Structure:**
```
if condition:
    code to run if True
    (can be multiple lines)
```

The colon `:` at the end of the `if` line is **required**.
The code inside the block must be **indented** — use 4 spaces or 1 Tab consistently.

### The `else` Clause

`else` provides an alternative block that runs when the `if` condition is `False`:

```python
score = 45

if score >= 50:
    print("You passed!")
else:
    print("Not quite — keep trying!")
```

Exactly one of these blocks will run — never both, never neither.

### Indentation — The Critical Rule

In Python, **indentation** (the spaces at the start of a line) defines what code belongs inside a block. Getting indentation wrong causes `IndentationError`.

```python
# CORRECT:
if x > 0:
    print("Positive")
    print("This is also inside the if")
print("This is outside — always runs")

# WRONG (will cause IndentationError):
if x > 0:
print("This isn't indented — Python won't understand this")
```

Thonny automatically indents for you after a `:`. If you press Backspace at the start of a line, it removes one level of indentation.

### Comparison Operators

These operators compare two values and produce `True` or `False`:

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `<` | Less than | `3 < 5` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<=` | Less than or equal | `5 <= 5` | `True` |
| `>=` | Greater than or equal | `6 >= 5` | `True` |

{: .important }
**`=` vs `==`**: `=` assigns a value to a variable. `==` checks if two values are equal. These are completely different! `if x = 5:` is an error. `if x == 5:` is correct.

### Nested `if` Statements

You can put an `if` inside another `if`:

```python
score = 85

if score >= 50:
    print("You passed!")
    if score >= 80:
        print("Excellent — that's a distinction!")
else:
    print("Better luck next time.")
```

---

## Guided Walkthrough

### Step 1: Basic `if/else` in the REPL

Try this in the Shell:

```python
>>> x = 10
>>> if x > 5:
...     print("x is greater than 5")
... else:
...     print("x is 5 or less")
...
x is greater than 5
```

(In the REPL, the `...` prompt means "continue this block". Press Enter on a blank line to finish.)

### Step 2: Comparison Operators

```python
x = 10
print(x == 10)   # True
print(x == 5)    # False
print(x != 5)    # True
print(x > 5)     # True
print(x < 5)     # False
print(x >= 10)   # True
print(x <= 9)    # False
```

### Step 3: Score-Based LED Feedback

```python
import machine, neopixel, time

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

score = int(input("Enter your score (0-100): "))

if score >= 50:
    np[0] = (0, 255, 0)    # Green = pass
    np.write()
    print(f"Score: {score} — PASS!")
else:
    np[0] = (255, 0, 0)    # Red = fail
    np.write()
    print(f"Score: {score} — Not quite. Keep trying!")

time.sleep(3)
np[0] = (0, 0, 0)
np.write()
```

Try entering different scores and see the LED change.

### Step 4: Nested `if` for Multiple Levels

```python
import machine, neopixel, time

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

score = int(input("Enter your score (0-100): "))

if score >= 50:
    print("You passed!")
    if score >= 90:
        np[0] = (255, 215, 0)  # Gold — outstanding
        print("Outstanding — gold award!")
    elif score >= 70:
        np[0] = (0, 0, 255)    # Blue — merit
        print("Merit level!")
    else:
        np[0] = (0, 255, 0)    # Green — pass
        print("Good pass!")
else:
    np[0] = (255, 0, 0)        # Red — fail
    print("You didn't pass this time.")

np.write()
time.sleep(3)
np[0] = (0, 0, 0)
np.write()
```

---

## Challenges

### ⭐ Core
Ask the user to enter a number. If the number is **even** (hint: `number % 2 == 0`), show green on the LED and print "Even". If odd, show blue and print "Odd".

### ⭐⭐ Extension
Ask for a temperature in Celsius. Display:
- Blue if below 10°C and print "Cold!"
- Green if between 10 and 25°C and print "Comfortable"
- Red if above 25°C and print "Hot!"

### ⭐⭐⭐ Stretch
Create a simple password checker. Define a correct password in your code. Ask the user to enter a password. If correct, show green and print "Access granted". If wrong, show red and print "Access denied" along with how many characters they typed. Also check: if the password is shorter than 8 characters, show yellow and print a warning about short passwords (check the length before checking if it's correct).

---

## Common Mistakes & Debugging

**`SyntaxError` on the `if` line**
Most likely you used `=` instead of `==`: `if x = 5:` should be `if x == 5:`.

**`IndentationError: expected an indented block`**
After `if ...:` the next line must be indented. Thonny does this automatically when you press Enter after the colon.

**`IndentationError: unexpected indent`**
A line is indented but shouldn't be. Check that all lines meant to be inside the block have the same indentation.

**Forgetting the colon `:`**
`if x > 5` (no colon) gives `SyntaxError`. Always end `if`, `else`, `elif` lines with `:`.

**Both branches seem to run**
Check your indentation — code after the `if` block that runs regardless may look like it's inside `else` but isn't.

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| **selection** | A programming construct that chooses between different code paths |
| **if statement** | Runs a block of code only if a condition is `True` |
| **else** | The block that runs when the `if` condition is `False` |
| **condition** | An expression that evaluates to `True` or `False` |
| **comparison operator** | Compares two values: `==`, `!=`, `<`, `>`, `<=`, `>=` |
| **indentation** | Spaces at the start of a line that define code blocks in Python |
| **boolean** | A `True` or `False` value — what conditions evaluate to |
| **nested** | A structure placed inside another of the same kind (e.g., `if` inside `if`) |
