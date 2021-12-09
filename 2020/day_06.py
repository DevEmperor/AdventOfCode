with open("text_06.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

groups = [""] * (content.count("") + 1)
n = 0

for i in content:
    if i != "":
        groups[n] += i
    else:
        n += 1

counter = 0
for i in groups:
    counter += len(set(i))

print(counter)
counter = 0

group = []
skip = False
for i in content:
    if i != "":
        group.append(i)
    else:
        for n in group[0]:
            for p in group:
                if n not in p:
                    skip = True
                    break
            if skip:
                skip = False
                continue
            counter += 1
        group = []

print(counter)
