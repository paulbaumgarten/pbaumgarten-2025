# Lesson 02 Challenge Solutions
# Variables and Data Types

import machine, neopixel, time

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

# ⭐ Core: RGB sliders
print("RGB variable demo:")
red   = 80
green = 0
blue  = 40

np[0] = (red, green, blue)
np.write()
print(f"Colour: red={red}, green={green}, blue={blue}")
time.sleep(2)

# Modify channels
red   = 0
green = 80
blue  = 80
np[0] = (red, green, blue)
np.write()
print(f"Colour: red={red}, green={green}, blue={blue}")
time.sleep(2)

np[0] = (0, 0, 0)
np.write()

# ⭐⭐ Extension: My data card
name    = "Alex"
age     = 15
height  = 1.72
is_student = True

print("\n--- My Data Card ---")
print(f"Name:    {name}   (type: {type(name).__name__})")
print(f"Age:     {age}    (type: {type(age).__name__})")
print(f"Height:  {height} (type: {type(height).__name__})")
print(f"Student: {is_student} (type: {type(is_student).__name__})")

# Colour based on age (pure fun)
if age < 13:
    np[0] = (80, 0, 0)   # Red — young
elif age < 18:
    np[0] = (0, 80, 0)   # Green — teen
else:
    np[0] = (0, 0, 80)   # Blue — adult
np.write()
time.sleep(2)
np[0] = (0, 0, 0)
np.write()

# ⭐⭐⭐ Stretch: Swap without temp variable
a = 10
b = 25
print(f"\nBefore swap: a={a}, b={b}")
a, b = b, a
print(f"After swap:  a={a}, b={b}")

# Multiple assignment and types
x = y = z = 0
print(f"\nx={x}, y={y}, z={z}")
x = 3.14
y = True
z = "hello"
print(f"x={x} ({type(x).__name__}), y={y} ({type(y).__name__}), z={z} ({type(z).__name__})")
