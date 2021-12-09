from itertools import permutations

with open("text_01.txt") as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]

p = permutations(content, 2)
for i in p:
    if sum(i) == 2020:
        print(i[0]*i[1])

p = permutations(content, 3)
for i in p:
    if sum(i) == 2020:
        print(i[0]*i[1]*i[2])
