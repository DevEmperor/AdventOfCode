def intcode(noun, verb):
    skip = 0
    numbers[1] = noun
    numbers[2] = verb
    for idx, k in enumerate(numbers):
        if skip > 0:
            skip -= 1
            continue
        if k == 1:
            numbers[numbers[idx + 3]] = numbers[numbers[idx + 1]] + numbers[numbers[idx + 2]]
            skip = 3
        elif k == 2:
            numbers[numbers[idx + 3]] = numbers[numbers[idx + 1]] * numbers[numbers[idx + 2]]
            skip = 3
        elif k == 99:
            break
    return numbers[0]


with open("text_02.txt") as f:
    content = f.readline().strip()

numbers = [int(i) for i in content.split(",")]
print(intcode(12, 2))


for noun in range(100):
    for verb in range(100):
        numbers = [int(i) for i in content.split(",")]
        if intcode(noun, verb) == 19690720:
            print(100 * noun + verb)
            exit()
