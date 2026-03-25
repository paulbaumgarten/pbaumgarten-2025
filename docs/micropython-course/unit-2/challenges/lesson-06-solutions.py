# Lesson 06 Challenge Solutions
# Buttons and elif

import machine, neopixel, time

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)
button = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)

# ⭐ Core: Button press counter
print("Press the button to count. Hold for 5 seconds to reset.")
count = 0
was_pressed = False
hold_start  = None

while True:
    pressed = button.value() == 0

    if pressed and not was_pressed:
        # Button just pressed
        count += 1
        print(f"Count: {count}")
        # Colour changes with count
        brightness = min(count * 10, 80)
        np[0] = (0, brightness, 0)
        np.write()
        hold_start = time.ticks_ms()

    if pressed and hold_start is not None:
        held_ms = time.ticks_diff(time.ticks_ms(), hold_start)
        if held_ms >= 5000:
            count = 0
            print("RESET — count back to 0")
            for _ in range(3):
                np[0] = (80, 0, 0); np.write(); time.sleep(0.1)
                np[0] = (0, 0, 0);  np.write(); time.sleep(0.1)
            hold_start = None

    if not pressed:
        hold_start = None

    was_pressed = pressed
    time.sleep(0.05)
