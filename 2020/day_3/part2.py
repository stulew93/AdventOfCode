from typing import List
import time


def tree_hits(tree_map: List[str], x_change: int, y_change: int) -> int:
    """Function to calculate how many trees (#) are hit when traversing the tree_map at the gradient -y/x."""

    # Get the width of the tree_map rows. These are continuously repetitive in the x direction.
    row_length = len(tree_map[0])

    # Initialise count of trees hit, and initial position and row.
    trees_hit = 0
    current_position = 0
    current_row = 0

    # Loop while we still have enough rows left.
    while current_row < len(tree_map) - y_change:
        # Move down y_change rows.
        current_row += y_change
        # Move right x_change rows. If we reach the end of a row in the map, move back to the start of the row (as
        # the rows are continuously repetitive).
        current_position = (current_position + x_change) % row_length
        # If there is a tree (#) in current position, increment trees_hit counter.
        if tree_map[current_row][current_position] == '#':
            trees_hit += 1
        #     print("Oof!")
        #     time.sleep(0.1)
        # else:
        #     print("Whee!")

    print("With a gradient of {} over {}, number of trees hit is {}.".format(y_change, x_change, trees_hit))

    return trees_hit


if __name__ == "__main__":
    # Initialise list of tree rows.
    trees_list = []

    # Parse values from file into list.
    with open("map.txt", 'r') as map_file:
        for row in map_file:
            # Strip new line from each row.
            row = row.rstrip()
            trees_list.append(row)

    check = tree_hits(trees_list, 3, 1)

    # x=1, y=1
    a = tree_hits(trees_list, 1, 1)
    # x=3, y=3
    b = tree_hits(trees_list, 3, 1)
    # x=5, y=1
    c = tree_hits(trees_list, 5, 1)
    # x=7, y=1
    d = tree_hits(trees_list, 7, 1)
    # x=1, y=2
    e = tree_hits(trees_list, 1, 2)

    print("Product of trees hit is {}.".format(a * b * c * d * e))
