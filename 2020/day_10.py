import collections

content = sorted([int(x.strip()) for x in
                  open("text_10.txt").readlines()])

one_jolts = 0
three_jolts = 0
for n, i in enumerate(content):
    for j in content[n + 1:]:
        if j - i == 1:
            one_jolts += 1
            break
        elif j - i == 3:
            three_jolts += 1
            break
print((one_jolts + 1) * (three_jolts + 1))

combinations = collections.defaultdict(int, {0: 1})
for adapter in content:
    combinations[adapter] = combinations[adapter - 1] + combinations[adapter - 2] + combinations[adapter - 3]
print(combinations[content[-1]])
