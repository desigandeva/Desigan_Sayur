# the filnal output is calculated based on 11 to the power of 0 to n
# using join() it's used to add specified character in between the input

# get the input from user to calculate the end result
n = int(input())

# print the numbers in right angle triangle 
# for i in range(n):
#     print(" ".join(str(11**i)))

# print the numbers in primad shape
for i in range(n):
    print(" "*(n-i)," ".join(str(11**i)),sep='')
