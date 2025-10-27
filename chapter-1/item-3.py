# Item 3: Never Expect Python to Detect Errors at Compile Time
print("\n Iteam 3: Never Expect Python to Detect Errors at Compile Time \n")


def bad_function(x):
    if x:
        var = 10
        print(var)

    print(var)


print(bad_function(True))
print(bad_function(False))
