with open("text_08.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

# part 1
print(sum(1 for x in [c.split(" | ")[1].split() for c in content] for y in x if len(y) in [2, 3, 4, 7]))

# part 2
s = 0
for line in content:
    digits = line.split(" | ")[0]
    values = line.split(" | ")[1]
    dd = {}
    for d in sorted(digits.split(), key=len):
        sd = sorted(d)
        if len(d) == 2: dd[1] = sd
        elif len(d) == 3: dd[7] = sd
        elif len(d) == 4: dd[4] = sd
        elif len(d) == 7: dd[8] = sd
        elif len(d) == 5:  # can be 2, 3 or 5
            if len(set(dd[1]) - set(d)) == 0: dd[3] = sd
            elif len(set(dd[4]) - set(d)) == 2: dd[2] = sd
            elif len(set(dd[7]) - set(d)) == 1: dd[5] = sd
        elif len(d) == 6: # can be 0, 6 or 9
            if len(set(dd[4]) - set(d)) == 0: dd[9] = sd
            elif len(set(dd[1]) - set(d)) == 0: dd[0] = sd
            else: dd[6] = sd

    s += int("".join(str(list(dd.keys())[list(dd.values()).index(sorted(v))]) for v in values.split()))
print(s)
