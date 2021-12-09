with open("text_03.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

import collections

g = ""
e = ""
for b in range(len(content[0])):
    t = [content[x][b] for x in range(len(content))]
    g += collections.Counter(t).most_common(1)[0][0]
    e += "".join("1" if g[-1] == "0" else "0")
print(int(g, 2) * int(e, 2))


copy = content
idx = 0
while len(copy) > 1:
    t = [copy[x][idx % len(copy[0])] for x in range(len(copy))]
    o = collections.Counter(t).most_common(1)[0]
    if o[1] == len(copy) // 2: o = "1"
    copy_2 = []
    for i, c in enumerate(copy):
        if c[idx % len(copy[0])] == o[0]:
            copy_2.append(c)
    copy = copy_2
    idx += 1
oxygen = int(copy[0], 2)

copy = content
idx = 0
while len(copy) > 1:
    t = [copy[x][idx % len(copy[0])] for x in range(len(copy))]
    o = collections.Counter(t).most_common(1)[0]
    o2 = "1" if o[0] == "0" else "0"
    if o[1] == len(copy) // 2: o2 = "0"
    copy_2 = []
    for i, c in enumerate(copy):
        if c[idx % len(copy[0])] == o2:
            copy_2.append(c)
    copy = copy_2
    idx += 1
co2 = int(copy[0], 2)
print(oxygen * co2)