# input: 264793-803935
def check_criteria(password):
    password = str(password)
    for idx, i in enumerate(password):
        if idx != 0 and int(i) < int(password[idx - 1]):
            return False
    if any(password.count(i) == 2 for i in password):  # for part 1 replace "== 2" with "> 1"
        return True
    return False


counter = 0
for num in range(264793, 803935 + 1):
    if check_criteria(num):
        counter += 1
print(counter)
