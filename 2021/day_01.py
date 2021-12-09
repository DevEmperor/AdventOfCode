with open("text_01.txt") as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]

c = 0
for x in range(len(content) - 1):
    if content[x] < content[x+1]:
        c += 1
print(c)

c = 0
for x in range(len(content) - 2):
    a = content[x:x+3]
    b = content[x+1:x+4]
    if sum(a) < sum(b):
        c += 1
print(c)
