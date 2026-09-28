#lab 3:task3.5

def gcd(a, b):
    if b == 0:
        return abs(a)
    return gcd(b, a % b)
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("GCD:", gcd(a, b))
print("LCM:", lcm(a, b))


#output:
#Enter first number: 9
#Enter second number: 3
#GCD: 3
#LCM: 9
