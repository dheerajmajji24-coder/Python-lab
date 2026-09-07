sentence = input("Enter a sentence: ")
words = sentence.split()
print("Number of words:", len(words))
#output:
# Number of words: 5
sentence = input("Enter a sentence: ")
words = sentence.split()
longest = max(words, key=len)
print("Longest word:", longest)
#output:
# Longest word: Hello
sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_words = words[::-1]
print("Reversed sentence:", " ".join(reversed_words))
#output:
# Reversed sentence: World Hello
sentence = input("Enter a sentence: ")
words = sentence.split()
result = []
for word in words:
    result.append(word[0].upper() + word[1:].lower())
print("Title Case:", " ".join(result))
#output:
# Title Case: Hello World
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()
if sorted(str1) == sorted(str2):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")
#output:
# Strings are anagrams
