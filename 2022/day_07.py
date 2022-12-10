content = [x.strip() for x in open("text_07.txt").readlines()]


def dir_size(dir):
    subs = dirs[dir]
    s = subs[0]
    if len(subs) > 1:
        for sub in subs[1:]:
            s += dir_size(sub)
    return s


dirs = {}
cdir = ""
d = [0]
for line in content:
    if not line.startswith("$"):
        l = line.split()
        if l[0].isdigit():
            d[0] += int(l[0])
        else:
            d.append(cdir + "/" + l[1])
        dirs[cdir] = d

    if line.startswith("$ cd /"): cdir = ""
    elif line.startswith("$ cd .."): cdir = cdir[:-cdir[::-1].index("/")-1]
    elif line.startswith("$ cd "): cdir += "/" + line.replace("$ cd ", "")

    if line == "$ ls": d = [0]


# Part 1
print(sum(dir_size(d) for d in dirs.keys() if dir_size(d) <= 100000))

# Part 2
we_need = 30000000 - (70000000 - dir_size(""))
print(min([dir_size(d) for d in dirs.keys() if dir_size(d) >= we_need]))
