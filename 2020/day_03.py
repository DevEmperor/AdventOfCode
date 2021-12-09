with open("text_03.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

file = open("text_03_refilled.txt", "w")
lines = []
for c, i in enumerate(content):
    lines.append("")
    for j in range(len(content) * 3):
        lines[c] += i
file.writelines(["%s\n" % item for item in lines])


with open("text_03_refilled.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

added = [[3, 1], [5, 1], [7, 1], [1, 2]]
xadded = 1
yadded = 1
result = 1
for x in range(5):
    counter = 0
    xpos = 0
    ypos = 0
    for i in range(len(content) - 1):
        xpos += xadded
        ypos += yadded
        if ypos > len(content):
            break
        line = content[ypos]
        if line[xpos] == "#":
            counter += 1
    print(counter)
    result = result * counter
    if x < 4:
        xadded = added[x][0]
        yadded = added[x][1]

print(f"Result: {result}")
