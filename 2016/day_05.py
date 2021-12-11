from hashlib import md5

content = "cxdnnyjw"
pwd = "        "  # part one: remove whitespaces
i = 0
while " " in pwd:  # part one: `while len(pwd) < 8:`
    i += 1
    h = md5(str(content + str(i)).encode()).hexdigest()
    if h.startswith("00000"):
        # pwd += h[5]  # uncomment for part one
        pos = h[5]  # comment for part one
        if not pos.isdigit(): continue
        elif int(pos) >= 8 or pwd[int(pos)] != " ": continue
        else:
            pwd = pwd[:int(pos)] + h[6] + pwd[int(pos)+1:]
            print(pwd)
print(pwd)
