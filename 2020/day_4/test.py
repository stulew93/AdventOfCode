# Ingest passports.txt file as list of dictionaries.
passports_list = []

with open("passports.txt", 'r') as passports_file:
    passports_list_raw = passports_file.read().split('\n\n')
    for i in range(len(passports_list_raw)):
        passport_str = passports_list_raw[i].replace('\n', ' ')
        passport_list = [field for field in passport_str.split()]
        passport_dict = dict(field.split(':') for field in passport_list)
        passports_list.append(passport_dict)

keys_check = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

for i in range(len(passports_list)):
    if not keys_check <= passports_list[i].keys():
        print(i, 'Key missing.')
        continue

    if passports_list[i]['hgt'][-2:] not in ('cm', 'in'):
        print(i, 'No in or cm in height')
        continue

    print(i, ' ', passports_list[i]['hgt'], end=' ')

    if(passports_list[i]['hgt'][-2:] == 'cm' and (int(passports_list[i]['hgt'][:-2]) < 150 or int(passports_list[i]['hgt'][:-2]) > 193)) \
            or (passports_list[i]['hgt'][-2:] == 'in' and (int(passports_list[i]['hgt'][:-2]) < 59 or int(passports_list[i]['hgt'][:-2]) > 76)):
        print(True)
    else:
        print(False)
