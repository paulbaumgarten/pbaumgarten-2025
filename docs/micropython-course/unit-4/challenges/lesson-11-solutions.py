# Lesson 11 Challenge Solutions
# Lists Introduction

import machine, neopixel, time

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

# ⭐ Core: Colour playlist
playlist = [
    (80, 0, 0),   # Red
    (0, 80, 0),   # Green
    (0, 0, 80),   # Blue
    (80, 80, 0),  # Yellow
    (0, 80, 80),  # Cyan
]

print(f"Playlist has {len(playlist)} colours.")
print(f"First colour: {playlist[0]}")
print(f"Last colour:  {playlist[-1]}")

print("\nPlaying through playlist:")
for i, colour in enumerate(playlist):
    print(f"  [{i}] {colour}")
    np[0] = colour
    np.write()
    time.sleep(0.8)

print("\nReverse order:")
for colour in playlist[::-1]:
    np[0] = colour
    np.write()
    time.sleep(0.5)

np[0] = (0, 0, 0)
np.write()

# ⭐⭐ Extension: Statistics
data = [14, 7, 23, 5, 19, 11, 8, 30, 16, 2]

print(f"\nData: {data}")
print(f"Length:  {len(data)}")
print(f"Min:     {min(data)}")
print(f"Max:     {max(data)}")
print(f"Sum:     {sum(data)}")
print(f"Average: {sum(data)/len(data):.2f}")
print(f"Sorted:  {sorted(data)}")
print(f"Median:  {sorted(data)[len(data)//2]}")

# Count values above the average
avg = sum(data) / len(data)
above = [x for x in data if x > avg]
print(f"Above average ({avg:.1f}): {above} — count: {len(above)}")

# ⭐⭐⭐ Stretch: Slice operations
letters = list("MICROPYTHON")
print(f"\nList of chars: {letters}")
print(f"First 5:  {letters[:5]}")
print(f"Last 3:   {letters[-3:]}")
print(f"Every 2nd: {letters[::2]}")
print(f"Reversed: {letters[::-1]}")
print(f"Middle 4: {letters[3:7]}")

# Join back to string
print(f"Joined: {''.join(letters)}")
print(f"Reversed word: {''.join(letters[::-1])}")
