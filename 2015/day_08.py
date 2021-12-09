with open("text_08.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

print(sum(len(current) - len(eval(current)) for current in content))

print(sum(current.count("\\") + current.count("\"") + 2 for current in content))
