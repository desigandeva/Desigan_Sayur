# assign the list of values
# append _ for duplicate values

# list 
list1 = [1,2,3,3,3,4,4,7,7,9]
# remove duplicate values
list2 = list(set(list1))
# change list to decending order
list2.sort(reverse=True)
# add '_' end of list2
for i in range(len(list2),len(list1)):
    list2.append('_')
# print list2
print(list2)