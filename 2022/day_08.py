content = [x.strip() for x in open("text_08.txt").readlines()]

part1 = 0
part2 = []

# Part 1
for idy, y in enumerate(content):
    for idx, x in enumerate(y):
        c = int(x)

        # Part 1
        top = all([int(content[ty][idx]) < c for ty in range(idy - 1, -1, -1)])
        bottom = all([int(content[ty][idx]) < c for ty in range(idy + 1, len(content))])
        left = all([int(content[idy][tx]) < c for tx in range(idx - 1, -1, -1)])
        right = all([int(content[idy][tx]) < c for tx in range(idx + 1, len(content[0]))])
        if any([top, bottom, left, right]):
            part1 += 1

# Part 2
for idy, y in enumerate(content):
    for idx, x in enumerate(y):
        c = int(x)
        score = 1
        for cidy, cy in enumerate([content[ty][idx] for ty in range(idy - 1, -1, -1)]):  # top
            if int(cy) >= c or cidy == idy - 1:
                score *= cidy + 1
                break
        for cidy, cy in enumerate([content[ty][idx] for ty in range(idy + 1, len(content))]):  # bottom
            if int(cy) >= c or cidy == len(content) - idy - 2:
                score *= cidy + 1
                break
        for cidx, cx in enumerate([content[idy][tx] for tx in range(idx - 1, -1, -1)]):  # left
            if int(cx) >= c or cidx == idx - 1:
                score *= cidx + 1
                break
        for cidx, cx in enumerate([content[idy][tx] for tx in range(idx + 1, len(content[0]))]):  # right
            if int(cx) >= c or cidx == len(content[0]) - idx - 2:
                score *= cidx + 1
                break
        part2.append(score)

print(part1)
print(max(part2))