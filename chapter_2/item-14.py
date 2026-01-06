# Item 14 - Know How to Slice Sequences
print("\n Item 14 - Know How to Slice Sequences \n")

print("""
** Things to Remember **

Avoid being verbose when slicing: Don’t supply 0 for the start index or the length of the sequence for the end index.

Slicing is forgiving of start or end indexes that are out of bounds, which means it’s easy to express slices on the front or back boundaries of a sequence (e.g., a[:20] or a[-20:]).

Assigning to a list slice replaces that range in the original sequence with what’s referenced even when the lengths are different.
""")
