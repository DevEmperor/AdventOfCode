with open("text_02.txt") as file:
    data = file.readlines()
data = [d.strip() for d in data]

pad = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

instr = {
    "U": (-1, 0),
    "D": (1, 0),
    "R": (0, 1),
    "L": (0, -1)
}

for line in data:
    pos = (1, 1)
    for cmd in line:
        try:
            pos = (pos[0] + instr[cmd][0], pos[1] + instr[cmd][1])
        except IndexError: continue
    print(pos)
    # print(pad[pos[0]], end="")
