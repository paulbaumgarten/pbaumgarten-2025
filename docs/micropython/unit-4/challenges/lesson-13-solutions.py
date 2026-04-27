# Lesson 13 Challenge Solutions
# Ultrasonic Sensor

import machine, neopixel, time

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)
trig = machine.Pin(5, machine.Pin.OUT)
echo = machine.Pin(4, machine.Pin.IN)

def get_distance():
    """Measure distance in cm. Returns -1 on timeout."""
    trig.off()
    time.sleep_us(2)
    trig.on()
    time.sleep_us(10)
    trig.off()

    timeout = time.ticks_us() + 30000
    while echo.value() == 0:
        if time.ticks_us() > timeout:
            return -1

    start = time.ticks_us()
    timeout = start + 30000
    while echo.value() == 1:
        if time.ticks_us() > timeout:
            return -1

    return round(time.ticks_diff(time.ticks_us(), start) / 58.2, 1)

# ⭐ Core: Distance-colour indicator
print("Distance sensor active. Move objects closer/further.")
print("Ctrl+C to stop.\n")

try:
    while True:
        dist = get_distance()
        if dist == -1:
            np[0] = (80, 0, 80)   # Purple = error
            np.write()
            time.sleep(0.1)
            continue

        if dist < 10:
            np[0] = (80, 0, 0)    # Red — very close
        elif dist < 20:
            np[0] = (80, 40, 0)   # Orange — close
        elif dist < 40:
            np[0] = (80, 80, 0)   # Yellow — medium
        elif dist < 80:
            np[0] = (0, 80, 0)    # Green — far
        else:
            np[0] = (0, 0, 80)    # Blue — very far

        np.write()
        print(f"\r  Distance: {dist:5.1f} cm   ", end="")
        time.sleep(0.2)

except KeyboardInterrupt:
    pass

np[0] = (0, 0, 0)
np.write()
print("\nStopped.")

# ⭐⭐ Extension: Running average and statistics
print("\nCollecting 20 readings for statistics...")
readings = []
for i in range(20):
    dist = get_distance()
    if dist != -1:
        readings.append(dist)
        print(f"  Reading {i+1:2d}: {dist:.1f} cm")
    time.sleep(0.3)

if readings:
    print(f"\nResults from {len(readings)} valid readings:")
    print(f"  Min:     {min(readings):.1f} cm")
    print(f"  Max:     {max(readings):.1f} cm")
    print(f"  Average: {sum(readings)/len(readings):.1f} cm")

    # Running average
    print("\nRunning average:")
    running_avg = []
    for i in range(len(readings)):
        avg = sum(readings[:i+1]) / (i+1)
        running_avg.append(avg)
        print(f"  After {i+1:2d} readings: {avg:.1f} cm")
