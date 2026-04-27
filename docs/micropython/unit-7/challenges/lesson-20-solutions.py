# Lesson 20 Challenge Solutions
# NeoPixel Grid

import machine, neopixel, time

pin = machine.Pin(6, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 64)

def make_fb():
    return [[(0,0,0)]*8 for _ in range(8)]

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

# ⭐ Core: Cross (plus sign)
fb = make_fb()
CROSS_COLOUR = (0, 70, 70)   # Teal

# Middle rows (3 and 4) — horizontal bars
for c in range(8):
    set_pixel(fb, 3, c, CROSS_COLOUR)
    set_pixel(fb, 4, c, CROSS_COLOUR)

# Middle cols (3 and 4) — vertical bars
for r in range(8):
    set_pixel(fb, r, 3, CROSS_COLOUR)
    set_pixel(fb, r, 4, CROSS_COLOUR)

render(fb)
print("Cross displayed. Wait 3 seconds...")
time.sleep(3)

clear(fb)
render(fb)

# ⭐⭐ Extension: Traffic light display
def fill_rect(fb, row, col, height, width, colour):
    for r in range(row, row+height):
        for c in range(col, col+width):
            set_pixel(fb, r, c, colour)

traffic_light_sequence = [
    ("red",        (80,0,0),  (0,0,0),   (0,0,0),   3.0),
    ("red+amber",  (80,0,0),  (60,30,0), (0,0,0),   1.0),
    ("green",      (0,0,0),   (0,0,0),   (0,60,0),  3.0),
    ("amber",      (0,0,0),   (60,30,0), (0,0,0),   1.0),
]

print("Traffic light cycling (3 times)...")
for cycle in range(3):
    for label, red_col, amber_col, green_col, duration in traffic_light_sequence:
        clear(fb)
        fill_rect(fb, 0, 2, 2, 4, red_col)    # Top section — red
        fill_rect(fb, 3, 2, 2, 4, amber_col)  # Mid section — amber
        fill_rect(fb, 6, 2, 2, 4, green_col)  # Bot section — green
        render(fb)
        print(f"  Cycle {cycle+1}: {label}")
        time.sleep(duration)

clear(fb)
render(fb)

# ⭐⭐⭐ Stretch: Digit display (0–9)
# Each digit is an 8×8 bitmap
ZERO = [
    [0,1,1,1,1,1,0,0],
    [1,0,0,0,0,0,1,0],
    [1,0,0,0,0,1,1,0],
    [1,0,0,0,1,0,1,0],
    [1,0,0,1,0,0,1,0],
    [1,0,1,0,0,0,1,0],
    [1,1,0,0,0,0,1,0],
    [0,1,1,1,1,1,0,0],
]
ONE = [
    [0,0,1,0,0,0,0,0],
    [0,1,1,0,0,0,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,1,0,0,0,0,0],
    [0,0,1,0,0,0,0,0],
    [0,1,1,1,0,0,0,0],
]
TWO = [
    [0,1,1,1,1,0,0,0],
    [1,0,0,0,0,1,0,0],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0,0],
    [0,0,1,0,0,0,0,0],
    [0,1,0,0,0,0,0,0],
    [1,1,1,1,1,1,0,0],
]
THREE = [
    [0,1,1,1,1,0,0,0],
    [1,0,0,0,0,1,0,0],
    [0,0,0,0,0,1,0,0],
    [0,0,1,1,1,0,0,0],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,0,1,0,0],
    [1,0,0,0,0,1,0,0],
    [0,1,1,1,1,0,0,0],
]

DIGITS = [ZERO, ONE, TWO, THREE]
DIGIT_NAMES = ["0", "1", "2", "3"]
DIGIT_COLOUR = (0, 60, 100)

def draw_bitmap(fb, bitmap, colour):
    for r in range(8):
        for c in range(8):
            fb[r][c] = colour if bitmap[r][c] else (0,0,0)

print("\nDisplaying digits 0–3...")
for i, digit in enumerate(DIGITS):
    draw_bitmap(fb, digit, DIGIT_COLOUR)
    render(fb)
    print(f"  Digit: {DIGIT_NAMES[i]}")
    time.sleep(1.5)

clear(fb)
render(fb)
print("Done.")
