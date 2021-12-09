import collections
import re

content = [x.strip() for x in open("text_07.txt").readlines()]

counter = 0
do_again = True
possible = ["shiny gold"]
while do_again:
    do_again = False
    for i in content:
        for p in possible:
            if p + " bag" in i and i.index(p + " bag") > i.index("contain"):
                first_word = i.split(" ")[0]
                second_word = i.split(" ")[1].split(" ")[0]
                if not (first_word + " " + second_word) in possible:
                    possible.append(first_word + " " + second_word)
                    counter += 1
                    do_again = True

print(counter)
counter = 0


contains = collections.defaultdict(list)
inside = collections.defaultdict(set)
for line in content:
    color = line.split(" bags contain ")[0]
    contains[color] = []
    if line.split(" contain ")[1] == "no other bags.":
        continue
    for value, inner in re.findall(r'(\d+) (.+?) bags?[,.]', line):
        contains[color].append((int(value), inner))
        inside[inner].add(color)


def bags(color):
    return sum(value * (1 + bags(inner)) for value, inner in contains[color])


print(bags("shiny gold"))
