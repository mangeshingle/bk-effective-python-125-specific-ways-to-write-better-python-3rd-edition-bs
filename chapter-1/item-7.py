# Item 7 - Consider Conditional Expressions for Simple Inline Logic
print("\n Item 7 - Consider Conditional Expressions for Simple Inline Logic \n")

# Don't
print("DON'T : ")
i = 30
x = (i % 2 == 0 and "even") or "odd"
print(x)
print("=" * 30)


# Don't
print("DON'T : ")
x = 20
y = 10
z = 30
w = 40
if x > y if z else w:  # Ambiguous
    print("Ambiguous")
print("=" * 30)


# Do
print("DO : ")
if x > (y if z else w):  # Clear
    print("Clear")
print("=" * 30)
