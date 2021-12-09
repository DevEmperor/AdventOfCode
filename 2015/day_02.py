with open("text_02.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

total_paper = 0
total_ribbon = 0
for i in content:
    l = int(i.split("x")[0])
    w = int(i.split("x")[1])
    h = int(i.split("x")[2])
    total_paper += 2 * l * w + 2 * w * h + 2 * h * l + min([l * w, w * h, h * l])
    total_ribbon += min([l * 2 + w * 2, l * 2 + h * 2, w * 2 + h * 2]) + l * w * h
print(total_paper)
print(total_ribbon)
