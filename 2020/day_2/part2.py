# Find passwords that have exactly one occurrence of the specified letter in the indicated positions.
# e.g. 6-7 w: wwhmzwtwwk --> must have exactly one 'w' in the 6th and 7th characters in string.

# Initialise list, and target sum.
passwords_list = []

# Parse values from file into list.
with open("passwords.txt", 'r') as passwords_file:
    for row in passwords_file:
        row = row.rstrip()
        passwords_list.append(row)

# Initiate count of correct passwords.
count = 0

for i in range(len(passwords_list)):
    # Remove the ':' character, replace the '-' with a space, and perform split around space character.
    password_info = passwords_list[i].replace(':', '').replace('-', ' ').split(' ')
    # String positions given as '1st' and '2nd' characters in string rather than as indices, so minus one.
    position_one = int(password_info[0]) - 1
    position_two = int(password_info[1]) - 1
    key_letter = password_info[2]
    password = password_info[3]

    # Define check statements as boolean variables.
    check_one = (password[position_one] == key_letter)
    check_two = (password[position_two] == key_letter)

    # Use bitwise XOR operation.
    if check_one ^ check_two:
        count += 1
        print(passwords_list[i], '\tyep')
    else:
        print(passwords_list[i], '\tnope')

print("\nOut of {} passwords, {} are valid.".format(len(passwords_list), count))
