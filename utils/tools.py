def separator(symbol="=", length=50, newline_after_separator=False, newline_before_separator=False):
    if newline_after_separator:        
        print(symbol * length)
        print("\n")
    elif newline_before_separator:
        print("\n")
        print(symbol * length)
    else:
        print(symbol * length)
