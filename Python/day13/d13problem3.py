# get name and mark
# Grade A > 90
# Grade B  -> 80 to 90
# Grade C -> 60 to 80
# Fail < 60

# get student detials
student = input("Enter Name and Mark (seperate by ,) : ").split(',')
# get student name from input
sname = student[0]
# gte student mark from input
smark = int(student[1])

# build function to fing a grade
def findMyGrade(name,mark):
    match mark:
        # mark > 90
        case 91|92|93|94|95|96|97|98|99|100:
            print(name,"you got grade 'A'")
        # mark 80-90
        case 81|82|83|84|85|86|87|88|89|90:
            print(name,"you got grade 'B'")
        # mark 60-80
        case 60|61|62|63|64|65|66|67|68|69|70|71|72|73|74|75|76|77|78|79|80:
            print(name,"you got grade 'C'")
        # mark < 60
        case _:
            print(name,"sorry your 'Fail'")

# call the findMyGrade() function
findMyGrade(sname.capitalize(),smark)