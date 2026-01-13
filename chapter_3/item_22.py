# Item 22 - Never Modify Containers While Iterating over Them; Use Copies or Caches Instead
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils.tools import separator

print("\n Item 22 - Never Modify Containers While Iterating over Them; Use Copies or Caches Instead\n")


separator(newline_after_separator=True)
print("dictionary changed size during iteration error......")
print("\n")
search_key = "red"
my_dict = {"red": 1, "blue": 2, "green": 3}
try:
    for key in my_dict:
        if key == "blue":
            my_dict["yellow"] = 4  # Causes error
except RuntimeError as e:
    print(f"RuntimeError: {e}")
separator(newline_before_separator=True)

separator(newline_after_separator=True)
print("dictionary changed size during iteration error remedy - copy......")
print("\n")
my_dict = {"red": 1, "blue": 2, "green": 3}
keys_copy = list(my_dict.keys())  # Copy
for key in keys_copy:             # Iterate over copy
    if key == "blue":
        my_dict["green"] = 4      # Modify original dict

print(my_dict)
separator(newline_before_separator=True)

separator(newline_after_separator=True)
print("dictionary changed size during iteration error remedy - caching......")
print("\n")
my_dict = {"red": 1, "blue": 2, "green": 3}
modifications = {}

for key in my_dict:
    if key == "blue":
        modifications["green"] = 4
    value = my_dict[key]
    other_value = modifications.get(key)  # Check cache
    if value == 4 or other_value == 4:
        modifications["yellow"] = 5

my_dict.update(modifications)             # Merge modifications
print(my_dict)
separator(newline_before_separator=True)

print("""
** Things to Remember **

 Adding or removing elements from lists, dictionaries, and sets while you’re iterating over them can cause runtime errors that are often hard to predict.

 You can iterate over a copy of a container to avoid runtime errors that might be caused by mutation during iteration.

 If you need to avoid copying for better performance, you can stage modifications in a second container cache that you later merge into the original.
""")
