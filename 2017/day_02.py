from itertools import combinations

with open("text_02.txt") as file:
    data = [list(map(int, line.split("\t"))) for line in file.readlines()]

print(sum(max(d) - min(d) for d in data))

print(sum(max(c) // min(c) for d in data for c in combinations(d, 2) if max(c) % min(c) == 0))
