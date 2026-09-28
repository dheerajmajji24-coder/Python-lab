#lab1:task4

def stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)
    return minimum, maximum, average
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
minimum, maximum, average = stats(numbers)
print("Minimum =", minimum)
print("Maximum =", maximum)
print("Average =", average)


#output:
#Enter numbers separated by spaces: 2 3 9 7 5
#Minimum = 2
#Maximum = 9
#Average = 5.2
