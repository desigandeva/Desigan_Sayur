# Get users name and age as input.
# kindergarten (age 3-6)
# primary school (7-11)
# middle school (12-15)
# highschool (16-19)
# college (20-24)
# Eg input Sam, 10

# get student detials
student = input("Enter Name and Age (seperate by ,) : ").split(',')
# get student name from input
sname = student[0]
# gte student age from input
sage = int(student[1])

# build a function to find my Education industry
def findMyEdu(name,age):
    # age < 3 for baby
    if age<3:
        print(name,"your are baby")
    # age 3-6 for kindergarden
    elif age<7 and age>=3:
        print(name,"goes to kindergarden")
    # age 7-11 for primary school
    elif age<=11:
        print(name,"goes to primary school")
    # age 12-15 for middle school
    elif age<=15:
        print(name,"goes to middle school")
    # age 16-19 for high school
    elif age<=19:
        print(name,"goes to highschool")
    # age 20-24 for collage
    elif age<=24:
        print(name,"goes to college")
    # age > 24 
    else:
        print(name,"you are not student")

# call finfMyEdu() function
findMyEdu(sname,sage)