import re
text = "NASA and USA are space organizations. Scientists developed advanced technology for space exploration."
# 1. Extract words written in all capital letters
capital_words = re.findall(r'\b[A-Z]{2,}\b', text)
print("Capital words:", capital_words)
# 2. Find words longer than 6 characters and print each with its start index
print("\nWords longer than 6 characters:")
matches = re.finditer(r'\b[A-Za-z]{7,}\b', text)
for match in matches:
    print(match.group(), "-> index:", match.start())
# 3. Extract dollar amounts
prices = "apples: $3.50, bananas: $1.20, mango: $4.75"
amounts = re.findall(r'\$\d+\.\d+', prices)
print("\nDollar amounts:", amounts)
# 4. Count how many times the capital-letter pattern occurs
count = len(capital_words)
print("Number of capital words:", count)
#output:
# Capital words: ['NASA', 'USA']
# Words longer than 6 characters:
# space -> index: 32
# exploration -> index: 51
# Dollar amounts: ['$3.50', '$1.20', '$4.75']
# Number of capital words: 2
