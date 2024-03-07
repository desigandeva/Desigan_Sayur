# Input is an integer list and another integer k. 
# Output is the k most frequently occuring numbers.
# output can be in any order.
# eg input = [1,1,1,2,2,3,5,5,5,5], k =2
# list1 = [1,1,2,2,4,4,4,5,6,6,6,7,8]

# get lits from input
list1 = input("Enter list (seperate by ,) : ").split(',')
# get k value
k = int(input("Enter k value : "))
# assign empty list
temp=[]
result=[]
new_list=[]
# get uniqe in new list
for i in list1:
    if i not in new_list:
        new_list.append(i)
# print(new_list)
# count the numbers
for i in new_list:
    temp.append(list1.count(i))
# print(temp)
# find result 
for j in range(k):
    length = len(temp)
    i=0
    while length>i:
        if temp[i]==max(temp):
            result.append(new_list[i])
            temp.remove(temp[i])
            new_list.remove(new_list[i])
            length=len(temp)
        i+=1
# print result
print(" ".join(i for i in result[:k]))









# new_list = list(set(list1))

# for j in range(len(temp)):
#     result.append(int(str(temp[j])+str(new_list[j])))
# print(result)
# result.sort(reverse=True)
# # print most frquently occuring numbers
# for i in range(k):
#     print(str(result[i])[-1],end=' ')