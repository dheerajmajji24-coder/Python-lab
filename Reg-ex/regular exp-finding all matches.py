#week-6
#task-2

#1
import re
paragraph = """
NASA is working with the USA on a new space mission.
The ISRO team is developing advanced technology.
"""
# Extract words written entirely in capital letters
capital_words = re.findall(r'\b[A-Z]+\b', paragraph)
print("Capital words:", capital_words)

#output
#Capital words: ['NASA', 'USA', 'ISRO']



#2
import re
paragraph = """
NASA is working with the USA on a new space mission.
The ISRO team is developing advanced technology.
"""
for match in re.finditer(r'\b[A-Za-z]{7,}\b', paragraph):
    print(match.group(), "Start index:", match.start())

#output
#working Start index: 9
#mission Start index: 45
#developing Start index: 71
#advanced Start index: 82
#technology Start index: 91



#3
import re
prices = "apples: $3.50, bananas: $1.20, mango: $4.75"
dollar_amounts = re.findall(r'\$\d+\.\d+', prices)
print(dollar_amounts)

#output
#['$3.50', '$1.20', '$4.75']




#4
import re
paragraph = """
NASA is working with the USA on a new space mission.
The ISRO team is developing advanced technology.
"""
capital_words = re.findall(r'\b[A-Z]+\b', paragraph)
count = len(capital_words)
print("Number of capital words:", count)

#output
#Number of capital words: 3
    
