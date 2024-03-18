# Problem #1
# You have a list of numbers in ascending order, but with duplicates.
# Remove the duplicated, append _ at the end for each duplicate removed 
# eg input = [1,2,3,3,3,4,4,7,7,9]
# output = [1,2,3,4,7,9,_,_,_,_]
# 
# assign the list of values
# append _ for duplicate values
# 

# list 
list1 = [1,2,3,3,3,4,4,7,7,9]
# remove duplicate values an store in ascending order
list2 = list(set(list1))
# add '_' end of list2
for i in range(len(list2),len(list1)):
    list2.append('_')
# print list2
print(list2)