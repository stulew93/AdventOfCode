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
    :return: A list of the items which ar esplit between compartments in each rucksack.
    """
    split_items = []
    for contents in contents_list:
        num_items = len(contents)
        split_item = next(iter(set(contents[:int(num_items/2)]).intersection(set(contents[int(num_items/2):]))))
        split_items.append(split_item)
    return split_items

def get_total_priority(contents_list: list) -> int:
    """
    Takes in the list containing the representations of the contents of each rucksack, figures out which items have
    been split between the compartments, and returns the combined priority value of all the items.
    :param contents_list: A list of strings, each representing the contents of a rucksack.
    :return: The total of the priority values of the split items.
    """
    # Get a list of the items which are split in each rucksack.
    split_item_list = get_split_item_list(contents_list)
    # Get the total priority using the priority dict.
    total_priority = sum([priority[item] for item in split_item_list])
    return total_priority

if __name__ == "__main__":
    filepath = "input.csv"
    input_list = ingest_csv_to_list(filepath)
    print(input_list)

    test = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw"
    ]
    test_output = get_total_priority(test)
    print(type(test_output))
    print(test_output)
