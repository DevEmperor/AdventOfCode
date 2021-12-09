import itertools

with open("text_13.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

happiness = {}
for i in content:
    if "lose" in i:
        happiness[i.split()[0] + "+" + i.split()[10][:-1]] = int("-" + i.split()[3])
    else:
        happiness[i.split()[0] + "+" + i.split()[10][:-1]] = int(i.split()[3])

names = list(set([name.split()[0] for name in content]))

combinations = []
for subset in itertools.permutations(names, len(names)):
    seating = list(subset)
    seating.append(seating[0])
    combinations.append(sum([sum(happiness[seating[idx] + "+" + seating[idx + 1]] for idx in range(len(seating) - 1)),
                             sum(happiness[seating[idx + 1] + "+" + seating[idx]] for idx in range(len(seating) - 1))]))
print(max(combinations))
# remove last 16 lines in input for part one
