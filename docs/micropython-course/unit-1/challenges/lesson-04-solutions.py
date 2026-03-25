# Lesson 04 Challenge Solutions
# Expressions and Type Conversion

import machine, neopixel, time

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

# ⭐ Core: Calculator
a = 17
b = 5

print(f"a = {a}, b = {b}")
print(f"a + b  = {a + b}")
print(f"a - b  = {a - b}")
print(f"a * b  = {a * b}")
print(f"a / b  = {a / b:.2f}")
print(f"a // b = {a // b}  (floor division)")
print(f"a % b  = {a % b}   (remainder)")
print(f"a ** b = {a ** b}  (power)")
print(f"a is odd: {a % 2 != 0}")

# ⭐⭐ Extension: Temperature converter
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

temps_c = [0, 20, 37, 100, -40]
print("\nTemperature conversions:")
print(f"{'Celsius':>10} | {'Fahrenheit':>12}")
print("-" * 25)
for c in temps_c:
    f = celsius_to_fahrenheit(c)
    print(f"{c:>10.1f} | {f:>12.1f}")

# Colour based on temperature
temp = 37
if temp < 0:
    np[0] = (0, 0, 80)    # Blue — freezing
elif temp < 20:
    np[0] = (0, 60, 60)   # Cyan — cold
elif temp < 30:
    np[0] = (0, 80, 0)    # Green — comfortable
elif temp < 38:
    np[0] = (80, 40, 0)   # Orange — warm
else:
    np[0] = (80, 0, 0)    # Red — hot
np.write()
time.sleep(2)
np[0] = (0, 0, 0)
np.write()

# ⭐⭐⭐ Stretch: Quadratic formula
# Solve ax² + bx + c = 0
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    print(f"\nSolving {a}x² + {b}x + {c} = 0")
    print(f"Discriminant = {discriminant}")
    if discriminant > 0:
        x1 = (-b + discriminant**0.5) / (2*a)
        x2 = (-b - discriminant**0.5) / (2*a)
        print(f"Two real roots: x1 = {x1:.3f}, x2 = {x2:.3f}")
    elif discriminant == 0:
        x = -b / (2*a)
        print(f"One real root: x = {x:.3f}")
    else:
        print("No real roots (discriminant is negative)")

solve_quadratic(1, -5, 6)   # roots: 3, 2
solve_quadratic(1, -2, 1)   # root: 1 (double)
solve_quadratic(1, 1, 1)    # no real roots
