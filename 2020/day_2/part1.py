# Ingest list of passwords; find the sub-set that have the specified letter between the min and max occurrences.

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
    min_count = password_info[0]
    max_count = password_info[1]
    key_letter = password_info[2]
    password = password_info[3]

    if int(min_count) <= password.count(key_letter) <= int(max_count):
        count += 1
        print(passwords_list[i], '\tyep')
    else:
        print(passwords_list[i], '\tnope')

print("\nOut of {} passwords, {} are valid.".format(len(passwords_list), count))
