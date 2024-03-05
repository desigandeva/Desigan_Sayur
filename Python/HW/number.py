# problem 1
# find sum of 'N' numbers
# 
# get input fron user
N = int(input("Enter 'N' value : "))
# sumOfNumers() function is add the numbers
def sumOfNumbers(n):
    # value of n is 1 it's return 1
    if n==1:
        return n
    # otherwise it return n + callthesame function of n-1
    else:
        return (n+sumOfNumbers(n-1))
# print sum of n numbers
print("Sum of",N,"numbers is :",sumOfNumbers(N))
 
# problem 2
# find the sum of 'N' numbers divisible by 5
# 
# build a function for find sum of n numbers only divisible by 5
def sumOfDivBy5(n):
    # initialy sum is 0
    sum = 0
    for i in range(n+1):
        if i%5==0:
            # add number to sum only if number is divisible by 5
            sum += i
    # print the sum of number only divisible by 5
    print("Sum of",n,"numbers only divisible by 5 is :",sum)

# call the sumofdivby5()
sumOfDivBy5(N)

# problem 3
# find the sum of 'N' numbers divisible by 5
# 
def sumOfDivBy5And10(n):
    # init sum is 0
    sum = 0
    for i in range(n+1):
        if i%5==0 and i%10==0:
            # add number to sum if number is divisible by 5 and 10
            sum += i
    # print the sum
    print("Sum of",n,"numbers only divisible by 5 and 10 is :",sum)

# call sumofdivby5and10() function
sumOfDivBy5And10(N)



# problrm 4
# Find the smallest number in list
#
# take the list of values like 40,28,6,37,100,2,30
# take first no in list and compare other no in list
# and find the minimumm value
# 
# list of numbers is
l = [40,28,6,37,100,2,30]

def findMin(lst):
    # take 1st num as min
    min = lst[0]
    for i in range(len(lst)):
        # check smallest one
        if min > lst[i]:
            # change min value
            min = lst[i]
    # print minimum value
    print("The smallest number in the list is :",min)
# call the findMin() function 
findMin(l)

# problem 5
# find the 2nd smallest number in the above list
# 
# build the functin for find nth smallest num in list
def findNthMin(lst,n):
    # call the sortTheList() function to sort the list
    lst = sortThelist(lst)
    # print 2nd smallest number
    if n==2:
        print("The ",n,"nd smallest number is : ",lst[n-1],sep='')
    # print 1st smallest number
    elif n==1:
        print("The ",n,"st smallest number is : ",lst[n-1],sep='')
    # print 3rd smallest number
    elif n==3:
        print("The ",n,"rd smallest number is : ",lst[n-1],sep='')
    # print nth smallest number
    else:
        print("The ",n,'th smallest number is : ',lst[n-1],sep='')

# build the function to sort the list
def sortThelist(lst):
    for j in range(len(lst)):
        for i in range(len(lst)):
            if(i<len(lst)-1):
                # check the smallest number and swap them
                if lst[i]>lst[i+1]:
                    temp = lst[i]
                    lst[i] = lst[i+1]
                    lst[i+1] = temp
    # return the sorted list
    return lst
# call the findNthMin() functiom
findNthMin(l,2)