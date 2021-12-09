with open("text_01.txt") as f:
    content = f.read().strip()

facing = 0
x = 0
y = 0
visitet = []
for i in content.split(", "):
    if i[0] == "L":
        facing -= 90
    else:
        facing += 90

    if facing == 360:
        facing = 0
    if facing < 0:
        facing = 360 + facing

    if facing == 0:
        y += int(i[1:])
    elif facing == 90:
        x += int(i[1:])
    elif facing == 180:
        y -= int(i[1:])
    elif facing == 270:
        x -= int(i[1:])
print(abs(x) + abs(y))
