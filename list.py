numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("List:", numbers)
print("Length of list:", len(numbers))
#output
# List: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Length of list: 10
my_list = [10, 3.14, "Python", True, [1, 2, 3]]
for element in my_list:
    print(element, "->", type(element))
#output:
# 10 -> <class 'int'>
# 3.14 -> <class 'float'>
# Python -> <class 'str'>
# True -> <class 'bool'>
# [1, 2, 3] -> <class 'list'>
my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
my_list.append(50)
print("Final list:", my_list)
#output:
# Final list: [10, 20, 30, 40, 50]
fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes", "Papaya", "Pineapple", "Watermelon"]
print("First element:", fruits[0])
print("Last element:", fruits[-1])
print("Element at index 3:", fruits[3])
#output:
# First element: Apple
# Last element: Watermelon
# Element at index 3: Orange
numbers = [10, 20, 30, 40, 50]
for index, value in enumerate(numbers):
    print("Index:", index, "Element:", value)
#output:
# Index: 0 Element: 10
# Index: 1 Element: 20
# Index: 2 Element: 30
# Index: 3 Element: 40
# Index: 4 Element: 50
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("First 3 elements:", numbers[:3])
print("Last 3 elements:", numbers[-3:])
print("Every alternate element:", numbers[::2])
#output:
# First 3 elements: [10, 20, 30]
# Last 3 elements: [80, 90, 100]
# Every alternate element: [10, 30, 50, 70, 90]
numbers = [10, 20, 30, 40, 50]
reverse_list = numbers[::-1]
print("Original list:", numbers)
print("Reversed list:", reverse_list)
#output:
# Original list: [10, 20, 30, 40, 50]
# Reversed list: [50, 40, 30, 20, 10]
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
middle = numbers[4:8]
print("Middle 4 elements:", middle)
#output:
# Middle 4 elements: [50, 60, 70, 80]
numbers = [10, 20, 30, 40, 50, 60, 70]
print("Last element:", numbers[-1])
print("Second-last element:", numbers[-2])
print("Last 3 elements:", numbers[-3:])\
#output:
# Last element: 70
# Second-last element: 60
# Last 3 elements: [50, 60, 70]
numbers = [10, 20, 30, 40, 50]
reverse_list = numbers[::-1]
print("Original list:", numbers)
print("Reverse order:", reverse_list)
#output:
#Original list: [10, 20, 30, 40, 50]
#Reverse order: [50, 40, 30, 20, 10]
numbers = [30, 10, 20, 10, 40]
numbers.append(50)
print("After append():", numbers)
numbers.insert(1, 15)
print("After insert():", numbers)
numbers.extend([60, 70])
print("After extend():", numbers)
numbers.remove(10)
print("After remove():", numbers)
numbers.pop()
print("After pop():", numbers)
numbers.sort()
print("After sort():", numbers)
numbers.reverse()
print("After reverse():", numbers)
print("Count of 10:", numbers.count(10))
print("Index of 30:", numbers.index(30))
#output:
# After append(): [30, 10, 20, 10, 40, 50]
# After insert(): [30, 15, 10, 20, 10, 40, 50]
# After extend(): [30, 15, 10, 20, 10, 40, 50, 60, 70]
# After remove(): [30, 15, 20, 10, 40, 50, 60, 70]
# After pop(): [30, 15, 20, 10, 40, 50, 60]
# After sort(): [10, 15, 20, 30, 40, 50, 60]
# After reverse(): [60, 50, 40, 30, 20, 15, 10]
numbers = [10, 20, 10, 30, 20, 40, 30, 50]
unique = []
for num in numbers:
    if num not in unique:
        unique.append(num)
print("Original list:", numbers)
print("List without duplicates:", unique)
#output:
# Original list: [10, 20, 10, 30, 20, 40, 30, 50]
# List without duplicates: [10, 20, 30, 40, 50]
numbers = [10, 25, 5, 40, 15]
maximum = numbers[0]
minimum = numbers[0]
total = 0
for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num
    total = total + num
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Sum:", total)
#output:
# Maximum: 40
# Minimum: 5
# Sum: 95
list1 = [10, 30, 20]
list2 = [50, 40, 60]
merged = list1 + list2
merged.sort(reverse=True)
print("Merged list in descending order:", merged)
#output:
# Merged list in descending order: [60, 50, 40, 30, 20, 10]
squares = [x * x for x in range(1, 21)]
print("Squares:", squares)
#output:
# Squares: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
even_numbers = [x for x in range(1, 51) if x % 2 == 0]
print("Even numbers:", even_numbers)
#output:
# Even numbers: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
words = ["Apple", "Cat", "Banana", "Dog", "Orange", "Book"]
long_words = [word for word in words if len(word) > 4]
print("Words with more than 4 letters:", long_words)
#output:
# Words with more than 4 letters: ['Apple', 'Banana', 'Orange']
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print("3x3 Matrix:")
for row in matrix:
    print(row)
#output:
# 3x3 Matrix:
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
numbers = [10, -5, 20, -8, 30, -2, 40]
result = [0 if x < 0 else x for x in numbers]
print("Original list:", numbers)
print("Modified list:", result)
#output:
# Original list: [10, -5, 20, -8, 30, -2, 40]
# Modified list: [10, 0, 20, 0, 30, 0, 40]


