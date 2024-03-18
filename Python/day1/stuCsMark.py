# Problem #2
# you have a list of student names and another list with their marks in CS. 
# hard code the values. no need to get it as input
# Pass mark is 50.
# Print a new list with all the students with pass marks along with their mark in the format name:mark.
# Also print the number of students who failed.
# 
# assign 2 list are student name as (student_name_list) and student mark in computer science as (cs_mark_list)
# check mark is grater than 50 to pass
# then put the valuse in new list format 'name:mark'
# and check how may of student fail
# 

# student's name list
student_name_list = ['arun','ram','kumar','giri','raj']
# student's cs mark list
cs_mark_list = [60,40,82,67,90]
# student's pass list as pass_stu_list' 
pass_stu_list = []
# assign fail count as 'fail_count'
fail_count = 0
# check pass mark
for index in range(0,len(student_name_list)):
    # check pass mark
    if(cs_mark_list[index]>=50):
        # add pass student in 'pass_stu_list' with mark
        pass_stu_list.append(student_name_list[index]+":"+str(cs_mark_list[index]))
    else:
        # else add fail_count
        fail_count+=1
# print passed student's list and fail count
print(pass_stu_list)
print("Total no of fail is :",fail_count)
