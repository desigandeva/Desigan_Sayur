# Problem #3
# you have a list of student names. you have one list each for their marks in CS, Math and English. 
# hard code the values. no need to get it as input
# Pass mark is 50.
# Grade A is, mark 90 or above
# Grade B , 80 or above
# Fail is < 50
# Print the name of the students who got A in all subjects or atleast one A and the rest B.
# Try to use only one if statement.
# 
# assign student's name list as 'student_name_list'
# assign student's computer science mark list as 'cs_mark_list'
# assign student's math mark list as 'math_mark_list'
# assign student's english mark list as 'eng_mark_list'
# Pass mark is 50
# Grade A is 90 or above
# Grade B is 80 or above
# Fail is < 50
# 

# student's name list
student_name_list = ['ram','giri','naveen','raj','kavin']
# computer science mark list
cs_mark_list = [80,96,72,46,66]
# math mark list
math_mark_list = [98,95,69,92,60]
# english mark list
eng_mark_list = [85,92,78,55,81]

for index in range(0,len(student_name_list)):
    # check students who got A in all subjects or atleast one A and the rest B.
    if((cs_mark_list[index]>=90 and math_mark_list[index]>=90 and eng_mark_list[index]>=90)or
       (cs_mark_list[index]>=90 and math_mark_list[index]>=80 and eng_mark_list[index]>=80)or
       (cs_mark_list[index]>=80 and math_mark_list[index]>=90 and eng_mark_list[index]>=80)or
       (cs_mark_list[index]>=80 and math_mark_list[index]>=80 and eng_mark_list[index]>=90)):
        # print the student name who got 'A' in all subject or any one 'A' and rest 'B'
        print(student_name_list[index])
