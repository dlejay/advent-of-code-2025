def valid_id_part_1(n):
    txt = str(n)
    l = len(txt)
    if (l % 2 != 0):
        return True
    for i in range(l // 2):
        if txt[i] != txt[l // 2 + i]:
            return True
    return False

def valid_id_part_2(n):
    txt = str(n)
    l = len(txt)
    divisors = [d for d in range(2, l + 1) if l % d == 0]
    for d in divisors:
        size = l // d
        chunks = [txt[i * size: (i + 1) * size] for i in range(0, d)]
        if all(txt[0:size] == chunk for chunk in chunks):
            return False
    return True

file = open("input.txt")
ranges = file.read().split(",")

total_part_one = 0
total_part_two = 0

for r in ranges:
    start = int(r.split("-")[0])
    end = int(r.split("-")[1])
    for n in range(start, end + 1):
        if not valid_id_part_1(n):
            total_part_one += n
        if not valid_id_part_2(n):
            total_part_two += n

print(f"Part One")
print(f"Total of all invalid IDs: {total_part_one}")
print("")

print(f"Part Two")
print(f"Total of all invalid IDs: {total_part_two}")
