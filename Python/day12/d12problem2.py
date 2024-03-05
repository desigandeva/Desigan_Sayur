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
a=[]
b=[]
# get uniqe in new list
new_list = list(set(list1))
# count the numbers
for i in new_list:
    a.append(list1.count(i))

for j in range(len(a)):
    b.append(int(str(a[j])+str(new_list[j])))

b.sort(reverse=True)
# print most frquently occuring numbers
for i in range(k):
    print(str(b[i])[-1],end=' ')