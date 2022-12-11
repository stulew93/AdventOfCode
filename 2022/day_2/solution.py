from common_functions import ingest_csv_to_list

# Constants:
move_points_pt_1 = {
    'X': 1,  # rock
    'Y': 2,  # paper
    'Z': 3   # scissors
}

round_points_pt_1 = {
    'A X': 3,  # rock, rock
    'A Y': 6,  # rock, paper
    'A Z': 0,  # rock, scissors
    'B X': 0,  # paper, rock
    'B Y': 3,  # paper, paper
    'B Z': 6,  # paper, scissors
    'C X': 6,  # scissors, rock
    'C Y': 0,  # scissors, paper
    'C Z': 3,  # scissors, scissors
}

result_points_pt_2 = {
    'X': 0,  # lose
    'Y': 3,  # draw
    'Z': 6   # win
}

round_points_pt_2 = {
    'A X': 3,  # rock, lose, scissors
    'A Y': 1,  # rock, draw, rock
    'A Z': 2,  # rock, win, paper
    'B X': 1,  # paper, lose, rock
    'B Y': 2,  # paper, draw, paper
    'B Z': 3,  # paper, win, scissors
    'C X': 2,  # scissors, lose, paper
    'C Y': 3,  # scissors, draw, scissors
    'C Z': 1,  # scissors, win, rock
}

def get_round_points(moves: str, part: int) -> int:
    """
    Takes an input representing a round of rock paper scissors, and uses the dicts above to calculate the score for the
    player. For part 1, player moves are second in the string (X, Y or Z). In part 2, the second char represents the
    desired result of the round.
    :param round: A string in the form "A X" representing a round of RPS.
    :param part: The part of the question, 1 or 2.
    :return: An int representing the points scored for the round.
    """
    if part == 1:
        player_move = moves[2]
        return move_points_pt_1[player_move] + round_points_pt_1[moves]
    elif part == 2:
        result = moves[2]
        return result_points_pt_2[result] + round_points_pt_2[moves]

def get_match_points(moves: list, part: int) -> int:
    """
    Takes a list of the moves from all rounds of a match and returns the total score.
    :param moves: A list of moves from all rounds of a match. Each set of moves is in the form "A X" representing a
    round of RPS.
    :param part: The part of the question, 1 or 2.
    :return: An int representing the total player score for the match.
    """
    return sum([get_round_points(round, part) for round in moves])

if __name__ == "__main__":
    filepath = "input.csv"
    strategy_list = ingest_csv_to_list(filepath)
    # Each element in list is three characters in form "A X"
    # for c in strategy_list[0]:
    #     print(c)

    print("Part 1 - total score using given strategy:")
    match_points = get_match_points(strategy_list, 1)
    print(match_points)

    print("Part 2 - total score using given strategy:")
    match_points = get_match_points(strategy_list, 2)
    print(match_points)