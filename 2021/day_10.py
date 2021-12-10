with open("text_10.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

# part 1
points = {")": 3, "]": 57, "}": 1197, ">": 25137}
valid = ["()", "[]", "{}", "<>"]
s = 0
for line in content:
    stack = []
    for c in line:
        if c in ["(", "[", "{", "<"]: stack.append(c)
        else:
            if stack[-1] + c in valid: stack.pop()
            else: s += points[c]; break
print(s)

# part 2
points = {"(": 1, "[": 2, "{": 3, "<": 4}
valid = ["()", "[]", "{}", "<>"]
s = []
for line in content:
    stack = []
    for c in line:
        if c in ["(", "[", "{", "<"]: stack.append(c)
        else:
            if stack[-1] + c in valid: stack.pop()
            else: break
    else:
        closing_chunk = "".join(stack[::-1])

        t = 0
        for c in closing_chunk:
            t *= 5
            t += points[c]
        s.append(t)
print(sorted(s)[(len(sorted(s))-1) // 2])
