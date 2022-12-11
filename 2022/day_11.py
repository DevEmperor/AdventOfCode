from math import lcm

content = [x.strip() for x in open("text_11.txt").readlines()]

monkeys = [
    {
        "idx": int(content[i][7]),
        "items": list(map(int, content[i + 1].split(": ")[1].split(", "))),
        "op": content[i + 2].split("= ")[1],
        "test": int(content[i + 3].split("by ")[1]),
        "test_true": int(content[i + 4].split("monkey ")[1]),
        "test_false": int(content[i + 5].split("monkey ")[1]),
        "inspected": 0
    } for i in range(0, len(content), 7)]


for current_round in range(20):  # 10000 for part 2
    for i in range(len(monkeys)):
        items = monkeys[i]["items"]
        for item in items:
            new = int(eval(monkeys[i]["op"].replace("old", str(item))))
            new //= 3  # remove for part 2

            if new % int(monkeys[i]["test"]) == 0:
                monkeys[monkeys[i]["test_true"]]["items"].append(new % lcm(*[int(monkeys[x]["test"]) for x in range(len(monkeys))]))
            else:
                monkeys[monkeys[i]["test_false"]]["items"].append(new)
        monkeys[i]["items"] = []
        monkeys[i]["inspected"] += len(items)

results = [x["inspected"] for x in monkeys]
print(sorted(results)[-1] * sorted(results)[-2])
