def display_message():
    print("This is the function: display_message()")
class Student:
    pass
age = 20
MAX_VALUE = 100
student_id = 101
print("Variable (age):", age)
print("Constant-style name (MAX_VALUE):", MAX_VALUE)
print("Name with underscore (student_id):", student_id)
display_message()
s = Student()
print("Class name: Student")
import keyword


identifiers = ["2value", "value_2", "_hidden", "class", "my-var", "MyClass", "total$"]

for name in identifiers:
    if name.isidentifier() and not keyword.iskeyword(name):
        print(name, "-> Valid Identifier")
    else:
        print(name, "-> Invalid Identifier")
        # Demonstrating Python's case sensitivity

Marks = 95
marks = 80

print("Marks =", Marks)
print("marks =", marks)
