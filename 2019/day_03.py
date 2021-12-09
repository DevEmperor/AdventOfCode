with open("text_03.txt") as f:
    first_wire = f.readline().strip()
    second_wire = f.readline().strip()


first_list = [i for i in first_wire.split(",")]
second_list = [i for i in second_wire.split(",")]

first_choords = []
second_choords = []
x = 0
y = 0
for i in first_list:
    if i[0] == "R":
        for j in range(int(i[1:])):
            x += 1
            first_choords.append((x, y))
    if i[0] == "L":
        for j in range(int(i[1:])):
            x -= 1
            first_choords.append((x, y))
    if i[0] == "U":
        for j in range(int(i[1:])):
            y += 1
            first_choords.append((x, y))
    if i[0] == "D":
        for j in range(int(i[1:])):
            y -= 1
            first_choords.append((x, y))

x = 0
y = 0
for i in second_list:
    if i[0] == "R":
        for j in range(int(i[1:])):
            x += 1
            second_choords.append((x, y))
    if i[0] == "L":
        for j in range(int(i[1:])):
            x -= 1
            second_choords.append((x, y))
    if i[0] == "U":
        for j in range(int(i[1:])):
            y += 1
            second_choords.append((x, y))
    if i[0] == "D":
        for j in range(int(i[1:])):
            y -= 1
            second_choords.append((x, y))

intersection_points = [point for point in first_choords if point in second_choords]
print(min(abs(x) + abs(y) for (x, y) in intersection_points))

combined_steps = []
for idx, i in enumerate(first_choords):
    # print(f"{idx} / {len(first_choords)}")
    for idj, j in enumerate(second_choords):
        if i == j:
            combined_steps.append(idx + idj + 2)
            print(idx + idj + 2)
print(min(combined_steps))
