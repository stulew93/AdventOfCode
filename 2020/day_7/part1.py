# --- Day 7: Handy Haversacks --- You land at the regional airport in time for your next flight. In fact,
# it looks like you'll even have time to grab some food: all flights are currently delayed due to issues in luggage
# processing.
#
# Due to recent aviation regulations, many rules (your puzzle input) are being enforced about bags and their
# contents; bags must be color-coded and must contain specific quantities of other color-coded bags. Apparently,
# nobody responsible for these regulations considered how long they would take to enforce!
#
# For example, consider the following rules:
#
# light red bags contain 1 bright white bag, 2 muted yellow bags. dark orange bags contain 3 bright white bags,
# 4 muted yellow bags. bright white bags contain 1 shiny gold bag. muted yellow bags contain 2 shiny gold bags,
# 9 faded blue bags. shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags. dark olive bags contain 3 faded
# blue bags, 4 dotted black bags. vibrant plum bags contain 5 faded blue bags, 6 dotted black bags. faded blue bags
# contain no other bags. dotted black bags contain no other bags. These rules specify the required contents for 9 bag
# types. In this example, every faded blue bag is empty, every vibrant plum bag contains 11 bags (5 faded blue and 6
# dotted black), and so on.
#
# You have a shiny gold bag. If you wanted to carry it in at least one other bag, how many different bag colors would
# be valid for the outermost bag? (In other words: how many colors can, eventually, contain at least one shiny gold
# bag?)
#
# In the above rules, the following options would be available to you:
#
# A bright white bag, which can hold your shiny gold bag directly. A muted yellow bag, which can hold your shiny gold
# bag directly, plus some other bags. A dark orange bag, which can hold bright white and muted yellow bags,
# either of which could then hold your shiny gold bag. A light red bag, which can hold bright white and muted yellow
# bags, either of which could then hold your shiny gold bag. So, in this example, the number of bag colors that can
# eventually contain at least one shiny gold bag is 4.
#
# How many bag colors can eventually contain at least one shiny gold bag? (The list of rules is quite long; make sure
# you get all of it.)

# Import bag colour rules from file into dictionary of dictionaries. Key is bag colour, value is dictionary with
# key secondary bag colour and value quantity.
colour_rules = {}

with open("bag_colours.txt", 'r') as colours_file:
    for row in colours_file:
        # Remove words 'bags', 'bag' and 'contain' from row, all commas, and remove trailing new line and full stop.
        row = row.replace(" bags", '').replace(" bag", '').replace(" contain", '').replace(',', '').rstrip('\n')\
            .rstrip('.')
        # Get list of elements to build up dict entry.
        row_elements = row.split(' ')

        # Key equals first two elements - delete them from list.
        row_key = row_elements[0] + ' ' + row_elements[1]
        del row_elements[1]
        del row_elements[0]

        # Build linking dictionary from remaining elements.
        row_value = {}

        # Using the integer division to set the range of the loop deals with the "no other bags" situation,
        # as in this instance row_elements only has len 2; 2 // 3 = 0, so we don't enter the for loop at all,
        # and row_value remains an empty dict.
        for i in range(len(row_elements) // 3):
            colour = row_elements[3 * i + 1] + ' ' + row_elements[3 * i + 2]
            quantity = row_elements[3 * i]
            row_value[colour] = int(quantity)

        # Add to colour_rules dictionary.
        colour_rules[row_key] = row_value

# for colour in colour_rules:
#     print(colour, ': ', colour_rules[colour])

print("There are {} colours.".format(len(colour_rules)))

# Find how many bags can contain a shiny gold bag.
gold_holders = set()

for colour in colour_rules:
    if "shiny gold" in colour_rules[colour].keys():
        gold_holders.add(colour)

        colour_added = True
        while colour_added:

