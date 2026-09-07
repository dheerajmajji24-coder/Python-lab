text = input("Enter a string: ")
print("Length of the string:", len(text))
#output:
# Length of the string: 11
text = input("Enter a string: ")
reverse = ""
for char in text:
    reverse = char + reverse
print("Reversed string:", reverse)
#output:
# Reversed string: olleh
text = input("Enter a string: ")
if text == text[::-1]:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
#output:
# The string is a palindrome
text = input("Enter a string: ")
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
#output:
# Uppercase: HELLO
# Lowercase: hello
text = input("Enter a string: ")
vowels = 0
consonants = 0
digits = 0
spaces = 0
for char in text:
    if char.lower() in "aeiou":
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        spaces += 1
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
#output:
# Vowels: 2
# Consonants: 3
# Digits: 0
# Spaces: 0
