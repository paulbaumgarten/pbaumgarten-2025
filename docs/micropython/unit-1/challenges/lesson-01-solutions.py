# Lesson 01 Challenge Solutions
# Hello MicroPython

import machine, neopixel, time

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

# ⭐ Core: Traffic light sequence
print("Traffic light sequence:")
colours = [
    ("RED",    (80, 0, 0)),
    ("AMBER",  (80, 40, 0)),
    ("GREEN",  (0, 80, 0)),
]
for name, colour in colours:
    print(f"  {name}")
    np[0] = colour
    np.write()
    time.sleep(2)

np[0] = (0, 0, 0)
np.write()

# ⭐⭐ Extension: Rainbow cycle (7 colours)
print("\nRainbow cycle:")
rainbow = [
    (80, 0,  0),    # Red
    (80, 30, 0),    # Orange
    (80, 80, 0),    # Yellow
    (0,  80, 0),    # Green
    (0,  0,  80),   # Blue
    (30, 0,  80),   # Indigo
    (60, 0,  80),   # Violet
]
for _ in range(3):   # 3 cycles
    for colour in rainbow:
        np[0] = colour
        np.write()
        time.sleep(0.3)

np[0] = (0, 0, 0)
np.write()

# ⭐⭐⭐ Stretch: Morse SOS (... --- ...)
print("\nSOS in Morse code:")
DOT  = 0.2
DASH = 0.6
GAP  = 0.2
LETTER_GAP = 0.6
ON_COLOUR = (0, 0, 80)

def dot():
    np[0] = ON_COLOUR; np.write(); time.sleep(DOT)
    np[0] = (0,0,0);   np.write(); time.sleep(GAP)

def dash():
    np[0] = ON_COLOUR; np.write(); time.sleep(DASH)
    np[0] = (0,0,0);   np.write(); time.sleep(GAP)

for _ in range(3):
    print("  SOS")
    dot(); dot(); dot()           # S  (...)
    time.sleep(LETTER_GAP)
    dash(); dash(); dash()        # O  (---)
    time.sleep(LETTER_GAP)
    dot(); dot(); dot()           # S  (...)
    time.sleep(1.5)               # Word gap

print("Done.")
