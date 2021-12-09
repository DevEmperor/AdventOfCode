from json import loads

with open("text_12.txt") as f:
    content = f.read().strip()

chars = [c for c in content]

total = 0
digit = ""
for idx, i in enumerate(chars):
    if i == "-" or i.isdigit():
        digit += i
    else:
        try:
            total += int(digit)
        except ValueError:
            pass
        digit = ""
print(total)


def n(j):
    if type(j) == int:
        return j
    if type(j) == list:
        return sum([n(j) for j in j])
    if type(j) != dict:
        return 0
    if 'red' in j.values():
        return 0
    return n(list(j.values()))


print(n(loads(content)))
