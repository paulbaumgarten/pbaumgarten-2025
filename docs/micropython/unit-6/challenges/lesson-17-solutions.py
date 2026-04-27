# Lesson 17 Challenge Solutions
# Reading Files

import machine, neopixel, time

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

# ⭐ Core: Colour file reader
# Create colours.txt first (via Thonny) with content like:
# red
# blue
# green
# yellow
# cyan
# purple

COLOUR_MAP = {
    "red":     (80, 0, 0),
    "green":   (0, 80, 0),
    "blue":    (0, 0, 80),
    "yellow":  (80, 80, 0),
    "cyan":    (0, 80, 80),
    "purple":  (80, 0, 80),
    "white":   (60, 60, 60),
    "orange":  (80, 30, 0),
}

try:
    with open("colours.txt", "r") as f:
        lines = f.readlines()

    colours = [line.strip().lower() for line in lines if line.strip()]
    print(f"Loaded {len(colours)} colours: {colours}")

    import random
    chosen = random.choice(colours)
    colour = COLOUR_MAP.get(chosen, (40, 40, 40))   # Grey if unknown
    print(f"Randomly chosen: {chosen} → {colour}")
    np[0] = colour
    np.write()
    time.sleep(3)
    np[0] = (0, 0, 0)
    np.write()

except OSError:
    print("colours.txt not found. Create it on the ESP32 via Thonny.")

# ⭐⭐ Extension: High score leaderboard
# Create highscores.txt with content like:
# Alice,87
# Bob,92
# Charlie,63
# Diana,78
# Eve,95

try:
    with open("highscores.txt", "r") as f:
        lines = f.readlines()

    players = []
    for line in lines:
        line = line.strip()
        if line and "," in line:
            name, score_str = line.split(",", 1)
            players.append((name.strip(), int(score_str.strip())))

    players.sort(key=lambda x: x[1], reverse=True)

    print("\nLeaderboard:")
    medals = ["GOLD", "SILVER", "BRONZE"]
    for i, (name, score) in enumerate(players):
        rank = medals[i] if i < 3 else f"#{i+1}"
        print(f"  {rank:8s}: {name:10s} — {score}")

    top_score = players[0][1] if players else 0
    if top_score > 90:
        np[0] = (200, 170, 0)   # Gold
        print(f"Top score {top_score} — GOLD")
    elif top_score > 70:
        np[0] = (150, 150, 150) # Silver
        print(f"Top score {top_score} — SILVER")
    else:
        np[0] = (160, 82, 45)   # Bronze
        print(f"Top score {top_score} — BRONZE")
    np.write()
    time.sleep(3)
    np[0] = (0, 0, 0)
    np.write()

except OSError:
    print("highscores.txt not found.")
