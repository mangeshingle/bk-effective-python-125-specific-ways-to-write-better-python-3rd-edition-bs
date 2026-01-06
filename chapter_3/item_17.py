# Item 17 - Prefer enumerate over range
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils.tools import separator

print("\n Item 17 - Prefer enumerate over range\n")

separator(newline_after_separator=True)
from random import randint
random_bits = 0
for i in range(32):
    if randint(0, 1):
        random_bits |= 1 << i        
print(bin(random_bits))
separator(newline_before_separator=True)

separator(newline_after_separator=True)
flavours = ['vanilla', 'chocolate', 'strawberry', 'mint', 'cookie dough']
it = enumerate(flavours)
print(next(it))
print(next(it))
print("\n")
print("using range......")
for i in range(len(flavours)):
    print(f"{i + 1}: {flavours[i]}")

separator(newline_before_separator=True)

separator(newline_after_separator=True)
print("using enumerator......")
for index, flavour in enumerate(flavours, 1):
    print(f"{index}: {flavour}")
separator(newline_before_separator=True)

print("""
** Things to Remember **

enumerate provides concise syntax for looping over an iterator and getting the index of each item from the iterator as you go.

Prefer enumerate instead of looping over a range and indexing into a sequence.

You can supply a second, optional parameter to enumerate that specifies the beginning number for counting (zero is the default).
""")
