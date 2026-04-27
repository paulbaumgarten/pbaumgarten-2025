---
title: "Lesson 22 - Capstone Setup"
layout: default
nav_order: 1
parent: "Unit 8: Capstone Project"
grand_parent: MicroPython
---

# Lesson 22 — Capstone Setup
{: .no_toc }

**Estimated time:** 75 minutes

- TOC
{:toc}

---

## Learning Objectives

By the end of this lesson you will be able to:

1. Set up all hardware (grid + two buttons) for the Dodge game
2. Create a working framebuffer system with render/clear helpers
3. Display the player dot at the correct starting position
4. Move the player left and right with button presses

---

## Hardware Setup

### Wiring

| Component | Pin | Connect To |
|-----------|-----|------------|
| NeoPixel grid DIN | GPIO 6 | DIN on grid |
| NeoPixel grid | 5V | 5V |
| NeoPixel grid | GND | GND |
| Left button leg 1 | GPIO 0 | Left button leg 2 |
| Left button leg 2 | GND | GND |
| Right button leg 1 | GPIO 14 | Right button leg 2 |
| Right button leg 2 | GND | GND |

{: .note }
Both buttons use **internal pull-up resistors** (`Pin.PULL_UP`). When pressed, `button.value()` returns `0`. When released, it returns `1`. This is "active low".

---

## Milestone 1 — Static Display

**Goal:** The grid initialises and shows the player dot at row 7 (bottom), column 3 (near-centre left).

### What you need

1. Import `machine`, `neopixel`, `time`
2. Create the NeoPixel object on GPIO 6 with 64 pixels
3. Create helper functions: `make_fb()`, `render(fb)`, `clear(fb)`, `set_pixel(fb, r, c, colour)`
4. Set `player_col = 3` (starting column)
5. The player is always on **row 7** (bottom row)
6. In your main code: clear the framebuffer, set the player pixel, render

### Player colour

Use a bright colour that's easy to see — e.g. `(0, 80, 200)` (light blue).

### Starter structure

```python
import machine, neopixel, time

# --- Hardware setup ---
grid_pin = machine.Pin(6, machine.Pin.OUT)
np = neopixel.NeoPixel(grid_pin, 64)

# --- Framebuffer helpers ---

def make_fb():
    # Return an 8x8 2D list of (0,0,0) tuples
    pass   # Replace with real code

def render(fb):
    # Copy fb to np and call np.write()
    pass

def clear(fb):
    # Set every cell in fb to (0,0,0)
    pass

def set_pixel(fb, row, col, colour):
    # Set fb[row][col] = colour if row/col are valid
    pass

# --- Game constants ---
PLAYER_ROW = 7
PLAYER_COLOUR = (0, 80, 200)

# --- Initial state ---
player_col = 3
fb = make_fb()

# --- Milestone 1: show the player ---
clear(fb)
set_pixel(fb, PLAYER_ROW, player_col, PLAYER_COLOUR)
render(fb)

print("Milestone 1 done - player shown at row 7, col 3")
```

### Test it
Run the code. You should see one blue pixel at the bottom of the grid.

---

## Milestone 2 — Button Movement

**Goal:** The left button moves the player left (decrease `player_col`). The right button moves the player right (increase `player_col`). The player cannot move off the edge (col must stay 0–7).

### What you need

1. Add button setup:
   ```python
   btn_left  = machine.Pin(0,  machine.Pin.IN, machine.Pin.PULL_UP)
   btn_right = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
   ```
2. Add a game loop (`while True:`)
3. Inside the loop:
   - Check if left button is pressed (`btn_left.value() == 0`) → decrease `player_col`
   - Check if right button is pressed → increase `player_col`
   - Clamp `player_col` so it stays within 0–7
   - Clear, draw player, render
   - Small sleep (e.g. `time.sleep(0.15)`) for debounce

### Hints

**Clamping:** Use `max()` and `min()`:
```python
player_col = max(0, min(7, player_col))
```

**Why sleep 0.15?** Without a delay, the loop runs thousands of times per second. A single press would move the player many columns. 150ms feels responsive without overshooting.

### Code skeleton for Milestone 2

Add this below your Milestone 1 code (replace the static display with the loop):

```python
# --- Milestone 2: movement ---
btn_left  = machine.Pin(0,  machine.Pin.IN, machine.Pin.PULL_UP)
btn_right = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    # Read buttons
    if btn_left.value() == 0:
        player_col -= 1
    if btn_right.value() == 0:
        player_col += 1

    # Clamp to grid
    player_col = max(0, min(7, player_col))

    # Draw
    clear(fb)
    set_pixel(fb, PLAYER_ROW, player_col, PLAYER_COLOUR)
    render(fb)

    time.sleep(0.15)
```

### Test it
Press the left button — the player dot should move left. Press the right button — it moves right. Holding a button moves it one step per 0.15 seconds. It should stop at the edges.

---

## Reflection Questions

Before moving to Lesson 23, make sure you can answer:

1. Why is the player always on row 7?
2. What happens if you remove the `max(0, min(7, player_col))` clamp? Try it.
3. What does `make_fb()` return? What type is it?
4. Why do we call `clear(fb)` before drawing the player each frame?
5. What would happen if you set `PLAYER_ROW = 0` instead of `7`?

---

## Common Mistakes

**Nothing appears on the grid**
Check GPIO 6 is correct and the grid is powered from 5V (not 3.3V). Print "rendered" inside `render()` to confirm it's being called.

**Player jumps multiple columns per press**
The loop is running too fast without a delay. Add `time.sleep(0.15)` at the bottom of the loop.

**Left and right are reversed**
Either the buttons are wired to the wrong GPIO, or you have the logic swapped. Check that GPIO 0 = left, GPIO 14 = right.

**`AttributeError: 'NoneType' object has no attribute ...`**
Your helper functions return `None` because you have `pass` instead of real code. Fill in `make_fb()`, `render()`, `clear()`, and `set_pixel()`.
