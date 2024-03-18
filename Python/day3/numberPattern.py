# Problem 1
# Print the following pattern
#      1
#     1 1
#    1 2 1
#   1 3 3 1
#  1 4 6 4 1
# 
# Observe how the nunmbers in the triangle are calculated. 
# Do it in two steps. Work on the generating the numbers first in right angle triangle
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 
# And then work on the final output using proper indendation
# 
# the filnal output is calculated based on 11 to the power of 0 to num
# using join() it's used to add specified character in between the input
# 


# get the input from user to calculate the end result
num = int(input())

# for iterator in range(num):
#     corner_num = 1
#     print(" "*(num-iterator),end='')
#     for iterator2 in range(iterator+1):
#         print(corner_num,end=' ')
#         corner_num = corner_num*(iterator-iterator2)//(iterator2+1)
#     print()

# print the numbers in right angle triangle 
# for iterator in range(num):
#     print(" ".join(str(11**iterator)))

# print the numbers in primad shape
for iterator in range(num):
    print(" "*(num-iterator)," ".join(str(11**iterator)),sep='')
