with open("text_03.txt") as file:
    data = file.readlines()
data = [list(map(int, d.split())) for d in data]

# uncomment for part 2
# data = [[data[x][y], data[x + 1][y], data[x + 2][y]] for x in range(0, len(data), 3) for y in range(3)]

s = 0
for d in data:
    mx = d.pop(d.index(max(d)))
    if sum(d) > mx: s += 1
print(s)