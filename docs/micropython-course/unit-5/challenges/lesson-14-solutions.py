# Lesson 14 Challenge Solutions
# Functions Introduction

import machine, neopixel, time

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

# --- LED helper functions ---
def set_led(r, g, b):
    np[0] = (r, g, b)
    np.write()

def led_off():
    set_led(0, 0, 0)

def flash(r, g, b, times=3, duration=0.2):
    """Flash the LED 'times' times."""
    for _ in range(times):
        set_led(r, g, b)
        time.sleep(duration)
        led_off()
        time.sleep(duration)

def pulse(r, g, b, steps=30):
    """Fade in and out once."""
    for i in range(steps + 1):
        factor = i / steps
        set_led(int(r * factor), int(g * factor), int(b * factor))
        time.sleep(0.02)
    for i in range(steps, -1, -1):
        factor = i / steps
        set_led(int(r * factor), int(g * factor), int(b * factor))
        time.sleep(0.02)

# ⭐ Core: LED toolkit demo
print("LED toolkit demo:")
print("Flashing red...")
flash(80, 0, 0)

print("Pulsing green...")
pulse(0, 80, 0)

print("3x blue flash fast...")
flash(0, 0, 80, times=5, duration=0.1)

led_off()

# ⭐⭐ Extension: Function composition
def temperature_colour(celsius):
    """Return (r, g, b) for a temperature value."""
    if celsius < 0:
        return (0, 0, 80)
    elif celsius < 15:
        return (0, 50, 80)
    elif celsius < 25:
        return (0, 80, 0)
    elif celsius < 35:
        return (80, 40, 0)
    else:
        return (80, 0, 0)

def show_temperature(celsius, hold=1.0):
    """Show temperature as LED colour with label."""
    r, g, b = temperature_colour(celsius)
    set_led(r, g, b)
    print(f"  {celsius}°C → ({r},{g},{b})")
    time.sleep(hold)
    led_off()

temps = [-10, 5, 20, 30, 40]
print("\nTemperature display:")
for t in temps:
    show_temperature(t, 0.8)

# ⭐⭐⭐ Stretch: Recursive functions
def factorial(n):
    """Calculate n! recursively."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """Return nth Fibonacci number recursively."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("\nFactorials:")
for i in range(1, 11):
    print(f"  {i}! = {factorial(i)}")

print("\nFibonacci sequence (first 12):")
fib_seq = [fibonacci(i) for i in range(12)]
print(f"  {fib_seq}")
