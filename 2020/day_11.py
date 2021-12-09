content = [x.strip() for x in open("text_11.txt").readlines()]

counter = 0
new_content = []
while True:
    last_counter = counter
    counter = 0
    for n, i in enumerate(content):
        last_line = ""
        next_line = ""
        line = ""
        for m, j in enumerate(i):
            if j == ".":
                line += "."
                continue
            if n > 0: last_line = content[n - 1]
            if n < len(content) - 1: next_line = content[n + 1]
            occupied_seats = 0
            if last_line != "":
                if last_line[m] == "#": occupied_seats += 1
            if last_line != "" and m < len(i) - 1:
                if last_line[m + 1] == "#": occupied_seats += 1
            if m < len(i) - 1:
                if i[m + 1] == "#": occupied_seats += 1
            if next_line != "" and m < len(i) - 1:
                if next_line[m + 1] == "#": occupied_seats += 1
            if next_line != "":
                if next_line[m] == "#": occupied_seats += 1
            if next_line != "" and n > 0:
                if next_line[m - 1] == "#": occupied_seats += 1
            if m > 0:
                if i[m - 1] == "#": occupied_seats += 1
            if last_line != "" and m > 0:
                if last_line[m - 1] == "#": occupied_seats += 1
            if j == "#" and occupied_seats >= 4:
                counter -= 1
                line += "L"
            elif j == "L" and occupied_seats == 0:
                counter += 1
                line += "#"
            else:
                line += j
        new_content.append(line)
    content = new_content
    new_content = []
    if 2303 == counter:
        print(counter)
        break
