file = open("input.txt")


areas = [7, 6, 7, 5, 7, 7]

lines = file.readlines()[30:]

possible = 0

for line in lines:
    l = line.strip().split()
    width, height = l[0].strip(":").split("x")
    total_area = int(width) * int(height)
    total_area_of_shapes = 0
    for i in range(6):
        total_area_of_shapes += areas[i] * int(l[i + 1])
        density = total_area_of_shapes / total_area
    if density < 0.95:
        possible += 1

print("Part One")
print(f"There are {possible} possible puzzles")
