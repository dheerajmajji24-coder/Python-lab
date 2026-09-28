#lab2:task2.4

def build_profile(**details):
    print("----- PROFILE CARD -----")
    for key, value in details.items():
        print(key.title(), ":", value)
    print("------------------------")
build_profile(name="Asha", age=20, city="Hyderabad", hobby="Reading")
print()
build_profile(name="Ravi", branch="CSE", college="GMRIT")
print()
build_profile(name="Priya", age=21, hobby="Painting")


#output:
#----- PROFILE CARD -----
#Name : Asha
#Age : 20
#City : Hyderabad
#Hobby : Reading
#------------------------
#----- PROFILE CARD -----
#Name : Ravi
#Branch : CSE
#College : GMRIT
#------------------------
#----- PROFILE CARD -----
#Name : Priya
#Age : 21
#Hobby : Painting
#------------------------
