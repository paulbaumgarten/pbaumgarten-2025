---
title: "Lesson 24 - Polish and Beyond"
layout: default
nav_order: 3
parent: "Unit 8: Capstone Project"
grand_parent: MicroPython
---

# Lesson 24 — Polish and Beyond
{: .no_toc }

**Estimated time:** 90 minutes

- TOC
{:toc}

---

## Learning Objectives

By the end of this lesson you will be able to:

1. Save and load the high score using file I/O
2. Add a title screen and game-over restart sequence
3. Increase difficulty automatically as the score rises
4. Reflect on everything you've learned across the full course

---

## Milestone 5 — High Score and Status LED

**Goal:** Save the best score to `highscore.txt`. When the game ends, compare the final score to the high score. If it's a new record, update the file. Use the single built-in NeoPixel (GPIO 48) to show current performance by colour.

### Loading the high score

```python
def load_highscore():
    """Load high score from file. Return 0 if file doesn't exist."""
    try:
        with open("highscore.txt", "r") as f:
            return int(f.read().strip())
    except OSError:
        return 0   # File doesn't exist yet
```

`try/except` lets you handle errors gracefully. `OSError` is raised when a file doesn't exist — here we just return 0 as the default.

### Saving the high score

```python
def save_highscore(score):
    """Save score to highscore.txt."""
    with open("highscore.txt", "w") as f:
        f.write(str(score) + "\n")
```

### Using it in game over

```python
def game_over(fb, score, high_score):
    """Flash, report score, update high score."""
    print(f"\nGAME OVER! Score: {score}")

    if score > high_score:
        high_score = score
        save_highscore(high_score)
        print(f"NEW HIGH SCORE: {high_score}!")
    else:
        print(f"High score: {high_score}")

    # Flash red
    for _ in range(3):
        for r in range(8):
            for c in range(8):
                fb[r][c] = (150, 0, 0)
        render(fb)
        time.sleep(0.2)
        clear(fb)
        render(fb)
        time.sleep(0.2)

    return high_score   # Return updated value
```

### Status LED (built-in NeoPixel on GPIO 48)

```python
pin48 = machine.Pin(48, machine.Pin.OUT)
status_np = neopixel.NeoPixel(pin48, 1)

def update_status_led(score):
    """Change built-in NeoPixel colour based on score."""
    if score >= 20:
        status_np[0] = (0, 80, 0)    # Green — doing great
    elif score >= 10:
        status_np[0] = (80, 80, 0)   # Yellow — decent
    elif score >= 5:
        status_np[0] = (80, 20, 0)   # Orange — warming up
    else:
        status_np[0] = (80, 0, 0)    # Red — just started
    status_np.write()
```

Call `update_status_led(score)` each time the score changes.

---

## Milestone 6 — Title Screen, Difficulty, and Restart

### Title screen

Show a pattern on the grid and wait for a button press before starting:

```python
def show_title(fb, btn_left, btn_right):
    """Display a 'D' pattern and wait for button press."""
    # A simple 'D' bitmap
    D_SHAPE = [
        [1, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0, 0],
    ]
    clear(fb)
    for r in range(8):
        for c in range(8):
            if D_SHAPE[r][c]:
                fb[r][c] = (0, 60, 120)
    render(fb)
    print("DODGE  — Press any button to start!")

    # Wait for a button press
    while btn_left.value() == 1 and btn_right.value() == 1:
        time.sleep(0.05)

    clear(fb)
    render(fb)
    time.sleep(0.3)   # Brief pause before game starts
```

### Difficulty scaling

Reduce `TICK_INTERVAL` as the score increases — obstacles fall faster:

```python
def get_tick_interval(score):
    """Return tick interval in seconds based on score."""
    if score < 5:
        return 0.45
    elif score < 10:
        return 0.35
    elif score < 20:
        return 0.25
    else:
        return 0.18   # Maximum speed
```

Use this inside the game loop:
```python
# Replace the fixed TICK_INTERVAL with:
tick_ms = int(get_tick_interval(score) * 1000)
if time.ticks_diff(now, last_tick) >= tick_ms:
    ...
```

### Restart without reboot

Wrap the entire game (title + main loop) in an outer `while True:` so pressing a button on the game-over screen restarts:

```python
high_score = load_highscore()

while True:   # Outer restart loop
    # Show title and wait for button press
    show_title(fb, btn_left, btn_right)

    # Reset state
    player_col = 3
    obs_row    = 0
    obs_col    = random.randint(0, 7)
    score      = 0
    last_tick  = time.ticks_ms()
    running    = True

    # Main game loop
    while running:
        # ... (your full game loop from Milestone 4) ...
        pass

    # Game over — wait for button press to restart
    print("Press any button to play again...")
    while btn_left.value() == 1 and btn_right.value() == 1:
        time.sleep(0.05)
```

---

## Complete Final Game

Below is the complete Dodge game with all milestones included. Study it carefully — every part connects to a lesson you have already completed.

```python
import machine, neopixel, time, random

# --- Hardware ---
grid_pin  = machine.Pin(6,  machine.Pin.OUT)
np        = neopixel.NeoPixel(grid_pin, 64)
pin48     = machine.Pin(48, machine.Pin.OUT)
status_np = neopixel.NeoPixel(pin48, 1)
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

# --- High score file I/O ---
def load_highscore():
    try:
        with open("highscore.txt", "r") as f:
            return int(f.read().strip())
    except OSError:
        return 0

def save_highscore(score):
    with open("highscore.txt", "w") as f:
        f.write(str(score) + "\n")

# --- Status LED ---
def update_status_led(score):
    if score >= 20:
        status_np[0] = (0, 80, 0)
    elif score >= 10:
        status_np[0] = (80, 80, 0)
    elif score >= 5:
        status_np[0] = (80, 20, 0)
    else:
        status_np[0] = (80, 0, 0)
    status_np.write()

# --- Title screen ---
D_SHAPE = [
    [1,1,0,0,0,0,0,0],
    [1,0,1,0,0,0,0,0],
    [1,0,0,1,0,0,0,0],
    [1,0,0,1,0,0,0,0],
    [1,0,0,1,0,0,0,0],
    [1,0,0,1,0,0,0,0],
    [1,0,1,0,0,0,0,0],
    [1,1,0,0,0,0,0,0],
]

def show_title(fb):
    clear(fb)
    for r in range(8):
        for c in range(8):
            if D_SHAPE[r][c]:
                fb[r][c] = (0, 60, 120)
    render(fb)
    print("DODGE — Press any button to start!")
    while btn_left.value() == 1 and btn_right.value() == 1:
        time.sleep(0.05)
    clear(fb)
    render(fb)
    time.sleep(0.3)

# --- Game over ---
def game_over_screen(fb, score, high_score):
    print(f"\nGAME OVER! Score: {score}")
    new_record = False
    if score > high_score:
        high_score = score
        save_highscore(high_score)
        new_record = True
        print(f"*** NEW HIGH SCORE: {high_score} ***")
    else:
        print(f"High score: {high_score}")

    # Flash grid
    for _ in range(4):
        for r in range(8):
            for c in range(8):
                fb[r][c] = (150, 0, 0) if not new_record else (150, 150, 0)
        render(fb)
        time.sleep(0.2)
        clear(fb)
        render(fb)
        time.sleep(0.2)

    return high_score

# --- Difficulty ---
def get_tick_ms(score):
    if score < 5:  return 450
    if score < 10: return 350
    if score < 20: return 250
    return 180

# --- Constants ---
PLAYER_ROW    = 7
PLAYER_COLOUR = (0, 80, 200)
OBS_COLOUR    = (200, 60, 0)

# --- Main program ---
fb         = make_fb()
high_score = load_highscore()
print(f"High score: {high_score}")
update_status_led(0)

while True:   # Outer restart loop
    show_title(fb)

    # Reset game state
    player_col = 3
    obs_row    = 0
    obs_col    = random.randint(0, 7)
    score      = 0
    last_tick  = time.ticks_ms()
    running    = True

    # Inner game loop
    while running:
        # Buttons
        if btn_left.value() == 0:
            player_col -= 1
        if btn_right.value() == 0:
            player_col += 1
        player_col = max(0, min(7, player_col))

        # Obstacle tick
        now = time.ticks_ms()
        if time.ticks_diff(now, last_tick) >= get_tick_ms(score):
            obs_row  += 1
            last_tick = now

            if obs_row > 7:
                obs_row = 0
                obs_col = random.randint(0, 7)
                score  += 1
                update_status_led(score)
                print(f"Score: {score}")

            if obs_row == PLAYER_ROW and obs_col == player_col:
                high_score = game_over_screen(fb, score, high_score)
                running = False

        # Draw
        if running:
            clear(fb)
            set_pixel(fb, PLAYER_ROW, player_col, PLAYER_COLOUR)
            set_pixel(fb, obs_row, obs_col, OBS_COLOUR)
            render(fb)

        time.sleep(0.05)

    # Wait for button press to restart
    print("Press any button to play again...")
    while btn_left.value() == 1 and btn_right.value() == 1:
        time.sleep(0.05)
```

---

## Course Completion — What You've Learned

Congratulations. Here is every concept you have mastered:

| Topic | Lessons |
|-------|---------|
| REPL, print, variables, data types | 1–2 |
| Strings, f-strings, input() | 3 |
| Arithmetic, type conversion | 4 |
| if / elif / else, comparison operators | 5–6 |
| Logical operators (and / or / not) | 7 |
| while loops, for loops, range() | 8–9 |
| break and continue | 10 |
| 1D lists, list methods | 11–12 |
| Functions, parameters, return, scope | 13–16 |
| File reading and writing, CSV, data logging | 17–18 |
| 2D lists, double indexing, nested loops | 19 |
| NeoPixel grid, framebuffer, pixel art | 20 |
| Animation loops, velocity, bouncing, effects | 21 |
| Capstone game design and implementation | 22–24 |

**Hardware you have used:**
- ESP32-S3 with built-in NeoPixel
- Push buttons (active-low, PULL_UP)
- IR obstacle sensor
- HC-SR04 ultrasonic distance sensor
- 9G servo motor (PWM)
- Relay + DC motor
- WS2812B 8×8 NeoPixel grid

---

## Extension Ideas

If you want to keep developing Dodge:

- **Two obstacles at once** — add `obs2_row`, `obs2_col`; a collision with either ends the game
- **Obstacle speed varies** — some obstacles fall faster than others
- **Score displayed on grid** — flash the score as a pattern before restarting
- **Sound effects** — add a buzzer on GPIO with `PWM` for beep on score/game-over
- **Lives system** — start with 3 lives; only game-over after 3 collisions

---

## Key Vocabulary (Full Course Glossary)

| Term | Definition |
|------|-----------|
| **REPL** | Read-Evaluate-Print Loop — interactive Python prompt |
| **variable** | A named storage location for a value |
| **data type** | The kind of value: `int`, `float`, `str`, `bool`, `list` |
| **f-string** | String with `{}` placeholders filled at runtime: `f"x = {x}"` |
| **operator** | Symbol performing an operation: `+`, `-`, `*`, `/`, `//`, `%`, `**` |
| **type conversion** | Changing type: `int()`, `float()`, `str()`, `bool()` |
| **if / elif / else** | Conditional execution based on Boolean expressions |
| **while loop** | Repeats while a condition is True |
| **for loop** | Iterates over a sequence or range |
| **break** | Exits the innermost loop immediately |
| **continue** | Skips the rest of the current loop iteration |
| **list** | Ordered, mutable collection: `[a, b, c]` |
| **index** | Position in a list or string, starting from 0 |
| **function** | Named block of reusable code defined with `def` |
| **parameter** | Variable in a function definition |
| **argument** | Value passed when calling a function |
| **return** | Sends a value back from a function |
| **scope** | Where a variable is visible (local inside function, global outside) |
| **global** | Keyword to access/modify a global variable inside a function |
| **open()** | Built-in function to open a file |
| **with** | Ensures a file is closed after use |
| **read / write / append** | File modes: `"r"`, `"w"`, `"a"` |
| **CSV** | Comma-Separated Values — text format for table data |
| **2D list** | A list of lists — represents a grid |
| **double indexing** | `grid[row][col]` to access a specific cell |
| **nested loop** | A loop inside another loop |
| **framebuffer** | 2D array holding pixel colours before sending to hardware |
| **pixel index** | Flat position of a grid pixel: `row * 8 + col` |
| **animation loop** | Cycle: clear → update → draw → render → wait |
| **velocity** | Pixels moved per frame in an animation |
| **NeoPixel** | WS2812B individually addressable RGB LED |
| **PWM** | Pulse Width Modulation — variable duty cycle signal for servo control |
| **relay** | Electrically-controlled switch; small signal controls a larger circuit |
| **active-low** | Signal is active (triggered) when the pin reads LOW (0) |
| **debounce** | Technique to prevent multiple readings from a single button press |
