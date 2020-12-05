MAXROWS = 4      #    contains the number of levels
MAXVALUES = 4    #    contains the maximum combination for a given nested variables.

# display = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# Initialise list, and target sum.
display = []
target = 2020

# Parse values from file into list.
with open("Input Values.txt", 'r') as values_file:
    for row in values_file:
        display.append(int(row))

arrs = [0] * MAXROWS   # represent the different variables in the for loops
status = False

while not status:

    total = 0
    # calculate total for exit condition
    for r in range(MAXROWS):
        total += arrs[r]
        # test for exit condition
    if total == (MAXVALUES - 1) * MAXROWS:
        status = True

    # printing
    for r in range(MAXROWS):
        print(display[arrs[r]], end=' ')  # print(arrs[r])
    print()

    # increment loop variables
    change = True
    r = MAXROWS-1    # start from innermost loop

    while change and r >= 0:
        # increment the innermost variable and check if spill overs
        if (arrs[r] + 1) > MAXVALUES-1:
            arrs[r] += 1
            arrs[r] = 0     #  // reintialize loop variable
            # Change the upper variable by one
            # We need to increment the immediate upper level loop by one
            change = True
        else:
            arrs[r] += 1
            change = False   # Stop as there the upper levels of the loop are unaffected

            # We can perform any inner loop calculation here arrs[r]

        r -= 1  #  move to upper level of the loop
