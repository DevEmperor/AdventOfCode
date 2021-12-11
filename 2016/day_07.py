with open("text_07.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

s = 0
for ip in content:
    splitted = ip.replace("[", "]").split("]")
    abba = False
    abba_hypernet = False
    for idx, chunk in enumerate(splitted):
        for i in range(len(chunk) - 3):
            if chunk[i] == chunk[i+3] and chunk[i+1] == chunk[i+2] and chunk[i] != chunk[i+1]:
                if idx % 2 != 0: abba_hypernet = True
                if idx % 2 == 0: abba = True
    if abba and not abba_hypernet: s += 1
print(s)
