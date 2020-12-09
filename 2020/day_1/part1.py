# Ingest list of values, find the pair that sum to 2020, and calculate the product.

# Initialise list, and target sum.
value_list = []
target = 2020

# Parse values from file into list.
with open("Input Values.txt", 'r') as values_file:
    for row in values_file:
        value_list.append(int(row))

print("Number of values is {}.\n".format(len(value_list)))

# Check list.
# for item in values_list:
#     print(item)

# Get max and min values in list.
max_val = max(value_list)
min_val = min(value_list)
print("Max value in list is {}.\nMin value in list is {}.\n".format(max_val, min_val))

# For each value in list x, see if target - x exists in list. If it does, then stop.
value_1 = None
value_2 = None
count = 1
for value in value_list:
    test_value = target - value
    if test_value in value_list:
        value_1 = value
        value_2 = test_value
        break
    count += 1

print("The values that sum to {0} are {1} and {2}.\nThe product of {1} and {2} is {3}.\n"
      .format(target, value_1, value_2, value_1 * value_2))
print(count)
