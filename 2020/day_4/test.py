passports_list = []

with open("passports.txt", 'r') as passports_file:
    passports_list_raw = passports_file.read().split('\n\n')
    for i in range(len(passports_list_raw)):
        passport_str = passports_list_raw[i].replace('\n', ' ')
        passport_list = [item for item in passport_str.split()]
        passport_dict = dict(item.split(':') for item in passport_list)
        passports_list.append(passport_dict)

# for i in range(1):
    # print(passports_list_raw[i].replace('\n', ' '))
    # thing = passports_list_raw[i].replace('\n', ' ')
    # test_gen = [item for item in thing.split()]
    # test_dict = dict(item.split(':') for item in test_gen)
    # print(test_dict)

for passport in passports_list:
    print(passport)
