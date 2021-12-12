# Initialise list.
directions = []
# Parse values from file into list.
with open("input.csv", 'r') as input_file:
    for row in input_file:
        directions.append(row.strip().split())

# Remove random empty strings...
directions = list(filter(None, directions))

for d in directions:
    print(d)

position = {"horizontal": 0,
            "depth": 0}

for direction in directions:
    if direction[0] == "forward":
        position["horizontal"] += int(direction[1])
    elif direction[0] == "up":
        position["depth"] -= int(direction[1])
    elif direction[0] == "down":
        position["depth"] += int(direction[1])
    else:
        print("Sorry, don't recognise command '{}'.".format(direction[0]))

    print(position)

print(position["horizontal"] * position["depth"])
