# Part I
count = 0
dial = 50

with open("input.txt") as file:
    for line in file:
        num = int(line[1:])
        if (line[0] == "L"):
            num = -num
        dial = (dial + num) % 100
        if (dial == 0):
            count += 1

print(f"The password is {count}")

# Part 2
count = 0
dial = 50

with open("input.txt") as file:
    for line in file:
        num = int(line[1:])
        if (line[0] == "R"):
            count += (dial + num) // 100
            dial = (dial + num) % 100
        else:
            count += ((100 - dial) % 100 + num) // 100
            dial = (dial - num) % 100

print(f"Using method 0x434C49434B, the password is {count}")
