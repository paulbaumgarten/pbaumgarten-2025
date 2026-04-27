---
title: "Lesson 21 - Grid Animations"
layout: default
nav_order: 3
parent: "Unit 7: The Grid"
grand_parent: MicroPython
---

# Lesson 21 — Grid Animations
{: .no_toc }

**Estimated time:** 90 minutes

- TOC
{:toc}

---

## Learning Objectives

By the end of this lesson you will be able to:

1. Build an animation loop that clears, draws, and renders at a target frame rate
2. Move a sprite across the grid using position variables
3. Implement bouncing using velocity and boundary detection
4. Create a falling-rain effect using a list of active drops
5. Build a rotating spinner using trigonometry (optional extension)

---

## Concepts

### The Animation Loop

Every animation follows the same structure:

```
while True:
    clear the framebuffer
    update the state (move things)
    draw the state into the framebuffer
    render the framebuffer to hardware
    wait (to control speed)
```

```python
import time

while True:
    clear(fb)          # 1. blank canvas
    update_state()     # 2. move/change things
    draw_state(fb)     # 3. paint into buffer
    render(fb)         # 4. send to hardware
    time.sleep(0.05)   # 5. ~20 frames/second
```

**Why clear first?** If you don't clear, pixels from the previous frame stay visible. Unless you're intentionally creating trails, always start with a blank canvas.

### Position and Velocity

A moving dot needs a **position** (where it is) and a **velocity** (how far it moves each frame):

```python
row = 0
col = 0
row_vel = 1    # Move down 1 pixel per frame
col_vel = 1    # Move right 1 pixel per frame
```

Each frame, update position:
```python
row += row_vel
col += col_vel
```

### Bouncing

When a dot hits a wall, reverse the appropriate velocity component:

```python
if row <= 0 or row >= 7:
    row_vel = -row_vel   # Reverse vertical direction

if col <= 0 or col >= 7:
    col_vel = -col_vel   # Reverse horizontal direction
```

**Analogy:** A billiard ball bouncing off the cushions. When it hits a horizontal wall, the vertical speed reverses but horizontal is unchanged, and vice versa.

### Frame Rate Control

`time.sleep(0.05)` gives 20 frames per second. Adjust the delay to speed up or slow down:
- `0.1` → 10 fps (slow, sluggish)
- `0.05` → 20 fps (smooth for simple animations)
- `0.033` → 30 fps (smoother, uses more CPU)

---

## Guided Walkthrough

### Step 1: Moving Dot

```python
import machine, neopixel, time

pin = machine.Pin(6, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 64)

def make_fb():
    return [[(0, 0, 0)] * 8 for _ in range(8)]

def render(fb):
    for row in range(8):
        for col in range(8):
            np[row * 8 + col] = fb[row][col]
    np.write()

def clear(fb):
    for row in range(8):
        for col in range(8):
            fb[row][col] = (0, 0, 0)

def set_pixel(fb, row, col, colour):
    if 0 <= row < 8 and 0 <= col < 8:
        fb[row][col] = colour

# --- Moving dot ---
fb = make_fb()
dot_row = 0
dot_col = 0

for _ in range(64):    # Traverse the whole grid
    clear(fb)
    set_pixel(fb, dot_row, dot_col, (0, 80, 0))
    render(fb)
    time.sleep(0.1)

    dot_col += 1
    if dot_col >= 8:
        dot_col = 0
        dot_row += 1
    if dot_row >= 8:
        dot_row = 0

clear(fb)
render(fb)
```

### Step 2: Bouncing Ball

```python
import machine, neopixel, time

pin = machine.Pin(6, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 64)
fb = [[(0,0,0)]*8 for _ in range(8)]

def render(fb):
    for r in range(8):
        for c in range(8):
            np[r*8+c] = fb[r][c]
    np.write()

def clear(fb):
    for r in range(8):
        for c in range(8):
            fb[r][c] = (0,0,0)

def set_pixel(fb, r, c, colour):
    if 0 <= r < 8 and 0 <= c < 8:
        fb[r][c] = colour

# Ball state
ball_row = 3
ball_col = 0
row_vel = 1
col_vel = 1

for _ in range(300):   # Run for 300 frames
    # Bounce off edges
    if ball_row <= 0 or ball_row >= 7:
        row_vel = -row_vel
    if ball_col <= 0 or ball_col >= 7:
        col_vel = -col_vel

    ball_row += row_vel
    ball_col += col_vel

    # Clamp to valid range (safety)
    ball_row = max(0, min(7, ball_row))
    ball_col = max(0, min(7, ball_col))

    clear(fb)
    set_pixel(fb, ball_row, ball_col, (80, 40, 0))   # Orange ball
    render(fb)
    time.sleep(0.08)

clear(fb)
render(fb)
```

### Step 3: Trail Effect

Instead of clearing fully, fade all pixels slightly to create a motion trail:

```python
import machine, neopixel, time

pin = machine.Pin(6, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 64)
fb = [[(0,0,0)]*8 for _ in range(8)]

def render(fb):
    for r in range(8):
        for c in range(8):
            np[r*8+c] = fb[r][c]
    np.write()

def fade(fb, factor=0.7):
    """Multiply every channel by factor to create fade-out trail."""
    for r in range(8):
        for c in range(8):
            col = fb[r][c]
            fb[r][c] = (
                int(col[0] * factor),
                int(col[1] * factor),
                int(col[2] * factor)
            )

def set_pixel(fb, r, c, colour):
    if 0 <= r < 8 and 0 <= c < 8:
        fb[r][c] = colour

ball_row = 3
ball_col = 0
row_vel = 1
col_vel = 1

for _ in range(300):
    if ball_row <= 0 or ball_row >= 7:
        row_vel = -row_vel
    if ball_col <= 0 or ball_col >= 7:
        col_vel = -col_vel

    ball_row += row_vel
    ball_col += col_vel
    ball_row = max(0, min(7, ball_row))
    ball_col = max(0, min(7, ball_col))

    fade(fb, 0.6)   # Fade instead of clear
    set_pixel(fb, ball_row, ball_col, (0, 80, 80))   # Cyan ball
    render(fb)
    time.sleep(0.08)

# Clear on exit
fb = [[(0,0,0)]*8 for _ in range(8)]
render(fb)
```

### Step 4: Falling Rain

Each raindrop is a `[row, col]` pair. Each frame, move drops down by 1. When a drop falls off the bottom, remove it and add a new one at the top.

```python
import machine, neopixel, time, random

pin = machine.Pin(6, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 64)
fb = [[(0,0,0)]*8 for _ in range(8)]

def render(fb):
    for r in range(8):
        for c in range(8):
            np[r*8+c] = fb[r][c]
    np.write()

def clear(fb):
    for r in range(8):
        for c in range(8):
            fb[r][c] = (0,0,0)

def set_pixel(fb, r, c, colour):
    if 0 <= r < 8 and 0 <= c < 8:
        fb[r][c] = colour

# Start with 4 drops at random columns and rows
drops = [[random.randint(0, 7), random.randint(0, 7)] for _ in range(4)]

for _ in range(200):
    # Move each drop down
    for drop in drops:
        drop[0] += 1   # Move down

    # Remove drops that fell off bottom; add new ones at top
    drops = [d for d in drops if d[0] < 8]
    while len(drops) < 4:
        drops.append([0, random.randint(0, 7)])

    # Draw
    clear(fb)
    for drop in drops:
        r, c = drop
        set_pixel(fb, r, c, (0, 80, 0))    # Green drop
        set_pixel(fb, r-1, c, (0, 40, 0))  # Dimmer tail
        set_pixel(fb, r-2, c, (0, 15, 0))  # Faintest tail

    render(fb)
    time.sleep(0.12)

clear(fb)
render(fb)
```

### Step 5: Sweeping Row Scanner

Light up one row at a time, sweeping back and forth (like a scanning effect):

```python
import machine, neopixel, time

pin = machine.Pin(6, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 64)
fb = [[(0,0,0)]*8 for _ in range(8)]

def render(fb):
    for r in range(8):
        for c in range(8):
            np[r*8+c] = fb[r][c]
    np.write()

def clear(fb):
    for r in range(8):
        for c in range(8):
            fb[r][c] = (0,0,0)

SCAN_COLOUR = (0, 0, 80)

rows = list(range(8)) + list(range(6, 0, -1))   # 0,1,2,3,4,5,6,7,6,5,4,3,2,1

for _ in range(5):    # 5 sweeps
    for scan_row in rows:
        clear(fb)
        for c in range(8):
            fb[scan_row][c] = SCAN_COLOUR
        render(fb)
        time.sleep(0.06)

clear(fb)
render(fb)
```

---

## Challenges

### ⭐ Core
Create a "pong paddle" effect: a 3-pixel-tall paddle bounces up and down on the left column of the grid. The paddle moves down, hits the bottom edge, then reverses and moves up, bounces off the top, and continues. Use the framebuffer pattern.

### ⭐⭐ Extension
Build a two-ball bouncing animation. Each ball has its own `row`, `col`, `row_vel`, `col_vel`. They bounce independently. Give them different colours. Add a trail effect (fade instead of clear). Run for 500 frames.

### ⭐⭐⭐ Stretch
Implement a **Snake** game preview (no user input needed — it's automatic). A snake starts at `(0,0)` and follows a pre-determined path that covers the whole grid in a spiral. Define the path as a list of `(row, col)` tuples. The snake has a body of 5 pixels. As the head moves, the tail follows. Light the head brighter than the body. When the snake reaches the end of the path, it disappears off the grid.

---

## Common Mistakes & Debugging

**Animation doesn't move / stays frozen**
You're probably calling `render()` but not updating the position variables before drawing. Check your loop order: update first, then draw.

**Ball immediately gets stuck at edge**
The bounce check triggers repeatedly. Make sure you clamp the position **after** reversing velocity:
```python
if ball_row <= 0 or ball_row >= 7:
    row_vel = -row_vel
ball_row += row_vel            # Move after reversing
ball_row = max(0, min(7, ball_row))   # Safety clamp
```

**Rain drops cluster on same column**
`random.randint(0, 7)` can produce the same column for multiple drops. This is fine — in real rain, drops overlap. If you want spread, track used columns.

**Framerate too slow / too fast**
Adjust the `time.sleep()` value. For a 20fps animation use `0.05`. For testing, use `0.2` so you can see what's happening step by step.

---

## Key Vocabulary

| Term | Definition |
|------|-----------|
| **animation loop** | A repeating cycle of: clear → update state → draw → render → wait |
| **velocity** | How many pixels a sprite moves per frame (row_vel, col_vel) |
| **bouncing** | Reversing velocity when a sprite hits an edge |
| **trail** | Residual glow from previous frames, created by fading instead of clearing |
| **sprite** | A small graphical object (like a dot or character) in an animation |
| **frame rate** | How many complete images are displayed per second |
