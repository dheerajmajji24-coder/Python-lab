#lab4:task4.3


students = [("Ravi", 78), ("Sita", 92), ("Amit", 65)]
sorted_students = sorted(students, key=lambda s: s[1], reverse=True)
print("Students sorted by marks:")
for student in sorted_students:
    print(student)
names = ["Ravi", "Sita", "Amit", "Pooja", "Raj"]
sorted_names = sorted(names, key=lambda name: len(name))
print("\nNames sorted by length:")
for name in sorted_names:
    print(name)



#output:
#Students sorted by marks:
#('Sita', 92)
#('Ravi', 78)
#('Amit', 65)
#Names sorted by length:
#Raj
#Ravi
#Sita
#Amit
#Pooja
