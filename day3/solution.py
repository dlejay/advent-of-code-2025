lines = open("input.txt")

def find_max_joltage(string, number):
    if len(string) < number:
        print("Error")
        return
    if number == 1:
        return int(max(string))
    if len(string) == number:
        return int(string)
    max_digit_index, max_digit = max(enumerate(string[:len(string) - number + 1]), key=lambda x: x[1])
    tail = string[max_digit_index + 1:]
    return int(max_digit + str(find_max_joltage(tail, number - 1)))

total_part_one = 0
total_part_two = 0

for line in lines:
    line = line.strip()
    total_part_one += find_max_joltage(line, 2)
    total_part_two += find_max_joltage(line, 12)

print("Part One")
print(f"Total output joltage: {total_part_one}")

print("\nPart Two")
print(f"Total output joltage: {total_part_two}")
