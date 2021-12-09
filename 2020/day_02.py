with open("text_02.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

passwords = []
policiyIndicesFirst = []
policiyIndicesSecond = []
policyChars = []
counter = 0

for i in content:
    passwords.append(i.split(": ")[1])
    policyChars.append(i.split(": ")[0].split(" ")[1])
    policiyIndicesFirst.append(i.split("-")[0])
    policiyIndicesSecond.append(i.split("-")[1].split(" ")[0])

for n in range(len(content)):
    if int(policiyIndicesFirst[n]) <= passwords[n].count(policyChars[n]) <= int(policiyIndicesSecond[n]):
        counter += 1

print(counter)
counter = 0

for n in range(len(content)):
    password = passwords[n]
    firstIndex = policiyIndicesFirst[n]
    secondIndex = policiyIndicesSecond[n]
    if password[int(firstIndex)-1] == policyChars[n] and password[int(secondIndex)-1] != policyChars[n]:
        counter += 1
    if password[int(firstIndex)-1] != policyChars[n] and password[int(secondIndex)-1] == policyChars[n]:
        counter += 1

print(counter)
