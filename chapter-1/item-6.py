# Item 6 - Always Surround Single-Element Tuples with Parentheses
print("\n Item 6 - Always Surround Single-Element Tuples with Parentheses \n")

value_a = (1,)  # No parentheses, right
list_b = [
    1,
]  # No parentheses, wrong
list_c = [(1,)]  # Parentheses, right
print("A:", value_a)
print("B:", list_b)
print("C:", list_c)
