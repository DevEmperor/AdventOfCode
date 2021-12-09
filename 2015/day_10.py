# 1113222113

content = "1113222113"
c = 0
for _ in range(50):  # 40 for part one
    temp = ""
    for idx, i in enumerate(content):
        if c > 0:
            c -= 1
            continue
        while True:
            if idx + 1 == len(content) or content[idx + 1 + c] is not i:
                if c > 0:
                    temp += str(c + 1) + i
                else:
                    temp += "1" + i
                break
            else:
                c += 1
    content = temp
print(len(content))
