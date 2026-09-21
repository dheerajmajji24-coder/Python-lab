#week-6
#task-3

#1
import re
def redact_emails(text):
    return re.sub(r'\b[\w.-]+@[\w.-]+\.\w+\b', '[EMAIL HIDDEN]', text)
text = "Contact john@example.com or mary@gmail.com for more information."
result = redact_emails(text)
print(result)
#output
#Contact [EMAIL HIDDEN] or [EMAIL HIDDEN] for more information



#2
import re
name = "Doe, John"
result = re.sub(r'(\w+),\s*(\w+)', r'\2 \1', name)
print(result)
#output
#John Doe



#3
import re
def double_number(match):
    number = int(match.group())
    return str(number * 2)
sentence = "I have 3 apples and 5 oranges."
result = re.sub(r'\d+', double_number, sentence)
print(result)
#output
#I have 6 apples and 10 oranges



#4
import re
text = "Wait!!! What??? Really!!!"
result, count = re.subn(r'([!?])\1+', r'\1', text)
print("Result:", result)
print("Number of replacements:", count)
#output
#Result: Wait! What? Really!
#Number of replacements: 3





