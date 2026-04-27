---
title: "Lesson 6 - Buttons and elif"
layout: default
nav_order: 2
parent: "Unit 2: Making Decisions"
grand_parent: MicroPython
---

# Lesson 6 — Buttons and elif
{: .no_toc }

**Estimated time:** 75 minutes

- TOC
{:toc}

---

## Learning Objectives

By the end of this lesson you will be able to:

1. Wire a push button to the ESP32-S3
2. Read button state using `machine.Pin`
3. Use `elif` to check multiple conditions in sequence
4. Build a button-controlled colour changer

---

## New Hardware: Push Button

A push button is a simple switch. When pressed, it completes a circuit. We wire it so pressing the button connects a GPIO pin to GND.

### Wiring

{: .important }
Always double-check wiring before powering on. Incorrect wiring can damage components.

| Button Leg | Connect To |
|-----------|-----------|
| Leg 1 | GPIO 0 |
| Leg 2 | GND |

A button has two pairs of legs. Legs within each pair are already connected internally — you need one leg from each pair.

### Why PULL_UP?

If you connect a pin to GND via a button, what does the pin read when the button is *not* pressed? Without anything pulling it up to 3.3V, it would "float" — giving random, unreliable values (sometimes 0, sometimes 1, seemingly at random).

The solution: a **pull-up resistor** connected between the pin and 3.3V. The ESP32-S3 has these built in — just pass `Pin.PULL_UP` when creating the pin:

```python
button = Pin(0, Pin.IN, Pin.PULL_UP)
```

**Result:**
- Button NOT pressed: pin reads `1` (pulled up to 3.3V)
- Button pressed: pin reads `0` (connected to GND)

This is called **active-low** — the signal is LOW (0) when active (pressed).

---

## Concepts

### `elif` — Else If

`elif` lets you check a series of conditions, one after another. Python tests each condition in order. As soon as one is `True`, it runs that block and skips all the rest.

```python
score = 75

if score >= 80:
    print("A grade")
elif score >= 70:
    print("B grade")
elif score >= 60:
    print("C grade")
elif score >= 50:
    print("D grade")
else:
    print("F grade")
```

**Why `elif` instead of multiple `if`?**

```python
# With elif (correct — only one block runs):
if score >= 80:
    print("A")
elif score >= 70:
    print("B")

# With separate ifs (might print multiple lines!):
if score >= 80:
    print("A")
if score >= 70:   # This also runs when score is 80+!
    print("B")
```

Use `elif` when the conditions are mutually exclusive (can't both be true at once). Use separate `if` statements when conditions are independent.

### Reading Buttons

```python
from machine import Pin

button = Pin(0, Pin.IN, Pin.PULL_UP)
state = button.value()   # Returns 0 or 1
```

`button.value()` returns:
- `0` if the button is pressed (connected to GND)
- `1` if not pressed (pulled up to 3.3V)

### Debouncing

When a physical button is pressed, the electrical contacts briefly "bounce" — rapidly switching on and off several times before settling. This can cause your code to register multiple presses for a single click.

**Simple software debounce:** add a short delay after detecting a press, or use a `was_pressed` flag:

```python
was_pressed = False

while True:
    if button.value() == 0:      # Button is down
        if not was_pressed:       # And it wasn't already down
            # Handle press (runs once per press)
            was_pressed = True
    else:
        was_pressed = False       # Button released — reset flag
```

---

## Guided Walkthrough

### Step 1: Read the Button State

Make sure your button is wired (leg 1 to GPIO 0, leg 2 to GND). Run this:

```python
from machine import Pin
import time

button = Pin(0, Pin.IN, Pin.PULL_UP)

print("Press the button! (Ctrl+C to stop)")
while True:
    state = button.value()
    if state == 0:
        print("PRESSED")
    else:
        print("not pressed")
    time.sleep(0.2)
```

You should see "not pressed" continuously until you press and hold the button, then "PRESSED".

### Step 2: `elif` with a Score System

```python
grade = int(input("Enter your percentage: "))

if grade >= 80:
    print("7 — Excellent!")
elif grade >= 70:
    print("6 — Good work!")
elif grade >= 60:
    print("5 — Satisfactory")
elif grade >= 50:
    print("4 — Adequate")
elif grade >= 40:
    print("3 — Below average")
elif grade >= 30:
    print("2 — Poor")
else:
    print("1 — Very poor")
```

Try entering values like 85, 72, 45, 28.

### Step 3: Button Changes LED Colour

Each time you press the button, the LED cycles to the next colour:

```python
import machine, neopixel, time
from machine import Pin

pin48 = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin48, 1)
button = Pin(0, Pin.IN, Pin.PULL_UP)

colours = [
    ("Red",    (255, 0, 0)),
    ("Green",  (0, 255, 0)),
    ("Blue",   (0, 0, 255)),
    ("Yellow", (255, 200, 0)),
    ("Purple", (128, 0, 255)),
    ("Cyan",   (0, 200, 255)),
]

colour_index = 0
was_pressed = False

# Show initial colour
np[0] = colours[colour_index][1]
np.write()
print(f"Starting colour: {colours[colour_index][0]}")
print("Press button to change colour. Ctrl+C to stop.")

while True:
    if button.value() == 0:    # Button pressed
        if not was_pressed:    # New press (not held)
            colour_index = (colour_index + 1) % len(colours)
            np[0] = colours[colour_index][1]
            np.write()
            print(f"Colour: {colours[colour_index][0]}")
            was_pressed = True
    else:
        was_pressed = False    # Reset when button released
    time.sleep(0.05)
```

**Explanation of `(colour_index + 1) % len(colours)`:**
This cycles through 0, 1, 2, 3, 4, 5, 0, 1, 2... When we reach the last index and add 1, the modulo (`%`) wraps it back to 0.

### Step 4: `elif` with the Button

Now use `elif` to give the button different behaviour depending on how long it's been held:

```python
import machine, neopixel, time
from machine import Pin

pin48 = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin48, 1)
button = Pin(0, Pin.IN, Pin.PULL_UP)

print("Hold button for different effects:")
print("  Short press (<0.5s) = Red")
print("  Medium press (0.5-1.5s) = Green")
print("  Long press (>1.5s) = Blue")
print("Ctrl+C to stop.")

while True:
    if button.value() == 0:    # Button pressed
        press_start = time.ticks_ms()

        # Wait until button released
        while button.value() == 0:
            time.sleep(0.01)

        press_duration = time.ticks_diff(time.ticks_ms(), press_start) / 1000.0

        if press_duration < 0.5:
            np[0] = (255, 0, 0)     # Red — short press
            print(f"Short press ({press_duration:.2f}s) — Red")
        elif press_duration < 1.5:
            np[0] = (0, 255, 0)     # Green — medium
            print(f"Medium press ({press_duration:.2f}s) — Green")
        else:
            np[0] = (0, 0, 255)     # Blue — long press
            print(f"Long press ({press_duration:.2f}s) — Blue")

        np.write()

    time.sleep(0.05)
```

---

## Challenges

### ⭐ Core
Use `elif` to create a mood display: ask the user to enter a number 1–4 (1=happy, 2=calm, 3=excited, 4=mysterious). Show yellow for happy, blue for calm, red for excited, and purple for mysterious. If they enter anything else, show white and print "Unknown mood".

### ⭐⭐ Extension
Use a button to **toggle** the LED on and off. Press once — LED turns on (green). Press again — LED turns off. Each press flips the state. Use a boolean variable `led_is_on = False` to track the current state.

### ⭐⭐⭐ Stretch
Create a "Simon Says" game (using `input()` for simplicity):
1. Choose a random colour and display it on the LED for 1 second
2. Ask the player to type the colour name
3. Give them 3 chances. Flash green for correct, red for wrong.
4. After 3 rounds, print the player's score.

Use `elif` to check the answer. Hint: `import random; random.choice(colour_list)`.

---

## Common Mistakes & Debugging

**Button always reads 1 (never 0)**
Check wiring. Make sure one leg is on GPIO 0 and the other is on GND. A button with 4 legs: opposing legs are connected internally; adjacent legs are the two different sides.

**Button seems to fire many times per press**
This is bounce. Add the `was_pressed` flag pattern from the walkthrough, or add `time.sleep(0.1)` after detecting a press.

**Forgetting `Pin.PULL_UP`**
Without it, the pin floats and reads random values. Always include `Pin.PULL_UP` for button inputs.

**`elif` not matching**
Check that conditions don't overlap unexpectedly. Test with specific values. Print the value being tested.

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| **elif** | "Else if" — checks another condition if previous conditions were `False` |
| **active-low** | Signal is LOW (0) when active, HIGH (1) when inactive |
| **pull-up resistor** | Connects a pin to 3.3V so it reads HIGH when nothing else is driving it |
| **debounce** | Handling the brief rapid switching when a button is physically pressed |
| **GPIO** | General Purpose Input/Output — configurable as input or output |
| **`Pin.IN`** | Configures a GPIO pin as an input |
| **`Pin.PULL_UP`** | Enables the internal pull-up resistor on a GPIO input pin |
