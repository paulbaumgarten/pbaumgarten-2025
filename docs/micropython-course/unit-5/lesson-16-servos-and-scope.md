---
title: "Lesson 16 - Servos and Variable Scope"
layout: default
nav_order: 3
parent: "Unit 5: Functions and Modularity"
grand_parent: MicroPython
---

# Lesson 16 — Servos and Variable Scope
{: .no_toc }

**Estimated time:** 90 minutes

- TOC
{:toc}

---

## Learning Objectives

By the end of this lesson you will be able to:

1. Wire and control a 9G servo motor with PWM
2. Understand local vs global variable scope
3. Use the `global` keyword when necessary
4. Build a button-controlled servo with LED feedback

---

## New Hardware: 9G Servo Motor

A servo motor moves to a precise **angle** (0°–180°) and holds that position. It uses three wires: power, ground, and a signal wire that receives PWM pulses.

### Wiring

| Servo Wire | Connect To |
|-----------|-----------|
| Red | 5V |
| Brown or Black (ground) | GND |
| Orange or Yellow (signal) | GPIO 13 |

{: .important }
Servos can draw significant current when moving. If your ESP32-S3 resets unexpectedly when the servo moves, power the servo from a separate 5V supply (connecting GND between both supplies).

### How Servo Control Works — PWM

**PWM (Pulse Width Modulation)** is a way to communicate an analogue value using a digital pin. The signal alternates rapidly between HIGH and LOW. The *proportion* of time it's HIGH (the **duty cycle**) carries the information.

For servos, we use 50Hz frequency (50 pulses per second). The width of each pulse determines the angle:
- ~0.5ms pulse → 0°
- ~1.5ms pulse → 90° (centre)
- ~2.5ms pulse → 180°

In MicroPython on ESP32, the `duty()` function takes a value 0–1023. For a 50Hz signal:
- 0° ≈ duty 40 (calibrate for your specific servo)
- 180° ≈ duty 115

{: .highlight }
**Did you know?** Servos are in RC cars and planes, robotic arms, camera gimbals (those systems that keep cameras steady), and even the tiny actuators inside automatic camera lenses. The servo principle was invented in the 1800s for controlling ship rudders.

---

## Concepts

### Local vs Global Scope

**Scope** is the region of code where a variable is visible and accessible.

**Local variable** — created *inside* a function. Only exists while the function is running. Disappears when the function returns.

**Global variable** — created *outside* any function. Exists throughout the whole program.

```python
x = 10    # Global

def my_function():
    y = 20          # Local — only exists inside this function
    print(x)        # Can READ global x ✓
    print(y)        # Can read local y ✓

my_function()
print(x)    # ✓ Can access global x
# print(y)  # ✗ ERROR — y doesn't exist here
```

**Why scope?** Functions get their own "workspace" so they don't accidentally overwrite each other's variables. This makes code safer and easier to reason about.

### Modifying a Global Variable

If you want to *change* a global variable from inside a function, use the `global` keyword:

```python
counter = 0

def increment():
    global counter        # Tell Python: use the GLOBAL counter
    counter = counter + 1 # Now this modifies the global

increment()
increment()
increment()
print(counter)   # 3
```

Without `global`, Python would create a new *local* variable called `counter` instead of modifying the global one.

{: .note }
**Best practice:** Use `global` sparingly. Prefer passing values in as parameters and getting results back via `return`. `global` is mainly useful for hardware objects and simple state variables that must be shared across many functions.

---

## Guided Walkthrough

### Step 1: Basic Servo Control

```python
from machine import Pin, PWM
import time

servo = PWM(Pin(13), freq=50)

def set_angle(angle):
    """Move servo to specified angle (0-180 degrees)."""
    # Map 0-180° to duty cycle
    # Adjust min_duty and max_duty to calibrate your servo
    min_duty = 40
    max_duty = 115
    duty = int(min_duty + (angle / 180) * (max_duty - min_duty))
    servo.duty(duty)

# Test: move through key positions
for angle in [0, 45, 90, 135, 180]:
    print(f"Moving to {angle}°")
    set_angle(angle)
    time.sleep(1)

set_angle(90)    # Return to centre
time.sleep(0.5)
servo.deinit()   # Release PWM when done
print("Done!")
```

**Calibrating your servo:** If 0° and 180° don't match what you expect, adjust `min_duty` (for 0°) and `max_duty` (for 180°). Try values between 30–55 for min and 100–130 for max.

### Step 2: Scope Demonstration

```python
score = 100    # Global

def add_points(points):
    # Can READ global score:
    new_score = score + points
    return new_score              # Return instead of modifying global

def reset_score():
    global score                  # Declare intent to modify global
    score = 0
    print("Score reset to 0")

print(f"Initial score: {score}")

result = add_points(50)
print(f"After adding 50: {result}")
print(f"Global score unchanged: {score}")

reset_score()
print(f"After reset: {score}")
```

### Step 3: Servo + LED + Scope

```python
from machine import Pin, PWM
import machine, neopixel, time

# Hardware (global objects — fine to be global)
servo = PWM(Pin(13), freq=50)
pin48 = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin48, 1)

# State variable (global — shared across functions)
current_angle = 90

def set_angle(angle):
    """Set servo angle and update LED colour."""
    global current_angle
    angle = max(0, min(180, angle))   # Clamp to valid range
    current_angle = angle

    duty = int(40 + (angle / 180) * 75)
    servo.duty(duty)

    # LED shows angle: 0°=red, 90°=yellow, 180°=green
    red   = int(255 * (1 - angle / 180))
    green = int(255 * (angle / 180))
    np[0] = (red, green, 0)
    np.write()

def sweep(start_angle, end_angle, step=5, delay=0.04):
    """Sweep servo from start to end angle."""
    direction = 1 if end_angle > start_angle else -1
    angle = start_angle
    while (direction == 1 and angle <= end_angle) or \
          (direction == -1 and angle >= end_angle):
        set_angle(angle)
        time.sleep(delay)
        angle += direction * step

def centre():
    """Move to centre (90°)."""
    set_angle(90)

# Demo sequence
print("Servo demo...")
centre()
time.sleep(1)

print("Sweeping 90° to 180°...")
sweep(90, 180)
time.sleep(0.5)

print("Sweeping 180° to 0°...")
sweep(180, 0, step=3, delay=0.03)
time.sleep(0.5)

print("Sweeping back to centre...")
sweep(0, 90)

print(f"Final angle: {current_angle}°")
servo.deinit()
```

### Step 4: Button-Controlled Servo

```python
from machine import Pin, PWM
import machine, neopixel, time

servo = PWM(Pin(13), freq=50)
btn_up   = Pin(0, Pin.IN, Pin.PULL_UP)
btn_down = Pin(14, Pin.IN, Pin.PULL_UP)
pin48 = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin48, 1)

current_angle = 90
STEP = 10

def set_angle(angle):
    global current_angle
    angle = max(0, min(180, angle))
    current_angle = angle
    servo.duty(int(40 + (angle / 180) * 75))
    np[0] = (int(255 * (1 - angle/180)), int(255 * angle/180), 0)
    np.write()

set_angle(90)
print("Button controls:")
print("  Button A (GPIO 0)  = increase angle")
print("  Button B (GPIO 14) = decrease angle")
print("Ctrl+C to stop.")

while True:
    if btn_up.value() == 0:
        set_angle(current_angle + STEP)
        print(f"Angle: {current_angle}°")
        time.sleep(0.25)   # Debounce + prevent rapid firing
    elif btn_down.value() == 0:
        set_angle(current_angle - STEP)
        print(f"Angle: {current_angle}°")
        time.sleep(0.25)
    time.sleep(0.05)
```

---

## Challenges

### ⭐ Core
Write a `servo_wave(speed)` function that sweeps the servo from 0° to 180° and back three times. `speed` should be a delay value (small = fast, large = slow). Test it with `servo_wave(0.02)` and `servo_wave(0.1)`.

### ⭐⭐ Extension
Write `map_distance_to_angle(distance, min_dist, max_dist)` that maps a distance value linearly to 0°–180°. Connect the ultrasonic sensor and use this function to make the servo track detected distance — move the servo to show how close the object is.

### ⭐⭐⭐ Stretch
Create a "servo recorder": use a global list `angle_history = []`. Write `log_angle(angle)` that calls `set_angle()` AND appends the angle to the history list. Write `replay()` that moves through the history list, calling `set_angle()` for each stored angle. Record a sequence using the buttons, then replay it. Print the history before replaying.

---

## Common Mistakes & Debugging

**Servo jitters or vibrates**
Often a power issue — servo draws more current than the ESP32 can supply. Try a separate 5V supply for the servo.

**`UnboundLocalError: local variable 'x' referenced before assignment`**
You have a global variable `x` and tried to use it inside a function, but also assigned to it in the same function without declaring `global x`. Either add `global x` at the top of the function, or pass the value as a parameter.

**Servo only moves to extremes**
Duty cycle range needs calibrating. Test values like `servo.duty(30)` through `servo.duty(130)` manually to find the range.

**Forgetting `servo.deinit()`**
If you restart your script without running `servo.deinit()`, the PWM channel may not reinitialise correctly. Press Ctrl+C, reset the board, and try again.

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| **servo** | A motor with a built-in control circuit that moves to and holds a precise angle |
| **PWM** | Pulse Width Modulation — varying the pulse width to communicate a value |
| **duty cycle** | The proportion of time a PWM signal is HIGH |
| **local variable** | A variable created inside a function — only exists within that function |
| **global variable** | A variable created outside functions — accessible everywhere |
| **scope** | The region of code where a variable is visible |
| **global keyword** | Declares that a variable inside a function refers to the global variable of that name |
