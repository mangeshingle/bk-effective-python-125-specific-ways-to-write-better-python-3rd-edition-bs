# Item 15 - Avoid Striding and Slicing in a Single Expression

print("\n Item 15 - Avoid Striding and Slicing in a Single Expression\n")

print("""
** Things to Remember **

Specifying start, end, and stride together in a single slice can be extremely confusing.

If striding is necessary, try to use only positive stride values without start or end indexes; avoid negative stride values.

If you need start, end, and stride in a single slice, consider doing two assignments (one to stride and another to slice) or using islice from the itertools built-in module.
""")
