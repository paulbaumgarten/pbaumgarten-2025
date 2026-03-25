# Lesson 15 Challenge Solutions
# Parameters and Return Values

import machine, neopixel, time

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

# ⭐ Core: Unit converter with return values
def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles * 1.60934

def kg_to_lbs(kg):
    return kg * 2.20462

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print("Unit converters:")
distances_km = [1, 5, 10, 42.195, 100]
print("\nKilometres → Miles:")
for km in distances_km:
    print(f"  {km:7.3f} km = {km_to_miles(km):.3f} miles")

print("\nMiles → Kilometres:")
for miles in [1, 5, 26.2, 100]:
    print(f"  {miles:5.1f} miles = {miles_to_km(miles):.3f} km")

# ⭐⭐ Extension: Colour blending function
def clamp(value, low=0, high=255):
    return max(low, min(high, value))

def blend_colours(c1, c2, ratio=0.5):
    """Blend two (r,g,b) colours. ratio=0 → c1, ratio=1 → c2."""
    r = int(c1[0] * (1 - ratio) + c2[0] * ratio)
    g = int(c1[1] * (1 - ratio) + c2[1] * ratio)
    b = int(c1[2] * (1 - ratio) + c2[2] * ratio)
    return (clamp(r), clamp(g), clamp(b))

def scale_colour(colour, factor):
    """Scale all channels by factor (0.0 to 1.0+)."""
    return tuple(clamp(int(ch * factor)) for ch in colour)

RED  = (80, 0, 0)
BLUE = (0, 0, 80)

print("\nBlending red → blue:")
steps = 10
for i in range(steps + 1):
    ratio = i / steps
    colour = blend_colours(RED, BLUE, ratio)
    np[0] = colour
    np.write()
    print(f"  ratio={ratio:.1f}: {colour}")
    time.sleep(0.2)

np[0] = (0, 0, 0)
np.write()

# ⭐⭐⭐ Stretch: Ultrasonic with clean function signature
def get_distance(trig_pin, echo_pin):
    """Measure distance in cm using HC-SR04. Returns -1 on timeout."""
    trig_pin.off()
    time.sleep_us(2)
    trig_pin.on()
    time.sleep_us(10)
    trig_pin.off()

    timeout = time.ticks_us() + 30000
    while echo_pin.value() == 0:
        if time.ticks_us() > timeout:
            return -1
    start = time.ticks_us()
    timeout = start + 30000
    while echo_pin.value() == 1:
        if time.ticks_us() > timeout:
            return -1
    return round(time.ticks_diff(time.ticks_us(), start) / 58.2, 1)

def average_distance(trig_pin, echo_pin, samples=5):
    """Take multiple readings and return the average, ignoring errors."""
    readings = []
    for _ in range(samples):
        d = get_distance(trig_pin, echo_pin)
        if d != -1:
            readings.append(d)
        time.sleep(0.1)
    if not readings:
        return -1
    return sum(readings) / len(readings)

# Uncomment below to use with actual hardware:
# trig = machine.Pin(5, machine.Pin.OUT)
# echo = machine.Pin(4, machine.Pin.IN)
# for _ in range(10):
#     avg = average_distance(trig, echo)
#     print(f"Avg distance: {avg:.1f} cm")
#     time.sleep(0.5)
print("\n(Ultrasonic functions defined — uncomment hardware section to run)")
