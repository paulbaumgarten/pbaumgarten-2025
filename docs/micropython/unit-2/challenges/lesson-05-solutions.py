# Lesson 05 Challenge Solutions
# Selection (if/elif/else)

import machine, neopixel, time

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

# ⭐ Core: Grade classifier
scores = [95, 82, 74, 61, 55, 42]

print("Grade report:")
for score in scores:
    if score >= 90:
        grade = "A"
        np[0] = (0, 80, 0)     # Bright green
    elif score >= 80:
        grade = "B"
        np[0] = (0, 60, 20)    # Green
    elif score >= 70:
        grade = "C"
        np[0] = (60, 60, 0)    # Yellow
    elif score >= 60:
        grade = "D"
        np[0] = (80, 30, 0)    # Orange
    else:
        grade = "F"
        np[0] = (80, 0, 0)     # Red
    np.write()
    print(f"  Score {score:3d} → Grade {grade}")
    time.sleep(1)

np[0] = (0, 0, 0)
np.write()

# ⭐⭐ Extension: Season detector
def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Autumn"
    else:
        return "Invalid month"

SEASON_COLOURS = {
    "Winter": (0, 0, 80),
    "Spring": (0, 80, 40),
    "Summer": (80, 60, 0),
    "Autumn": (80, 20, 0),
}

print("\nSeasons:")
for month in range(1, 13):
    season = get_season(month)
    colour = SEASON_COLOURS[season]
    np[0] = colour
    np.write()
    print(f"  Month {month:2d} → {season}")
    time.sleep(0.5)

np[0] = (0, 0, 0)
np.write()

# ⭐⭐⭐ Stretch: BMI calculator
def bmi_category(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    if bmi < 18.5:
        category = "Underweight"
        colour = (0, 0, 80)
    elif bmi < 25.0:
        category = "Normal weight"
        colour = (0, 80, 0)
    elif bmi < 30.0:
        category = "Overweight"
        colour = (80, 40, 0)
    else:
        category = "Obese"
        colour = (80, 0, 0)
    return bmi, category, colour

print("\nBMI calculator:")
test_cases = [(50, 1.70), (70, 1.75), (90, 1.70), (110, 1.68)]
for weight, height in test_cases:
    bmi, category, colour = bmi_category(weight, height)
    np[0] = colour
    np.write()
    print(f"  {weight}kg / {height}m → BMI {bmi:.1f} ({category})")
    time.sleep(1)

np[0] = (0, 0, 0)
np.write()
