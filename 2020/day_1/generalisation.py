from typing import List
from functools import reduce

# Todo: Try and generalise the concept to work for any number of values in the list.


def target_sum_product(values: List[int], sum_target: int, num_values: int = 2) -> int:
    """Returns the product of the first set of n values found in l which add up to s.
    If no set of values found that satisfy requirements, return -1.

    Complexity increases with size of values list, and size of num_values.
    """
    print("Number of values in list is {}.".format(len(values)))

    value_set = None

    for i in range(len(values) - (num_values - 1)):
        loop_level = num_values - 1
        test_set = [0] * num_values

        while loop_level >= 0:
            test_set[loop_level] = values[i + loop_level]
            loop_level -= 1

        print(test_set, ': ', sum(test_set))

        if sum(test_set) == sum_target:
            value_set = test_set
            break

    print("Values in list with sum {} are:")
    for value in value_set:
        print(value)

    product = reduce(lambda x, y: x * y, value_set, 1)

    return product


# Initialise list, target sum and number of values wanted from list.
value_list = []
target = 2020
num_vals = 3

# Parse values from file into list.
with open("Input Values.txt", 'r') as values_file:
    for row in values_file:
        value_list.append(int(row))

result = target_sum_product(value_list, target, num_vals)

print("The product is {].".format(result))
