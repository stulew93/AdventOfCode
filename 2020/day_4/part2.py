# Ingest passports.txt file as list of dictionaries.
passports_list = []

with open("passports.txt", 'r') as passports_file:
    passports_list_raw = passports_file.read().split('\n\n')
    for i in range(len(passports_list_raw)):
        passport_str = passports_list_raw[i].replace('\n', ' ')
        passport_list = [field for field in passport_str.split()]
        passport_dict = dict(field.split(':') for field in passport_list)
        passports_list.append(passport_dict)

hex_chars = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'}

test = passports_list[0]
print(test)
print(test['hcl'])
print(test['hcl'][1:])
print(set(test['hcl'][1:]))
print(not set('789327adef') <= hex_chars)

# Increment count of valid passports as in part 1, but also applying the additional checks each time.
keys_check = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
valid_passports = 0

for i in range(len(passports_list)):
    print(i, end=' ')
    # Check for missing passport fields, i.e. keys_check is not a subset of the keys in passport.
    if not keys_check <= passports_list[i].keys():
        print('Invalid - Key missing.')
        continue
    # Invalid if birth year is not 4 digits, or not between 1920 and 2002 inclusive.
    elif len(passports_list[i]['byr']) != 4 or int(passports_list[i]['byr']) < 1920 or int(passports_list[i]['byr']) > 2002:
        print('Invalid - Birth year.')
        continue
    # Invalid if issue year is not 4 digits, or not between 2010 and 2020 inclusive.
    elif len(passports_list[i]['iyr']) != 4 or int(passports_list[i]['iyr']) < 2010 or int(passports_list[i]['iyr']) > 2020:
        print('Invalid - Issue year.')
        continue
    # Invalid if expiration year is not 4 digits, or not between 2020 and 2030 inclusive.
    elif len(passports_list[i]['eyr']) != 4 or int(passports_list[i]['eyr']) < 2020 or int(passports_list[i]['eyr']) > 2030:
        print('Invalid - Expiration year.')
        continue
    # Invalid if height does not end in 'in' or 'cm', or value not between either 150-193cm or 59-76in.
    elif passports_list[i]['hgt'][-2:] not in ('cm', 'in'):
        print('Invalid - Height not end with in or cm.')
        continue
    # Invalid if height value not between either 150-193cm or 59-76in.
    elif (passports_list[i]['hgt'][-2:] == 'cm' and (int(passports_list[i]['hgt'][:-2]) < 150 or int(passports_list[i]['hgt'][:-2]) > 193))\
            or (passports_list[i]['hgt'][-2:] == 'in' and (int(passports_list[i]['hgt'][:-2]) < 59 or int(passports_list[i]['hgt'][:-2]) > 76)):
        print('Invalid - Height not in required range.')
        continue
    # Invalid if hair colour first char not a #.
    elif passports_list[i]['hcl'][0] != '#':
        print('Invalid - Hair colour # char.')
        continue
    # Invalid if hair colour not string of 6 chars in 0-9 and a-f following the #, i.e. the string is a superset.
    elif not set(passports_list[i]['hcl'][1:]) <= hex_chars or len(passports_list[i]['hcl'][1:]) != 6:
        print('Invalid - Hair colour code.')
        continue
    # Invalid if eye colour not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}.
    elif passports_list[i]['ecl'] not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
        print('Invalid - Eye colour.')
        continue
    # Invalid if passport ID not a nine-digit number, inc leading zeros.
    elif not set(passports_list[i]['pid']) <= {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'} or len(passports_list[i]['pid']) != 9:
        print('Invalid - Passport ID.')
        continue
    # If none of above are true, passport is valid.
    else:
        print('Valid')
        valid_passports += 1

print("There are {} passports in the sample, of which {} are valid.".format(len(passports_list), valid_passports))
