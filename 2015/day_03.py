with open("text_03.txt") as f:
    content = f.read().strip()

x = 0
y = 0
houses = []
for i in content:
    if i == "^":
        y += 1
    elif i == "v":
        y -= 1
    elif i == ">":
        x += 1
    elif i == "<":
        x -= 1
    if (x, y) not in houses:
        houses.append((x, y))
print(len(houses))

houses = []
man = content[0::2]
robo = content[1::2]
x = 0
y = 0
for i in man:
    if i == "^":
        y += 1
    elif i == "v":
        y -= 1
    elif i == ">":
        x += 1
    elif i == "<":
        x -= 1
    if (x, y) not in houses:
        houses.append((x, y))

x = 0
y = 0
for i in robo:
    if i == "^":
        y += 1
    elif i == "v":
        y -= 1
    elif i == ">":
        x += 1
    elif i == "<":
        x -= 1
    if (x, y) not in houses:
        houses.append((x, y))
print(len(houses))
