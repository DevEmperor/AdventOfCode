content = [x.strip() for x in open("text_03.txt").readlines()]

prios = 0
for ruck in content:  # Part 2: for i in range(0, len(content), 3):
    common = list(set(ruck[:len(ruck) // 2]) & set(ruck[len(ruck) // 2:]))[0]
    # common = list(set.intersection(set(content[i]), set(content[i + 1]), set(content[i + 2])))[0]
    if common.islower():
        prios += ord(common) - 96
    else:
        prios += ord(common) - 38
print(prios)

