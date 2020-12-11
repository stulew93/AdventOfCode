# Ingest passports.txt file as list of dictionaries.
passports_list = []

with open("passports.txt", 'r') as passports_file:
    passports_list_raw = passports_file.read().split('\n\n')
    for i in range(len(passports_list_raw)):
        passport_str = passports_list_raw[i].replace('\n', ' ')
        passport_list = [field for field in passport_str.split()]
        passport_dict = dict(field.split(':') for field in passport_list)
        passports_list.append(passport_dict)

# # Check dictionaries exist.
# for passport in passports_list:
#     print(passport)

# Define keys to check for.
keys_check = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

# Initialise count of valid passports.
valid_passports = 0

# Check that keys_check is subset of keys for each passport.
for passport in passports_list:
    if keys_check <= passport.keys():
        valid_passports += 1

print("There are {} passports in the sample, of which {} are valid.".format(len(passports_list), valid_passports))
