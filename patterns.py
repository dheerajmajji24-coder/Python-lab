#n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
#output:
*
* *
* * *
* * * *
* * * * *
#n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
output:
* * * * *
* * * *
* * *
* *
*    
#n = 5
for i in range(1, n + 1):
 for j in range(n - i):
 print(" ", end=" ")
 for j in range(2 * i - 1):
 print("*", end=" ")
print()
#output:
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
#n = 5
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()
#output:
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
#n = 4
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()
#output:
      *
    * * *
  * * * * *
* * * * * * *
  * * * * *
    * * *
      *
#n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()
#output:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
#n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
#output:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
#n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()
#output:
1
1 2 1
1 2 3 2 1
1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
#n = 5
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    print()
output:
A
A B
A B C
A B C D
A B C D E
#n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
#output:
* * * * *
*       *
*       *
*       *
* * * * *
#n = 4
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2:
            print("*", end=" ")
 else:
  print(" ", end=" ")
  print()
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end=" ")
    for j in range(2 * i - 1):
        if j == 0 or j == 2 * i - 2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
#output:
      *
    *   *
  *       *
*           *
  *       *
    *   *
      *
#n = 5
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
#output:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
#n = 4
for i in range(1, n + 1):
    print("*" * i, end="")
    print(" " * (2 * (n - i)), end="")
    print("*" * i)
for i in range(n, 0, -1):
    print("*" * i, end="")
    print(" " * (2 * (n - i)), end="")
    print("*" * i)
output:
*      *
**    **
***  ***
********
********
***  ***
**    **
*      *