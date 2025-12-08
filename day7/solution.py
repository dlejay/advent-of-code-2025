import copy
from functools import cache

file = open("input.txt")

GRID = []
for line in file:
    GRID.append(list(line.strip()))

matrix = copy.deepcopy(GRID)

HEIGHT = len(GRID)
WIDTH = len(GRID[0])

for l in range(HEIGHT):
    for c in range(WIDTH):
        if (matrix[l][c] == "S"):
            matrix[l + 1][c] = "|"
        if (matrix[l][c] == "^" and matrix[l - 1][c] == "|"):
            matrix[l][c - 1] = "|"
            matrix[l][c + 1] = "|"
        if (matrix[l][c] == "." and matrix[l - 1][c] == "|"):
            matrix[l][c] = "|"

splits = 0
for l in range(HEIGHT):
    for c in range(WIDTH):
        if (matrix[l][c] == "^" and matrix[l - 1][c] == "|"):
            splits += 1

@cache
def timelines(l, c):
    if (l == HEIGHT - 1):
        return 1
    if (GRID[l + 1][c] == "."):
        return timelines(l + 1, c)
    if (GRID[l + 1][c] == "^"):
        return timelines(l, c - 1) + timelines(l, c + 1)

print("Part One")
print(f"Total: {splits} splits")
print("")
print("Part Two")
print(f"There are {timelines(0, WIDTH // 2)} timelines")
