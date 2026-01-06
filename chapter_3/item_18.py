# Item 18 - Use zip to Process Iterators in Parallel
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils.tools import separator

print("\n Item 18 - Use zip to Process Iterators in Parallel\n")

names = ["Cecilia", "Lise", "Marie"]
counts = [len(n) for n in names]

separator(newline_after_separator=True)
print("Find the max length name without zip......")
print("\n")
longest_name = None
max_count = 0
for i, name in enumerate(names):
    count = counts[i]
    if count > max_count:
        longest_name = name
        max_count = count
print(f"The longest name is {longest_name} with {max_count} letters")
separator(newline_before_separator=True)

separator(newline_after_separator=True)
print("Find the max length name with zip......")
print("\n")
longest_name = None
max_count = 0

for name, count in zip(names, counts):
    if count > max_count:
        longest_name = name
        max_count = count
print(f"The longest name is {longest_name} with {max_count} letters")
separator(newline_before_separator=True)

separator(newline_after_separator=True)
print("zip with strict option......")
print("\n")
names.append("Rosalind")
for name, count in zip(names, counts, strict=True):
    print(name)
separator(newline_before_separator=True)


print("""
** Things to Remember **

The zip built-in function can be used to iterate over multiple iterators in parallel.

zip creates a lazy generator that produces tuples; it can be used on infinitely long inputs.

zip truncates its output silently to the shortest iterator if you supply it with iterators of different lengths.

Pass the strict keyword argument to zip if you want to ensure that silent truncation is not possible and mismatched iterator lengths should result in a runtime error.
""")
