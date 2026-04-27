---
title: "Lesson 8 - While Loops"
layout: default
nav_order: 1
parent: "Unit 3: Loops and Repetition"
grand_parent: MicroPython
---

# Lesson 8 — While Loops
{: .no_toc }

**Estimated time:** 75 minutes

- TOC
{:toc}

---

## Learning Objectives

By the end of this lesson you will be able to:

1. Use a `while` loop to repeat code while a condition is True
2. Use counter variables and the `+=` operator
3. Write an infinite loop (`while True:`) and understand why it's useful
4. Create fading and pulsing LED effects

---

## Concepts

### What is a Loop?

A **loop** repeats a block of code. Think of a washing machine programme — it keeps running cycles until done. Without loops, you'd have to copy-paste the same code dozens or hundreds of times.

### The `while` Loop

A `while` loop keeps running **as long as its condition is True**. When the condition becomes False, the loop ends and the program continues after it.

```
while condition:
    code to run (loop body)
    ...
(code here runs after the loop ends)
```

**Example — countdown:**
```python
count = 5
while count > 0:
    print(count)
    count -= 1    # count = count - 1
print("Blastoff!")
```

Output: `5 4 3 2 1 Blastoff!`

**What happens step by step:**
1. Check: `5 > 0`? Yes → print 5, count becomes 4
2. Check: `4 > 0`? Yes → print 4, count becomes 3
3. Check: `3 > 0`? Yes → print 3, count becomes 2
4. Check: `2 > 0`? Yes → print 2, count becomes 1
5. Check: `1 > 0`? Yes → print 1, count becomes 0
6. Check: `0 > 0`? No → exit loop
7. Print "Blastoff!"

### Counter Variables and `+=`

A **counter variable** tracks how many times the loop has run. The **`+=` operator** is shorthand for "add and assign":

```python
count = 0
count += 1    # Same as: count = count + 1
count += 5    # Same as: count = count + 5

x = 10
x -= 3        # Same as: x = x - 3  → x = 7
x *= 2        # Same as: x = x * 2  → x = 14
```

### Infinite Loops with `while True:`

`while True:` creates an **infinite loop** — it runs forever because `True` is always `True`. This is actually *very useful* in embedded programming! Your microcontroller should keep running:

```python
import time

while True:
    print("I run forever!")
    time.sleep(1)
```

Press **Ctrl+C** in Thonny to stop an infinite loop.

{: .important }
In embedded programming, infinite loops are normal and expected. A program controlling a temperature sensor should loop forever — that's its job. On a laptop, infinite loops are usually bugs, but on a microcontroller, they're the design.

### Input Validation Loop

A common pattern: keep asking until the user gives a valid answer:

```python
while True:
    age = int(input("Enter your age (1-120): "))
    if 1 <= age <= 120:
        break    # Exit the loop — we have a valid answer
    print("That doesn't look right. Try again.")

print(f"You are {age} years old.")
```

(`break` will be covered fully in Lesson 10 — for now, just know it exits the loop.)

---

## Guided Walkthrough

### Step 1: Basic while Loop

```python
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1
print("Loop complete!")
```

Try changing `5` to different values. What happens with `count <= 0`?

### Step 2: Countdown + LED Flash

```python
import machine, neopixel, time

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

countdown = 10
while countdown > 0:
    print(f"T minus {countdown}...")

    # Flash colour based on urgency
    if countdown <= 3:
        np[0] = (255, 0, 0)    # Red — urgent
    elif countdown <= 6:
        np[0] = (255, 150, 0)  # Orange — getting close
    else:
        np[0] = (0, 255, 0)    # Green — plenty of time

    np.write()
    time.sleep(0.9)
    np[0] = (0, 0, 0)
    np.write()
    time.sleep(0.1)

    countdown -= 1

print("LAUNCH!")
np[0] = (255, 255, 255)   # White flash
np.write()
time.sleep(0.5)
np[0] = (0, 0, 0)
np.write()
```

### Step 3: LED Breathing Effect

A smooth fade in and out using a `while` loop with a direction variable:

```python
import machine, neopixel, time

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

brightness = 0
direction = 5    # How much to change per step (+5 = getting brighter)

print("Breathing blue LED... Ctrl+C to stop")
while True:
    np[0] = (0, 0, brightness)
    np.write()

    brightness += direction

    # Bounce at the limits
    if brightness >= 255:
        direction = -5
        brightness = 255
    elif brightness <= 0:
        direction = 5
        brightness = 0

    time.sleep(0.02)   # Small delay for smooth animation
```

### Step 4: While Loop with Button

Wait until the button is pressed, then do something:

```python
import machine, neopixel, time
from machine import Pin

pin48 = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin48, 1)
button = Pin(0, Pin.IN, Pin.PULL_UP)

print("Press the button to start the countdown!")

# Wait for button press
while button.value() == 1:   # While button NOT pressed...
    time.sleep(0.05)          # ...keep waiting

print("Button pressed! Starting countdown...")
np[0] = (255, 200, 0)   # Yellow
np.write()
time.sleep(0.5)

# Now do the countdown
count = 5
while count > 0:
    print(f"  {count}...")
    np[0] = (255, int(200 * count/5), 0)   # Orange fading to red
    np.write()
    time.sleep(1)
    count -= 1

np[0] = (0, 255, 0)
np.write()
print("GO!")
time.sleep(2)
np[0] = (0, 0, 0)
np.write()
```

---

## Challenges

### ⭐ Core
Write a while loop that counts from 1 to 20. For each even number, flash the LED green for 0.1 seconds. For odd numbers, just print the number. After the loop, print how many flashes occurred.

### ⭐⭐ Extension
Create a "patience tester" — the LED slowly pulses green (breathing effect). The program counts how many complete breath cycles occur. After 5 cycles, it turns the LED gold and prints "You are very patient!" If the user presses Ctrl+C before 5 cycles, they see the partial count.

### ⭐⭐⭐ Stretch
Create a **reaction timer** in two phases:
1. The LED shows a random colour for a random time (0.5–3 seconds using `time.sleep(random.uniform(0.5, 3))`)
2. Then the LED turns WHITE — the user presses Enter as fast as possible
3. Use `time.ticks_ms()` to measure reaction time between the LED going white and Enter being pressed
4. Repeat 5 times and print the average reaction time and best time

---

## Common Mistakes & Debugging

**Infinite loop that never ends**
You forgot to update the loop variable! `while count < 5:` with no `count += 1` inside will run forever. Check your loop body modifies the variable being tested.

**Off-by-one error**
`while count < 5` runs for count = 0, 1, 2, 3, 4 (5 times). `while count <= 5` runs for 0, 1, 2, 3, 4, 5 (6 times). Decide carefully which you want.

**Loop body not indented**
All code inside the loop must be indented by the same amount.

**Press Ctrl+C if stuck**
If your loop runs forever and you didn't intend it to, press Ctrl+C in Thonny to stop it.

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| **while loop** | Repeats a block of code as long as a condition is True |
| **loop body** | The indented block of code that runs on each iteration |
| **iteration** | One complete execution of the loop body |
| **counter variable** | A variable used to count loop iterations |
| **`+=`** | Shorthand for "add and assign": `x += 1` means `x = x + 1` |
| **infinite loop** | A loop that runs forever — `while True:` — common in embedded programs |
| **`break`** | Immediately exits the current loop (covered fully in Lesson 10) |
