content = [x.strip() for x in open("text_12.txt").readlines()]

facing = "E"
east_west = 0
north_south = 0
for i in content:
    action = i[0]
    value = int(i[1:])
    if action == "N": north_south += value
    if action == "S": north_south -= value
    if action == "E": east_west += value
    if action == "W": east_west -= value
    if action == "F":
        if facing == "E": east_west += value
        if facing == "W": east_west -= value
        if facing == "N": north_south += value
        if facing == "S": north_south -= value
    if action == "R":
        if facing == "N":
            if value == 90: facing = "E"
            if value == 180: facing = "S"
            if value == 270: facing = "W"
            continue
        if facing == "E":
            if value == 90: facing = "S"
            if value == 180: facing = "W"
            if value == 270: facing = "N"
            continue
        if facing == "S":
            if value == 90: facing = "W"
            if value == 180: facing = "N"
            if value == 270: facing = "E"
            continue
        if facing == "W":
            if value == 90: facing = "N"
            if value == 180: facing = "E"
            if value == 270: facing = "S"
            continue
    if action == "L":
        if facing == "N":
            if value == 90: facing = "W"
            if value == 180: facing = "S"
            if value == 270: facing = "E"
            continue
        if facing == "W":
            if value == 90: facing = "S"
            if value == 180: facing = "E"
            if value == 270: facing = "N"
            continue
        if facing == "S":
            if value == 90: facing = "E"
            if value == 180: facing = "N"
            if value == 270: facing = "W"
            continue
        if facing == "E":
            if value == 90: facing = "N"
            if value == 180: facing = "W"
            if value == 270: facing = "S"
            continue
print(abs(east_west) + abs(north_south))



