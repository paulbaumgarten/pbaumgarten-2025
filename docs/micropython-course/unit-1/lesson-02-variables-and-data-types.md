---
title: "Lesson 2 - Variables and Data Types"
layout: default
nav_order: 2
parent: "Unit 1: Getting Started"
grand_parent: MicroPython
---

# Lesson 2 — Variables and Data Types
{: .no_toc }

**Estimated time:** 60 minutes

- TOC
{:toc}

---

## Learning Objectives

By the end of this lesson you will be able to:

1. Create variables to store values
2. Identify and use the four basic data types: `int`, `float`, `bool`, `str`
3. Use `type()` to check what type a value is
4. Use variables to control the NeoPixel colour

---

## Concepts

### What is a Variable?

A **variable** is a named storage location in your program's memory. Think of it as a labelled jar — the label is the variable name, and the contents are the value stored inside.

```python
score = 0          # A jar labelled "score" containing the number 0
player_name = "Alex"   # A jar labelled "player_name" containing "Alex"
```

You create a variable by writing its name, then `=`, then the value. The `=` is called the **assignment operator** — it puts the value into the variable.

You can then use the variable name anywhere you'd use the value:
```python
score = 42
print(score)        # Prints: 42
print(score + 10)   # Prints: 52
```

**Variable naming rules:**
- Must start with a letter or underscore (not a number)
- Can contain letters, numbers, and underscores
- Case-sensitive: `Score` and `score` are different variables!
- No spaces: use `player_name` not `player name`
- Good names: `score`, `led_brightness`, `is_running`, `sensor_value`
- Bad names: `2score`, `my variable`, `s@core`

### The Four Basic Data Types

Python has four basic **data types** — categories of value:

#### `int` — Integer
Whole numbers. No decimal point. Can be positive, negative, or zero.
```python
score = 0
lives = 3
year = 2025
temperature = -5
max_brightness = 255
```

#### `float` — Floating Point Number
Numbers with a decimal point.
```python
pi = 3.14159
temperature = 36.6
distance = 23.4
percentage = 87.5
```

#### `bool` — Boolean
Only two possible values: `True` or `False` (capital T/F required!). Used for yes/no decisions.
```python
game_over = False
light_is_on = True
player_is_alive = True
```

#### `str` — String
Text — any sequence of characters, enclosed in single or double quotes.
```python
player_name = "Alex"
greeting = "Hello!"
colour = 'red'
message = "The score is 42"   # Even if it contains a number, it's text
```

{: .important }
Notice: `42` is an int (the number forty-two), but `"42"` is a str (the text "42"). They look similar but behave completely differently! You can do maths with `42` but not with `"42"`.

### Checking the Type

Use `type()` to check what type a value or variable is:

```python
print(type(42))         # <class 'int'>
print(type(3.14))       # <class 'float'>
print(type(True))       # <class 'bool'>
print(type("hello"))    # <class 'str'>
```

### Updating Variables

You can change what's in a variable at any time:

```python
score = 0
print(score)    # 0

score = 10
print(score)    # 10

score = score + 5    # Take the current value, add 5, store result back
print(score)    # 15
```

---

## Guided Walkthrough

### Step 1: Creating Variables

Type this in the Script Editor and run it:

```python
# Integer variables
score = 0
lives = 3
year = 2025

# Float variables
temperature = 36.6
pi = 3.14159

# Boolean variables
game_over = False
light_is_on = True

# String variables
player_name = "Alex"
favourite_colour = "blue"

# Print them all
print("Score:", score)
print("Lives:", lives)
print("Temperature:", temperature)
print("Game over?", game_over)
print("Player name:", player_name)
```

### Step 2: Checking Types

Try these in the REPL:

```python
>>> print(type(42))
<class 'int'>
>>> print(type(3.14))
<class 'float'>
>>> print(type(True))
<class 'bool'>
>>> print(type("hello"))
<class 'str'>
>>> x = 100
>>> print(type(x))
<class 'int'>
```

### Step 3: Variables with the NeoPixel

This is where variables become genuinely useful. Instead of hardcoding numbers, use variables:

```python
import machine
import neopixel
import time

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

# Store the colour components in variables
red_value = 200
green_value = 0
blue_value = 150

np[0] = (red_value, green_value, blue_value)
np.write()
print("LED colour set!")
print("Red:", red_value)
print("Green:", green_value)
print("Blue:", blue_value)

time.sleep(3)
np[0] = (0, 0, 0)
np.write()
```

Try changing `red_value`, `green_value`, `blue_value` and re-running. Notice how much easier it is to adjust the colour when it's stored in named variables.

### Step 4: Updating Variables — Brightness Fade

Here's a more advanced example that updates a variable inside a loop to create a fading effect:

```python
import machine
import neopixel
import time

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

# Start with brightness 0 and increase to 255 in steps
brightness = 0

# This is a loop (we'll cover loops properly in Unit 3)
# For now, just notice that brightness changes each iteration
for step in range(11):
    brightness = step * 25          # 0, 25, 50, 75, ... 250
    np[0] = (brightness, 0, 0)      # Red, getting brighter
    np.write()
    print("Brightness:", brightness)
    time.sleep(0.2)

# Turn off
np[0] = (0, 0, 0)
np.write()
print("Done!")
```

---

## Challenges

### ⭐ Core
Create variables for your name, age, and favourite colour. Print a sentence using all three: `"My name is [name], I am [age] years old, and my favourite colour is [colour]."`. Then look up the RGB values for your favourite colour and display it on the LED.

### ⭐⭐ Extension
Create a boolean variable `is_bright = True`. Use it to decide whether the LED shows full brightness (255) or dim (40). Then change the variable to `False` and re-run — the LED should change automatically. Print which mode is active.

### ⭐⭐⭐ Stretch
Create variables for three different colours (look up RGB values for each). Show each colour for 2 seconds, printing the colour name and its R, G, B values each time. After showing all three, show a "white" for 1 second (hint: white is all three channels at full brightness), then turn off.

---

## Common Mistakes & Debugging

**`NameError: name 'x' is not defined`**
You used a variable before creating it, or you misspelled the name. Python is case-sensitive: `Score` and `score` are completely different.

**Using `=` to compare instead of `==`**
`=` *assigns* a value. `==` *checks if two things are equal*. You'll use `==` in Unit 2 when you start making decisions.

**Forgetting quotes around strings**
`name = Alex` — Python thinks `Alex` is a variable name. You need `name = "Alex"`.

**Variable names with spaces**
`player name = "Alex"` is a syntax error. Use underscores: `player_name = "Alex"`.

**`TypeError` when mixing types**
`"My score is " + 42` will fail because you can't add a string and an integer directly. You'll learn how to fix this in Lesson 4.

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| **variable** | A named storage location in memory that holds a value |
| **assignment** | Giving a variable a value using the `=` operator |
| **data type** | The category of a value — int, float, bool, or str |
| **int** | Integer — a whole number with no decimal point |
| **float** | Floating-point number — a number with a decimal point |
| **bool** | Boolean — can only be `True` or `False` |
| **str** | String — a sequence of text characters, written in quotes |
| **type()** | A built-in function that returns the data type of a value |
| **case-sensitive** | Uppercase and lowercase letters are treated as different: `Score ≠ score` |
