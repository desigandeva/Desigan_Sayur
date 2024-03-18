# Problem #2
# Use switch stmt, think of all possible age as input.
# Print if the user goes to kindergarten (age 3-6), primary school (7-11), ,middle school (12-15),
# highschool (16-19), college (20-24).
# Get users name and age as input.
# Eg input Sam, 10
# Output is Sam goes to primary school
# 
# Get users name and age as input.
# kindergarten (age 3-6)
# primary school (7-11)
# middle school (12-15)
# highschool (16-19)
# college (20-24)
# Eg input Sam, 10
# 

# get student detials
student_detial_list = input("Enter Name and Age (seperate by ,) : ").split(',')
# get student name from input
student_name = student_detial_list[0]
# gte student age from input
student_age = int(student_detial_list[1])

# build a function to find my Education industry
def findMyEdu(name,age):
    match age:
        # age < 3 for baby
        # if age<3:
        case 1|2:
            print(name,"your are baby")
        # age 3-6 for kindergarden
        # elif age<7 and age>=3:
        case 3|4|5|6:
            print(name,"goes to kindergarden")
        # age 7-11 for primary school
        # elif age<=11:
        case 7|8|9|10|11:
            print(name,"goes to primary school")
        # age 12-15 for middle school
        # elif age<=15:
        case 12|13|14|15:
            print(name,"goes to middle school")
        # age 16-19 for high school
        # elif age<=19:
        case 16|17|18|19:
            print(name,"goes to highschool")
        # age 20-24 for collage
        # elif age<=24:
        case 20|21|22|23|24:
            print(name,"goes to college")
        # age > 24 
        # else:
        case _:
            print(name,"you are not student")

# call finfMyEdu() function
findMyEdu(student_name,student_age)