import re
import string

with open("text_04.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

counter = 0
matches = ["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]
array = []

paragraph = ""
for i in content:
    if i != "":
        paragraph += i
    else:
        array.append(paragraph)
        paragraph = ""

for i in array:
    if all(x in i for x in matches):
        counter += 1

print(counter)
counter = 0

for i in array:
    try:
        # byr
        if 1920 <= int((i.split("byr:")[1])[:4]) <= 2002:
            # iyr
            if 2010 <= int((i.split("iyr:")[1])[:4]) <= 2020:
                # eyr
                if 2020 <= int((i.split("eyr:")[1])[:4]) <= 2030:
                    # hgt
                    five_chars = (i.split("hgt:")[1])[:5]
                    number = int("".join(re.findall(r'\d+', five_chars)))
                    unit = five_chars[len(str(number))] + five_chars[len(str(number)) + 1]
                    if (unit == "cm" and 150 <= number <= 193) or (unit == "in" and 59 <= number <= 76):
                        # hcl
                        five_chars = (i.split("hcl:")[1])[:7]
                        if five_chars[0] == "#" and all(c in string.hexdigits for c in five_chars[1:]):
                            # ecl
                            matches = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                            if (i.split("ecl:")[1])[:3] in matches:
                                # pid
                                if all(c in string.digits for c in (i.split("pid:")[1])[:9]):
                                    counter += 1
    except IndexError:
        continue

print(counter)
