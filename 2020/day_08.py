content = [x.strip() for x in open("text_08.txt").readlines()]


def run_code(code):
    accumulator = 0
    line_number = 0
    lines_done = []
    while line_number not in lines_done:
        try:
            i = code[line_number]
        except IndexError:
            break
        command = i.split(" ")[0]
        attr = i.split(" ")[1]
        lines_done.append(line_number)
        if command == "acc":
            accumulator += int(attr)
            line_number += 1
        if command == "nop":
            line_number += 1
        if command == "jmp":
            line_number += int(attr)
    if line_number == len(code):
        return [accumulator, True]
    else:
        return [accumulator, False]


print(run_code(content)[0])

for x, n in enumerate(content):
    attribute = n.split(" ")[1]
    before = ""
    if n.split(" ")[0] == "nop":
        before = "nop "
        content[x] = "jmp " + attribute
    elif n.split(" ")[0] == "jmp":
        before = "jmp "
        content[x] = "nop " + attribute
    else:
        continue
    results = run_code(content)
    if not results[1]:
        content[x] = before + attribute
    else:
        print(results[0])
        break

