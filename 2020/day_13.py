timestamp = int(open("text_13.txt").readline().strip())
notes = open("text_13.txt").readlines()[1]

ids = [i for i in notes.split(',') if i != "x"]
wait = []
for bus_id in ids:
    bus_id = int(bus_id)
    value = bus_id
    while value < timestamp:
        value += bus_id
    wait.append(value - timestamp)

print(min(wait) * int(ids[wait.index(min(wait))]))

