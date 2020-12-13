# Import group answers from file.
group_answers_list = []

with open("answers.txt", 'r') as answers_file:
    for group in answers_file.read().split('\n\n'):
        group_answers_list.append(group.replace('\n', ''))

# Get number of individual questions with 'Yes' answers by converting each group string into a set and taking the
# size. Add each total to the overall sum.
total_yes = 0

for group in group_answers_list:
    group_yes = len(set(group))
    total_yes += group_yes

print("There are {} groups.".format(len(group_answers_list)))
print("The sum of the counts of the questions answered with a 'Yes' by at least one member of a group is {}.".format(
    total_yes))
