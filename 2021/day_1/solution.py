from typing import List, Dict


def changes_in_list(values: List[int], window_length: int = 1) -> Dict:
    # Function take a list of ints and returns a dictionary with the following elements:
    # sample_size - the length of the input list of ints.
    # window_length - the size of the window over which we are to sum the int values for comparison. E.g. a window of 3
    #                 would sum the next three values in the list (say x, x+1, and x+2), and compare this sum to the
    #                 sum of the subsequent set of three values (x+1, x+2 and x+3).
    #                 The window length defaults to 1.
    # comparisons - the number of comparisons made between the sets created using the specified window length.
    # increases - the number of times the total increases from one set to the next.
    # decreases - the number of times the total decreases from one set to the next.

    # Initialise counts for number of increases and decreases.
    increases = 0
    decreases = 0

    # Loop through the list until we have no sets of the required window length remaining.
    for i in range(len(values) - window_length):
        # if the current set sums to less than the next set, add an increase.
        if sum(values[i: i + window_length]) < sum(values[i + 1: i + 1 + window_length]):
            increases += 1
        # if the current set sums to more than the next set, add a decrease.
        elif sum(values[i: i + window_length]) > sum(values[i + 1: i + 1 + window_length]):
            decreases += 1

    result = {"sample_size": len(values),
              "window_length": window_length,
              "comparisons": len(values) - window_length,
              "increases": increases,
              "decreases": decreases}

    return result


# Read in list and count the number of times an element is greater than the previous element.

# Initialise list.
readings = []
# Parse values from file into list.
with open("input.csv", 'r') as input_file:
    for row in input_file:
        readings.append(int(row.strip()))

changes = changes_in_list(readings, window_length=3)

print("The number of readings is {}.\n"
      "The set window length used is {}.\n"
      "Number of comparisons made is {}.\n"
      "Number of times the depth increases is {}.\n"
      "Number of times the depth decreases is {}."
      .format(changes["sample_size"],
              changes["window_length"],
              changes["comparisons"],
              changes["increases"],
              changes["decreases"]))
