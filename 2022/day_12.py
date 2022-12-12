from collections import deque

content = [x.strip() for x in open("text_12.txt").readlines()]

def get_dist(grid, start, end):
    visited = { start: 0 }

    to_visit = deque()
    to_visit.append(start)

    deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while to_visit:
        (cx, cy) = to_visit.popleft()
        current_steps = visited[(cx, cy)]

        for (dx, dy) in deltas:
            nx, ny = (cx+dx, cy+dy)
            if (nx, ny) in visited or nx in [-1, len(grid[0])] or ny in [-1, len(grid)]:
                continue
            if ord(grid[ny][nx]) - ord(grid[cy][cx]) <= 1:
                visited[(nx, ny)] = current_steps + 1
                to_visit.append((nx, ny))

                if (nx, ny) == end:
                    return current_steps + 1
    return None

# Part 1
grid = []
start = end = (0, 0)
for y in range(len(content)):
    grid.append(list(content[y]))
    if "S" in content[y]:
        start = (content[y].index("S"), y)
    if "E" in content[y]:
        end = (content[y].index("E"), y)
grid[start[1]][start[0]] = "a"
grid[end[1]][end[0]] = "z"

print(get_dist(grid, start, end))

# Part 2
start = 0
distances = []
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] in "a":
            start = (x, y)
            distances.append(get_dist(grid, start, end))
print(min(filter(lambda x: x is not None, distances)))
