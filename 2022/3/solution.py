import os
import string
import sys

# To import from utils
sys.path.append(os.path.join(os.path.dirname(sys.path[0])))

from utils import get_demo_data, get_input_data

lines = get_input_data()

priority_dict = {letter: idx + 1 for idx, letter in enumerate(string.ascii_letters)}

#Part 1
common_letters = []
for line in lines:
    line = line.strip()  # Remove trailing \n --perhaps I rethink utils?
    first_rucksack, second_rucksack = set(line[: len(line) // 2]), set(line[len(line) // 2 :])
    common_letters.extend(list(first_rucksack.intersection(second_rucksack)))

print(sum([priority_dict[letter] for letter in common_letters]))


#Part 2
badges = []
for idx in range(0,len(lines),3):
    first_elf, second_elf, third_elf = [set(line.strip()) for line in lines[idx:idx+3]] #Really need to do strip in utils..
    badge = first_elf.intersection(second_elf).intersection(third_elf).pop()
    badges.append(badge)

print(sum([priority_dict[badge] for badge in badges]))