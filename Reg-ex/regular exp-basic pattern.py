#week-6
#task-1
#1
import re
sentence = "1024 requests were served in 3 seconds"
# Test whether the sentence starts with a digit
result = re.match(r'\d', sentence)
if result:
    print("The sentence starts with a digit.")
else:
    print("The sentence does not start with a digit.")
#output
#The sentence starts with a digit.


#2
import re
sentence = "1024 requests were served in 3 seconds"
#Search for "served" anywhere in the sentence
result = re.search(r"served", sentence)
if result:
    print("Found:", result.group())
    print("Start/End position:", result.span())
else:
    print("Word not found.")

#output
#Found: served
#Start/End position: (19, 25)


#3
import re
# Test "12345"
string1 = "12345"
result1 = re.fullmatch(r"\d+", string1)
if result1:
    print(string1, "contains only digits.")
else:
    print(string1, "does not contain only digits.")
# Test "123a5"
string2 = "123a5"
result2 = re.fullmatch(r"\d+", string2)
if result2:
    print(string2, "contains only digits.")
else:
    print(string2, "does not contain only digits.")

#output
#12345 contains only digits.
#123a5 does not contain only digits.



#4
# match() checks only the beginning of the string, while fullmatch() requires the entire string to match the pattern.
# Therefore, a string that starts with digits but contains other characters later can match with match() but not with fullmatch().






    
