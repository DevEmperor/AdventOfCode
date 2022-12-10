content = [x.strip() for x in open("text_10.txt").readlines()]

# Part 1
X = [1]
for line in content:
    if line == "noop":
        X.append(X[-1])  # cycle does not do anything

    if line.startswith("addx"):
        a = int(line.split()[1])
        X.append(X[-1])  # first cycle does not add yet
        X.append(X[-1] + a)

print(sum(X[y-1] * y for y in [20, 60, 100, 140, 180, 220]))


# Part 2
X = 1
crt = ""
for line in content:
    crt += "X" if any(len(crt) == y for y in [X - 1, X, X + 1]) else "."
    if len(crt) == 40:  # next line of screen starts as soon as we reach 40
        print(crt)
        crt = ""

    if line.startswith("addx"):
        crt += "X" if any(len(crt) == y for y in [X - 1, X, X + 1]) else "."
        if len(crt) == 40:
            print(crt)
            crt = ""

        X += int(line.split()[1])
