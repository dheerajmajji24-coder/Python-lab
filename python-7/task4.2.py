#lab 4:task4.2


grade = lambda marks: "Pass" if marks >= 40 else "Fail"
marks_list = [35, 45, 67, 28, 90, 39]
for marks in marks_list:
    print(marks, ":", grade(marks))


#output:
#35 : Fail
#45 : Pass
#67 : Pass
#28 : Fail
#90 : Pass
#39 : Fail
