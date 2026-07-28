
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}, you will turn {age + 1} next year.")


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Sum =", num1 + num2)
print("Difference =", num1 - num2)
print("Product =", num1 * num2)
print("Quotient =", num1 / num2)


name = "John"
marks = 95
print("Name:", name, "marks:",marks)
print("Name: {} Marks: {}".format(name, marks))
print(f"Name: {name} Marks: {marks}")

numbers = input("Enter numbers separated by spaces: ").split()
numbers = list(map(int, numbers))
print("Sum =", sum(numbers))
