with open("text_05.txt") as file:
    data = [int(n) for n in file.readlines()]

pos = 0
counter = 0
while True:
    try:
        last_pos = pos
        pos += data[pos]
        if data[last_pos] >= 3:
            data[last_pos] -= 1
        else:
            data[last_pos] += 1
        counter += 1
    except IndexError:
        print(counter)
        break
