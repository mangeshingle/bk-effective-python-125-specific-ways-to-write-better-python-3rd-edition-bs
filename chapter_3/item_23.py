# Item 23 - Pass Iterators to any and all for Efficient Short-Circuiting Logic
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils.tools import separator

print("\n Item 23 - Pass Iterators to any and all for Efficient Short-Circuiting Logic\n")

import random

def flip_coin():
    if random.randint(0, 1) == 0:
        return "Heads"
    else:
        return "Tails"

def flip_is_heads():
    return flip_coin() == "Heads"

def flip_is_tails():
    return flip_coin() == "Tails"

separator(newline_after_separator=True)
print("using list comprehension without short-circuiting......")
print("\n")
flips = [flip_is_heads() for _ in range(20)]
all_heads = False not in flips
print(f"All heads: {all_heads}")
separator(newline_before_separator=True)

separator(newline_after_separator=True)
print("using list comprehension with short-circuiting......")
print("\n")
all_heads = True
for _ in range(20):
    if not flip_is_heads():
        all_heads = False
        break
print(f"All heads: {all_heads}")
separator(newline_before_separator=True)

separator(newline_after_separator=True)
print("using `all` with generator expressions......")
print("\n")
def repeated_is_heads(count):
    for _ in range(count):
        yield flip_is_heads()  # Generator expression
        
all_heads = all(repeated_is_heads(20))
print(f"All heads: {all_heads}")
separator(newline_before_separator=True)

separator(newline_after_separator=True)
print("using `any` with generator expressions......")
print("\n")
def repeated_is_tails(count):
    for _ in range(count):
        yield flip_is_tails()  # Generator expression
        
all_heads = not any(repeated_is_tails(20))
print(f"All heads: {all_heads}")
separator(newline_before_separator=True)


print("""
** Things to Remember **

The all built-in function returns True if all items provided are truthy. It stops processing input and returns False as soon as a falsey item is encountered.

The any built-in function works similarly but with opposite logic: It returns False if all items are falsey and ends early with True as soon as it sees a truthy value.

any and all always return the Boolean values True or False, unlike the or and and logical operators, which return the last item that needed to be tested.

Using list comprehensions with any or all instead of generator expression undermines the efficiency benefits of these functions.
""")
