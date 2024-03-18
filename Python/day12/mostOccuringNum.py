# Problem #2
# Input is an integer list and another integer k. Output is the k most frequently occuring numbers.
# output can be in any order.
# eg input = [1,1,1,2,2,3,5,5,5,5], k =2
# output [1,5] (top 2 most frequently occuring numbers)
# input = [4,5,4,5,4,5,3,3,3,7,8,1,1,1], k = 4
# output [4,5,3,1]
# 
# Input is an integer list and another integer k. 
# Output is the k most frequently occuring numbers.
# output can be in any order.
# eg input = [1,1,1,2,2,3,5,5,5,5], k =2
# input_list = [1,1,2,2,4,4,4,5,6,6,6,7,8]
# 

# get lits from input
input_list = input("Enter list (seperate by ,) : ").split(',')
# get k value
k = int(input("Enter k value : "))
# assign empty list
count_list=[]
result_list=[]
unique_item_list=[]
# get uniqe in new list
for item in input_list:
    if item not in unique_item_list:
        # add item into unique_item_list
        unique_item_list.append(item)
# print(unique_item_list)
# count the numbers
for item in unique_item_list:
    # add count of item into count_list
    count_list.append(input_list.count(item))
# print(count_list)
# find result_list 
for j in range(k):
    # store the length of count_list in length
    length = len(count_list)
    # initialize index as 0
    index=0
    while length>index:
        # check max in templist
        if count_list[index]==max(count_list):
            # add max occurense of num into result _list
            result_list.append(unique_item_list[index])
            # remove the max occurence num in count_list
            count_list.remove(count_list[index])
            # remove the item unique_list 
            unique_item_list.remove(unique_item_list[index])
            # change the length
            length=len(count_list)
        # increment the index value
        index+=1
# print result_list
print(" ".join(str(num) for num in result_list[:k]))


# unique_item_list = list(set(input_list))

# for j in range(len(count_list)):
#     result_list.append(int(str(count_list[j])+str(unique_item_list[j])))
# print(result_list)
# result_list.sort(reverse=True)
# # print most frquently occuring numbers
# for i in range(k):
#     print(str(result_list[i])[-1],end=' ')