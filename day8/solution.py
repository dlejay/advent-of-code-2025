from collections import Counter

file = open("input.txt")

def norm(x, y):
    return (x[0] - y[0])** 2 + (x[1] - y[1])** 2 + (x[2] - y[2])** 2

class DSU:

    def __init__(self, n):
        self.parents = list(range(n))
        self.count = n

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if (rx != ry):
            self.parents[rx] = ry
            self.count -= 1


junction_boxes = []
for line in file:
    junction_boxes.append(tuple(map(int, line.strip().split(","))))

total_boxes = len(junction_boxes)

dsu = DSU(total_boxes)

distances = []
for i in range(total_boxes):
    for j in range(i + 1, total_boxes):
        distances.append((norm(junction_boxes[i], junction_boxes[j]), i, j))

distances.sort()

MAX = 1000

for n in range(MAX):
    dsu.union(distances[n][1], distances[n][2])

c = Counter()
for n in range(total_boxes):
    c[dsu.find(n)] += 1

circuits = list(c.values())
circuits.sort(reverse=True)
print("Part One")
print(f"Result: {circuits[0] * circuits[1] * circuits[2]}")


# --- Part Two

dsu = DSU(total_boxes)
n = 0
while (dsu.count > 1):
    dsu.union(distances[n][1], distances[n][2])
    n += 1

_, i, j = distances[n - 1]

print("\nPart Two")
print(f"Result: {junction_boxes[i][0] * junction_boxes[j][0]}")
