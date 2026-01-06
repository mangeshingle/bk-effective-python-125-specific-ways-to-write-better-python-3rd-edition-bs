# Item 19 - Avoid else Blocks After for and while Loops
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils.tools import separator

print("\n Item 19 - Avoid else Blocks After for and while Loops\n")

names = ["Cecilia", "Lise", "Marie"]
counts = [len(n) for n in names]

separator(newline_after_separator=True)
print("else after loop(not recommended)......")
print("\n")
a = 4
b = 9
for i in range(2, min(a, b) + 1):
    print("Testing", i)
    if a % i == 0 and b % i == 0:
        print("Not coprime")
        break
else:
    print("Coprime")
separator(newline_before_separator=True)

separator(newline_after_separator=True)
print("avoiding else after loop......")
def coprime_alternate(a, b):
    is_coprime = True
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            is_coprime = False
            break
    return is_coprime

print("for 4,9: Coprime" if coprime_alternate(4, 9) else "for 4,9: Not Coprime")
print("for 3,6: Coprime" if coprime_alternate(3, 6) else "for 3,6: Not Coprime")
separator(newline_before_separator=True)



print("""
** Things to Remember **

Python has special syntax that allows else blocks to immediately follow for and while loop interior blocks.

The else block after a loop runs only if the loop body did not encounter a break statement.

Avoid using else blocks after loops because their behavior isn’t intuitive and can be confusing.
""")
