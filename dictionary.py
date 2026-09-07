students = {
    101: "Ravi",
    102: "Sita",
    103: "Kiran",
    104: "Anu",
    105: "Rahul"
}
print("Student Dictionary:", students)
#output:
# Student Dictionary: {101: 'Ravi', 102: 'Sita', 103: 'Kiran', 104: 'Anu', 105: 'Rahul'}
student = {
    101: "Ravi",
    102: "Sita"
}
student[103] = "Kiran"
student[104] = "Anu"
student[105] = "Rahul"
print("Updated Dictionary:", student)
#output:
# Updated Dictionary: {101: 'Ravi', 102: 'Sita', 103: 'Kiran', 104: 'Anu', 105: 'Rahul'}
student = {
    101: "Ravi",
    102: "Sita",
    103: "Kiran"
}
print("Before Update:", student)
student[102] = "Priya"
print("After Update:", student)
#output:
# Before Update: {101: 'Ravi', 102: 'Sita', 103: 'Kiran'}
# After Update: {101: 'Ravi', 102: 'Priya', 103: 'Kiran'}
keys = ["name", "age", "city", "course"]
values = ["Ravi", 20, "Hyderabad", "BTech"]
student = dict(zip(keys, values))
print("Dictionary:", student)
#output:
# Dictionary: {'name': 'Ravi', 'age': 20, 'city': 'Hyderabad', 'course': 'BTech'}
employees = {
    101: {
        "name": "Ravi",
        "department": "IT",
        "salary": 40000
    },
    102: {
        "name": "Sita",
        "department": "HR",
        "salary": 35000
    },
    103: {
        "name": "Kiran",
        "department": "Finance",
        "salary": 45000
    }
}
print("Employee Details:")
for emp_id, details in employees.items():
    print(emp_id, details)
#output:
# Employee Details:
# 101 {'name': 'Ravi', 'department': 'IT', 'salary': 40000}
# 102 {'name': 'Sita', 'department': 'HR', 'salary': 35000}
# 103 {'name': 'Kiran', 'department': 'Finance', 'salary': 45000}
student = {
    101: "Ravi",
    102: "Sita",
    103: "Kiran"
}
print("Keys:")
for key in student.keys():
    print(key)
print("Values:")
for value in student.values():
    print(value)
print("Key-Value Pairs:")
for key, value in student.items():
    print(key, value)
#output:
# Keys: 101
# Keys: 102
# Keys: 103
# Values: Ravi
# Values: Sita
# Values: Kiran
# Key-Value Pairs:
# 101 Ravi
# 102 Sita
# 103 Kiran
student = {
    101: "Ravi",
    102: "Sita",
    103: "Kiran"
}
removed = student.pop(102)
print("Removed:", removed)
print("Dictionary:", student)
key = 105
value = student.get(key, "Key does not exist")
print("Result:", value)
#output:
# Removed: Sita
# Dictionary: {101: 'Ravi', 103: 'Kiran'}
# Result: Key does not exist
student = {
    101: "Ravi",
    102: "Sita",
    103: "Kiran"
}
key = 102
if key in student:
    print("Key exists")
    print("Value:", student[key])
else:
    print("Key does not exist")
#output:
# Key exists
# Value: Sita
dict1 = {"a": 10, "b": 20}
dict2 = {"c": 30, "d": 40}
dict1.update(dict2)
print("Using update():", dict1)
#output:
# Using update(): {'a': 10, 'b': 20, 'c': 30, 'd': 40}
items = {
    "Laptop": 50000,
    "Mobile": 25000,
    "Headphones": 3000,
    "Tablet": 20000
}
highest = max(items, key=items.get)
lowest = min(items, key=items.get)
print("Highest priced item:", highest, items[highest])
print("Lowest priced item:", lowest, items[lowest])
#output:
# Highest priced item: Laptop 
50000
# Lowest priced item: Headphones 3000
text = "hello"
frequency = {}
for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print("Character Frequency:", frequency)
#output:
# Character Frequency: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
cubes = {num: num**3 for num in range(1, 11)}
print("Cubes:", cubes)
#output:
# Cubes: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512, 9: 729, 10: 1000}