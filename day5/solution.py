file = open("input.txt")

ing_id_ranges = []
ing_ids = []

for line in file:
    line = line.strip()
    if "-" in line:
        tmp = line.split("-")
        ing_id_ranges.append((int(tmp[0]), int(tmp[1])))
    elif line == "":
        continue
    else:
        ing_ids += [int(line)]

total_fresh_ings = 0
def fresh(ing_id, range_list):
    for lo, hi in range_list:
        if lo <= ing_id <= hi:
            return True
    return False

for ing in ing_ids:
    total_fresh_ings += fresh(ing, ing_id_ranges)

# Assumes range_1[0] <= range_2[0]
def intersect(range_1, range_2):
    if (range_1[1] >= range_2[0]):
        return True
    return False

# Assumes range_1[0] <= range_2[0] and range_1[1] >= range_2[0]
def merge(range_1, range_2):
    if (range_1[1] >= range_2[1]):
        return range_1
    else:
        return (range_1[0], range_2[1])

ing_id_ranges.sort()

i = 0
while (True):
    if i == len(ing_id_ranges) - 1:
        break
    if intersect(ing_id_ranges[i], ing_id_ranges[i + 1]):
        ing_id_ranges[i] = merge(ing_id_ranges[i], ing_id_ranges[i + 1])
        ing_id_ranges.pop(i + 1)
        continue
    i += 1

available_fresh_ings = 0
for r in ing_id_ranges:
    available_fresh_ings += 1 + r[1] - r[0]

print("Part One")
print(f"There are {total_fresh_ings} fresh ings.")
print("\nPart Two")
print(f"There are {available_fresh_ings} available fresh ings.")

