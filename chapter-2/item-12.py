# Item 12 - Understand the Difference Between repr and str when Printing Objects
print("\n Item 12 - Understand the Difference Between repr and str when Printing Objects \n")

print("""
** Things to Remember **
Calling print on built-in Python types produces the human-readable string version of a value, which hides type information.

Calling repr on built-in Python types produces a string that contains the printable representation of a value. repr strings can often be passed to the eval built-in function to get back the original value.

%s in format strings produces human-readable strings like str. %r produces printable strings like repr. F-strings produce human-readable strings for replacement text expressions unless you specify the !r conversion suffix.

You can define the __repr__ and __str__ special methods on your classes to customize the printable and human-readable representations of instances, which can help with debugging and can simplify integrating objects into human interfaces.
      
""")