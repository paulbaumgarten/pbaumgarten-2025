---
title: "Lesson 23 - The Game Loop"
layout: default
nav_order: 2
parent: "Unit 8: Capstone Project"
grand_parent: MicroPython Course
---

# Lesson 23 — The Game Loop
{: .no_toc }

**Estimated time:** 90 minutes

- TOC
{:toc}

---

## Learning Objectives

By the end of this lesson you will be able to:

1. Add falling obstacles to the game
2. Detect collision between the player and an obstacle
3. Implement a game-over state
4. Track and display the score

---

## Milestone 3 — Falling Obstacles

**Goal:** Obstacles fall from the top of the grid. A new obstacle spawns at a random column when the previous one reaches the bottom (or is destroyed). The player must dodge them.

### How obstacles work

Each obstacle is a single pixel that starts at row 0 and moves down by 1 each "tick". A tick is a game step — you'll control how often a tick happens with a timer.

Store the obstacle as two variables:
```python
obs_row = 0
obs_col = random.randint(0, 7)
```

Each game tick, increase `obs_row`. When `obs_row > 7`, the obstacle went off the bottom — respawn it at the top in a new random column and add 1 to the score.

### The two-speed problem

The player responds to button presses many times per second. But obstacles should fall slowly — maybe once every 0.3–0.5 seconds.

**Solution: track last tick time.**

```python
import time

TICK_INTERVAL = 0.4   # Seconds between obstacle moves
last_tick = time.ticks_ms()

while True:
    # --- Button input (every frame) ---
    if btn_left.value() == 0:
        player_col -= 1
    if btn_right.value() == 0:
        player_col += 1
    player_col = max(0, min(7, player_col))

    # --- Obstacle tick (every TICK_INTERVAL seconds) ---
    now = time.ticks_ms()
    if time.ticks_diff(now, last_tick) >= int(TICK_INTERVAL * 1000):
        obs_row += 1
        last_tick = now

        if obs_row > 7:   # Obstacle reached the bottom — respawn
            obs_row = 0
            obs_col = random.randint(0, 7)
            score += 1
            print(f"Score: {score}")

    # --- Draw ---
    clear(fb)
    set_pixel(fb, PLAYER_ROW, player_col, PLAYER_COLOUR)
    set_pixel(fb, obs_row, obs_col, (200, 0, 0))   # Red obstacle
    render(fb)

    time.sleep(0.05)   # 20fps display loop
```

### Starter additions for Milestone 3

Add these near the top of your game (after imports and hardware setup):

```python
import random

# Obstacle state
obs_row = 0
obs_col = random.randint(0, 7)

# Score
score = 0

# Timing
TICK_INTERVAL = 0.4   # Seconds per obstacle step
last_tick = time.ticks_ms()
```

### Obstacle colour

Use red `(200, 0, 0)` or orange `(200, 80, 0)` so it's clearly different from the blue player.

### Test it
Obstacles should fall slowly from the top. When one exits the bottom, a new one appears at a random column at the top. The score printed in the REPL increases each time you successfully dodge one.

---

## Milestone 4 — Collision Detection

**Goal:** If the obstacle is at the same row and column as the player, the game ends.

### When does collision happen?

After moving the obstacle (inside the tick section), check:

```python
if obs_row == PLAYER_ROW and obs_col == player_col:
    game_over()
```

### The `game_over()` function

This function should:
1. Flash the grid red 3 times (or show a red X pattern)
2. Print the final score to the REPL
3. Stop the game loop (return from the function, or set a flag)

```python
def game_over(fb, np, score):
    """Flash the grid and end the game."""
    print(f"\nGAME OVER! Final score: {score}")

    # Flash red 3 times
    for _ in range(3):
        for r in range(8):
            for c in range(8):
                fb[r][c] = (150, 0, 0)
        render(fb)
        time.sleep(0.2)
        clear(fb)
        render(fb)
        time.sleep(0.2)
```

### Restructuring with a flag

Use a `running` variable to control the main loop:

```python
running = True

while running:
    # ... buttons ...
    # ... tick ...

    # Inside tick, after moving obstacle:
    if obs_row == PLAYER_ROW and obs_col == player_col:
        game_over(fb, np, score)
        running = False   # Exit the loop after game_over

    # ... draw ...
    time.sleep(0.05)

print("Game ended. Restart to play again.")
```

### Test it
Let an obstacle hit the player. The grid should flash red, the REPL should print the final score, and the game should stop.

---

## Milestone 4 Complete: Full Code So Far

Here is the complete structure after Milestones 1–4. Fill in the function bodies you wrote in Lesson 22:

```python
import machine, neopixel, time, random

# --- Hardware ---
grid_pin = machine.Pin(6, machine.Pin.OUT)
np = neopixel.NeoPixel(grid_pin, 64)
btn_left  = machine.Pin(0,  machine.Pin.IN, machine.Pin.PULL_UP)
btn_right = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

# --- Framebuffer helpers ---
def make_fb():
    return [[(0, 0, 0)] * 8 for _ in range(8)]

def render(fb):
    for r in range(8):
        for c in range(8):
            np[r * 8 + c] = fb[r][c]
    np.write()

def clear(fb):
    for r in range(8):
        for c in range(8):
            fb[r][c] = (0, 0, 0)

def set_pixel(fb, row, col, colour):
    if 0 <= row < 8 and 0 <= col < 8:
        fb[row][col] = colour

# --- Game over ---
def game_over(fb, score):
    print(f"\nGAME OVER! Final score: {score}")
    for _ in range(3):
        for r in range(8):
            for c in range(8):
                fb[r][c] = (150, 0, 0)
        render(fb)
        time.sleep(0.2)
        clear(fb)
        render(fb)
        time.sleep(0.2)

# --- Constants ---
PLAYER_ROW    = 7
PLAYER_COLOUR = (0, 80, 200)
OBS_COLOUR    = (200, 0, 0)
TICK_INTERVAL = 0.4   # seconds

# --- Initial state ---
fb         = make_fb()
player_col = 3
obs_row    = 0
obs_col    = random.randint(0, 7)
score      = 0
last_tick  = time.ticks_ms()
running    = True

print("Dodge! Use buttons to avoid the red obstacles.")
print("Score increases each time an obstacle passes.")

# --- Main loop ---
while running:
    # Button input
    if btn_left.value() == 0:
        player_col -= 1
    if btn_right.value() == 0:
        player_col += 1
    player_col = max(0, min(7, player_col))

    # Obstacle tick
    now = time.ticks_ms()
    if time.ticks_diff(now, last_tick) >= int(TICK_INTERVAL * 1000):
        obs_row += 1
        last_tick = now

        if obs_row > 7:
            obs_row = 0
            obs_col = random.randint(0, 7)
            score += 1
            print(f"Score: {score}")

        # Collision check
        if obs_row == PLAYER_ROW and obs_col == player_col:
            game_over(fb, score)
            running = False

    # Draw
    if running:
        clear(fb)
        set_pixel(fb, PLAYER_ROW, player_col, PLAYER_COLOUR)
        set_pixel(fb, obs_row, obs_col, OBS_COLOUR)
        render(fb)

    time.sleep(0.05)
```

---

## Reflection Questions

1. Why is `TICK_INTERVAL` separate from the `time.sleep(0.05)` at the bottom of the loop?
2. What would happen if you check collision **before** moving the obstacle instead of after?
3. How would you add a second obstacle to make the game harder?
4. The obstacle can randomly spawn in the same column as the player at row 0. Is this fair? How could you prevent it?
5. What does `time.ticks_diff(now, last_tick)` do? Why is `ticks_diff` better than simple subtraction for timers?

---

## Common Mistakes

**Obstacle moves every frame (too fast)**
You forgot the `ticks_diff` check. The obstacle should only move inside the `if time.ticks_diff(...)` block.

**Collision never triggers**
Double-check that you compare `obs_row == PLAYER_ROW` (not `obs_row == 7`). If `PLAYER_ROW` is 7 and `obs_row` is also 7, they should match. Use `print(obs_row, obs_col, player_col)` to debug.

**`NameError: name 'random' is not defined`**
Add `import random` at the top.

**Game over triggers immediately**
The obstacle spawns at `(0, obs_col)` and the player starts at `(7, 3)`. They can't be in the same position on frame 1 unless both are at row 7 — which is only possible if your initial `obs_row` is 7. Make sure `obs_row = 0` initially.
