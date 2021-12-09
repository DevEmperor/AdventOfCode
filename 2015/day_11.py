# hepxcrrq
from string import ascii_lowercase


def next_pwd(password):
    password = list(password)
    for idx in range(len(password), 0, -1):
        password[idx - 1] = chr(ord(password[idx - 1]) + 1)
        if password[idx - 1] not in ascii_lowercase:
            password[idx - 1] = "a"
            continue
        return "".join(password)


three_letters = [ascii_lowercase[x] + ascii_lowercase[x + 1] + ascii_lowercase[x + 2] for x in range(24)]
doubles = [x*2 for x in ascii_lowercase]

current = "hepxcrrq"
current = "hepxxyzz"  # comment for first part
while True:
    current = next_pwd(current)
    if not any(three in current for three in three_letters):
        continue
    if any(c in current for c in ["i", "l", "o"]):
        continue
    for d in doubles:
        if d in current:
            doubles2 = [c for c in doubles if c is not d]
            for d2 in doubles2:
                if d2 in current:
                    print(current)
                    exit()
