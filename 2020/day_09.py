content = [int(x.strip()) for x in open("text_09.txt").readlines()]

result = 0
preamble = [int(content[i]) for i in range(25)]

for i in range(25, len(content) - 25):
    summe = content[i]
    done = False
    for j in preamble:
        for k in preamble:
            if (j + k == summe) and (j != k):
                done = True
                break
        if done:
            break
    if not done:
        result = summe
        break
    preamble = preamble[1:]
    preamble.append(summe)

print(result)

for idx, i in enumerate(content):
    lst = [i]
    for r in content[idx + 1:]:
        lst.append(r)
        if sum(lst) == result:
            print(min(lst) + max(lst))
            exit()
