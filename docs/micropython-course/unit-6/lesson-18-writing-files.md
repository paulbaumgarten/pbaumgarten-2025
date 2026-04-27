---
title: "Lesson 18 - Writing Files and Data Logging"
layout: default
nav_order: 2
parent: "Unit 6: Working with Files"
grand_parent: MicroPython
---

# Lesson 18 — Writing Files and Data Logging
{: .no_toc }

**Estimated time:** 90 minutes

- TOC
{:toc}

---

## Learning Objectives

By the end of this lesson you will be able to:

1. Write to files using write mode (`"w"`) and append mode (`"a"`)
2. Log sensor data to a CSV file over time
3. Wire and control a relay to switch a DC motor
4. Build a complete sensor-logging system with motor control

---

## New Hardware: Relay Module + DC Motor

### What is a Relay?

A relay is an electrically-controlled switch. A small signal (3.3V from the ESP32) controls an electromagnet that physically opens or closes a larger circuit — in our case, the 5V motor circuit.

{: .highlight }
**Did you know?** Relays are the ancestors of modern computers. Early computers in the 1940s (like the Harvard Mark I) used electromechanical relays to perform calculations — thousands of them, clicking away. Transistors replaced them because they're much smaller and faster, but relays are still used today in automotive systems, power distribution, and industrial control.

### Wiring

**Relay control (ESP32 side):**

| Relay Pin | Connect To |
|----------|-----------|
| VCC | 3.3V |
| GND | GND |
| IN | GPIO 15 |

**Motor circuit (separate 5V supply):**

| Connection | Notes |
|-----------|-------|
| Motor (+) | Relay COM terminal |
| 5V supply (+) | Relay NO terminal |
| Motor (−) and 5V supply (−) | Common GND (same as ESP32 GND) |

{: .important }
**The motor uses a separate power circuit from the ESP32.** The relay acts as the bridge. Never power the motor from the ESP32's 3.3V pin — motors draw too much current. Wire the motor to a separate 5V supply, with GND connected to the ESP32's GND.

**NO vs NC terminals:**
- **NO (Normally Open):** Disconnected when relay is off, connected when on. Use this.
- **NC (Normally Closed):** Connected when relay is off, disconnected when on.

---

## Concepts

### Writing Files

**Write mode `"w"`** — creates a new file or **overwrites** an existing one:
```python
with open("greeting.txt", "w") as f:
    f.write("Hello!\n")
    f.write("This is a new file.\n")
```

{: .important }
Write mode destroys all existing content in the file. If you want to preserve existing content, use append mode.

**Append mode `"a"`** — adds to the **end** of the file without deleting existing content:
```python
with open("log.txt", "a") as f:
    f.write("New entry added.\n")
```

**Always add `\n` at the end of `.write()` lines** — unlike `print()`, `.write()` doesn't add a newline automatically.

### Writing Numbers

`.write()` only accepts strings. Convert numbers first:
```python
# These FAIL:
f.write(42)         # TypeError
f.write(3.14)       # TypeError

# These WORK:
f.write(str(42) + "\n")
f.write(f"{temperature:.1f}\n")   # f-string (cleanest)
```

### Timestamps in MicroPython

Without internet/RTC, we use **relative time** — milliseconds since boot:

```python
import time
timestamp = time.ticks_ms()   # Milliseconds since boot
```

To get elapsed time from a reference point:
```python
start = time.ticks_ms()
# ... do things ...
elapsed = time.ticks_diff(time.ticks_ms(), start)   # ms elapsed
```

---

## Guided Walkthrough

### Step 1: Writing a File

```python
# Create and write a file
with open("greeting.txt", "w") as f:
    f.write("Hello, filesystem!\n")
    f.write("Written by MicroPython.\n")
    f.write(f"Time: {time.ticks_ms()} ms since boot\n")

print("File written. Reading back...")

# Read it back to verify
with open("greeting.txt", "r") as f:
    print(f.read())
```

### Step 2: Appending to a File

```python
import time

# Initialise log file (write mode clears it first)
with open("events.txt", "w") as f:
    f.write("timestamp_ms,event\n")   # CSV header

print("Logging 5 events...")
for i in range(5):
    ts = time.ticks_ms()
    event = f"event_{i+1}"
    with open("events.txt", "a") as f:   # Append each entry
        f.write(f"{ts},{event}\n")
    print(f"Logged: {ts}ms — {event}")
    time.sleep(1)

# Show the complete log
print("\n--- events.txt ---")
with open("events.txt", "r") as f:
    print(f.read())
```

### Step 3: Relay Control

```python
from machine import Pin
import time

relay = Pin(15, Pin.OUT)
relay.off()    # Make sure motor starts off

print("Motor test:")

print("Motor ON")
relay.on()
time.sleep(3)

print("Motor OFF")
relay.off()
time.sleep(1)

# Pulse the motor 3 times
for i in range(3):
    print(f"Pulse {i+1}")
    relay.on()
    time.sleep(0.5)
    relay.off()
    time.sleep(0.5)

print("Done.")
```

### Step 4: Complete Data-Logging System

This program logs ultrasonic distance readings and motor events to a CSV file for 30 seconds:

```python
from machine import Pin
import machine, neopixel, time

# Hardware
trig = Pin(5, Pin.OUT)
echo = Pin(4, Pin.IN)
relay = Pin(15, Pin.OUT)
relay.off()
pin48 = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin48, 1)

def get_distance():
    """Measure distance in cm, return -1 on failure."""
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

def log_entry(elapsed_ms, distance, motor_state, event=""):
    """Append one CSV row to the log file."""
    with open("sensor_log.csv", "a") as f:
        f.write(f"{elapsed_ms},{distance},{motor_state},{event}\n")

# Initialise log file
with open("sensor_log.csv", "w") as f:
    f.write("elapsed_ms,distance_cm,motor_on,event\n")
log_entry(0, 0, 0, "system_start")

print("Logging for 30 seconds. Move objects near sensor!")
print("Motor activates when closer than 20cm.")

motor_on = False
start_time = time.ticks_ms()
DURATION = 30000    # 30 seconds in ms

while time.ticks_diff(time.ticks_ms(), start_time) < DURATION:
    elapsed = time.ticks_diff(time.ticks_ms(), start_time)
    dist = get_distance()

    if dist == -1:
        time.sleep(0.1)
        continue   # Skip invalid readings

    event = ""

    # Motor control logic
    if dist < 20 and not motor_on:
        relay.on()
        motor_on = True
        event = "motor_start"
        np[0] = (255, 50, 0)   # Orange — motor running
        np.write()
        print(f"  t={elapsed}ms: Motor START ({dist}cm)")

    elif dist >= 20 and motor_on:
        relay.off()
        motor_on = False
        event = "motor_stop"
        np[0] = (0, 80, 0)    # Dim green — standby
        np.write()
        print(f"  t={elapsed}ms: Motor STOP ({dist}cm)")

    log_entry(elapsed, dist, 1 if motor_on else 0, event)
    print(f"t={elapsed:6d}ms: {dist:5.1f}cm motor={'ON' if motor_on else 'off'}", end="\r")
    time.sleep(1)

# Stop everything
relay.off()
np[0] = (0, 0, 0)
np.write()
print("\n\nLogging complete!")

# Show summary
with open("sensor_log.csv", "r") as f:
    lines = f.readlines()

total = len(lines) - 1   # Minus header
print(f"Total entries: {total}")

starts = sum(1 for l in lines if "motor_start" in l)
print(f"Motor activations: {starts}")

print("\nFirst 5 data rows:")
for line in lines[1:6]:
    print(" ", line.strip())
```

---

## Challenges

### ⭐ Core
Ask the user to enter 5 of their favourite movies (via `input()`). Save them to `movies.txt`, one per line. Then read the file back and print them in reverse order with line numbers.

### ⭐⭐ Extension
Simulate a temperature sensor (`random.uniform(18.0, 30.0)`) that takes a reading every 2 seconds for 20 seconds. Log all readings to `temp_log.csv` (timestamp, temperature). After logging, read the file and calculate: average, min, max, and how many readings were above 25°C. Write a summary to `temp_summary.txt`.

### ⭐⭐⭐ Stretch
Build a motor-control logger: the motor (relay) switches on when the IR sensor detects an object, and off when it doesn't. Log every ON and OFF event with timestamp. After 1 minute (or Ctrl+C), stop logging and analyse: total time motor was ON (sum of ON durations), number of activations, average activation duration. Write an analysis report to `motor_report.txt`. Display the LED colour based on duty cycle: green <30%, yellow 30–70%, red >70%.

---

## Common Mistakes & Debugging

**Using `"w"` when you meant `"a"`**
Write mode DELETES existing content before writing. Use `"a"` for logging (appending), `"w"` only to initialise a fresh file.

**Forgetting `\n` at the end of `.write()`**
All data runs together on one line. Always end with `\n`: `f.write(f"{value}\n")`.

**`TypeError: write() argument must be str`**
Convert numbers to strings: use f-strings or `str()`.

**Flash storage full**
`OSError: [Errno 28] ENOSPC` — no space left. Delete old log files using Thonny's file manager, or limit log file size in your code.

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| **write mode (`"w"`)** | Opens for writing — erases any previous content |
| **append mode (`"a"`)** | Opens for adding to the end without erasing |
| **data logging** | Automatically recording sensor values to a file over time |
| **relay** | An electrically-controlled switch using a small signal to control a larger circuit |
| **NO (Normally Open)** | Relay terminal disconnected when relay is off, connected when on |
| **timestamp** | A value recording when something happened |
| **CSV** | Comma-Separated Values — a text format for table data |
