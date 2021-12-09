def cal_fuel(mass):
    return int(mass / 3) - 2


def cal_fuel_2(mass):
    fuel = int(mass / 3) - 2
    if fuel < 0:
        return total_fuel
    else:
        return fuel + cal_fuel_2(fuel)


with open("text_01.txt") as f:
    content = f.readlines()
content = [int(x.strip()) for x in content]

total = 0
for i in content:
    total += cal_fuel(i)
print(total)


total = 0
for i in content:
    total_fuel = 0
    total += cal_fuel_2(i)
print(total)