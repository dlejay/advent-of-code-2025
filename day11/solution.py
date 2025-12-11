from functools import cache

file = open("input.txt")

graph = {}

for line in file:
    source = line.strip().split(":")[0]
    targets = set(line.strip().split(":")[1].split())
    graph[source] = targets

@cache
def number_of_paths(source, destination):
    if source == destination:
        return 1
    if source == "out":
        return 0
    return sum(number_of_paths(target, destination) for target in graph[source])

print("Part One")
print(f"There are a total of {number_of_paths("you", "out")} paths from you to out")


solution = number_of_paths("svr", "fft") * number_of_paths("fft", "dac") * number_of_paths("dac", "out") \
        + number_of_paths("svr", "dac") * number_of_paths("dac", "fft") * number_of_paths("fft", "out")

print("\nPart Two")
print(f"There are a total of {solution} paths from svr to out that go through both fft and dac")
