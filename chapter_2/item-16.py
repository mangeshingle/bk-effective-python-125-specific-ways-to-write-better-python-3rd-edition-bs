# Item 16 - Prefer Catch-All Unpacking over Slicing
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils.tools import separator

print("\n Item 16 - Prefer Catch-All Unpacking over Slicing\n")

separator(newline_after_separator=True)
car_ages = [0, 9, 4, 8, 7, 20, 19, 1, 6, 15]

car_ages_descending = sorted(car_ages, reverse=True)
try:
    oldeset, second_oldest = car_ages_descending
except Exception as e:
    print("Error - ",e)
separator(newline_before_separator=True)

separator(newline_after_separator=True)
oldest = car_ages_descending[0]
second_oldest = car_ages_descending[1]
others = car_ages_descending[2:]
print(f"Oldest: {oldest}, Second Oldest: {second_oldest}, Others: {others}")
separator(newline_before_separator=True)

separator(newline_after_separator=True)
oldest, second_oldest, *others = car_ages_descending
print(f"Oldest: {oldest}, Second Oldest: {second_oldest}, Others: {others}")
separator(newline_before_separator=True)

separator(newline_after_separator=True)
first, *middle, last = car_ages_descending
print(f"First: {first}, Middle: {middle}, Last: {last}")
separator(newline_before_separator=True) 

separator(newline_after_separator=True)
short_list = [1, 2]
first, second, *others = short_list
print(f"First: {first}, Second: {second}, Others: {others}")
separator(newline_before_separator=True)

print("""
** Things to Remember **

Unpacking assignments may include a starred expression to store all values that weren’t assigned to the other parts of the unpacking pattern in a list.

Starred expressions may appear in any position of the unpacking pattern. They will always become a list instance containing zero or more values.

When dividing a list into non-overlapping pieces, catch-all unpacking is much less error prone than using separate statements that do slicing and indexing.
""")