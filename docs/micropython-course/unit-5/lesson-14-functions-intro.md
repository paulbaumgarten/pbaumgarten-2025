---
title: "Lesson 14 - Writing Your Own Functions"
layout: default
nav_order: 1
parent: "Unit 5: Functions and Modularity"
grand_parent: MicroPython
---

# Lesson 14 — Writing Your Own Functions
{: .no_toc }

**Estimated time:** 60 minutes

- TOC
{:toc}

---

## Learning Objectives

By the end of this lesson you will be able to:

1. Define a function using `def`
2. Call a function to run it
3. Explain why functions make code better
4. Write a set of reusable NeoPixel control functions

---

## Concepts

### What is a Function?

A **function** is a named, reusable block of code. Think of it as a recipe — you write the recipe once, then follow it as many times as you want without rewriting it.

You've been using functions all along: `print()`, `len()`, `input()`, `time.sleep()` — these are all built-in functions. Now you'll write your own.

**Why functions?**

1. **Avoid repetition** — the DRY principle: "Don't Repeat Yourself". If you find yourself copy-pasting code, it should probably be a function.
2. **Readability** — `flash_red()` is much easier to understand than 6 lines of LED code.
3. **Maintainability** — fix a bug in one function and it's fixed everywhere that function is used.

### Defining a Function

```python
def function_name():
    # function body
    # (indented code that runs when called)
```

- `def` keyword — tells Python you're defining a function
- `function_name` — the name you give it (same naming rules as variables)
- `():` — empty parentheses and colon (we'll add parameters in Lesson 15)
- Indented body — the code that runs when the function is called

**Nothing happens until you call it!** Defining a function just writes the recipe. Calling it actually executes it.

### Calling a Function

```python
# Define first:
def say_hello():
    print("Hello!")
    print("Welcome to my program.")

# Then call (can call multiple times):
say_hello()   # Runs the function
say_hello()   # Runs it again
say_hello()   # And again — same code, no repetition
```

### Docstrings

A **docstring** is a string immediately after the `def` line that describes what the function does. It's optional but good practice:

```python
def flash_led():
    """Flash the LED red once."""
    # ... code here ...
```

### Functions Calling Functions

Functions can call other functions — building up complexity from simple pieces:

```python
def led_on():
    np[0] = (255, 0, 0)
    np.write()

def led_off():
    np[0] = (0, 0, 0)
    np.write()

def flash():
    led_on()
    time.sleep(0.3)
    led_off()
    time.sleep(0.3)

def triple_flash():
    flash()   # Calls flash(), which calls led_on() and led_off()
    flash()
    flash()
```

This is called **composition** — building complex behaviour from simple functions.

---

## Guided Walkthrough

### Step 1: Your First Function

```python
def greet():
    """Print a friendly greeting."""
    print("Hello!")
    print("Welcome to MicroPython.")
    print("Let's write some code!")

# Call it three times:
greet()
greet()
greet()
```

Notice how much cleaner this is than copying those 3 print statements three times.

### Step 2: Refactoring Repetitive Code

**Without functions (messy):**
```python
import machine, neopixel, time
pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

np[0] = (255, 0, 0); np.write(); time.sleep(0.5); np[0] = (0,0,0); np.write(); time.sleep(0.5)
np[0] = (255, 0, 0); np.write(); time.sleep(0.5); np[0] = (0,0,0); np.write(); time.sleep(0.5)
np[0] = (255, 0, 0); np.write(); time.sleep(0.5); np[0] = (0,0,0); np.write(); time.sleep(0.5)
```

**With functions (clean):**
```python
import machine, neopixel, time

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

def flash_red():
    """Flash the LED red once."""
    np[0] = (255, 0, 0)
    np.write()
    time.sleep(0.5)
    np[0] = (0, 0, 0)
    np.write()
    time.sleep(0.5)

flash_red()
flash_red()
flash_red()
```

If you want to change the flash timing, you only change it in **one place**.

### Step 3: LED Toolkit — Functions for Common Actions

```python
import machine, neopixel, time

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

def led_on(r, g, b):
    """Turn LED on with RGB colour."""
    np[0] = (r, g, b)
    np.write()

def led_off():
    """Turn LED off."""
    np[0] = (0, 0, 0)
    np.write()

def flash(r, g, b, times=3, delay=0.3):
    """Flash LED a number of times. times and delay have defaults."""
    for _ in range(times):
        led_on(r, g, b)
        time.sleep(delay)
        led_off()
        time.sleep(delay)

# Using the toolkit:
flash(255, 0, 0)           # Flash red 3 times (defaults)
time.sleep(0.5)
flash(0, 255, 0, times=5)  # Flash green 5 times
time.sleep(0.5)
flash(0, 0, 255, times=2, delay=0.1)  # Fast blue flashes
```

**Default parameters:** `times=3` means "if no `times` is given, use 3". You'll learn more about this in Lesson 15.

### Step 4: Functions Calling Functions

```python
def alert():
    """Urgent alert pattern."""
    flash(255, 0, 0, times=5, delay=0.1)   # Rapid red flashes
    led_on(255, 0, 0)                        # Hold red
    time.sleep(1)
    led_off()

def standby():
    """Calm standby pattern — slow green pulse."""
    for brightness in range(0, 100, 5):
        led_on(0, brightness, 0)
        time.sleep(0.04)
    for brightness in range(100, -1, -5):
        led_on(0, brightness, 0)
        time.sleep(0.04)
    led_off()

def startup_sequence():
    """Run startup: breathe green, then alert."""
    print("Starting up...")
    standby()
    time.sleep(0.5)
    print("Alert!")
    alert()
    print("Done.")

startup_sequence()
```

---

## Challenges

### ⭐ Core
Write three functions: `show_red()`, `show_green()`, `show_blue()` — each shows that colour for 1 second and turns off. Then write a `show_rainbow()` function that calls them in order with short pauses. Call `show_rainbow()` twice.

### ⭐⭐ Extension
Write `morse_dot()` (short flash — 0.1s) and `morse_dash()` (long flash — 0.3s) functions. Use them to spell SOS in Morse code: `... --- ...` (S=dot dot dot, O=dash dash dash).

### ⭐⭐⭐ Stretch
Write these functions: `police_lights(duration)` — alternating rapid red/blue flashes for `duration` seconds; `ambulance_lights(duration)` — rapid white flashes; `traffic_light_cycle(cycles)` — full red/amber/green sequence repeated `cycles` times. Create a `demo()` function that calls all three in a dramatic sequence. Comment each function with a docstring.

---

## Common Mistakes & Debugging

**Defining a function but never calling it**
Nothing happens! `def my_function():` just defines it. You must call `my_function()` to run it.

**Calling before defining**
Python reads top to bottom. If you call `my_function()` on line 5 but define `def my_function():` on line 10, you'll get a `NameError`. Define functions before calling them.

**Forgetting the parentheses when calling**
`my_function` (no brackets) refers to the function *object* itself. `my_function()` (with brackets) *runs* it.

**Indentation errors in the function body**
All code inside the function must be indented the same amount.

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| **function** | A named, reusable block of code |
| **def** | The keyword used to define a function |
| **call** | Executing a function by writing its name followed by `()` |
| **DRY** | "Don't Repeat Yourself" — use functions instead of copying code |
| **function body** | The indented code inside the function that runs when called |
| **docstring** | A string at the top of a function body describing what it does |
| **default parameter** | A parameter with a pre-set value used when no argument is provided |
| **composition** | Building complex functions by calling simpler functions |
