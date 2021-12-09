with open("text_14.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

reindeers = {}
for i in content:
    reindeers[i.split()[0]] = [int(i.split()[3]), int(i.split()[6]), int(i.split()[13]), 0, 0, 0]

final = {}
for i in reindeers:
    final[i] = 0

for x in range(2503):
    for i in reindeers.keys():
        if reindeers[i][5] > 0:
            reindeers[i][5] -= 1
            continue
        if reindeers[i][4] == reindeers[i][1]:
            reindeers[i][5] = reindeers[i][2] - 1
            reindeers[i][4] = 0
            continue
        reindeers[i][3] += reindeers[i][0]
        reindeers[i][4] += 1
    for i in reindeers.keys():
        if reindeers[i][3] == max(reindeers[i][3] for i in reindeers.keys()):
            final[i] += 1

print(max(reindeers[i][3] for i in reindeers.keys()))
print(max(final.values()))
