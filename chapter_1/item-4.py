# Item 4: Write Helper Functions Instead of Complex Expressions
from urllib.parse import parse_qs

print("\n Item 4: Write Helper Functions Instead of Complex Expressions \n")

my_values = parse_qs("red=5&blue=0&green=", keep_blank_values=True)

# Don't - 1
# For query string 'red=5&blue=0&green='
red = my_values.get("red", [""])[0] or 0
green = my_values.get("green", [""])[0] or 0
opacity = my_values.get("opacity", [""])[0] or 0
print(f"Red:     {red!r}")
print(f"Green:   {green!r}")
print(f"Opacity: {opacity!r}")
print("=" * 30)

# Don't - 2
green_str = my_values.get("green", [""])
if green_str[0]:
    green = int(green_str[0])
else:
    green = 0
print(f"Green:   {green!r}")
print("=" * 30)


# Do - DRY principle: Don’t repeat yourself
def get_first_int(values, key, default=0):
    found = values.get(key, [""])
    if found[0]:
        return int(found[0])
    return default


green = get_first_int(my_values, "green")
print(f"Green:   {green!r}")
print("=" * 30)
