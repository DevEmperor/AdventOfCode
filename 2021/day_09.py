from PIL import Image

with open("text_09.txt") as f:
    content = f.readlines()
content = [x.strip() for x in content]

# part 1
s = 0
for y in range(len(content)):
    for x in range(len(content[y])):
        if y > 0 and content[y-1][x] <= content[y][x]: continue  # top
        if y < len(content) - 1 and content[y + 1][x] <= content[y][x]: continue  # bottom
        if x > 0 and content[y][x-1] <= content[y][x]: continue  # right
        if x < len(content[y]) - 1 and content[y][x+1] <= content[y][x]: continue  # left

        s += 1 + int(content[y][x])
print(s)


# part 2
img = Image.new(mode="RGB", size=(100, 100), color=(255, 255, 255))
for idy, y in enumerate(content):
    for idx, x in enumerate(y):
        if x == "9": img.putpixel((idx, idy), (0, 0, 0))
img.save("text_09_part2.png")
# find three largest basins using GIMP and magic wand ;)
