# Item 13 - Prefer Explicit String Concatenation over Implicit, Especially in Lists
print("\n Item 13 - Prefer Explicit String Concatenation over Implicit, Especially in Lists \n")

print("""
** Things to Remember **
When two string literals are next to each other in Python code, they will be merged as if the + operator were present between them, in a similar fashion to the implicit string concatenation feature of the C programming language.

Avoid implicit string concatenation of items in list and tuple literals because it creates ambiguity about the original author’s intent. Instead, you should use explicit concatenation with the + operator.

In function calls, it is fine to use implicit string concatenation with one positional argument and any number of keyword arguments, but you should use explicit concatenation when there are multiple positional arguments.
""")


