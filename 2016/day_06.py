from collections import Counter

with open("text_06.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

s = ""
for x in range(len(content[0])):
    t = "".join(c[x] for c in content)
    # s += Counter(t).most_common()[0][0]  # part 1
    s += Counter(t).most_common()[-1][0]  # part 2
print(s)
