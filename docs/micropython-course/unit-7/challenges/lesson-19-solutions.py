# Lesson 19 Challenge Solutions
# 2D Lists

# ⭐ Core: 6×6 bordered grid
SIZE = 6
grid = [[0] * SIZE for _ in range(SIZE)]

# Fill border with 1s
for r in range(SIZE):
    for c in range(SIZE):
        if r == 0 or r == SIZE-1 or c == 0 or c == SIZE-1:
            grid[r][c] = 1

print("6×6 bordered grid:")
for row in grid:
    for cell in row:
        print("█" if cell else ".", end=" ")
    print()

# ⭐⭐ Extension: Checkerboard with complement
SIZE = 8
board = [[1 if (r + c) % 2 == 0 else 0 for c in range(SIZE)] for r in range(SIZE)]
complement = [[1 - cell for cell in row] for row in board]

ones  = sum(cell for row in board for cell in row)
zeros = SIZE * SIZE - ones

print(f"\nCheckerboard: {ones} ones, {zeros} zeros")

print("\nBoard:          Complement:")
for r in range(SIZE):
    row_str  = " ".join("█" if c else "." for c in board[r])
    comp_str = " ".join("█" if c else "." for c in complement[r])
    print(f"  {row_str}    {comp_str}")

# ⭐⭐⭐ Stretch: Conway's Game of Life (one step)
import random

SIZE = 6

def random_grid(size):
    return [[random.randint(0, 1) for _ in range(size)] for _ in range(size)]

def count_neighbours(grid, r, c, size):
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue   # Skip the cell itself
            nr, nc = r + dr, c + dc
            if 0 <= nr < size and 0 <= nc < size:
                count += grid[nr][nc]
    return count

def next_generation(grid, size):
    new_grid = [[0] * size for _ in range(size)]
    for r in range(size):
        for c in range(size):
            neighbours = count_neighbours(grid, r, c, size)
            alive = grid[r][c] == 1
            if alive and neighbours in [2, 3]:
                new_grid[r][c] = 1   # Survives
            elif not alive and neighbours == 3:
                new_grid[r][c] = 1   # Born
            # else: stays dead (0)
    return new_grid

def print_grid(grid, label=""):
    if label:
        print(f"\n{label}:")
    for row in grid:
        print("  " + " ".join("█" if c else "." for c in row))

grid = random_grid(SIZE)
print_grid(grid, "Before (random):")

new_grid = next_generation(grid, SIZE)
print_grid(new_grid, "After one step:")

# Count population change
pop_before = sum(c for row in grid for c in row)
pop_after  = sum(c for row in new_grid for c in row)
print(f"\nPopulation: {pop_before} → {pop_after}")
