with open("text_01.txt") as file:
    data = file.read().strip()
data += data[0]

s = 0
for x, y in [data[i:i + 2] for i in range(len(data) - 1)]:
    if x == y: s += int(x)
print(s)

s = 0
data = data[:-1]
for x, y in [(data[i], data[(i + len(data) // 2) % len(data)]) for i in range(len(data))]:
    print(x, y)
    if x == y: s += int(x)
print(s)
