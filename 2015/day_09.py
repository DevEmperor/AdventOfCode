import itertools

with open("text_09.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

distances = {}
for i in content:
    distances[i.split(" = ")[0]] = int(i.split(" ")[4])
    a = i.split(" = ")[0].split()
    a.reverse()
    distances[" ".join(a)] = int(i.split(" ")[4])

places = []
for i in distances.keys():
    if i.split(" ")[0] not in places:
        places.append(i.split(" ")[0])
    if i.split(" ")[2] not in places:
        places.append(i.split(" ")[2])

possible = {}
for subset in itertools.permutations(places, len(places)):
    possible[" to ".join(subset)] = sum(distances[subset[i] + " to " + subset[i + 1]] for i in range(len(subset) - 1))

print(min(possible.values()))
print(max(possible.values()))
