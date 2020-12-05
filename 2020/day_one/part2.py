from typing import List


def target_sum_product_three(values: List[int], sum_target: int) -> tuple:
    """Returns a tuple containing the first set of 3 values found in values which add up to sum_target,
    their product, and a count of how many combinations were tried.
    If no set of values found that satisfy requirements, return None values and product = -1.
    """
    # Initialise variable.
    value_1 = None
    value_2 = None
    value_3 = None
    product = -1
    count = 1

    for i in range(len(value_list)):
        for j in range(len(value_list)):
            if j <= i:
                continue
            for k in range(len(value_list)):
                if k <= j:
                    continue
                elif value_list[i] + value_list[j] + value_list[k] == target:
                    value_1 = value_list[i]
                    value_2 = value_list[j]
                    value_3 = value_list[k]
                    product = value_1 * value_2 * value_3
                    return value_1, value_2, value_3, product, count
                else:
                    count += 1

    return value_1, value_2, value_3, product, count


if __name__ == "__main__":

    # Initialise list, and target sum.
    value_list = []
    target = 2020

    # Parse values from file into list.
    with open("Input Values.txt", 'r') as values_file:
        for row in values_file:
            value_list.append(int(row))

    print("Number of values is {}.\n".format(len(value_list)))

    # Get max and min values in list.
    max_val = max(value_list)
    min_val = min(value_list)
    print("Max value in list is {}.\nMin value in list is {}.\n".format(max_val, min_val))

    result = target_sum_product_three(value_list, target)

    # Get the three values (x, y, z), the product (p), and the count (c).
    x, y, z, p, c = result

    print("The values that sum to {0} are {1}, {2} and {3}.\nThe product of {1}, {2} and {3} is {4}.\n"
          .format(target, x, y, z, p))
    print("Combinations of values checked: ", c)
