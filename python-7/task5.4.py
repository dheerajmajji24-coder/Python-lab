#lab5:task5.4


def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
counter = make_counter()
print(counter())
print(counter())
print(counter())
print(counter())
print(counter())


#output:
#1
#2
#3
#4
#5
