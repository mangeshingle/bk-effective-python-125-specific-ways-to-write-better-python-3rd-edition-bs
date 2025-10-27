# Item 8 - Prevent Repetition with Assignment Expressions(:=)
print("\n Item 8 - Prevent Repetition with Assignment Expressions \n")
fresh_fruit = {
    "apple": 10,
    "banana": 8,
    "lemon": 5,
}


def slice_bananas(x):
    print(f"Slicing {x} bananas")
    return x * 4


def make_smoothies(x):
    return f"Making smoothies with {x} banana slices"


def make_cider(x):
    return f"Making cider with {x} apples"


def make_lemonade(x):
    return f"Making {x} lemons into lemonade"


# Don't
print("DON'T : ")
count = fresh_fruit.get("banana", 0)
if count >= 2:
    pieces = slice_bananas(count)
    to_enjoy = make_smoothies(pieces)
else:
    count = fresh_fruit.get("apple", 0)
    if count >= 4:
        to_enjoy = make_cider(count)
    else:
        count = fresh_fruit.get("lemon", 0)
        if count:
            to_enjoy = make_lemonade(count)
        else:
            to_enjoy = "Nothing"
print(to_enjoy)
print("=" * 30)

# Do
print("DO : ")
if (count := fresh_fruit.get("banana", 0)) >= 2:
    pieces = slice_bananas(count)
    to_enjoy = make_smoothies(pieces)
elif (count := fresh_fruit.get("apple", 0)) >= 4:
    to_enjoy = make_cider(count)
elif count := fresh_fruit.get("lemon", 0):
    to_enjoy = make_lemonade(count)
else:
    to_enjoy = "Nothing"
print(to_enjoy)
print("=" * 30)
