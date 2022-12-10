content = [x.strip() for x in open("text_06.txt").readlines()][0]

# for Part 2 replace all "4" with "14"
for i in range(4, len(content)):
    if len(set(content[i-4:i])) == len(content[i-4:i]):
        print(i)
        break
