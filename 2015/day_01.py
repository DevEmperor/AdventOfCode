with open("text_01.txt") as f:
	content = f.read().strip()

floor = 0
for idx, i in enumerate(content):
	if i == "(":
		floor += 1
	elif i == ")":
		floor -= 1
	# if floor < 0:  # uncomment for part 2
	# 	print(idx + 1)
	# 	break
print(floor)

