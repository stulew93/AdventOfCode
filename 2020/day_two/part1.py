# Ingest list of values, find the pair that sum to 2020, and calculate the product.

# Initialise list, and target sum.
value_list = []

# Parse values from file into list.
with open("Input Values.txt", 'r') as values_file:
    for row in values_file:
        value_list.append(int(row))