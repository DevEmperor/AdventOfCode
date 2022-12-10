with open("text_04.txt") as f:
    content = f.readline()

action = True
while action:
    reacted = ""
    action = False
    for a, b in zip(content, content[1:]):
        if a.lower() == b.lower() and (a.islower() and b.isupper() or a.isupper() and b.islower()):
            continue
        else:
            reacted += a
            action = True
    print(reacted)
    content = reacted
