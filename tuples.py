countries = ("India", "USA", "Japan", "Australia", "Canada", "Germany")
print("Tuple:", countries)
print("Type:", type(countries))
print("Length:", len(countries))
#output:
# Tuple: ('India', 'USA', 'Japan', 'Australia', 'Canada', '
#,Germany')
my_tuple = (10,)
print("Tuple:", my_tuple)
print("Type:", type(my_tuple))
#output:
# Tuple: (10,)
# Type: <class 'tuple'>
# List to tuple
my_list = [10, 20, 30, 40, 50]
my_tuple = tuple(my_list)
print("List:", my_list)
print("Tuple:", my_tuple)
new_list = list(my_tuple)
print("Tuple:", my_tuple)
print("List:", new_list)
#output:
# List: [10, 20, 30, 40, 50]
# Tuple: (10, 20, 30, 40, 50)
# Tuple: (10, 20, 30, 40, 50)
# List: [10, 20, 30, 40, 50]
numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print("Element at index 0:", numbers[0])
print("Element at index 5:", numbers[5])
print("Last element:", numbers[-1])
#output:
# Element at index 0: 10
# Element at index 5: 60
# Last element: 100
numbers = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120)
first_half = numbers[:6]
second_half = numbers[6:]
print("First half:", first_half)
print("Second half:", second_half)
#output:
# First half: (10, 20, 30, 40, 50, 60)
# Second half: (70, 80, 90, 100, 110, 120)
numbers = (10, 20, 30, 40, 50)
value = 30
if value in numbers:
    print(value, "exists in the tuple")
else:
    print(value, "does not exist in the tuple")
#output:
# 30 exists in the tuple
numbers = (10, 20, 30, 20, 40, 50, 20, 60)
maximum = max(numbers)
minimum = min(numbers)
value = 20
count = numbers.count(value)
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Count of", value, ":", count)
#output:
# Maximum: 60
# Minimum: 10
# Count of 20: 3
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
# Concatenate two tuples
result = tuple1 + tuple2
print("Concatenated tuple:", result)
# Repeat tuple 3 times
repeated = tuple1 * 3
print("Repeated tuple:", repeated)
#output:
# Concatenated tuple: (1, 2, 3, 4, 5, 6)
# Repeated tuple: (1, 2, 3, 1, 2, 3, 1, 2, 3)
marks = (80, 75, 90, 85, 70)
m1, m2, m3, m4, m5 = marks
average = (m1 + m2 + m3 + m4 + m5) / 5
print("Marks:", m1, m2, m3, m4, m5)
print("Average:", average)
#output:
# Marks: 80 75 90 85 70
# Average: 78.0
numbers = (10, 20, 30, 40)
try:
    numbers[1] = 50
except TypeError as e:
    print("Error:", e)
#output:
# Error: 'tuple' object does not support item assignment
data = (10, 20, [30, 40, 50])
data[2].append(60)
print("Tuple:", data)
#output:
# Tuple: (10, 20, [30, 40, 50, 60])
numbers = (50, 20, 40, 10, 30)
sorted_numbers = sorted(numbers)
print("Original tuple:", numbers)
print("Sorted list:", sorted_numbers)
#output:
# Original tuple: (50, 20, 40, 10, 30)
# Sorted list: [10, 20, 30, 40, 50]
