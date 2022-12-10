content = [x.strip() for x in open("text_02.txt").readlines()]

# Part 1
score = 0
my = {"X": 1, "Y": 2, "Z": 3}
results = {
    "A X": 3,
    "A Y": 6,
    "A Z": 0,
    "B X": 0,
    "B Y": 3,
    "B Z": 6,
    "C X": 6,
    "C Y": 0,
    "C Z": 3,
}
for line in content:
    opp, me = line.split(" ")
    score += results[line]
    score += my[me]
print(score)

# Part 2
score = 0
results = {
    "A X": 3,
    "A Y": 1,
    "A Z": 2,
    "B X": 1,
    "B Y": 2,
    "B Z": 3,
    "C X": 2,
    "C Y": 3,
    "C Z": 1,
}
for line in content:
    opp, end = line.split(" ")
    score += results[line]
    score += [0, 3, 6][["X", "Y", "Z"].index(end)]
print(score)