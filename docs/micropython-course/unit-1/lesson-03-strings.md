---
title: "Lesson 3 - Working with Strings"
layout: default
nav_order: 3
parent: "Unit 1: Getting Started"
grand_parent: MicroPython Course
---

# Lesson 3 — Working with Strings
{: .no_toc }

**Estimated time:** 60 minutes

- TOC
{:toc}

---

## Learning Objectives

By the end of this lesson you will be able to:

1. Join strings together using `+` and f-strings
2. Use string methods: `.upper()`, `.lower()`, `.find()`, `len()`
3. Access individual characters and slices of a string
4. Use `input()` in the Thonny console to get text from the user

---

## Concepts

### What is a String?

A **string** is an ordered sequence of characters. Every character has a **position** (called an **index**) starting at 0.

```
"MicroPython"
 0123456789...
```

So `"MicroPython"[0]` is `'M'`, and `"MicroPython"[5]` is `'P'`.

### Concatenation

**Concatenation** means joining strings together. Use `+`:

```python
first = "Hello"
second = "World"
combined = first + " " + second   # "Hello World"
```

Think of it like linking train carriages together.

### f-Strings (Formatted Strings)

**f-strings** are a cleaner way to embed variable values inside strings. Put `f` before the opening quote, then use `{}` to insert variables:

```python
name = "Alex"
age = 15
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Alex and I am 15 years old.
```

f-strings are almost always easier to read than concatenation. Use them!

### String Methods

A **method** is a function that belongs to an object, called with a dot. Strings come with several built-in tools:

```python
text = "Hello MicroPython"

text.upper()    # "HELLO MICROPYTHON" — all uppercase
text.lower()    # "hello micropython" — all lowercase
len(text)       # 17 — number of characters
text.find("Micro")   # 6 — position where "Micro" starts
text.find("xyz")     # -1 — not found (always -1 for "not found")
```

{: .note }
`len()` is not a method — it's a standalone function. You call it with the string as an argument: `len(text)`, not `text.len()`.

### String Indexing

Access individual characters using square brackets and the index:

```python
word = "Python"
#       012345

print(word[0])   # 'P'  (first character — index 0)
print(word[2])   # 't'
print(word[-1])  # 'n'  (last character — negative index counts from the end)
print(word[-2])  # 'o'
```

### String Slicing

Extract a **slice** (portion) of a string using `[start:end]`. The result includes `start` but *not* `end`:

```python
word = "MicroPython"
#       01234567890

print(word[0:5])   # "Micro"  (indices 0,1,2,3,4)
print(word[5:])    # "Python" (from index 5 to the end)
print(word[:5])    # "Micro"  (from start up to but not including 5)
print(word[::-1])  # "nohtyPorciM" (reversed — step of -1)
```

Slicing never causes an error even if the indices are out of range — it just gives you as much as it can.

### The `input()` Function

`input()` asks the user to type something and returns their text as a **string**:

```python
name = input("What is your name? ")
print(f"Hello, {name}!")
```

{: .important }
**Important — how `input()` works in this course:**
When your ESP32-S3 is connected to Thonny, `input()` works fine — the text you type in the Thonny Shell is sent to the ESP32. However, if the ESP32 is running standalone (not connected to Thonny), there's no keyboard to type on! That's why later lessons use **physical buttons** as the hardware equivalent of input. For now, always use `input()` with Thonny connected.

---

## Guided Walkthrough

### Step 1: Concatenation and f-Strings

Type this in the Script Editor:

```python
first_name = "Alex"
last_name = "Smith"

# Method 1: concatenation with +
full_name = first_name + " " + last_name
print("Hello, " + full_name + "!")

# Method 2: f-string (cleaner!)
print(f"Hello, {full_name}!")
print(f"First: {first_name} | Last: {last_name}")

# f-strings can contain expressions, not just variables
age = 15
print(f"In 5 years you will be {age + 5} years old.")
```

### Step 2: String Methods

```python
message = "Hello MicroPython World"

print(len(message))             # Number of characters: 23
print(message.upper())          # HELLO MICROPYTHON WORLD
print(message.lower())          # hello micropython world

position = message.find("Python")
print(f"'Python' starts at index: {position}")  # 11

not_found = message.find("xyz")
print(f"'xyz' found at: {not_found}")           # -1
```

### Step 3: Indexing and Slicing

```python
word = "MicroPython"

print(f"First character: {word[0]}")      # M
print(f"Sixth character: {word[5]}")      # P
print(f"Last character: {word[-1]}")      # n
print(f"First 5: {word[0:5]}")            # Micro
print(f"From index 5: {word[5:]}")        # Python
print(f"Last 6: {word[-6:]}")             # Python
print(f"Reversed: {word[::-1]}")          # nohtyPorciM
```

### Step 4: Using `input()` — Colour Selector

This program asks the user to type a colour name, then sets the NeoPixel to that colour:

```python
import machine, neopixel, time

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

# Get colour choice from user (via Thonny console)
colour_name = input("Enter a colour (red/green/blue/yellow/purple): ")
colour_name = colour_name.lower()   # Convert to lowercase so "RED" and "red" both work

if colour_name == "red":
    np[0] = (255, 0, 0)
elif colour_name == "green":
    np[0] = (0, 255, 0)
elif colour_name == "blue":
    np[0] = (0, 0, 255)
elif colour_name == "yellow":
    np[0] = (255, 200, 0)
elif colour_name == "purple":
    np[0] = (128, 0, 255)
else:
    np[0] = (255, 255, 255)   # White for unknown
    colour_name = "unknown (showing white)"

np.write()
print(f"LED set to: {colour_name}")
time.sleep(3)
np[0] = (0, 0, 0)
np.write()
```

Run this and type a colour name in the Thonny Shell when prompted. Notice we use `.lower()` so the comparison works regardless of capitalisation.

{: .note }
You're previewing `if/elif/else` here — you'll learn exactly how this works in Unit 2. For now, just notice that it checks which colour was typed and sets the LED accordingly.

### Step 5: String Analysis

```python
sentence = input("Type a sentence: ")

print(f"Your sentence: '{sentence}'")
print(f"Length: {len(sentence)} characters")
print(f"Uppercase version: {sentence.upper()}")
print(f"First character: '{sentence[0]}'")
print(f"Last character: '{sentence[-1]}'")

# Find a word
search = input("Search for a word: ")
pos = sentence.lower().find(search.lower())
if pos == -1:
    print(f"'{search}' was not found.")
else:
    print(f"'{search}' found at position {pos}.")
```

---

## Challenges

### ⭐ Core
Write a program that asks for the user's name. Print:
- Their name in uppercase
- Their name in lowercase
- How many characters their name has
- The first and last characters of their name

### ⭐⭐ Extension
Ask the user to enter a sentence. Then print:
- The total length of the sentence
- The first word (hint: use `.find(" ")` to find the first space, then slice)
- Whether the word `"python"` appears in the sentence (case-insensitive)
- The sentence reversed

### ⭐⭐⭐ Stretch
Create a "word analyser" program. Ask the user for a word. Print:
- The word reversed
- The number of vowels (a, e, i, o, u) — use a loop to count them
- The word in "alternating case" — first character upper, second lower, third upper, etc.
- Whether the word is a palindrome (reads the same forwards and backwards)

---

## Common Mistakes & Debugging

**`TypeError: can only concatenate str (not "int") to str`**
You tried to join a string and a number with `+`. Use an f-string instead: `f"Score: {score}"`, or convert the number: `"Score: " + str(score)`.

**`IndexError: string index out of range`**
You tried to access a character at an index beyond the string's length. Check with `len()` first.

**`.find()` returning -1 unexpectedly**
Check capitalisation! `"hello".find("Hello")` returns `-1`. Use `.lower()` on both strings before comparing.

**`input()` prompt not appearing**
Make sure you're running on the ESP32 through Thonny, not "Local Python 3". Check the bottom-right corner of Thonny.

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| **string** | A sequence of characters enclosed in quotes |
| **concatenation** | Joining two or more strings together using `+` |
| **f-string** | A string prefixed with `f` that allows embedding variable values using `{}` |
| **index** | The position of a character in a string — starts at 0 |
| **negative index** | Counting from the end: -1 is the last character, -2 is second-to-last |
| **slicing** | Extracting a portion of a string using `[start:end:step]` |
| **len()** | A built-in function returning the number of characters in a string |
| **method** | A function attached to an object, called with a dot (e.g., `.upper()`) |
| **input()** | A function that prompts the user to type something and returns their answer as a string |
