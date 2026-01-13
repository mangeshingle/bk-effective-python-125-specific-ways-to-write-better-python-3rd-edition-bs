# Item 20 - Never Use for Loop Variables After the Loop Ends
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils.tools import separator

print("\n Item 20 - Never Use for Loop Variables After the Loop Ends\n")

names = ["Cecilia", "Lise", "Marie"]
counts = [len(n) for n in names]

separator(newline_after_separator=True)
print("for loop variable outside for loop......")
print("\n")
for i in range(3):
    print(f"Inside {i=}")
print(f"After  {i=}")
separator(newline_before_separator=True)

separator(newline_after_separator=True)
print("for loop variable with break......")
print("\n")
categories = ["Hydrogen", "Uranium", "Iron", "Other"]
for i, name in enumerate(categories):
    if name == "Iron":
        break
print(i)
separator(newline_before_separator=True)


print("""
** Things to Remember **

The loop variable from for loops can be accessed in the current scope even after the loop terminates.

for loop variables will not be assigned in the current scope if the loop never did a single iteration.

Generator expressions and list comprehensions do not leak loop variables by default.

Exception handlers do not leak exception instance variables.
""")
