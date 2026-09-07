numbers = {10, 20, 30, 20, 40, 50, 30, 60}
print("Set:", numbers)
#output:
# Set: {40, 10, 50, 20, 60, 30}
numbers = [1, 2, 3, 2, 4, 3, 5]
text = "hello"
set_from_list = set(numbers)
set_from_string = set(text)
print("Set from list:", set_from_list)
print("Set from string:", set_from_string)
#output:
# Set from list: {1, 2, 3, 4, 5}
# Set from string: {'h', 'e', 'l', 'o'}
numbers = {10, 20, 30}
numbers.add(40)
numbers.update([50, 60, 70])
print("Updated set:", numbers)
#output:
# Updated set: {70, 40, 10, 50, 20, 60, 30}
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))
print("Symmetric Difference:", set1.symmetric_difference(set2))
#output:
# Union: {1, 2, 3, 4, 5, 6, 7, 8}
# Intersection: {4, 5}
# Difference: {1, 2, 3}
# Symmetric Difference: {1, 2, 3, 6, 7, 8}
set1 = {1, 2, 3, 4, 5}
set2 = {2, 3, 4}
print("Is set2 a subset of set1?", set2.issubset(set1))
print("Is set1 a superset of set2?", set1.issuperset(set2))
#output:
# Is set2 a subset of set1? True
# Is set1 a superset of set2? True
numbers = {10, 20, 30, 40}
numbers.remove(20)
print("After remove():", numbers)
numbers.discard(50)
print("After discard():", numbers)
#output:
# After remove(): {40, 10, 30}
# After discard(): {40, 10, 30}
set1 = {1, 2, 3}
set2 = {4, 5, 6}
if set1.isdisjoint(set2):
    print("The sets are disjoint")
else:
    print("The sets are not disjoint")
#output:
# The sets are disjoint
numbers = [5, 2, 8, 2, 1, 5, 9, 8, 3]
unique = set(numbers)
sorted_list = sorted(unique)
print("Unique elements:", unique)
print("Sorted list:", sorted_list)
#output:
# Unique elements: {1, 2, 3, 5, 8, 9}
# Sorted list: [1, 2, 3, 5, 8, 9]
squares = {num ** 2 for num in range(1, 21) if num % 2 != 0}
print("Squares of odd numbers:", squares)
#output:
# Squares of odd numbers: {1, 9, 25, 49, 81, 121, 169, 225, 289, 361}

