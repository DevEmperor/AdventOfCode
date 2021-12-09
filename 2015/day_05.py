import string

with open("text_05.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

counter = 0
for nice_string in content:
    if len([c for c in nice_string if c in ("a", "e", "i", "o", "u")]) < 3:
        continue
    if len([i+j for i, j in zip(nice_string, nice_string[1:]) if i == j]) == 0:
        continue
    if any(x in nice_string for x in ["ab", "cd", "pq", "xy"]):
        continue
    counter += 1
print(counter)

counter = 0
for nice_string in content:
    if len([i for i in range(len(nice_string) - 2) if nice_string[i + 2] == nice_string[i]]) == 0:
        continue
    if len([i for i in [x + y for x in list(string.ascii_lowercase) for y in list(string.ascii_lowercase)]
            if nice_string.count(i) > 1]) == 0:
        continue
    counter += 1
print(counter)
