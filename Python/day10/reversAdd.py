# Problem #3 
# Add two number represented in a list as reversed. print the sum also as a list in reverse order
# eg input list1 = [1,2,3] list2 = [5,6,7]
# answer= [6,8,0,1]
#  explanation (321 + 765 = 1086)
# 
# Add two number represented in a list as reversed
# print the sum also as a list in reverse order
# 

# list1
list1 = [1,2,3]
# list2
list2 = [5,6,7]
# empty string
str1=''
str2=''
# revers the list1 and convet to string
for item in list1[::-1]:
    str1=str1+str(item)

for item in list2[::-1]:
    str2=str2+str(item)

# add str1 and str2
sum = int(str1)+int(str2)
# print the sum
print(sum)