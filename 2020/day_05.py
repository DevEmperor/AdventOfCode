import math

with open("text_05.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]


def decoder(binary):
    first_bin = binary[:7]
    second_bin = binary[7:]

    temp_min = 0
    temp_max = 127
    for n in first_bin:
        sum_first = (temp_min + temp_max) / 2
        if n == "F":
            temp_max = math.floor(sum_first)
        if n == "B":
            temp_min = math.ceil(sum_first)
    first_result = temp_max

    temp_min = 0
    temp_max = 7
    for n in second_bin:
        sum_second = (temp_min + temp_max) / 2
        if n == "R":
            temp_min = math.ceil(sum_second)
        if n == "L":
            temp_max = math.floor(sum_second)
    second_result = temp_max

    return [first_result, second_result]


all_ids = []
for i in content:
    seat = decoder(i)
    all_ids.append(seat[0] * 8 + seat[1])

highest_id = max(all_ids)
print(highest_id)

for i in range(highest_id):
    if i not in all_ids:
        print(i)
