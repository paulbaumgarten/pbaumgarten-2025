---
title: "Lesson 4 - Expressions and Type Conversion"
layout: default
nav_order: 4
parent: "Unit 1: Getting Started"
grand_parent: MicroPython Course
---

# Lesson 4 — Expressions and Type Conversion
{: .no_toc }

**Estimated time:** 60 minutes

- TOC
{:toc}

---

## Learning Objectives

By the end of this lesson you will be able to:

1. Use arithmetic operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`
2. Understand operator precedence (order of operations)
3. Convert between data types using `int()`, `float()`, `str()`, `bool()`
4. Handle user input correctly (always comes as a string — convert it!)

---

## Concepts

### Arithmetic Operators

You already know `+`, `-`, `*`, `/`. Python has a few more:

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `7 + 3` | `10` |
| `-` | Subtraction | `7 - 3` | `4` |
| `*` | Multiplication | `7 * 3` | `21` |
| `/` | Division | `7 / 2` | `3.5` (always float!) |
| `//` | Integer division | `7 // 2` | `3` (drops decimal) |
| `%` | Modulo (remainder) | `7 % 2` | `1` (remainder after dividing) |
| `**` | Exponent (power) | `2 ** 8` | `256` |

{: .highlight }
**`/` always gives a float** in Python 3 and MicroPython — even `10 / 2` gives `5.0`, not `5`. If you want an integer result, use `//`.

**`%` (modulo)** is particularly useful in programming. It gives the *remainder* after division:
- `10 % 3 = 1` (10 ÷ 3 = 3 remainder 1)
- `15 % 5 = 0` (15 ÷ 5 = 3 remainder 0 — divisible!)
- Used to check if a number is even: `if n % 2 == 0:`

**`**` (power)** is useful for understanding colour depth: `2 ** 8 = 256`, which is why each colour channel goes 0–255 (256 possible values).

### Operator Precedence

Python follows **BIDMAS/BODMAS** — the same order of operations you learned in maths:

1. **B**rackets first: `(2 + 3) * 4 = 20`
2. **I**ndices (powers): `2 ** 3 = 8`
3. **D**ivision and **M**ultiplication (left to right)
4. **A**ddition and **S**ubtraction (left to right)

```python
print(2 + 3 * 4)    # 14 (multiply first, then add)
print((2 + 3) * 4)  # 20 (brackets first)
print(10 / 2 + 1)   # 6.0 (divide first, then add)
print(2 ** 3 + 1)   # 9 (power first: 8 + 1)
```

When in doubt, use brackets to make your intention clear.

### Type Conversion

Sometimes you need to convert a value from one type to another. Python provides built-in **conversion functions**:

| Function | Converts to | Example | Result |
|----------|------------|---------|--------|
| `int()` | Integer | `int("42")` | `42` |
| `int()` | Integer | `int(3.9)` | `3` (truncates!) |
| `float()` | Float | `float("3.14")` | `3.14` |
| `float()` | Float | `float(5)` | `5.0` |
| `str()` | String | `str(42)` | `"42"` |
| `str()` | String | `str(3.14)` | `"3.14"` |
| `bool()` | Boolean | `bool(0)` | `False` |
| `bool()` | Boolean | `bool(1)` | `True` |
| `bool()` | Boolean | `bool("")` | `False` (empty string) |
| `bool()` | Boolean | `bool("hi")` | `True` (non-empty) |

{: .important }
**`int()` truncates, it doesn't round.** `int(3.9)` gives `3`, not `4`. If you want rounding, use `round(3.9)` which gives `4`.

### Why Type Conversion Matters: `input()` Always Returns a String

This is crucial: **`input()` always returns a string**, even if the user types a number.

```python
age = input("Enter your age: ")   # User types: 16
print(type(age))                   # <class 'str'> — not int!
print(age + 1)                     # ERROR: can't add str and int
```

You must convert it:
```python
age = int(input("Enter your age: "))   # Convert immediately
print(age + 1)                          # Works: 17
```

---

## Guided Walkthrough

### Step 1: Try the Operators in the REPL

Click in the Thonny Shell and try each of these:

```python
>>> print(10 + 3)    # 13
>>> print(10 - 3)    # 7
>>> print(10 * 3)    # 30
>>> print(10 / 3)    # 3.3333...
>>> print(10 // 3)   # 3
>>> print(10 % 3)    # 1
>>> print(2 ** 8)    # 256
>>> print(2 ** 10)   # 1024
```

### Step 2: Operator Precedence

```python
# In the Script Editor:
print(2 + 3 * 4)       # 14 — multiplication first
print((2 + 3) * 4)     # 20 — brackets first
print(100 / 5 / 2)     # 10.0 — left to right
print(100 / (5 / 2))   # 40.0 — different!
print(3 ** 2 ** 2)     # 81 — powers go right to left: 3 ** (2**2) = 3**4 = 81
print((3 ** 2) ** 2)   # 81 — same here, but watch out in other cases
```

### Step 3: Type Conversion

```python
# Strings to numbers
print(int("42"))        # 42
print(float("3.14"))    # 3.14
print(int("10") + 5)    # 15

# Numbers to strings
print(str(42))          # "42"
print(str(3.14))        # "3.14"
print("Score: " + str(100))   # "Score: 100"

# Truncation vs rounding
print(int(9.9))         # 9 (not 10!)
print(round(9.9))       # 10
print(int(-3.7))        # -3 (towards zero)

# bool conversions
print(bool(0))     # False
print(bool(1))     # True
print(bool(-5))    # True (any non-zero is True)
print(bool(""))    # False (empty string)
print(bool("hi"))  # True
```

### Step 4: Converting `input()` — Essential Pattern

```python
# Always convert input() to the right type before doing maths
age_str = input("Enter your age: ")
age = int(age_str)   # Convert string to int
print(f"In 10 years you will be {age + 10}")
print(f"In 5 years you will be {age + 5}")
print(f"You were born around {2025 - age}")
```

Or do it in one line (more common):
```python
age = int(input("Enter your age: "))
```

### Step 5: LED Brightness Calculator

This program asks for a brightness percentage and converts it to the 0–255 range used by NeoPixels:

```python
import machine, neopixel, time

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

# Get percentage from user
percent = int(input("Enter LED brightness (0-100): "))

# Convert 0-100% to 0-255 range
# 100% = 255, 50% = 127, 0% = 0
brightness = int(255 * percent / 100)

print(f"Brightness: {percent}% = {brightness}/255")

# White at that brightness
np[0] = (brightness, brightness, brightness)
np.write()

time.sleep(3)
np[0] = (0, 0, 0)
np.write()
```

Notice: `255 * percent / 100` gives a float, so we use `int()` to convert it before using it as a colour value.

### Step 6: A Colour Mixer

```python
import machine, neopixel, time

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

print("Custom colour mixer!")
r = int(input("Red (0-255): "))
g = int(input("Green (0-255): "))
b = int(input("Blue (0-255): "))

# Clamp values to valid range (in case user enters out-of-range)
r = max(0, min(255, r))
g = max(0, min(255, g))
b = max(0, min(255, b))

np[0] = (r, g, b)
np.write()

total = r + g + b
average = total / 3
print(f"Colour: R={r}, G={g}, B={b}")
print(f"Total brightness sum: {total}")
print(f"Average brightness: {average:.1f}")   # :.1f = 1 decimal place

time.sleep(5)
np[0] = (0, 0, 0)
np.write()
```

Note the `:.1f` in the f-string — this formats the float to 1 decimal place. You'll see this pattern a lot.

---

## Challenges

### ⭐ Core
Write a program that asks for two numbers and prints their sum, difference, product, quotient (normal `/`), integer quotient (`//`), and remainder (`%`). Format the output neatly using f-strings.

### ⭐⭐ Extension
Ask for a number of seconds. Calculate and print: how many minutes and seconds that is (e.g., `150 seconds = 2 minutes 30 seconds`). Then calculate hours, minutes, and seconds (e.g., `3665 seconds = 1 hours 1 minutes 5 seconds`). Hint: use `//` and `%`.

### ⭐⭐⭐ Stretch
Ask the user to enter R, G, B values. Calculate:
- The total brightness (R+G+B) and average
- Whether the colour is "warm" (R > B), "cool" (B > R), or "neutral" (R == B)
- The complementary colour (subtract each value from 255: `comp_r = 255 - r`)
Display the original colour on the LED for 3 seconds, then the complementary colour for 3 seconds. Print both colours' details.

---

## Common Mistakes & Debugging

**`ValueError: invalid literal for int() with base 10: 'hello'`**
You tried `int("hello")` — can't convert non-numeric text to an int. Make sure the user entered a number.

**`ValueError: invalid literal for int() with base 10: '3.14'`**
You tried `int("3.14")` — use `float("3.14")` first, then `int()` if needed, or use `int(float("3.14"))`.

**`int()` doesn't round**
`int(3.9)` gives `3`, not `4`. Use `round(3.9)` to get `4`.

**Forgetting to convert `input()`**
`age = input("Age: ")` then `age + 1` gives `TypeError`. Always convert: `age = int(input("Age: "))`.

**`ZeroDivisionError`**
`10 / 0` or `10 // 0` — you can't divide by zero! Check your divisor isn't zero before dividing.

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| **expression** | A piece of code that produces a value (e.g., `2 + 3`, `len("hi")`) |
| **operator** | A symbol that performs an operation (`+`, `-`, `*`, `/`, `//`, `%`, `**`) |
| **integer division (`//`)** | Division that drops the decimal part, always giving an int |
| **modulo (`%`)** | The remainder after integer division |
| **exponent (`**`)** | Raises a number to a power: `2 ** 8 = 256` |
| **operator precedence** | The order in which operators are applied (BIDMAS) |
| **type conversion** | Changing a value from one data type to another |
| **int()** | Converts a value to an integer (truncates floats — does not round) |
| **float()** | Converts a value to a float |
| **str()** | Converts a value to a string |
| **truncate** | Remove the decimal part of a number (towards zero, not rounded) |
