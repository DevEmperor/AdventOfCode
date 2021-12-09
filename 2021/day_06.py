from collections import Counter

with open("text_06.txt") as f:
    content = f.readlines()
content = Counter([int(x) for x in content[0].split(",")])

for _ in range(256):  # range(80) for part 1
    temp = Counter()
    for x in range(0, 9):
        temp[x - 1] = content[x]
    temp[8] = content[0]
    temp[6] += content[0]
    content = temp
print(sum(content.values()) - content[-1])
