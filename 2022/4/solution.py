import os
import string
import sys

# To import from utils
sys.path.append(os.path.join(os.path.dirname(sys.path[0])))

from utils import get_demo_data, get_input_data

lines = get_input_data()

fully_contained_count = 0
for idx,line in enumerate(lines):
    first_elf_section, second_elf_section = [set(range(int(section.split("-")[0]),int(section.split("-")[-1]) + 1)) for section in line.split(",")]
    if first_elf_section.issubset(second_elf_section) or first_elf_section.issuperset(second_elf_section):
        fully_contained_count += 1
print(fully_contained_count)

overlap_count = 0
for idx,line in enumerate(lines):
    first_elf_section, second_elf_section = [set(range(int(section.split("-")[0]),int(section.split("-")[-1]) + 1)) for section in line.split(",")]
    if first_elf_section.intersection(second_elf_section):
        overlap_count += 1
print(overlap_count)
