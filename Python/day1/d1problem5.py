# assume 3 department as dep1, dep2 and dep3 (3 list)
# get dep1 students mark
# similar for dep2 and dep3
# find top 3 marks in each department
# and overall top 3 marks
# find average mark with passing mark (assume: pass mark as 50) in each department and overall
# find which department get best average mark and least fail


# department 1 list
dep1 = list(map(int,input("Enter the department 1 mark (seperate by ,) ").split(','))) 
# department 2 list
dep2 = list(map(int,input("Enter the department 2 mark (seperate by ,) ").split(',')))
# department 3 list
dep3 = list(map(int,input("Enter the department 3 mark (seperate by ,) ").split(',')))
# dep1=[20,46,79,31,8]
# dep2=[64,87,20,97,67]
# dep3=[54,97,67,81,81]
# assign empty list as 'alldep' for store all students mark 
alldep = []

# function for add all department students mark in single list
def addtolist(dept):
    for i in range(0,len(dept)):
        alldep.append(dept[i])

# function for find top 3 marks in 
def findtop3(dept,department):
    dept.sort(reverse=True)
    print("Top 3 marks in",department,"is :")
    for i in range(0,3):
        print(dept[i])

# function for find average mark with pass mark
def avgmark(dept):
    sum=0
    pcount=0
    for i in range(0,len(dept)):
        if(dept[i]>=50):
            sum=sum+dept[i]
            pcount+=1
    # print(sum,pcount)
    return(sum/pcount)

# print top 3 marks in department 1
findtop3(dep1,"Department 1")
# print top 3 marks in department 2
findtop3(dep2,"Department 2")
# print top 3 marks in department 3
findtop3(dep3,"Department 3")

addtolist(dep1)
addtolist(dep2)
addtolist(dep3)
# print top 3 marks in over all department
findtop3(alldep,"Over all")

# print average mark with pass mark for dep1
print("Average of dep1 :",int(avgmark(dep1)))
# print average mark with pass mark for dep2
print("Average of dep2 :",int(avgmark(dep2)))
# print average mark with pass mark for dep3
print("Average of dep3 :",int(avgmark(dep3)))
# print average mark with pass mark for overall
print("Average of overall :",int(avgmark(alldep)))

if(avgmark(dep1)>avgmark(dep2) and avgmark(dep1)>avgmark(dep3)):
    print("Department 1 is the best average")
elif(avgmark(dep2)>avgmark(dep1) and avgmark(dep2)>avgmark(dep3)):
    print("Department 2 is the best average")
else:
    print("Department 3 is the best average")