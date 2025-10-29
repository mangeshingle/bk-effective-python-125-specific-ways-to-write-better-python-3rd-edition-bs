# Item 11 - Prefer Interpolated F-Strings over C-Style Format Strings and str.format
print("\n Item 11 - Prefer Interpolated F-Strings over C-Style Format Strings and str.format \n")

print("""
** Things to Remember **
C-style format strings that use the % operator suffer from a variety of gotchas and verbosity problems.

The str.format method introduces some useful concepts in its formatting specifiers mini-language, but it otherwise repeats the mistakes of C-style format strings and should be avoided.

F-strings are a new syntax for formatting values into strings that solves the biggest problems with C-style format strings.

F-strings are succinct yet powerful because they allow for arbitrary Python expressions to be directly embedded within format specifiers.
      
""")