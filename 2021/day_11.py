with open("text_11.txt") as f:
    content = f.readlines()
content = [list(map(int, x.strip())) for x in content]


def get_adj(row, col):
    adj = [(row - 1, col), (row - 1, col - 1), (row - 1, col + 1), (row, col - 1), (row, col + 1), (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
    return [(r, c) for r, c in adj if 0 <= r <= 9 and 0 <= c <= 9]


def trig_adj(row, col):
    fs = 0
    if content[row][col] > 9:
        fs += 1
        content[row][col] = 0
        flashed.append(content[row][col])
        for adj in get_adj(row, col):
            if content[adj[0]][adj[1]] not in flashed: content[adj[0]][adj[1]] += 1
        for adj in get_adj(row, col):
            fs += trig_adj(adj[0], adj[1])
        return fs
    else:
        return 0


flashes = 0
for _ in range(1000):
    for y in range(10):
        for x in range(10):
            content[y][x] += 1
    flashed = []
    for y in range(10):
        for x in range(10):
            flashes += trig_adj(y, x)
    if all(x == 0 for y in content for x in y):
        print("2: " + str(_ + 1)); break
print("1: " + str(flashes))
