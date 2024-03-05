# assign 2 list are student name as (sname) and student mark in computer science as (cs_mark)
# check mark is grater than 50 to pass
# then put the valuse in new list format 'name:mark'
# and check how may of student fail

# student's name list
sname = ['arun','ram','kumar','giri','raj']
# student's cs mark list
cs_mark = [60,40,82,67,90]
# student's pass list as plist' 
plist = []
# assign fail count as 'fcount'
fcount = 0
# check pass mark
for i in range(0,len(sname)):
    if(cs_mark[i]>=50):
        plist.append(sname[i]+":"+str(cs_mark[i]))
    else:
        fcount+=1
# print passed student's list and fail count
print(plist)
print("Total no of fail is :",fcount)
