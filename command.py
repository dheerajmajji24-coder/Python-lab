

import sys

name = sys.argv[1]
print("Hello,", name + "!")


import sys
if len(sys.argv) != 3:
    print("Usage: python sum.py <num1> <num2>")
else:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    print("Sum =", num1 + num2)

    

import sys

print("Script name:", sys.argv[0])
print("Total arguments passed:", len(sys.argv) - 1)
