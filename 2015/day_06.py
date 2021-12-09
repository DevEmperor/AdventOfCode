with open("text_06.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

lamps = {}
for x in range(1000):
    for y in range(1000):
        lamps[(x, y)] = ["off", 0]

for string in content:
    if string.startswith("turn"):
        instruction = string.split(" ")[1]
        start = (string.split(" ")[2].split(",")[0], string.split(" ")[2].split(",")[1])
        end = (string.split(" ")[4].split(",")[0], string.split(" ")[4].split(",")[1])
    else:
        instruction = "toggle"
        start = (string.split(" ")[1].split(",")[0], string.split(" ")[1].split(",")[1])
        end = (string.split(" ")[3].split(",")[0], string.split(" ")[3].split(",")[1])

    for x in range(int(start[0]), int(end[0]) + 1):
        for y in range(int(start[1]), int(end[1]) + 1):
            if instruction == "on":
                lamps[(x, y)][1] += 1
                if lamps[(x, y)][0] == "off":
                    lamps[(x, y)][0] = "on"
            elif instruction == "off":
                lamps[(x, y)][1] -= 1
                if lamps[(x, y)][0] == "on":
                    lamps[(x, y)][0] = "off"
            else:
                lamps[(x, y)][1] += 2
                if lamps[(x, y)][0] == "on":
                    lamps[(x, y)][0] = "off"
                else:
                    lamps[(x, y)][0] = "on"

            if lamps[(x, y)][1] < 0:
                lamps[(x, y)][1] = 0

print(sum(value[0] == "on" for value in lamps.values()))
print(sum(value[1] for value in lamps.values()))
