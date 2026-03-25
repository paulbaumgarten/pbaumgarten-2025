---
title: "Lesson 10 - IR Sensor, break, and continue"
layout: default
nav_order: 3
parent: "Unit 3: Loops and Repetition"
grand_parent: MicroPython Course
---

# Lesson 10 — IR Sensor, break, and continue
{: .no_toc }

**Estimated time:** 75 minutes

- TOC
{:toc}

---

## Learning Objectives

By the end of this lesson you will be able to:

1. Wire and read an IR proximity sensor
2. Use `break` to exit a loop immediately
3. Use `continue` to skip the current iteration
4. Build a sensor-triggered alarm

---

## New Hardware: IR Proximity Sensor

An IR (infrared) sensor emits infrared light and detects when it reflects off a nearby object. The output pin goes LOW (0) when an object is detected.

### Wiring

| IR Sensor Pin | Connect To |
|--------------|-----------|
| VCC | 3.3V |
| GND | GND |
| OUT | GPIO 12 |

{: .important }
Double-check wiring before powering on. VCC must go to **3.3V**, not 5V.

Most IR sensor modules have a small potentiometer (adjustment screw) to tune the detection sensitivity. Turning it adjusts the detection range.

{: .highlight }
**Did you know?** IR sensors use the same principle as TV remote controls and automatic hand sanitiser dispensers. They're also used in robot obstacle-detection systems and even smartphone proximity sensors (that turn off the screen when you hold the phone to your ear).

---

## Concepts

### `break` — Exit the Loop Immediately

`break` instantly exits the current loop, regardless of the loop condition. Think of it as an emergency exit.

```python
for i in range(10):
    if i == 5:
        break          # Exit immediately when i is 5
    print(i)

# Output: 0 1 2 3 4
# (never reaches 5,6,7,8,9)
```

`break` works in both `for` and `while` loops. After `break`, execution continues from the first line *after* the loop.

**Common use:** exit when you've found what you're looking for:

```python
numbers = [3, 7, 2, 8, 1, 9, 4]
target = 8

for i, num in enumerate(numbers):
    if num == target:
        print(f"Found {target} at index {i}")
        break    # Stop searching — no point checking the rest
```

### `continue` — Skip This Iteration

`continue` skips the rest of the *current* iteration and jumps back to the top of the loop to check the condition (while) or move to the next item (for).

```python
for i in range(10):
    if i % 2 == 0:
        continue      # Skip even numbers
    print(i)          # Only runs for odd numbers

# Output: 1 3 5 7 9
```

Think of `continue` as "skip this one, move on to the next".

### Flow Diagrams

```
Normal for loop:
  → check if items remain → YES → run body → back to check
                          → NO  → exit loop

With break:
  → check if items remain → YES → run body → if break: EXIT
                          → NO  → exit loop

With continue:
  → check if items remain → YES → run body → if continue: skip rest, back to check
```

### `break` in Nested Loops

Important: `break` only exits the **innermost** loop it's inside. It doesn't break out of all nested loops at once.

```python
for row in range(3):
    for col in range(3):
        if col == 1:
            break       # Breaks inner loop only
        print(f"({row},{col})", end=" ")
    print()
# Output:
# (0,0)
# (1,0)
# (2,0)
```

---

## Guided Walkthrough

### Step 1: Read the IR Sensor

```python
from machine import Pin
import time

ir = Pin(12, Pin.IN)   # Active-low: 0 = detected, 1 = not detected

print("IR sensor ready. Wave your hand in front!")
print("Ctrl+C to stop.")

while True:
    if ir.value() == 0:
        print("OBJECT DETECTED!")
    else:
        print("clear")
    time.sleep(0.2)
```

Wave your hand close to the sensor — you should see "OBJECT DETECTED!" appear.

### Step 2: `break` — Stop When Detected

```python
from machine import Pin
import machine, neopixel, time

ir = Pin(12, Pin.IN)
pin48 = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin48, 1)

print("Waiting for object detection...")

# Show pulsing green while waiting
brightness = 0
direction = 10

while True:
    if ir.value() == 0:    # Object detected!
        print("Detected! Stopping wait loop.")
        break

    # Pulse green while waiting
    np[0] = (0, brightness, 0)
    np.write()
    brightness += direction
    if brightness >= 150 or brightness <= 0:
        direction = -direction
    time.sleep(0.05)

# Code here runs after break exits the loop
np[0] = (255, 0, 0)   # Red alert!
np.write()
print("Object detected — red alert!")
time.sleep(2)
np[0] = (0, 0, 0)
np.write()
```

### Step 3: `continue` — Skip Some Numbers

```python
# Print 1-20 but skip multiples of 3
print("Numbers 1-20, skipping multiples of 3:")
for i in range(1, 21):
    if i % 3 == 0:
        continue   # Skip this iteration
    print(i, end=" ")
print()

# Count valid sensor readings (skip -1 errors)
import random
readings = []
for _ in range(20):
    # Simulate sensor: random reading, 20% chance of error
    reading = random.randint(10, 100) if random.random() > 0.2 else -1
    if reading == -1:
        continue   # Skip invalid readings
    readings.append(reading)

print(f"Got {len(readings)} valid readings out of 20 attempts")
print(f"Average: {sum(readings)/len(readings):.1f}")
```

### Step 4: IR Alarm System

```python
from machine import Pin
import machine, neopixel, time

ir = Pin(12, Pin.IN)
pin48 = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin48, 1)

ALARM_THRESHOLD = 5    # Number of detections before alarm

detection_count = 0
print(f"Security system: alarm triggers after {ALARM_THRESHOLD} detections")
print("Ctrl+C to stop.")

# Standby indicator — dim green
np[0] = (0, 30, 0)
np.write()

while True:
    if ir.value() == 0:    # Detection!
        detection_count += 1
        print(f"Detection #{detection_count}")

        # Brief red flash for each detection
        for _ in range(3):
            np[0] = (200, 0, 0)
            np.write()
            time.sleep(0.08)
            np[0] = (0, 30, 0)   # Back to standby green
            np.write()
            time.sleep(0.08)

        if detection_count >= ALARM_THRESHOLD:
            break    # Trigger alarm — exit the monitoring loop

        time.sleep(0.3)   # Brief pause between detections

    time.sleep(0.05)

# Alarm sequence (runs after break)
print("ALARM TRIGGERED!")
for _ in range(20):
    np[0] = (255, 0, 0)
    np.write()
    time.sleep(0.05)
    np[0] = (255, 100, 0)
    np.write()
    time.sleep(0.05)

np[0] = (0, 0, 0)
np.write()
print(f"Alarm triggered after {detection_count} detections.")
```

---

## Challenges

### ⭐ Core
Write a number guessing game using `break`. The computer picks a random number between 1 and 20 (`random.randint(1, 20)`). The player keeps guessing. Print "Too high" or "Too low" after each wrong guess. When correct, print "Correct!" and how many guesses it took. Use `break` to exit when they guess right.

### ⭐⭐ Extension
Use `continue` to collect exactly 10 *valid* IR sensor readings (skipping any that are invalid or from sensors that aren't triggering). For each invalid reading, print "skipped". After 10 valid readings, print how many total attempts it took (valid + skipped).

### ⭐⭐⭐ Stretch
Create a "watchdog timer" using the IR sensor:
- The LED shows solid green normally
- Every 5 seconds, it checks if the IR sensor has been triggered at least once in that window
- If yes: flash green twice (all good), reset the detection counter
- If no: flash orange once as a warning, increment a "missed windows" counter
- If 3 windows are missed in a row: trigger a red alarm (rapid flashing, print "MISSED CONTACT"), then reset
Use `break` if you want to add a stop condition (e.g., 10 missed contacts total).

---

## Common Mistakes & Debugging

**IR sensor always reads 0 (always "detected")**
Check VCC is connected to 3.3V. Also try adjusting the sensitivity potentiometer on the module.

**IR sensor always reads 1 (never detects)**
Check the OUT pin is connected. Try adjusting the potentiometer in the other direction. Some modules need the object to be within 3–10cm.

**`break` only exits one loop**
If you have nested loops, `break` only exits the innermost one. If you need to exit multiple levels, consider using a flag variable or reorganising your code.

**`continue` in a `while` loop — infinite loop risk**
If you use `continue` in a `while` loop, make sure the loop variable/condition still gets updated. Otherwise you might loop forever on the same condition.

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| **break** | Immediately exits the current loop and continues from the first line after it |
| **continue** | Skips the rest of the current loop iteration and jumps to the next check/item |
| **IR sensor** | Infrared proximity sensor — detects objects by emitting and receiving infrared light |
| **active-low** | Signal is LOW (0) when active/detected, HIGH (1) when inactive |
| **loop control statement** | `break` or `continue` — changes normal loop flow |
