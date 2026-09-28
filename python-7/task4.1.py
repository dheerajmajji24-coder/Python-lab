#lab 4:task 4.1


square = lambda x: x * x
is_even = lambda x: x % 2 == 0
larger = lambda a, b: a if a > b else b
print("Square:", square(5))
print("Is Even:", is_even(8))
print("Larger:", larger(10, 20))


#output:
#Square: 25
#Is Even: True
#Larger: 20
