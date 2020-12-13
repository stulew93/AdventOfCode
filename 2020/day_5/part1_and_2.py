# Import list of seat references from file.
seat_refs = []

with open("seats.txt", 'r') as refs:
    for ref in refs:
        ref = ref.rstrip()
        seat_refs.append(ref)

# for seat_ref in seat_refs:
#     print(seat_ref)

# Save seat_ref, row, column, and seat ID as dict (key = seat_id) in list seat_info.
# Seat ID = ( row * 8 ) + column
seat_info = {}

for seat in seat_refs:
    # Row reference contained in first 7 characters of seat_ref.
    seat_row = seat[:7]
    min_row, max_row = 0, 127
    for char in seat_row:
        if min_row == max_row:
            break
        elif char == 'F':
            max_row -= (max_row - min_row) // 2
            max_row -= 1
        else:  # char == 'B'
            min_row += (max_row - min_row) // 2
            min_row += 1

    # Column reference contained in final 3 characters of seat_ref.
    seat_column = seat[7:]
    min_col, max_col = 0, 7
    for char in seat_column:
        if min_col == max_col:
            break
        elif char == 'L':
            max_col -= (max_col - min_col) // 2
            max_col -= 1
        else:  # char = 'R'
            min_col += (max_col - min_col) // 2
            min_col += 1

    seat_id = (max_row * 8) + max_col
    seat_info[seat_id] = (seat, max_row, max_col)

# for seat in seat_info:
#     print(seat, ': ', seat_info[seat])

print("There are {} seats counted.".format(len(seat_refs)))
print("The Seat IDs are between {} and {}.".format(min(seat_info), max(seat_info)))

# Part 2

# To find missing seat number, use set difference function.
# Define complete set of integers between 6 and 951 to compare against.
int_set = set(range(6, 952))
my_seat = list(int_set.difference(set(seat_info)))[0]

print("My seat ID is {}.".format(my_seat))
