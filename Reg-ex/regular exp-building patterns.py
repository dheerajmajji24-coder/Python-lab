#week-6
#task-4

#1
import re
pattern = r'^[A-Za-z_][A-Za-z0-9_]*$'
variables = ["_count2", "2fast", "total_sum"]
for variable in variables:
    if re.fullmatch(pattern, variable):
        print(variable, "-> Valid")
    else:
        print(variable, "-> Invalid")

#output
#_count2 -> Valid
#2fast -> Invalid
#total_sum -> Valid





#2
import re
pattern = r'\b(cat|dog|bird)\b'
sentence = "I have a cat, a dog, and a bird. My cat likes the dog."
pets = re.findall(pattern, sentence)
print(pets)

#output
#['cat', 'dog', 'bird', 'cat', 'dog']



#3
import re
pattern = r'^#(?:[0-9A-Fa-f]{3}|[0-9A-Fa-f]{6})$'
colors = ["#FFAA00", "#000", "#12G", "#12345"]
for color in colors:
    if re.fullmatch(pattern, color):
        print(color, "-> Valid")
    else:
        print(color, "-> Invalid")

#output
#FFAA00 -> Valid
#000 -> Valid
#12G -> Invalid
#12345 -> Invalid





#4
import re
pattern = (
    r'(?P<date>\d{4}-\d{2}-\d{2}) '
    r'(?P<time>\d{2}:\d{2}:\d{2}) '
    r'(?P<level>\w+) '
    r'(?P<message>.*)'
)
log = "2024-06-01 08:15:32 ERROR Disk full"
match = re.match(pattern, log)
if match:
    print("Date:", match.group("date"))
    print("Time:", match.group("time"))
    print("Level:", match.group("level"))
    print("Message:", match.group("message"))
       
#output
#Date: 2024-06-01
#Time: 08:15:32
#Level: ERROR
#Message: Disk full


