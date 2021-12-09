# yzbqklnj
import hashlib

for i in range(1000000000):
    if hashlib.md5(("yzbqklnj" + str(i)).encode()).hexdigest().startswith("00000"):  # add one zero for part two
        print(i)
        break
