import re
sentence = "1024 requests were served in 3 seconds"
# 1. Check whether sentence starts with a digit
result = re.match(r"\d", sentence)
if result:
    print("Sentence starts with a digit")
else:
    print("Sentence does not start with a digit")
# 2. Find the word "served"
result = re.search(r"served", sentence)
if result:
    print("served found at:", result.span())
# 3. Check whether the whole string contains only digits
result1 = re.fullmatch(r"\d+", "12345")
print("12345:", bool(result1))
result2 = re.fullmatch(r"\d+", "123a5")
print("123a5:", bool(result2))


