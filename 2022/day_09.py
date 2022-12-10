import math

content = [x.strip() for x in open("text_09.txt").readlines()]

headx = heady = tailx = taily = 0
visited = []
for line in content:
    d, c = line.split()
    for _ in range(int(c)):  # move head
        if d == "U": heady += 1
        if d == "D": heady -= 1
        if d == "L": headx -= 1
        if d == "R": headx += 1

        # move tail
        if round(math.dist([headx, heady], [tailx, taily])) < 2:  # change to 9 for part 2 (+ 4... have no idea why)
            continue
        if headx > tailx: tailx += 1
        if headx < tailx: tailx -= 1
        if heady > taily: taily += 1
        if heady < taily: taily -= 1

        visited.append((tailx, taily))

print(len(set(visited)) + 1)

