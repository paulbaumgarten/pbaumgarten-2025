# Dodge — Complete Game
# Unit 8 Capstone Project — Reference Solution
#
# Hardware:
#   8×8 NeoPixel grid → GPIO 6 (5V, GND)
#   Built-in NeoPixel → GPIO 48
#   Left button       → GPIO 0  (other leg to GND)
#   Right button      → GPIO 14 (other leg to GND)
#
# Controls:
#   Left button  → move player left
#   Right button → move player right
#   Press any button at title or game-over screen to start/restart

import machine, neopixel, time, random

# ---------------------------------------------------------------------------
# Hardware
# ---------------------------------------------------------------------------
grid_pin  = machine.Pin(6,  machine.Pin.OUT)
np        = neopixel.NeoPixel(grid_pin, 64)
pin48     = machine.Pin(48, machine.Pin.OUT)
status_np = neopixel.NeoPixel(pin48, 1)
btn_left  = machine.Pin(0,  machine.Pin.IN, machine.Pin.PULL_UP)
btn_right = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

# ---------------------------------------------------------------------------
# Framebuffer
# ---------------------------------------------------------------------------
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

# ---------------------------------------------------------------------------
# File I/O — high score
# ---------------------------------------------------------------------------
HIGHSCORE_FILE = "dodge_highscore.txt"

def load_highscore():
    try:
        with open(HIGHSCORE_FILE, "r") as f:
            return int(f.read().strip())
    except OSError:
        return 0

def save_highscore(score):
    with open(HIGHSCORE_FILE, "w") as f:
        f.write(str(score) + "\n")

# ---------------------------------------------------------------------------
# Status LED (built-in NeoPixel)
# ---------------------------------------------------------------------------
def update_status_led(score):
    if score >= 20:
        colour = (0, 80, 0)     # Green — excellent
    elif score >= 10:
        colour = (80, 80, 0)    # Yellow — good
    elif score >= 5:
        colour = (80, 20, 0)    # Orange — warming up
    else:
        colour = (80, 0, 0)     # Red — just started
    status_np[0] = colour
    status_np.write()

# ---------------------------------------------------------------------------
# Title screen
# ---------------------------------------------------------------------------
D_BITMAP = [
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
            if D_BITMAP[r][c]:
                fb[r][c] = (0, 60, 120)
    render(fb)
    print("DODGE — Press any button to start!")
    while btn_left.value() == 1 and btn_right.value() == 1:
        time.sleep(0.05)
    clear(fb)
    render(fb)
    time.sleep(0.3)

# ---------------------------------------------------------------------------
# Game over screen
# ---------------------------------------------------------------------------
def game_over_screen(fb, score, high_score):
    new_record = score > high_score
    if new_record:
        high_score = score
        save_highscore(high_score)
        print(f"\n*** NEW HIGH SCORE: {high_score} ***")
    else:
        print(f"\nGame over! Score: {score}  (High score: {high_score})")

    flash_colour = (150, 120, 0) if new_record else (150, 0, 0)

    for _ in range(4):
        for r in range(8):
            for c in range(8):
                fb[r][c] = flash_colour
        render(fb)
        time.sleep(0.2)
        clear(fb)
        render(fb)
        time.sleep(0.2)

    return high_score

# ---------------------------------------------------------------------------
# Difficulty: obstacle tick interval in ms
# ---------------------------------------------------------------------------
def get_tick_ms(score):
    if score < 5:   return 450
    if score < 10:  return 350
    if score < 20:  return 250
    if score < 30:  return 200
    return 160

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
PLAYER_ROW    = 7
PLAYER_COLOUR = (0, 80, 200)    # Blue
OBS_COLOUR    = (200, 60, 0)    # Orange

# ---------------------------------------------------------------------------
# Main program
# ---------------------------------------------------------------------------
fb         = make_fb()
high_score = load_highscore()
print(f"Dodge! High score: {high_score}")
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

    update_status_led(score)

    # Inner game loop
    while running:
        # --- Button input ---
        if btn_left.value() == 0:
            player_col -= 1
        if btn_right.value() == 0:
            player_col += 1
        player_col = max(0, min(7, player_col))

        # --- Obstacle tick ---
        now = time.ticks_ms()
        if time.ticks_diff(now, last_tick) >= get_tick_ms(score):
            obs_row  += 1
            last_tick = now

            if obs_row > 7:   # Obstacle exited bottom — player dodged it
                obs_row = 0
                obs_col = random.randint(0, 7)
                score  += 1
                update_status_led(score)
                print(f"Score: {score}")

            # Collision check
            if obs_row == PLAYER_ROW and obs_col == player_col:
                high_score = game_over_screen(fb, score, high_score)
                running = False

        # --- Draw ---
        if running:
            clear(fb)
            set_pixel(fb, PLAYER_ROW, player_col, PLAYER_COLOUR)
            set_pixel(fb, obs_row, obs_col, OBS_COLOUR)
            render(fb)

        time.sleep(0.05)   # ~20 fps

    # Wait for button press before restarting
    print("Press any button to play again...")
    while btn_left.value() == 1 and btn_right.value() == 1:
        time.sleep(0.05)
