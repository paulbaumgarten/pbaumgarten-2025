---
title: "Lesson 13 - Ultrasonic Sensor and Sensor Logging"
layout: default
nav_order: 3
parent: "Unit 4: Collections of Data"
grand_parent: MicroPython Course
---

# Lesson 13 — Ultrasonic Sensor and Sensor Logging
{: .no_toc }

**Estimated time:** 90 minutes

- TOC
{:toc}

---

## Learning Objectives

By the end of this lesson you will be able to:

1. Wire the HC-SR04 ultrasonic distance sensor
2. Write a measurement function using digital I/O and timing
3. Store multiple distance readings in a list
4. Build a distance-responsive LED indicator

---

## New Hardware: HC-SR04 Ultrasonic Distance Sensor

The HC-SR04 measures distance by sending a burst of ultrasonic sound (40kHz — too high for human ears) and measuring how long it takes to bounce back.

{: .highlight }
**Did you know?** This is the exact same principle bats use for echolocation — they emit high-pitched squeaks and use the returning echoes to "see" in complete darkness. The US Navy also uses the same principle in sonar systems on submarines.

### Wiring

| HC-SR04 Pin | Connect To |
|------------|-----------|
| VCC | 5V (or 3.3V if using HC-SR04P variant) |
| GND | GND |
| TRIG | GPIO 5 |
| ECHO | GPIO 4 (see note below) |

{: .important }
**ECHO pin voltage:** Standard HC-SR04 modules output 5V on the ECHO pin. The ESP32-S3 GPIO pins are 3.3V only — connecting 5V directly could damage the chip. Add a **voltage divider**: ECHO → 1kΩ resistor → junction, and junction → 2kΩ resistor → GND. Connect GPIO 4 to the junction. This brings 5V down to ~3.3V safely. The **HC-SR04P** variant runs at 3.3V natively and doesn't need this.

### How It Works

1. Send a 10 microsecond HIGH pulse to the **TRIG** pin
2. The sensor emits 8 ultrasonic pulses
3. The **ECHO** pin goes HIGH and stays HIGH until the pulses return
4. Measure how long ECHO was HIGH (in microseconds)
5. Calculate: `distance (cm) = echo_duration_µs / 58.2`

The division by 58.2 accounts for the speed of sound (343 m/s) and the fact that the sound travels twice the distance (out AND back).

---

## Concepts

### Microsecond Timing

Sound travels fast — about 0.034cm per microsecond. To measure distance to 1cm accuracy, we need microsecond timing.

MicroPython provides:
- **`time.ticks_us()`** — returns the current time in microseconds since boot
- **`time.ticks_diff(end, start)`** — calculates the difference correctly (handles overflow)
- **`time.sleep_us(n)`** — sleeps for n microseconds

{: .note }
Always use `time.ticks_diff(end, start)` rather than `end - start` for timing. The ticks counter can overflow (wrap back to zero), and `ticks_diff` handles this correctly.

### Writing a Measurement Function

This is a preview of Unit 5 (Functions). For now, just notice the structure:

```python
def get_distance():
    # ... measurement code ...
    return distance_value
```

This function does all the messy timing work and returns just the clean distance value.

---

## Guided Walkthrough

### Step 1: Wire and Test the Sensor

Make sure wiring is correct (check voltage divider if needed). Run this to see raw readings:

```python
from machine import Pin
import time

trig = Pin(5, Pin.OUT)
echo = Pin(4, Pin.IN)

def get_distance():
    """Measure distance in cm. Returns -1 if no reading obtained."""
    # Send 10µs trigger pulse
    trig.off()
    time.sleep_us(2)
    trig.on()
    time.sleep_us(10)
    trig.off()

    # Wait for echo to go HIGH (with timeout to avoid hanging)
    timeout = time.ticks_us() + 30000   # 30ms timeout
    while echo.value() == 0:
        if time.ticks_us() > timeout:
            return -1   # No echo received

    # Measure how long echo stays HIGH
    pulse_start = time.ticks_us()
    timeout = pulse_start + 30000
    while echo.value() == 1:
        if time.ticks_us() > timeout:
            return -1   # Echo too long (object too close or stuck)

    pulse_end = time.ticks_us()

    # Calculate and return distance
    duration = time.ticks_diff(pulse_end, pulse_start)
    return round(duration / 58.2, 1)

print("Distance sensor ready. Move your hand closer/further.")
print("Ctrl+C to stop.")

while True:
    dist = get_distance()
    if dist == -1:
        print("No reading")
    else:
        print(f"Distance: {dist} cm")
    time.sleep(0.5)
```

Move your hand toward and away from the sensor. You should see the distance change smoothly.

### Step 2: Distance-Based LED Colour

```python
from machine import Pin
import machine, neopixel, time

trig = Pin(5, Pin.OUT)
echo = Pin(4, Pin.IN)
pin48 = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin48, 1)

def get_distance():
    trig.off(); time.sleep_us(2)
    trig.on(); time.sleep_us(10); trig.off()
    t = time.ticks_us() + 30000
    while echo.value() == 0:
        if time.ticks_us() > t: return -1
    s = time.ticks_us()
    t = s + 30000
    while echo.value() == 1:
        if time.ticks_us() > t: return -1
    return round(time.ticks_diff(time.ticks_us(), s) / 58.2, 1)

print("Distance indicator! Ctrl+C to stop.")

while True:
    dist = get_distance()

    if dist == -1 or dist > 200:
        np[0] = (5, 5, 5)       # Dim white — no reading
    elif dist < 10:
        np[0] = (255, 0, 0)     # Red — very close (<10cm)
    elif dist < 20:
        np[0] = (255, 100, 0)   # Orange — close (10-20cm)
    elif dist < 40:
        np[0] = (255, 230, 0)   # Yellow — medium (20-40cm)
    else:
        np[0] = (0, 255, 0)     # Green — far away (>40cm)

    np.write()

    if dist != -1:
        print(f"{dist:6.1f} cm", end="\r")   # \r = overwrite same line

    time.sleep(0.15)
```

{: .note }
The `end="\r"` in `print()` makes the output overwrite the same line in the terminal, giving a cleaner live display.

### Step 3: Collecting Readings Into a List

```python
from machine import Pin
import time

trig = Pin(5, Pin.OUT)
echo = Pin(4, Pin.IN)

def get_distance():
    trig.off(); time.sleep_us(2)
    trig.on(); time.sleep_us(10); trig.off()
    t = time.ticks_us() + 30000
    while echo.value() == 0:
        if time.ticks_us() > t: return -1
    s = time.ticks_us()
    t = s + 30000
    while echo.value() == 1:
        if time.ticks_us() > t: return -1
    return round(time.ticks_diff(time.ticks_us(), s) / 58.2, 1)

readings = []
print("Collecting 20 readings (1 per second)...")

for i in range(20):
    dist = get_distance()
    if dist != -1 and dist <= 300:     # Only store valid, in-range readings
        readings.append(dist)
        print(f"Reading {i+1:2d}: {dist} cm ✓")
    else:
        print(f"Reading {i+1:2d}: invalid — skipped")
    time.sleep(1)

# Analyse collected data
if len(readings) > 0:
    readings.sort()
    print(f"\n--- Results ({len(readings)} valid readings) ---")
    print(f"Minimum:  {min(readings)} cm")
    print(f"Maximum:  {max(readings)} cm")
    print(f"Average:  {sum(readings)/len(readings):.1f} cm")
    print(f"Median:   {readings[len(readings)//2]} cm")

    close = [r for r in readings if r < 20]
    print(f"Under 20cm: {len(close)} readings")
else:
    print("No valid readings collected!")
```

---

## Challenges

### ⭐ Core
Collect 10 distance readings (1 per second). Print them as a list. Then print how many were above 30cm and how many were 30cm or under. Display the LED green if more than half were above 30cm, red if not.

### ⭐⭐ Extension
Build a "rolling average": keep a list of the last 5 distance readings only. After each new reading, if the list has more than 5 items, remove the oldest (hint: `.pop(0)` removes the first item). Print the rolling average after each reading. If the rolling average drops below 15cm, flash the LED red.

### ⭐⭐⭐ Stretch
Collect 30 readings over 30 seconds. Then calculate:
- Min, max, average, median
- The **largest change** between any two consecutive readings (abs difference)
- The 10th **percentile** (the value below which 10% of readings fall — sort the list and take index `len//10`)
Print a nicely formatted summary. Flash the LED once per 5cm of the median distance.

---

## Common Mistakes & Debugging

**Sensor always returns -1**
Check TRIG and ECHO pin connections. Verify VCC is correct voltage. Try increasing the timeout value in the function.

**Readings are wildly inconsistent**
Add at least 60ms between readings — the sensor needs time to settle. Some objects (soft fabrics, angled surfaces) absorb or scatter ultrasound poorly.

**Distance seems too large**
Make sure you're dividing by 58.2 (not 29.1). The sound travels twice the distance (out and back), and 58.2 accounts for both.

**Overflow issues with `ticks_us()`**
Always use `time.ticks_diff(end, start)` instead of `end - start`. The raw ticks value wraps around and direct subtraction gives wrong results.

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| **HC-SR04** | An ultrasonic distance sensor using sound pulses |
| **TRIG pin** | Trigger pin — send a 10µs pulse to start a measurement |
| **ECHO pin** | Echo pin — stays HIGH for the duration of the sound's round trip |
| **microsecond (µs)** | One millionth of a second — used for timing sound pulses |
| **voltage divider** | Two resistors that reduce a voltage proportionally |
| **time.ticks_us()** | Returns the current time in microseconds since boot |
| **time.ticks_diff()** | Correctly calculates the difference between two ticks values |
| **sensor logging** | Storing sensor readings in a list for later analysis |
