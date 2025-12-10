from itertools import combinations
from scipy.optimize import milp, LinearConstraint
from functools import reduce
from operator import xor
import numpy as np

file = open("input.txt")

targets = []
ops = []

def read_target(text):
    result = 0
    l = list(text.strip("[]"))
    for n in range(len(l)):
        if (l[n] == "#"):
            result += 2 ** n
    return result

def read_ops(text):
    result = 0
    l = list(map(int, text.strip("()").split(",")))
    for n in l:
        result ^= 2 ** n
    return result

def solve(target, coins):
    if target == 0:
        return 0
    n = 1
    while True:
        for combo in combinations(coins, n):
            if target == reduce(xor, combo):
                return n
        n += 1

for line in file:
    x = line.strip().split()
    x.pop()
    s = x.pop(0)
    targets.append(read_target(s))
    local_list = []
    for y in x:
        local_list.append(read_ops(y))
    ops.append(local_list)

total = 0
for n in range(len(targets)):
    total += solve(targets[n], ops[n])

print("Part One")
print(f"Total: {total}")


# Part Two
file = open("input.txt")

targets = []
vectors = []

def read_joltage(text):
    return np.array(list(map(int, list(text.strip("{}").split(",")))))

def read_vector(text, size):
    l = list(map(int, text.strip("()").split(",")))
    result = np.zeros(size, dtype=int)
    for n in l:
        result[n] = 1
    return result

def solve_p2(target, vectors):
    A = np.array(vectors).T 
    ones = np.ones(len(vectors))
    
    res = milp(c=ones, 
               constraints=LinearConstraint(A, lb=target, ub=target),
               integrality=ones)

    return int(res.fun)

for line in file:
    x = line.strip().split()
    size = len(x.pop(0)) - 2
    j = x.pop()
    targets.append(read_joltage(j))
    local_list = []
    for y in x:
        local_list.append(read_vector(y, size))
    vectors.append(local_list)

total = 0
for n in range(len(targets)):
    total += solve_p2(targets[n], sorted(vectors[n], key=sum, reverse=True))

print("\nPart Two")
print(f"Total: {total}")
