from collections import Counter

with open("text_04.txt") as file:
    data = file.readlines()
data = [d.strip() for d in data]

data = ["aaaaa-bbb-z-y-x-123[abxyz]"]
for room in data:
    mcl = room.split("[")[1][:-1]
    sid = int(room.split("-")[-1].split("[")[0])
    name = "".join(room.split("-")[:-1])
    c = Counter(name).most_common(5)

    print(c); exit()
