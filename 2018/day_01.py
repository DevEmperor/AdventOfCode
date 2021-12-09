with open("text_01.txt") as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]

print(sum(content))

freqs = {0}
current = 0
while True:
    for i in content:
        current += i
        if current in freqs:
            print(current)
            exit()
        else:
            freqs.add(current)
