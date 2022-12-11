def ingest_csv(filepath: str) -> list:
    result_list = []
    with open(filepath, 'r') as input_file:
        for row in input_file:
            result_list.append(str(row.strip()))

    return result_list

def create_nested_list(x: list) -> list:
    """
    Given a list input, the function will return a list of lists. The input list will be broken up using empty string
    elements as delimiters between lists.
    :param x: list to be collapsed into a list of lists.
    :return: list of lists.
    """
    result_list = []
    current_sub_list = []
    # Cycle through the values in the input list.
    for y in x:
        # If the value is an empty string, that means we've reached the end of the current sub list. Append the sub
        # list to the result.
        if y == "":
            result_list.append(current_sub_list)
            current_sub_list = []
        # Otherwise add the current value to the current sub list.
        else:
            current_sub_list.append(y)
    # Append the final sub list to the result.
    result_list.append(current_sub_list)

    return result_list

def get_max_nested_list_sum(x: list) -> tuple:
    """
    Given a list of lists containing numerical values, the function will return a tuple containing the index of the
    list with the greatest sum, and the sum.
    :param x: List of lists containing numerical values.
    :return: Tuple containing the index of the list with the greatest sum, and the sum.
    """
    current_max = 0
    current_index = None
    for i in range(len(x)):
        current_sum = sum([int(y) for y in x[i]])
        if current_sum > current_max:
            current_max, current_index = current_sum, i

    return current_index, current_max

def nested_lists_totals(x: list) -> list:
    """
    Given a list of lists containing numerical values, returns a list of the totals of those nested lists.
    :param x: List of lists containing numerical values.
    :return: List of the totals of each nested list.
    """
    return_list = []
    for y in x:
        nested_sum = sum([int(z) for z in y])
        return_list.append(nested_sum)

    return return_list

def get_three_greatest_vals(x: list) -> list:
    """
    Returns a list of the three greatest values in the input list, in descending order.
    :param x: List of numerical values.
    :return: List of the three greatest values in input, in descending order.
    """
    x.sort(reverse=True)
    return x[:3]


if __name__ == "__main__":
    filepath = "input.csv"
    calorie_list = ingest_csv(filepath)
    list_by_elf = create_nested_list(calorie_list)
    print(list_by_elf)
    max_calories = get_max_nested_list_sum(list_by_elf)
    print(max_calories)
    calorie_totals_by_elf = nested_lists_totals(list_by_elf)
    print("Part 1 - Get the greatest calorie total:")
    calorie_totals_by_elf.sort(reverse=True)
    print(calorie_totals_by_elf[0])

    greatest_cal_totals = get_three_greatest_vals(calorie_totals_by_elf)
    print("Part 2 - Get the sum of the three greatest calorie totals:")
    print(greatest_cal_totals, "Total:", sum(greatest_cal_totals))
