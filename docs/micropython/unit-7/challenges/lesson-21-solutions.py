# Lesson 21 Challenge Solutions
# Grid Animations

import machine, neopixel, time, random

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

fb = make_fb()

# ⭐ Core: Bouncing paddle on left column
print("Bouncing paddle on left column...")
paddle_top = 0
paddle_vel = 1
PADDLE_COLOUR = (0, 80, 50)

for _ in range(200):
    # Bounce
    if paddle_top <= 0:
        paddle_vel = 1
    if paddle_top >= 5:   # 3-pixel paddle, max top = 5
        paddle_vel = -1
    paddle_top += paddle_vel

    clear(fb)
    for i in range(3):   # 3-pixel tall paddle
        set_pixel(fb, paddle_top + i, 0, PADDLE_COLOUR)
    render(fb)
    time.sleep(0.08)

clear(fb)
render(fb)

# ⭐⭐ Extension: Two bouncing balls with trails
print("\nTwo bouncing balls with trails...")

def fade(fb, factor=0.65):
    for r in range(8):
        for c in range(8):
            col = fb[r][c]
            fb[r][c] = (
                int(col[0] * factor),
                int(col[1] * factor),
                int(col[2] * factor),
            )

# Ball 1
b1r, b1c = 1, 0
b1rv, b1cv = 1, 1
B1_COLOUR = (0, 80, 0)   # Green

# Ball 2
b2r, b2c = 6, 7
b2rv, b2cv = -1, -1
B2_COLOUR = (80, 40, 0)  # Orange

for _ in range(500):
    # Bounce ball 1
    if b1r <= 0 or b1r >= 7: b1rv = -b1rv
    if b1c <= 0 or b1c >= 7: b1cv = -b1cv
    b1r = max(0, min(7, b1r + b1rv))
    b1c = max(0, min(7, b1c + b1cv))

    # Bounce ball 2
    if b2r <= 0 or b2r >= 7: b2rv = -b2rv
    if b2c <= 0 or b2c >= 7: b2cv = -b2cv
    b2r = max(0, min(7, b2r + b2rv))
    b2c = max(0, min(7, b2c + b2cv))

    fade(fb, 0.6)
    set_pixel(fb, b1r, b1c, B1_COLOUR)
    set_pixel(fb, b2r, b2c, B2_COLOUR)
    render(fb)
    time.sleep(0.08)

clear(fb)
render(fb)

# ⭐⭐⭐ Stretch: Automatic snake following a spiral path
print("\nSpiral snake...")

def make_spiral_path(size=8):
    """Generate a spiral path covering an 8x8 grid."""
    path = []
    top, bottom, left, right = 0, size-1, 0, size-1
    while top <= bottom and left <= right:
        for c in range(left, right+1):
            path.append((top, c))
        top += 1
        for r in range(top, bottom+1):
            path.append((r, right))
        right -= 1
        if top <= bottom:
            for c in range(right, left-1, -1):
                path.append((bottom, c))
            bottom -= 1
        if left <= right:
            for r in range(bottom, top-1, -1):
                path.append((r, left))
            left += 1
    return path

path = make_spiral_path(8)
BODY_LEN = 5
HEAD_COLOUR = (0, 80, 80)
BODY_COLOUR = (0, 30, 30)

for i in range(len(path) + BODY_LEN):
    clear(fb)
    # Draw body (tail to head-1)
    for j in range(BODY_LEN - 1):
        idx = i - BODY_LEN + j
        if 0 <= idx < len(path):
            r, c = path[idx]
            set_pixel(fb, r, c, BODY_COLOUR)
    # Draw head
    head_idx = i
    if 0 <= head_idx < len(path):
        r, c = path[head_idx]
        set_pixel(fb, r, c, HEAD_COLOUR)
    render(fb)
    time.sleep(0.08)

clear(fb)
render(fb)
print("Done.")
