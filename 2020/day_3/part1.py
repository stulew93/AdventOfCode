# Ingest map of trees as list.

# Initialise list of tree rows.
trees_list = []

# Parse values from file into list.
with open("map.txt", 'r') as map_file:
    for row in map_file:
        # Strip new line from each row.
        row = row.rstrip()
        trees_list.append(row)

# for row in trees_list:
#     print(row)

# Get number of positions in each row on the map.
row_length = len(trees_list[0])
map_depth = len(trees_list)
print("Length of each row on map is {}.".format(row_length))
print("There are {} rows of trees on the map.".format(map_depth))

# Just checking there are actually 31 characters in each row!
# print(trees_list[0])
# for i in range(len(trees_list[0])):
#     print(trees_list[0][i], end='')
#     if (i + 1) % 10 == 0:
#         print()

# Initialise count of trees hit, and initial position.
trees_hit = 0
current_position = 0

# Parse through each row in the map. Move three characters to the left on each new row. If you hit the end of the
# row, go to the start of the same row. If there is a tree (#) in the final position, increment trees_hit.
for i in range(len(trees_list) - 1):
    # Move down one row.
    row = trees_list[i + 1]
    # Move right 3 positions.
    current_position = (current_position + 3) % row_length
    if row[current_position] == '#':
        trees_hit += 1
    # print("Row {}, trees hit {}".format(i + 2, trees_hit))

print("Number of trees hit is {}.".format(trees_hit))
