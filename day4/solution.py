NEIGHBOURS = [(-1,-1), (-1, 0), (0, -1), (1, 0), (0, 1), (1, 1), (1, -1), (-1, 1)]
def is_valid(line, col):
    total = 0
    for dx, dy in NEIGHBOURS:
        if not (0 <= line + dy < height and 0 <= col + dx < width):
            continue
        if matrix[line + dy][col + dx] == "@":
            total += 1
    return (total < 4)

file = open("input.txt")

matrix = [list(line.strip()) for line in file]
height = len(matrix)
width = len(matrix[0])

grand_total_part_one = 0
grand_total_part_two = 0
level = 0

while (True):
    new_total = 0
    for l in range(height):
        for c in range(width):
            if (matrix[l][c] == "@" and is_valid(l,c)):
                new_total += 1
                matrix[l][c] = "."
    grand_total_part_two += new_total
    if level == 0:
        grand_total_part_one = new_total
    level += 1
    if (new_total == 0):
        break

print(f"Part One")
print(f"Total is: {grand_total_part_one}")
print("---")
print(f"Part Two")
print(f"Total is: {grand_total_part_two}")

