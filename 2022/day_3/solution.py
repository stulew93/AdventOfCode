import string
from AdventOfCode.common_functions import ingest_csv_to_list
# import AdventOfCode.common_functions as cf

# Create list of letters for prioritising - a-z then A-Z in one string.
letters = string.ascii_letters
# Dict for priority order.
priority = {}
i = 1
for l in letters:
    priority[l] = i
    i += 1

def get_split_item_list(contents_list: list) -> list:
    """
    Find the split items in each rucksack by splitting each content representation string in half and identifying the
    item (char) which is in both halves.
    :param contents_list: A list of strings, each representing the contents of a rucksack.
    :return: A list of the items which are split between compartments in each rucksack.
    """
    split_items = []
    for contents in contents_list:
        num_items = len(contents)
        split_item = next(iter(set(contents[:int(num_items/2)]).intersection(set(contents[int(num_items/2):]))))
        split_items.append(split_item)
    return split_items

def get_groups(contents_list: list) -> list:
    """
    Get a list of lists - each list is a group of three elves.
    :param contents_list: A list of strings, each representing the contents of a rucksack.
    :return: A list of lists of size three, representing each group of three elves.
    """
    groups = []
    current_group = []
    for elf in contents_list:
        current_group.append(elf)
        if len(current_group) == 3:
            groups.append(current_group)
            current_group = []
    return groups

def get_shared_item_list(contents_list: list) -> list:
    """
    Find the item that's shared between the three elves in each group. Each group is made up of each set of three
    consecutive items in the contents list.
    :param contents_list: A list of strings, each representing the contents of a rucksack.
    :return: A list of the items which are shared between each group of three elves.
    """
    # Get a list of lists - each list is a group of three elves.
    groups = get_groups(contents_list)
    shared_items = []
    for group in groups:
        shared_item = next(iter(set(group[0]).intersection(set(group[1]).intersection(set(group[2])))))
        shared_items.append(shared_item)
    return shared_items

def get_total_priority(contents_list: list, part: int) -> int:
    """
    Takes in the list containing the representations of the contents of each rucksack, figures out which items have
    been split between the compartments, and returns the combined priority value of all the items.
    :param contents_list: A list of strings, each representing the contents of a rucksack.
    :return: The total of the priority values of the split items.
    """
    if part == 1:
        # Get a list of the items which are split in each rucksack.
        target_item_list = get_split_item_list(contents_list)
    elif part == 2:
        # Get a list of the items which are shared between the three elves in each group.
        target_item_list = get_shared_item_list(contents_list)
    # Get the total priority using the priority dict.
    total_priority = sum([priority[item] for item in target_item_list])
    return total_priority

if __name__ == "__main__":
    filepath = "input.csv"
    input_list = ingest_csv_to_list(filepath)
    # print(input_list)

    print("Part 1 - total priority:")
    total_priority = get_total_priority(input_list, 1)
    print(total_priority)

    print("Part 2 - total priority:")
    total_priority = get_total_priority(input_list, 2)
    print(total_priority)
