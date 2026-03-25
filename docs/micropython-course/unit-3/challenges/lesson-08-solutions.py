# Lesson 08 Challenge Solutions
# While Loops

import machine, neopixel, time

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

# ⭐ Core: Countdown timer
print("5-second countdown:")
count = 5
while count > 0:
    print(f"  {count}...")
    brightness = int(count * 16)   # Gets dimmer as count decreases
    np[0] = (brightness, 0, 0)
    np.write()
    time.sleep(1)
    count -= 1

print("BLAST OFF!")
for _ in range(5):
    np[0] = (80, 80, 0); np.write(); time.sleep(0.1)
    np[0] = (0, 0, 0);   np.write(); time.sleep(0.1)

# ⭐⭐ Extension: Breathing LED (smooth pulse)
print("\nBreathing LED (30 seconds)...")
STEPS  = 50
MAX_BR = 80
end_time = time.ticks_ms() + 30000

while time.ticks_diff(time.ticks_ms(), end_time) < 0:
    # Fade in
    for i in range(STEPS + 1):
        brightness = int((i / STEPS) * MAX_BR)
        np[0] = (0, brightness, brightness)
        np.write()
        time.sleep(0.02)
    # Fade out
    for i in range(STEPS, -1, -1):
        brightness = int((i / STEPS) * MAX_BR)
        np[0] = (0, brightness, brightness)
        np.write()
        time.sleep(0.02)

np[0] = (0, 0, 0)
np.write()

# ⭐⭐⭐ Stretch: Collatz conjecture
def collatz(n):
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

print("\nCollatz conjecture steps to reach 1:")
longest = 0
longest_n = 0
for start in range(1, 101):
    s = collatz(start)
    if s > longest:
        longest = s
        longest_n = start

print(f"Longest chain for n=1..100: n={longest_n} takes {longest} steps")

# Show a few examples
for n in [6, 27, 97]:
    s = collatz(n)
    print(f"  n={n}: {s} steps")
