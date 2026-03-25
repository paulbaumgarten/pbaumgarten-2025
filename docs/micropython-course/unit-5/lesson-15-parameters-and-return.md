---
title: "Lesson 15 - Parameters and Return Values"
layout: default
nav_order: 2
parent: "Unit 5: Functions and Modularity"
grand_parent: MicroPython Course
---

# Lesson 15 — Parameters and Return Values
{: .no_toc }

**Estimated time:** 75 minutes

- TOC
{:toc}

---

## Learning Objectives

By the end of this lesson you will be able to:

1. Pass data into functions using parameters
2. Get results back from functions using `return`
3. Use return values in expressions and conditions
4. Distinguish between functions that do things vs functions that calculate things

---

## Concepts

### Parameters and Arguments

A **parameter** is a variable in the function definition that holds the passed-in value. An **argument** is the actual value you pass when calling.

```python
def greet(name):        # 'name' is a parameter
    print(f"Hello, {name}!")

greet("Alice")          # "Alice" is an argument
greet("Bob")            # "Bob" is an argument
```

**Multiple parameters:**
```python
def introduce(first_name, last_name, age):
    print(f"Name: {first_name} {last_name}, Age: {age}")

introduce("Alex", "Smith", 15)
```

**Default parameters:**
```python
def flash(colour, times=3, delay=0.3):
    # If times or delay aren't passed, use the defaults
    ...

flash((255, 0, 0))              # Uses times=3, delay=0.3
flash((0, 255, 0), times=5)     # Uses delay=0.3
flash((0, 0, 255), 2, 0.1)      # All three provided
```

Default parameters must come *after* non-default ones.

### Return Values

A `return` statement sends a value back to whoever called the function:

```python
def add(a, b):
    result = a + b
    return result

total = add(5, 3)    # total gets the value 8
print(total)         # 8
print(add(10, 20))   # 30 — use return value directly
```

**Three ways to use a return value:**
```python
# 1. Store in a variable
area = calculate_area(5, 3)

# 2. Use directly in an expression
print(calculate_area(5, 3) * 2)

# 3. Use in a condition
if calculate_area(width, height) > 100:
    print("Large area!")
```

### None — The "No Value" Value

If a function has no `return` statement (or `return` with no value), it returns `None`:

```python
def just_print():
    print("hello")

result = just_print()
print(result)   # None
```

`None` is Python's way of saying "nothing was returned". It's not an error — it's a valid value meaning "no value".

### Two Types of Functions

**"Do something" functions** (no return): perform actions (light an LED, print, write a file):
```python
def flash_red():
    np[0] = (255, 0, 0)
    np.write()
    time.sleep(0.3)
    np[0] = (0, 0, 0)
    np.write()
```

**"Calculate something" functions** (with return): take inputs, compute, return a result:
```python
def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

temp_f = celsius_to_fahrenheit(25)  # 77.0
```

Good functions tend to do *one thing* — either perform an action or calculate a value.

---

## Guided Walkthrough

### Step 1: Functions with Parameters

```python
def greet(name):
    print(f"Hello, {name}! Great to meet you.")

greet("Alex")
greet("MicroPython")
greet("the ESP32-S3")
```

### Step 2: Return Values

```python
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def average(numbers):
    return sum(numbers) / len(numbers)

# Use return values
print(add(5, 3))           # 8
print(multiply(6, 7))      # 42
print(add(5, 3) * 2)       # 16 — use return value in expression

scores = [85, 72, 91, 68]
avg = average(scores)
print(f"Average: {avg:.1f}")

if average(scores) >= 75:
    print("Class average is good!")
```

### Step 3: NeoPixel Functions with Parameters and Returns

```python
import machine, neopixel, time

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

def scale_colour(r, g, b, brightness):
    """Scale an RGB colour by brightness factor (0.0 to 1.0)."""
    return (int(r * brightness), int(g * brightness), int(b * brightness))

def blend(colour1, colour2, amount):
    """
    Blend two colours. amount=0.0 gives colour1, 1.0 gives colour2.
    """
    r = int(colour1[0] * (1 - amount) + colour2[0] * amount)
    g = int(colour1[1] * (1 - amount) + colour2[1] * amount)
    b = int(colour1[2] * (1 - amount) + colour2[2] * amount)
    return (r, g, b)

def show_colour(colour, duration=1.0):
    """Display a colour for a given duration."""
    np[0] = colour
    np.write()
    time.sleep(duration)
    np[0] = (0, 0, 0)
    np.write()

# Fade from red to blue across 11 steps
red = (255, 0, 0)
blue = (0, 0, 255)

for step in range(11):
    amount = step / 10    # 0.0, 0.1, ..., 1.0
    colour = blend(red, blue, amount)
    np[0] = colour
    np.write()
    print(f"Step {step}: {colour}")
    time.sleep(0.2)

np[0] = (0, 0, 0)
np.write()
```

### Step 4: A Clean Distance Function (Building on Lesson 13)

```python
from machine import Pin
import time

def get_distance(trig, echo):
    """
    Measure distance using HC-SR04.
    Parameters: trig (Pin, output), echo (Pin, input)
    Returns: distance in cm (float), or -1 if no reading
    """
    trig.off()
    time.sleep_us(2)
    trig.on()
    time.sleep_us(10)
    trig.off()

    timeout = time.ticks_us() + 30000
    while echo.value() == 0:
        if time.ticks_us() > timeout:
            return -1

    start = time.ticks_us()
    timeout = start + 30000
    while echo.value() == 1:
        if time.ticks_us() > timeout:
            return -1

    duration = time.ticks_diff(time.ticks_us(), start)
    return round(duration / 58.2, 1)

# Now the calling code is clean and readable:
trig = Pin(5, Pin.OUT)
echo = Pin(4, Pin.IN)

while True:
    dist = get_distance(trig, echo)
    if dist > 0:
        print(f"Distance: {dist} cm")
    time.sleep(0.5)
```

Notice how the messy timing code is hidden inside the function. The calling code is simple and readable.

### Step 5: Classify with Return

```python
def classify_distance(dist):
    """Returns a category string based on distance."""
    if dist < 0:
        return "invalid"
    elif dist < 10:
        return "very close"
    elif dist < 30:
        return "close"
    elif dist < 60:
        return "medium"
    else:
        return "far"

def colour_for_distance(dist):
    """Returns an RGB tuple based on distance category."""
    category = classify_distance(dist)
    if category == "very close":
        return (255, 0, 0)
    elif category == "close":
        return (255, 100, 0)
    elif category == "medium":
        return (255, 220, 0)
    elif category == "far":
        return (0, 255, 0)
    else:
        return (20, 20, 20)   # Dim for invalid

# Test
for test_dist in [-1, 5, 15, 45, 80]:
    cat = classify_distance(test_dist)
    colour = colour_for_distance(test_dist)
    print(f"{test_dist}cm → {cat} → {colour}")
```

---

## Challenges

### ⭐ Core
Write `is_even(n)` that returns `True` if n is even, `False` if odd. Write `classify_grade(score)` that returns "A" (≥80), "B" (≥70), "C" (≥60), "D" (≥50), or "F" (<50). Test both with at least 5 different inputs each.

### ⭐⭐ Extension
Write `brightness_from_distance(distance, max_dist)` that returns a brightness value 0–255 where closer = brighter and `max_dist` or beyond = 0. Use this to make the LED brightness track the ultrasonic sensor distance.

### ⭐⭐⭐ Stretch
Write these functions and test them:
- `rgb_to_hex(r, g, b)` — returns a hex colour string like `"#FF8000"`
- `hex_to_rgb(hex_str)` — parses `"#FF8000"` and returns `(255, 128, 0)` (reverse of above)
- `complementary(r, g, b)` — returns the complementary colour `(255-r, 255-g, 255-b)`
Verify: `hex_to_rgb(rgb_to_hex(r, g, b))` should equal `(r, g, b)`.

---

## Common Mistakes & Debugging

**Forgetting `return` — function returns `None`**
The function runs but gives nothing back. The variable you assign the result to will be `None`.

**Printing instead of returning**
`print()` displays to the screen. `return` sends a value back to the caller. A function that `print()`s its result can't be used in `result = my_function()`.

**Parameters vs global variables**
Inside `def greet(name):`, `name` is a *local* parameter — it's separate from any global variable also called `name`. They don't interfere.

**Return exits the function immediately**
Any code after `return` in the same block never runs. This can be used deliberately (early return) but can also be an accidental bug.

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| **parameter** | A variable in the function definition that receives the passed-in value |
| **argument** | The actual value passed to a function when calling it |
| **return** | Sends a value back from the function to the caller |
| **return value** | The value sent back by `return` |
| **None** | Python's "no value" — what a function returns if it has no `return` statement |
| **default parameter** | A parameter with a pre-set value used when no argument is provided |
| **void function** | A function that performs an action but doesn't return a meaningful value |
