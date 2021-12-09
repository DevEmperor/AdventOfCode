import numpy as np

with open("text_03.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

claims = []
for instruction in content:
    fabric_id = int(instruction[1:].split(" ")[0])
    left_edge = int(instruction.split(" ")[2].split(",")[0])
    top_edge = int(instruction.split(" ")[2].split(",")[1][:-1])
    width = int(instruction.split(" ")[3].split("x")[0])
    height = int(instruction.split(" ")[3].split("x")[1])

    temp = []
    for x in range(width):
        for y in range(height):
            temp.append((x + left_edge, y + top_edge))
    claims.append(temp)

rect = np.zeros((1000, 1000))
for claim in claims:
    rect[left_edge:left_edge + width, top_edge:top_edge+height] += 1
print(np.size(np.where(rect >= 2)[0]))

