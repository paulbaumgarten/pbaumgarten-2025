# Lesson 07 Challenge Solutions
# Logical Operators

import machine, neopixel, time

pin  = machine.Pin(48, machine.Pin.OUT)
np   = neopixel.NeoPixel(pin, 1)
btn_a = machine.Pin(0,  machine.Pin.IN, machine.Pin.PULL_UP)
btn_b = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

# ⭐ Core: Two-button colour mixer
# A only → Red, B only → Blue, Both → Purple, Neither → Off
print("Two-button colour mixer:")
print("  A only  → Red")
print("  B only  → Blue")
print("  A + B   → Purple")
print("  Neither → Off")
print("Hold both for 3 seconds to exit.")

hold_both_start = None

while True:
    a = btn_a.value() == 0
    b = btn_b.value() == 0

    if a and b:
        np[0] = (80, 0, 80)   # Purple
        if hold_both_start is None:
            hold_both_start = time.ticks_ms()
        elif time.ticks_diff(time.ticks_ms(), hold_both_start) >= 3000:
            print("Exiting.")
            break
    elif a and not b:
        np[0] = (80, 0, 0)    # Red
        hold_both_start = None
    elif b and not a:
        np[0] = (0, 0, 80)    # Blue
        hold_both_start = None
    else:
        np[0] = (0, 0, 0)     # Off
        hold_both_start = None

    np.write()
    time.sleep(0.05)

np[0] = (0, 0, 0)
np.write()

# ⭐⭐ Extension: Logic gate simulator (printed)
print("\nLogic gate truth tables:")
inputs = [(False, False), (False, True), (True, False), (True, True)]

print("\nAND gate:")
for a, b in inputs:
    print(f"  {int(a)} AND {int(b)} = {int(a and b)}")

print("\nOR gate:")
for a, b in inputs:
    print(f"  {int(a)} OR  {int(b)} = {int(a or b)}")

print("\nNAND gate (not AND):")
for a, b in inputs:
    print(f"  {int(a)} NAND {int(b)} = {int(not (a and b))}")

print("\nXOR gate (one but not both):")
for a, b in inputs:
    xor = (a or b) and not (a and b)
    print(f"  {int(a)} XOR  {int(b)} = {int(xor)}")
