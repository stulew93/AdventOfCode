# Import group answers from file.
group_answers_list = []

with open("answers.txt", 'r') as answers_file:
    for group in answers_file.read().split('\n\n'):
        member_answers = []
        for member in group.split('\n'):
            member_answers.append(member)
        group_answers_list.append(member_answers)

# Find count of questions for each group that each group member answered 'Yes' (i.e. the question appears in their
# list). Get total of the counts for each group.
total_yes = 0

for group in group_answers_list:
    print(group)
    group_yes = {}
    for member in group:
        print(member)
        if group_yes == {}:
            group_yes = set(member)
        else:
            group_yes = group_yes.intersection(set(member))
        print(group_yes)
        print(len(group_yes))

    total_yes += len(group_yes)

print("There are {} groups.".format(len(group_answers_list)))
print("The sum of the counts of the questions answered with a 'Yes' by all members of a group is {}.".format(total_yes))
