file = open("input.txt")

lines = []
for line in file:
    lines.append(line.strip().split())

height = len(lines)
width = len(lines[0])

grand_total = 0

for c in range(width):
    op = lines[height - 1][c]
    if (op == "+"):
        subtotal = 0
        for l in range(height - 1):
            subtotal += int(lines[l][c])
    else:
        subtotal = 1
        for l in range(height - 1):
            subtotal *= int(lines[l][c])
    grand_total += subtotal


print("Part One")
print(f"The grand total is: {grand_total}")

file = open("input.txt")

lines = file.readlines()

def read_number(matrix, c):
    number = 0
    for l in range(height - 1):
        if matrix[l][c] == " ":
            continue
        number = 10 * number + int(matrix[l][c])
    return number

width = len(lines[0])
grand_total = 0
subtotal = 0

for c in range(width):
    if (lines[height - 1][c] not in " \n"):
        current_op = lines[height - 1][c]
        if current_op == "*":
            subtotal = 1
        else:
            subtotal = 0
    if all(lines[l][c] in " \n" for l in range(height)):
        grand_total += subtotal
        continue
    number = read_number(lines, c)
    if current_op == "*":
        subtotal *= number
    else:
        subtotal += number

print("")
print("Part Two")
print(f"The grand total is: {grand_total}")
