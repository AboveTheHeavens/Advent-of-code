import sys
import os
#To import from utils
sys.path.append(os.path.join(os.path.dirname(sys.path[0])))

from utils import get_demo_data, get_input_data

lines = get_input_data()

#Part 1:
calories = 0
max_calories = 0
for line in lines:
    try:
        calories += int(line.strip())
    except ValueError:
        if max_calories < calories:
            max_calories = calories        
        calories = 0

print(max_calories)

#Part 2
calories_list = []
calories=0
for line in lines:
    try:
        calories += int(line.strip())
    except ValueError:
        calories_list.append(calories)
        calories = 0

print(sum(sorted(calories_list,reverse=True)[:3]))
