from itertools import groupby

content = [x.strip() for x in open("text_01.txt").readlines()]

# Part 1
cals = [sum(list(map(int, group))) for k, group in groupby(content, bool) if k]
print(max(cals))

# Part 2
cals = sorted(cals)
print(sum(cals[-3:]))