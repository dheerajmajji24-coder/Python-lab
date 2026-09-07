text = input("Enter a string: ")
print("First character:", text[0])
print("Last character:", text[-1])
#output:
# First character: H
text = input("Enter a string: ")
print("Every second character:", text[::2])
#output:
# Every second character: Hlo ol!
text = input("Enter a string: ")
substring = input("Enter substring: ")
if substring in text:
    print("Substring exists")
else:
    print("Substring does not exist")
#output:
# Substring exists
text = input("Enter a string: ")
char = input("Enter a character: ")
first = text.find(char)
last = text.rfind(char)
if first != -1:
    print("First occurrence index:", first)
    print("Last occurrence index:", last)
else:
    print("Character not found")
#output:
# First occurrence index: 2
# Last occurrence index: 5
