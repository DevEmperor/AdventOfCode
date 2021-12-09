with open("text_15.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

igds = []
for i in content:
    igds.append([int(i.split()[2][:-1]), int(i.split()[4][:-1]), int(i.split()[6][:-1]),
                 int(i.split()[8][:-1]), int(i.split()[10])])

scores = []
for i in range(100):
    for j in range(100 - i):
        for k in range(100 - i - j):
            h = 100 - i - j - k
            a = igds[0][0] * i + igds[1][0] * j + igds[2][0] * k + igds[3][0] * h
            b = igds[0][1] * i + igds[1][1] * j + igds[2][1] * k + igds[3][1] * h
            c = igds[0][2] * i + igds[1][2] * j + igds[2][2] * k + igds[3][2] * h
            d = igds[0][3] * i + igds[1][3] * j + igds[2][3] * k + igds[3][3] * h
            e = igds[0][4] * i + igds[1][4] * j + igds[2][4] * k + igds[3][4] * h

            # comment next two lines for part one
            if e != 500:
                continue
            if a <= 0 or b <= 0 or c <= 0 or d <= 0:
                continue
            scores.append(a * b * c * d)

print(max(scores))
