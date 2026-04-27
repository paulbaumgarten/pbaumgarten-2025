---
title: "Lesson 17 - Reading Files"
layout: default
nav_order: 1
parent: "Unit 6: Working with Files"
grand_parent: MicroPython
---

# Lesson 17 — Reading Files
{: .no_toc }

**Estimated time:** 75 minutes

- TOC
{:toc}

---

## Learning Objectives

By the end of this lesson you will be able to:

1. Open a text file for reading using `open()` and `with`
2. Read file contents using `.read()`, `.readline()`, `.readlines()`
3. Parse simple CSV data from a file
4. Load configuration settings from a file

---

## Concepts

### Why Files?

Variables live in **RAM** — they exist while your program runs, then vanish when power is cut. **Files** live in **flash memory** (or on a hard drive) — they persist.

Use files for:
- **High scores** — remember the best score between sessions
- **Configuration** — store settings that shouldn't be in code
- **Logging** — record sensor readings over time
- **Data** — question banks, word lists, colour palettes

### The MicroPython Filesystem

The ESP32-S3 has a small filesystem in its flash memory. You can see and manage files in **Thonny's Files panel** (View > Files). The "MicroPython device" section shows files on the ESP32.

To create a file on the ESP32:
1. Write content in Thonny's editor
2. Click **File > Save As**
3. Choose **"MicroPython device"** and save with the right filename

### `open()` and File Modes

```python
f = open("filename.txt", "r")   # Open for reading
```

**File modes:**
- `"r"` — Read. File must exist. Default mode.
- `"w"` — Write. Creates new or **overwrites** existing file.
- `"a"` — Append. Adds to end without overwriting.

### The `with` Statement

The `with` statement automatically closes the file when the block ends, even if an error occurs:

```python
# Without with (must manually close):
f = open("data.txt", "r")
content = f.read()
f.close()   # Easy to forget!

# With with (cleaner, safer):
with open("data.txt", "r") as f:
    content = f.read()
# File is automatically closed here
```

**Always use `with` for file operations.**

### Reading Methods

**`.read()`** — reads the entire file as one string:
```python
with open("data.txt", "r") as f:
    all_text = f.read()
```

**`.readline()`** — reads one line at a time (includes `\n`):
```python
with open("data.txt", "r") as f:
    line1 = f.readline()   # First line
    line2 = f.readline()   # Second line
```

**`.readlines()`** — reads all lines, returns a list:
```python
with open("data.txt", "r") as f:
    lines = f.readlines()  # List of strings, each ending with \n
```

**Iterating line by line (most memory-efficient):**
```python
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())   # strip() removes \n and spaces
```

### `.strip()` — Always Strip Your Lines

When reading lines, each one ends with `\n` (newline character). Use `.strip()` to remove it:

```python
line = "Hello World\n"
clean = line.strip()   # "Hello World"
```

`.strip()` removes whitespace (spaces, tabs, newlines) from both ends.

---

## Guided Walkthrough

### Step 1: Create a Test File on the ESP32

In Thonny, create a new file and type this content:
```
Hello from the filesystem!
This is line 2.
This is line 3.
MicroPython is fun.
```

Save it to the **MicroPython device** as `message.txt`.

### Step 2: Read the Whole File

```python
# Read the entire file at once
with open("message.txt", "r") as f:
    content = f.read()

print(content)
print("---")
print(f"Total characters: {len(content)}")
```

### Step 3: Read Line by Line

```python
with open("message.txt", "r") as f:
    lines = f.readlines()

print(f"Number of lines: {len(lines)}")

for i, line in enumerate(lines):
    clean = line.strip()
    print(f"Line {i+1}: '{clean}'")
```

### Step 4: Configuration File

This pattern — storing settings in a file instead of hardcoding them — is used everywhere in real software.

Create a file called `config.txt` on the ESP32:
```
led_colour=0,128,255
brightness=80
message=Hello from config!
repeat=3
```

Read and use it:
```python
import machine, neopixel, time

config = {}

with open("config.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line and "=" in line:   # Skip blank lines and malformed ones
            key, value = line.split("=", 1)   # Split at FIRST = only
            config[key.strip()] = value.strip()

print("Loaded config:", config)

# Use the config
pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

# Parse the LED colour (stored as "R,G,B")
r, g, b = config["led_colour"].split(",")
np[0] = (int(r), int(g), int(b))
np.write()

# Show the message n times
repeat = int(config["repeat"])
msg = config["message"]
for i in range(repeat):
    print(f"Message {i+1}: {msg}")

time.sleep(3)
np[0] = (0, 0, 0)
np.write()
```

### Step 5: Reading CSV Data

Create `scores.csv` on the ESP32:
```
name,score,grade
Alice,87,B
Bob,92,A
Charlie,63,C
Diana,78,B
```

Parse and display it:
```python
with open("scores.csv", "r") as f:
    lines = f.readlines()

# First line is the header
headers = lines[0].strip().split(",")
print("Headers:", headers)

# Parse data rows
students = []
for line in lines[1:]:    # Skip header
    line = line.strip()
    if line:
        parts = line.split(",")
        student = {
            "name":  parts[0],
            "score": int(parts[1]),
            "grade": parts[2]
        }
        students.append(student)

print(f"\nLoaded {len(students)} students:")
for s in students:
    print(f"  {s['name']:10s}: {s['score']:3d} ({s['grade']})")

# Analysis
scores = [s["score"] for s in students]
print(f"\nClass average: {sum(scores)/len(scores):.1f}")
print(f"Highest: {max(scores)}")
print(f"Lowest:  {min(scores)}")
```

{: .note }
The `{s['name']:10s}` format spec in the f-string pads the name to 10 characters wide, making output nicely aligned.

---

## Challenges

### ⭐ Core
Create a file `colours.txt` on the ESP32 with 6 colour names (one per line). Write a program that reads the file and picks a random colour (`import random; random.choice(lines)`). Print it and show a matching LED colour (you'll need a lookup in your code for each name).

### ⭐⭐ Extension
Create a `highscores.txt` CSV file with 5 players and scores (format: `name,score`). Read the file, sort by score descending, and print a numbered leaderboard. Display the LED colour based on the top score: gold (`255,215,0`) if >90, silver (`180,180,180`) if >70, bronze (`205,127,50`) if lower.

### ⭐⭐⭐ Stretch
Create a `quiz.txt` file with 5 questions and answers in the format `question|answer`. Write a quiz program that reads each question, asks the user (via `input()`), and checks the answer (case-insensitive). Track score. After all questions, print the result and display an appropriate LED colour (green ≥80%, yellow ≥50%, red <50%).

---

## Common Mistakes & Debugging

**`OSError: [Errno 2] ENOENT`**
File not found. Check: (1) the file is saved to the **ESP32**, not your computer, (2) the filename is spelled correctly (case-sensitive!), (3) refresh Thonny's file browser.

**Lines have unexpected `\n` in them**
Always use `.strip()` when reading lines. `line.strip()` removes the trailing newline.

**`ValueError: not enough values to unpack`**
Your `.split(",")` produced fewer parts than expected. Check the file format — a line might be blank or malformed.

**File panel not showing your file**
Click the refresh/reload button in Thonny's Files panel. If the file still doesn't appear, it may have been saved to your computer instead of the ESP32.

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| **filesystem** | The system that organises and stores files — the ESP32 has one in flash memory |
| **open()** | Built-in function that opens a file and returns a file object |
| **file mode** | How the file is opened: `"r"` read, `"w"` write, `"a"` append |
| **with statement** | Ensures a file is properly closed after use, even if an error occurs |
| **read()** | Reads entire file contents as a string |
| **readlines()** | Reads all lines and returns them as a list |
| **strip()** | Removes whitespace (including `\n`) from the start and end of a string |
| **CSV** | Comma-Separated Values — a text format for tabular data |
| **parse** | Extract structured data from raw text |
