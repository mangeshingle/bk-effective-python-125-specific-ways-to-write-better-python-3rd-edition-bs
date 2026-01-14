# Item 24 - Consider itertools for Working with Iterators and Generators
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from utils.tools import separator

print("\n Item 24 - Consider itertools for Working with Iterators and Generators\n")
import itertools
separator(newline_after_separator=True)
print("Linking Iterators Together - `chain`......")
print("\n")
it = itertools.chain([1, 2, 3], [4, 5, 6])
print("chain: ", list(it))

it1 = [i * 3 for i in ("a", "b", "c")]
it2 = [j * 2 for j in ("x", "y", "z")]
nested_it = [it1, it2]
output_it = itertools.chain.from_iterable(nested_it)
print("chain: ",list(output_it))
separator(newline_before_separator=True)

separator(newline_after_separator=True)
print("Linking Iterators Together - `repeat`......")
print("\n")
it = itertools.repeat("hello", 3)
print("repeat: ",list(it))
separator(newline_before_separator=True)

separator(newline_after_separator=True)
print("Linking Iterators Together - `cycle`......")
print("\n")
it = itertools.cycle([1, 2])
result = [next(it) for _ in range(10)]
print("cycle: ",result)
separator(newline_before_separator=True)

separator(newline_after_separator=True)
print("Linking Iterators Together - `tee`......")
print("\n")
it1, it2, it3 = itertools.tee(["first", "second"], 3)
print("tee 1: ",list(it1))
print("tee 2: ",list(it2))
print("tee 3: ",list(it3))
separator(newline_before_separator=True)

separator(newline_after_separator=True)
print("Linking Iterators Together - `zip_longest`......")
print("\n")
keys = ["one", "two", "three"]
values = [1, 2]
normal = list(zip(keys, values))
print("zip:        ", normal)
it = itertools.zip_longest(keys, values, fillvalue="filler-value")
longest = list(it)
print("zip_longest:", longest)
separator(newline_before_separator=True)

separator(newline_after_separator=True)
print("Filtering Items from an Iterator - `islice`......")
print("\n")
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_five = itertools.islice(values, 5)
print("islice - First five: ", list(first_five))
middle_odds = itertools.islice(values, 2, 8, 2)
print("islice - Middle odds:", list(middle_odds))
separator(newline_before_separator=True)

separator(newline_after_separator=True)
print("Filtering Items from an Iterator - `takewhile`......")
print("\n")
values = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
values1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
less_than_seven = lambda x: x < 7
it = itertools.takewhile(less_than_seven, values)
it1 = itertools.takewhile(less_than_seven, values1)
print("takewhile: ", list(it))
print("takewhile: ", list(it1))
separator(newline_before_separator=True)

separator(newline_after_separator=True)
print("Filtering Items from an Iterator - `dropwhile`......")
print("\n")
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
values1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
less_than_seven = lambda x: x < 7
it = itertools.dropwhile(less_than_seven, values)
it1 = itertools.dropwhile(less_than_seven, values1)
print("dropwhile: ", list(it))
print("dropwhile: ", list(it1))
separator(newline_after_separator=True)

separator(newline_before_separator=True)
print("Filtering Items from an Iterator - `filterfalse`......")
print("\n")
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = lambda x: x % 2 == 0
filter_result = filter(evens, values)
print("filter:      ", list(filter_result))
filter_false_result = itertools.filterfalse(evens, values)
print("filterfalse: ", list(filter_false_result))
separator(newline_before_separator=True)

separator(newline_after_separator=True)
print("Producing Combinations of Items from Iterators - `batched`......")
print("\n")
it = itertools.batched([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
print("batched: ", list(it))
it = itertools.batched([1, 2, 3], 2)
print("batched: ", list(it))
separator(newline_before_separator=True)

separator(newline_after_separator=True)
print("Producing Combinations of Items from Iterators - `pairwise`......")
print("\n")
route = ["Los Angeles", "Bakersfield", "Modesto", "Sacramento"]
it = itertools.pairwise(route)
print("pairwise: ", list(it))
separator(newline_before_separator=True)

separator(newline_after_separator=True)
print("Producing Combinations of Items from Iterators - `accumulate`......")
print("\n")
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def sum_modulo_20(first, second):
    output = first + second
    return output % 20
sum_reduce = itertools.accumulate(values)
print("accumulate - Sum:   ", list(sum_reduce))
modulo_reduce = itertools.accumulate(values, sum_modulo_20)
print("accumulate - Modulo:", list(modulo_reduce))
separator(newline_before_separator=True)

separator(newline_after_separator=True)
print("Producing Combinations of Items from Iterators - `product`......")
print("\n")
single = itertools.product([1, 2], repeat=2)
multiple = itertools.product([1, 2], ["a", "b"])
print("product - Single:  ", list(single))
print("product - Multiple:", list(multiple))
separator(newline_before_separator=True)

separator(newline_after_separator=True)
print("Producing Combinations of Items from Iterators - `permutations`......")
print("\n")
it = itertools.permutations([1, 2, 3, 4], 2)
print("permutations: ", list(it))
separator(newline_before_separator=True)

separator(newline_after_separator=True)
print("Producing Combinations of Items from Iterators - `combinations`......")
print("\n")
it = itertools.combinations([1, 2, 3, 4], 2)
print("combinations: ", list(it))
separator(newline_before_separator=True)

separator(newline_after_separator=True)
print("Producing Combinations of Items from Iterators - `combinations_with_replacement`......")
print("\n")
it = itertools.combinations_with_replacement([1, 2, 3, 4], 2)
print("combinations_with_replacement: ", list(it))
separator(newline_before_separator=True)

print("""
** Things to Remember **

The itertools functions fall into three main categories for working with iterators and generators: linking iterators together, filtering items they output, and producing combinations of items.

There are more advanced functions, additional parameters, and useful recipes available in the official documentation.
""")
