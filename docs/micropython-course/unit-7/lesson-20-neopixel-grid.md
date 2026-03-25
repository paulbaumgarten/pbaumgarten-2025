---
title: "Lesson 20 - The 8×8 NeoPixel Grid"
layout: default
nav_order: 2
parent: "Unit 7: The Grid"
grand_parent: MicroPython Course
---

# Lesson 20 — The 8×8 NeoPixel Grid
{: .no_toc }

**Estimated time:** 90 minutes

- TOC
{:toc}

---

## Learning Objectives

By the end of this lesson you will be able to:

1. Wire the WS2812B 8×8 NeoPixel grid to the ESP32
2. Convert row/column coordinates to a pixel index using `index = row * 8 + col`
3. Use a framebuffer (2D list of colours) to prepare a frame before sending it
4. Draw pixel art, borders, and shapes on the grid
5. Perform batch updates to minimise flicker

---

## New Hardware: WS2812B 8×8 NeoPixel Grid

### Wiring

| Grid Pin | Connect To |
|---------|------------|
| 5V      | 5V (not 3.3V!) |
| GND     | GND |
| DIN     | GPIO 6 |

{: .important }
The 8×8 grid needs 5V — it won't work reliably from 3.3V. All 64 LEDs at full white can draw ~3.8A, so **never** set all pixels to `(255, 255, 255)` at full brightness. Keep colours dim (max 50–80 per channel) during development.

---

## Concepts

### 64 Pixels, One Long Strip

The 8×8 grid is actually a single strip of 64 LEDs snaked back and forth. The `neopixel` module treats them as a flat list: `np[0]` through `np[63]`.

To control pixel at row `r`, column `c`, you need to find its index in that flat list.

### Row × 8 + Col

```
Row 0:  index  0  1  2  3  4  5  6  7
Row 1:  index  8  9 10 11 12 13 14 15
Row 2:  index 16 17 18 19 20 21 22 23
...
Row 7:  index 56 57 58 59 60 61 62 63
```

The formula: `index = row * 8 + col`

```python
def pixel_index(row, col):
    return row * 8 + col
```

So `pixel_index(2, 3)` = `2 * 8 + 3` = `19`.

### Setting Up the Grid

```python
import machine, neopixel

NUM_PIXELS = 64
pin = machine.Pin(6, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, NUM_PIXELS)
```

Set a single pixel and update:
```python
np[pixel_index(3, 4)] = (0, 100, 0)   # Dim green at row 3, col 4
np.write()
```

### The Framebuffer Pattern

Instead of setting individual pixels and calling `.write()` for each one, build the entire frame in a 2D list first, then send it all at once. This avoids flicker.

```python
# Framebuffer: 8 rows × 8 columns of (R, G, B) tuples
fb = [[(0, 0, 0)] * 8 for _ in range(8)]

# Draw into the framebuffer — no hardware update yet
fb[3][4] = (0, 100, 0)
fb[0][0] = (100, 0, 0)

# Send the whole frame at once
def render(fb, np):
    for row in range(8):
        for col in range(8):
            np[row * 8 + col] = fb[row][col]
    np.write()

render(fb, np)
```

**Why framebuffer?**
- Pixels are updated instantly and simultaneously
- No partially-lit frames visible to the eye
- Easy to reason about — the 2D list mirrors the physical grid

### Clearing the Grid

```python
def clear(fb):
    for row in range(8):
        for col in range(8):
            fb[row][col] = (0, 0, 0)
```

### Drawing Helpers

```python
def set_pixel(fb, row, col, colour):
    """Set one pixel (bounds-checked)."""
    if 0 <= row < 8 and 0 <= col < 8:
        fb[row][col] = colour

def draw_border(fb, colour):
    """Draw a 1-pixel border around the edge."""
    for c in range(8):
        set_pixel(fb, 0, c, colour)   # Top row
        set_pixel(fb, 7, c, colour)   # Bottom row
    for r in range(8):
        set_pixel(fb, r, 0, colour)   # Left column
        set_pixel(fb, r, 7, colour)   # Right column

def draw_rect(fb, row, col, height, width, colour):
    """Fill a rectangle."""
    for r in range(row, row + height):
        for c in range(col, col + width):
            set_pixel(fb, r, c, colour)
```

---

## Guided Walkthrough

### Step 1: Basic Setup and Single Pixels

```python
import machine, neopixel, time

NUM_PIXELS = 64
pin = machine.Pin(6, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, NUM_PIXELS)

def pixel_index(row, col):
    return row * 8 + col

# Clear all pixels
np.fill((0, 0, 0))
np.write()
time.sleep(0.5)

# Light up the four corners
corners = [(0,0), (0,7), (7,0), (7,7)]
for (r, c) in corners:
    np[pixel_index(r, c)] = (80, 0, 80)   # Purple

np.write()
time.sleep(2)

# Light up the centre 2×2
for r in range(3, 5):
    for c in range(3, 5):
        np[pixel_index(r, c)] = (0, 80, 0)   # Green

np.write()
time.sleep(2)

np.fill((0, 0, 0))
np.write()
```

### Step 2: Framebuffer Setup

```python
import machine, neopixel, time

pin = machine.Pin(6, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 64)

# --- Framebuffer helpers ---

def make_fb():
    return [[(0, 0, 0)] * 8 for _ in range(8)]

def render(fb):
    for row in range(8):
        for col in range(8):
            np[row * 8 + col] = fb[row][col]
    np.write()

def set_pixel(fb, row, col, colour):
    if 0 <= row < 8 and 0 <= col < 8:
        fb[row][col] = colour

def clear(fb):
    for row in range(8):
        for col in range(8):
            fb[row][col] = (0, 0, 0)

# --- Draw something ---

fb = make_fb()

# Diagonal stripe
for i in range(8):
    set_pixel(fb, i, i, (80, 80, 0))   # Yellow diagonal

render(fb)
time.sleep(2)

clear(fb)
render(fb)
```

### Step 3: Border and Rectangle

```python
def draw_border(fb, colour):
    for c in range(8):
        set_pixel(fb, 0, c, colour)
        set_pixel(fb, 7, c, colour)
    for r in range(1, 7):
        set_pixel(fb, r, 0, colour)
        set_pixel(fb, r, 7, colour)

def fill_rect(fb, row, col, height, width, colour):
    for r in range(row, row + height):
        for c in range(col, col + width):
            set_pixel(fb, r, c, colour)

# Demo
fb = make_fb()
draw_border(fb, (0, 50, 100))    # Blue border
fill_rect(fb, 2, 2, 4, 4, (80, 0, 0))   # Red inner square
render(fb)
time.sleep(3)

clear(fb)
render(fb)
```

### Step 4: Pixel Art from a Bitmap

A bitmap is a 2D list of 0s and 1s (or 0s and colours). Map them to actual RGB values when rendering:

```python
# Smiley face bitmap (1 = on, 0 = off)
SMILEY = [
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
]

def draw_bitmap(fb, bitmap, colour):
    for row in range(8):
        for col in range(8):
            if bitmap[row][col] == 1:
                fb[row][col] = colour
            else:
                fb[row][col] = (0, 0, 0)

fb = make_fb()
draw_bitmap(fb, SMILEY, (80, 80, 0))   # Yellow smiley
render(fb)
time.sleep(3)

clear(fb)
render(fb)
```

### Step 5: Colour Wash

Cycle through all pixels with a colour sweep:

```python
import time

COLOURS = [
    (60, 0, 0),   # Red
    (0, 60, 0),   # Green
    (0, 0, 60),   # Blue
    (60, 60, 0),  # Yellow
    (0, 60, 60),  # Cyan
    (60, 0, 60),  # Magenta
]

fb = make_fb()

for colour in COLOURS:
    for row in range(8):
        for col in range(8):
            fb[row][col] = colour
        render(fb)
        time.sleep(0.05)
    time.sleep(0.3)

clear(fb)
render(fb)
```

---

## Challenges

### ⭐ Core
Draw a cross (plus sign) on the 8×8 grid: the middle row (row 3 or 4) and middle column (col 3 or 4) should be lit. Choose your own colour. Use the framebuffer pattern.

### ⭐⭐ Extension
Create a traffic light display. Use the top section of the grid for red, middle for amber, and bottom for green. Cycle through red (3s) → red+amber (1s) → green (3s) → amber (1s) → red (3s), repeating 3 full cycles. Each colour should fill a rough 2-row rectangle in the appropriate area.

### ⭐⭐⭐ Stretch
Display the digits 0–9 as pixel art on the 8×8 grid, one at a time, cycling through them with a 1-second delay. Define each digit as an 8×8 bitmap (1=on, 0=off). Use a list of bitmaps: `DIGITS = [ZERO, ONE, TWO, ...]`. You only need to define 3 or more digits to count for full marks.

---

## Common Mistakes & Debugging

**Grid doesn't light up / wrong pixels**
Check that you're using GPIO 6 (not GPIO 48 — that's the single built-in pixel). Confirm the DIN wire is connected to data-in (not data-out) on the grid.

**`np[64]` — IndexError**
The grid has indices 0–63. `row * 8 + col` with row=7, col=7 gives 63 — the maximum. Any row or col outside 0–7 goes out of bounds. Always use `set_pixel()` with bounds checking.

**Flickering display**
You're probably calling `np.write()` inside your inner loop. Call it once per frame, after building the entire framebuffer.

**Grid too bright / colours washed out**
Keep individual channel values ≤ 80 for comfortable viewing. Full white (255, 255, 255) on all 64 pixels draws ~3.8A and can brownout your USB power.

**Row and column swapped**
`index = row * 8 + col` — row first, column second. If your art is rotated 90°, you have them backwards.

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| **WS2812B** | The LED driver chip inside each NeoPixel — controls colour from a single data wire |
| **pixel index** | The flat position of a pixel in the NeoPixel strip: `row * 8 + col` |
| **framebuffer** | A 2D array holding the colour of every pixel before sending to hardware |
| **render** | Copy the framebuffer to the NeoPixel strip and call `.write()` |
| **bitmap** | A 2D array of 0s and 1s used to define a shape or character |
| **batch update** | Setting all pixels then writing once — prevents partial frames from showing |
