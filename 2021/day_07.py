with open("text_07.txt") as f:
    content = f.readlines()
content = [int(x) for x in content[0].split(",")]

costs = {}
for pos in range(min(content), max(content)):
    costs[pos] = sum(sum(range(abs(c - pos) + 1)) for c in content)  # part 2
    # costs[pos] = sum(abs(c - pos) for c in content)  # part 1
print(min(costs.values()))
