---
title: "Lesson 7 - Logical Operators"
layout: default
nav_order: 3
parent: "Unit 2: Making Decisions"
grand_parent: MicroPython
---

# Lesson 7 — Logical Operators
{: .no_toc }

**Estimated time:** 60 minutes

- TOC
{:toc}

---

## Learning Objectives

By the end of this lesson you will be able to:

1. Use `and`, `or`, `not` to combine multiple conditions
2. Read and use truth tables
3. Combine two buttons for richer control
4. Build complex, real-world conditions

---

## Concepts

### Logical Operators

**Logical operators** combine multiple conditions into one:

- **`and`** — True only if BOTH sides are True
  - "I'll go to the park if it's sunny AND it's not raining."
- **`or`** — True if EITHER side is True (or both)
  - "I'll stay home if I'm tired OR it's raining."
- **`not`** — Flips True to False and False to True
  - "If NOT raining, I'll go outside."

### Truth Tables

A **truth table** shows all possible inputs and outputs for a logical operator:

**`and`:**

| A | B | A and B |
|---|---|---------|
| True | True | True |
| True | False | False |
| False | True | False |
| False | False | False |

**`or`:**

| A | B | A or B |
|---|---|--------|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | False |

**`not`:**

| A | not A |
|---|-------|
| True | False |
| False | True |

### Precedence of Logical Operators

`not` is applied first, then `and`, then `or`. Use brackets to be explicit:

```python
# Without brackets (can be confusing):
if a or b and c:    # Means: a or (b and c)

# With brackets (clear):
if a or (b and c):  # Same, but readable
if (a or b) and c:  # Different meaning!
```

When in doubt, add brackets. It doesn't hurt and makes your intent clear.

### Common Mistake: `if x == 1 or 2`

This is a classic mistake:

```python
# WRONG:
if x == 1 or 2:     # Python reads: (x == 1) or (2)
                    # (2) is always True! This condition is always True.

# CORRECT:
if x == 1 or x == 2:  # Both comparisons are explicit
```

### Combining Buttons

With two buttons (A on GPIO 0, B on GPIO 14), you can detect four states:

```python
a_pressed = button_a.value() == 0
b_pressed = button_b.value() == 0

if a_pressed and b_pressed:
    print("Both pressed!")
elif a_pressed and not b_pressed:
    print("Only A")
elif b_pressed and not a_pressed:
    print("Only B")
else:
    print("Neither")
```

---

## Hardware Setup

Add a second button:

| Button B Leg | Connect To |
|-------------|-----------|
| Leg 1 | GPIO 14 |
| Leg 2 | GND |

---

## Guided Walkthrough

### Step 1: `and`, `or`, `not` in the REPL

```python
>>> True and True
True
>>> True and False
False
>>> False or True
True
>>> False or False
False
>>> not True
False
>>> not False
True
>>> x = 10
>>> x > 5 and x < 20
True
>>> x > 5 and x < 8
False
>>> x < 5 or x > 8
True
```

### Step 2: Combining Conditions for the LED

```python
import machine, neopixel

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

temp = int(input("Temperature (°C): "))
humidity = int(input("Humidity (%): "))

# Comfortable: 18–25°C AND humidity 40–60%
if 18 <= temp <= 25 and 40 <= humidity <= 60:
    np[0] = (0, 255, 0)     # Green — comfortable
    print("Comfortable conditions!")
elif temp > 30 or humidity > 80:
    np[0] = (255, 0, 0)     # Red — uncomfortable
    print("Uncomfortable — too hot or too humid!")
else:
    np[0] = (255, 200, 0)   # Yellow — acceptable but not ideal
    print("Acceptable, but not ideal.")

np.write()
```

Notice the **chained comparison**: `18 <= temp <= 25`. Python allows this! It means `18 <= temp AND temp <= 25`.

### Step 3: Two-Button LED Control

Wire both buttons (A = GPIO 0, B = GPIO 14), then run:

```python
import machine, neopixel, time
from machine import Pin

pin48 = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin48, 1)
button_a = Pin(0, Pin.IN, Pin.PULL_UP)
button_b = Pin(14, Pin.IN, Pin.PULL_UP)

print("Button controls:")
print("  A only = Red")
print("  B only = Blue")
print("  A + B  = Purple")
print("  None   = Off")
print("Ctrl+C to stop.")

while True:
    a = button_a.value() == 0   # True if pressed
    b = button_b.value() == 0

    if a and b:
        np[0] = (128, 0, 255)   # Purple
    elif a and not b:
        np[0] = (255, 0, 0)     # Red
    elif b and not a:
        np[0] = (0, 0, 255)     # Blue
    else:
        np[0] = (0, 0, 0)       # Off

    np.write()
    time.sleep(0.05)
```

Try all four combinations: neither button, only A, only B, both together.

### Step 4: Complex Real-World Conditions

```python
# Simulate a security door access system
name = input("Enter name: ")
pin_code = input("Enter PIN: ")
is_vip = False   # Could be True for VIP users

has_name = name.lower() in ["alice", "bob", "charlie"]
has_correct_pin = pin_code == "1234"
time_is_okay = True   # Imagine this checks business hours

# Access rule:
# - VIP OR (correct name AND correct pin) AND it's business hours
if (is_vip or (has_name and has_correct_pin)) and time_is_okay:
    print("Access GRANTED")
else:
    print("Access DENIED")
    if not has_name:
        print("  — Name not on list")
    if not has_correct_pin:
        print("  — Wrong PIN")
```

{: .highlight }
**Did you know?** The `and`, `or`, `not` operators you're learning here are the same operations used in electronic circuit design. A computer's CPU is built from billions of tiny circuits called logic gates that each perform AND, OR, and NOT operations.

---

## Challenges

### ⭐ Core
Write a "safe driving" alert system. Ask for current speed (as an int) and whether it's raining (enter "yes" or "no"). Print a warning if: `speed > 120` OR `(speed > 80 and it's raining)`. Otherwise print "Driving safely".

### ⭐⭐ Extension
Create a password system that requires **both** a correct numeric PIN (4 digits) **and** a correct keyword. If either is wrong, print which one failed. Only turn the LED green if both are correct.

### ⭐⭐⭐ Stretch
Using two buttons, implement a "combination lock":
- The lock opens ONLY if button A is pressed, fully released, then button B is pressed
- Any other sequence (both at once, B first, etc.) keeps it locked
- Show green when unlocked, red when locked
- After unlocking, it automatically re-locks after 3 seconds

---

## Common Mistakes & Debugging

**`if a == 1 or 2:` is always True**
Python evaluates this as `(a == 1) or (2)`. The value `2` is truthy — it's always `True`. Write `if a == 1 or a == 2:`.

**`not` applies to one value by default**
`not a and b` means `(not a) and b`. If you want `not (a and b)`, use brackets.

**Confusing `and` and `or`**
Use the English translation as a check: "`a and b`" means "both A AND B must be true". If your sentence uses "or", use `or`.

**Short-circuit evaluation**
Python doesn't always evaluate the right side of `and`/`or`. With `a and b`, if `a` is False, Python skips `b` entirely. This matters if `b` has a side effect or could error.

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| **logical operator** | `and`, `or`, `not` — combines boolean conditions |
| **truth table** | A table showing all possible inputs and the resulting output of a logical operation |
| **and** | True only if both conditions are True |
| **or** | True if at least one condition is True |
| **not** | Flips True to False and False to True |
| **chained comparison** | `18 <= x <= 25` — Python's shorthand for `x >= 18 and x <= 25` |
| **short-circuit evaluation** | Python stops evaluating `and` if the left side is False; stops evaluating `or` if the left side is True |
