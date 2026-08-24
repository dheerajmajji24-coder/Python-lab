#num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)
 #output:Enter a number: 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
#num = int(input("Enter a number: "))
factorial = 1
for i in range(1, num + 1):
    factorial = factorial * i
print("Factorial =", factorial)
#output:Enter a number: 5
Factorial = 120
#text = input("Enter a string: ")
vowels = 0
consonants = 0
digits = 0
spaces = 0
for ch in text:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
print("Vowels =", vowels)
print("Consonants =", consonants)
print("Digits =", digits)
print("Spaces =", spaces)
#output:Enter a string: Hello World 123
Vowels = 3
Consonants = 7
Digits = 3
Spaces = 2
#n = int(input("Enter a number: "))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
if n > 1 and count == 2:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
#output:Enter a number: 7
7 is a prime number
#lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))
print("Prime numbers are:")
for num in range(lower, upper + 1):
    if num > 1:
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count == 2:
            print(num, end=" ")
#output:Enter lower limit: 10
Enter upper limit: 30
Prime numbers are:
11 13 17 19 23 29