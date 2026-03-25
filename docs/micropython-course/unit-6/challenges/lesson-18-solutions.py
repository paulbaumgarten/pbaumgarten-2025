# Lesson 18 Challenge Solutions
# Writing Files and Data Logging

import machine, neopixel, time, random

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

# ⭐ Core: Movie list saved to file
# (Using hardcoded list since no keyboard input on hardware)
movies = [
    "Interstellar",
    "The Matrix",
    "Spirited Away",
    "Parasite",
    "The Grand Budapest Hotel",
]

with open("movies.txt", "w") as f:
    for movie in movies:
        f.write(movie + "\n")

print("Saved movies.txt. Reading back in reverse:")
with open("movies.txt", "r") as f:
    lines = f.readlines()

for i, line in enumerate(reversed(lines)):
    print(f"  {len(lines) - i}. {line.strip()}")

# ⭐⭐ Extension: Temperature logger with analysis
print("\nLogging temperature simulation (20 readings over 20 seconds)...")

with open("temp_log.csv", "w") as f:
    f.write("timestamp_ms,temperature\n")

start = time.ticks_ms()
for i in range(20):
    temp = round(random.uniform(18.0, 30.0), 2)
    ts = time.ticks_diff(time.ticks_ms(), start)

    with open("temp_log.csv", "a") as f:
        f.write(f"{ts},{temp}\n")

    # LED colour based on temp
    if temp > 27:
        np[0] = (80, 0, 0)
    elif temp > 23:
        np[0] = (80, 40, 0)
    else:
        np[0] = (0, 80, 0)
    np.write()

    print(f"  t={ts:5d}ms: {temp:.2f}°C")
    time.sleep(1)

np[0] = (0, 0, 0)
np.write()

# Read and analyse
with open("temp_log.csv", "r") as f:
    lines = f.readlines()

temps = []
for line in lines[1:]:   # Skip header
    line = line.strip()
    if line:
        _, t = line.split(",")
        temps.append(float(t))

avg  = sum(temps) / len(temps)
mn   = min(temps)
mx   = max(temps)
above25 = sum(1 for t in temps if t > 25)

summary = (
    f"Readings: {len(temps)}\n"
    f"Average:  {avg:.2f}°C\n"
    f"Min:      {mn:.2f}°C\n"
    f"Max:      {mx:.2f}°C\n"
    f"Above 25°C: {above25}\n"
)

with open("temp_summary.txt", "w") as f:
    f.write(summary)

print("\n--- Temperature Summary ---")
print(summary)
print("Summary saved to temp_summary.txt")
