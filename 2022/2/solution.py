import os
import sys

# To import from utils
sys.path.append(os.path.join(os.path.dirname(sys.path[0])))

from utils import get_demo_data, get_input_data

lines = get_input_data()

# How many points each shape is worth
shape_score_mappings = {"X": 1, "Y": 2, "Z": 3, "A": 1, "B": 2, "C": 3}

# Part 1
final_score = 0
for line in lines:
    opponent_choice, our_choice = line.strip().split()

    # choice score
    our_score = shape_score_mappings[our_choice]
    final_score += our_score

    opponent_score = shape_score_mappings[opponent_choice]
    # outcome score
    if our_score - opponent_score == 1 or our_score - opponent_score == -2:  # win
        final_score += 6
    elif our_score == opponent_score:  # draw
        final_score += 3

print(final_score)

# Part 2
final_score = 0
for line in lines:
    opponent_choice, our_choice = line.strip().split()

    opponent_score = shape_score_mappings[opponent_choice]
    # choice score
    if our_choice == "X":  # lose
        # only shape score is added
        shape_score = opponent_score - 1 if opponent_score - 1 > 0 else 3
        final_score += shape_score
    elif our_choice == "Y":  # draw
        # shape score + draw score
        final_score += opponent_score
        final_score += 3
    else:  # Win
        # shape score + win score
        shape_score = opponent_score + 1 if opponent_score + 1 < 4 else 1
        final_score += shape_score
        final_score += 6

print(final_score)
