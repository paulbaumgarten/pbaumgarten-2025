# Lesson 12 Challenge Solutions
# List Operations

import machine, neopixel, time

pin = machine.Pin(48, machine.Pin.OUT)
np = neopixel.NeoPixel(pin, 1)

# ⭐ Core: Dynamic colour queue
colours = []
colour_names = ["Red", "Green", "Blue", "Yellow", "Cyan", "Magenta"]
colour_values = [
    (80, 0, 0), (0, 80, 0), (0, 0, 80),
    (80, 80, 0), (0, 80, 80), (80, 0, 80)
]

# Build the queue
for name, value in zip(colour_names, colour_values):
    colours.append(value)
    print(f"Added {name}: queue length = {len(colours)}")

print(f"\nQueue: {colours}")

# Display each and remove
print("\nDisplaying and removing:")
while colours:
    colour = colours.pop(0)   # Remove from front
    np[0] = colour
    np.write()
    print(f"  Showing {colour}, {len(colours)} remaining")
    time.sleep(0.5)

np[0] = (0, 0, 0)
np.write()

# ⭐⭐ Extension: Leaderboard
scores = [("Alice", 920), ("Bob", 750), ("Charlie", 830),
          ("Diana", 990), ("Eve", 680)]

# Sort by score descending
scores.sort(key=lambda x: x[1], reverse=True)

print("\nLeaderboard:")
medals = ["🥇", "🥈", "🥉"]
for i, (name, score) in enumerate(scores):
    medal = medals[i] if i < 3 else f"#{i+1}"
    print(f"  {medal} {name}: {score}")

# Top 3 only
top3 = scores[:3]
top3_names = [name for name, _ in top3]
print(f"\nTop 3: {', '.join(top3_names)}")

# ⭐⭐⭐ Stretch: Stack (LIFO) implementation
print("\nStack simulation:")

class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self._data.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)

s = Stack()
for val in [10, 20, 30, 40]:
    s.push(val)
    print(f"  Pushed {val}, top={s.peek()}, size={s.size()}")

print("  Popping all:")
while not s.is_empty():
    print(f"    Popped: {s.pop()}")
