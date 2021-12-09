with open("text_06.txt") as file:
    banks = [int(bank) for bank in file.readline().split("\t")]

seen = [tuple(banks)]
counter = 0

while len(seen) == len(set(seen)):
    most = max(banks)
    idx_most = banks.index(most)
    banks[idx_most] = 0
    for i in range(most):
        banks[(idx_most + i + 1) % len(banks)] += 1
    seen.append(tuple(banks))
    counter += 1

print(counter)

print(counter - seen.index(seen[-1]))