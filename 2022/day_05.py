content = [x.strip() for x in open("text_05.txt").readlines()]

stacks = ["PLMNWVBH", "HQM", "LMQFGBDN", "GWMQFTZ", "PHTM", "TGHDJMBC", "RVFBNM", "SGRMHLP", "NCBDP"]

for line in content:
    a = int(line.split()[1])
    _from = int(line.split()[3])
    to = int(line.split()[5])

    str_from = stacks[_from - 1]
    str_to = stacks[to - 1]

    # Part 1
    # for x in range(a):
    #     str_to = str_from[0] + str_to
    #     str_from = str_from[1:]

    # Part 2
    str_to = str_from[:a] + str_to
    str_from = str_from[a:]

    stacks[_from - 1] = str_from
    stacks[to - 1] = str_to
print("".join(s[0] for s in stacks))
