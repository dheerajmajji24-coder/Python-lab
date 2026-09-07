text = input("Enter a string: ")
char = input("Enter the character to count: ")
count = text.count(char)
print("Occurrences:", count)
#output:
# Occurrences: 2
text = input("Enter a string: ")
result = ""
for char in text:
    if not char.isspace():
        result += char
print("String without whitespace:", result)
#output:
# String without whitespace: HelloWorld
text = input("Enter a string: ")
old = input("Enter the character/word to replace: ")
new = input("Enter the new character/word: ")
result = text.replace(old, new)
print("Updated string:", result)
#output:
# Updated string: Hello, Python!
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
result = "{}{}".format(str1, str2)
print("Concatenated string:", result)
#output:
# Concatenated string: Hello, World!
text = input("Enter a string: ")
result = text.swapcase()
print("After swapping case:", result)
#output:
# After swapping case: hELLO, wORLD!

