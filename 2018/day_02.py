with open("text_02.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

two = 0
three = 0
for string in content:
    for c in string:
        if string.count(c) == 2:
            two += 1
            break
    for c in string:
        if string.count(c) == 3:
            three += 1
            break
print(two * three)


for string in content:
    for compare in content:
        if sum(string[i] != compare[i] for i in range(len(string))) == 1:
            print(string + "\n" + compare)  # submit without the char that is only in the first string
            exit()
# bvnfawcnyoeyudzrpgslimtkj
