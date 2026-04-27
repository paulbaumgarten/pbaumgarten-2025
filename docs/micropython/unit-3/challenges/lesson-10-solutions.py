# Lesson 10 Challenge Solutions
# IR Sensor, break and continue

import machine, neopixel, time

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)
ir = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)

# ⭐ Core: IR alarm with LED
print("IR alarm active. Block sensor to trigger.")
print("Hold object in front for 3 seconds to dismiss alarm.")

while True:
    if ir.value() == 0:   # Object detected
        print("ALARM! Object detected!")
        alarm_start = time.ticks_ms()
        dismissed = False

        while not dismissed:
            # Flash red
            np[0] = (80, 0, 0); np.write()
            time.sleep(0.1)
            np[0] = (0, 0, 0);  np.write()
            time.sleep(0.1)

            # Check if held for 3 seconds to dismiss
            if ir.value() == 0:
                held = time.ticks_diff(time.ticks_ms(), alarm_start)
                if held >= 3000:
                    print("Alarm dismissed.")
                    dismissed = True
            else:
                alarm_start = time.ticks_ms()   # Reset hold timer

        np[0] = (0, 80, 0); np.write(); time.sleep(1)
        np[0] = (0, 0, 0);  np.write()
        print("Back to monitoring...")
    else:
        np[0] = (0, 20, 0)   # Dim green — all clear
        np.write()

    time.sleep(0.05)
