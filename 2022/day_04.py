content = [x.strip() for x in open("text_04.txt").readlines()]

p1 = 0
p2 = 0
for pairs in content:
    a, b = pairs.split(",")
    ax, ay = map(int, a.split("-"))
    bx, by = map(int, b.split("-"))
    if (ax >= bx and ay <= by) or (bx >= ax and by <= ay): p1 += 1
    if bx <= ax <= by or ax <= bx <= ay: p2 += 1
print(p1)
print(p2)
