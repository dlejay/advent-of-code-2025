from functools import cache

file = open("test.txt")

red_tiles = [tuple(map(int, line.strip().split(","))) for line in file]

def surface(t1, t2):
    return (abs(t1[0] - t2[0]) + 1) * (abs(t1[1] - t2[1]) + 1)

print("Part One")
print(f"Largest area: {max(surface(x, y) for x in red_tiles for y in red_tiles)}")


# --- Part Two

def border(x):
    for i in range(-1, len(red_tiles) - 1):
        x1, y1 = red_tiles[i]
        x2, y2 = red_tiles[i + 1]
        if x1 == x2 == x[0]:
            ymin, ymax = sorted((y1, y2))
            if (ymin <= x[1] <= ymax):
                return True
        if y1 == y2 == x[1]:
            xmin, xmax = sorted((x1, x2))
            if (xmin <= x[0] <= xmax):
                return True
    return False


# Determine if x is inside the shape drawn by the red tiles
# by counting the intersections between the ray x-- and the boundary
# The point x is inside if and only if this is odd
@cache
def inside(x):
    if border(x):
        return True
    intersections = 0
    for i in range(-1, len(red_tiles) - 1):
        x1, y1 = red_tiles[i]
        x2, y2 = red_tiles[i + 1]
        if x1 == x2 and x[0] >= x1:
            ymin, ymax = sorted((y1, y2))
            if ymin <= x[1] < ymax:
                intersections += 1
    return intersections % 2 == 1

# Does the line t1->t2 intersect the interior of the c1-c2 rectangle?
def intersects(c1, c2, t1, t2):
    xmin, xmax = sorted((c1[0], c2[0]))
    ymin, ymax = sorted((c1[1], c2[1]))
    if t1[0] <= xmin and t2[0] <= xmin:
        return False
    if t1[0] >= xmax and t2[0] >= xmax:
        return False
    if t1[1] <= ymin and t2[1] <= ymin:
        return False
    if t1[1] >= ymax and t2[1] >= ymax:
        return False
    return True

# We check that:
# 1. One point inside the rectangle is inside the shape
# 2. The boundary of the shape never intersects the interior of the rectangle

def valid(t1, t2):
    if not inside(((t1[0] + t2[0]) // 2, (t1[1] + t2[1]) // 2 )):
        return False
    xmin, xmax = sorted((t1[0], t2[0]))
    ymin, ymax = sorted((t1[1], t2[1]))
    for i in range(-1, len(red_tiles) - 1):
        if intersects(t1, t2, red_tiles[i], red_tiles[i + 1]):
            return False
    return True

max_surface = 0
for i in range(len(red_tiles)):
    for j in range(i + 1, len(red_tiles)):
        x = red_tiles[i]
        y = red_tiles[j]
        if surface(x, y) <= max_surface:
            continue
        if not valid(x, y):
            continue
        max_surface = surface(x, y)
print("\nPart Two")
print(f"Largest valid area: {max_surface}")
