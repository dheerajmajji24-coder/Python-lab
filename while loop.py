#n = int(input("Enter N: "))
i = 1
while i <= n:
    print(i, end=" ")
    i += 1
 #output:Enter N: 5
1 2 3 4 5
#num = int(input("Enter a number: "))
sum_digits = 0
count = 0
while num > 0:
    digit = num % 10
    sum_digits += digit
    count += 1
    num //= 10
average = sum_digits / count
print("Sum of digits =", sum_digits)
print("Average of digits =", average)
#Enter a number: 1234
Sum of digits = 10
Average of digits = 2.5
#num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print("Reverse =", reverse)
#output:Enter a number: 1234
Reverse = 4321
#num = int(input("Enter a number: "))
original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
if original == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")
    #output:Enter a number: 121
Palindrome