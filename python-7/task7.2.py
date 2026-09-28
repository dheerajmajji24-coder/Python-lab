#lab 7:task7.2

# Task 2: Basic Logging Decorator
def log_call(func):
    def wrapper(*args, **kwargs):
        print("Calling:", func.__name__)
        print("Arguments:", args, kwargs)
        result = func(*args, **kwargs)
        print("Returned:", result)
        return result
    return wrapper

@log_call
def add(a, b):
    return a + b
result = add(10, 20)
print("Result:", result)


#output:
#Calling: add
#Arguments: (10, 20) {}
#Returned: 30
#Result: 30

