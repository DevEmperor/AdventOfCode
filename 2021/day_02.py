with open("text_02.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

x = 0
y = 0
for i in content:
    action = i.split()[0]
    value = int(i.split()[1])
    if action == "forward":
        x += value
    elif action == "down":
        y -= value
    else:
        y += value
print(abs(x * y))

x = 0
y = 0
a = 0
for i in content:
    action = i.split()[0]
    value = int(i.split()[1])
    if action == "down":
        a += value
    elif action == "up":
        a -= value
    else:
        x += value
        y += a * value
print(abs(x * y))
