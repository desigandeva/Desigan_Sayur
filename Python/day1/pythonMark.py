# problem #5
# In your college Python is taught in 3 different departments by the same professor. 
# For each dept, get the no of students studying Python and their marks in the final exam 
# Get the input as comma seperated string
# 
# Find the top 3 marks in each class
# Find the top 3 marks in all classes are combined.
# Find the avg mark of students with passing mark in each class and the classes combined.
# Find which class has the best average mark and least number of failed students.
# 
# assume 3 department as dep1_list, dep2_list and dep3_list (3 list)
# get dep1_list students mark
# similar for dep2_list and dep3_list
# find top 3 marks in each department
# and overall top 3 marks
# find average mark with passing mark (assume: pass mark as 50) in each department and overall
# find which department get best average mark and least fail
# 

# department 1 list
# dep1_list = list(map(int,input("Enter the department 1 mark (seperate by ,) ").split(','))) 
# department 2 list
# dep2_list = list(map(int,input("Enter the department 2 mark (seperate by ,) ").split(',')))
# department 3 list
# dep3_list = list(map(int,input("Enter the department 3 mark (seperate by ,) ").split(',')))
dep1_list=[20,46,79,31,8]
dep2_list=[64,87,20,97,67]
dep3_list=[54,97,67,81,81]
# assign empty list as 'all_dep_list' for store all students mark 
all_dep_list = []

# function for add all department students mark in single list
def addtolist(dept):
    for mark in dept:
        # add dep mark to all_dep_list
        all_dep_list.append(mark)

# function for find top 3 marks in 
def findtop3(dept,department):
    # sort the mark in descending order
    dept.sort(reverse=True)
    print("Top 3 marks in",department,"is :")
    # print the  mark
    for index in range(0,3):
        print(dept[index])

# function for find average mark with pass mark
def avgmark(dept):
    # initialze the sum as 0
    sum=0
    # initialze the pass_count as 0
    pass_count=0
    for index in range(0,len(dept)):
        # check mark > 50
        if(dept[index]>=50):
            # add mark's to sum
            sum=sum+dept[index]
            # increase the pass_count
            pass_count+=1
    # print(sum,pass_count)
    return(sum/pass_count)

# build a function for find the fail count
def failCount(dept):
    # initialze fail_count as 0
    fail_count = 0
    for mark in dept:
        # check the mark's are < 50
        if mark < 50:
            # add fail_count
            fail_count+=1
    # return fail_count
    return fail_count

# print top 3 marks in department 1
findtop3(dep1_list,"Department 1")
# dep1_list.sort(reverse=True)
# print(dep1_list[:3])
# print top 3 marks in department 2
findtop3(dep2_list,"Department 2")
# dep2_list.sort(reverse=True)
# print(dep2_list[:3])
# print top 3 marks in department 3
findtop3(dep3_list,"Department 3")
# dep3_list.sort(reverse=True)
# print(dep3_list[:3])
# add dep1_list,dep2_list,dep3_list into overall
addtolist(dep1_list)
addtolist(dep2_list)
addtolist(dep3_list)
# print top 3 marks in over all department
findtop3(all_dep_list,"Over all")
# all_dep_list.sort(reverse=True)
# print(all_dep_list[:3])

# print average mark with pass mark for dep1_list
print("Average of dep1 :",int(avgmark(dep1_list)))
# print average mark with pass mark for dep2_list
print("Average of dep2 :",int(avgmark(dep2_list)))
# print average mark with pass mark for dep3_list
print("Average of dep3 :",int(avgmark(dep3_list)))
# print average mark with pass mark for overall
print("Average of overall :",int(avgmark(all_dep_list)))

# find best average
if(avgmark(dep1_list)>avgmark(dep2_list) and avgmark(dep1_list)>avgmark(dep3_list)):
    print("Department 1 is the best average")
elif(avgmark(dep2_list)>avgmark(dep1_list) and avgmark(dep2_list)>avgmark(dep3_list)):
    print("Department 2 is the best average")
else:
    print("Department 3 is the best average")

# find least failCount
if (failCount(dep1_list)<failCount(dep2_list) and failCount(dep1_list)<failCount(dep3_list)):
    print("Department 1 is the least fail count")
elif(failCount(dep2_list)<failCount(dep1_list) and failCount(dep2_list)<failCount(dep3_list)):
    print("Department 2 is the least fail count")
else:
    print("Department 3 is the least fail count")
