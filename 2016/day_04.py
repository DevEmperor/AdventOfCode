from collections import Counter
from string import ascii_letters

with open("text_04.txt") as file:
    data = file.readlines()
data = [d.strip() for d in data]

s = 0
abc = ascii_letters[:26]
for room in data:
    mcl = room.split("[")[1][:-1]
    sid = int(room.split("-")[-1].split("[")[0])
    name = "".join(room.split("-")[:-1])
    name = "".join(abc[(abc.index(c) + sid) % 26] for c in name)  # remove for part 1
    if name == "northpoleobjectstorage": print(sid); exit()  # remove for part 1
    c = Counter(sorted(name)).most_common()
    if all(c[idx][0] == mcl[idx] for idx in range(len(mcl))):
        s += sid
print(s)