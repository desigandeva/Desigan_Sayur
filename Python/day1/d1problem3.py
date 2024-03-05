# assign student's name list as 'sname'
# assign student's computer science mark list as 'cs_mark'
# assign student's math mark list as 'math_mark'
# assign student's english mark list as 'e_mark'
# Pass mark is 50
# Grade A is 90 or above
# Grade B is 80 or above
# Fail is < 50


# student's name list
sname = ['ram','giri','naveen','raj','kavin']
# computer science mark list
cs_mark = [80,96,72,46,66]
# math mark list
math_mark = [98,95,69,92,60]
# english mark list
e_mark = [85,92,78,55,81]

for i in range(0,len(sname)):
    if((cs_mark[i]>=90 and math_mark[i]>=90 and e_mark[i]>=90)or
       (cs_mark[i]>=90 and math_mark[i]>=80 and e_mark[i]>=80)or
       (cs_mark[i]>=80 and math_mark[i]>=90 and e_mark[i]>=80)or
       (cs_mark[i]>=80 and math_mark[i]>=80 and e_mark[i]>=90)):
        # print the student name who got 'A' in all subject or any one 'A' and rest 'B'
        print(sname[i])
