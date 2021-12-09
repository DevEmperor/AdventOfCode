from collections import Counter

with open("text_05.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

points = []
for line in content:
    x1 = int(line.split(",")[0])
    y1 = int(line.split(" -> ")[0].split(",")[1])
    x2 = int(line.split(" -> ")[1].split(",")[0])
    y2 = int(line.split(",")[2])
    sx = 1 if x1 <= x2 else -1
    sy = 1 if y1 <= y2 else -1

    if x1 != x2 and y1 != y2:
        # continue  # uncommment for part 1
        for i in range(abs(x1 - x2) + 1):
            points.append((x1 + i * sx, y1 + i * sy))
        continue

    for x in range(x1, x2 + sx, sx):
        for y in range(y1, y2 + sy, sy):
            points.append((x, y))

print(sum(1 for c in Counter(points).values() if c >= 2))
