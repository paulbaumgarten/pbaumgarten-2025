---
title: "Lesson 1 - Hello MicroPython"
layout: default
nav_order: 1
parent: "Unit 1: Getting Started"
grand_parent: MicroPython Course
---

# Lesson 1 — Hello MicroPython
{: .no_toc }

**Estimated time:** 60 minutes

- TOC
{:toc}

---

## Learning Objectives

By the end of this lesson you will be able to:

1. Use the REPL in Thonny to run Python commands interactively
2. Write and run a Python script using `print()`
3. Add comments to your code
4. Control the built-in NeoPixel LED with colour commands

---

## Concepts

### What is a Microcontroller?

Your ESP32-S3 is a **microcontroller** — a tiny computer built into a single chip. Unlike a laptop, it has no screen, no keyboard, no hard drive, and barely any memory. But it's incredibly good at running one program repeatedly, very efficiently, while controlling physical hardware like LEDs and sensors.

Think of a microcontroller as the brain inside a smart device — it's in your TV remote, your microwave's timer, your car's engine management system, and millions of other products.

### What is MicroPython?

**MicroPython** is a lean version of the Python programming language, specially written to run on tiny microcontrollers. It understands almost all the same Python you'd write on a laptop — so everything you learn here applies to Python in general.

The key difference: instead of your laptop running the program, the *ESP32-S3* runs it. You write code in Thonny, send it to the board, and the board executes it.

### What is the REPL?

The **REPL** (pronounced "rep-ul") stands for **Read-Eval-Print Loop**. It's the interactive `>>>` prompt at the bottom of Thonny. Type a line of Python, press Enter, and it runs immediately and shows the result. It's brilliant for experimenting.

### The `print()` Function

`print()` is a **function** — a named command that does something. `print()` displays whatever you put inside the brackets in the console (the Shell panel at the bottom of Thonny). It's the simplest way to get your program to communicate back to you.

```python
print("Hello, world!")    # Displays: Hello, world!
print(42)                 # Displays: 42
print(2 + 2)              # Displays: 4
```

### Comments

A **comment** is a line (or part of a line) that Python completely ignores. It starts with `#`. Comments are notes for humans — for yourself, or anyone else reading your code.

```python
# This whole line is a comment - Python ignores it
print("Hello!")   # This part after # is also a comment
```

Good programmers write lots of comments. Get into the habit early.

---

## Hardware Setup

No wiring needed for this lesson. The ESP32-S3 has a **built-in NeoPixel RGB LED** already connected to GPIO pin 48 on the board. It can show any colour.

{: .note }
**GPIO** stands for General Purpose Input/Output — the numbered pins on your ESP32-S3 that you can control with code.

---

## Guided Walkthrough

### Step 1: Your First REPL Commands

Make sure your ESP32-S3 is connected and Thonny shows `>>>` in the Shell panel. Click in the Shell and type each line, pressing Enter after each:

```python
>>> print("Hello, MicroPython!")
Hello, MicroPython!
>>> print(2 + 2)
4
>>> print("My name is", "Alex")
My name is Alex
```

Notice that `print()` can take multiple items separated by commas — it joins them with a space.

### Step 2: Your First Script

Now let's write a proper script (not just REPL commands). Click in the **Script Editor** panel at the top of Thonny and type:

```python
# My first MicroPython program
# Comments start with # and are ignored by Python

print("Hello from my ESP32-S3!")
print("I am learning MicroPython")
print(2025 - 2010)
print("The answer to everything is", 6 * 7)
```

Click the **Run** button (green triangle) or press F5. You should see four lines of output in the Shell.

{: .highlight }
**Congratulations!** You just wrote and ran your first MicroPython program on real embedded hardware. That's something to be proud of.

### Step 3: Light Up the NeoPixel

Now for the exciting part — let's control the hardware. Type this in the Script Editor:

```python
import machine
import neopixel
import time

# The built-in NeoPixel is on GPIO pin 48
pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)   # 1 LED on this pin

# Set the colour to red
# Colours are (Red, Green, Blue) — each value from 0 to 255
np[0] = (255, 0, 0)
np.write()                        # Send the colour to the LED
print("The LED should be red now!")

time.sleep(2)                     # Wait 2 seconds

# Turn it off
np[0] = (0, 0, 0)
np.write()
print("LED is off")
```

Run it. The LED should glow red for 2 seconds, then turn off.

**Understanding the new lines:**
- `import machine` — loads the `machine` module, which talks to the ESP32's hardware
- `import neopixel` — loads the NeoPixel driver
- `import time` — loads timing functions like `time.sleep()`
- `np = neopixel.NeoPixel(pin, 1)` — creates a NeoPixel controller for 1 LED on that pin
- `np[0] = (255, 0, 0)` — sets LED 0 to red (full red, no green, no blue)
- `np.write()` — actually sends the colour data to the LED (nothing shows until you call this!)
- `time.sleep(2)` — pauses execution for 2 seconds

### Step 4: Add More Colours

Extend the program to cycle through red, green, and blue:

```python
import machine
import neopixel
import time

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

# Colours: (Red, Green, Blue), values 0-255
print("Red...")
np[0] = (255, 0, 0)
np.write()
time.sleep(1)

print("Green...")
np[0] = (0, 255, 0)
np.write()
time.sleep(1)

print("Blue...")
np[0] = (0, 0, 255)
np.write()
time.sleep(1)

print("Yellow...")
np[0] = (255, 200, 0)   # Mix red and green for yellow
np.write()
time.sleep(1)

print("Off.")
np[0] = (0, 0, 0)
np.write()
```

{: .note }
**Mixing colours:** The NeoPixel is an RGB LED — Red + Green + Blue mixed together create any colour. Think of it like mixing light, not paint. Red + Green = Yellow. Red + Blue = Magenta. Green + Blue = Cyan. All three = White.

---

## Challenges

### ⭐ Core
Make the LED flash yellow and off **three times**. Each flash should be on for 0.5 seconds and off for 0.5 seconds. Add a `print()` statement to show which flash you're on.

### ⭐⭐ Extension
Create a "rainbow" sequence that shows at least 6 different colours, spending 0.4 seconds on each. Print the name of each colour as it's displayed.

### ⭐⭐⭐ Stretch
Create a **traffic light** sequence: red for 3 seconds, amber/orange for 1 second, green for 3 seconds. Repeat the full sequence 3 times, printing the current light at each step. After all 3 cycles, turn the LED off and print "Traffic light demo complete."

---

## Common Mistakes & Debugging

**"SyntaxError: invalid syntax"**
Check your brackets, quote marks, and colons. Python is very precise. A missing `"` or `)` causes this.

**"ModuleNotFoundError: No module named 'neopixel'"**
You're probably running Python on your *computer* rather than MicroPython on the ESP32. Check the bottom-right corner of Thonny — it should show your ESP32, not "Local Python 3".

**LED doesn't light up**
- Check that `np.write()` is called after setting the colour
- Make sure pin number is 48 (the built-in LED)
- Try running just `np[0] = (255, 0, 0); np.write()` in the REPL to test

**LED shows wrong colour**
Remember the order is (Red, Green, Blue). `(255, 0, 0)` is red, not `(0, 0, 255)`.

**Program runs too fast / too slow**
Adjust the numbers in `time.sleep()`. `time.sleep(1)` = 1 second, `time.sleep(0.5)` = half a second.

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| **microcontroller** | A tiny computer chip designed to run a single program and control hardware |
| **MicroPython** | A version of Python designed to run on microcontrollers |
| **REPL** | The interactive `>>>` prompt where Python commands run immediately |
| **print()** | A function that displays text or values in the console |
| **comment** | A line starting with `#` that Python ignores — notes for humans |
| **import** | Loads a module (collection of pre-written code) so you can use it |
| **GPIO** | General Purpose Input/Output — the numbered pins on the ESP32 you control with code |
| **NeoPixel** | An RGB LED with a built-in controller chip, controlled by a single data wire |
| **function** | A named command that performs an action — `print()`, `time.sleep()`, etc. |
| **module** | A collection of related functions and tools — `machine`, `neopixel`, `time` |
