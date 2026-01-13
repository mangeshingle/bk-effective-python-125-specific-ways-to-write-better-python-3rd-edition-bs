# Item 21 - Be Defensive when Iterating over Arguments
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils.tools import separator

print("\n Item 21 - Be Defensive when Iterating over Arguments\n")

def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

def read_visits(data_path):
    p = Path(data_path)
    if not p.is_absolute():
        p = (Path(__file__).resolve().parent / p).resolve(strict=False)
    with p.open() as f:
        for line in f:
            yield int(line)

separator(newline_after_separator=True)
print("iterator or generator that has already raised StopIteration......")
print("\n")
it = read_visits("../resources/data/texas_tourist_numbers.txt")
print(list(it))
print(list(it))  # Already exhausted
separator(newline_before_separator=True)

separator(newline_after_separator=True)
print("iterating over iterator object using container type......")
print("\n")

class ReadVisits:
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        p = Path(self.data_path)
        if not p.is_absolute():
            p = (Path(__file__).resolve().parent / p).resolve(strict=False)
        with p.open() as f:
            for line in f:
                yield int(line)

visits = ReadVisits("../resources/data/texas_tourist_numbers.txt")
percentages = normalize(visits)  # Changed
print(percentages)
assert sum(percentages) == 100.0
separator(newline_before_separator=True)

separator(newline_after_separator=True)
print("iterating over iterator object using container type with defensive normalize......")
print("\n")
from collections.abc import Iterator

def normalize_defensive(numbers):
    if isinstance(numbers, Iterator):  # Another way to check
        raise TypeError("Must supply a container")
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result

class ReadVisits:
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        p = Path(self.data_path)
        if not p.is_absolute():
            p = (Path(__file__).resolve().parent / p).resolve(strict=False)
        with p.open() as f:
            for line in f:
                yield int(line)

input_visits = [15, 35, 80]
file_visits = ReadVisits("../resources/data/texas_tourist_numbers.txt")
ip_percentages = normalize_defensive(input_visits)
file_percentages = normalize_defensive(file_visits)
print(ip_percentages)
print(file_percentages)
assert sum(ip_percentages) == 100.0
assert sum(file_percentages) == 100.0

visits = [15, 35, 80]
it = iter(visits)
normalize_defensive(it)

separator(newline_before_separator=True)

print("""
** Things to Remember **

 Beware of functions and methods that iterate over input arguments multiple times. If these arguments are iterators, you might see strange behavior and missing values.

 Python’s iterator protocol defines how containers and iterators interact with the iter and next built-in functions, for loops, and related expressions.

 You can easily define your own iterable container type by implementing the __iter__ method as a generator.

 You can detect that a value is an iterator (instead of a container) if calling iter on it produces the same value that you passed in. Alternatively, you can use the isinstance built-in function along with the collections.abc.Iterator class.
""")
